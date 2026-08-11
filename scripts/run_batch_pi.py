"""Batch-run screen or standard mode assessment across a product list — pi edition.

Same logic as run_batch.py but uses `pi --mode json` instead of `claude -p
--output-format stream-json`. All file paths, validation, and summary
collection are identical to run_batch.py.

Modes:
  --mode screen    → runs <domain>/prompts/screen_mode.md
  --mode standard  → runs <domain>/prompts/standard_mode.md

For each product:
  1. Render the mode-specific prompt template with {VENDOR}, {PRODUCT_NAME},
     {product_id}.
  2. Spawn a FRESH `pi --mode json` session (--no-session) with project skills
     auto-loaded (cwd = repo root).
  3. Stream the full trace into runs/<pid>/pi_run.jsonl.
  4. Run validate_assessment.py against the produced assessment.json and
     record the outcome in runs/<pid>/pi_run.meta.json.

--skip-done skips a product only when its existing assessment.json is in the
SAME mode as the current run.

--concurrency N runs up to N products in parallel (ThreadPoolExecutor).

Requires: pi CLI on PATH, venv Python for the validator.
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

# Module-level defaults — reassigned in main() via select_domain().
CSV_PATH = DOMAINS["microsegmentation"]["csv"]
PROMPTS_DIR = DOMAINS["microsegmentation"]["dir"] / "prompts"
PROMPT_FILES = {
    "screen": PROMPTS_DIR / "screen_mode.md",
    "standard": PROMPTS_DIR / "standard_mode.md",
}
RUNS_ROOT = DOMAINS["microsegmentation"]["dir"] / "runs"
VALIDATOR = DOMAINS["microsegmentation"]["dir"] / "scripts" / "validate_assessment.py"
VENV_PY = REPO_ROOT / "venv" / "Scripts" / "python.exe"
BATCH_DIR = RUNS_ROOT / "_batch"


def select_domain(domain: str) -> None:
    """Reassign the module-level path constants for the chosen domain."""
    global CSV_PATH, PROMPTS_DIR, PROMPT_FILES, RUNS_ROOT, VALIDATOR, BATCH_DIR
    cfg = DOMAINS[domain]
    CSV_PATH = cfg["csv"]
    PROMPTS_DIR = cfg["dir"] / "prompts"
    PROMPT_FILES = {
        "screen": PROMPTS_DIR / "screen_mode.md",
        "standard": PROMPTS_DIR / "standard_mode.md",
    }
    RUNS_ROOT = cfg["dir"] / "runs"
    VALIDATOR = cfg["dir"] / "scripts" / "validate_assessment.py"
    BATCH_DIR = RUNS_ROOT / "_batch"


# ---------------------------------------------------------------------------
# Prompt template loading (unchanged from run_batch.py)
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# CSV product loading (unchanged)
# ---------------------------------------------------------------------------

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
            .replace("{VENDOR}", product["vendor"])
            .replace("{PRODUCT_NAME}", product["product_name"])
            .replace("{product_id}", product["product_id"]))


# ---------------------------------------------------------------------------
# pi JSON mode stream parsing
# ---------------------------------------------------------------------------

def parse_pi_stream_result(log_path: Path) -> dict | None:
    """Scan pi --mode json log for session-level cost/usage summary.

    Pi emits per-message usage (on each assistant message_end), not a single
    'result' event like Claude. We aggregate from all assistant message_end
    events and also look for the final agent_end + agent_settled.
    """
    if not log_path.exists():
        return None
    total_usage = {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0}
    total_cost = 0.0
    num_turns = 0
    session_id = None
    model_info = {"provider": None, "model": None}
    stop_reason = None
    error_message = None
    duration_ms = None
    agent_start_ts = None
    agent_end_ts = None
    first_event_ts = None   # fallback when agent_start is missing
    last_event_ts = None    # fallback when agent_end is missing

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

                etype = ev.get("type")
                ts = ev.get("timestamp")

                # Fallback timestamps (first & last event in stream)
                if ts:
                    if first_event_ts is None:
                        first_event_ts = ts
                    last_event_ts = ts

                # Session header
                if etype == "session":
                    session_id = ev.get("id")

                # Turn counting
                elif etype == "turn_start":
                    num_turns += 1

                # Timing
                elif etype == "agent_start":
                    agent_start_ts = ev.get("timestamp")

                elif etype == "agent_end":
                    agent_end_ts = ev.get("timestamp")
                    # agent_end carries the final messages array including usage.
                    # We prefer this over individual message_end events because
                    # it's the authoritative final state (message_end fires on
                    # every message, including retries, which would double-count).

                # Per-message usage (assistant) — aggregate from message_end.
                # This is the reliable way because agent_end may not be emitted
                # if the process is killed (timeout).
                elif etype == "message_end":
                    msg = ev.get("message") or {}
                    # Extract message timestamp as fallback duration source.
                    # Pi emits message.timestamp as Unix ms on message_end.
                    msg_ts = msg.get("timestamp")
                    if msg_ts:
                        if first_event_ts is None:
                            first_event_ts = msg_ts
                        last_event_ts = msg_ts
                    if msg.get("role") == "assistant":
                        # Only count if this is a terminal message (not pending).
                        # stopReason == "pending" means it's still streaming;
                        # the final message_end for that turn will have a real stopReason.
                        if msg.get("stopReason") != "pending":
                            u = msg.get("usage") or {}
                            total_usage["input"] += u.get("input", 0)
                            total_usage["output"] += u.get("output", 0)
                            total_usage["cacheRead"] += u.get("cacheRead", 0)
                            total_usage["cacheWrite"] += u.get("cacheWrite", 0)
                            c = u.get("cost") or {}
                            total_cost += c.get("total", 0)
                        model_info["provider"] = msg.get("provider")
                        model_info["model"] = msg.get("model")
                        stop_reason = msg.get("stopReason")
                        if msg.get("errorMessage"):
                            error_message = msg["errorMessage"]

    except Exception:
        pass

    # Compute duration — prefer agent_start/agent_end, fall back to
    # first/last message timestamps (covers runs killed before agent_end).
    # Pi emits two timestamp formats: ISO 8601 strings (session/agent events)
    # and Unix milliseconds integers (message.timestamp on message_end).
    def _parse_ts(ts: str | int | None) -> datetime | None:
        if ts is None:
            return None
        if isinstance(ts, (int, float)):
            # Unix milliseconds
            return datetime.fromtimestamp(ts / 1000, tz=timezone.utc)
        # ISO 8601 string
        try:
            return datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
        except Exception:
            return None

    start_ts = _parse_ts(agent_start_ts) or _parse_ts(first_event_ts)
    end_ts = _parse_ts(agent_end_ts) or _parse_ts(last_event_ts)
    if start_ts and end_ts:
        duration_ms = int((end_ts - start_ts).total_seconds() * 1000)

    return {
        "session_id": session_id,
        "provider": model_info["provider"],
        "model": model_info["model"],
        "num_turns": num_turns,
        "duration_ms": duration_ms,
        "stop_reason": stop_reason,
        "error_message": error_message,
        "usage": total_usage,
        "total_cost_usd": total_cost,
    }


# ---------------------------------------------------------------------------
# Progress display helpers (adapted from run_batch.py)
# ---------------------------------------------------------------------------

def _safe_console(s: str) -> str:
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
    full pi_run.jsonl trace is unaffected — it's written to the log file
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
    name_lower = name.lower()
    if name_lower in ("bash",):
        return _truncate(inp.get("command", ""), 90)
    if name_lower in ("read", "edit", "write"):
        return inp.get("path", inp.get("file_path", ""))
    if name_lower in ("grep", "find", "ls"):
        return _truncate(inp.get("pattern", "") or inp.get("path", ""), 60)
    keys = ", ".join(list(inp.keys())[:3])
    return f"{{{keys}}}" if keys else ""


def summarize_event(ev: dict) -> str | None:
    """One-line progress summary for a pi --mode json event.

    Pi JSON mode events: session, agent_start, agent_end, agent_settled,
    turn_start, turn_end, message_start, message_update, message_end,
    tool_execution_start, tool_execution_update, tool_execution_end,
    compaction_start, compaction_end, queue_update.
    """
    etype = ev.get("type")
    if etype == "session":
        return f"session init  id={ev.get('id', '?')}  cwd={ev.get('cwd', '?')}"
    if etype == "agent_start":
        return "agent started"
    if etype == "agent_settled":
        return "agent settled (done)"
    if etype == "tool_execution_start":
        name = ev.get("toolName", "?")
        args = ev.get("args") or {}
        brief = _brief_tool_input(name, args)
        return f"tool_start  {name}({brief})" if brief else f"tool_start  {name}"
    if etype == "tool_execution_end":
        name = ev.get("toolName", "?")
        is_err = ev.get("isError", False)
        tag = "ERROR" if is_err else "ok"
        return f"tool_end[{tag}]  {name}"
    if etype == "message_update":
        ame = ev.get("assistantMessageEvent") or {}
        delta_type = ame.get("type")
        if delta_type == "text_delta":
            # Return raw delta — caller accumulates to avoid one-line-per-token spam.
            return ("text", ame.get("delta", ""))
        elif delta_type == "thinking_delta":
            return None
        elif delta_type == "toolcall_end":
            tc = ame.get("toolCall") or {}
            name = tc.get("name", "?")
            args = tc.get("arguments") or {}
            brief = _brief_tool_input(name, args)
            return f"toolcall  {name}({brief})" if brief else f"toolcall  {name}"
        elif delta_type == "toolcall_start":
            return None
        return None
    if etype == "compaction_start":
        return "compaction started"
    if etype == "compaction_end":
        return "compaction ended"
    return None


# ---------------------------------------------------------------------------
# Validator runner (unchanged)
# ---------------------------------------------------------------------------

def run_validator(pid: str) -> dict | None:
    assessment = RUNS_ROOT / pid / "assessment.json"
    if not assessment.exists():
        return {"exit_code": None, "note": "assessment.json missing"}
    py = str(VENV_PY) if VENV_PY.exists() else sys.executable
    proc = subprocess.run(
        [py, str(VALIDATOR), str(assessment),
         "--evidence-store", str(RUNS_ROOT / pid)],
        capture_output=True, text=True,
    )
    return {
        "exit_code": proc.returncode,
        "stdout_tail": proc.stdout.strip().splitlines()[-5:] if proc.stdout else [],
        "stderr_tail": proc.stderr.strip().splitlines()[-5:] if proc.stderr else [],
    }


# ---------------------------------------------------------------------------
# Single product runner
# ---------------------------------------------------------------------------

def run_one(product, prompt_text, model, timeout, dry_run, quiet=False, overwrite: int | None = None) -> dict:
    pid = product["product_id"]
    run_dir = RUNS_ROOT / pid

    pi_bin = shutil.which("pi")
    if not pi_bin:
        raise SystemExit("`pi` CLI not on PATH")

    # Write prompt to a temp file so we can use pi's @file syntax.
    # Windows CreateProcess has a 32K command-line limit; long prompts
    # (9K+) easily exceed it after list2cmdline quoting.  @file avoids
    # the limit entirely.
    prompt_file = run_dir / "prompt_pi.txt"
    run_dir.mkdir(parents=True, exist_ok=True)
    prompt_file.write_text(prompt_text, encoding="utf-8")

    # pi --mode json outputs streaming events; -nc disables context-file
    # loading (our prompt already has all instructions embedded).
    # --no-session avoids polluting ~/.pi/agent/sessions/ with ephemeral runs.
    # --approve auto-trusts the project so the skill under .pi/skills/ loads.
    cmd = [
        pi_bin, "--mode", "json",
        "--no-session",
        "--approve",
        "-nc",
        f"@{prompt_file}",
    ]
    if model:
        cmd.extend(["--model", model])

    started_iso = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    print(f"[{pid}] start {started_iso}  prompt={len(prompt_text)}B  model={model or 'default'}")

    if dry_run:
        return {
            "product_id": pid, "vendor": product["vendor"],
            "started_at": started_iso, "elapsed_seconds": 0,
            "exit_code": 0, "status": "dry-run",
            "total_cost_usd": None, "validator": None,
        }

    # prompt_pi.txt already written above (before Popen to avoid the
    # Windows command-line length limit).
    log_path = run_dir / "pi_run.jsonl"
    meta_path = run_dir / "pi_run.meta.json"

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
        # Pump pipe on background thread
        line_q: queue.Queue[str | None] = queue.Queue()

        def _pump() -> None:
            assert proc.stdout is not None
            for line in iter(proc.stdout.readline, ""):
                line_q.put(line)
            line_q.put(None)

        threading.Thread(target=_pump, daemon=True).start()

        win = _LineWindow(overwrite) if overwrite else None

        def _emit(text: str) -> None:
            line_out = _safe_console(text)
            if win is not None:
                win.push(line_out)
            else:
                print(line_out, flush=True)

        text_buf = ""  # accumulate text_delta chunks for compact progress lines
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
                    if isinstance(ev, dict):
                        result = summarize_event(ev)
                        if isinstance(result, tuple) and result[0] == "text":
                            # Buffer text deltas; flush on non-text event or when
                            # buffer fills up (avoid one-line-per-token spam).
                            text_buf += result[1]
                            if len(text_buf) >= 140:
                                _emit(f"  [{pid}] t+{time.time() - t0:6.1f}s  text      {_truncate(text_buf, 140)}")
                                text_buf = ""
                        else:
                            # Flush any buffered text before printing this event.
                            if text_buf:
                                _emit(f"  [{pid}] t+{time.time() - t0:6.1f}s  text      {_truncate(text_buf, 140)}")
                                text_buf = ""
                            if result:
                                _emit(f"  [{pid}] t+{time.time() - t0:6.1f}s  {result}")
    except Exception as e:
        exit_code, status = -1, f"error: {e}"
    elapsed = round(time.time() - t0, 1)

    result_event = parse_pi_stream_result(log_path)
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
        "agent": "pi",
        "provider": (result_event or {}).get("provider"),
        "model": (result_event or {}).get("model"),
        "num_turns": (result_event or {}).get("num_turns"),
        "duration_ms": (result_event or {}).get("duration_ms"),
        "total_cost_usd": cost,
        "stop_reason": (result_event or {}).get("stop_reason"),
        "error_message": (result_event or {}).get("error_message"),
        "usage": {
            "input_tokens": usage.get("input"),
            "output_tokens": usage.get("output"),
            "cache_read_input_tokens": usage.get("cacheRead"),
            "cache_creation_input_tokens": usage.get("cacheWrite"),
        },
        "session_id": (result_event or {}).get("session_id"),
        "validator": val,
        "log_path": str(log_path.relative_to(REPO_ROOT)),
    }
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    v_summary = "n/a" if not val else val.get("exit_code")
    print(f"[{pid}] {status} in {elapsed}s  turns={meta['num_turns']}  "
          f"tokens in={usage.get('input', 0)} out={usage.get('output', 0)} "
          f"cache_read={usage.get('cacheRead', 0)} "
          f"cache_write={usage.get('cacheWrite', 0)}  "
          f"cost=${cost or 0:.4f}  validator={v_summary}")
    return meta


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--domain", choices=list(DOMAINS.keys()), required=True,
                    help="Which project to run against.")
    ap.add_argument("--mode", choices=["screen", "standard"], required=True,
                    help="Assessment mode: screen (gate items) | standard (all items).")
    ap.add_argument("--csv", type=Path, default=None,
                    help="Defaults to the domain's vendor CSV under providers/.")
    ap.add_argument("--queue-file", type=Path, default=None,
                    help="Text file with one product_id per line.")
    ap.add_argument("--only", help="Run just one product_id")
    ap.add_argument("--start-at", help="Start from this product_id")
    ap.add_argument("--limit", type=int, help="Cap number of products")
    ap.add_argument("--skip-done", action="store_true",
                    help="Skip products whose assessment.json is already in the SAME mode.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--model", help="e.g. deepseek/deepseek-v4-pro or anthropic/claude-sonnet-4-5")
    ap.add_argument("--timeout", type=int, default=1800,
                    help="Per-product wall-clock timeout in seconds (default 30 min).")
    ap.add_argument("--sleep", type=int, default=5,
                    help="Seconds to pause between products.")
    ap.add_argument("--quiet", action="store_true",
                    help="Suppress live per-event progress lines.")
    ap.add_argument("--concurrency", type=int, default=1, metavar="N",
                    help="Run up to N products in parallel (default 1 = sequential).")
    ap.add_argument("--overwrite", type=int, nargs="?", const=5, default=None, metavar="N",
                    help="Show a live N-line window of progress (default 5 if flag given with no "
                         "value; pass 1 for a single overwritten line), redrawn in place instead of "
                         "scrolling one line per event. No effect if --quiet is set. The full "
                         "stream trace is still written to pi_run.jsonl either way.")
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
        qp = args.queue_file
        rel = qp.relative_to(REPO_ROOT) if qp.is_relative_to(REPO_ROOT) else qp
        print(f"queue-file={rel}  ({len(queue_pids)} pid(s))")
    print(f"model={args.model or 'default'}  timeout={args.timeout}s  sleep={args.sleep}s")
    print(f"agent=pi  cwd={REPO_ROOT}")
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
            # Concurrent runs always use quiet per-product output to avoid
            # interleaved progress lines. The final summary is printed per product.
            meta = run_one(prod, prompt_text, args.model, args.timeout, args.dry_run,
                           quiet=args.quiet or args.concurrency > 1, overwrite=args.overwrite)
        except Exception as e:
            with print_lock:
                print(f"[{pid}] EXCEPTION: {e}", file=sys.stderr)
            meta = {"product_id": pid, "status": f"exception: {e}", "total_cost_usd": None}

        # Print per-product summary
        u = meta.get("usage") or {}
        with print_lock:
            print(f"[{pid}] {meta.get('status')} in {meta.get('elapsed_seconds', '?')}s  "
                  f"turns={meta.get('num_turns')}  "
                  f"cost=${meta.get('total_cost_usd') or 0:.4f}  "
                  f"val={meta.get('validator', {}).get('exit_code', '-')}")
        return meta

    if args.concurrency > 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as ex:
            futures = {ex.submit(_run_product, i, prod): i for i, prod in enumerate(products, 1)}
            for fut in concurrent.futures.as_completed(futures):
                summary.append(fut.result())
        # Restore original order
        summary.sort(key=lambda s: next(
            (i for i, p in enumerate(products, 1) if p["product_id"] == s.get("product_id")),
            9999))
    else:
        for i, prod in enumerate(products, 1):
            meta = _run_product(i, prod)
            summary.append(meta)
            if args.sleep and i < len(products) and not args.dry_run:
                time.sleep(args.sleep)

    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    summary_path = BATCH_DIR / f"summary-pi-{ts}.json"
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
        "agent": "pi",
        "mode": args.mode,
        "csv": str(args.csv.relative_to(REPO_ROOT)) if args.csv.is_relative_to(REPO_ROOT) else str(args.csv),
        "queue_file": str(args.queue_file) if args.queue_file else None,
        "model": args.model,
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
