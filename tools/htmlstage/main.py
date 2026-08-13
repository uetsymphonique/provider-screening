"""Fetch a web page (URL), STAGE the raw HTML, and extract plain text.

Purpose:
  WebFetch (used by the deep-research skill inside an agent session) fetches
  a page AND summarizes it through a small model in the same call -- nothing
  raw ever touches disk. That makes it impossible to later verify whether an
  `evidence.jsonl` quote actually appears on the cited page, which is exactly
  how fabricated-but-plausible quotes slip past `validate_assessment.py`
  (that script only checks evidence_id/source_id referential integrity, not
  quote grounding).

  This is the HTML sibling of `tools/pdfstage/main.py`: it fetches the page (no
  summarization), ALWAYS stages the raw content into the artifacts
  directory, extracts plain text, and appends a manifest.jsonl entry with
  URL + sha256 + timing -- same schema, same file, same directory as
  tools/pdfstage/main.py (distinguished by "kind": "html" vs "pdf"), so one
  grounding-check script can walk both kinds uniformly.

Fetch methods (--method, default "auto"):
  This consolidates what used to be four separate scripts (html_to_text.py,
  stage_proxied_html.py, stage_md_proxied.py, cc_fetch.py) into one, since
  they were all manually-invoked variations on "get the page's raw content
  somehow" with an identical staging/manifest contract:
    direct     -- HTTP GET impersonating a real browser's TLS/JA3
                  fingerprint via curl_cffi, not just its headers
                  (tools/htmlstage/core/fetchers/direct.py:fetch_direct)
    proxy-html -- r.jina.ai HTML-mode render, for bot-protected pages
                  (fetch_proxy_html)
    proxy-md   -- r.jina.ai Markdown-mode render, last-resort proxy fallback
                  for pages whose HTML-mode render still hits a challenge
                  (fetch_proxy_md)
    stealthy   -- real fingerprint-spoofed Chromium (Scrapling's
                  StealthyFetcher), executes JS and solves Cloudflare
                  Turnstile/Interstitial challenges -- the only method that
                  can render JS-only/SPA pages or clear a live challenge
                  rather than just detect and escalate past it
                  (fetch_stealthy)
    wayback    -- most recent Wayback Machine (web.archive.org) capture, via
                  one CDX API lookup + raw snapshot fetch (fetch_wayback)
    cc         -- Common Crawl archived WARC record, for pages no longer
                  reachable live (fetch_common_crawl)
  In "auto" mode these run in the order above, escalating to the next
  method when one fails outright, extracts fewer than
  core.extract.MIN_REAL_CONTENT_CHARS (250) chars, OR the extracted
  text matches a known bot-challenge banner (core.extract.
  detect_interstitial -- Cloudflare/Incapsula/PerimeterX/etc. interstitials
  are HTTP-200 and often well over 250 chars of "checking your browser"
  boilerplate, so the length check alone wouldn't catch them). stealthy runs
  after the proxy methods (it's the heaviest live-fetch method -- spins up a
  real browser) and before wayback/cc, since a live render is still
  preferable to an archived copy when it can be gotten. wayback runs before
  cc because it archives continuously (vs Common Crawl's periodic, incomplete
  crawls) and needs one HTTP round-trip instead of scanning dozens of CC
  collections -- cc stays as the final fallback since it occasionally has a
  capture wayback missed. The winning method is printed and recorded as
  "fetch_method" in the manifest entry: a quote sourced from Jina's markdown
  rendering is, provenance-wise, a quote from Jina rendering the vendor's
  page, not from the vendor's raw HTML, so which method actually produced
  the .txt must stay visible, not silently swallowed. `origin` in the
  manifest is always the ORIGINAL page URL regardless of method, so
  verify_citation_grounding.py's origin match keeps working unchanged.
  Pass an explicit --method to skip straight to a known-good method (e.g. a
  domain you already know needs the proxy) instead of paying for failed
  attempts; a forced method accepts whatever it returns (just warns if short).

Extraction engine:
  Trafilatura (boilerplate-removal heuristics -- strips nav/header/footer/ads
  far more reliably than a hand-rolled tag-stripper, used by
  HuggingFace/IBM/Microsoft Research) is the primary extractor for
  HTML-kind content. When it returns nothing (page too short/irregular for
  its heuristics), falls back to a stdlib `html.parser`-based tag-stripper
  (core.extract._TextExtractor) so a page never silently yields 0 chars
  just because one engine bailed. Markdown-kind content (proxy-md) is
  already clean prose and is staged as-is, engine "raw_markdown". The
  manifest's "extractor" field records which one actually produced the .txt.

Staging layout (with --product):
  <domain>/runs/<product_id>/artifacts/
    <slug>.html (or .md for proxy-md)   raw content, staged
    <slug>.txt                           extracted plain text
    manifest.jsonl                       append-only ledger, shared with tools/pdfstage/main.py

Usage:
  python tools/htmlstage/main.py <url> --product <product_id> [--domain bsg]
  python tools/htmlstage/main.py <url> --method proxy-html --product <id>
  python tools/htmlstage/main.py <url> [--out-dir <dir>] [--slug <name>]
                                        [--preview <N>]

`--product` and `--out-dir` are mutually exclusive; `--product` is preferred
because it keeps every raw artifact next to the assessment that cited it.
`--domain` selects which project tree `--product` stages into (default
microsegmentation) -- get this wrong and the page silently lands under the
wrong project's runs/ directory.

Without either flag, files are staged into the shared cache
<domain>/runs/_html_cache/ (no manifest written there).

Exit 0 on success; the last line of stdout is the absolute path to the .txt.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

from shared.domains import DOMAINS, domain_dir
from tools.htmlstage.core.extract import MIN_REAL_CONTENT_CHARS, detect_interstitial, extract_text
from tools.htmlstage.core.fetchers import (
    REGISTRY,
    FetchError,
    fetch_common_crawl,
    fetch_direct,
    fetch_wayback,
)
from tools.htmlstage.core.staging import append_manifest, resolve_staging, sha256_bytes, slugify

AUTO_CHAIN = ("direct", "proxy-html", "proxy-md", "stealthy", "wayback", "cc")


def _run_method(method: str, url: str, args: argparse.Namespace) -> tuple[bytes, str, dict]:
    # direct/wayback/cc need CLI-specific override kwargs, so they're wired
    # explicitly rather than through core.fetchers.REGISTRY -- see
    # tools/htmlstage/core/fetchers/__init__.py's docstring for the split rationale.
    if method == "direct":
        return fetch_direct(url, browser_ua=args.browser_ua)
    if method == "wayback":
        return fetch_wayback(url, timestamp=args.wayback_timestamp)
    if method == "cc":
        return fetch_common_crawl(url, index=args.cc_index, status=args.cc_status)
    if method in REGISTRY:
        return REGISTRY[method](url)
    raise ValueError(f"unknown method: {method}")  # unreachable, argparse validates choices


def fetch_with_fallback(
    url: str, args: argparse.Namespace
) -> tuple[str, bytes, str, str, dict]:
    """Run the fetch/extract chain. Returns (method, raw_bytes, text, engine, meta)."""
    chain = list(AUTO_CHAIN) if args.method == "auto" else [args.method]
    last_error: Exception | None = None

    for i, method in enumerate(chain):
        is_last = i == len(chain) - 1
        try:
            raw_bytes, raw_text, meta = _run_method(method, url, args)
        except FetchError as e:
            print(f"WARN {method} fetch failed: {e}", file=sys.stderr)
            last_error = e
            continue

        if meta["content_kind"] == "html":
            text, engine = extract_text(raw_text, url, args.favor_recall, not args.no_fallback)
        else:
            text, engine = raw_text, "raw_markdown"

        thin_reason = None
        if len(text) < MIN_REAL_CONTENT_CHARS:
            thin_reason = f"only {len(text)} chars (< {MIN_REAL_CONTENT_CHARS})"
        else:
            challenge = detect_interstitial(text)
            if challenge:
                thin_reason = f"bot-challenge page detected (matched {challenge!r})"

        if args.method != "auto" or thin_reason is None or is_last:
            return method, raw_bytes, text, engine, meta

        print(f"WARN {method} yielded {thin_reason}, escalating to next method...", file=sys.stderr)

    raise SystemExit(f"ERROR all fetch methods exhausted for {url}: {last_error}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url", help="Page URL (http/https)")
    ap.add_argument("--domain", choices=list(DOMAINS), default="microsegmentation",
                     help="Which project's runs/ tree --product stages into.")
    ap.add_argument("--product", default=None,
                     help="Stage into <domain>/runs/<product>/artifacts/ + append manifest.jsonl "
                          "(same file tools/pdfstage/main.py writes to).")
    ap.add_argument("--out-dir", type=Path, default=None,
                     help="Custom staging dir (no manifest written). Mutually exclusive with --product.")
    ap.add_argument("--slug", default=None)
    ap.add_argument("--method", choices=["auto", *AUTO_CHAIN], default="auto",
                     help="Fetch method. 'auto' tries direct -> proxy-html -> proxy-md -> wayback -> cc, "
                          "escalating on failure or thin (<250 char) extraction. Force one to "
                          "skip straight to a known-good method.")
    ap.add_argument("--wayback-timestamp", default=None,
                     help="Force a specific Wayback capture (14-digit YYYYMMDDhhmmss, from a prior "
                          "manifest's wayback_timestamp) instead of looking up the most recent one.")
    ap.add_argument("--cc-index", default=None, help="Force a specific Common Crawl collection id.")
    ap.add_argument("--cc-status", default="200", help="Common Crawl status filter (--method cc only).")
    ap.add_argument("--browser-ua", action="store_true",
                     help="For --method direct: impersonate Safari's TLS fingerprint instead of "
                          "Chrome's (curl_cffi). Try this if a site specifically fingerprints/blocks "
                          "Chrome's signature (e.g. support.elisity.com).")
    ap.add_argument("--favor-recall", action="store_true",
                     help="Favor more text over precision in trafilatura (default: favor precision).")
    ap.add_argument("--no-fallback", action="store_true",
                     help="Do not fall back to the stdlib HTMLParser when trafilatura returns nothing.")
    ap.add_argument("--preview", type=int, default=800)
    args = ap.parse_args()

    if not args.url.startswith(("http://", "https://")):
        print(f"ERROR not a URL: {args.url!r}", file=sys.stderr)
        return 1

    runs_root = domain_dir(args.domain) / "runs"
    staging_dir, write_manifest = resolve_staging(args.product, args.out_dir, runs_root)
    staging_dir.mkdir(parents=True, exist_ok=True)

    captured_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    parsed = urllib.parse.urlparse(args.url)
    path_parts = [p for p in parsed.path.split("/") if p]
    basename = path_parts[-1] if path_parts else (parsed.netloc or "page")
    url_hash = hashlib.sha256(args.url.encode("utf-8")).hexdigest()[:8]
    slug = args.slug or f"{slugify(basename)}-{url_hash}"

    method, raw_bytes, text, engine, meta = fetch_with_fallback(args.url, args)

    raw_ext = "md" if meta["content_kind"] == "markdown" else "html"
    raw_path = staging_dir / f"{slug}.{raw_ext}"
    txt_path = staging_dir / f"{slug}.txt"
    raw_path.write_bytes(raw_bytes)
    txt_path.write_text(text, encoding="utf-8")

    file_hash = sha256_bytes(raw_bytes)
    size_bytes = len(raw_bytes)
    chars = len(text)

    if chars == 0:
        print(f"WARN extracted 0 chars of text from {args.url} -- page may be JS-rendered "
              f"(client-side only) and unusable as ground truth for citation checks.",
              file=sys.stderr)

    if write_manifest:
        entry = {
            "captured_at": captured_at,
            "kind": "html",
            "fetch_method": method,
            "extractor": engine,
            "origin": args.url,
            "slug": slug,
            "html_path": raw_path.name,
            "txt_path": txt_path.name,
            "sha256": file_hash,
            "size_bytes": size_bytes,
            "chars": chars,
        }
        entry.update({k: v for k, v in meta.items() if k != "content_kind"})
        append_manifest(staging_dir / "manifest.jsonl", entry)

    print(f"method  : {method}")
    print(f"staged  : {raw_path}")
    print(f"text    : {txt_path}")
    print(f"chars   : {chars}")
    print(f"engine  : {engine}")
    print(f"sha256  : {file_hash}")
    if write_manifest:
        print(f"manifest: {staging_dir / 'manifest.jsonl'}")
    if args.preview > 0:
        preview = txt_path.read_text(encoding="utf-8")[: args.preview]
        print("----- preview -----")
        print(preview)
        print("----- /preview -----")
    print(str(txt_path.resolve()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
