---
name: provider-assessment
description: Use when scoring one or more vendor products against a structured checklist with evidence-cited verdicts (supported/partial/not_supported/unknown/not_applicable), validating assessment.json, rendering per-product report.md, or aggregating many products into a comparison matrix. Shared machinery across domains (bsg, microsegmentation, ...). Not for the raw research phase itself - use the deep-research skill for that; this skill consumes its sources.jsonl/evidence.jsonl output.
---

# Provider Assessment

Structured, checklist-driven vendor screening built on top of the
[`deep-research`](../deep-research/) skill. For a given **domain** (a folder
under `providers-workspace/`, like `providers-workspace/bsg/` or
`providers-workspace/microsegmentation/`, with its own `checklist.yaml`),
every product is scored against the same items and aggregated into one
comparison matrix.

The MACHINE-READABLE truth is `assessment.json` (validated against
`schema`); `report.md` and `comparison_matrix.xlsx` are derived from it.

## When to use

- Scoring ONE product against a domain's `checklist.yaml` (standard/deep mode).
- Validating an existing `assessment.json`.
- Rendering/regenerating a product's `report.md` from validated data.
- Aggregating all assessed products into `comparison_matrix.xlsx`.

## Do NOT use for

- The research/evidence-gathering itself - that is the `deep-research` skill.
- Cross-domain comparisons - each domain has its own checklist.

## Core workflow

Per product (one fresh agent session per vendor, no context leakage - `claude -p` or `pi --mode json`, see `scripts/batch/run_batch.py claude|pi`):

1. **Prompt** - paste the domain's standard-mode prompt
   (`.claude/skills/provider-assessment/prompts/standard_mode.md`) with
   `{DOMAIN}`, `{VENDOR}`, `{PRODUCT_NAME}`, `{product_id}` filled in. It
   drives: stage sources → write `assessment.json` → validate → render
   `report.md`.
2. **Validate** - `scripts/validate_assessment.py --domain <DOMAIN> <assessment.json>`
   Exit code 0 = pass. Fix in place; never fabricate evidence to pass.
3. **Grounding check** - `scripts/verify_citation_grounding.py --dir providers-workspace/<DOMAIN>/runs/<pid> --strict --require-staged`
   catches fabricated quotes the validator can't see.
4. **Render** - `scripts/render_report.py --domain <DOMAIN> <assessment.json>`
   generates report.md's mechanical sections; write the 4 narrative sections
   by hand, then re-run to merge.
5. **Aggregate** - `scripts/aggregate/aggregate_matrix.py --domain <DOMAIN> [--mode standard|deep|any]`
   produces `providers-workspace/<DOMAIN>/comparison_matrix.xlsx`.

## Scripts (shared; `--domain`, except `verify_citation_grounding.py` which takes `--dir`)

| Script | Purpose |
|---|---|
| `scripts/validate_assessment.py` | Schema + checklist-aware validation (coverage, evidence presence, confidence caps, numeric thresholds, not_applicable rules) |
| `scripts/verify_citation_grounding.py` | Checks evidence.jsonl quotes against staged source text (`--dir`, not `--domain`); catches fabricated quotes validation can't see |
| `scripts/render_report.py` | Regenerates report.md's mechanical sections from assessment.json (never drifts) |
| `scripts/aggregate/aggregate_matrix.py` | Multi-sheet xlsx: Legend, Comparison Matrix, Coverage Summary, Raw/Weighted Scores, top-10 product sheets |
| `scripts/batch/run_batch.py claude\|pi` (repo root) | Batch one-prompt-per-product runs over a vendor CSV; `--domain` + `--mode` required. One entrypoint, subcommand per code agent - shared driver in `scripts/batch/core/`, per-agent handler in `scripts/batch/core/handlers/` |

Per-domain checklist/guide/outputs stay in each domain folder under
`providers-workspace/` (`providers-workspace/bsg/checklist.yaml`,
`providers-workspace/microsegmentation/checklist.yaml`, ...). Only
`checklist.*`, `GUIDE.md`, `runs/`, and generated outputs live there - all
machinery is here.

## Source of truth for rules

See [`GUIDE.md`](./GUIDE.md) for the verdict contract, anti-fabrication rules,
workflow details, source-type taxonomy, and staging/citation etiquette. It is
the OVERRIDE for the deep-research skill's default report contract.
