"""Aggregate all product assessments into a single comparison matrix.

Scans <runs-root>/**/assessment.json, then emits:
  - comparison_matrix.csv     — one row per product × one column per checklist item
                                 (verdict + confidence + evidence count)
  - coverage_summary.csv      — per-product verdict counts + evidence quality
                                 + absolute_pct + applicable_pct
  - product_scores.csv        — per-category + total weighted scores
                                 absolute_pct (weighted/33) + applicable_pct (weighted/applicable_max)

Usage:
    python aggregate_matrix.py
        [--runs-root microsegmentation/runs]
        [--checklist microsegmentation/checklist.yaml]
        [--out-dir microsegmentation]
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
DEFAULT_RUNS = REPO_ROOT / "microsegmentation" / "runs"
DEFAULT_CHECKLIST = REPO_ROOT / "microsegmentation" / "checklist.yaml"
DEFAULT_OUT = REPO_ROOT / "microsegmentation"


VERDICT_GLYPH = {
    "supported": "Y",
    "partial": "P",
    "not_supported": "N",
    "unknown": "?",
    "not_applicable": "-",
}

# Scoring: verdict_score * confidence_weight
VERDICT_SCORE = {
    "supported": 1.0,
    "partial": 0.5,
    "not_supported": 0.0,
    "unknown": 0.0,
    "not_applicable": 0.0,
}

CONFIDENCE_WEIGHT = {
    "high": 1.0,
    "medium": 0.75,
    "low": 0.5,
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


def compute_item_score(item: dict) -> float:
    """Weighted score for a single checklist item: verdict_score * confidence_weight."""
    v_score = VERDICT_SCORE.get(item["verdict"], 0.0)
    c_weight = CONFIDENCE_WEIGHT.get(item.get("confidence", "low"), 0.5)
    return v_score * c_weight


def compute_total_score(items: list[dict]) -> tuple[float, int, float]:
    """Return (weighted_sum, max_possible, raw_sum) across all items."""
    weighted = sum(compute_item_score(it) for it in items)
    raw = sum(VERDICT_SCORE.get(it["verdict"], 0.0) for it in items)
    return weighted, len(items), raw


def build_score_row(assessment: dict, categories: list[dict]) -> dict[str, object]:
    """Build a per-category + total score row for a product."""
    per_item = {it["item_id"]: it for it in assessment["items"]}
    row: dict[str, object] = {
        "product_id": assessment["product_id"],
        "vendor": assessment["vendor"],
        "product_name": assessment["product_name"],
        "mode": assessment["assessment_mode"],
    }
    total_weighted = 0.0
    total_max = 0
    total_raw = 0.0
    total_excluded = 0
    for cat in categories:
        cat_id = cat["id"]
        cat_items = [per_item[iid] for iid in cat["item_ids"] if iid in per_item]
        if cat_items:
            w, m, r = compute_total_score(cat_items)
            excluded = sum(1 for it in cat_items if it["verdict"] == "not_applicable")
        else:
            w, m, r, excluded = 0.0, 0, 0.0, 0
        row[f"{cat_id}_weighted"] = round(w, 2)
        row[f"{cat_id}_max"] = m
        row[f"{cat_id}_raw"] = round(r, 2)
        total_weighted += w
        total_max += m
        total_raw += r
        total_excluded += excluded
    applicable_max = total_max - total_excluded
    row["total_weighted"] = round(total_weighted, 2)
    row["total_max"] = total_max
    row["total_raw"] = round(total_raw, 2)
    row["items_excluded"] = total_excluded
    row["absolute_pct"] = round(100 * total_weighted / total_max, 1) if total_max > 0 else 0.0
    row["applicable_pct"] = round(100 * total_weighted / applicable_max, 1) if applicable_max > 0 else 0.0
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
    total_w, total_m, total_r = compute_total_score(assessment["items"])
    applicable_m = total_m - verdicts["not_applicable"]
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
        "weighted_score": round(total_w, 2),
        "max_score": total_m,
        "absolute_pct": round(100 * total_w / total_m, 1) if total_m > 0 else 0.0,
        "applicable_pct": round(100 * total_w / applicable_m, 1) if applicable_m > 0 else 0.0,
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

    # Build category list with their item IDs for score breakdown
    categories = []
    for c in checklist["categories"]:
        cat_item_ids = [it["id"] for it in checklist["items"] if it["category"] == c["id"]]
        categories.append({"id": c["id"], "name": c["name"], "item_ids": cat_item_ids})

    assessments = collect_assessments(args.runs_root, args.mode)
    if not assessments:
        print(f"No assessment.json found under {args.runs_root}", file=sys.stderr)
        return 0

    matrix_rows = [build_matrix_row(a, item_ids) for _, a in assessments]
    summary_rows = [build_summary_row(a) for _, a in assessments]
    score_rows = [build_score_row(a, categories) for _, a in assessments]

    matrix_fields = ["product_id", "vendor", "product_name", "mode", "checklist_version", "assessed_at"]
    for iid in item_ids:
        matrix_fields.extend([iid, f"{iid}_conf", f"{iid}_ev"])

    summary_fields = list(summary_rows[0].keys())

    # Score fields: product info + per-category columns + totals
    score_fields = ["product_id", "vendor", "product_name", "mode"]
    for cat in categories:
        score_fields.extend([f"{cat['id']}_weighted", f"{cat['id']}_max", f"{cat['id']}_raw"])
    score_fields.extend(["total_weighted", "total_max", "total_raw", "items_excluded", "absolute_pct", "applicable_pct"])

    matrix_path = args.out_dir / "comparison_matrix.csv"
    summary_path = args.out_dir / "coverage_summary.csv"
    score_path = args.out_dir / "product_scores.csv"
    write_csv(matrix_path, matrix_rows, matrix_fields)
    write_csv(summary_path, summary_rows, summary_fields)
    write_csv(score_path, score_rows, score_fields)

    print(f"Wrote {matrix_path} ({len(matrix_rows)} products, {len(item_ids)} items)")
    print(f"Wrote {summary_path}")
    print(f"Wrote {score_path} ({len(categories)} categories: {', '.join(c['name'] for c in categories)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
