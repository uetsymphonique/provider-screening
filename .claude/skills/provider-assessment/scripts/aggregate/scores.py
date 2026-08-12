"""Scoring domain logic for checklist item and product evaluation."""

from __future__ import annotations

from collections import Counter


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


def build_score_row(assessment: dict, categories: list[dict], include_applicable: bool = False) -> dict[str, object]:
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
    row["total_weighted"] = round(total_weighted, 2)
    row["total_max"] = total_max
    row["total_raw"] = round(total_raw, 2)
    row["items_excluded"] = total_excluded
    row["absolute_pct"] = round(100 * total_weighted / total_max, 1) if total_max > 0 else 0.0
    if include_applicable:
        applicable_max = total_max - total_excluded
        row["applicable_pct"] = round(100 * total_weighted / applicable_max, 1) if applicable_max > 0 else 0.0
    return row


def build_raw_row(
    assessment: dict, categories: list[dict], cat_headers: dict[str, str], total_header: str
) -> dict[str, object]:
    """Per-category raw score row (like weighted but shows raw scores)."""
    score_row = build_score_row(assessment, categories)
    row: dict[str, object] = {
        "Product ID": assessment["product_id"],
        "Vendor": assessment["vendor"],
        "Product Name": assessment["product_name"],
    }
    for cat in categories:
        row[cat_headers[cat["id"]]] = score_row[f"{cat['id']}_raw"]
    row[total_header] = score_row["total_raw"]
    return row


def build_weighted_row(
    assessment: dict, categories: list[dict], cat_headers: dict[str, str], total_header: str,
    include_applicable: bool = False,
) -> dict[str, object]:
    """Simplified per-category row with weighted score only (see build_score_row for raw/max)."""
    score_row = build_score_row(assessment, categories, include_applicable)
    row: dict[str, object] = {
        "Product ID": assessment["product_id"],
        "Vendor": assessment["vendor"],
        "Product Name": assessment["product_name"],
    }
    for cat in categories:
        row[cat_headers[cat["id"]]] = score_row[f"{cat['id']}_weighted"]
    row[total_header] = score_row["total_weighted"]
    row["Weighted %"] = score_row["absolute_pct"]
    if include_applicable:
        row["Weighted Applicable %"] = score_row["applicable_pct"]
    return row


def build_summary_row(assessment: dict, include_applicable: bool = False) -> dict[str, object]:
    verdicts = Counter(it["verdict"] for it in assessment["items"])
    total_w, total_m, total_r = compute_total_score(assessment["items"])
    applicable_m = total_m - verdicts["not_applicable"]
    row: dict[str, object] = {
        "Product ID": assessment["product_id"],
        "Vendor": assessment["vendor"],
        "Product Name": assessment["product_name"],
        "Supported": verdicts["supported"],
        "Partial": verdicts["partial"],
        "Not Supported": verdicts["not_supported"],
        "Unknown": verdicts["unknown"],
        "Not Applicable": verdicts["not_applicable"],
        f"Raw Score (max {total_m})": round(total_r, 2),
        f"Weighted Score (max {total_m})": round(total_w, 2),
        "Absolute %": round(100 * total_w / total_m, 1) if total_m > 0 else 0.0,
    }
    if include_applicable:
        row["Applicable %"] = round(100 * total_w / applicable_m, 1) if applicable_m > 0 else 0.0
    return row
