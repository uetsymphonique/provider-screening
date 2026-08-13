"""Batch-run standard-mode assessment across a product list, for any code agent.

    python scripts/batch/run_batch.py claude --domain <domain> --mode standard ...
    python scripts/batch/run_batch.py pi     --domain <domain> --mode standard ...

Mode:
  --mode standard → runs the shared skill's prompt
                    (.claude/skills/provider-assessment/prompts/standard_mode.md)
                    against the domain's vendor CSV.

For each product:
  1. Render the mode-specific prompt template with {DOMAIN}, {VENDOR},
     {PRODUCT_NAME}, {product_id}.
  2. Spawn a FRESH agent session (no prior context) with the project's
     skills auto-loaded (cwd = repo root).
  3. Stream the full trace into runs/<pid>/<agent>_run.jsonl.
  4. Run validate_assessment.py against the produced assessment.json and
     record the outcome in runs/<pid>/<agent>_run.meta.json.

--skip-done skips a product only when its existing assessment.json is in the
SAME mode as the current run (so a partial pass doesn't block a re-run).

--concurrency N runs up to N products in parallel (ThreadPoolExecutor). Any
concurrency > 1 forces quiet=True for every product regardless of --quiet, so
the --overwrite line-window (which redraws via ANSI cursor moves) is never
driven by more than one thread at a time.

Agent-specific behavior (CLI invocation, stream-event schema, meta fields)
lives in scripts/batch/handlers/*; everything else is shared in
scripts/batch/{common,driver}.py.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from batch import driver  # noqa: E402
from batch.handlers import HANDLERS, get_handler  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="agent", required=True, metavar="AGENT",
                             help=f"Code agent to drive: {', '.join(HANDLERS)}")
    for agent_name, handler_cls in HANDLERS.items():
        handler = handler_cls()
        agent_parser = sub.add_parser(agent_name, help=f"Drive `{agent_name}` for each product")
        driver.add_common_arguments(agent_parser)
        handler.add_arguments(agent_parser)

    args = ap.parse_args()
    handler = get_handler(args.agent)
    return driver.run_batch(handler, args)


if __name__ == "__main__":
    sys.exit(main())
