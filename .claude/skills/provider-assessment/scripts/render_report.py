"""Regenerate report.md's mechanical sections from assessment.json (+ sources.jsonl
+ evidence.jsonl + run_manifest.json), which are already validated/structured data.

Only 4 sections in the standard/deep template require free-text synthesis that a
script cannot produce: "1. Overview", "4. Notable Strengths", "5. Notable Gaps /
Risks", "6. Evidence Quality Notes". Everything else (header metadata, verdict
summary table, per-item verdict tables, bibliography, appendix stats) is derived
deterministically here so it can never drift from assessment.json.

Behavior on rerun: if an existing report.md is found at the output path, its
narrative sections are extracted and carried over verbatim so re-running this
script after fixing/re-validating assessment.json never destroys prior prose.
Missing narrative sections are left as the template's own placeholder text so
it's obvious what still needs to be written.

Shared across domains (bsg, microsegmentation, ...). The domain's checklist.yaml
and runs/ tree are resolved from --domain; templates live in the skill.

Usage:
    python .claude/skills/provider-assessment/scripts/render_report.py \
        --domain bsg <path/to/assessment.json>
        [--checklist <path>]            # default: providers-workspace/<domain>/checklist.yaml
        [--templates-dir <dir>]         # default: skill templates/
        [--out <path/to/report.md>]     # default: sibling report.md next to assessment.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

try:
    from .constants import DOMAINS, SKILL_ROOT, domain_paths
except ImportError:
    _parent = Path(__file__).resolve().parent
    sys.path.insert(0, str(_parent))
    from constants import DOMAINS, SKILL_ROOT, domain_paths  # type: ignore[no-redef]


VERDICT_BADGE = {
    "supported": "Supported",
    "partial": "Partial",
    "not_supported": "Not Supported",
    "unknown": "Unknown",
    "not_applicable": "N/A",
}
VERDICT_ORDER = ["supported", "partial", "not_supported", "unknown", "not_applicable"]
CONFIDENCE_ORDER = ["high", "medium", "low"]
VENDOR_ONLY_TYPES = {"vendor_doc", "vendor_datasheet", "vendor_blog"}

# Sections a human/LLM writes by hand; preserved verbatim across regenerations.
NARRATIVE_HEADINGS = {
    "1. Overview",
    "4. Notable Strengths",
    "5. Notable Gaps / Risks",
    "6. Evidence Quality Notes",
}


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def parse_old_bibliography_numbers(old_text: str) -> dict[str, int]:
    """Map raw_url -> display number, parsed from an existing report.md's
    Bibliography section. Preserved narrative sections (1, 4, 5, 6) contain
    hand-written [N] citations baked in as literal text - if the bibliography
    were renumbered on every regeneration, those citations would silently point
    at the wrong source. Reusing old numbers keeps them valid."""
    if not old_text:
        return {}
    parts = re.split(r"(?m)^## (.+)$", old_text)
    body = ""
    for i in range(1, len(parts), 2):
        if parts[i].strip() == "Bibliography":
            body = parts[i + 1]
            break
    mapping: dict[str, int] = {}
    for line in body.splitlines():
        num_match = re.match(r"\[(\d+)\]", line.strip())
        url_match = re.search(r"(https?://\S+)", line)
        if num_match and url_match:
            url = url_match.group(1).rstrip("<>().,;:")
            mapping[url] = int(num_match.group(1))
    return mapping


def build_source_display_map(sources: list[dict], old_text: str = "") -> dict[str, int]:
    """Display numbers in first-registration order, EXCEPT a source whose URL
    already had a number in the previous report.md keeps that number (see
    parse_old_bibliography_numbers)."""
    old_by_url = parse_old_bibliography_numbers(old_text)
    mapping: dict[str, int] = {}
    used_numbers: set[int] = set()

    for src in sources:
        sid = src["source_id"]
        if sid in mapping:
            continue
        n = old_by_url.get(src.get("raw_url", ""))
        if n is not None and n not in used_numbers:
            mapping[sid] = n
            used_numbers.add(n)

    next_n = 1
    for src in sources:
        sid = src["source_id"]
        if sid in mapping:
            continue
        while next_n in used_numbers:
            next_n += 1
        mapping[sid] = next_n
        used_numbers.add(next_n)

    return mapping


def cite(source_ids: list[str], display_map: dict[str, int]) -> str:
    nums = sorted({display_map[sid] for sid in source_ids if sid in display_map})
    return ", ".join(f"[{n}]" for n in nums)


def render_bibliography(sources: list[dict], display_map: dict[str, int]) -> str:
    if not sources:
        return "[1] ...\n[2] ..."
    by_number = sorted(display_map.items(), key=lambda kv: kv[1])
    by_id = {s["source_id"]: s for s in sources}
    lines = []
    for sid, n in by_number:
        src = by_id.get(sid, {})
        publisher = src.get("publisher") or "Unknown"
        title = src.get("title", "Untitled")
        url = src.get("raw_url", "")
        captured = src.get("captured_at", "")
        lines.append(f'[{n}] {publisher}. "{title}". {url} (Retrieved: {captured})')
    return "\n".join(lines)


def normalize_heading(heading: str) -> str:
    """Strip a trailing editorial annotation like '(<= 200 words)' so the same
    logical section matches whether or not that guidance text is present -
    the template carries it on section 1, but written reports typically drop it."""
    return re.sub(r"\s*\([^)]*\)\s*$", "", heading).strip()


def extract_narrative_sections(old_text: str) -> dict[str, str]:
    """Split an existing report.md by top-level '## ' headings and keep only the
    bodies of headings in NARRATIVE_HEADINGS, verbatim, stripped of any trailing
    '---' separator (the assembler re-inserts separators itself)."""
    if not old_text:
        return {}
    parts = re.split(r"(?m)^## (.+)$", old_text)
    # parts[0] is preamble before first '## '; then alternating [heading, body, heading, body, ...]
    sections: dict[str, str] = {}
    for i in range(1, len(parts), 2):
        heading = normalize_heading(parts[i])
        body = parts[i + 1] if i + 1 < len(parts) else ""
        if heading in NARRATIVE_HEADINGS:
            body = re.sub(r"\n*^---\s*$", "", body, flags=re.MULTILINE)
            sections[heading] = body.strip("\n")
    return sections


def placeholder_for(heading: str, template_text: str) -> str:
    """Pull the placeholder body for `heading` straight out of the template file,
    so if the template's guidance text changes, placeholders stay in sync."""
    parts = re.split(r"(?m)^## (.+)$", template_text)
    for i in range(1, len(parts), 2):
        if normalize_heading(parts[i]) == heading:
            body = parts[i + 1] if i + 1 < len(parts) else ""
            body = re.sub(r"\n*^---\s*$", "", body, flags=re.MULTILINE)
            return body.strip("\n")
    return "\n[TODO: not found in template]\n"


# ---------------------------------------------------------------------------
# Standard / deep mode
# ---------------------------------------------------------------------------


def render_verdict_summary(items: list[dict]) -> str:
    counts = {v: 0 for v in VERDICT_ORDER}
    conf_counts = {v: {c: 0 for c in CONFIDENCE_ORDER} for v in VERDICT_ORDER}
    for it in items:
        v = it.get("verdict")
        if v in counts:
            counts[v] += 1
            c = it.get("confidence")
            if c in CONFIDENCE_ORDER:
                conf_counts[v][c] += 1

    rows = ["| Verdict          | Count | Confidence: high | medium | low |",
            "|------------------|-------|------------------|--------|-----|"]
    for v in VERDICT_ORDER:
        cc = conf_counts[v]
        rows.append(
            f"| {v:<16} | {counts[v]:<5} | {cc['high']:<16} | {cc['medium']:<6} | {cc['low']:<3} |"
        )

    triangulated = sum(1 for it in items if len(set(it.get("source_types") or [])) >= 2)
    vendor_only = sum(
        1
        for it in items
        if it.get("source_types") and all(st in VENDOR_ONLY_TYPES for st in it["source_types"])
    )

    lines = [f"**Counts across {len(items)} checklist items:**", "", *rows, ""]
    lines.append(
        f"**Evidence quality:** {triangulated} items backed by ≥ 2 source_types; "
        f"{vendor_only} items backed by vendor_doc only (confidence capped at medium per validator rule)."
    )

    na_items = [it for it in items if it.get("verdict") == "not_applicable" and it.get("notes")]
    if na_items:
        lines.append("")
        lines.append("**Not-applicable items:**")
        for it in na_items:
            lines.append(f"- **{it['item_id']}:** {it['notes']}")

    return "\n".join(lines)


def render_per_item_tables(items: list[dict], checklist: dict, display_map: dict[str, int]) -> str:
    by_id = {it["item_id"]: it for it in items}
    checklist_items = checklist["items"]
    categories = checklist["categories"]

    chunks = []
    for cat in categories:
        cat_id = cat["id"]
        cat_items = [ci for ci in checklist_items if ci["category"] == cat_id]
        if not cat_items:
            continue
        chunks.append(f"### Category {cat_id} - {cat['name']}")
        chunks.append("")
        chunks.append("| ID  | Requirement | Verdict | Conf | Value | Evidence |")
        chunks.append("|-----|-------------|:-------:|:----:|-------|----------|")
        for ci in cat_items:
            item = by_id.get(ci["id"])
            if item is None:
                chunks.append(f"| {ci['id']} | {ci['requirement']} | - | - | - | not evaluated |")
                continue

            verdict = item.get("verdict", "unknown")
            badge = VERDICT_BADGE.get(verdict, "?")
            conf = item.get("confidence") or "-"

            if ci.get("verdict_type") == "numeric_threshold" and item.get("numeric_value") is not None:
                value = f"{item['numeric_value']} {item.get('unit', '')}".strip()
            elif ci.get("verdict_type") == "numeric_threshold" and verdict == "partial":
                value = "n/a (qualitative)"
            else:
                value = "-"

            if verdict == "unknown":
                gaps = item.get("gaps")
                evidence = f"no evidence found ({gaps})" if gaps else "no evidence found"
            else:
                notes = item.get("notes") or ""
                citation = cite(item.get("cited_source_ids") or [], display_map)
                evidence = f"{notes} {citation}".strip() if citation else notes

            # Escape pipes so table cells don't break.
            req = ci["requirement"].replace("|", "\\|")
            evidence = evidence.replace("|", "\\|")
            chunks.append(f"| {ci['id']} | {req} | {badge} | {conf} | {value} | {evidence} |")
        chunks.append("")
    return "\n".join(chunks).rstrip("\n")


def render_appendix_a(assessment: dict, sources: list[dict], run_manifest: dict) -> str:
    type_counts: dict[str, int] = {}
    for s in sources:
        t = s.get("source_type", "unknown")
        type_counts[t] = type_counts.get(t, 0) + 1
    dist = ", ".join(f"{k}: {v}" for k, v in sorted(type_counts.items())) or "n/a"

    lines = [
        f"- **Research mode used:** {assessment.get('assessment_mode', 'n/a')}",
        f"- **Queries executed:** {run_manifest.get('queries_executed', 'n/a (not tracked)')}",
        f"- **Sources reviewed:** {len(sources)} (kept: {len(sources)}, discarded for low credibility: n/a (not tracked))",
        f"- **Source_types distribution:** {dist}",
        "- **Verify script results:** see validate_assessment.py output for this run",
    ]
    return "\n".join(lines)


def render_standard(assessment: dict, checklist: dict, sources: list[dict],
                     evidence: list[dict], run_manifest: dict, template_text: str,
                     old_text: str) -> str:
    items = assessment["items"]
    display_map = build_source_display_map(sources, old_text)
    preserved = extract_narrative_sections(old_text)

    def narrative(heading: str) -> str:
        return preserved.get(heading) or placeholder_for(heading, template_text)

    title_line = template_text.splitlines()[0]
    title = title_line.replace("{VENDOR}", assessment.get("vendor", "")).replace(
        "{PRODUCT_NAME}", assessment.get("product_name", "")
    )

    out = [
        title,
        "",
        f"**Product ID:** `{assessment['product_id']}`",
        f"**Version reference:** {assessment.get('product_version_reference') or 'n/a'}",
        f"**Assessment mode:** {assessment['assessment_mode']}",
        f"**Checklist version:** {assessment['checklist_version']}",
        f"**Assessed at:** {assessment.get('assessed_at', 'n/a')}",
        f"**Total evidence items collected:** {len(evidence)}",
        f"**Total distinct sources:** {len(sources)}",
        "",
        "---",
        "",
        "## 1. Overview",
        "",
        narrative("1. Overview"),
        "",
        "---",
        "",
        "## 2. Verdict Summary",
        "",
        render_verdict_summary(items),
        "",
        "---",
        "",
        "## 3. Per-Item Verdicts",
        "",
        render_per_item_tables(items, checklist, display_map),
        "",
        "---",
        "",
        "## 4. Notable Strengths",
        "",
        narrative("4. Notable Strengths"),
        "",
        "## 5. Notable Gaps / Risks",
        "",
        narrative("5. Notable Gaps / Risks"),
        "",
        "## 6. Evidence Quality Notes",
        "",
        narrative("6. Evidence Quality Notes"),
        "",
        "---",
        "",
        "## Bibliography",
        "",
        render_bibliography(sources, display_map),
        "",
        "---",
        "",
        "## Appendix A - Methodology",
        "",
        render_appendix_a(assessment, sources, run_manifest),
        "",
        "## Appendix B - Machine-readable outputs",
        "",
        "Companion files in this run directory:",
        "- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)",
        "- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill",
        "- `run_manifest.json` - research config and provenance",
        "",
    ]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("assessment", type=Path)
    ap.add_argument("--domain", required=True, choices=list(DOMAINS))
    ap.add_argument("--checklist", type=Path, default=None)
    ap.add_argument("--templates-dir", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()

    paths = domain_paths(args.domain)
    checklist_path = args.checklist or paths["checklist"]
    templates_dir = args.templates_dir or (SKILL_ROOT / "templates")

    assessment = load_json(args.assessment)
    checklist = load_yaml(checklist_path)
    run_dir = args.assessment.parent
    sources = read_jsonl(run_dir / "sources.jsonl")
    evidence = read_jsonl(run_dir / "evidence.jsonl")
    run_manifest = {}
    if (run_dir / "run_manifest.json").exists():
        run_manifest = load_json(run_dir / "run_manifest.json")

    out_path = args.out or (run_dir / "report.md")
    old_text = out_path.read_text(encoding="utf-8") if out_path.exists() else ""

    template_text = (templates_dir / "product_report.md").read_text(encoding="utf-8")
    rendered = render_standard(assessment, checklist, sources, evidence, run_manifest,
                                template_text, old_text)

    out_path.write_text(rendered, encoding="utf-8")
    print(f"OK   wrote {out_path} (mode={assessment.get('assessment_mode')})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
