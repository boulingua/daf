#!/usr/bin/env python3
"""
inject_aliases.py — add Hugo `aliases:` frontmatter entries so every
public URL the old Quarto deploy served still resolves on the new
Hugo deploy.

Mapping rules:
  content/<x>.md             aliases  /<x>.html
  content/anhaenge/<x>.md    aliases  /anhaenge/<x>.html
  content/kurs_<L>/_index.md aliases  /kurs_<L>/index.html, /kurs_<L>/uebersicht.html
  content/kurs_<L>/units/unit<NN>_<slug>.md
                             aliases  /kurs_<L>/units/unit<NN>_<slug>.html
                                      /kurs_<L>/units/unit<NN>_slides.html
  content/_index.md          aliases  /index.html

The two HANDOVER.html and LEGAL.html URLs from the old sitemap are
intentionally NOT redirected — those were repo docs, not user-facing
curriculum. They will 404 on the new site (improvement, not regression).
"""
from __future__ import annotations

import re
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def patch(md: Path, aliases: list[str]) -> None:
    text = md.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        print(f"  skip  {md.relative_to(REPO)} (no frontmatter)")
        return
    fm = yaml.safe_load(m.group(1)) or {}
    cur = fm.get("aliases") or []
    merged = list(dict.fromkeys(list(cur) + aliases))
    if merged == cur:
        return
    fm["aliases"] = merged
    new_fm = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    md.write_text(f"---\n{new_fm}\n---\n{text[m.end():]}", encoding="utf-8")
    print(f"  +     {md.relative_to(REPO)}  ({len(aliases)} aliases)")


def main() -> int:
    UNIT_RE = re.compile(r"^unit(\d{2})_([a-z0-9_-]+)\.md$")

    # Top-level pages
    for md in CONTENT.glob("*.md"):
        if md.name == "_index.md":
            patch(md, ["/index.html"])
        else:
            stem = md.stem
            patch(md, [f"/{stem}.html"])

    # Anhaenge
    for md in (CONTENT / "anhaenge").glob("*.md"):
        patch(md, [f"/anhaenge/{md.stem}.html"])

    # Course landings
    for course in sorted(CONTENT.glob("kurs_*")):
        idx = course / "_index.md"
        if idx.exists():
            patch(idx, [
                f"/{course.name}/index.html",
                f"/{course.name}/uebersicht.html",
            ])
        units_dir = course / "units"
        if not units_dir.is_dir():
            continue
        for md in sorted(units_dir.glob("unit*.md")):
            m = UNIT_RE.match(md.name)
            if not m:
                continue
            nr = m.group(1)
            stem = md.stem
            patch(md, [
                f"/{course.name}/units/{stem}.html",
                f"/{course.name}/units/unit{nr}_slides.html",
            ])
    return 0


if __name__ == "__main__":
    main()
