"""Registry of code-agent handlers for the batch runner.

Each handler encapsulates everything agent-specific about driving a batch
run: CLI invocation, stream-event schema, and meta/summary fields. Adding a
new agent means adding one handler module and one registry entry here — the
shared driver (scripts/batch/driver.py) never branches on agent name.
"""

from __future__ import annotations

from .base import AgentHandler
from .claude_handler import ClaudeHandler
from .pi_handler import PiHandler

HANDLERS: dict[str, type[AgentHandler]] = {
    "claude": ClaudeHandler,
    "pi": PiHandler,
}


def get_handler(name: str) -> AgentHandler:
    return HANDLERS[name]()
