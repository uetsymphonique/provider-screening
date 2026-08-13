"""Handler for `pi --mode json`."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from ..common import truncate
from .base import AgentHandler


def _brief_tool_input(name: str, inp: dict) -> str:
    name_lower = name.lower()
    if name_lower in ("bash",):
        return truncate(inp.get("command", ""), 90)
    if name_lower in ("read", "edit", "write"):
        return inp.get("path", inp.get("file_path", ""))
    if name_lower in ("grep", "find", "ls"):
        return truncate(inp.get("pattern", "") or inp.get("path", ""), 60)
    keys = ", ".join(list(inp.keys())[:3])
    return f"{{{keys}}}" if keys else ""


def _parse_ts(ts: str | int | None) -> datetime | None:
    """Pi emits two timestamp formats: ISO 8601 strings (session/agent events)
    and Unix milliseconds integers (message.timestamp on message_end)."""
    if ts is None:
        return None
    if isinstance(ts, (int, float)):
        return datetime.fromtimestamp(ts / 1000, tz=timezone.utc)
    try:
        return datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
    except Exception:
        return None


class PiHandler(AgentHandler):
    name = "pi"
    log_filename = "pi_run.jsonl"
    meta_filename = "pi_run.meta.json"
    summary_prefix = "summary-pi"

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--model", help="e.g. deepseek/deepseek-v4-pro or anthropic/claude-sonnet-4-5")

    def find_binary(self) -> str:
        pi_bin = shutil.which("pi")
        if not pi_bin:
            raise SystemExit("`pi` CLI not on PATH")
        return pi_bin

    def write_prompt_file(self, run_dir: Path, prompt_text: str) -> None:
        # Written before Popen and referenced via @file (see build_command):
        # Windows CreateProcess has a 32K command-line limit; long prompts
        # (9K+) easily exceed it after list2cmdline quoting.
        (run_dir / "prompt_pi.txt").write_text(prompt_text, encoding="utf-8")

    def build_command(self, run_dir: Path, prompt_text: str, args: argparse.Namespace) -> list[str]:
        prompt_file = run_dir / "prompt_pi.txt"
        # --mode json outputs streaming events; -nc disables context-file
        # loading (our prompt already has all instructions embedded).
        # --no-session avoids polluting ~/.pi/agent/sessions/ with ephemeral
        # runs. --approve auto-trusts the project so the skill under
        # .pi/skills/ loads.
        cmd = [
            self.find_binary(), "--mode", "json",
            "--no-session",
            "--approve",
            "-nc",
            f"@{prompt_file}",
        ]
        if args.model:
            cmd.extend(["--model", args.model])
        return cmd

    def summarize_event(self, ev: dict) -> str | tuple[str, str] | None:
        """One-line progress summary for a pi --mode json event.

        Pi JSON mode events: session, agent_start, agent_end, agent_settled,
        turn_start, turn_end, message_start, message_update, message_end,
        tool_execution_start, tool_execution_update, tool_execution_end,
        compaction_start, compaction_end, queue_update.
        """
        etype = ev.get("type")
        if etype == "session":
            return f"session init  id={ev.get('id', '?')}  cwd={ev.get('cwd', '?')}"
        if etype == "agent_start":
            return "agent started"
        if etype == "agent_settled":
            return "agent settled (done)"
        if etype == "tool_execution_start":
            name = ev.get("toolName", "?")
            args_ = ev.get("args") or {}
            brief = _brief_tool_input(name, args_)
            return f"tool_start  {name}({brief})" if brief else f"tool_start  {name}"
        if etype == "tool_execution_end":
            name = ev.get("toolName", "?")
            is_err = ev.get("isError", False)
            tag = "ERROR" if is_err else "ok"
            return f"tool_end[{tag}]  {name}"
        if etype == "message_update":
            ame = ev.get("assistantMessageEvent") or {}
            delta_type = ame.get("type")
            if delta_type == "text_delta":
                # Caller buffers/flushes this to avoid one-line-per-token spam.
                return ("text", ame.get("delta", ""))
            if delta_type == "toolcall_end":
                tc = ame.get("toolCall") or {}
                name = tc.get("name", "?")
                tc_args = tc.get("arguments") or {}
                brief = _brief_tool_input(name, tc_args)
                return f"toolcall  {name}({brief})" if brief else f"toolcall  {name}"
            return None
        if etype == "compaction_start":
            return "compaction started"
        if etype == "compaction_end":
            return "compaction ended"
        return None

    def parse_result(self, log_path: Path) -> dict | None:
        """Scan pi --mode json log for session-level cost/usage summary.

        Pi emits per-message usage (on each assistant message_end), not a
        single 'result' event like Claude. We aggregate from all assistant
        message_end events and also look for the final agent_start/agent_end
        for timing.
        """
        if not log_path.exists():
            return None
        total_usage = {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0}
        total_cost = 0.0
        num_turns = 0
        session_id = None
        provider = None
        model = None
        stop_reason = None
        error_message = None
        agent_start_ts = None
        agent_end_ts = None
        first_event_ts = None
        last_event_ts = None

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

                    etype = ev.get("type")
                    ts = ev.get("timestamp")
                    if ts:
                        if first_event_ts is None:
                            first_event_ts = ts
                        last_event_ts = ts

                    if etype == "session":
                        session_id = ev.get("id")
                    elif etype == "turn_start":
                        num_turns += 1
                    elif etype == "agent_start":
                        agent_start_ts = ev.get("timestamp")
                    elif etype == "agent_end":
                        agent_end_ts = ev.get("timestamp")
                    elif etype == "message_end":
                        msg = ev.get("message") or {}
                        msg_ts = msg.get("timestamp")
                        if msg_ts:
                            if first_event_ts is None:
                                first_event_ts = msg_ts
                            last_event_ts = msg_ts
                        if msg.get("role") == "assistant":
                            # Only count terminal messages — stopReason ==
                            # "pending" means still streaming; the final
                            # message_end for that turn has a real stopReason.
                            if msg.get("stopReason") != "pending":
                                u = msg.get("usage") or {}
                                total_usage["input"] += u.get("input", 0)
                                total_usage["output"] += u.get("output", 0)
                                total_usage["cacheRead"] += u.get("cacheRead", 0)
                                total_usage["cacheWrite"] += u.get("cacheWrite", 0)
                                c = u.get("cost") or {}
                                total_cost += c.get("total", 0)
                            provider = msg.get("provider")
                            model = msg.get("model")
                            stop_reason = msg.get("stopReason")
                            if msg.get("errorMessage"):
                                error_message = msg["errorMessage"]
        except Exception:  # noqa: BLE001
            pass

        # Duration: prefer agent_start/agent_end, fall back to first/last
        # event timestamps (covers runs killed before agent_end).
        start_ts = _parse_ts(agent_start_ts) or _parse_ts(first_event_ts)
        end_ts = _parse_ts(agent_end_ts) or _parse_ts(last_event_ts)
        duration_ms = int((end_ts - start_ts).total_seconds() * 1000) if start_ts and end_ts else None

        return {
            "session_id": session_id,
            "num_turns": num_turns,
            "duration_ms": duration_ms,
            "total_cost_usd": total_cost,
            "usage": {
                "input_tokens": total_usage["input"],
                "output_tokens": total_usage["output"],
                "cache_read_input_tokens": total_usage["cacheRead"],
                "cache_creation_input_tokens": total_usage["cacheWrite"],
            },
            "_raw": {
                "provider": provider,
                "model": model,
                "stop_reason": stop_reason,
                "error_message": error_message,
            },
        }

    def meta_extra(self, result_event: dict | None, args: argparse.Namespace) -> dict:
        raw = (result_event or {}).get("_raw") or {}
        return {
            "agent": "pi",
            "provider": raw.get("provider"),
            "model": raw.get("model"),
            "stop_reason": raw.get("stop_reason"),
            "error_message": raw.get("error_message"),
        }
