"""Aggregate all product assessments into a single comparison matrix.

Scans <runs-root>/**/assessment.json, then emits:
  - comparison_matrix.csv     — one row per product × one column per checklist item
                                 (verdict + confidence + evidence count)
  - coverage_summary.csv      — per-product verdict counts + evidence quality

Usage:
    python aggregate_matrix.py
        [--runs-root bsg/runs]
        [--checklist bsg/checklist.yaml]
        [--out-dir bsg]
        [--mode any|screen|standard|deep]   # filter by assessment_mode
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RUNS = REPO_ROOT / "bsg" / "runs"
DEFAULT_CHECKLIST = REPO_ROOT / "bsg" / "checklist.yaml"
DEFAULT_OUT = REPO_ROOT / "bsg"


VERDICT_GLYPH = {
    "supported": "Y",
    "partial": "P",
    "not_supported": "N",
    "unknown": "?",
    "not_applicable": "-",
}


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def collect_assessments(runs_root: Path, mode_filter: str) -> list[tuple[Path, dict]]:
    if not runs_root.exists():
        return []
    results: list[tuple[Path, dict]] = []
    for path in sorted(runs_root.rglob("assessment.json")):
        try:
            data = load_json(path)
        except Exception as e:  # noqa: BLE001
            print(f"WARN skipping {path}: {e}", file=sys.stderr)
            continue
        if mode_filter != "any" and data.get("assessment_mode") != mode_filter:
            continue
        results.append((path, data))
    return results


def build_matrix_row(assessment: dict, item_ids: list[str]) -> dict[str, str]:
    per_item = {it["item_id"]: it for it in assessment["items"]}
    row = {
        "product_id": assessment["product_id"],
        "vendor": assessment["vendor"],
        "product_name": assessment["product_name"],
        "mode": assessment["assessment_mode"],
        "checklist_version": assessment["checklist_version"],
        "assessed_at": assessment.get("assessed_at", ""),
    }
    for iid in item_ids:
        item = per_item.get(iid)
        if item is None:
            row[iid] = ""            # not evaluated (screen mode skipping)
            row[f"{iid}_conf"] = ""
            row[f"{iid}_ev"] = ""
        else:
            row[iid] = VERDICT_GLYPH.get(item["verdict"], "?")
            row[f"{iid}_conf"] = item.get("confidence", "")
            row[f"{iid}_ev"] = len(item.get("evidence_ids", []))
    return row


def build_summary_row(assessment: dict) -> dict[str, object]:
    verdicts = Counter(it["verdict"] for it in assessment["items"])
    confidences = Counter(it["confidence"] for it in assessment["items"])
    vendor_only = sum(
        1
        for it in assessment["items"]
        if it.get("source_types")
        and all(st in {"vendor_doc", "vendor_datasheet", "vendor_blog"} for st in it["source_types"])
    )
    triangulated = sum(
        1 for it in assessment["items"] if len(set(it.get("cited_source_ids", []))) >= 3
    )
    return {
        "product_id": assessment["product_id"],
        "vendor": assessment["vendor"],
        "product_name": assessment["product_name"],
        "mode": assessment["assessment_mode"],
        "items_assessed": len(assessment["items"]),
        "supported": verdicts["supported"],
        "partial": verdicts["partial"],
        "not_supported": verdicts["not_supported"],
        "unknown": verdicts["unknown"],
        "not_applicable": verdicts["not_applicable"],
        "confidence_high": confidences["high"],
        "confidence_medium": confidences["medium"],
        "confidence_low": confidences["low"],
        "vendor_only_items": vendor_only,
        "triangulated_items": triangulated,
    }


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-root", type=Path, default=DEFAULT_RUNS)
    ap.add_argument("--checklist", type=Path, default=DEFAULT_CHECKLIST)
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--mode", choices=["any", "screen", "standard", "deep"], default="any")
    args = ap.parse_args()

    checklist = load_yaml(args.checklist)
    item_ids = [it["id"] for it in checklist["items"]]

    assessments = collect_assessments(args.runs_root, args.mode)
    if not assessments:
        print(f"No assessment.json found under {args.runs_root}", file=sys.stderr)
        return 0

    matrix_rows = [build_matrix_row(a, item_ids) for _, a in assessments]
    summary_rows = [build_summary_row(a) for _, a in assessments]

    matrix_fields = ["product_id", "vendor", "product_name", "mode", "checklist_version", "assessed_at"]
    for iid in item_ids:
        matrix_fields.extend([iid, f"{iid}_conf", f"{iid}_ev"])

    summary_fields = list(summary_rows[0].keys())

    matrix_path = args.out_dir / "comparison_matrix.csv"
    summary_path = args.out_dir / "coverage_summary.csv"
    write_csv(matrix_path, matrix_rows, matrix_fields)
    write_csv(summary_path, summary_rows, summary_fields)

    print(f"Wrote {matrix_path} ({len(matrix_rows)} products, {len(item_ids)} items)")
    print(f"Wrote {summary_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
