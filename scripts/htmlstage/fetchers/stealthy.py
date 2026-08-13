"""Stealth-browser fetch via Scrapling's StealthyFetcher -- see this
package's __init__ docstring for why it's the only method that renders JS
and actively clears Cloudflare challenges. Needs only a URL, so it
registers into base.REGISTRY."""
from __future__ import annotations

from .base import FetchError, _decode, register


@register("stealthy")
def fetch_stealthy(url: str) -> tuple[bytes, str, dict]:
    """Render `url` in a real, fingerprint-spoofed Chromium via Scrapling's
    StealthyFetcher, solving Cloudflare Turnstile/Interstitial challenges if
    one is served. The only method in the chain that executes JS, so it's
    the last live-fetch attempt before falling back to archives -- heavier
    (spins up a browser) than every method before it, worth paying only
    after direct/proxy have failed or come back thin."""
    from scrapling.fetchers import StealthyFetcher  # noqa: PLC0415 -- heavy import, paid only when this method runs

    try:
        resp = StealthyFetcher.fetch(url, solve_cloudflare=True, network_idle=True)
    except Exception as e:  # noqa: BLE001
        raise FetchError(f"stealthy fetch failed: {e}") from e

    if resp.status >= 400:
        raise FetchError(f"stealthy fetch failed: HTTP {resp.status}")

    data = resp.body
    ctype = resp.headers.get("content-type") or resp.headers.get("Content-Type") or ""
    return data, _decode(data, ctype), {"content_kind": "html", "via_browser": True, "solve_cloudflare": True}
