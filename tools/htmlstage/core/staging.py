"""Staging primitives shared by tools/htmlstage/main.py (and, historically, its now-
retired sibling scripts). Deliberately dependency-free (stdlib only) and
generic enough that tools/pdfstage/main.py could adopt it later -- not done
now, scope of this refactor is HTML only.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


def slugify(value: str) -> str:
    v = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return v or "page"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


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
