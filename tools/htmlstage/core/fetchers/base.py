"""Shared contract for every fetch method: the FetchError exception, the
charset-sniffing _decode() helper, and a name -> callable registry so
main.py's chain driver doesn't need an if/elif branch per method.

Register the common case -- a fetcher that only ever needs the URL -- with
@register("name"). Fetchers that also take CLI-specific override kwargs
(direct's browser_ua, wayback's timestamp, cc's index/status) are NOT
registered here; main.py._run_method wires those explicitly,
since threading argparse.Namespace fields through a generic registry would
obscure the mapping rather than simplify it. Everything else -- a new
archive source, a new proxy provider -- needs no changes to _run_method at
all: write the module, decorate the function, add the method name to
AUTO_CHAIN.
"""
from __future__ import annotations

import re
from typing import Callable

FetchFn = Callable[[str], "tuple[bytes, str, dict]"]
REGISTRY: dict[str, FetchFn] = {}


def register(name: str) -> Callable[[FetchFn], FetchFn]:
    def deco(fn: FetchFn) -> FetchFn:
        REGISTRY[name] = fn
        return fn
    return deco


class FetchError(Exception):
    """A fetch method failed outright (network/HTTP error, no data found)."""


def _decode(data: bytes, content_type: str) -> str:
    charset = None
    m = re.search(r"charset=([\w-]+)", content_type, re.IGNORECASE)
    if m:
        charset = m.group(1)
    if not charset:
        m = re.search(rb'charset=["\']?([\w-]+)', data[:2048], re.IGNORECASE)
        if m:
            charset = m.group(1).decode("ascii", "ignore")
    try:
        return data.decode(charset or "utf-8", errors="replace")
    except (LookupError, UnicodeDecodeError):
        return data.decode("utf-8", errors="replace")
