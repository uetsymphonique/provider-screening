"""Batch-run screen or standard mode assessment across a product list.

Modes:
  --mode screen    (default) → runs microsegmentation/prompts/screen_mode.md;
                     source is providers/Microsegmentation.csv (all 50 rows).
  --mode standard  → runs microsegmentation/prompts/standard_mode.md;
                     source should be --queue-file microsegmentation/decisions/deep_queue.txt
                     produced by promote_to_deep.py.

For each product:
  1. Render the mode-specific prompt template with {VENDOR}, {PRODUCT_NAME},
     {product_id}.
  2. Spawn a FRESH `claude -p` session (no --continue / --resume) with the
     project's .claude/skills/deep-research auto-loaded (cwd = repo root).
  3. Stream the full trace into runs/<pid>/claude_run.jsonl.
  4. Run validate_assessment.py against the produced assessment.json and
     record the outcome in runs/<pid>/claude_run.meta.json.

--skip-done skips a product only when its existing assessment.json is in the
SAME mode as the current run (so a screen result doesn't block a standard rerun).

Requires:  claude CLI on PATH, venv Python for the validator.
Docs cross-checked: https://code.claude.com/docs/en/headless.md
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
import time
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

# Pre-approve the tools the screen-mode prompt actually needs. Combined with
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
            .replace("{VENDOR}", product["vendor"])
            .replace("{PRODUCT_NAME}", product["product_name"])
            .replace("{product_id}", product["product_id"]))


def parse_stream_cost(log_path: Path) -> float | None:
    """Scan stream-json log for the final result event; return total_cost_usd."""
    if not log_path.exists():
        return None
    cost = None
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
                    c = ev.get("total_cost_usd") or ev.get("cost_usd")
                    if c is not None:
                        cost = float(c)
    except Exception:  # noqa: BLE001
        pass
    return cost


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


def run_one(product, prompt_text, model, timeout, dry_run) -> dict:
    pid = product["product_id"]
    run_dir = RUNS_ROOT / pid

    claude_bin = shutil.which("claude")
    if not claude_bin:
        raise SystemExit("`claude` CLI not on PATH")

    cmd = [
        claude_bin, "-p",
        "--output-format", "stream-json",
        "--verbose",  # required for stream-json in -p mode
        "--permission-mode", "acceptEdits",
        "--allowedTools", ALLOWED_TOOLS,
    ]
    if model:
        cmd.extend(["--model", model])
    cmd.append(prompt_text)

    started_iso = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    print(f"[{pid}] start {started_iso}  prompt={len(prompt_text)}B  model={model or 'default'}")

    if dry_run:
        return {
            "product_id": pid, "vendor": product["vendor"],
            "started_at": started_iso, "elapsed_seconds": 0,
            "exit_code": 0, "status": "dry-run",
            "total_cost_usd": None, "validator": None,
        }

    # Only create the run directory + write prompt for real runs, so a dry-run
    # doesn't pollute runs/ with empty per-product dirs (breaks promote_to_deep).
    run_dir.mkdir(parents=True, exist_ok=True)
    prompt_path = run_dir / "prompt.txt"
    log_path = run_dir / "claude_run.jsonl"
    meta_path = run_dir / "claude_run.meta.json"
    prompt_path.write_text(prompt_text, encoding="utf-8")

    t0 = time.time()
    try:
        with log_path.open("w", encoding="utf-8") as logf:
            proc = subprocess.run(
                cmd, cwd=str(REPO_ROOT),
                stdout=logf, stderr=subprocess.STDOUT,
                timeout=timeout, check=False,
            )
        exit_code = proc.returncode
        status = "ok" if exit_code == 0 else f"exit-{exit_code}"
    except subprocess.TimeoutExpired:
        exit_code = -1
        status = "timeout"
    elapsed = round(time.time() - t0, 1)

    cost = parse_stream_cost(log_path)
    val = run_validator(pid)

    meta = {
        "product_id": pid,
        "vendor": product["vendor"],
        "product_name": product["product_name"],
        "started_at": started_iso,
        "elapsed_seconds": elapsed,
        "exit_code": exit_code,
        "status": status,
        "total_cost_usd": cost,
        "validator": val,
        "log_path": str(log_path.relative_to(REPO_ROOT)),
    }
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    v_summary = "n/a" if not val else val.get("exit_code")
    print(f"[{pid}] {status} in {elapsed}s  cost=${cost or 0:.4f}  validator={v_summary}")
    return meta


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--domain", choices=list(DOMAINS.keys()), default="microsegmentation",
                    help="Which project (checklist/prompts/runs tree) to run against.")
    ap.add_argument("--mode", choices=["screen", "standard"], default="screen",
                    help="Assessment mode: screen (6 gate items) | standard (all items)")
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
                    help="Per-product timeout in seconds (default 30 min)")
    ap.add_argument("--sleep", type=int, default=5,
                    help="Seconds to pause between products (rate-limit hygiene)")
    args = ap.parse_args()

    select_domain(args.domain)
    if args.csv is None:
        args.csv = CSV_PATH

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
    for i, prod in enumerate(products, 1):
        pid = prod["product_id"]
        print(f"--- [{i}/{len(products)}] {pid} ({prod['vendor']}) ---")
        if args.skip_done and already_done_for_mode(pid, args.mode):
            print(f"[{pid}] skipped (assessment.json already in mode={args.mode})")
            summary.append({"product_id": pid, "status": "skipped"})
            continue

        prompt_text = render_prompt(template, prod)
        try:
            meta = run_one(prod, prompt_text, args.model, args.timeout, args.dry_run)
        except Exception as e:  # noqa: BLE001
            print(f"[{pid}] EXCEPTION: {e}", file=sys.stderr)
            meta = {"product_id": pid, "status": f"exception: {e}", "total_cost_usd": None}
        summary.append(meta)

        if args.sleep and i < len(products) and not args.dry_run:
            time.sleep(args.sleep)

    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    summary_path = BATCH_DIR / f"summary-{ts}.json"
    total_cost = sum((s.get("total_cost_usd") or 0.0) for s in summary)
    payload = {
        "started_at": ts,
        "mode": args.mode,
        "csv": str(args.csv.relative_to(REPO_ROOT)) if args.csv.is_relative_to(REPO_ROOT) else str(args.csv),
        "queue_file": str(args.queue_file) if args.queue_file else None,
        "model": args.model,
        "count": len(summary),
        "total_cost_usd": total_cost,
        "results": summary,
    }
    summary_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    print()
    print("=" * 78)
    print(f"{'product_id':40s} {'status':14s} {'cost':>10s}  val")
    print("-" * 78)
    for s in summary:
        cost = s.get("total_cost_usd") or 0.0
        val = s.get("validator")
        val_ec = val.get("exit_code") if isinstance(val, dict) else "-"
        print(f"{s.get('product_id',''):40s} {s.get('status','?'):14s} "
              f"${cost:>9.4f}  {val_ec}")
    print("-" * 78)
    print(f"TOTAL COST: ${total_cost:.4f}")
    print(f"summary saved to {summary_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
