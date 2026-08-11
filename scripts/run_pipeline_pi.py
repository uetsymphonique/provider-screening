"""End-to-end pipeline orchestrator (pi edition): screen → promote → standard → render → aggregate.

Same logic as run_pipeline.py but calls run_batch_pi.py instead of run_batch.py.
All stage logic, promotion, render, and aggregation are identical.

Stages:
  1. screen    — run_batch_pi.py --mode screen over the FULL domain CSV (--skip-done)
  2. promote   — <domain>/scripts/promote_to_deep.py buckets gate decisions
  3. standard  — run_batch_pi.py --mode standard over deep_queue.txt (--skip-done)
  4. render    — <domain>/scripts/render_report.py for every product
  5. aggregate — <domain>/scripts/aggregate_matrix.py

Usage:
    venv/Scripts/python.exe scripts/run_pipeline_pi.py --domain bsg
    venv/Scripts/python.exe scripts/run_pipeline_pi.py --domain microsegmentation
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

# Fixed settings for BOTH screen and standard stages
PIPELINE_TIMEOUT = 3600
PIPELINE_MODEL = "deepseek/deepseek-v4-pro"


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
        PYTHON, str(REPO_ROOT / "scripts" / "run_batch_pi.py"),
        "--domain", domain,
        "--mode", mode,
        "--skip-done",
        "--timeout", str(PIPELINE_TIMEOUT),
        "--model", PIPELINE_MODEL,
    ]
    cmd.extend(extra)
    return run_step(f"run_batch_pi.py --mode {mode}", cmd)


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
                    help="Which project to run the full pipeline for.")
    args = ap.parse_args()

    domain = args.domain
    domain_dir = REPO_ROOT / domain
    scripts_dir = domain_dir / "scripts"
    decisions_dir = domain_dir / "decisions"
    runs_dir = domain_dir / "runs"
    deep_queue = decisions_dir / "deep_queue.txt"

    print(f"=== pipeline start (pi)  domain={domain}  model={PIPELINE_MODEL}  "
          f"timeout={PIPELINE_TIMEOUT}s ===")

    # 1. screen — full CSV
    rc = run_batch(domain, "screen", [])
    if rc != 0:
        print(f"ABORT: screen stage failed (exit {rc})", file=sys.stderr)
        return rc

    # 2. promote
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

    # 4. render
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

    # 5. aggregate
    rc = run_step("aggregate_matrix.py",
                  [PYTHON, str(scripts_dir / "aggregate_matrix.py")])
    if rc != 0:
        print(f"WARN: aggregate stage failed (exit {rc})", file=sys.stderr)

    print()
    print("=" * 100)
    print(f"pipeline done (pi)  domain={domain}  advanced-to-deep={len(queue_pids)}  "
          f"render_failures={len(render_failures)}")
    if render_failures:
        print(f"  failed render: {render_failures}", file=sys.stderr)
    print("=" * 100)
    return 1 if render_failures else 0


if __name__ == "__main__":
    sys.exit(main())
