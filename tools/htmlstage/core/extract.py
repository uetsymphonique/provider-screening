"""HTML-to-text extraction: Trafilatura primary, stdlib tag-stripper fallback.

Trafilatura's boilerplate-removal heuristics (nav/header/footer/ad stripping)
beat the hand-rolled tag-stripper on real vendor pages, but it can return
None on very short or irregularly-structured pages -- _TextExtractor never
returns None, so it's the backstop that guarantees a page never silently
yields 0 chars just because Trafilatura's heuristics bailed.
"""
from __future__ import annotations

import re
from html.parser import HTMLParser

import trafilatura

# Trafilatura's own MIN_EXTRACTED_SIZE (settings.cfg) -- below this, its
# internal pipeline treats a first-pass extraction as "not enough, retry
# with recall settings". Reused here as the auto-fallback-chain threshold
# in main.py: a result this short is "not real content", not a
# small-but-valid page (min useful page bodies run well above 250 chars).
MIN_REAL_CONTENT_CHARS = 250

# Known bot-challenge / interstitial page banners (Cloudflare, Incapsula,
# PerimeterX/HUMAN, Akamai, generic captcha walls). These pages are HTTP 200
# and often extract to well over MIN_REAL_CONTENT_CHARS (retry countdown
# text, "why am I seeing this" explainer, support links) so the length check
# alone lets them through as if they were real content -- matched here so
# the auto chain in main.py escalates past them too. Lowercase,
# checked as substrings against lowercased extracted text.
INTERSTITIAL_SIGNATURES = (
    "checking your browser before accessing",
    "just a moment...",
    "attention required! | cloudflare",
    "please stand by, while we are checking your browser",
    "enable javascript and cookies to continue",
    "verifying you are human",
    "press & hold to confirm you are a human",
    "additional security check is required",
    "request unsuccessful. incapsula incident id",
    "pardon our interruption",
    "ddos protection by",
)

# Tags whose content is never real page text and should be dropped entirely
# rather than leaked into the extracted text. nav/header/footer/aside are
# site chrome (breadcrumbs, sidebar TOC, global nav) -- confirmed empirically
# on a real vendor docs page (docs.paloaltonetworks.com/.../pa-400r-.../
# physical-specifications): 107 of 150 extracted lines were duplicated
# nav/breadcrumb chrome, only 43 were the actual spec content. Tradeoff: a
# page that nests real content inside <header> (e.g. an <article>'s title
# block) would lose that too -- accepted, since vendor spec/product pages
# rarely structure content that way and the chrome-noise cost was far larger
# across real samples.
SKIP_TAGS = {"script", "style", "noscript", "template", "svg",
             "nav", "header", "footer", "aside"}

# Block-level tags: emit a newline at open/close so paragraph structure
# survives (helps keep quotes on recognizable line boundaries for later
# grounding checks, though checks should still normalize whitespace).
BLOCK_TAGS = {
    "p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6",
    "section", "article", "ul", "ol", "table", "blockquote", "main",
}

# Table cell tags: emit a " | " separator, NOT a newline -- otherwise
# adjacent cells on the same row concatenate with no boundary at all
# (e.g. a "10 Gbps" throughput cell next to a "2 ms" latency cell becomes
# the unreadable, misleading "10 Gbps2 ms"). This matters most for spec
# tables, which is exactly where numeric_threshold checklist items pull
# their numbers from.
CELL_TAGS = {"td", "th"}


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._chunks: list[str] = []
        self._skip_stack: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:  # noqa: ANN001
        if tag in SKIP_TAGS:
            self._skip_stack.append(tag)
        elif tag in CELL_TAGS:
            self._chunks.append(" | ")
        elif tag in BLOCK_TAGS:
            self._chunks.append("\n")

    def handle_startendtag(self, tag: str, attrs) -> None:  # noqa: ANN001
        if tag == "br":
            self._chunks.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self._skip_stack and self._skip_stack[-1] == tag:
            self._skip_stack.pop()
        elif tag in BLOCK_TAGS:
            self._chunks.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_stack:
            return
        self._chunks.append(data)

    def get_text(self) -> str:
        raw = "".join(self._chunks)
        lines = []
        for ln in raw.splitlines():
            ln = re.sub(r"[ \t]+", " ", ln).strip()
            ln = re.sub(r"\s*\|\s*", " | ", ln).strip(" |")
            if ln:
                lines.append(ln)
        return "\n".join(lines) + "\n" if lines else ""


def detect_interstitial(text: str) -> str | None:
    """Return the matched signature if `text` looks like a bot-challenge
    page rather than real content, else None."""
    lowered = text.lower()
    for sig in INTERSTITIAL_SIGNATURES:
        if sig in lowered:
            return sig
    return None


def stdlib_extract(html_text: str) -> str:
    parser = _TextExtractor()
    parser.feed(html_text)
    return parser.get_text()


def extract_text(
    html_text: str, url: str | None = None, favor_recall: bool = False, use_fallback: bool = True
) -> tuple[str, str]:
    """Extract text from an HTML string. Returns (text, engine_used)."""
    text = trafilatura.extract(
        html_text,
        url=url,
        output_format="txt",
        include_tables=True,
        include_comments=False,
        favor_precision=not favor_recall,
        favor_recall=favor_recall,
        deduplicate=True,
    )
    if text:
        return text, "trafilatura"
    if use_fallback:
        return stdlib_extract(html_text), "html_parser_fallback"
    return "", "trafilatura"
