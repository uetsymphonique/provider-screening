"""Check whether evidence.jsonl quotes are actually grounded in fetched source text.

Purpose:
  `validate_assessment.py` only checks REFERENTIAL integrity: does
  evidence_id exist in evidence.jsonl, does source_id exist in sources.jsonl.
  It never compares an evidence.quote against the text that was actually
  fetched -- so a model can invent a plausible-sounding quote and attribute
  it to a real source_id, and the validator passes. That failure mode was
  confirmed empirically on bsg/runs/zoneguard: ~6 evidence entries cited
  quotes (SIEM/SNMP integration, "four-eyes" governance, database proxy
  support, etc.) that do not appear anywhere on the cited vendor pages,
  across items whose verdict rested entirely on that fabricated evidence.

  This script closes that gap using the ground truth pdf_to_text.py /
  html_to_text.py already stage: artifacts/manifest.jsonl maps each fetched
  source's origin URL to a persisted .txt file with a sha256 anchor. For
  every evidence entry whose source was staged, this script normalizes and
  substring-matches the quote (split on "..." so legitimately elided quotes
  are checked fragment-by-fragment) against that persisted text.

  Evidence citing a source that was NEVER staged (no pdf_to_text.py /
  html_to_text.py run for it -- e.g. WebFetch was used directly, skipping
  the mandated staging step) is reported separately as UNVERIFIABLE, not as
  grounded or fabricated -- there is no ground truth to check it against.
  A high UNVERIFIABLE rate means the prompt's staging requirement isn't
  being followed, which is itself worth flagging.

Status per evidence entry:
  grounded      every quote fragment found verbatim (normalized) in the
                staged text for its source_id
  fabricated    source WAS staged, but >=1 quote fragment is absent from it
                (fully_fabricated: 0/N fragments found; partial: some found)
  unverifiable  source_id has no staged artifact to check against

Usage:
  python scripts/verify_citation_grounding.py --dir bsg/runs/zoneguard
  python scripts/verify_citation_grounding.py --dir bsg/runs/zoneguard --strict
  python scripts/verify_citation_grounding.py --dir bsg/runs/zoneguard --json

--strict exits 1 if any evidence is `fabricated` (unverifiable does not fail
by default -- pass --require-staged to also fail on unverifiable, once the
prompt-level staging requirement is actually enforced upstream).
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.parse
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.exists():
        return rows
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def normalize(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_url(url: str) -> str:
    """Loose match key: scheme+host+path(+query) with trailing slash / case ignored.

    Query strings are kept because two URLs that differ only in query (e.g.
    support-portal document pages) point at different documents; collapsing
    them onto one key would route evidence to the wrong staged text.
    """
    if url.startswith("local:"):
        return url
    p = urllib.parse.urlparse(url.strip())
    path = p.path.rstrip("/")
    if p.query:
        return f"{p.netloc.lower()}{path}?{p.query}"
    return f"{p.netloc.lower()}{path}"


def load_staged_texts(run_dir: Path) -> dict[str, tuple[str, dict]]:
    """Return {normalized_origin_url: (normalized_text, manifest_entry)}."""
    manifest = read_jsonl(run_dir / "artifacts" / "manifest.jsonl")
    staged: dict[str, tuple[str, dict]] = {}
    for entry in manifest:
        origin = entry.get("origin", "")
        txt_name = entry.get("txt_path")
        if not txt_name:
            continue
        txt_path = run_dir / "artifacts" / txt_name
        if not txt_path.exists():
            continue
        text = normalize(txt_path.read_text(encoding="utf-8"))
        staged[normalize_url(origin)] = (text, entry)
    return staged


def check_evidence(
    evidence: list[dict],
    sources_by_id: dict[str, dict],
    staged: dict[str, tuple[str, dict]],
) -> list[dict]:
    results = []
    for e in evidence:
        eid = e.get("evidence_id", "")
        item_id = e.get("item_id", "")
        source_id = e.get("source_id", "")
        quote = e.get("quote", "")

        src = sources_by_id.get(source_id)
        raw_url = (src or {}).get("raw_url", "")
        key = normalize_url(raw_url) if raw_url else None
        staged_entry = staged.get(key) if key else None

        if staged_entry is None:
            results.append({
                "evidence_id": eid, "item_id": item_id, "source_id": source_id,
                "status": "unverifiable", "quote": quote,
                "reason": "source not staged via pdf_to_text.py / html_to_text.py "
                          f"(raw_url={raw_url!r})",
            })
            continue

        text, manifest_entry = staged_entry
        fragments = [f.strip() for f in quote.split("...") if f.strip()]
        if not fragments:
            fragments = [quote.strip()]
        frag_status = [(f, normalize(f) in text) for f in fragments]
        n_found = sum(1 for _, ok in frag_status if ok)

        if n_found == len(frag_status):
            status = "grounded"
        elif n_found == 0:
            status = "fabricated"
        else:
            status = "fabricated"  # partial fabrication still fails grounding

        results.append({
            "evidence_id": eid, "item_id": item_id, "source_id": source_id,
            "status": status, "quote": quote,
            "fragments": [{"text": f, "found": ok} for f, ok in frag_status],
            "artifact": manifest_entry.get("txt_path"),
            "artifact_sha256": manifest_entry.get("sha256"),
        })
    return results


def load_item_verdicts(run_dir: Path) -> dict[str, dict]:
    assessment_path = run_dir / "assessment.json"
    if not assessment_path.exists():
        return {}
    data = json.loads(assessment_path.read_text(encoding="utf-8"))
    return {item["item_id"]: item for item in data.get("items", [])}


def render_report(results: list[dict], items: dict[str, dict]) -> str:
    lines = []
    counts = {"grounded": 0, "fabricated": 0, "unverifiable": 0}
    for r in results:
        counts[r["status"]] += 1

    lines.append("# Citation grounding report")
    lines.append("")
    lines.append(f"**Total evidence entries:** {len(results)}")
    lines.append(f"**By status:** {counts}")
    lines.append("")

    fabricated = [r for r in results if r["status"] == "fabricated"]
    if fabricated:
        lines.append("## Fabricated (source staged, quote fragment(s) absent from it)")
        lines.append("")
        affected_items = sorted({r["item_id"] for r in fabricated})
        lines.append(f"Affects checklist item(s): {', '.join(affected_items)}")
        lines.append("")
        for r in fabricated:
            verdict = items.get(r["item_id"], {})
            v_note = (f"  [item verdict={verdict.get('verdict')!r} "
                      f"confidence={verdict.get('confidence')!r}]") if verdict else ""
            lines.append(f"- `{r['evidence_id']}` item={r['item_id']} source={r['source_id']}{v_note}")
            for frag in r["fragments"]:
                mark = "OK" if frag["found"] else "MISSING"
                lines.append(f"    [{mark}] {frag['text']}")
        lines.append("")

    unverifiable = [r for r in results if r["status"] == "unverifiable"]
    if unverifiable:
        lines.append("## Unverifiable (source never staged -- no ground truth to check)")
        lines.append("")
        for r in unverifiable:
            lines.append(f"- `{r['evidence_id']}` item={r['item_id']} source={r['source_id']}: {r['reason']}")
        lines.append("")

    if not fabricated and not unverifiable:
        lines.append("## All evidence grounded in staged source text.")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dir", required=True, type=Path,
                     help="Run directory, e.g. bsg/runs/zoneguard "
                          "(must contain sources.jsonl, evidence.jsonl, artifacts/manifest.jsonl).")
    ap.add_argument("--strict", action="store_true",
                     help="Exit 1 if any evidence is `fabricated`.")
    ap.add_argument("--require-staged", action="store_true",
                     help="Also exit 1 on `unverifiable` evidence (source never staged). "
                          "Only meaningful once prompts mandate staging every cited source.")
    ap.add_argument("--json", action="store_true", help="Print raw JSON instead of the report.")
    args = ap.parse_args()

    run_dir = args.dir
    if not run_dir.exists():
        print(f"ERROR: {run_dir} does not exist", file=sys.stderr)
        return 1

    sources = read_jsonl(run_dir / "sources.jsonl")
    evidence = read_jsonl(run_dir / "evidence.jsonl")
    sources_by_id = {s["source_id"]: s for s in sources if "source_id" in s}
    staged = load_staged_texts(run_dir)
    items = load_item_verdicts(run_dir)

    results = check_evidence(evidence, sources_by_id, staged)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(render_report(results, items))

    n_fabricated = sum(1 for r in results if r["status"] == "fabricated")
    n_unverifiable = sum(1 for r in results if r["status"] == "unverifiable")

    failed = (args.strict and n_fabricated > 0) or (args.require_staged and n_unverifiable > 0)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
