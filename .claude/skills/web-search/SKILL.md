---
name: web-search
description: Use when you need to search the web for information -- find pages, check facts, discover sources to dig into further. Wraps the `ddgs` package (installed in this project's venv) as a subprocess-callable metasearch tool covering bing/brave/duckduckgo/google and more, no API key required.
---

# Web Search

## How to call it

Run this via the Bash tool, from the project root (`venv/` is relative to it, same
convention as `scripts/htmlstage/README.md`'s Usage section):

```
venv/Scripts/python.exe -c "
from ddgs import DDGS
import json
print(json.dumps(DDGS(timeout=10).text('YOUR QUERY', max_results=5, backend='bing,brave'), indent=2))
"
```

This prints a JSON array straight to stdout -- read it directly, no file
created. Each item is `{"title": ..., "href": ..., "body": ...}` (`body` is
a short snippet, not the full page).

`backend='bing,brave'` is a **deliberate choice, not the default** --
empirically tested against this network path: `bing` and `brave` (ddgs
scraping Brave's public results page, NOT the paid Brave Search API)
answered reliably; `duckduckgo`, `mojeek`, and `startpage` returned "No
results found", and the library's own `backend='auto'` default picked
`yahoo` and timed out. Always pass `backend='bing,brave'` explicitly
instead of relying on the default -- ddgs tries them in order and falls
through on failure, same fallback-chain idea as `scripts/htmlstage`'s
`AUTO_CHAIN`.

For a quick human-readable look instead of JSON (e.g. deciding which
result to dig into), the CLI's default table output also works and needs
no Python:

```
venv/Scripts/ddgs.exe text -q "YOUR QUERY" -m 5 -b bing
```

(The CLI's `-b` flag only accepts one backend at a time -- it's the Python
`DDGS(...).text(backend=...)` call that accepts the comma-separated
fallback list. Also avoid the CLI's `-o json` flag: it writes a
timestamped `.json` file into the current directory instead of printing to
stdout, leaving stray files behind.)

## Error handling

`ddgs` raises (from `ddgs.exceptions`): `DDGSException` (base -- includes
"no results found"), `RatelimitException`, `TimeoutException`. All three
subclass `DDGSException`, so a bare `except Exception` around the one-liner
is enough for a single query; there's no built-in retry/backoff, so on
failure just try the next query variation or a narrower `backend=` list
rather than looping the same call.

## What this is NOT for

This returns search-result **snippets** for discovery/triage only -- same
role WebSearch/WebFetch play in the provider-assessment prompt's step 4.
Never quote `evidence.jsonl` text from a `body` snippet. Once a result
looks worth citing, stage the actual page first:

```
venv/Scripts/python.exe scripts/htmlstage/html_to_text.py <href> \
  --product {product_id} --domain {DOMAIN}
```

and quote only from the staged `.txt` (see `scripts/htmlstage/README.md`
and `provider-assessment/GUIDE.md`'s source-staging rule).

## Caveats

`ddgs` scrapes public search-result pages rather than calling an official
search API -- same risk class as this project's other scraping-based tools
(`r.jina.ai` proxy, Wayback/Common Crawl fetch via `cdx_toolkit`), not a
new category of risk. Backends can degrade or break without notice since
there's no contract; if `bing,brave` both start failing, re-run the
backend probe above before assuming the query itself is at fault.
