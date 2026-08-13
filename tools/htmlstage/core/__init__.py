"""Shared machinery for tools/htmlstage/main.py: staging, extraction, and
multi-method fetching (direct / r.jina.ai proxy / Common Crawl). Kept as a
package (not inlined into main.py) so the CLI stays a thin driver
and each concern is independently testable.
"""
