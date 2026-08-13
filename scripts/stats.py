"""
Aggregate cost / turn / time stats across all pi runs in all domains.

Usage:
  python scripts/stats.py                          # all domains, all modes
  python scripts/stats.py --domain bsg             # single domain
  python scripts/stats.py --sort cost              # sort by cost, turns, time, tokens
  python scripts/stats.py --csv                    # machine-readable output
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _fmt_dur(ms: int | None, elapsed_s: float | None = None) -> str:
    # Prefer wall-clock elapsed (from batch runner) over parsed duration_ms
    # when the latter is suspiciously small (< 1s) or missing.
    if elapsed_s and elapsed_s > 1 and (ms is None or ms < 1000):
        s = elapsed_s
    elif ms and ms > 0:
        s = ms / 1000
    else:
        return "-"
    if s < 60:
        return f"{s:.0f}s"
    m, sec = divmod(s, 60)
    return f"{int(m)}m{int(sec)}s"


def _fmt_tok(n: int | None) -> str:
    if n is None:
        return "-"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.0f}K"
    return str(n)


def _fmt_cost(c: float | None) -> str:
    if c is None:
        return "-"
    return f"${c:.4f}"


# ---------------------------------------------------------------------------
# collect
# ---------------------------------------------------------------------------

def collect_runs(domain_filter: str | None = None) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    for domain_dir in sorted((REPO / "providers-workspace").glob("*/runs")):
        domain = domain_dir.parent.name
        if domain_filter and domain != domain_filter:
            continue

        for meta_path in sorted(domain_dir.glob("*/pi_run.meta.json")):
            pid = meta_path.parent.name
            if pid == "_batch":
                continue
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue

            usage = meta.get("usage") or {}
            validator = meta.get("validator") or {}

            rows.append({
                "domain": domain,
                "product_id": pid,
                "vendor": meta.get("vendor", "?"),
                "model": f"{meta.get('provider', '?')}/{meta.get('model', '?')}",
                "turns": meta.get("num_turns") or 0,
                "cost": meta.get("total_cost_usd"),
                "duration_ms": meta.get("duration_ms"),
                "elapsed_seconds": meta.get("elapsed_seconds"),
                "input_tok": usage.get("input_tokens") or usage.get("input") or 0,
                "output_tok": usage.get("output_tokens") or usage.get("output") or 0,
                "cache_read": usage.get("cache_read_input_tokens") or usage.get("cacheRead") or 0,
                "stop_reason": meta.get("stop_reason", "?"),
                "status": meta.get("status", "?"),
                "val_exit": validator.get("exit_code"),
            })

    return rows


# ---------------------------------------------------------------------------
# display
# ---------------------------------------------------------------------------

def print_table(rows: list[dict[str, Any]]) -> None:
    if not rows:
        print("No runs found.")
        return

    # header
    header = (
        f"{'Domain':<18s} {'Product':<34s} {'Model':<32s} "
        f"{'Turns':>6s} {'Time':>8s} {'Cost':>9s} "
        f"{'InTok':>7s} {'OutTok':>7s} {'CacheR':>8s} "
        f"{'Stop':<9s} {'Val':>4s}"
    )
    sep = "-" * len(header)
    print(sep)
    print(header)
    print(sep)

    totals = {"turns": 0, "cost": 0.0, "input": 0, "output": 0, "cache": 0}

    for r in rows:
        totals["turns"] += r["turns"]
        totals["cost"] += r["cost"] or 0
        totals["input"] += r["input_tok"]
        totals["output"] += r["output_tok"]
        totals["cache"] += r["cache_read"]

        val_icon = "PASS" if r["val_exit"] == 0 else ("FAIL" if r["val_exit"] is not None else "-")
        print(
            f"{r['domain']:<18s} {r['product_id']:<34s} {r['model']:<32s} "
            f"{r['turns']:>6d} {_fmt_dur(r['duration_ms'], r['elapsed_seconds']):>8s} {_fmt_cost(r['cost']):>9s} "
            f"{_fmt_tok(r['input_tok']):>7s} {_fmt_tok(r['output_tok']):>7s} {_fmt_tok(r['cache_read']):>8s} "
            f"{(r['stop_reason'] or '?'):<9s} {val_icon:>4s}"
        )

    print(sep)
    print(
        f"{'':>18s} {'':>34s} {'':>32s} "
        f"{totals['turns']:>6d} {'':>8s} {_fmt_cost(totals['cost']):>9s} "
        f"{_fmt_tok(totals['input']):>7s} {_fmt_tok(totals['output']):>7s} {_fmt_tok(totals['cache']):>8s} "
        f"{'':>9s} {'':>4s}"
    )
    print(sep)
    print(f"  {len(rows)} product(s)  |  {_fmt_cost(totals['cost'])} total cost")


def print_csv(rows: list[dict[str, Any]]) -> None:
    import csv
    w = csv.writer(sys.stdout)
    w.writerow(["domain", "product_id", "vendor", "model", "turns", "duration_ms",
                "cost_usd", "input_tokens", "output_tokens", "cache_read_tokens",
                "stop_reason", "status", "validator_exit"])
    for r in rows:
        w.writerow([
            r["domain"], r["product_id"], r["vendor"], r["model"],
            r["turns"], r["duration_ms"] or "",
            f"{r['cost']:.6f}" if r["cost"] is not None else "",
            r["input_tok"], r["output_tok"], r["cache_read"],
            r["stop_reason"], r["status"],
            r["val_exit"] if r["val_exit"] is not None else "",
        ])


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Aggregate pi run stats")
    ap.add_argument("--domain", help="filter to single domain (bsg, microsegmentation)")
    ap.add_argument("--sort", choices=["cost", "turns", "time", "tokens"],
                    default="cost", help="sort column (default: cost)")
    ap.add_argument("--csv", action="store_true", help="CSV output")
    ap.add_argument("--desc", action="store_true", help="descending sort")
    args = ap.parse_args()

    rows = collect_runs(args.domain)

    key = {
        "cost":   lambda r: r["cost"] or 0,
        "turns":  lambda r: r["turns"],
        "time":   lambda r: r["duration_ms"] or 0,
        "tokens": lambda r: r["input_tok"] + r["output_tok"],
    }[args.sort]
    rows.sort(key=key, reverse=args.desc)

    if args.csv:
        print_csv(rows)
    else:
        print_table(rows)


if __name__ == "__main__":
    main()
