"""Batch-run standard-mode assessment across a product list.

Mode:
  --mode standard → runs the shared skill's prompt
                    (.claude/skills/provider-assessment/prompts/standard_mode.md)
                    against the domain's vendor CSV.

For each product:
  1. Render the mode-specific prompt template with {VENDOR}, {PRODUCT_NAME},
     {product_id}.
  2. Spawn a FRESH `claude -p` session (no --continue / --resume) with the
     project's .claude/skills/deep-research auto-loaded (cwd = repo root).
  3. Stream the full trace into runs/<pid>/claude_run.jsonl.
  4. Run validate_assessment.py against the produced assessment.json and
     record the outcome in runs/<pid>/claude_run.meta.json.

--skip-done skips a product only when its existing assessment.json is in the
SAME mode as the current run (so a partial pass doesn't block a re-run).

--concurrency N runs up to N products in parallel (ThreadPoolExecutor). Any
concurrency > 1 forces quiet=True for every product regardless of --quiet, so
the --overwrite line-window (which redraws via ANSI cursor moves) is never
driven by more than one thread at a time — at concurrency=1 (the default)
--overwrite behaves exactly as before.

Requires:  claude CLI on PATH, venv Python for the validator.
Docs cross-checked: https://code.claude.com/docs/en/headless.md
"""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import json
import os
import queue
import re
import shutil
import subprocess
import sys
import threading
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Domain-specific config. Each domain is a self-contained sibling of
# microsegmentation/ with its own checklist, prompts, runs/, and scripts/.
DOMAINS = {
    "microsegmentation": {
        "csv": REPO_ROOT / "providers" / "Microsegmentation.csv",
        "dir": REPO_ROOT / "microsegmentation",
    },
    "bsg": {
        "csv": REPO_ROOT / "providers" / "BSG.csv",
        "dir": REPO_ROOT / "bsg",
    },
}

# Module-level defaults (microsegmentation) — reassigned in main() when
# --domain selects a different one. Kept as constants so existing call sites
# (load_prompt_template, already_done_for_mode, run_validator, run_one,
# BATCH_DIR) don't need a domain parameter threaded through every call.
CSV_PATH = DOMAINS["microsegmentation"]["csv"]
PROMPTS_DIR = REPO_ROOT / ".claude" / "skills" / "provider-assessment" / "prompts"
PROMPT_FILES = {
    "standard": PROMPTS_DIR / "standard_mode.md",
}
RUNS_ROOT = DOMAINS["microsegmentation"]["dir"] / "runs"
VALIDATOR = REPO_ROOT / ".claude" / "skills" / "provider-assessment" / "scripts" / "validate_assessment.py"
CURRENT_DOMAIN = "microsegmentation"
VENV_PY = REPO_ROOT / "venv" / "Scripts" / "python.exe"
BATCH_DIR = RUNS_ROOT / "_batch"


def select_domain(domain: str) -> None:
    """Reassign the module-level path constants for the chosen domain."""
    global CSV_PATH, PROMPTS_DIR, PROMPT_FILES, RUNS_ROOT, VALIDATOR, CURRENT_DOMAIN, BATCH_DIR
    cfg = DOMAINS[domain]
    CSV_PATH = cfg["csv"]
    PROMPTS_DIR = REPO_ROOT / ".claude" / "skills" / "provider-assessment" / "prompts"
    PROMPT_FILES = {
        "standard": PROMPTS_DIR / "standard_mode.md",
    }
    RUNS_ROOT = cfg["dir"] / "runs"
    VALIDATOR = REPO_ROOT / ".claude" / "skills" / "provider-assessment" / "scripts" / "validate_assessment.py"
    CURRENT_DOMAIN = domain
    BATCH_DIR = RUNS_ROOT / "_batch"

# Pre-approve the tools the standard-mode prompt actually needs. Combined with
# --permission-mode acceptEdits this covers file R/W without blanket approval.
ALLOWED_TOOLS = "Bash,Read,Edit,Write,Grep,Glob,WebFetch,WebSearch,Skill,TodoWrite"


def load_prompt_template(mode: str) -> str:
    prompt_file = PROMPT_FILES[mode]
    if not prompt_file.exists():
        raise SystemExit(f"prompt file for mode={mode!r} not found: {prompt_file}")
    text = prompt_file.read_text(encoding="utf-8")
    m = re.search(r"```\r?\n(.*?)\r?\n```", text, re.DOTALL)
    if not m:
        raise SystemExit(f"could not find fenced code block in {prompt_file}")
    return m.group(1)


def load_queue_file(path: Path) -> list[str]:
    pids: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if line:
            pids.append(line)
    return pids


def already_done_for_mode(pid: str, mode: str) -> bool:
    """True iff runs/<pid>/assessment.json exists AND was produced in the same mode."""
    p = RUNS_ROOT / pid / "assessment.json"
    if not p.exists():
        return False
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    return data.get("assessment_mode") == mode


def load_products(csv_path: Path) -> list[dict]:
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    header_idx = next(
        (i for i, r in enumerate(rows) if r and r[0].strip() == "STT"),
        None,
    )
    if header_idx is None:
        raise SystemExit(f"no header row (STT,...) found in {csv_path}")
    header = [h.strip() for h in rows[header_idx]]
    out: list[dict] = []
    for row in rows[header_idx + 1:]:
        if not row or not row[0].strip():
            continue
        rec = dict(zip(header, row))
        pid = (rec.get("product_id") or "").strip()
        if not pid:
            continue
        out.append({
            "stt": rec.get("STT", "").strip(),
            "vendor": (rec.get("Company") or "").strip(),
            "product_name": (rec.get("Product") or rec.get("Product Name") or "").strip(),
            "product_id": pid,
        })
    return out


def filter_products(products, only, start_at, limit, queue_pids):
    if queue_pids is not None:
        pid_map = {p["product_id"]: p for p in products}
        missing = [q for q in queue_pids if q not in pid_map]
        if missing:
            print(f"WARN queue-file has {len(missing)} pid(s) not in CSV: {missing[:5]}"
                  f"{'…' if len(missing) > 5 else ''}", file=sys.stderr)
        products = [pid_map[q] for q in queue_pids if q in pid_map]
    if only:
        products = [p for p in products if p["product_id"] == only]
        if not products:
            raise SystemExit(f"--only {only} not found")
    if start_at:
        idx = next((i for i, p in enumerate(products) if p["product_id"] == start_at), None)
        if idx is None:
            raise SystemExit(f"--start-at {start_at} not found")
        products = products[idx:]
    if limit:
        products = products[:limit]
    return products


def render_prompt(template: str, product: dict) -> str:
    return (template
            .replace("{DOMAIN}", CURRENT_DOMAIN)
            .replace("{VENDOR}", product["vendor"])
            .replace("{PRODUCT_NAME}", product["product_name"])
            .replace("{product_id}", product["product_id"]))


def parse_stream_result(log_path: Path) -> dict | None:
    """Scan stream-json log for the final `type: "result"` event; return it whole.

    Schema (SDKResultMessage — https://code.claude.com/docs/en/agent-sdk/typescript.md):
      subtype, is_error, duration_ms, duration_api_ms, num_turns, total_cost_usd,
      usage.{input_tokens, output_tokens, cache_creation_input_tokens,
      cache_read_input_tokens}, permission_denials, result, session_id.
    """
    if not log_path.exists():
        return None
    result_event = None
    try:
        with log_path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    ev = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(ev, dict) and ev.get("type") == "result":
                    result_event = ev
    except Exception:  # noqa: BLE001
        pass
    return result_event


def _safe_console(s: str) -> str:
    """Sanitize for print() on a non-UTF-8 console (default cp1252 on Windows).

    Progress lines echo arbitrary file/web content (tool_result text, model
    text output) which routinely contains characters cp1252 can't encode
    (Vietnamese diacritics, em-dashes, curly quotes) -- confirmed by testing
    summarize_event() against a real claude_run.jsonl, which raised
    UnicodeEncodeError on a plain print(). Replacing unencodable characters
    here means a batch run degrades to '?' placeholders instead of crashing
    mid-run on whichever product happens to cite non-ASCII text first.
    """
    enc = sys.stdout.encoding or "utf-8"
    return s.encode(enc, errors="replace").decode(enc, errors="replace")


def _truncate(s: str, n: int = 100) -> str:
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "…"


def _enable_windows_ansi() -> None:
    """Best-effort: turn on ANSI escape processing in the classic Windows console.

    Windows Terminal / PowerShell 7 already do this; PowerShell 5.1's conhost
    needs ENABLE_VIRTUAL_TERMINAL_PROCESSING (0x0004) set explicitly or the
    cursor-up/clear-line codes used by _LineWindow print as literal garbage.
    """
    if os.name != "nt":
        return
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_uint32()
        kernel32.GetConsoleMode(handle, ctypes.byref(mode))
        kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    except Exception:  # noqa: BLE001
        pass


class _LineWindow:
    """Redraws the last N progress lines in place instead of scrolling.

    Each push() moves the cursor back up over the previously drawn block and
    rewrites it, so at most N lines of live status are ever on screen. The
    full stream-json trace is unaffected — it's written to the log file
    separately, before this is ever called.
    """

    def __init__(self, size: int):
        self.lines: deque[str] = deque(maxlen=max(1, size))
        self.printed = 0

    def push(self, text: str) -> None:
        width = shutil.get_terminal_size((100, 20)).columns - 1
        self.lines.append(text[:width])
        chunks = []
        if self.printed:
            chunks.append(f"\x1b[{self.printed}A")
        for line in self.lines:
            chunks.append("\x1b[2K" + line + "\n")
        sys.stdout.write("".join(chunks))
        sys.stdout.flush()
        self.printed = len(self.lines)


def _brief_tool_input(name: str, inp: dict) -> str:
    if name == "Bash":
        return _truncate(inp.get("command", ""), 90)
    if name in ("Read", "Edit", "Write"):
        return inp.get("file_path", "")
    if name in ("Grep", "Glob"):
        return _truncate(inp.get("pattern", ""), 60)
    if name == "WebFetch":
        return inp.get("url", "")
    if name == "WebSearch":
        return _truncate(inp.get("query", ""), 60)
    if name == "Skill":
        return inp.get("skill", "") or inp.get("command", "")
    keys = ", ".join(list(inp.keys())[:3])
    return f"{{{keys}}}" if keys else ""


def summarize_event(ev: dict) -> str | None:
    """One-line progress summary for a stream-json event, or None to skip it.

    Schema per https://code.claude.com/docs/en/headless.md stream-json output:
    type in {system, assistant, user, result}; assistant/user carry a
    message.content list of blocks (text | tool_use | tool_result).
    """
    etype = ev.get("type")
    if etype == "system" and ev.get("subtype") == "init":
        tools = ev.get("tools") or []
        return f"session init  model={ev.get('model', '?')}  tools={len(tools)}"
    if etype == "assistant":
        for block in (ev.get("message") or {}).get("content") or []:
            btype = block.get("type")
            if btype == "tool_use":
                name = block.get("name", "?")
                brief = _brief_tool_input(name, block.get("input") or {})
                return f"tool_use  {name}({brief})" if brief else f"tool_use  {name}"
            if btype == "text":
                text = _truncate(block.get("text", ""))
                if text:
                    return f"text      {text}"
        return None
    if etype == "user":
        for block in (ev.get("message") or {}).get("content") or []:
            if block.get("type") == "tool_result":
                content = block.get("content")
                text = ""
                if isinstance(content, list):
                    text = " ".join(
                        c.get("text", "") for c in content
                        if isinstance(c, dict) and c.get("type") == "text"
                    )
                elif isinstance(content, str):
                    text = content
                tag = "ERROR" if block.get("is_error") else "ok"
                return f"tool_result[{tag}]  {_truncate(text)}"
        return None
    return None


def run_validator(pid: str) -> dict | None:
    assessment = RUNS_ROOT / pid / "assessment.json"
    if not assessment.exists():
        return {"exit_code": None, "note": "assessment.json missing"}
    py = str(VENV_PY) if VENV_PY.exists() else sys.executable
    proc = subprocess.run(
        [py, str(VALIDATOR), "--domain", CURRENT_DOMAIN, str(assessment),
         "--evidence-store", str(RUNS_ROOT / pid)],
        capture_output=True, text=True,
    )
    return {
        "exit_code": proc.returncode,
        "stdout_tail": proc.stdout.strip().splitlines()[-5:] if proc.stdout else [],
        "stderr_tail": proc.stderr.strip().splitlines()[-5:] if proc.stderr else [],
    }


def run_one(product, prompt_text, model, timeout, dry_run, max_turns=None, max_budget_usd=None,
            skip_permissions=False, quiet=False, overwrite: int | None = None) -> dict:
    pid = product["product_id"]
    run_dir = RUNS_ROOT / pid

    claude_bin = shutil.which("claude")
    if not claude_bin:
        raise SystemExit("`claude` CLI not on PATH")

    cmd = [
        claude_bin, "-p",
        "--output-format", "stream-json",
        "--verbose",  # required for stream-json in -p mode
    ]
    if skip_permissions:
        # No prompts for ANY tool call, in or out of the project tree — the
        # scoped acceptEdits + allowedTools combo below is the safe default;
        # this is opt-in per invocation via --dangerously-skip-permissions.
        cmd.append("--dangerously-skip-permissions")
    else:
        cmd.extend(["--permission-mode", "acceptEdits", "--allowedTools", ALLOWED_TOOLS])
    if model:
        cmd.extend(["--model", model])
    if max_turns is not None:
        cmd.extend(["--max-turns", str(max_turns)])
    if max_budget_usd is not None:
        cmd.extend(["--max-budget-usd", str(max_budget_usd)])
    cmd.append(prompt_text)

    started_iso = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    budget_str = f"${max_budget_usd}" if max_budget_usd is not None else "none"
    perm_str = "DANGEROUSLY-SKIP-PERMISSIONS" if skip_permissions else "acceptEdits+allowlist"
    print(f"[{pid}] start {started_iso}  prompt={len(prompt_text)}B  model={model or 'default'}  "
          f"max_turns={max_turns or 'none'}  max_budget={budget_str}  perm={perm_str}")

    if dry_run:
        return {
            "product_id": pid, "vendor": product["vendor"],
            "started_at": started_iso, "elapsed_seconds": 0,
            "exit_code": 0, "status": "dry-run",
            "total_cost_usd": None, "validator": None,
        }

    # Only create the run directory + write prompt for real runs, so a dry-run
    # doesn't pollute runs/ with empty per-product dirs.
    run_dir.mkdir(parents=True, exist_ok=True)
    prompt_path = run_dir / "prompt.txt"
    log_path = run_dir / "claude_run.jsonl"
    meta_path = run_dir / "claude_run.meta.json"
    prompt_path.write_text(prompt_text, encoding="utf-8")

    t0 = time.time()
    exit_code: int | None = None
    status: str | None = None
    try:
        proc = subprocess.Popen(
            cmd, cwd=str(REPO_ROOT),
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, bufsize=1,
            encoding="utf-8", errors="replace",
        )
        # Pump the pipe on a background thread (not select()) so this works
        # identically on Windows and POSIX, and so the main loop can still
        # enforce --timeout even while readline() is blocked waiting on the
        # next stream-json line.
        line_q: queue.Queue[str | None] = queue.Queue()

        def _pump() -> None:
            assert proc.stdout is not None
            for line in iter(proc.stdout.readline, ""):
                line_q.put(line)
            line_q.put(None)

        threading.Thread(target=_pump, daemon=True).start()

        win = _LineWindow(overwrite) if overwrite else None
        with log_path.open("w", encoding="utf-8") as logf:
            while status is None:
                if timeout is not None and (time.time() - t0) > timeout:
                    proc.kill()
                    proc.wait()
                    exit_code, status = -1, "timeout"
                    break
                try:
                    line = line_q.get(timeout=1.0)
                except queue.Empty:
                    continue
                if line is None:
                    exit_code = proc.wait()
                    status = "ok" if exit_code == 0 else f"exit-{exit_code}"
                    break
                logf.write(line)
                logf.flush()
                if not quiet:
                    try:
                        ev = json.loads(line)
                    except json.JSONDecodeError:
                        ev = None
                    summary_line = summarize_event(ev) if isinstance(ev, dict) else None
                    if summary_line:
                        line_out = _safe_console(f"  [{pid}] t+{time.time() - t0:6.1f}s  {summary_line}")
                        if win is not None:
                            win.push(line_out)
                        else:
                            print(line_out, flush=True)
    except Exception as e:  # noqa: BLE001
        exit_code, status = -1, f"error: {e}"
    elapsed = round(time.time() - t0, 1)

    result_event = parse_stream_result(log_path)
    usage = (result_event or {}).get("usage") or {}
    cost = (result_event or {}).get("total_cost_usd")
    val = run_validator(pid)

    meta = {
        "product_id": pid,
        "vendor": product["vendor"],
        "product_name": product["product_name"],
        "started_at": started_iso,
        "elapsed_seconds": elapsed,
        "exit_code": exit_code,
        "status": status,
        "skip_permissions": skip_permissions,
        "subtype": (result_event or {}).get("subtype"),
        "is_error": (result_event or {}).get("is_error"),
        "num_turns": (result_event or {}).get("num_turns"),
        "duration_ms": (result_event or {}).get("duration_ms"),
        "duration_api_ms": (result_event or {}).get("duration_api_ms"),
        "total_cost_usd": cost,
        "usage": {
            "input_tokens": usage.get("input_tokens"),
            "output_tokens": usage.get("output_tokens"),
            "cache_creation_input_tokens": usage.get("cache_creation_input_tokens"),
            "cache_read_input_tokens": usage.get("cache_read_input_tokens"),
        },
        "permission_denials": len((result_event or {}).get("permission_denials") or []),
        "session_id": (result_event or {}).get("session_id"),
        "validator": val,
        "log_path": str(log_path.relative_to(REPO_ROOT)),
    }
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    v_summary = "n/a" if not val else val.get("exit_code")
    print(f"[{pid}] {status} in {elapsed}s  turns={meta['num_turns']}  "
          f"tokens in={usage.get('input_tokens', 0)} out={usage.get('output_tokens', 0)} "
          f"cache_read={usage.get('cache_read_input_tokens', 0)} "
          f"cache_write={usage.get('cache_creation_input_tokens', 0)}  "
          f"cost=${cost or 0:.4f}  validator={v_summary}")
    return meta


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--domain", choices=list(DOMAINS.keys()), required=True,
                    help="Which project (checklist/runs tree) to run against. Required — "
                         "no default, so a mistyped command fails fast instead of silently running "
                         "against the wrong domain.")
    ap.add_argument("--mode", choices=["standard"], required=True,
                    help="Assessment mode: standard (all items). Required — "
                         "no default, so a mistyped command fails fast instead of silently running "
                         "the wrong pass.")
    ap.add_argument("--csv", type=Path, default=None,
                    help="Defaults to the domain's vendor CSV under providers/.")
    ap.add_argument("--queue-file", type=Path, default=None,
                    help="Text file with one product_id per line (e.g. decisions/deep_queue.txt). "
                         "Filters CSV rows; queue order is preserved.")
    ap.add_argument("--only", help="Run just one product_id")
    ap.add_argument("--start-at", help="Start from this product_id (applied after --queue-file)")
    ap.add_argument("--limit", type=int, help="Cap number of products")
    ap.add_argument("--skip-done", action="store_true",
                    help="Skip products whose assessment.json is already in the SAME mode.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--model", help="opus | sonnet | haiku | fable (default: session default)")
    ap.add_argument("--timeout", type=int, default=1800,
                    help="Per-product wall-clock timeout in seconds (default 30 min). "
                         "This kills the subprocess; it does not stop mid-turn like --max-turns/--max-budget-usd.")
    ap.add_argument("--max-turns", type=int, default=None,
                    help="Cap on agentic turns per product, forwarded to `claude -p --max-turns`. "
                         "Unset by default (no cap) — a standard-mode pass over 24-33 checklist items "
                         "with multi-source research routinely needs more turns than a typical single-skill "
                         "task, so borrow run-pipeline.py's 70-turn default only after checking actual usage "
                         "in a real run's claude_run.meta.json.")
    ap.add_argument("--max-budget-usd", type=float, default=None,
                    help="Cap on USD spend per product, forwarded to `claude -p --max-budget-usd`. "
                         "Unset by default (no cap) — check a real run's total_cost_usd before picking a number.")
    ap.add_argument("--dangerously-skip-permissions", action="store_true",
                    help="Forward `--dangerously-skip-permissions` to `claude -p` instead of the default "
                         "--permission-mode acceptEdits + --allowedTools whitelist. No prompt for ANY tool "
                         "call — any Bash command, any file write, in or out of the project tree. Off by "
                         "default; pass explicitly per invocation since this removes all guardrails for "
                         "an unattended batch run.")
    ap.add_argument("--sleep", type=int, default=5,
                    help="Seconds to pause between products (rate-limit hygiene)")
    ap.add_argument("--quiet", action="store_true",
                    help="Suppress live per-event progress lines (tool_use/text/tool_result) while "
                         "a product runs; only the final one-line-per-product summary prints. The "
                         "full stream-json trace is always written to claude_run.jsonl either way.")
    ap.add_argument("--overwrite", type=int, nargs="?", const=5, default=None, metavar="N",
                    help="Show a live N-line window of progress (default 5 if flag given with no "
                         "value; pass 1 for a single overwritten line), redrawn in place instead of "
                         "scrolling one line per event. No effect if --quiet is set, or if "
                         "--concurrency > 1 (multiple threads redrawing the same cursor position "
                         "would corrupt the display, so concurrency > 1 forces quiet=True). The "
                         "full stream-json trace is still written to claude_run.jsonl either way.")
    ap.add_argument("--concurrency", type=int, default=1, metavar="N",
                    help="Run up to N products in parallel (default 1 = sequential, same as before). "
                         "Products run in separate `claude -p` subprocesses via ThreadPoolExecutor; "
                         "final summary table is reordered back to CSV/queue order regardless of "
                         "completion order.")
    args = ap.parse_args()

    select_domain(args.domain)
    if args.csv is None:
        args.csv = CSV_PATH
    if args.overwrite and not args.quiet:
        _enable_windows_ansi()

    template = load_prompt_template(args.mode)
    all_products = load_products(args.csv)
    queue_pids = load_queue_file(args.queue_file) if args.queue_file else None
    products = filter_products(all_products, args.only, args.start_at, args.limit, queue_pids)
    if not products:
        print("no products to run", file=sys.stderr)
        return 1

    print(f"domain={args.domain}  mode={args.mode}  loaded={len(all_products)} products, running={len(products)}")
    if queue_pids is not None:
        print(f"queue-file={args.queue_file.relative_to(REPO_ROOT) if args.queue_file.is_relative_to(REPO_ROOT) else args.queue_file}  ({len(queue_pids)} pid(s))")
    print(f"model={args.model or 'default'}  timeout={args.timeout}s  sleep={args.sleep}s")
    print(f"cwd={REPO_ROOT}")
    print()

    summary: list[dict] = []
    print_lock = threading.Lock()

    def _run_product(i: int, prod: dict) -> dict:
        pid = prod["product_id"]
        with print_lock:
            print(f"--- [{i}/{len(products)}] {pid} ({prod['vendor']}) ---")
        if args.skip_done and already_done_for_mode(pid, args.mode):
            with print_lock:
                print(f"[{pid}] skipped (assessment.json already in mode={args.mode})")
            return {"product_id": pid, "status": "skipped"}

        prompt_text = render_prompt(template, prod)
        try:
            # Concurrent runs always use quiet per-product output — interleaved
            # progress lines (or worse, interleaved --overwrite cursor moves)
            # from multiple threads writing to the same terminal are unreadable.
            meta = run_one(prod, prompt_text, args.model, args.timeout, args.dry_run,
                            max_turns=args.max_turns, max_budget_usd=args.max_budget_usd,
                            skip_permissions=args.dangerously_skip_permissions,
                            quiet=args.quiet or args.concurrency > 1, overwrite=args.overwrite)
        except Exception as e:  # noqa: BLE001
            with print_lock:
                print(f"[{pid}] EXCEPTION: {e}", file=sys.stderr)
            meta = {"product_id": pid, "status": f"exception: {e}", "total_cost_usd": None}
        return meta

    if args.concurrency > 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
            futures = {ex.submit(_run_product, i, prod): i for i, prod in enumerate(products, 1)}
            for fut in concurrent.futures.as_completed(futures):
                summary.append(fut.result())
        order = {p["product_id"]: idx for idx, p in enumerate(products)}
        summary.sort(key=lambda s: order.get(s.get("product_id"), 9999))
    else:
        for i, prod in enumerate(products, 1):
            meta = _run_product(i, prod)
            summary.append(meta)
            if args.sleep and i < len(products) and not args.dry_run:
                time.sleep(args.sleep)

    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    summary_path = BATCH_DIR / f"summary-{ts}.json"
    total_cost = sum((s.get("total_cost_usd") or 0.0) for s in summary)
    totals = {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0, "turns": 0}
    for s in summary:
        u = s.get("usage") or {}
        totals["input"] += u.get("input_tokens") or 0
        totals["output"] += u.get("output_tokens") or 0
        totals["cache_read"] += u.get("cache_read_input_tokens") or 0
        totals["cache_write"] += u.get("cache_creation_input_tokens") or 0
        totals["turns"] += s.get("num_turns") or 0
    payload = {
        "started_at": ts,
        "mode": args.mode,
        "csv": str(args.csv.relative_to(REPO_ROOT)) if args.csv.is_relative_to(REPO_ROOT) else str(args.csv),
        "queue_file": str(args.queue_file) if args.queue_file else None,
        "model": args.model,
        "max_turns": args.max_turns,
        "max_budget_usd": args.max_budget_usd,
        "dangerously_skip_permissions": args.dangerously_skip_permissions,
        "count": len(summary),
        "total_cost_usd": total_cost,
        "totals": totals,
        "results": summary,
    }
    summary_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    print()
    print("=" * 100)
    print(f"{'product_id':38s} {'status':10s} {'turns':>5s} {'in':>8s} {'out':>7s} "
          f"{'cache_rd':>9s} {'cache_wr':>9s} {'cost':>9s}  val")
    print("-" * 100)
    for s in summary:
        cost = s.get("total_cost_usd") or 0.0
        u = s.get("usage") or {}
        val = s.get("validator")
        val_ec = val.get("exit_code") if isinstance(val, dict) else "-"
        print(f"{s.get('product_id',''):38s} {s.get('status','?'):10s} "
              f"{s.get('num_turns') or 0:>5d} "
              f"{u.get('input_tokens') or 0:>8d} {u.get('output_tokens') or 0:>7d} "
              f"{u.get('cache_read_input_tokens') or 0:>9d} {u.get('cache_creation_input_tokens') or 0:>9d} "
              f"${cost:>8.4f}  {val_ec}")
    print("-" * 100)
    print(f"TOTAL: turns={totals['turns']}  tokens in={totals['input']} out={totals['output']} "
          f"cache_read={totals['cache_read']} cache_write={totals['cache_write']}  "
          f"cost=${total_cost:.4f}")
    print(f"summary saved to {summary_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
