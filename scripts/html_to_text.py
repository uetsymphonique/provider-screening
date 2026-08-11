"""Fetch a web page (URL), STAGE the raw HTML, and extract plain text.

Purpose:
  WebFetch (used by the deep-research skill inside an agent session) fetches
  a page AND summarizes it through a small model in the same call -- nothing
  raw ever touches disk. That makes it impossible to later verify whether an
  `evidence.jsonl` quote actually appears on the cited page, which is exactly
  how fabricated-but-plausible quotes slip past `validate_assessment.py`
  (that script only checks evidence_id/source_id referential integrity, not
  quote grounding).

  This is the HTML sibling of `pdf_to_text.py`: it downloads the page with a
  plain HTTP request (no summarization), ALWAYS stages the raw HTML into the
  artifacts directory, extracts stripped-tag plain text, and appends a
  manifest.jsonl entry with URL + sha256 + timing -- same schema, same file,
  same directory as pdf_to_text.py (distinguished by "kind": "html" vs
  "pdf"), so one grounding-check script can walk both kinds uniformly.

  Stdlib only (html.parser), matching this repo's / the deep-research
  skill's no-new-dependency convention -- no bs4/lxml.

Staging layout (with --product):
  <domain>/runs/<product_id>/artifacts/
    <slug>.html              raw HTML, staged
    <slug>.txt                stripped-tag plain text
    manifest.jsonl             append-only ledger, shared with pdf_to_text.py

Usage:
  python scripts/html_to_text.py <url> --product <product_id> [--domain bsg]
  python scripts/html_to_text.py <url> [--out-dir <dir>] [--slug <name>]
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
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ("microsegmentation", "bsg")

# Tags whose content is never real page text and should be dropped entirely
# rather than leaked into the extracted text. nav/header/footer/aside are
# site chrome (breadcrumbs, sidebar TOC, global nav) -- confirmed empirically
# on a real vendor docs page (docs.paloaltonetworks.com/.../pa-400r-.../
# physical-specifications): 107 of 150 extracted lines were duplicated
# nav/breadcrumb chrome, only 43 were the actual spec content. Tradeoff: a
# page that nests real content inside <header> (e.g. an <article>'s title
# block) would lose that too -- accepted, since vendor spec/product pages
# rarely structure content that way and the chrome-noise cost was far larger
# across real samples.
SKIP_TAGS = {"script", "style", "noscript", "template", "svg",
             "nav", "header", "footer", "aside"}

# Block-level tags: emit a newline at open/close so paragraph structure
# survives (helps keep quotes on recognizable line boundaries for later
# grounding checks, though checks should still normalize whitespace).
BLOCK_TAGS = {
    "p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6",
    "section", "article", "ul", "ol", "table", "blockquote", "main",
}

# Table cell tags: emit a " | " separator, NOT a newline -- otherwise
# adjacent cells on the same row concatenate with no boundary at all
# (e.g. a "10 Gbps" throughput cell next to a "2 ms" latency cell becomes
# the unreadable, misleading "10 Gbps2 ms"). This matters most for spec
# tables, which is exactly where numeric_threshold checklist items pull
# their numbers from.
CELL_TAGS = {"td", "th"}


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._chunks: list[str] = []
        self._skip_stack: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:  # noqa: ANN001
        if tag in SKIP_TAGS:
            self._skip_stack.append(tag)
        elif tag in CELL_TAGS:
            self._chunks.append(" | ")
        elif tag in BLOCK_TAGS:
            self._chunks.append("\n")

    def handle_startendtag(self, tag: str, attrs) -> None:  # noqa: ANN001
        if tag == "br":
            self._chunks.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self._skip_stack and self._skip_stack[-1] == tag:
            self._skip_stack.pop()
        elif tag in BLOCK_TAGS:
            self._chunks.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_stack:
            return
        self._chunks.append(data)

    def get_text(self) -> str:
        raw = "".join(self._chunks)
        lines = []
        for ln in raw.splitlines():
            ln = re.sub(r"[ \t]+", " ", ln).strip()
            ln = re.sub(r"\s*\|\s*", " | ", ln).strip(" |")
            if ln:
                lines.append(ln)
        return "\n".join(lines) + "\n" if lines else ""


def slugify(value: str) -> str:
    v = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return v or "page"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, dest: Path, browser_ua: bool = False) -> str:
    """Download raw HTML to `dest`. Returns the decoded text (str).
    Set browser_ua=True to use a browser User-Agent for sites that block
    the default UA (e.g. support.elisity.com returns 403)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    ua = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
        if browser_ua
        else "Mozilla/5.0 (provider-screening html_to_text.py)"
    )
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": ua,
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        ctype = resp.headers.get("Content-Type", "")
        data = resp.read()
    dest.write_bytes(data)
    if "html" not in ctype.lower() and not data.lstrip()[:15].lower().startswith(b"<!doctype html") \
            and b"<html" not in data[:2000].lower():
        print(f"WARN {url} content-type={ctype!r} first-bytes={data[:40]!r}", file=sys.stderr)

    charset = None
    m = re.search(r"charset=([\w-]+)", ctype, re.IGNORECASE)
    if m:
        charset = m.group(1)
    if not charset:
        m = re.search(rb'charset=["\']?([\w-]+)', data[:2048], re.IGNORECASE)
        if m:
            charset = m.group(1).decode("ascii", "ignore")
    try:
        return data.decode(charset or "utf-8", errors="replace")
    except (LookupError, UnicodeDecodeError):
        return data.decode("utf-8", errors="replace")


def extract(html_text: str, txt_path: Path) -> int:
    parser = _TextExtractor()
    parser.feed(html_text)
    text = parser.get_text()
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.write_text(text, encoding="utf-8")
    return len(text)


def resolve_staging(
    product: str | None, out_dir: Path | None, runs_root: Path
) -> tuple[Path, bool]:
    """Return (staging_dir, write_manifest). Manifest only when product is set."""
    if product and out_dir:
        raise SystemExit("Pass EITHER --product OR --out-dir, not both.")
    if product:
        return runs_root / product / "artifacts", True
    if out_dir:
        return out_dir, False
    return runs_root / "_html_cache", False


def append_manifest(manifest_path: Path, entry: dict) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url", help="Page URL (http/https)")
    ap.add_argument("--domain", choices=DOMAINS, default="microsegmentation",
                     help="Which project's runs/ tree --product stages into.")
    ap.add_argument("--product", default=None,
                     help="Stage into <domain>/runs/<product>/artifacts/ + append manifest.jsonl "
                          "(same file pdf_to_text.py writes to).")
    ap.add_argument("--out-dir", type=Path, default=None,
                     help="Custom staging dir (no manifest written). Mutually exclusive with --product.")
    ap.add_argument("--slug", default=None)
    ap.add_argument("--browser-ua", action="store_true",
                    help="Use browser User-Agent (evades 403 on some support portals).")
    ap.add_argument("--preview", type=int, default=800)
    args = ap.parse_args()

    if not args.url.startswith(("http://", "https://")):
        print(f"ERROR not a URL: {args.url!r}", file=sys.stderr)
        return 1

    runs_root = REPO_ROOT / args.domain / "runs"
    staging_dir, write_manifest = resolve_staging(args.product, args.out_dir, runs_root)
    staging_dir.mkdir(parents=True, exist_ok=True)

    captured_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    parsed = urllib.parse.urlparse(args.url)
    path_parts = [p for p in parsed.path.split("/") if p]
    basename = path_parts[-1] if path_parts else (parsed.netloc or "page")
    url_hash = hashlib.sha256(args.url.encode("utf-8")).hexdigest()[:8]
    slug = args.slug or f"{slugify(basename)}-{url_hash}"

    html_path = staging_dir / f"{slug}.html"
    txt_path = staging_dir / f"{slug}.txt"

    try:
        html_text = download(args.url, html_path, browser_ua=args.browser_ua)
    except Exception as e:  # noqa: BLE001
        print(f"ERROR fetching {args.url}: {e}", file=sys.stderr)
        return 1

    chars = extract(html_text, txt_path)
    file_hash = sha256_file(html_path)
    size_bytes = html_path.stat().st_size

    if chars == 0:
        print(f"WARN extracted 0 chars of text from {args.url} -- page may be JS-rendered "
              f"(client-side only) and unusable as ground truth for citation checks.",
              file=sys.stderr)

    if write_manifest:
        append_manifest(staging_dir / "manifest.jsonl", {
            "captured_at": captured_at,
            "kind": "html",
            "origin": args.url,
            "slug": slug,
            "html_path": html_path.name,
            "txt_path": txt_path.name,
            "sha256": file_hash,
            "size_bytes": size_bytes,
            "chars": chars,
        })

    print(f"staged: {html_path}")
    print(f"text  : {txt_path}")
    print(f"chars : {chars}")
    print(f"sha256: {file_hash}")
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
