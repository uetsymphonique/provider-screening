"""Stage a bot-protected page via r.jina.ai markdown render (fallback for pages
whose HTML mode hits the Incapsula challenge). Mirrors stage_proxied_html.py's
manifest contract: origin = ORIGINAL URL, raw markdown persisted, sha256 anchor."""
import argparse, hashlib, json, sys, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PROXY = "https://r.jina.ai/"

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--product", required=True)
    ap.add_argument("--domain", default="bsg")
    ap.add_argument("--slug", default=None)
    args = ap.parse_args()

    staging_dir = REPO_ROOT / args.domain / "runs" / args.product / "artifacts"
    staging_dir.mkdir(parents=True, exist_ok=True)

    proxy_url = PROXY + args.url
    req = urllib.request.Request(proxy_url, headers={"User-Agent": "Mozilla/5.0 (provider-screening stage_md_proxied.py)"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = resp.read()

    parsed = urllib.parse.urlparse(args.url)
    basename = [p for p in parsed.path.split("/") if p][-1] if parsed.path.split("/") else parsed.netloc
    url_hash = hashlib.sha256(args.url.encode("utf-8")).hexdigest()[:8]
    slug = args.slug or f"{slugify(basename)}-{url_hash}"
    def slugify(v):
        import re
        return re.sub(r"[^A-Za-z0-9]+", "-", v).strip("-").lower() or "page"

    html_path = staging_dir / f"{slug}.html"   # holds raw markdown render
    txt_path = staging_dir / f"{slug}.txt"
    html_path.write_bytes(data)
    text = data.decode("utf-8", errors="replace")
    txt_path.write_text(text, encoding="utf-8")

    def sha256_file(path):
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()

    captured_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    entry = {
        "captured_at": captured_at,
        "kind": "html",
        "origin": args.url,
        "via_proxy": True,
        "proxy_url": proxy_url,
        "render_mode": "markdown",
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
    print(str(txt_path.resolve()))
    return 0

if __name__ == "__main__":
    sys.exit(main())
