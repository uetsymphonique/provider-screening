"""r.jina.ai-based proxy fetchers: HTML-mode render and Markdown-mode
render. Both need only a URL, so both register into base.REGISTRY."""
from __future__ import annotations

import urllib.request

from .base import FetchError, register

PROXY = "https://r.jina.ai/"


@register("proxy-html")
def fetch_proxy_html(url: str, timeout: int = 90) -> tuple[bytes, str, dict]:
    """Render via r.jina.ai in HTML mode -- works around bot-protection
    (e.g. Incapsula challenge) that blocks fetch_direct.

    x-no-cache avoids replaying a previously-cached bot-challenge/thin
    response on retry (Reader caches for 3600s by default). x-timeout tells
    Reader to wait for network idle (up to 60s here, under our own urlopen
    timeout) instead of returning as soon as *some* content is parseable --
    without it, SPA pages that lazy-render past the fold can come back thin
    and force an unnecessary escalation to proxy-md/stealthy."""
    proxy_url = PROXY + url
    req = urllib.request.Request(
        proxy_url,
        headers={
            "User-Agent": "Mozilla/5.0 (provider-screening tools/htmlstage/main.py)",
            "Accept": "text/html,*/*;q=0.8",
            "x-respond-with": "html",
            "x-no-cache": "true",
            "x-timeout": "60",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
    except Exception as e:  # noqa: BLE001
        raise FetchError(f"proxy-html fetch failed: {e}") from e
    return data, data.decode("utf-8", errors="replace"), {
        "content_kind": "html", "via_proxy": True, "proxy_url": proxy_url,
    }


@register("proxy-md")
def fetch_proxy_md(url: str, timeout: int = 120) -> tuple[bytes, str, dict]:
    """Render via r.jina.ai in Markdown mode -- last-resort proxy fallback
    for pages whose HTML-mode render still hits a bot challenge.

    Same x-no-cache/x-timeout rationale as fetch_proxy_html -- see its
    docstring."""
    proxy_url = PROXY + url
    req = urllib.request.Request(
        proxy_url,
        headers={
            "User-Agent": "Mozilla/5.0 (provider-screening tools/htmlstage/main.py)",
            "x-no-cache": "true",
            "x-timeout": "60",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
    except Exception as e:  # noqa: BLE001
        raise FetchError(f"proxy-md fetch failed: {e}") from e
    return data, data.decode("utf-8", errors="replace"), {
        "content_kind": "markdown", "via_proxy": True, "proxy_url": proxy_url, "render_mode": "markdown",
    }
