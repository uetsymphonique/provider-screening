# Adding a New Provider Group (Domain)

A "provider group" (called a **domain** everywhere else in this repo - `bsg`,
`microsegmentation`, `ngfw`, ...) is a self-contained vendor-screening track:
its own vendor CSV, its own `checklist.yaml`, its own `<domain>/runs/` tree,
aggregated into its own `<domain>/comparison_matrix.xlsx`. All the scoring
machinery (`deep-research` + `provider-assessment` skills, validators,
renderer, aggregator, batch runner) is shared and selected at run time via
`--domain <name>`.

This guide is the checklist for adding one. It was written while adding
`ngfw`, which surfaced a footgun since fixed: the domain name used to be
hard-coded as an allow-list in six separate files, so missing one made a
script fail late with a confusing `invalid choice` error. `scripts/domains.py`
is now the single registry every one of those files imports from - see below.

## 1. Vendor CSV - `providers/<NAME>.csv`

Read by `scripts/batch/common.py`'s `load_products()`. Required shape:

```
<optional free-text title row>,,,
STT,Company,Product Name,product_id
1,Acme Corp,Acme Widget Firewall,acme-widget-firewall
```

- The loader scans for the first row whose **column 0 is literally `"STT"`**
  to find the header - everything above that row is ignored (useful for a
  human-readable title row), but if no row starts with `STT` it raises
  `SystemExit: no header row (STT,...) found`.
- Only three columns are actually read: `Company` -> `vendor`, `Product Name`
  (or `Product`) -> `product_name`, `product_id` -> the run directory key.
  Other columns some CSVs carry (`Country`, `Founded`, `Product Category`,
  `Website`, `Short Description`) are display-only for humans - no script
  reads them, so don't fabricate values for them just to match column count.
- `product_id` must be a unique slug (kebab-case, matches `<domain>/runs/<product_id>/`
  once assessed). No uniqueness check runs automatically - a duplicate
  silently makes two CSV rows collide onto the same run directory.

## 2. Register the domain - one place

`scripts/domains.py` is the single source of truth for the `DOMAINS` registry
(`{name: {"csv": Path, "dir": Path}}`). Add one entry:

```python
"<name>": {
    "csv": REPO_ROOT / "providers" / "<NAME>.csv",
    "dir": REPO_ROOT / "<name>",
},
```

Everything else imports `DOMAINS` from there instead of carrying its own
copy: `scripts/batch/common.py`, `scripts/pdf_to_text.py`,
`scripts/htmlstage/html_to_text.py`, and
`.claude/skills/provider-assessment/scripts/constants.py` (which re-exports
`DOMAINS`/`domain_dir`/`domain_paths`, so `validate_assessment.py`,
`render_report.py`, and `aggregate/aggregate_matrix.py` pick up the new
domain automatically with no changes of their own - they only import from
`constants.py`, never from `scripts/domains.py` directly).

`deep-research` does not import `scripts/domains.py` or anything else touched
here - it stays fully independent of this registry by design, unlike
`provider-assessment`, which only applies to this repo.

Two more spots reference domain names but need **no edit**, confirmed while
adding `ngfw` - worth knowing so you don't go hunting for a second place
that doesn't exist:
- `scripts/batch/tail_run_logs.py` - its `--domain` reads
  `common.DOMAINS.keys()` directly, so it inherits the registry automatically
  through `scripts/batch/common.py` (verify with `--help`, the choices list
  should already show the new name).
- `scripts/stats.py --domain` - a free-text filter with no `choices=`
  restriction at all; any domain name works immediately, the mention of
  `bsg`/`microsegmentation` in its `--help` text is just an example, not an
  enforced list.

If a future domain addition still trips a `choices=[...]` error somewhere
else, that's a new copy that slipped in and should import `DOMAINS` from
`scripts/domains.py` (directly, or transitively via `common.py`/
`constants.py`) instead of hard-coding a fresh list.

## 3. Domain folder - `<domain>/`

Mirror an existing domain (`bsg/` is the smaller reference):

```
<domain>/
├── checklist.md        # human-readable wording (source of truth for wording)
├── checklist.yaml       # machine-readable: stable IDs, verdict_type, thresholds
├── GUIDE.md              # domain-specific notes ONLY (provider list, checklist source notes) -
│                          #   the shared rules (verdict contract, workflow, staging, pitfalls)
│                          #   live in .claude/skills/provider-assessment/GUIDE.md; link to it,
│                          #   don't repeat it
├── .gitignore            # copy verbatim from bsg/.gitignore or microsegmentation/.gitignore
└── runs/                  # created on demand by the first product run - don't pre-create by hand
```

### `checklist.yaml` essentials

- `meta.version` starts at `1`; bump it (never renumber item IDs) whenever
  requirement wording changes - `assessment.json.checklist_version` must
  match or the validator rejects it.
- `verdict_type: boolean` for yes/no capability items; `numeric_threshold`
  (with `threshold: {op, value, unit}`) only when the requirement states an
  actual number.
- `not_applicable_class: mechanism` (+ `na_test_scope: broad|narrow`) is
  **opt-in per item** - how many items end up carrying it is whatever falls
  out of applying the test in
  `.claude/skills/provider-assessment/GUIDE.md` rules 7-8 to each item's own
  wording, not a frequency to aim for. Getting the classification wrong (in
  either direction) either lets a product dodge a requirement it should
  simply fail, or penalizes it for an undefined question it was never fair
  to ask - read rules 7-8's worked examples before assigning one.
- Full field-by-field semantics are documented as comments at the top of any
  existing `checklist.yaml` (`bsg/checklist.yaml` or
  `microsegmentation/checklist.yaml`) - copy that comment block as the
  starting point for a new one rather than re-deriving it.

### Authoring the checklist

Content and scope are entirely up to whoever is authoring the checklist for
that domain - this guide has no opinion on item count or category count, and
none should be inferred from `bsg`/`microsegmentation`'s current numbers.

- `checklist.md` is the same content as `checklist.yaml`, as plain
  `### category` / `+ item` Markdown - keep the two in sync by hand (there is
  no generator).
- If a vendor datasheet is used as seed material (as `ngfw/vNGFW.md` was for
  `ngfw/checklist.yaml`), note that explicitly in the domain's `GUIDE.md` -
  whether the checklist stays close to that one vendor's feature list or is
  deliberately generalized beyond it is, again, the author's call, not
  something this guide prescribes.

### `GUIDE.md`

Copy `bsg/GUIDE.md`'s structure: one line pointing at the shared GUIDE for
everything generic (verdict contract, workflow, batch runner, staging), then
domain-specific facts only - provider CSV path and vendor count, checklist
item/category count, any product-class notes relevant to *where to look for
evidence* (never to *what verdict to give* - see the shared GUIDE's
rules 7-8 on why product class must never justify `not_applicable`).

## 4. Smoke-test the wiring before running any real assessment

Cheap, no-cost checks that catch a missed registration or a malformed CSV
immediately, before spending a `deep-research` run on it:

```bash
# CSV loads, domain resolves, prompt renders - no agent actually spawned
venv/Scripts/python.exe scripts/batch/run_batch.py claude --domain <name> --mode standard --dry-run

# checklist.yaml parses, IDs are unique
venv/Scripts/python.exe -c "
import yaml
d = yaml.safe_load(open('<name>/checklist.yaml', encoding='utf-8'))
ids = [i['id'] for i in d['items']]
assert len(ids) == len(set(ids)), 'duplicate item id'
print('categories:', len(d['categories']), 'items:', len(d['items']))
"

# --domain <name> is accepted everywhere (confirms the registration in scripts/domains.py took)
venv/Scripts/python.exe .claude/skills/provider-assessment/scripts/validate_assessment.py --help | head -1
venv/Scripts/python.exe .claude/skills/provider-assessment/scripts/aggregate/aggregate_matrix.py --domain <name>
```

The aggregate command above is expected to print `No assessment.json found
under <domain>/runs` on a brand-new domain - that's success, not failure; it
means the domain resolved correctly and there's just nothing to aggregate
yet.

## 5. Then: the normal per-product workflow

Once the domain is wired and smoke-tested, everything from here on is the
standard, domain-agnostic flow - see
`.claude/skills/provider-assessment/SKILL.md` (entry point) and `GUIDE.md`
(verdict contract, staging/citation rules, batch runner, pitfalls). Nothing
in that workflow needs to know a new domain was just added.
