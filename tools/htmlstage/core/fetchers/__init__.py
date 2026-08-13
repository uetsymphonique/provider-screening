"""Fetch methods for main.py's auto-fallback chain: direct HTTP,
r.jina.ai proxy (HTML render and Markdown render), stealth browser, Wayback
Machine, and Common Crawl archive.

Package layout (grouped by dependency weight, not one file per method):
    base.py     -- FetchError, the charset-sniffing _decode() helper, and
                   the method registry (REGISTRY / @register) that lets
                   main.py dispatch by name instead of growing an
                   if/elif ladder per method.
    direct.py   -- fetch_direct: curl_cffi, TLS/JA3 impersonation.
    proxy.py    -- fetch_proxy_html / fetch_proxy_md: r.jina.ai, no extra
                   heavy deps.
    stealthy.py -- fetch_stealthy: scrapling + playwright/patchright/
                   browserforge, imported lazily inside the function so the
                   heavy import cost is only paid when this method runs.
    archive.py  -- fetch_wayback / fetch_common_crawl: cdx_toolkit.

Adding a 7th method that only needs a URL (a new archive source, a new
proxy provider) requires: a new module, a @register("name") decorator on
the function, and adding the name to AUTO_CHAIN in main.py -- no
changes to main.py's dispatch logic. Methods that also need
CLI-specific override kwargs (direct's browser_ua, wayback's timestamp,
cc's index/status) stay wired explicitly in main.py._run_method
instead of being forced through the registry, since threading
argparse.Namespace fields through a generic single-arg signature would
obscure the mapping rather than simplify it.

Each fetcher takes a URL (plus optional method-specific kwargs) and returns
(raw_bytes, decoded_text, meta), where meta always includes "content_kind"
("html" or "markdown") plus any method-specific provenance fields
(proxy_url, cc_index, ...). Fetchers never write to disk -- main.py
stages only the winning method's output, so failed/escalated attempts leave
no artifact clutter behind.

All fetchers raise FetchError (never SystemExit) on failure so the chain
driver in main.py can catch and escalate to the next method instead
of the process dying mid-chain.
"""
from __future__ import annotations

from .archive import fetch_common_crawl, fetch_wayback
from .base import REGISTRY, FetchError
from .direct import fetch_direct
from .proxy import fetch_proxy_html, fetch_proxy_md
from .stealthy import fetch_stealthy

__all__ = [
    "REGISTRY",
    "FetchError",
    "fetch_direct",
    "fetch_proxy_html",
    "fetch_proxy_md",
    "fetch_stealthy",
    "fetch_wayback",
    "fetch_common_crawl",
]
