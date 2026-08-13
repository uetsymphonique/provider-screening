"""Shared machinery for scripts/htmlstage/html_to_text.py: staging, extraction, and
multi-method fetching (direct / r.jina.ai proxy / Common Crawl). Kept as a
package (not inlined into html_to_text.py) so the CLI stays a thin driver
and each concern is independently testable.
"""
