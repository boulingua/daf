#!/usr/bin/env python3
"""
link_audit.py — walk the rendered Hugo output, extract every internal
href, and check the target file exists. Pure stdlib, no network.

Treats /daf/foo/  -> public/foo/index.html
       /daf/foo.pdf -> public/foo.pdf
Anchors and query strings are stripped before resolution.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

PUBLIC = Path(__file__).resolve().parent.parent / "public"
PREFIX = "/daf/"

HREF_RE = re.compile(r'href=(?:["\']([^"\']+)["\']|([^\s>]+))', re.I)


def _href(m: re.Match) -> str:
    return m.group(1) or m.group(2)


SITE_HOST = "boulingua.github.io"


def resolve(href: str) -> Path | None:
    u = urlparse(href)
    if u.scheme and u.netloc and u.netloc != SITE_HOST:
        return None  # external
    p = u.path
    if not p or p.startswith("#"):
        return None
    if not p.startswith("/"):
        return None
    if not p.startswith(PREFIX):
        return None
    rel = p[len(PREFIX):].lstrip("/")
    if rel == "":
        return PUBLIC / "index.html"
    if rel.endswith("/"):
        return PUBLIC / (rel + "index.html")
    if "." not in Path(rel).name:
        return PUBLIC / (rel + "/index.html")
    return PUBLIC / rel


def main() -> int:
    if not PUBLIC.is_dir():
        print("public/ not found — run hugo --minify first", file=sys.stderr)
        return 2

    bad: list[tuple[str, str]] = []
    seen = 0
    for html in PUBLIC.rglob("*.html"):
        text = html.read_text(encoding="utf-8", errors="replace")
        for m in HREF_RE.finditer(text):
            href = _href(m)
            target = resolve(href)
            if target is None:
                continue
            seen += 1
            if not target.exists():
                bad.append((str(html.relative_to(PUBLIC)), href))

    if bad:
        print(f"BROKEN: {len(bad)} internal link(s) (out of {seen} checked)")
        for src, href in bad[:50]:
            print(f"  {src}  ->  {href}")
        return 1
    print(f"clean: {seen} internal links resolved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
