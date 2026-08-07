"""End-to-end pipeline orchestrator: screen -> promote -> standard -> render -> aggregate.

Runs the full vendor-screening pipeline for ONE domain, start to finish. The
only CLI argument is --domain — every run_batch.py knob (model/timeout/
permissions) is hard-coded in PIPELINE_* below so a pipeline run is
reproducible and can't silently drift between invocations. Edit the constants
directly if the fixed settings need to change.

Stages:
  1. screen    — run_batch.py --mode screen over the FULL domain CSV (--skip-done)
  2. promote   — <domain>/scripts/promote_to_deep.py buckets gate decisions into
                 <domain>/decisions/{deep_queue,needs_more_info,dropped}.txt
  3. standard  — run_batch.py --mode standard over deep_queue.txt (--skip-done)
  4. render    — <domain>/scripts/render_report.py for every product in
                 deep_queue.txt that has an assessment.json
  5. aggregate — <domain>/scripts/aggregate_matrix.py (comparison_matrix.csv,
                 coverage_summary.csv across everything assessed so far)

Usage:
    venv/Scripts/python.exe scripts/run_pipeline.py --domain bsg
    venv/Scripts/python.exe scripts/run_pipeline.py --domain microsegmentation

Any stage failing (non-zero exit, except a single product's render_report.py)
aborts the pipeline. --skip-done in stages 1 and 3 means already-completed
products are not re-billed on a re-run.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VENV_PY = REPO_ROOT / "venv" / "Scripts" / "python.exe"
PYTHON = str(VENV_PY) if VENV_PY.exists() else sys.executable

DOMAINS = ["microsegmentation", "bsg"]

# Fixed run_batch.py settings applied to BOTH the screen and standard stages
# of a pipeline run — intentionally not exposed as CLI flags so every
# pipeline run uses the same, already-agreed settings.
PIPELINE_TIMEOUT = 3600
PIPELINE_MODEL = "deepseek-v4-pro"
PIPELINE_SKIP_PERMISSIONS = True


def run_step(title: str, cmd: list[str]) -> int:
    print()
    print("=" * 100)
    print(f"STEP: {title}")
    print(f"$ {' '.join(cmd)}")
    print("=" * 100)
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT))
    return proc.returncode


def run_batch(domain: str, mode: str, extra: list[str]) -> int:
    cmd = [
        PYTHON, str(REPO_ROOT / "scripts" / "run_batch.py"),
        "--domain", domain,
        "--mode", mode,
        "--skip-done",
        "--timeout", str(PIPELINE_TIMEOUT),
        "--model", PIPELINE_MODEL,
    ]
    if PIPELINE_SKIP_PERMISSIONS:
        cmd.append("--dangerously-skip-permissions")
    cmd.extend(extra)
    return run_step(f"run_batch.py --mode {mode}", cmd)


def load_queue(path: Path) -> list[str]:
    if not path.exists():
        return []
    pids = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if line:
            pids.append(line)
    return pids


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--domain", choices=DOMAINS, required=True,
                     help="Which project (checklist/prompts/runs tree) to run the full pipeline for.")
    args = ap.parse_args()

    domain = args.domain
    domain_dir = REPO_ROOT / domain
    scripts_dir = domain_dir / "scripts"
    decisions_dir = domain_dir / "decisions"
    runs_dir = domain_dir / "runs"
    deep_queue = decisions_dir / "deep_queue.txt"

    print(f"=== pipeline start: domain={domain}  model={PIPELINE_MODEL}  "
          f"timeout={PIPELINE_TIMEOUT}s  skip_permissions={PIPELINE_SKIP_PERMISSIONS} ===")

    # 1. screen — full CSV
    rc = run_batch(domain, "screen", [])
    if rc != 0:
        print(f"ABORT: screen stage failed (exit {rc})", file=sys.stderr)
        return rc

    # 2. promote — bucket gate decisions into decisions/*.txt
    rc = run_step("promote_to_deep.py",
                  [PYTHON, str(scripts_dir / "promote_to_deep.py")])
    if rc != 0:
        print(f"ABORT: promote stage failed (exit {rc})", file=sys.stderr)
        return rc

    queue_pids = load_queue(deep_queue)
    if not queue_pids:
        print(f"no product advanced to deep (empty {deep_queue.relative_to(REPO_ROOT)}) — "
              f"skipping standard/render/aggregate stages")
        return 0

    # 3. standard — deep_queue.txt only
    rc = run_batch(domain, "standard", ["--queue-file", str(deep_queue)])
    if rc != 0:
        print(f"ABORT: standard stage failed (exit {rc})", file=sys.stderr)
        return rc

    # 4. render — per-product report.md (mechanical sections). A single
    #    product's render failure is reported but does not abort the batch.
    render_failures = []
    for pid in queue_pids:
        assessment = runs_dir / pid / "assessment.json"
        if not assessment.exists():
            print(f"[render] skip {pid}: no assessment.json")
            continue
        rc = run_step(f"render_report.py {pid}",
                      [PYTHON, str(scripts_dir / "render_report.py"), str(assessment)])
        if rc != 0:
            render_failures.append(pid)

    # 5. aggregate — comparison matrix across everything assessed so far
    rc = run_step("aggregate_matrix.py",
                  [PYTHON, str(scripts_dir / "aggregate_matrix.py")])
    if rc != 0:
        print(f"WARN: aggregate stage failed (exit {rc})", file=sys.stderr)

    print()
    print("=" * 100)
    print(f"pipeline done: domain={domain}  advanced-to-deep={len(queue_pids)}  "
          f"render_failures={len(render_failures)}")
    if render_failures:
        print(f"  failed render: {render_failures}", file=sys.stderr)
    print("=" * 100)
    return 1 if render_failures else 0


if __name__ == "__main__":
    sys.exit(main())
