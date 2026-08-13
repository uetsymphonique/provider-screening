"""Single source of truth for the domain registry (bsg, microsegmentation, ngfw, ...).

Consumed by scripts/pdf_to_text.py, scripts/htmlstage/html_to_text.py,
scripts/batch/common.py, and .claude/skills/provider-assessment/scripts/constants.py
(which re-exports DOMAINS/domain_dir/domain_paths for its own consumers). Adding a
new domain means adding one entry to DOMAINS here plus a CSV under providers/ - see
guides/append-provider-groups.md.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

DOMAINS = {
    "bsg": {
        "csv": REPO_ROOT / "providers" / "BSG.csv",
        "dir": REPO_ROOT / "bsg",
    },
    "microsegmentation": {
        "csv": REPO_ROOT / "providers" / "Microsegmentation.csv",
        "dir": REPO_ROOT / "microsegmentation",
    },
    "ngfw": {
        "csv": REPO_ROOT / "providers" / "NGFW.csv",
        "dir": REPO_ROOT / "ngfw",
    },
}


def domain_dir(domain: str) -> Path:
    """Per-domain folder (checklist.yaml, runs/, outputs live here)."""
    return DOMAINS[domain]["dir"]


def domain_paths(domain: str) -> dict[str, Path]:
    d = domain_dir(domain)
    return {
        "runs": d / "runs",
        "checklist": d / "checklist.yaml",
        "out": d,
    }
