"""Fetch a PDF (URL or local path), STAGE the raw file, and extract text.

Purpose:
  WebFetch returns raw binary for application/pdf and cannot summarize it. This
  helper downloads (or ingests) the PDF, ALWAYS stages the raw file into an
  artifacts directory (so it survives for later audit), extracts text page-by-
  page, and appends a manifest.jsonl entry with URL + sha256 + timing.

Staging layout (with --product):
  <domain>/runs/<product_id>/artifacts/
    <slug>.pdf              raw PDF, staged
    <slug>.txt              extracted text with ===== PAGE N ===== delimiters
    manifest.jsonl          append-only ledger of every artifact captured

Usage:
  python scripts/pdf_to_text.py <url-or-path> --product <product_id> [--domain bsg]
  python scripts/pdf_to_text.py <url-or-path> [--out-dir <dir>] [--slug <name>]
                                              [--preview <N>]

`--product` and `--out-dir` are mutually exclusive; `--product` is preferred
because it keeps every raw artifact next to the assessment that cited it.
`--domain` selects which project tree `--product` stages into (default
microsegmentation) — get this wrong and the PDF silently lands under the
wrong project's runs/ directory.

Without either flag, files are staged into the shared cache
<domain>/runs/_pdf_cache/ (no manifest written there).

Exit 0 on success; the last line of stdout is the absolute path to the .txt.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader

from domains import DOMAINS, REPO_ROOT


def slugify(value: str) -> str:
    v = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return v or "pdf"


def is_url(s: str) -> bool:
    return s.startswith(("http://", "https://"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (provider-screening pdf_to_text.py)",
            "Accept": "application/pdf,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        ctype = resp.headers.get("Content-Type", "")
        data = resp.read()
    dest.write_bytes(data)
    if "pdf" not in ctype.lower() and not data[:4] == b"%PDF":
        print(f"WARN {url} content-type={ctype!r} first-bytes={data[:8]!r}", file=sys.stderr)


def extract(pdf_path: Path, txt_path: Path) -> tuple[int, int]:
    reader = PdfReader(str(pdf_path))
    pages = len(reader.pages)
    parts: list[str] = []
    for i, page in enumerate(reader.pages, start=1):
        try:
            t = page.extract_text() or ""
        except Exception as e:  # noqa: BLE001
            t = f"[pypdf extract_text failed on page {i}: {e}]"
        parts.append(f"\n\n===== PAGE {i} =====\n\n{t.strip()}")
    text = "\n".join(parts).strip() + "\n"
    txt_path.parent.mkdir(parents=True, exist_ok=True)
    txt_path.write_text(text, encoding="utf-8")
    return pages, len(text)


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
    return runs_root / "_pdf_cache", False


def append_manifest(manifest_path: Path, entry: dict) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="URL or local .pdf path")
    ap.add_argument("--domain", choices=list(DOMAINS), default="microsegmentation",
                    help="Which project's runs/ tree --product stages into.")
    ap.add_argument("--product", default=None,
                    help="Stage into <domain>/runs/<product>/artifacts/ + write manifest.jsonl")
    ap.add_argument("--out-dir", type=Path, default=None,
                    help="Custom staging dir (no manifest written). Mutually exclusive with --product.")
    ap.add_argument("--slug", default=None)
    ap.add_argument("--preview", type=int, default=800)
    args = ap.parse_args()

    runs_root = REPO_ROOT / args.domain / "runs"
    staging_dir, write_manifest = resolve_staging(args.product, args.out_dir, runs_root)
    staging_dir.mkdir(parents=True, exist_ok=True)

    captured_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    origin: str  # url or "local:<abspath>"
    if is_url(args.target):
        url = args.target
        origin = url
        parsed = urllib.parse.urlparse(url)
        basename = Path(parsed.path).stem or "document"
        url_hash = hashlib.sha256(url.encode("utf-8")).hexdigest()[:8]
        slug = args.slug or f"{slugify(basename)}-{url_hash}"
        pdf_path = staging_dir / f"{slug}.pdf"
        download(url, pdf_path)
    else:
        src = Path(args.target).resolve()
        if not src.exists():
            print(f"ERROR file not found: {src}", file=sys.stderr)
            return 1
        origin = f"local:{src}"
        slug = args.slug or slugify(src.stem)
        pdf_path = staging_dir / f"{slug}.pdf"
        # STAGE: copy raw file into artifacts dir (unless it's already there)
        if pdf_path.resolve() != src.resolve():
            shutil.copy2(src, pdf_path)

    txt_path = staging_dir / f"{slug}.txt"
    pages, chars = extract(pdf_path, txt_path)
    file_hash = sha256_file(pdf_path)
    size_bytes = pdf_path.stat().st_size

    if write_manifest:
        append_manifest(staging_dir / "manifest.jsonl", {
            "captured_at": captured_at,
            "kind": "pdf",
            "origin": origin,
            "slug": slug,
            "pdf_path": pdf_path.name,
            "txt_path": txt_path.name,
            "sha256": file_hash,
            "size_bytes": size_bytes,
            "pages": pages,
            "chars": chars,
        })

    print(f"staged: {pdf_path}")
    print(f"text  : {txt_path}")
    print(f"pages : {pages}")
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
