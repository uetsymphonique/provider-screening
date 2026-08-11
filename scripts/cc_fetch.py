"""Fetch an archived page from Common Crawl and stage it like html_to_text.py.

Finds the latest CC index entry for the URL (with optional status filter),
downloads the WARC record via HTTP range request, extracts the HTTP payload
(HTML), and stages it into runs/<product>/artifacts/ with a manifest.jsonl
entry whose origin is the ORIGINAL URL (so citation grounding matches).

Usage:
  python scripts/cc_fetch.py <url> --product <product_id> [--domain microsegmentation]
      [--index CC-MAIN-2024-26] [--slug <name>] [--status 200]
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from html_to_text import _TextExtractor, slugify  # noqa: E402

DATA_BASE = "https://data.commoncrawl.org/"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def get(url: str, timeout: int = 120) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "provider-screening cc_fetch.py"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def find_index_entry(url: str, index: str | None, status: str | None) -> dict:
    base = index or "CC-MAIN-2025-05"
    if index:
        collections = [index]
    else:
        collections = ["CC-MAIN-2025-05", "CC-MAIN-2024-51", "CC-MAIN-2024-42",
                       "CC-MAIN-2024-33", "CC-MAIN-2024-26", "CC-MAIN-2024-18",
                       "CC-MAIN-2024-10", "CC-MAIN-2023-50", "CC-MAIN-2023-40",
                       "CC-MAIN-2023-23", "CC-MAIN-2022-49", "CC-MAIN-2022-40"]
    q = "url=" + urllib.parse.quote(url, safe="")
    if status:
        q += f"&filter=status:{status}"
    for coll in collections:
        try:
            data = get(f"https://index.commoncrawl.org/{coll}-index?{q}&output=json")
        except Exception:
            continue
        lines = [l for l in data.decode("utf-8", "replace").splitlines() if l.strip()]
        if lines:
            entry = json.loads(lines[0])
            entry["collection"] = coll
            return entry
    raise SystemExit(f"ERROR no CC index entry found for {url}")


def extract_payload(warc_bytes: bytes) -> bytes:
    """Extract the HTTP response body from a WARC record."""
    headers, _, rest = warc_bytes.partition(b"\r\n\r\n")
    # WARC header block ends with two CRLFs; then HTTP response follows
    # Try: first find end of WARC headers
    idx = warc_bytes.find(b"\r\n\r\n")
    if idx == -1:
        raise SystemExit("ERROR malformed WARC record (no header terminator)")
    http = warc_bytes[idx + 4:]
    # HTTP headers end with blank line
    hidx = http.find(b"\r\n\r\n")
    if hidx == -1:
        return http
    return http[hidx + 4:]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--product", required=True)
    ap.add_argument("--domain", default="microsegmentation")
    ap.add_argument("--index", default=None)
    ap.add_argument("--slug", default=None)
    ap.add_argument("--status", default="200")
    args = ap.parse_args()

    staging_dir = REPO_ROOT / args.domain / "runs" / args.product / "artifacts"
    staging_dir.mkdir(parents=True, exist_ok=True)

    parsed = re.sub(r"^https?://", "", args.url)
    slug = args.slug or slugify(parsed)[:80]
    html_path = staging_dir / f"{slug}.html"
    txt_path = staging_dir / f"{slug}.txt"

    entry = find_index_entry(args.url, args.index, args.status)
    warc_url = DATA_BASE + entry["filename"]
    offset, length = int(entry["offset"]), int(entry["length"])

    req = urllib.request.Request(warc_url, headers={
        "User-Agent": "provider-screening cc_fetch.py",
        "Range": f"bytes={offset}-{offset + length - 1}",
    })
    with urllib.request.urlopen(req, timeout=180) as resp:
        warc_bytes = resp.read()

    if warc_bytes[:2] == b"\x1f\x8b":  # gzip magic
        warc_bytes = gzip.decompress(warc_bytes)

    payload = extract_payload(warc_bytes)
    html_path.write_bytes(payload)

    parser = _TextExtractor()
    parser.feed(payload.decode("utf-8", errors="replace"))
    text = parser.get_text()
    if not text.strip():
        print("WARN extracted 0 chars of text", file=sys.stderr)
    txt_path.write_text(text, encoding="utf-8")

    captured_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    man = {
        "captured_at": captured_at,
        "kind": "html",
        "origin": args.url,
        "slug": slug,
        "html_path": html_path.name,
        "txt_path": txt_path.name,
        "sha256": sha256_file(html_path),
        "size_bytes": html_path.stat().st_size,
        "chars": len(text),
        "cc_index": entry.get("collection"),
        "cc_timestamp": entry.get("timestamp"),
    }
    with (staging_dir / "manifest.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(man, ensure_ascii=False) + "\n")

    print(f"staged: {html_path}")
    print(f"text  : {txt_path}")
    print(f"chars : {len(text)}")
    print(f"sha256: {man['sha256']}")
    print(f"cc    : {entry.get('collection')} @ {entry.get('timestamp')}")
    print(str(txt_path.resolve()))
    return 0


if __name__ == "__main__":
    main()
