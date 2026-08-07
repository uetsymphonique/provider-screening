# Microsegmentation Screening: {VENDOR} - {PRODUCT_NAME}

<!--
QUICK-SCREEN template. Purpose: fast gate to decide whether to spend a
standard/deep pass on this vendor. Only items with screen:true in checklist.yaml
are assessed here. Anti-fabrication rules from the parent skill apply.
Machine-readable truth is assessment.json (mode = "screen").
-->

**Product ID:** `{product_id}`
**Mode:** screen
**Assessed at:** {YYYY-MM-DD}
**Checklist version:** {N}

---

## Gate Decision

<!--
Derived from assessment.json → gate_decision. The RULE-BASED default is computed
by validate_assessment.py:
  - drop            if any item.verdict == "not_supported"
  - needs-more-info if unknown_count >= 3
  - advance-to-deep otherwise
If the agent's recommendation differs from the default, gate_decision.override_reason
MUST be non-empty (validator fails otherwise). Render override_reason below only
when present.
-->

**Rule-based default:** {advance-to-deep | drop | needs-more-info}
**Recommendation:** {advance-to-deep | drop | needs-more-info}   *(matches default | OVERRIDE)*

**Rationale (≤ 3 sentences):** [Why this recommendation, tied to specific gate items and citations.]

<!-- Only when recommendation != default -->
**Override reason:** [Why the model diverged from the rule-based default.]

---

## Gate Item Verdicts

<!-- Only items with screen:true in checklist.yaml. Order matches checklist. -->

| ID  | Requirement (short) | Verdict | Conf | Evidence |
|-----|---------------------|:-------:|:----:|----------|
| 1.1 | Real-time auto-discovery | | | |
| 2.1 | Tag/Identity-based policy | | | |
| 3.2 | Container / K8s / OpenShift | | | |
| 4.4 | Agent fail-safe | | | |
| 5.1 | Full REST API | | | |
| 6.4 | TLS 1.3 / mutual auth | | | |

Verdict badges (plain text, no icons): Supported · Partial · Not Supported · Unknown

---

## What was NOT investigated

Screen mode skips the remaining {N} checklist items. See `../schemas/assessment.schema.json` for the full set. Do not assume unassessed items are unsupported.

---

## Bibliography

[1] ...
[2] ...

---

## Machine-readable outputs

- `assessment.json` (mode = "screen") - validator applies the same rules; missing gate items = validation error
- `sources.jsonl`, `evidence.jsonl` - inherited from deep-research skill
