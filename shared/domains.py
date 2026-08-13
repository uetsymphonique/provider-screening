"""Single source of truth for the domain registry (bsg, microsegmentation, ngfw, ...).

Part of the `shared` package (see pyproject.toml, `pip install -e .`), so any
module in this repo can `from shared.domains import DOMAINS` without manual
sys.path edits. Consumed by tools/pdfstage/main.py, tools/htmlstage/main.py,
scripts/batch/core/common.py, and .claude/skills/provider-assessment/scripts/constants.py
(which re-exports DOMAINS/domain_dir/domain_paths for its own consumers). Adding a
new domain means adding one entry to DOMAINS here plus a CSV under providers/ - see
guides/append-provider-groups.md.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROVIDERS_WORKSPACE = REPO_ROOT / "providers-workspace"

DOMAINS = {
    "bsg": {
        "csv": REPO_ROOT / "providers" / "BSG.csv",
        "dir": PROVIDERS_WORKSPACE / "bsg",
    },
    "microsegmentation": {
        "csv": REPO_ROOT / "providers" / "Microsegmentation.csv",
        "dir": PROVIDERS_WORKSPACE / "microsegmentation",
    },
    "ngfw": {
        "csv": REPO_ROOT / "providers" / "NGFW.csv",
        "dir": PROVIDERS_WORKSPACE / "ngfw",
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
