# Standard-mode prompt template

Full 33-item deep pass. Only run this on products that came out of screen mode
with `gate_decision.recommendation == "advance-to-deep"` (see
`microsegmentation/decisions/deep_queue.txt`).

Fill in `{VENDOR}`, `{PRODUCT_NAME}`, `{product_id}` and paste into a Claude Code session:

---

```
Use the deep-research skill in STANDARD mode to assess ONE product against
the FULL microsegmentation checklist (all 33 items).

  Vendor:       {VENDOR}
  Product:      {PRODUCT_NAME}
  product_id:   {product_id}

Follow the project's output contract in
d:/vcs/provider-screening/microsegmentation/GUIDE.md — it OVERRIDES the
skill's default report_template.md.

1. CHECKLIST
   Read d:/vcs/provider-screening/microsegmentation/checklist.yaml.
   Assess EVERY item (all 33 across 8 categories). Order by category:
     1. Visibility & Mapping      (1.1 - 1.5)
     2. Policy Management         (2.1 - 2.5)
     3. Architecture & Support    (3.1 - 3.5)
     4. Performance & Impact      (4.1 - 4.5)
     5. Integration & Automation  (5.1 - 5.4)
     6. Security & Compliance     (6.1 - 6.4)
     7. High Availability         (7.1 - 7.3)
     8. Standards Certification   (8.1 - 8.2)
   If the screen-mode assessment already exists at
   runs/{product_id}/assessment.json, treat it as prior evidence — you may
   REUSE its evidence_ids / cited_source_ids for items 1.1, 2.1, 3.2, 4.4,
   5.1, 6.4 but should re-verify against fresh queries and refine any
   `unknown` verdicts if new evidence surfaces.

2. OUTPUT LOCATION
   Put ALL outputs in
     d:/vcs/provider-screening/microsegmentation/runs/{product_id}/
   Files (screen artifacts may already exist here — APPEND to sources.jsonl
   / evidence.jsonl / claims.jsonl, do not overwrite):
     - sources.jsonl, evidence.jsonl, claims.jsonl, run_manifest.json
     - assessment.json      (validated against schemas/assessment.schema.json;
                             REPLACE the screen version with the full 33-item one)
     - artifacts/           (raw PDFs staged there via the helper — see step 4)

   Do NOT hand-write report.md. After assessment.json validates (step 8), run:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/microsegmentation/scripts/render_report.py \
       d:/vcs/provider-screening/microsegmentation/runs/{product_id}/assessment.json
   This generates report.md's mechanical sections (header, verdict tables,
   bibliography, appendix) straight from assessment.json/sources.jsonl — they
   can never drift from the data that way. It leaves 4 narrative sections as
   template placeholders for you to fill by hand, then re-run the same command
   to merge your prose back in (it preserves those 4 sections verbatim on
   every subsequent run, so re-running after fixing assessment.json is safe):
     1. Overview, 4. Notable Strengths, 5. Notable Gaps / Risks,
     6. Evidence Quality Notes
   See templates/product_report.md for what belongs in each. No icons/emoji
   in report.md — plain text verdict labels only (Supported/Partial/etc.).

3. SCHEMA FIXED FIELDS
   assessment.json MUST have:
     assessment_mode   = "standard"
     checklist_version = 1
     product_id        = "{product_id}"
   One entry per checklist item; item_ids match the checklist exactly.
   ALL 33 items must be present — validator rejects partial coverage.

4. SOURCE STAGING (mandatory for EVERY cited source — PDF or web page)
   WebFetch either can't read the content at all (PDF binaries) or fetches
   AND summarizes through a small model in the same call (web pages) — either
   way nothing raw survives on disk, which is how fabricated quotes have
   slipped through before (validate_assessment.py only checks that an
   evidence_id/source_id exists, never that the quote is real). Before citing
   ANY source in sources.jsonl / evidence.jsonl, stage it first:

   PDF source:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/scripts/pdf_to_text.py <pdf-url> \
       --product {product_id} --domain microsegmentation
   Web page source:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/scripts/html_to_text.py <page-url> \
       --product {product_id} --domain microsegmentation

   Both stage the raw file into runs/{product_id}/artifacts/, write extracted
   text to <slug>.txt, and append an entry (URL, sha256, timestamp) to the
   SAME artifacts/manifest.jsonl. Then Read the .txt (last line of the
   script's stdout is its absolute path) — this is the ONLY text you may
   quote from. WebFetch is still fine for initial discovery/triage of which
   pages are worth staging, but the evidence quote itself must come from the
   staged .txt, never from WebFetch's summary. If the screen-mode assessment
   already staged a source for this product, reuse its artifacts/ instead of
   re-fetching.
   Citation etiquette:
     - sources.jsonl.raw_url  → the ORIGINAL URL (PDF or page), not the local
                                 artifact path — must match exactly what you
                                 passed to pdf_to_text.py / html_to_text.py
     - evidence.jsonl.locator → include the page for PDFs, e.g. "page 3,
                                 'Kubernetes' section"; a section heading for
                                 web pages, e.g. "Deployment options section"
     - evidence.jsonl.quote   → an EXACT substring of the staged .txt, not a
                                 paraphrase. If quoting two non-adjacent
                                 sentences, join them with " ... " so the gap
                                 is visible — never silently stitch text that
                                 wasn't contiguous in the source.

5. NUMERIC-THRESHOLD ITEMS (extra requirement over screen)
   Items with `verdict_type: numeric_threshold` in checklist.yaml are:
     1.3  connection history retention
     3.5  workloads per controller
     4.1  agent CPU overhead
     4.2  agent RAM footprint
     4.3  network policy latency
   For each, read the exact `threshold.op` / `threshold.value` / `threshold.unit`
   from checklist.yaml itself — do not rely on any value repeated in this
   prompt, which may drift out of sync with the checklist over time.
   assessment.json MUST include:
     numeric_value : the ACTUAL number cited (or measured) — no rounding to the
                     requirement threshold, no fabrication.
     unit          : must exactly match checklist.yaml threshold.unit
   If sources give only qualitative language ("low CPU", "supports large fleets"):
     verdict       = "partial"
     numeric_value = null
     notes         = explain the imprecision
   If no source mentions the metric at all:
     verdict       = "unknown"  (empty evidence, as always)

6. ANTI-FABRICATION (validator enforces these, non-negotiable)
   - `unknown` verdict when no evidence found. Unknown items must have
     empty evidence_ids / cited_source_ids / source_types. Never invent
     `not_supported` from silence.
   - Non-unknown verdicts REQUIRE non-empty evidence_ids, cited_source_ids,
     and source_types (tags from GUIDE.md § "Source type taxonomy").
   - If source_types are only vendor_doc / vendor_datasheet / vendor_blog,
     `confidence` is capped at "medium" — "high" requires >= 1 independent
     source (analyst_report, third_party_review, peer_reviewed, etc.).
   - `notes` <= 2 sentences, paraphrase of cited evidence only. No
     cross-product comparison in notes.

7. SOURCE PREFERENCE
   Deep pass is where triangulation matters: aim for >= 3 sources per item
   with at least 1 non-vendor source when possible. Cover categories 7 (HA)
   and 8 (Certifications) with regulator/registry sources where applicable
   (NIST CMVP, Common Criteria portal, FIPS validation registry).

8. VALIDATE
   After generating everything, run:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/microsegmentation/scripts/validate_assessment.py \
       d:/vcs/provider-screening/microsegmentation/runs/{product_id}/assessment.json \
       --evidence-store d:/vcs/provider-screening/microsegmentation/runs/{product_id}
   If it fails, fix assessment.json in place. NEVER fabricate evidence to
   pass — downgrade verdicts to `unknown` instead and re-run.
   Note: gate_decision is NOT required for standard mode (only for screen).

   Then run the grounding check (validate_assessment.py does NOT verify a
   quote is real, only that its IDs exist — this does):
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/scripts/verify_citation_grounding.py \
       --dir d:/vcs/provider-screening/microsegmentation/runs/{product_id} --strict --require-staged
   If ANY evidence comes back `fabricated`, that quote is not real — go back
   to the staged .txt and fix the quote to an exact substring, or downgrade
   the item's verdict (`partial`/`unknown`) if the claim genuinely isn't
   supported. Never edit the quote just to force a match without re-reading
   the .txt. `unverifiable` means a source was cited without being staged
   per step 4 — go stage it, then re-run.

   Once both pass, run render_report.py (see step 2) to produce report.md.
   First pass leaves the 4 narrative sections as template placeholders — Edit
   report.md to write those 4 sections, then run render_report.py again to
   regenerate the mechanical sections cleanly while keeping your prose.
```

---

## Differences from screen mode

| Concern              | Screen                             | Standard                                           |
|----------------------|------------------------------------|----------------------------------------------------|
| Item coverage        | 6 items with `screen: true`        | All 33 items                                       |
| `assessment_mode`    | `"screen"`                         | `"standard"`                                       |
| Report template      | `screening_report.md`              | `product_report.md`                                |
| Numeric thresholds   | Not enforced (no such items)       | Required for 5 items (1.3, 3.5, 4.1, 4.2, 4.3)     |
| `gate_decision`      | REQUIRED (drives promotion bucket) | Optional (no early-stopping yet — see GUIDE.md)    |
| Prior screen results | N/A                                | REUSE evidence for the 6 gate items where possible |
