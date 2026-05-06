#!/usr/bin/env python3
"""
verify_cefr.py — DaF Goethe Phase-6.3 gate.

Every unit article (content/kurs_*/units/unit*.md) must carry
`cefr_level` set to exactly one of A1, A2, B1, B2, C1, C2.

Exit 1 on any violation, with file-pathed ::error:: messages.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"
ALLOWED = {"A1", "A2", "B1", "B2", "C1", "C2"}
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def main() -> int:
    bad: list[tuple[str, str]] = []
    n = 0
    for md in sorted(CONTENT.glob("kurs_*/units/unit*.md")):
        n += 1
        m = FM_RE.match(md.read_text(encoding="utf-8"))
        fm = yaml.safe_load(m.group(1)) if m else {}
        v = (fm or {}).get("cefr_level")
        if not v or str(v).upper() not in ALLOWED:
            bad.append((str(md.relative_to(REPO)), str(v)))

    for path, v in bad:
        print(f"::error file={path}::cefr_level='{v}' not in {sorted(ALLOWED)}")

    print(f"\nverify_cefr: {n} units checked; {len(bad)} violation(s).")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
