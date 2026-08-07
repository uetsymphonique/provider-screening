"""Validate one product assessment.json against schema + checklist-aware rules.

Usage:
    python validate_assessment.py <path/to/assessment.json>
        [--checklist bsg/checklist.yaml]
        [--schema bsg/schemas/assessment.schema.json]
        [--evidence-store <dir>]   # optional: cross-check evidence_ids

Exit code 0 = pass, 1 = validation errors (printed to stderr).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import jsonschema
import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CHECKLIST = REPO_ROOT / "bsg" / "checklist.yaml"
DEFAULT_SCHEMA = REPO_ROOT / "bsg" / "schemas" / "assessment.schema.json"


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


def compute_default_recommendation(items: list[dict]) -> str:
    """Rule-based baseline. Priority: drop > needs-more-info > advance-to-deep.

    - drop            if any item.verdict == "not_supported"
    - needs-more-info if unknown_count >= 3   (half the 6 gates missing)
    - advance-to-deep otherwise
    """
    verdicts = [it.get("verdict") for it in items]
    if any(v == "not_supported" for v in verdicts):
        return "drop"
    if sum(1 for v in verdicts if v == "unknown") >= 3:
        return "needs-more-info"
    return "advance-to-deep"


def check_gate_decision(assessment: dict) -> list[str]:
    """Validate assessment.gate_decision block against the rule engine.

    Only applies when assessment_mode == 'screen'.
    """
    errors: list[str] = []
    if assessment.get("assessment_mode") != "screen":
        return errors

    gd = assessment.get("gate_decision")
    if not gd:
        errors.append(
            "gate_decision: required when assessment_mode='screen' "
            "(must include recommendation + rationale; see schema)"
        )
        return errors

    default = compute_default_recommendation(assessment.get("items", []))
    provided_default = gd.get("default_recommendation")
    if provided_default is not None and provided_default != default:
        errors.append(
            f"gate_decision.default_recommendation={provided_default!r} "
            f"disagrees with rule engine (expected={default!r}). "
            "Do not hand-set default_recommendation; leave it null or match the rule."
        )

    recommendation = gd.get("recommendation")
    override_reason = (gd.get("override_reason") or "").strip()
    if recommendation != default and not override_reason:
        errors.append(
            f"gate_decision.recommendation={recommendation!r} differs from "
            f"rule-based default={default!r} — override_reason is REQUIRED."
        )
    if recommendation == default and override_reason:
        errors.append(
            "gate_decision.override_reason present but recommendation matches default; "
            "clear override_reason to avoid confusion."
        )
    return errors


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

    # Coverage rule per mode
    mode = assessment["assessment_mode"]
    required_ids: set[str]
    if mode == "screen":
        required_ids = {it["id"] for it in checklist["items"] if it.get("screen")}
    else:
        required_ids = set(checklist_items.keys())

    provided_ids = {it["item_id"] for it in assessment["items"]}
    missing = required_ids - provided_ids
    if missing:
        errors.append(
            f"mode={mode!r} requires items {sorted(required_ids)}; "
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
    ap.add_argument("--checklist", type=Path, default=DEFAULT_CHECKLIST)
    ap.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    ap.add_argument(
        "--evidence-store",
        type=Path,
        default=None,
        help="Directory containing sources.jsonl + evidence.jsonl for cross-check.",
    )
    args = ap.parse_args()

    schema = load_json(args.schema)
    checklist = load_yaml(args.checklist)
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
    gate_errors = check_gate_decision(assessment)

    all_errors = schema_errors + rule_errors + gate_errors
    if all_errors:
        print(f"FAIL {args.assessment} ({len(all_errors)} errors)", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    default = compute_default_recommendation(assessment["items"])
    gd = assessment.get("gate_decision") or {}
    rec = gd.get("recommendation") or "-"
    override_note = " (OVERRIDE)" if rec != default and rec != "-" else ""
    print(
        f"OK   {args.assessment} ({len(assessment['items'])} items, "
        f"mode={assessment['assessment_mode']}, gate={rec}{override_note}, default={default})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
