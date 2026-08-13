"""Validate one product assessment.json against schema + checklist-aware rules.

Shared across domains (bsg, microsegmentation, ...). The domain's checklist.yaml
and runs/ tree are resolved from --domain.

Usage:
    python .claude/skills/provider-assessment/scripts/validate_assessment.py \
        --domain bsg <path/to/assessment.json>
        [--checklist <path>]            # default: providers-workspace/<domain>/checklist.yaml
        [--schema <path>]               # default: skill schemas/assessment.schema.json
        [--evidence-store <dir>]        # optional: cross-check evidence_ids

Exit code 0 = pass, 1 = validation errors (printed to stderr).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import jsonschema
import yaml

try:
    from .constants import DOMAINS, SKILL_ROOT, domain_paths
except ImportError:
    _parent = Path(__file__).resolve().parent
    sys.path.insert(0, str(_parent))
    from constants import DOMAINS, SKILL_ROOT, domain_paths  # type: ignore[no-redef]


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_evidence_ids(store_dir: Path) -> tuple[set[str], set[str]]:
    """Return (evidence_ids, source_ids) found in a run directory."""
    evidence_ids: set[str] = set()
    source_ids: set[str] = set()

    ev = store_dir / "evidence.jsonl"
    if ev.exists():
        for line in ev.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if "evidence_id" in row:
                evidence_ids.add(row["evidence_id"])

    src = store_dir / "sources.jsonl"
    if src.exists():
        for line in src.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if "source_id" in row:
                source_ids.add(row["source_id"])

    return evidence_ids, source_ids


def check_custom_rules(
    assessment: dict,
    checklist: dict,
    evidence_ids: set[str] | None,
    source_ids: set[str] | None,
) -> list[str]:
    errors: list[str] = []

    checklist_items = {it["id"]: it for it in checklist["items"]}
    checklist_version = checklist["meta"]["version"]

    # Version pin
    if assessment.get("checklist_version") != checklist_version:
        errors.append(
            f"checklist_version mismatch: assessment={assessment.get('checklist_version')} "
            f"vs checklist.yaml meta.version={checklist_version}"
        )

    # Coverage: all checklist items must be present
    required_ids = set(checklist_items.keys())
    provided_ids = {it["item_id"] for it in assessment["items"]}
    missing = required_ids - provided_ids
    if missing:
        errors.append(
            f"assessment requires all {len(required_ids)} checklist items; "
            f"missing from assessment: {sorted(missing)}"
        )

    # Unknown items (ids not in checklist)
    unknown = provided_ids - set(checklist_items.keys())
    if unknown:
        errors.append(f"assessment references item_ids not in checklist: {sorted(unknown)}")

    # Per-item rules
    for item in assessment["items"]:
        iid = item["item_id"]
        prefix = f"item {iid}:"
        checklist_item = checklist_items.get(iid)
        if not checklist_item:
            continue  # already reported above

        verdict = item["verdict"]
        confidence = item["confidence"]
        evidence_list = item.get("evidence_ids", [])
        source_list = item.get("cited_source_ids", [])
        source_types = item.get("source_types", [])

        # Evidence presence
        if verdict != "unknown":
            if not evidence_list:
                errors.append(f"{prefix} verdict={verdict!r} requires non-empty evidence_ids")
            if not source_list:
                errors.append(f"{prefix} verdict={verdict!r} requires non-empty cited_source_ids")
            if not source_types:
                errors.append(f"{prefix} verdict={verdict!r} requires non-empty source_types")
        else:
            # unknown MUST NOT smuggle claims
            if evidence_list or source_list:
                errors.append(
                    f"{prefix} verdict='unknown' must have empty evidence_ids and cited_source_ids"
                )

        # not_applicable is only legitimate on items the checklist marks eligible
        if verdict == "not_applicable" and "not_applicable_class" not in checklist_item:
            errors.append(
                f"{prefix} verdict='not_applicable' but checklist item has no "
                f"not_applicable_class - not_applicable is not a legitimate verdict "
                f"for this item (see GUIDE.md rule 7)"
            )

        # Vendor-doc cap on confidence
        vendor_only = source_types and all(
            st in {"vendor_doc", "vendor_datasheet", "vendor_blog"} for st in source_types
        )
        if vendor_only and confidence == "high":
            errors.append(
                f"{prefix} confidence='high' not allowed when source_types are vendor-only "
                f"({source_types}); cap at 'medium'"
            )

        # Numeric-threshold obligations
        if checklist_item.get("verdict_type") == "numeric_threshold":
            threshold = checklist_item.get("threshold") or {}
            numeric_value = item.get("numeric_value")
            if verdict in {"supported", "not_supported"} and numeric_value is None:
                errors.append(
                    f"{prefix} numeric_threshold item requires numeric_value when verdict={verdict!r} "
                    f"(threshold={threshold})"
                )
            elif verdict == "partial" and numeric_value is None and not (item.get("notes") or "").strip():
                errors.append(
                    f"{prefix} verdict='partial' with numeric_value=null requires non-empty notes "
                    f"explaining the qualitative/imprecise evidence"
                )
            if numeric_value is not None and item.get("unit") != threshold.get("unit"):
                errors.append(
                    f"{prefix} unit {item.get('unit')!r} does not match checklist unit "
                    f"{threshold.get('unit')!r}"
                )

        # Cross-check against evidence store if provided
        if evidence_ids is not None:
            for eid in evidence_list:
                if eid not in evidence_ids:
                    errors.append(f"{prefix} evidence_id {eid} not found in evidence.jsonl")
        if source_ids is not None:
            for sid in source_list:
                if sid not in source_ids:
                    errors.append(f"{prefix} source_id {sid} not found in sources.jsonl")

    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("assessment", type=Path)
    ap.add_argument("--domain", required=True, choices=list(DOMAINS))
    ap.add_argument("--checklist", type=Path, default=None)
    ap.add_argument("--schema", type=Path, default=None)
    ap.add_argument(
        "--evidence-store",
        type=Path,
        default=None,
        help="Directory containing sources.jsonl + evidence.jsonl for cross-check.",
    )
    args = ap.parse_args()

    paths = domain_paths(args.domain)
    checklist_path = args.checklist or paths["checklist"]
    schema_path = args.schema or (SKILL_ROOT / "schemas" / "assessment.schema.json")

    schema = load_json(schema_path)
    checklist = load_yaml(checklist_path)
    assessment = load_json(args.assessment)

    schema_errors: list[str] = []
    validator = jsonschema.Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(assessment), key=lambda e: e.path):
        loc = "/".join(str(p) for p in err.absolute_path) or "<root>"
        schema_errors.append(f"schema {loc}: {err.message}")

    evidence_ids = source_ids = None
    if args.evidence_store:
        evidence_ids, source_ids = load_evidence_ids(args.evidence_store)

    rule_errors = check_custom_rules(assessment, checklist, evidence_ids, source_ids)

    all_errors = schema_errors + rule_errors
    if all_errors:
        print(f"FAIL {args.assessment} ({len(all_errors)} errors)", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print(
        f"OK   {args.assessment} ({len(assessment['items'])} items, "
        f"mode={assessment['assessment_mode']})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
