"""Comparison matrix: transposed with items as rows and top-10 products as columns."""

from __future__ import annotations

import sys
from pathlib import Path

# Support both direct execution and package import
try:
    from ..constants import VERDICT_LABEL
except ImportError:
    _scripts = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(_scripts))
    from constants import VERDICT_LABEL  # type: ignore[no-redef]


def build_transposed_matrix(
    top10: list[tuple[float, Path, dict]],
    checklist_items: list[dict],
    categories: list[dict],
) -> tuple[list[dict[str, str]], list[str]]:
    """Build transposed comparison matrix: rows = items (grouped by category), columns = products."""
    product_verdicts: dict[str, dict[str, str]] = {}
    product_ids = []
    for _, _, a in top10:
        pid = a["product_id"]
        product_ids.append(pid)
        per_item = {it["item_id"]: it for it in a["items"]}
        product_verdicts[pid] = {}
        for item in checklist_items:
            iid = item["id"]
            entry = per_item.get(iid)
            if entry is None:
                product_verdicts[pid][iid] = ""
            else:
                product_verdicts[pid][iid] = VERDICT_LABEL.get(entry["verdict"], "?")

    rows: list[dict[str, str]] = []
    for item in checklist_items:
        cat_name = next((c["name"] for c in categories if c["id"] == item["category"]), "")
        row: dict[str, str] = {
            "category": cat_name,
            "item_id": item["id"],
            "requirement": item["requirement"],
        }
        for pid in product_ids:
            row[pid] = product_verdicts[pid][item["id"]]
        rows.append(row)

    fields = ["category", "item_id", "requirement"] + product_ids
    return rows, fields
