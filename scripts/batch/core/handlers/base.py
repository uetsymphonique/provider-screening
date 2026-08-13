"""Abstract interface every code-agent handler implements.

scripts/batch/core/driver.py drives a run using only this interface - it never
branches on agent name. See scripts/batch/core/handlers/claude_handler.py and
pi_handler.py for the two current implementations.
"""

from __future__ import annotations

import argparse
from abc import ABC, abstractmethod
from pathlib import Path


class AgentHandler(ABC):
    name: str
    log_filename: str
    meta_filename: str
    summary_prefix: str

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Add agent-only CLI flags to this agent's subparser. Default: none."""

    @abstractmethod
    def find_binary(self) -> str:
        """Locate the agent CLI on PATH, or raise SystemExit with a clear message."""

    @abstractmethod
    def write_prompt_file(self, run_dir: Path, prompt_text: str) -> None:
        """Persist the rendered prompt under run_dir (record and/or @file input)."""

    @abstractmethod
    def build_command(self, run_dir: Path, prompt_text: str, args: argparse.Namespace) -> list[str]:
        """Build the subprocess argv for one product run."""

    def describe_run(self, prompt_text: str, args: argparse.Namespace) -> str:
        """Trailing detail fragment for the "[pid] start <iso>  <details>" console line."""
        return f"prompt={len(prompt_text)}B  model={args.model or 'default'}"

    @abstractmethod
    def summarize_event(self, ev: dict) -> str | tuple[str, str] | None:
        """One-line progress summary for a stream event, or None to skip it.

        May return ("text", delta) for streaming text chunks that the caller
        should buffer and flush as a single line rather than one-per-token -
        driver.py handles that buffering generically for any handler.
        """

    @abstractmethod
    def parse_result(self, log_path: Path) -> dict | None:
        """Scan the written log for the final result; return the normalized dict:

        session_id, num_turns, duration_ms, total_cost_usd,
        usage: {input_tokens, output_tokens, cache_read_input_tokens,
        cache_creation_input_tokens}
        """

    def meta_extra(self, result_event: dict | None, args: argparse.Namespace) -> dict:
        """Agent-only fields merged into the per-product meta.json. Default: none."""
        return {}

    def batch_payload_extra(self, args: argparse.Namespace) -> dict:
        """Agent-only fields merged into the top-level summary-*.json. Default: none."""
        return {}
