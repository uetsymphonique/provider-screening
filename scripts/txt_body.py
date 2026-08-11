"""View the article body of a staged docs.trendmicro.com .txt file.

The staged text interleaves article chrome, the body, and a big JSON nav
tree. This helper prints the body region (between the article 'Title/Content'
markers and the first JSON nav blob) so quote extraction targets real prose.
Usage: python scripts/txt_body.py <file.txt> [pattern...]
"""
import re
import sys


def body_of(text: str) -> str:
    # Cut at the JSON nav tree (a '[' followed by '{"title"')
    m = re.search(r"\[\{\"title\"", text)
    if m:
        text = text[: m.start()]
    # Drop leading chrome up to the 'Title' 'Content' markers if present
    m = re.search(r"Title\nContent\n", text)
    if m:
        text = text[m.end():]
    return text


def main() -> int:
    path = sys.argv[1]
    pats = [p.lower() for p in sys.argv[2:]]
    t = open(path, encoding="utf-8", errors="replace").read()
    body = body_of(t)
    if not pats:
        print(body[:6000])
        return 0
    lines = body.splitlines()
    for i, ln in enumerate(lines):
        ll = ln.lower()
        if any(p in ll for p in pats):
            start = max(0, i - 2)
            end = min(len(lines), i + 4)
            print("\n".join(lines[start:end]))
            print("-----")
    return 0


if __name__ == "__main__":
    sys.exit(main())
