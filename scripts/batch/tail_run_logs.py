"""Interactive live-tail viewer for concurrent pi batch runs.

Reads the same runs/<pid>/pi_run.jsonl files `run_batch.py pi` already writes
and formats events with the exact same PiHandler.summarize_event / truncate /
safe_console helpers used by scripts/batch/core/driver.py - no duplicated
formatting logic, so this can never drift from what the batch runner
actually emits. The batch runner itself is untouched; this is a read-only
viewer that can be started/stopped independently of the batch run.

The whole screen (header + N-line window) is one redraw-in-place block:
switching products overwrites the previous block entirely instead of
scrolling a new one below it. Switching (n/p/r) seeds the window from the
last N formatted lines already in that product's pi_run.jsonl, then keeps
redrawing it live in place as new events arrive.

Usage:
  python scripts/batch/tail_run_logs.py --domain microsegmentation
  python scripts/batch/tail_run_logs.py --domain bsg --only illumio-zero-trust-segmentation zero-networks-segment
  python scripts/batch/tail_run_logs.py --domain microsegmentation --overwrite 10

Keys while running:
  n / p     next / previous product
  r         rescan runs/ for new pi_run.jsonl files
  q         quit (Ctrl+C also works)
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from collections import deque

from scripts.batch.core import common  # reuse DOMAINS/select_domain/formatting helpers
from scripts.batch.core.handlers.pi_handler import PiHandler

_pi = PiHandler()

try:
    import msvcrt
except ImportError:  # pragma: no cover - non-Windows fallback
    msvcrt = None


def discover_products(only: list[str] | None) -> list[str]:
    if only:
        return only
    if not common.RUNS_ROOT.exists():
        return []
    files = sorted(common.RUNS_ROOT.glob("*/pi_run.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
    return [p.parent.name for p in files]


def format_event(pid: str, ev: dict, text_buf: str) -> tuple[list[str], str]:
    """Returns (formatted_lines, updated_text_buf)."""
    result = _pi.summarize_event(ev)
    now = time.strftime("%H:%M:%S")
    if isinstance(result, tuple) and result[0] == "text":
        text_buf += result[1]
        if len(text_buf) >= 140:
            line = common.safe_console(f"  [{pid}] {now}  text      {common.truncate(text_buf, 140)}")
            return [line], ""
        return [], text_buf
    lines: list[str] = []
    if text_buf:
        lines.append(common.safe_console(f"  [{pid}] {now}  text      {common.truncate(text_buf, 140)}"))
        text_buf = ""
    if result:
        lines.append(common.safe_console(f"  [{pid}] {now}  {result}"))
    return lines, text_buf


class Screen:
    """Redraws a fixed-size block (header + N content lines) in place.

    Content is always padded to win_size lines so the block's total height
    never shrinks between redraws - otherwise a switch to a product with
    fewer buffered lines than the last one would leave stale lines from the
    previous block dangling below the new, shorter one.
    """

    def __init__(self, win_size: int):
        self.win_size = win_size
        self.printed = 0

    def redraw(self, header: list[str], content: deque[str]) -> None:
        width = shutil.get_terminal_size((100, 20)).columns - 1
        pad = [""] * (self.win_size - len(content))
        lines = [*header, *pad, *content]
        chunks = []
        if self.printed:
            chunks.append(f"\x1b[{self.printed}A")
        for line in lines:
            chunks.append("\x1b[2K" + line[:width] + "\n")
        sys.stdout.write("".join(chunks))
        sys.stdout.flush()
        self.printed = len(lines)


class LiveView:
    """Buffers the last N formatted lines of one product's log.

    Seeded from the last N *formatted* lines already in pi_run.jsonl (not
    the last N raw JSON events - one event can fold into 0-2 display
    lines), then kept live by polling for bytes appended after the seed.
    Drawing is Screen's job, not this class's - it only holds state.
    """

    def __init__(self, pid: str, win_size: int):
        self.pid = pid
        self.path = common.RUNS_ROOT / pid / "pi_run.jsonl"
        self.lines: deque[str] = deque(maxlen=win_size)
        self.text_buf = ""
        self.offset = 0
        self._seed(win_size)

    def _seed(self, win_size: int) -> None:
        if not self.path.exists():
            return
        raw = self.path.read_bytes()
        self.offset = len(raw)
        text_buf = ""
        collected: list[str] = []
        for raw_line in raw.decode("utf-8", errors="replace").splitlines():
            raw_line = raw_line.strip()
            if not raw_line:
                continue
            try:
                ev = json.loads(raw_line)
            except json.JSONDecodeError:
                continue
            fmt_lines, text_buf = format_event(self.pid, ev, text_buf)
            collected.extend(fmt_lines)
        self.text_buf = text_buf
        for line in collected[-win_size:]:
            self.lines.append(line)

    def poll(self) -> bool:
        """Reads newly-appended events. Returns True if any new line was buffered."""
        if not self.path.exists():
            return False
        size = self.path.stat().st_size
        if size <= self.offset:
            return False
        with self.path.open("r", encoding="utf-8", errors="replace") as f:
            f.seek(self.offset)
            data = f.read()
            self.offset = f.tell()
        changed = False
        for raw_line in data.splitlines():
            raw_line = raw_line.strip()
            if not raw_line:
                continue
            try:
                ev = json.loads(raw_line)
            except json.JSONDecodeError:
                continue
            fmt_lines, self.text_buf = format_event(self.pid, ev, self.text_buf)
            for line in fmt_lines:
                self.lines.append(line)
                changed = True
        return changed


def header_lines(products: list[str], idx: int) -> list[str]:
    return [
        "=" * 100,
        f"[{idx + 1}/{len(products)}] following: {products[idx]}   "
        f"(n=next  p=prev  r=rescan  q=quit)",
        "=" * 100,
    ]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--domain", choices=list(common.DOMAINS.keys()), required=True)
    ap.add_argument("--only", nargs="+", metavar="PID",
                     help="Restrict to these product_ids (default: autodiscover all under runs/, newest first)")
    ap.add_argument("--overwrite", type=int, default=5, metavar="N",
                     help="Redraw-in-place window size: number of most-recent formatted log "
                          "lines shown per product (default 5), same mechanism as "
                          "`run_batch.py pi`'s --overwrite.")
    args = ap.parse_args()

    common.select_domain(args.domain)
    products = discover_products(args.only)
    if not products:
        print("no pi_run.jsonl files found yet under runs/ - start a batch first", file=sys.stderr)
        return 1

    common.enable_windows_ansi()
    if msvcrt is None:
        print("WARN interactive key switching needs msvcrt (Windows); "
              "following product[0] only, Ctrl+C to quit.", file=sys.stderr)

    screen = Screen(args.overwrite)
    idx = 0
    view = LiveView(products[idx], args.overwrite)
    screen.redraw(header_lines(products, idx), view.lines)

    def focus(new_idx: int) -> None:
        nonlocal idx, view
        idx = new_idx
        view = LiveView(products[idx], args.overwrite)
        screen.redraw(header_lines(products, idx), view.lines)

    try:
        while True:
            if msvcrt is not None and msvcrt.kbhit():
                ch = msvcrt.getch().decode("utf-8", errors="ignore").lower()
                if ch == "q":
                    break
                elif ch == "n":
                    focus((idx + 1) % len(products))
                elif ch == "p":
                    focus((idx - 1) % len(products))
                elif ch == "r":
                    products = discover_products(args.only)
                    focus(min(idx, len(products) - 1))

            if view.poll():
                screen.redraw(header_lines(products, idx), view.lines)
            time.sleep(0.3)
    except KeyboardInterrupt:
        pass

    return 0


if __name__ == "__main__":
    sys.exit(main())
