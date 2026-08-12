"""Stage a bot-protected web page via the r.jina.ai render proxy.

Same staging contract as html_to_text.py: fetch raw HTML (via
r.jina.ai?url=... with x-respond-with: html), save it into
runs/<product_id>/artifacts/<slug>.html, extract text with the same
HTMLParser, append one manifest.jsonl entry with origin = the ORIGINAL
page URL (so verify_citation_grounding.py matches source.raw_url).

Usage:
  python scripts/stage_proxied_html.py <original-url> \
      --product <product_id> --domain bsg [--slug name]

The proxy response is recorded in the manifest as "via_proxy": true so the
audit trail is explicit about how the raw HTML was obtained.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ("microsegmentation", "bsg")
PROXY = "https://r.jina.ai/"

# Reuse the exact extractor from html_to_text.py
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from html_to_text import (  # noqa: E402
    _TextExtractor,
    sha256_file,
    slugify,
)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url", help="Original page URL (http/https)")
    ap.add_argument("--domain", choices=DOMAINS, default="bsg")
    ap.add_argument("--product", required=True)
    ap.add_argument("--slug", default=None)
    args = ap.parse_args()

    runs_root = REPO_ROOT / args.domain / "runs"
    staging_dir = runs_root / args.product / "artifacts"
    staging_dir.mkdir(parents=True, exist_ok=True)

    proxy_url = PROXY + args.url
    req = urllib.request.Request(
        proxy_url,
        headers={
            "User-Agent": "Mozilla/5.0 (provider-screening stage_proxied_html.py)",
            "Accept": "text/html,*/*;q=0.8",
            "x-respond-with": "html",
        },
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = resp.read()

    parsed = urllib.parse.urlparse(args.url)
    basename = [p for p in parsed.path.split("/") if p][-1] if parsed.path.split("/") else parsed.netloc
    url_hash = hashlib.sha256(args.url.encode("utf-8")).hexdigest()[:8]
    slug = args.slug or f"{slugify(basename)}-{url_hash}"

    html_path = staging_dir / f"{slug}.html"
    txt_path = staging_dir / f"{slug}.txt"
    html_path.write_bytes(data)

    parser = _TextExtractor()
    parser.feed(data.decode("utf-8", errors="replace"))
    text = parser.get_text()
    txt_path.write_text(text, encoding="utf-8")

    captured_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    entry = {
        "captured_at": captured_at,
        "kind": "html",
        "origin": args.url,
        "via_proxy": True,
        "proxy_url": proxy_url,
        "slug": slug,
        "html_path": html_path.name,
        "txt_path": txt_path.name,
        "sha256": sha256_file(html_path),
        "size_bytes": html_path.stat().st_size,
        "chars": len(text),
    }
    with (staging_dir / "manifest.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"staged: {html_path}")
    print(f"text  : {txt_path}")
    print(f"chars : {len(text)}")
    print(f"sha256: {entry['sha256']}")
    print(str(txt_path.resolve()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
