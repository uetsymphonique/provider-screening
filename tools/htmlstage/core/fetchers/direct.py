"""Direct HTTP fetch. Not registered in base.REGISTRY -- takes a
CLI-specific browser_ua kwarg, wired explicitly by main.py._run_method."""
from __future__ import annotations

from curl_cffi import requests as curl_requests

from .base import FetchError, _decode


def fetch_direct(url: str, browser_ua: bool = False, timeout: int = 60) -> tuple[bytes, str, dict]:
    """HTTP GET impersonating a real browser's TLS/JA3 fingerprint via
    curl_cffi. Plain urllib's Python TLS handshake gets fingerprinted and
    blocked by many WAFs before headers are even inspected, so a spoofed
    User-Agent *string* alone doesn't help against that layer -- the whole
    handshake (cipher suites, extensions order, ALPN) has to look like an
    actual browser too. Set browser_ua=True to switch the impersonation
    target from Chrome to Safari, for the rarer case a site specifically
    fingerprints/blocks Chrome's signature (e.g. support.elisity.com)."""
    target = "safari" if browser_ua else "chrome"
    try:
        resp = curl_requests.get(
            url,
            headers={"Accept": "text/html,application/xhtml+xml,*/*;q=0.8"},
            impersonate=target,
            timeout=timeout,
        )
    except Exception as e:  # noqa: BLE001
        raise FetchError(f"direct fetch failed: {e}") from e

    if resp.status_code >= 400:
        raise FetchError(f"direct fetch failed: HTTP {resp.status_code}")

    ctype = resp.headers.get("Content-Type", "")
    data = resp.content

    if "html" not in ctype.lower() and not data.lstrip()[:15].lower().startswith(b"<!doctype html") \
            and b"<html" not in data[:2000].lower():
        raise FetchError(f"unexpected content-type={ctype!r} first-bytes={data[:40]!r}")

    return data, _decode(data, ctype), {"content_kind": "html"}
