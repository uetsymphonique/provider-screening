"""Handler for `claude -p --output-format stream-json`.

Docs cross-checked: https://code.claude.com/docs/en/headless.md
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from ..common import truncate
from .base import AgentHandler

# Pre-approve the tools the standard-mode prompt actually needs. Combined with
# --permission-mode acceptEdits this covers file R/W without blanket approval.
ALLOWED_TOOLS = "Bash,Read,Edit,Write,Grep,Glob,WebFetch,WebSearch,Skill,TodoWrite"


def _brief_tool_input(name: str, inp: dict) -> str:
    if name == "Bash":
        return truncate(inp.get("command", ""), 90)
    if name in ("Read", "Edit", "Write"):
        return inp.get("file_path", "")
    if name in ("Grep", "Glob"):
        return truncate(inp.get("pattern", ""), 60)
    if name == "WebFetch":
        return inp.get("url", "")
    if name == "WebSearch":
        return truncate(inp.get("query", ""), 60)
    if name == "Skill":
        return inp.get("skill", "") or inp.get("command", "")
    keys = ", ".join(list(inp.keys())[:3])
    return f"{{{keys}}}" if keys else ""


class ClaudeHandler(AgentHandler):
    name = "claude"
    log_filename = "claude_run.jsonl"
    meta_filename = "claude_run.meta.json"
    summary_prefix = "summary"

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--model", help="opus | sonnet | haiku | fable (default: session default)")
        parser.add_argument("--max-turns", type=int, default=None,
                             help="Cap on agentic turns per product, forwarded to `claude -p --max-turns`. "
                                  "Unset by default (no cap) — a standard-mode pass over 24-33 checklist items "
                                  "with multi-source research routinely needs more turns than a typical "
                                  "single-skill task, so borrow run-pipeline.py's 70-turn default only after "
                                  "checking actual usage in a real run's claude_run.meta.json.")
        parser.add_argument("--max-budget-usd", type=float, default=None,
                             help="Cap on USD spend per product, forwarded to `claude -p --max-budget-usd`. "
                                  "Unset by default (no cap) — check a real run's total_cost_usd before "
                                  "picking a number.")
        parser.add_argument("--dangerously-skip-permissions", action="store_true",
                             help="Forward `--dangerously-skip-permissions` to `claude -p` instead of the "
                                  "default --permission-mode acceptEdits + --allowedTools whitelist. No "
                                  "prompt for ANY tool call, in or out of the project tree. Off by default; "
                                  "pass explicitly per invocation since this removes all guardrails for an "
                                  "unattended batch run.")

    def find_binary(self) -> str:
        claude_bin = shutil.which("claude")
        if not claude_bin:
            raise SystemExit("`claude` CLI not on PATH")
        return claude_bin

    def write_prompt_file(self, run_dir: Path, prompt_text: str) -> None:
        (run_dir / "prompt.txt").write_text(prompt_text, encoding="utf-8")

    def build_command(self, run_dir: Path, prompt_text: str, args: argparse.Namespace) -> list[str]:
        cmd = [
            self.find_binary(), "-p",
            "--output-format", "stream-json",
            "--verbose",  # required for stream-json in -p mode
        ]
        if args.dangerously_skip_permissions:
            # No prompts for ANY tool call, in or out of the project tree — the
            # scoped acceptEdits + allowedTools combo below is the safe default;
            # this is opt-in per invocation via --dangerously-skip-permissions.
            cmd.append("--dangerously-skip-permissions")
        else:
            cmd.extend(["--permission-mode", "acceptEdits", "--allowedTools", ALLOWED_TOOLS])
        if args.model:
            cmd.extend(["--model", args.model])
        if args.max_turns is not None:
            cmd.extend(["--max-turns", str(args.max_turns)])
        if args.max_budget_usd is not None:
            cmd.extend(["--max-budget-usd", str(args.max_budget_usd)])
        cmd.append(prompt_text)
        return cmd

    def describe_run(self, prompt_text: str, args: argparse.Namespace) -> str:
        budget_str = f"${args.max_budget_usd}" if args.max_budget_usd is not None else "none"
        perm_str = "DANGEROUSLY-SKIP-PERMISSIONS" if args.dangerously_skip_permissions else "acceptEdits+allowlist"
        return (f"prompt={len(prompt_text)}B  model={args.model or 'default'}  "
                f"max_turns={args.max_turns or 'none'}  max_budget={budget_str}  perm={perm_str}")

    def summarize_event(self, ev: dict) -> str | tuple[str, str] | None:
        """One-line progress summary for a stream-json event, or None to skip it.

        Schema per https://code.claude.com/docs/en/headless.md stream-json output:
        type in {system, assistant, user, result}; assistant/user carry a
        message.content list of blocks (text | tool_use | tool_result).
        """
        etype = ev.get("type")
        if etype == "system" and ev.get("subtype") == "init":
            tools = ev.get("tools") or []
            return f"session init  model={ev.get('model', '?')}  tools={len(tools)}"
        if etype == "assistant":
            for block in (ev.get("message") or {}).get("content") or []:
                btype = block.get("type")
                if btype == "tool_use":
                    name = block.get("name", "?")
                    brief = _brief_tool_input(name, block.get("input") or {})
                    return f"tool_use  {name}({brief})" if brief else f"tool_use  {name}"
                if btype == "text":
                    text = truncate(block.get("text", ""))
                    if text:
                        return f"text      {text}"
            return None
        if etype == "user":
            for block in (ev.get("message") or {}).get("content") or []:
                if block.get("type") == "tool_result":
                    content = block.get("content")
                    text = ""
                    if isinstance(content, list):
                        text = " ".join(
                            c.get("text", "") for c in content
                            if isinstance(c, dict) and c.get("type") == "text"
                        )
                    elif isinstance(content, str):
                        text = content
                    tag = "ERROR" if block.get("is_error") else "ok"
                    return f"tool_result[{tag}]  {truncate(text)}"
            return None
        return None

    def parse_result(self, log_path: Path) -> dict | None:
        """Scan stream-json log for the final `type: "result"` event; return it normalized.

        Raw schema (SDKResultMessage — https://code.claude.com/docs/en/agent-sdk/typescript.md):
        subtype, is_error, duration_ms, duration_api_ms, num_turns, total_cost_usd,
        usage.{input_tokens, output_tokens, cache_creation_input_tokens,
        cache_read_input_tokens}, permission_denials, result, session_id.
        """
        if not log_path.exists():
            return None
        result_event = None
        try:
            with log_path.open(encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        ev = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if isinstance(ev, dict) and ev.get("type") == "result":
                        result_event = ev
        except Exception:  # noqa: BLE001
            pass
        if result_event is None:
            return None
        usage = result_event.get("usage") or {}
        return {
            "session_id": result_event.get("session_id"),
            "num_turns": result_event.get("num_turns"),
            "duration_ms": result_event.get("duration_ms"),
            "total_cost_usd": result_event.get("total_cost_usd"),
            "usage": {
                "input_tokens": usage.get("input_tokens"),
                "output_tokens": usage.get("output_tokens"),
                "cache_read_input_tokens": usage.get("cache_read_input_tokens"),
                "cache_creation_input_tokens": usage.get("cache_creation_input_tokens"),
            },
            "_raw": result_event,
        }

    def meta_extra(self, result_event: dict | None, args: argparse.Namespace) -> dict:
        raw = (result_event or {}).get("_raw") or {}
        return {
            "skip_permissions": args.dangerously_skip_permissions,
            "subtype": raw.get("subtype"),
            "is_error": raw.get("is_error"),
            "duration_api_ms": raw.get("duration_api_ms"),
            "permission_denials": len(raw.get("permission_denials") or []),
        }

    def batch_payload_extra(self, args: argparse.Namespace) -> dict:
        return {
            "max_turns": args.max_turns,
            "max_budget_usd": args.max_budget_usd,
            "dangerously_skip_permissions": args.dangerously_skip_permissions,
        }
