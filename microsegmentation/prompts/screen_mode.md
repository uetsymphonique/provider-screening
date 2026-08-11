# Screen-mode prompt template

Fill in `{VENDOR}`, `{PRODUCT_NAME}`, `{product_id}` (slug from `providers/Microsegmentation.csv`) and paste into a Claude Code session:

---

```
Use the deep-research skill in STANDARD mode to assess ONE product:

  Vendor:       {VENDOR}
  Product:      {PRODUCT_NAME}
  product_id:   {product_id}

Follow the project's output contract in
d:/vcs/provider-screening/microsegmentation/GUIDE.md — it OVERRIDES the
skill's default report_template.md.

CRITICAL SAFETY RULE — NEVER run a command that kills processes by name,
especially "taskkill //F //IM python.exe" or "pkill python". You are
running inside a Python orchestrator process; killing all python.exe
processes kills your own parent and aborts the entire run. To stop a
background script you started, use Ctrl-C logic (write a sentinel file
that the script checks) or kill ONLY the specific PIDs you own.

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
   staged .txt, never from WebFetch's summary.
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

   Once both pass, generate report.md:
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
