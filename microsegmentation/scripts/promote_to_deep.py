"""Bucket screen-mode assessments and produce the deep-pass queue.

Scans every `microsegmentation/runs/<product_id>/assessment.json` where
`assessment_mode == "screen"`, reads the (validator-enforced) gate_decision,
and writes:

    microsegmentation/decisions/
      deep_queue.txt        one product_id per line (bucket = advance-to-deep)
      needs_more_info.txt   one product_id per line (bucket = needs-more-info)
      dropped.txt           one product_id per line (bucket = drop)
      summary.md            audit table: bucket, override?, rationale

Rules are NOT re-applied here — validate_assessment.py already enforces:
  - gate_decision present in screen mode
  - recommendation != rule-default requires non-empty override_reason
So this script trusts `gate_decision.recommendation` and only reports the
rule-default alongside for audit visibility.

Run the validator on every assessment first (or via run_batch_screen.py),
otherwise garbage in / garbage out.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_ROOT = REPO_ROOT / "microsegmentation" / "runs"
DEFAULT_OUT = REPO_ROOT / "microsegmentation" / "decisions"
SCRIPTS_DIR = REPO_ROOT / "microsegmentation" / "scripts"

sys.path.insert(0, str(SCRIPTS_DIR))
from validate_assessment import compute_default_recommendation  # noqa: E402


def iter_assessments():
    for pdir in sorted(RUNS_ROOT.iterdir()):
        if not pdir.is_dir() or pdir.name.startswith("_"):
            continue
        assess = pdir / "assessment.json"
        if not assess.exists():
            yield {"pid": pdir.name, "status": "no_assessment_json"}
            continue
        try:
            data = json.loads(assess.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            yield {"pid": pdir.name, "status": f"parse_error: {e}"}
            continue
        mode = data.get("assessment_mode")
        if mode != "screen":
            yield {"pid": pdir.name, "status": f"non_screen_mode:{mode}"}
            continue
        gd = data.get("gate_decision")
        if not gd or not gd.get("recommendation"):
            yield {"pid": pdir.name, "status": "missing_gate_decision"}
            continue
        default = compute_default_recommendation(data.get("items", []))
        yield {
            "pid": pdir.name,
            "status": "ok",
            "vendor": data.get("vendor", ""),
            "product_name": data.get("product_name", ""),
            "recommendation": gd["recommendation"],
            "default": default,
            "override": gd["recommendation"] != default,
            "rationale": (gd.get("rationale") or "").strip(),
            "override_reason": (gd.get("override_reason") or "").strip(),
            "assessed_at": data.get("assessed_at", ""),
        }


def write_queue(path: Path, entries: list[dict]) -> None:
    body = "\n".join(r["pid"] for r in entries)
    path.write_text(body + ("\n" if body else ""), encoding="utf-8")


def render_summary(buckets: dict[str, list[dict]]) -> str:
    total = sum(len(v) for v in buckets.values())
    lines = [
        "# Screen-mode bucketing summary",
        "",
        f"**Total scanned:** {total}",
        "",
        "| Bucket | Count |",
        "|---|---:|",
    ]
    for b in ["advance-to-deep", "needs-more-info", "drop", "error"]:
        lines.append(f"| {b} | {len(buckets[b])} |")
    lines.append("")

    for b in ["advance-to-deep", "needs-more-info", "drop"]:
        entries = buckets[b]
        if not entries:
            continue
        lines.append(f"## {b} ({len(entries)})")
        lines.append("")
        lines.append("| product_id | vendor | override? | default | rationale |")
        lines.append("|---|---|:---:|:---:|---|")
        for r in entries:
            override = "**OVERRIDE**" if r["override"] else ""
            rat = (r["rationale"] or "").replace("\n", " ").replace("|", "\\|")
            if r["override"] and r["override_reason"]:
                reason = r["override_reason"].replace("\n", " ").replace("|", "\\|")
                rat = f"{rat}<br>*override: {reason}*"
            lines.append(
                f"| `{r['pid']}` | {r['vendor']} | {override} | `{r['default']}` | {rat} |"
            )
        lines.append("")

    if buckets["error"]:
        lines.append(f"## errors ({len(buckets['error'])})")
        lines.append("")
        lines.append("| product_id | issue |")
        lines.append("|---|---|")
        for r in buckets["error"]:
            lines.append(f"| `{r['pid']}` | {r['status']} |")
        lines.append("")
        lines.append("Errors are NOT auto-bucketed. Fix the assessment (or re-run screen) "
                     "then re-run this script.")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--dry-run", action="store_true",
                    help="Print bucket counts + errors; do not write files.")
    args = ap.parse_args()

    buckets: dict[str, list[dict]] = {
        "advance-to-deep": [],
        "needs-more-info": [],
        "drop": [],
        "error": [],
    }
    for rec in iter_assessments():
        if rec["status"] != "ok":
            buckets["error"].append(rec)
        else:
            buckets[rec["recommendation"]].append(rec)

    total = sum(len(v) for v in buckets.values())
    print(f"scanned {total} product(s) under {RUNS_ROOT.relative_to(REPO_ROOT)}")
    for b in ["advance-to-deep", "needs-more-info", "drop", "error"]:
        entries = buckets[b]
        overrides = sum(1 for r in entries if r.get("override"))
        note = f"  (with {overrides} override)" if overrides else ""
        print(f"  {b:16s} {len(entries):3d}{note}")

    if buckets["error"]:
        print("errors:")
        for r in buckets["error"]:
            print(f"  - {r['pid']}: {r['status']}")

    if args.dry_run:
        print("(dry-run — no files written)")
        return 0

    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_queue(args.out_dir / "deep_queue.txt", buckets["advance-to-deep"])
    write_queue(args.out_dir / "needs_more_info.txt", buckets["needs-more-info"])
    write_queue(args.out_dir / "dropped.txt", buckets["drop"])
    (args.out_dir / "summary.md").write_text(render_summary(buckets), encoding="utf-8")
    print(f"wrote outputs to {args.out_dir.relative_to(REPO_ROOT)}/")
    print(f"  deep queue = {len(buckets['advance-to-deep'])} product(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
