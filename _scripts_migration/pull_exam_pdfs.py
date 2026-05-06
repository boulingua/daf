#!/usr/bin/env python3
"""
pull_exam_pdfs.py — one-time download of the 60 exam PDFs that the
Quarto deploy of boulingua.github.io/daf currently serves at
/downloads/<level>/unit<NN>_<slug>_exam.pdf.

Hugo cannot regenerate them (no LaTeX path), so we pull them in
once as static assets, preserving the existing public URL exactly.

Run from repo root:  python _scripts_migration/pull_exam_pdfs.py
"""
from __future__ import annotations

import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"
DEST = REPO / "static" / "downloads"
BASE = "https://boulingua.github.io/daf"

UNIT_RE = re.compile(r"^unit(\d{2})_([a-z0-9_-]+)\.md$")


def main() -> int:
    pulled, failed, skipped = 0, [], 0
    for course in sorted(CONTENT.glob("kurs_*")):
        units_dir = course / "units"
        if not units_dir.is_dir():
            continue
        level = course.name.removeprefix("kurs_").lower()
        for md in sorted(units_dir.glob("unit*.md")):
            m = UNIT_RE.match(md.name)
            if not m:
                continue
            nr, slug = m.group(1), m.group(2)
            name = f"unit{nr}_{slug}_exam.pdf"
            url = f"{BASE}/downloads/{level}/{name}"
            target = DEST / level / name
            if target.exists():
                skipped += 1
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    target.write_bytes(r.read())
                print(f"  pulled  {level}/{name}")
                pulled += 1
                time.sleep(0.05)
            except urllib.error.HTTPError as e:
                print(f"  FAIL    {level}/{name}  ({e.code})")
                failed.append((level, name, e.code))

    print(f"\npulled={pulled}  skipped={skipped}  failed={len(failed)}")
    if failed:
        for level, name, code in failed:
            print(f"  {level}/{name} -> HTTP {code}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
