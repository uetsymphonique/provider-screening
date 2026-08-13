"""Wayback Machine and Common Crawl archive fetchers, both built on
cdx_toolkit (Common Crawl Foundation's own maintained CDX client, see
utils/cdx_tookit/ for its vendored source) instead of hand-rolled CDX-JSON
parsing and manual WARC-record byte-slicing. It buys: a unified query
interface across the IA and pywb CDX dialects, warcio-based WARC parsing
(more robust than a raw b"\r\n\r\n" split), per-host rate limiting with
429/5xx retry+backoff (myrequests.py), and a 24h-cached collinfo.json
lookup.

Not registered in base.REGISTRY -- both take CLI-specific override kwargs
(timestamp / index+status), wired explicitly by
html_to_text.py._run_method."""
from __future__ import annotations

import re
from datetime import datetime, timezone

import cdx_toolkit

from .base import FetchError, _decode

WAYBACK_WEB = "https://web.archive.org/web/"

_CC_FILENAME_RE = re.compile(r"CC-MAIN-\d{4}-\d{2}")


def fetch_wayback(url: str, timestamp: str | None = None) -> tuple[bytes, str, dict]:
    """Look up a Wayback Machine capture for `url` via cdx_toolkit (CDX API
    query + un-toolbared snapshot fetch), defaulting to the capture closest
    to now (i.e. most recent). Broader single-URL coverage than Common Crawl
    (continuous archiving vs CC's periodic, incomplete crawls) and one CDX
    round-trip instead of scanning dozens of CC collections, so it runs
    before `cc` in the auto chain. Pass timestamp (14-digit YYYYMMDDhhmmss,
    as recorded by a prior run's manifest) to pin a specific capture instead
    of "most recent". No timeout parameter -- cdx_toolkit's HTTP layer
    (myrequests.py) uses its own fixed 30s connect/read timeout plus
    per-host rate limiting and retry/backoff, not independently tunable."""
    ts = timestamp or datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    cdx = cdx_toolkit.CDXFetcher(source="ia")
    try:
        objs = cdx.get(url, filter="status:200", closest=ts, sort="closest", limit=1)
    except Exception as e:  # noqa: BLE001
        raise FetchError(f"Wayback CDX lookup failed: {e}") from e
    if not objs:
        raise FetchError(f"no Wayback capture found for {url}")

    obj = objs[0]
    capture_ts = obj["timestamp"]
    snapshot_url = f"{WAYBACK_WEB}{capture_ts}id_/{url}"
    try:
        data = obj.content
    except Exception as e:  # noqa: BLE001
        raise FetchError(f"Wayback snapshot fetch failed: {e}") from e

    return data, _decode(data, obj.get("mime", "")), {
        "content_kind": "html", "wayback_timestamp": capture_ts, "wayback_url": snapshot_url,
    }


def fetch_common_crawl(url: str, index: str | None = None, status: str | None = "200") -> tuple[bytes, str, dict]:
    """Look up the latest Common Crawl index entry for `url` via cdx_toolkit
    (knits the monthly CDX indices into one virtual index) and download the
    WARC record's HTTP payload. Last-resort fetch for pages that can no
    longer be reached live. Pass index (a CC-MAIN-YYYY-WW collection id, as
    recorded by a prior run's manifest) to pin a specific collection instead
    of the default (most recent ~12 months). No timeout parameter -- see
    fetch_wayback's docstring."""
    cdx = cdx_toolkit.CDXFetcher(source="cc", crawl=index)
    try:
        objs = cdx.get(url, filter=f"=status:{status}" if status else None, limit=1)
    except Exception as e:  # noqa: BLE001
        raise FetchError(f"Common Crawl CDX lookup failed: {e}") from e
    if not objs:
        raise FetchError(f"no Common Crawl index entry found for {url}")

    obj = objs[0]
    try:
        payload = obj.content
    except Exception as e:  # noqa: BLE001
        raise FetchError(f"WARC download failed: {e}") from e

    m = _CC_FILENAME_RE.search(obj.get("filename", ""))
    return payload, payload.decode("utf-8", errors="replace"), {
        "content_kind": "html",
        "cc_index": m.group(0) if m else index,
        "cc_timestamp": obj.get("timestamp"),
    }
