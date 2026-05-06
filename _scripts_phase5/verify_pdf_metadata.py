#!/usr/bin/env python3
"""
verify_pdf_metadata.py — Phase-6.6 gate (restored from the Quarto-era
publish.yml). Every PDF served from this site must carry author
metadata containing 'Le Boulanger' (the canonical attribution).

Walks static/**/*.pdf. Exits 1 on any miss with file-pathed
::error:: messages.

Requires: pip install pypdf
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("::error::need pypdf — pip install pypdf", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).resolve().parent.parent
STATIC = REPO / "static"
NEEDLE = "Le Boulanger"


def main() -> int:
    pdfs = sorted(STATIC.rglob("*.pdf"))
    if not pdfs:
        print("verify_pdf_metadata: no PDFs found.")
        return 0

    bad: list[tuple[str, str]] = []
    for p in pdfs:
        rel = str(p.relative_to(REPO))
        try:
            r = PdfReader(str(p))
            author = (r.metadata or {}).get("/Author", "") or ""
        except Exception as exc:
            bad.append((rel, f"read error: {exc}"))
            continue
        if NEEDLE not in author:
            bad.append((rel, f"author='{author}' (missing '{NEEDLE}')"))

    for path, reason in bad[:50]:
        print(f"::error file={path}::{reason}")

    print(f"\nverify_pdf_metadata: {len(pdfs)} PDFs checked; {len(bad)} violation(s).")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
