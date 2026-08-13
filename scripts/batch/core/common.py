"""Shared, agent-agnostic machinery for the batch runner.

Domain/CSV/prompt loading, product filtering, the validator subprocess call,
and console/progress-window rendering - all identical regardless of which
code agent (claude, pi, ...) is driving a given run. Agent-specific behavior
(CLI invocation, stream-event schema, meta fields) lives in
scripts/batch/core/handlers/*.
"""

from __future__ import annotations

import csv
import json
import os
import shutil
import subprocess
import sys
from collections import deque
from pathlib import Path

from shared.domains import DOMAINS, REPO_ROOT

# Module-level defaults (microsegmentation) - reassigned by select_domain()
# when --domain selects a different one. Kept as module-level state so
# existing call sites (and scripts/batch/tail_run_logs.py, which imports this
# module directly) don't need a domain parameter threaded through every call.
CSV_PATH = DOMAINS["microsegmentation"]["csv"]
PROMPTS_DIR = REPO_ROOT / ".claude" / "skills" / "provider-assessment" / "prompts"
PROMPT_FILES = {
    "standard": PROMPTS_DIR / "standard_mode.md",
}
RUNS_ROOT = DOMAINS["microsegmentation"]["dir"] / "runs"
VALIDATOR = REPO_ROOT / ".claude" / "skills" / "provider-assessment" / "scripts" / "validate_assessment.py"
CURRENT_DOMAIN = "microsegmentation"
VENV_PY = REPO_ROOT / "venv" / "Scripts" / "python.exe"
BATCH_DIR = RUNS_ROOT / "_batch"


def select_domain(domain: str) -> None:
    """Reassign the module-level path constants for the chosen domain."""
    global CSV_PATH, RUNS_ROOT, CURRENT_DOMAIN, BATCH_DIR
    cfg = DOMAINS[domain]
    CSV_PATH = cfg["csv"]
    RUNS_ROOT = cfg["dir"] / "runs"
    CURRENT_DOMAIN = domain
    BATCH_DIR = RUNS_ROOT / "_batch"


def render_prompt(template: str, product: dict) -> str:
    return (template
            .replace("{DOMAIN}", CURRENT_DOMAIN)
            .replace("{VENDOR}", product["vendor"])
            .replace("{PRODUCT_NAME}", product["product_name"])
            .replace("{product_id}", product["product_id"]))


# ---------------------------------------------------------------------------
# Prompt template loading
# ---------------------------------------------------------------------------

def load_prompt_template(mode: str) -> str:
    import re
    prompt_file = PROMPT_FILES[mode]
    if not prompt_file.exists():
        raise SystemExit(f"prompt file for mode={mode!r} not found: {prompt_file}")
    text = prompt_file.read_text(encoding="utf-8")
    m = re.search(r"```\r?\n(.*?)\r?\n```", text, re.DOTALL)
    if not m:
        raise SystemExit(f"could not find fenced code block in {prompt_file}")
    return m.group(1)


def load_queue_file(path: Path) -> list[str]:
    pids: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if line:
            pids.append(line)
    return pids


def already_done_for_mode(pid: str, mode: str) -> bool:
    """True iff runs/<pid>/assessment.json exists AND was produced in the same mode."""
    p = RUNS_ROOT / pid / "assessment.json"
    if not p.exists():
        return False
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    return data.get("assessment_mode") == mode


# ---------------------------------------------------------------------------
# CSV product loading
# ---------------------------------------------------------------------------

def load_products(csv_path: Path) -> list[dict]:
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    header_idx = next(
        (i for i, r in enumerate(rows) if r and r[0].strip() == "STT"),
        None,
    )
    if header_idx is None:
        raise SystemExit(f"no header row (STT,...) found in {csv_path}")
    header = [h.strip() for h in rows[header_idx]]
    out: list[dict] = []
    for row in rows[header_idx + 1:]:
        if not row or not row[0].strip():
            continue
        rec = dict(zip(header, row))
        pid = (rec.get("product_id") or "").strip()
        if not pid:
            continue
        out.append({
            "stt": rec.get("STT", "").strip(),
            "vendor": (rec.get("Company") or "").strip(),
            "product_name": (rec.get("Product") or rec.get("Product Name") or "").strip(),
            "product_id": pid,
        })
    return out


def filter_products(products, only, start_at, limit, queue_pids):
    if queue_pids is not None:
        pid_map = {p["product_id"]: p for p in products}
        missing = [q for q in queue_pids if q not in pid_map]
        if missing:
            print(f"WARN queue-file has {len(missing)} pid(s) not in CSV: {missing[:5]}"
                  f"{'…' if len(missing) > 5 else ''}", file=sys.stderr)
        products = [pid_map[q] for q in queue_pids if q in pid_map]
    if only:
        products = [p for p in products if p["product_id"] == only]
        if not products:
            raise SystemExit(f"--only {only} not found")
    if start_at:
        idx = next((i for i, p in enumerate(products) if p["product_id"] == start_at), None)
        if idx is None:
            raise SystemExit(f"--start-at {start_at} not found")
        products = products[idx:]
    if limit:
        products = products[:limit]
    return products


# ---------------------------------------------------------------------------
# Validator
# ---------------------------------------------------------------------------

def run_validator(pid: str) -> dict | None:
    assessment = RUNS_ROOT / pid / "assessment.json"
    if not assessment.exists():
        return {"exit_code": None, "note": "assessment.json missing"}
    py = str(VENV_PY) if VENV_PY.exists() else sys.executable
    proc = subprocess.run(
        [py, str(VALIDATOR), "--domain", CURRENT_DOMAIN, str(assessment),
         "--evidence-store", str(RUNS_ROOT / pid)],
        capture_output=True, text=True,
    )
    return {
        "exit_code": proc.returncode,
        "stdout_tail": proc.stdout.strip().splitlines()[-5:] if proc.stdout else [],
        "stderr_tail": proc.stderr.strip().splitlines()[-5:] if proc.stderr else [],
    }


# ---------------------------------------------------------------------------
# Console / progress-window helpers
# ---------------------------------------------------------------------------

def safe_console(s: str) -> str:
    """Sanitize for print() on a non-UTF-8 console (default cp1252 on Windows).

    Progress lines echo arbitrary file/web content (tool_result text, model
    text output) which routinely contains characters cp1252 can't encode
    (Vietnamese diacritics, em-dashes, curly quotes) -- confirmed by testing
    summarize_event() against a real run log, which raised UnicodeEncodeError
    on a plain print(). Replacing unencodable characters here means a batch
    run degrades to '?' placeholders instead of crashing mid-run on whichever
    product happens to cite non-ASCII text first.
    """
    enc = sys.stdout.encoding or "utf-8"
    return s.encode(enc, errors="replace").decode(enc, errors="replace")


def truncate(s: str, n: int = 100) -> str:
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "…"


def enable_windows_ansi() -> None:
    """Best-effort: turn on ANSI escape processing in the classic Windows console.

    Windows Terminal / PowerShell 7 already do this; PowerShell 5.1's conhost
    needs ENABLE_VIRTUAL_TERMINAL_PROCESSING (0x0004) set explicitly or the
    cursor-up/clear-line codes used by LineWindow print as literal garbage.
    """
    if os.name != "nt":
        return
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_uint32()
        kernel32.GetConsoleMode(handle, ctypes.byref(mode))
        kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    except Exception:  # noqa: BLE001
        pass


class LineWindow:
    """Redraws the last N progress lines in place instead of scrolling.

    Each push() moves the cursor back up over the previously drawn block and
    rewrites it, so at most N lines of live status are ever on screen. The
    full stream trace is unaffected - it's written to the log file
    separately, before this is ever called.
    """

    def __init__(self, size: int):
        self.lines: deque[str] = deque(maxlen=max(1, size))
        self.printed = 0

    def push(self, text: str) -> None:
        width = shutil.get_terminal_size((100, 20)).columns - 1
        self.lines.append(text[:width])
        chunks = []
        if self.printed:
            chunks.append(f"\x1b[{self.printed}A")
        for line in self.lines:
            chunks.append("\x1b[2K" + line + "\n")
        sys.stdout.write("".join(chunks))
        sys.stdout.flush()
        self.printed = len(self.lines)
