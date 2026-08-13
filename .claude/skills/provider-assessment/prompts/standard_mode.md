# Standard-mode prompt template

Full deep pass across all checklist items (shared across domains — bsg,
microsegmentation, ...). Fill in `{DOMAIN}`, `{VENDOR}`, `{PRODUCT_NAME}`,
`{product_id}` and paste into a Claude Code session:

---

```
Use the deep-research skill in STANDARD mode to assess ONE product against
the FULL {DOMAIN} checklist (every item).

  Vendor:       {VENDOR}
  Product:      {PRODUCT_NAME}
  product_id:   {product_id}

Follow the project's output contract in
d:/vcs/provider-screening/{DOMAIN}/GUIDE.md — it OVERRIDES the
skill's default report_template.md.

CRITICAL SAFETY RULE — NEVER run a command that kills processes by name,
especially "taskkill //F //IM python.exe" or "pkill python". You are
running inside a Python orchestrator process; killing all python.exe
processes kills your own parent and aborts the entire run. To stop a
background script you started, use Ctrl-C logic (write a sentinel file
that the script checks) or kill ONLY the specific PIDs you own.

1. CHECKLIST
   Read d:/vcs/provider-screening/{DOMAIN}/checklist.yaml.
   Assess EVERY item, in checklist order, grouped by the categories the
   file defines. Do not skip or merge items.

2. OUTPUT LOCATION
   Put ALL outputs in
     d:/vcs/provider-screening/{DOMAIN}/runs/{product_id}/
   Files:
     - sources.jsonl, evidence.jsonl, claims.jsonl, run_manifest.json
     - assessment.json      (validated against schemas/assessment.schema.json)
     - artifacts/           (raw PDFs staged there via the helper — see step 4)

   Do NOT hand-write report.md. After assessment.json validates (step 8), run:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/.claude/skills/provider-assessment/scripts/render_report.py \
       --domain {DOMAIN} \
       d:/vcs/provider-screening/{DOMAIN}/runs/{product_id}/assessment.json
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
     checklist_version = <the exact value of checklist.yaml meta.version>
     product_id        = "{product_id}"
   One entry per checklist item; item_ids match the checklist exactly.
   ALL items must be present — validator rejects partial coverage.

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
       --product {product_id} --domain {DOMAIN}
   Web page source:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/scripts/htmlstage/html_to_text.py <page-url> \
       --product {product_id} --domain {DOMAIN}

   Both stage the raw file into runs/{product_id}/artifacts/, write extracted
   text to <slug>.txt, and append an entry (URL, sha256, timestamp) to the
   SAME artifacts/manifest.jsonl. Then Read the .txt (last line of the
   script's stdout is its absolute path) — this is the ONLY text you may
   quote from. WebFetch is still fine for initial discovery/triage of which
   pages are worth staging, but the evidence quote itself must come from the
   staged .txt, never from WebFetch's summary.
   Citation etiquette:
     - sources.jsonl.raw_url  → the ORIGINAL URL (PDF or page), not the local
                                 artifact path — must match exactly what you
                                 passed to pdf_to_text.py / html_to_text.py
     - evidence.jsonl.locator → include the page for PDFs, e.g. "page 3,
                                 'throughput' section"; a section heading for
                                 web pages, e.g. "Validation section"
     - evidence.jsonl.quote   → an EXACT substring of the staged .txt, not a
                                 paraphrase. If quoting two non-adjacent
                                 sentences, join them with " ... " so the gap
                                 is visible — never silently stitch text that
                                 wasn't contiguous in the source.

5. NUMERIC-THRESHOLD ITEMS
   Items with `verdict_type: numeric_threshold` in checklist.yaml — read the
   exact `threshold.op` / `threshold.value` / `threshold.unit` from the file
   itself; do not rely on any value repeated in this prompt, which may drift
   out of sync with the checklist over time.
   assessment.json MUST include for each:
     numeric_value : the ACTUAL number cited (or measured) — no rounding to the
                     requirement threshold, no fabrication.
     unit          : must exactly match checklist.yaml threshold.unit
   If sources give only qualitative language ("high throughput", "low CPU"):
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
     source (analyst_report, third_party_review, certification_registry, etc.).
   - `notes` <= 2 sentences, paraphrase of cited evidence only. No
     cross-product comparison in notes.
   - `not_applicable` is ONLY legitimate on checklist items that carry a
     `not_applicable_class` field in checklist.yaml (validator rejects it on
     any other item). Full test in GUIDE.md rule 7 — quick version:
       `mechanism` items (a named component + a property of it) — does an
       instance of that component exist ANYWHERE in the product's
       architecture, for ANY purpose, not just the purpose this item cares
       about? Check the rest of THIS SAME assessment before answering no —
       if another item already relies on that component existing (e.g. it's
       the basis for a `supported`/`partial` verdict elsewhere), it exists,
       so the correct verdict here is `unknown` (referent exists, property
       unpublished), never `not_applicable`. No instance anywhere ->
       `not_applicable`.
       `outcome` items (can the product produce a result) — does it produce
       the outcome via ANY means? A product that itself applies/pushes the
       result to an enforcement point counts, even through a narrower
       mechanism than the wording suggests; a product that only emits
       information/rules for some OTHER, separately-operated system to apply
       does not count on that basis alone. No means at all + explicit-absence
       evidence -> `not_supported`. Produced, but only at a narrower scope
       that the CURRENT mechanism structurally cannot exceed (fixing it would
       require swapping the mechanism, not improving it) -> `not_applicable`;
       scope just not built out yet on the same mechanism -> `partial`.
     Never decide `not_applicable` vs `not_supported` per-vendor by feel —
     it is a property of the item's wording, fixed once in checklist.yaml.

7. SOURCE PREFERENCE
   Deep pass is where triangulation matters: aim for >= 3 sources per item
   with at least 1 non-vendor source when possible. Cover certification items
   with regulator/registry sources where applicable (Common Criteria portal,
   NIST CMVP / FIPS validation list, national certification registries).

8. VALIDATE
   After generating everything, run:
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/.claude/skills/provider-assessment/scripts/validate_assessment.py \
       --domain {DOMAIN} \
       d:/vcs/provider-screening/{DOMAIN}/runs/{product_id}/assessment.json \
       --evidence-store d:/vcs/provider-screening/{DOMAIN}/runs/{product_id}
    If it fails, fix assessment.json in place. NEVER fabricate evidence to
    pass — downgrade verdicts to `unknown` instead and re-run.

    Then run the grounding check (validate_assessment.py does NOT verify a
   quote is real, only that its IDs exist — this does):
     d:/vcs/provider-screening/venv/Scripts/python.exe \
       d:/vcs/provider-screening/.claude/skills/provider-assessment/scripts/verify_citation_grounding.py \
       --dir d:/vcs/provider-screening/{DOMAIN}/runs/{product_id} --strict --require-staged
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

## Notes

- Screen mode (6 gate items + gate_decision + promote_to_deep.py) has been
  removed. Every assessment now covers all checklist items and uses the
  `product_report.md` template. The `assessment_mode` enum is `standard` or
  `deep` only.
- Scripts live in `.claude/skills/provider-assessment/scripts/` (shared across
  all domains). Each script takes `--domain` so the right checklist.yaml /
  runs/ tree is used.
