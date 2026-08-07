# Screen-mode prompt template

Fill in `{VENDOR}`, `{PRODUCT_NAME}`, `{product_id}` (slug from `providers/Microsegmentation.csv`) and paste into a Claude Code session:

---

```
Use the deep-research skill in QUICK mode to assess ONE product:

  Vendor:       {VENDOR}
  Product:      {PRODUCT_NAME}
  product_id:   {product_id}

Follow the project's output contract in
d:/vcs/provider-screening/microsegmentation/GUIDE.md — it OVERRIDES the
skill's default report_template.md.

1. CHECKLIST
   Read d:/vcs/provider-screening/microsegmentation/checklist.yaml.
   For screen mode, only assess items with `screen: true`:
     1.1, 2.1, 3.2, 4.4, 5.1, 6.4

2. OUTPUT LOCATION
   Put ALL outputs in
     d:/vcs/provider-screening/microsegmentation/runs/{product_id}/
   Files:
     - sources.jsonl, evidence.jsonl, claims.jsonl, run_manifest.json  (from the skill)
     - assessment.json      (validated against schemas/assessment.schema.json)
     - artifacts/           (raw PDFs staged there via the helper — see step 4)

   Do NOT hand-write report.md — it is fully generated from assessment.json
   by scripts/render_report.py (step 7 below); screen mode has no free-text
   sections to author.

3. SCHEMA FIXED FIELDS
   assessment.json MUST have:
     assessment_mode  = "screen"
     checklist_version = 1
     product_id       = "{product_id}"
   One entry per screen item; item_ids match the checklist exactly.

4. PDF HANDLING (mandatory when a source is a PDF)
   WebFetch cannot read PDF binaries. When a relevant source is a PDF:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/scripts/pdf_to_text.py <pdf-url> \
       --product {product_id}
   This stages the raw PDF into runs/{product_id}/artifacts/<slug>.pdf,
   writes the extracted text to <slug>.txt, and appends a manifest.jsonl
   entry with the URL, sha256, page count, and timestamp.
   Then Read the .txt (last line of the script's stdout is its absolute path).
   Citation etiquette:
     - sources.jsonl.raw_url  → the ORIGINAL PDF URL (not the local artifact path)
     - evidence.jsonl.locator → include the page, e.g. "page 3, 'Kubernetes' section"

5. ANTI-FABRICATION (validator enforces these, non-negotiable)
   - `unknown` verdict when no evidence found. Unknown items must have
     empty evidence_ids / cited_source_ids / source_types. Never invent
     `not_supported` from silence.
   - Non-unknown verdicts REQUIRE non-empty evidence_ids, cited_source_ids,
     and source_types (tags from GUIDE.md § "Source type taxonomy").
   - If source_types are only vendor_doc / vendor_datasheet / vendor_blog,
     `confidence` is capped at "medium" — "high" requires ≥ 1 independent
     source (analyst_report, third_party_review, peer_reviewed, etc.).
   - `notes` ≤ 2 sentences, paraphrase of cited evidence only. No
     cross-product comparison in notes.

6. SOURCE PREFERENCE
   Prefer independent sources over vendor marketing. Vendor docs are fine
   to cite but must be tagged accurately.

7. VALIDATE
   After generating everything, run:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/microsegmentation/scripts/validate_assessment.py \
       d:/vcs/provider-screening/microsegmentation/runs/{product_id}/assessment.json \
       --evidence-store d:/vcs/provider-screening/microsegmentation/runs/{product_id}
   If it fails, fix assessment.json in place. NEVER fabricate evidence to
   pass — downgrade verdicts to `unknown` instead and re-run.

   Once it passes, generate report.md:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/microsegmentation/scripts/render_report.py \
       d:/vcs/provider-screening/microsegmentation/runs/{product_id}/assessment.json

8. GATE DECISION (structured, rule-checked)
   Populate assessment.gate_decision (validator enforces both structure and
   agreement with the rule engine):

     gate_decision.recommendation      → one of {advance-to-deep, drop, needs-more-info}
     gate_decision.rationale           → ≤ 3 sentences citing specific item IDs
     gate_decision.default_recommendation → leave null (validator fills / checks)
     gate_decision.override_reason     → REQUIRED (non-empty) IFF recommendation
                                          differs from the rule-based default;
                                          otherwise omit / null.

   Rule the validator applies (priority order):
     drop            ← ANY item.verdict == "not_supported"
     needs-more-info ← unknown_count >= 3
     advance-to-deep ← otherwise

   Only diverge from the default when evidence context genuinely warrants it
   (e.g. the single `not_supported` came from a stale 2019 doc contradicted
   by a 2025 release note in the same evidence set — say so in
   override_reason). Do NOT override to make the vendor look better.

   The report.md's "Gate Decision" section is derived from these fields.
```

---

For the deep pass (all 33 items), see [`standard_mode.md`](./standard_mode.md).
