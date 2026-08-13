# Product Assessment: {VENDOR} - {PRODUCT_NAME}

<!--
This template REPLACES the default deep-research report_template.md for this project.
Anti-fabrication rules from the parent skill still apply:
  - Every factual claim needs an inline [N] citation.
  - Bibliography lists every [N] used.
  - No placeholders. If unknown, say unknown.
Verdict semantics live in ../schemas/assessment.schema.json.
The MACHINE-READABLE truth is assessment.json - this prose is derived from it.
-->

**Product ID:** `{product_id}`
**Version reference:** {product_version_reference | "n/a"}
**Assessment mode:** {standard | deep}
**Checklist version:** {N}
**Assessed at:** {YYYY-MM-DD}
**Total evidence items collected:** {N}
**Total distinct sources:** {N}

---

## 1. Overview (≤ 200 words)

[One paragraph describing what the product is, how the vendor positions it in this domain, and the deployment shapes it supports. Cited. No marketing adjectives.]

---

## 2. Verdict Summary

**Counts across {N} checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        |       |                  |        |     |
| partial          |       |                  |        |     |
| not_supported    |       |                  |        |     |
| unknown          |       |                  |        |     |
| not_applicable   |       |                  |        |     |

**Evidence quality:** {N} items backed by ≥ 2 source_types; {N} items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

<!--
One row per item in checklist.yaml (in ID order). Do not skip items.
- Verdict badges (plain text, no icons): Supported, Partial, Not Supported, Unknown, N/A
- "Evidence" cell cites source numbers [N] tied to the Bibliography.
- If verdict = unknown, the Evidence cell says "no evidence found" - never a fabricated citation.
- For numeric_threshold items, the Evidence cell MUST include the measured value + unit.
-->

### Category 1

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | [Requirement wording] | Supported | high | - | [1] |

<!-- Repeat one table per category. Item order MUST match checklist.yaml. -->

---

## 4. Notable Strengths

[3-5 short bullets. Each bullet ties to specific item IDs and a citation. No hyperbole.]

- **{Capability name} (items {X.Y}, {X.Z}):** [one sentence, cited]

## 5. Notable Gaps / Risks

[3-5 short bullets. Include items marked partial/not_supported/unknown that are load-bearing for the buyer's use case.]

- **{Gap name} (item {X.Y}):** [one sentence describing the gap and what would resolve it]

## 6. Evidence Quality Notes

[1-2 paragraphs describing:
- How many items were triangulated across ≥ 3 independent sources vs single-source
- Which items relied only on vendor documentation and why that matters
- Any items where sources contradicted each other, and how the verdict was chosen]

---

## Bibliography

<!--
Every [N] used above must have an entry here.
Format: [N] Author/Organization (Year). "Title". Publication. URL (Retrieved: YYYY-MM-DD)
Source IDs (16-hex) live in sources.jsonl - this list is the human-readable projection.
-->

[1] ...
[2] ...

---

## Appendix A - Methodology

- **Research mode used:** {standard | deep}
- **Queries executed:** {N}
- **Sources reviewed:** {N} (kept: {N}, discarded for low credibility: {N})
- **Source_types distribution:** {vendor_doc: N, analyst_report: N, third_party_review: N, ...}
- **Verify script results:** claim-support pass, citation pass

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
