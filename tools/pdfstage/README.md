# tools/pdfstage

PDF-staging tool: fetch a PDF (URL or local path), **stage** the raw file
plus extracted text into `artifacts/`, and append a line to
`manifest.jsonl` -- so `verify_citation_grounding.py` can later check
whether a quote in `evidence.jsonl` actually appears on the page it cites.

This is the sibling of `tools/htmlstage/main.py`: same manifest schema, same
`artifacts/` dir, differing only in `"kind": "pdf"` vs `"html"` -- one
grounding-check script can walk both kinds.

## Usage

```bash
# Auto chain, stage into a product's artifacts (writes manifest.jsonl)
venv/Scripts/python.exe tools/pdfstage/main.py <url-or-path> \
  --domain bsg --product <product_id>

# No --product/--out-dir -> stages into the shared cache, no manifest written
venv/Scripts/python.exe tools/pdfstage/main.py <url-or-path> --out-dir <dir>
```

`--product` and `--out-dir` are mutually exclusive; `--product` is preferred
because it keeps every raw artifact next to the assessment that cited it.
`--domain` selects which project tree `--product` stages into (default
`microsegmentation`) -- get this wrong and the PDF silently lands under the
wrong project's `runs/` directory.

Extraction is page-by-page via `pypdf`, delimited by `===== PAGE N =====`
headers in the staged `.txt`.

Exits 0 on success; the last line of stdout is the absolute path to the
`.txt` file.

## Output / staging

```
<domain>/runs/<product_id>/artifacts/
    <slug>.pdf     raw PDF, staged
    <slug>.txt     extracted text, ===== PAGE N ===== delimiters
    manifest.jsonl append-only, shared with tools/htmlstage/main.py
```
