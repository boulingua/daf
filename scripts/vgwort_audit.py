#!/usr/bin/env python3
"""
vgwort_audit.py — flag long-form content (>=1800 chars body, post
shortcode/HTML strip) that has no VG Wort Zählmarke registered.

Looks for a token in:
  1. per-page frontmatter (`vgwort_pixel:` or `vgwort:`)
  2. data/vgwort.yaml entry whose `path` matches the .md path

Emits ::warning:: on every miss so the CI run shows them. Does NOT
fail the build — registration is async (you can't generate a
Zählmarke from CI). Exit 0 always.

Run from repo root:  python scripts/vgwort_audit.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"
DATA = REPO / "data" / "vgwort.yaml"
MIN_CHARS = 1800

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
SHORTCODE_RE = re.compile(r"\{\{[<%].*?[>%]\}\}", re.S)
HTML_TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def load_registry() -> dict[str, dict]:
    if not DATA.exists():
        return {}
    raw = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    if not raw or not isinstance(raw, list):
        return {}
    # Accept both key forms. The registry moved from path: to url: because a
    # path: key names the exact source file and stops matching the moment that
    # file moves — including the URL-neutral move to a leaf bundle. This script
    # walks source files, so it derives the URL the way Hugo does: a page and
    # its bundle form both resolve to the containing directory.
    #
    # Deriving is acceptable HERE and nowhere else in the VG Wort path. This is
    # an advisory warning about pages that look long enough to register; being
    # wrong costs a spurious line of output. The registry itself is keyed by
    # measurement, because being wrong there costs the mark.
    out: dict[str, dict] = {}
    for e in raw:
        if "path" in e:
            out[e["path"]] = e
        if "url" in e:
            out[str(e["url"]).strip("/")] = e
    return out


def body_chars(md_text: str) -> int:
    body = FM_RE.sub("", md_text, count=1)
    body = SHORTCODE_RE.sub(" ", body)
    body = HTML_TAG_RE.sub(" ", body)
    body = WS_RE.sub(" ", body)
    return len(body.strip())


def main() -> int:
    registry = load_registry()
    flagged = 0
    skipped = 0
    for md in sorted(CONTENT.rglob("*.md")):
        rel = md.relative_to(REPO).as_posix()
        # Don't audit hub/list pages.
        if md.name == "_index.md":
            skipped += 1
            continue
        if rel.startswith("content/materials/"):
            skipped += 1
            continue
        text = md.read_text(encoding="utf-8")
        m = FM_RE.match(text)
        fm = yaml.safe_load(m.group(1)) if m else {}
        if (fm or {}).get("vgwort_pixel") or (fm or {}).get("vgwort"):
            continue
        if rel in registry:
            continue
        parts = rel.split("/")[1:]          # drop the leading content/
        if parts and parts[-1] in ("index.md", "_index.md"):
            parts = parts[:-1]
        elif parts:
            parts[-1] = parts[-1][:-3] if parts[-1].endswith(".md") else parts[-1]
        if "/".join(parts) in registry:
            continue
        chars = body_chars(text)
        if chars >= MIN_CHARS:
            print(f"::warning file={rel}::{chars} chars >= {MIN_CHARS} but no VG Wort Zählmarke registered")
            flagged += 1

    print(f"\nvgwort_audit: {flagged} unregistered long-form page(s); {skipped} pages skipped (lists/hub).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
