# Standard-mode prompt template

Full 24-item deep pass. Only run this on products that came out of screen mode
with `gate_decision.recommendation == "advance-to-deep"` (see
`bsg/decisions/deep_queue.txt`).

Fill in `{VENDOR}`, `{PRODUCT_NAME}`, `{product_id}` and paste into a Claude Code session:

---

```
Use the deep-research skill in STANDARD mode to assess ONE product against
the FULL bsg checklist (all 24 items).

  Vendor:       {VENDOR}
  Product:      {PRODUCT_NAME}
  product_id:   {product_id}

Follow the project's output contract in
d:/vcs/provider-screening/bsg/GUIDE.md - it OVERRIDES the
skill's default report_template.md.

1. CHECKLIST
   Read d:/vcs/provider-screening/bsg/checklist.yaml.
   Assess EVERY item (all 24 across 5 categories). Order by category:
     1. Architecture & Security             (1.1 - 1.5)
     2. Inspection & CDR Engine             (2.1 - 2.7)
     3. Protocol Support                    (3.1 - 3.4)
     4. Performance & High Availability     (4.1 - 4.4)
     5. Management & Compliance             (5.1 - 5.4)
   If the screen-mode assessment already exists at
   runs/{product_id}/assessment.json, treat it as prior evidence - you may
   REUSE its evidence_ids / cited_source_ids for items 1.1, 1.3, 2.1, 3.2,
   4.4, 5.2 but should re-verify against fresh queries and refine any
   `unknown` verdicts if new evidence surfaces.

2. OUTPUT LOCATION
   Put ALL outputs in
     d:/vcs/provider-screening/bsg/runs/{product_id}/
   Files (screen artifacts may already exist here - APPEND to sources.jsonl
   / evidence.jsonl / claims.jsonl, do not overwrite):
     - sources.jsonl, evidence.jsonl, claims.jsonl, run_manifest.json
     - assessment.json      (validated against schemas/assessment.schema.json;
                             REPLACE the screen version with the full 24-item one)
     - artifacts/           (raw PDFs staged there via the helper - see step 4)

   Do NOT hand-write report.md. After assessment.json validates (step 9), run:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/bsg/scripts/render_report.py \
       d:/vcs/provider-screening/bsg/runs/{product_id}/assessment.json
   This generates report.md's mechanical sections (header, verdict tables,
   bibliography, appendix) straight from assessment.json/sources.jsonl - they
   can never drift from the data that way. It leaves 4 narrative sections as
   template placeholders for you to fill by hand, then re-run the same command
   to merge your prose back in (it preserves those 4 sections verbatim on
   every subsequent run, so re-running after fixing assessment.json is safe):
     1. Overview, 4. Notable Strengths, 5. Notable Gaps / Risks,
     6. Evidence Quality Notes
   See templates/product_report.md for what belongs in each. No icons/emoji
   in report.md - plain text verdict labels only (Supported/Partial/etc.).

3. SCHEMA FIXED FIELDS
   assessment.json MUST have:
     assessment_mode   = "standard"
     checklist_version = 1
     product_id        = "{product_id}"
   One entry per checklist item; item_ids match the checklist exactly.
   ALL 24 items must be present - validator rejects partial coverage.

4. PDF HANDLING (mandatory when a source is a PDF)
   WebFetch cannot read PDF binaries. When a relevant source is a PDF:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/scripts/pdf_to_text.py <pdf-url> \
       --product {product_id} --domain bsg
   This stages the raw PDF into runs/{product_id}/artifacts/<slug>.pdf,
   writes the extracted text to <slug>.txt, and appends a manifest.jsonl
   entry with the URL, sha256, page count, and timestamp.
   Then Read the .txt (last line of the script's stdout is its absolute path).
   Citation etiquette:
     - sources.jsonl.raw_url  → the ORIGINAL PDF URL (not the local artifact path)
     - evidence.jsonl.locator → include the page, e.g. "page 3, 'throughput' section"

5. NUMERIC-THRESHOLD ITEMS (extra requirement over screen)
   Items with `verdict_type: numeric_threshold` in checklist.yaml are:
     4.1  processing throughput
     4.2  processing / realtime protocol latency
     4.3  HA failover switchover time
   For each, read the exact `threshold.op` / `threshold.value` / `threshold.unit`
   from checklist.yaml itself - do not rely on any value repeated in this
   prompt, which may drift out of sync with the checklist over time.
   assessment.json MUST include for each:
     numeric_value : the ACTUAL number cited (or measured) - no rounding to the
                     requirement threshold, no fabrication.
     unit          : must exactly match checklist.yaml threshold.unit
   If sources give only qualitative language ("high throughput", "low latency"):
     verdict       = "partial"
     numeric_value = null
     notes         = explain the imprecision
   If no source mentions the metric at all:
     verdict       = "unknown"  (empty evidence, as always)

6. PRODUCT CLASS AWARENESS (BSG-specific)
   providers/BSG.csv mixes high-assurance Cross Domain Solutions /
   protocol-break guards with ruggedized industrial NGFWs. The most
   guard/CDS-specific items - 1.1 (protocol break), 1.2 (hardware isolation),
   1.5 (internal data stamping), 2.1 (CDR), 2.4 (schema validation), 2.5
   (IFC/security labels), 2.7 (anti-steganography) - may legitimately be
   "not_applicable" for a firewall-class product - but ONLY when a source
   establishes the product's category (e.g. vendor markets it as a standard
   NGFW, not a guard/diode). Do not default to not_applicable without that
   citation; the default for "not discussed" is always "unknown".

7. ANTI-FABRICATION (validator enforces these, non-negotiable)
   - `unknown` verdict when no evidence found. Unknown items must have
     empty evidence_ids / cited_source_ids / source_types. Never invent
     `not_supported` from silence.
   - Non-unknown verdicts REQUIRE non-empty evidence_ids, cited_source_ids,
     and source_types (tags from GUIDE.md § "Source type taxonomy").
   - If source_types are only vendor_doc / vendor_datasheet / vendor_blog,
     `confidence` is capped at "medium" - "high" requires >= 1 independent
     source (analyst_report, third_party_review, certification_registry, etc.).
   - `notes` <= 2 sentences, paraphrase of cited evidence only. No
     cross-product comparison in notes.

8. SOURCE PREFERENCE
   Deep pass is where triangulation matters: aim for >= 3 sources per item
   with at least 1 non-vendor source when possible. Cover item 5.4
   (certifications) with regulator/registry sources where applicable
   (NCDSMO Baseline / Raise the Bar, Common Criteria portal, BSI Germany,
   ANSSI France, NIST CMVP / FIPS validation list, or the national "Chứng
   nhận Cơ yếu" registry where applicable).

9. VALIDATE
   After generating everything, run:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/bsg/scripts/validate_assessment.py \
       d:/vcs/provider-screening/bsg/runs/{product_id}/assessment.json \
       --evidence-store d:/vcs/provider-screening/bsg/runs/{product_id}
   If it fails, fix assessment.json in place. NEVER fabricate evidence to
   pass - downgrade verdicts to `unknown` instead and re-run.
   Note: gate_decision is NOT required for standard mode (only for screen).

   Once it passes, run render_report.py (see step 2) to produce report.md.
   First pass leaves the 4 narrative sections as template placeholders - Edit
   report.md to write those 4 sections, then run render_report.py again to
   regenerate the mechanical sections cleanly while keeping your prose.
```

---

## Differences from screen mode

| Concern              | Screen                              | Standard                                           |
|-----------------------|-------------------------------------|-----------------------------------------------------|
| Item coverage         | 6 items with `screen: true`         | All 24 items                                         |
| `assessment_mode`     | `"screen"`                          | `"standard"`                                        |
| Report template       | `screening_report.md`               | `product_report.md`                                 |
| Numeric thresholds    | Not enforced (no such items)        | Required for 3 items (4.1, 4.2, 4.3)                 |
| `gate_decision`       | REQUIRED (drives promotion bucket)  | Optional (no early-stopping yet - see GUIDE.md)      |
| Prior screen results  | N/A                                  | REUSE evidence for the 6 gate items where possible   |
