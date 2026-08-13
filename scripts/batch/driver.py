"""Agent-agnostic batch driver: subprocess spawn/pump loop, product loop,
concurrency, and summary aggregation/printing.

Everything here is written once against the AgentHandler interface
(scripts/batch/handlers/base.py) — no branching on agent name. Per-agent
behavior (CLI invocation, event schema, meta fields) lives entirely in the
handler passed in.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import queue
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

from . import common
from .handlers.base import AgentHandler

# Text-delta buffering threshold (chars) before a streaming "text" tuple is
# flushed as one progress line — avoids one-line-per-token spam for agents
# (pi) that stream text incrementally.
TEXT_BUFFER_FLUSH_LEN = 140


def add_common_arguments(parser: argparse.ArgumentParser) -> None:
    """Flags shared by every agent subcommand. --model is handler-owned
    (help text differs per agent) and added by handler.add_arguments()."""
    parser.add_argument("--domain", choices=list(common.DOMAINS.keys()), required=True,
                         help="Which project (checklist/runs tree) to run against. Required — "
                              "no default, so a mistyped command fails fast instead of silently "
                              "running against the wrong domain.")
    parser.add_argument("--mode", choices=["standard"], required=True,
                         help="Assessment mode: standard (all items). Required — "
                              "no default, so a mistyped command fails fast instead of silently "
                              "running the wrong pass.")
    parser.add_argument("--csv", type=Path, default=None,
                         help="Defaults to the domain's vendor CSV under providers/.")
    parser.add_argument("--queue-file", type=Path, default=None,
                         help="Text file with one product_id per line (e.g. decisions/deep_queue.txt). "
                              "Filters CSV rows; queue order is preserved.")
    parser.add_argument("--only", help="Run just one product_id")
    parser.add_argument("--start-at", help="Start from this product_id (applied after --queue-file)")
    parser.add_argument("--limit", type=int, help="Cap number of products")
    parser.add_argument("--skip-done", action="store_true",
                         help="Skip products whose assessment.json is already in the SAME mode.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--timeout", type=int, default=1800,
                         help="Per-product wall-clock timeout in seconds (default 30 min). This kills "
                              "the subprocess; it does not stop mid-turn like claude's --max-turns.")
    parser.add_argument("--sleep", type=int, default=5,
                         help="Seconds to pause between products (rate-limit hygiene)")
    parser.add_argument("--quiet", action="store_true",
                         help="Suppress live per-event progress lines (tool_use/text/tool_result) while "
                              "a product runs; only the final one-line-per-product summary prints. The "
                              "full stream trace is always written to the log file either way.")
    parser.add_argument("--overwrite", type=int, nargs="?", const=5, default=None, metavar="N",
                         help="Show a live N-line window of progress (default 5 if flag given with no "
                              "value; pass 1 for a single overwritten line), redrawn in place instead of "
                              "scrolling one line per event. No effect if --quiet is set, or if "
                              "--concurrency > 1 (multiple threads redrawing the same cursor position "
                              "would corrupt the display, so concurrency > 1 forces quiet=True). The "
                              "full stream trace is still written to the log file either way.")
    parser.add_argument("--concurrency", type=int, default=1, metavar="N",
                         help="Run up to N products in parallel (default 1 = sequential). Products run "
                              "in separate subprocesses via ThreadPoolExecutor; final summary table is "
                              "reordered back to CSV/queue order regardless of completion order.")


def run_one(handler: AgentHandler, product: dict, prompt_text: str, args: argparse.Namespace,
            quiet: bool, overwrite: int | None) -> dict:
    pid = product["product_id"]
    run_dir = common.RUNS_ROOT / pid

    started_iso = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    print(f"[{pid}] start {started_iso}  {handler.describe_run(prompt_text, args)}")

    if args.dry_run:
        return {
            "product_id": pid, "vendor": product["vendor"],
            "started_at": started_iso, "elapsed_seconds": 0,
            "exit_code": 0, "status": "dry-run",
            "total_cost_usd": None, "validator": None,
        }

    # Only create the run directory + write the prompt file for real runs, so
    # a dry-run doesn't pollute runs/ with empty per-product dirs.
    run_dir.mkdir(parents=True, exist_ok=True)
    handler.write_prompt_file(run_dir, prompt_text)
    cmd = handler.build_command(run_dir, prompt_text, args)

    log_path = run_dir / handler.log_filename
    meta_path = run_dir / handler.meta_filename

    t0 = time.time()
    exit_code: int | None = None
    status: str | None = None
    try:
        proc = subprocess.Popen(
            cmd, cwd=str(common.REPO_ROOT),
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, bufsize=1,
            encoding="utf-8", errors="replace",
        )
        # Pump the pipe on a background thread (not select()) so this works
        # identically on Windows and POSIX, and so the main loop can still
        # enforce --timeout even while readline() is blocked waiting on the
        # next stream line.
        line_q: queue.Queue[str | None] = queue.Queue()

        def _pump() -> None:
            assert proc.stdout is not None
            for line in iter(proc.stdout.readline, ""):
                line_q.put(line)
            line_q.put(None)

        threading.Thread(target=_pump, daemon=True).start()

        win = common.LineWindow(overwrite) if overwrite else None

        def _emit(text: str) -> None:
            line_out = common.safe_console(text)
            if win is not None:
                win.push(line_out)
            else:
                print(line_out, flush=True)

        text_buf = ""  # accumulates ("text", delta) chunks into compact progress lines
        with log_path.open("w", encoding="utf-8") as logf:
            while status is None:
                if args.timeout is not None and (time.time() - t0) > args.timeout:
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
                    result = handler.summarize_event(ev) if isinstance(ev, dict) else None
                    if isinstance(result, tuple) and result[0] == "text":
                        text_buf += result[1]
                        if len(text_buf) >= TEXT_BUFFER_FLUSH_LEN:
                            _emit(f"  [{pid}] t+{time.time() - t0:6.1f}s  text      "
                                  f"{common.truncate(text_buf, TEXT_BUFFER_FLUSH_LEN)}")
                            text_buf = ""
                    else:
                        if text_buf:
                            _emit(f"  [{pid}] t+{time.time() - t0:6.1f}s  text      "
                                  f"{common.truncate(text_buf, TEXT_BUFFER_FLUSH_LEN)}")
                            text_buf = ""
                        if result:
                            _emit(f"  [{pid}] t+{time.time() - t0:6.1f}s  {result}")
    except Exception as e:  # noqa: BLE001
        exit_code, status = -1, f"error: {e}"
    elapsed = round(time.time() - t0, 1)

    result_event = handler.parse_result(log_path)
    usage = (result_event or {}).get("usage") or {}
    cost = (result_event or {}).get("total_cost_usd")
    val = common.run_validator(pid)

    meta = {
        "product_id": pid,
        "vendor": product["vendor"],
        "product_name": product["product_name"],
        "started_at": started_iso,
        "elapsed_seconds": elapsed,
        "exit_code": exit_code,
        "status": status,
        "num_turns": (result_event or {}).get("num_turns"),
        "duration_ms": (result_event or {}).get("duration_ms"),
        "total_cost_usd": cost,
        "usage": {
            "input_tokens": usage.get("input_tokens"),
            "output_tokens": usage.get("output_tokens"),
            "cache_read_input_tokens": usage.get("cache_read_input_tokens"),
            "cache_creation_input_tokens": usage.get("cache_creation_input_tokens"),
        },
        "session_id": (result_event or {}).get("session_id"),
        **handler.meta_extra(result_event, args),
        "validator": val,
        "log_path": str(log_path.relative_to(common.REPO_ROOT)),
    }
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    v_summary = "n/a" if not val else val.get("exit_code")
    print(f"[{pid}] {status} in {elapsed}s  turns={meta['num_turns']}  "
          f"tokens in={usage.get('input_tokens', 0) or 0} out={usage.get('output_tokens', 0) or 0} "
          f"cache_read={usage.get('cache_read_input_tokens', 0) or 0} "
          f"cache_write={usage.get('cache_creation_input_tokens', 0) or 0}  "
          f"cost=${cost or 0:.4f}  validator={v_summary}")
    return meta


def run_batch(handler: AgentHandler, args: argparse.Namespace) -> int:
    common.select_domain(args.domain)
    if args.csv is None:
        args.csv = common.CSV_PATH
    if args.overwrite and not args.quiet:
        common.enable_windows_ansi()

    template = common.load_prompt_template(args.mode)
    all_products = common.load_products(args.csv)
    queue_pids = common.load_queue_file(args.queue_file) if args.queue_file else None
    products = common.filter_products(all_products, args.only, args.start_at, args.limit, queue_pids)
    if not products:
        print("no products to run", file=sys.stderr)
        return 1

    print(f"agent={handler.name}  domain={args.domain}  mode={args.mode}  "
          f"loaded={len(all_products)} products, running={len(products)}")
    if queue_pids is not None:
        qp = args.queue_file
        rel = qp.relative_to(common.REPO_ROOT) if qp.is_relative_to(common.REPO_ROOT) else qp
        print(f"queue-file={rel}  ({len(queue_pids)} pid(s))")
    print(f"model={args.model or 'default'}  timeout={args.timeout}s  sleep={args.sleep}s")
    print(f"cwd={common.REPO_ROOT}")
    print()

    summary: list[dict] = []
    print_lock = threading.Lock()

    def _run_product(i: int, prod: dict) -> dict:
        pid = prod["product_id"]
        with print_lock:
            print(f"--- [{i}/{len(products)}] {pid} ({prod['vendor']}) ---")
        if args.skip_done and common.already_done_for_mode(pid, args.mode):
            with print_lock:
                print(f"[{pid}] skipped (assessment.json already in mode={args.mode})")
            return {"product_id": pid, "status": "skipped"}

        prompt_text = common.render_prompt(template, prod)
        try:
            # Concurrent runs always use quiet per-product output — interleaved
            # progress lines (or worse, interleaved --overwrite cursor moves)
            # from multiple threads writing to the same terminal are unreadable.
            meta = run_one(handler, prod, prompt_text, args,
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

    common.BATCH_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    summary_path = common.BATCH_DIR / f"{handler.summary_prefix}-{ts}.json"
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
        "agent": handler.name,
        "mode": args.mode,
        "csv": str(args.csv.relative_to(common.REPO_ROOT)) if args.csv.is_relative_to(common.REPO_ROOT) else str(args.csv),
        "queue_file": str(args.queue_file) if args.queue_file else None,
        "model": args.model,
        **handler.batch_payload_extra(args),
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
    print(f"summary saved to {summary_path.relative_to(common.REPO_ROOT)}")
    return 0
