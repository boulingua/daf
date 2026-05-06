#!/usr/bin/env python3
"""
inject_author_date.py — backfill `author` and `date` frontmatter on
every content/**/*.md.

- author: always "S. Le Boulanger" (the canonical attribution).
- date:   first git-commit date of the corresponding source file
          (the .qmd if it ever existed, otherwise the .md). RFC3339
          UTC. Real, not invented — derived from git, not now().

Idempotent. Skips files that already have both keys.

Run from repo root:  python _scripts_phase5/inject_author_date.py
"""
from __future__ import annotations

import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"
AUTHOR = "S. Le Boulanger"
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def first_commit_date(*paths: Path) -> str:
    """RFC3339 UTC of the earliest commit touching any of the given paths.

    Falls back to today's UTC if git has no record (new file).
    """
    best: str | None = None
    for p in paths:
        try:
            out = subprocess.check_output(
                [
                    "git",
                    "log",
                    "--diff-filter=A",
                    "--follow",
                    "--format=%aI",
                    "--",
                    str(p),
                ],
                cwd=REPO,
                text=True,
                stderr=subprocess.DEVNULL,
            ).strip().splitlines()
        except subprocess.CalledProcessError:
            continue
        if out:
            cand = out[-1]  # earliest 'A' entry across history
            if best is None or cand < best:
                best = cand
    if best:
        return best
    return datetime.now(tz=timezone.utc).isoformat(timespec="seconds")


def find_qmd_pair(md: Path) -> Path | None:
    """The .qmd that this .md was migrated from, if it ever existed in git
    (the migration deleted them, but git still remembers)."""
    rel_md = md.relative_to(REPO).as_posix()
    # content/anhaenge/glossar.md  -> anhaenge/glossar.qmd
    # content/kurs_a1/units/unit01_x.md -> kurs_a1/units/unit01_x.qmd
    # content/kurs_a1/_index.md  -> kurs_a1/index.qmd OR kurs_a1/uebersicht.qmd
    rel = rel_md[len("content/"):]
    if rel.endswith("/_index.md"):
        section = rel[: -len("/_index.md")]
        for c in (
            REPO / f"{section}/index.qmd",
            REPO / f"{section}/uebersicht.qmd",
        ):
            if file_in_git(c):
                return c
        return None
    qmd = REPO / rel.replace(".md", ".qmd")
    return qmd if file_in_git(qmd) else None


def file_in_git(p: Path) -> bool:
    rel = p.relative_to(REPO).as_posix()
    out = subprocess.run(
        ["git", "log", "--all", "--format=%H", "--", rel],
        cwd=REPO, text=True, capture_output=True,
    )
    return out.returncode == 0 and out.stdout.strip() != ""


def patch(md: Path) -> str | None:
    text = md.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        return "no frontmatter"
    fm = yaml.safe_load(m.group(1)) or {}

    has_author = bool(fm.get("author"))
    has_date = bool(fm.get("date"))
    if has_author and has_date:
        return None  # nothing to do

    if not has_author:
        fm["author"] = AUTHOR
    if not has_date:
        sources = [md]
        if (q := find_qmd_pair(md)):
            sources.insert(0, q)
        fm["date"] = first_commit_date(*sources)

    new_fm = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    md.write_text(f"---\n{new_fm}\n---\n{text[m.end():]}", encoding="utf-8")
    return "patched"


def main() -> int:
    n_patched = 0
    n_skipped = 0
    n_nofm = 0
    for md in sorted(CONTENT.rglob("*.md")):
        r = patch(md)
        if r == "patched":
            n_patched += 1
            print(f"  +  {md.relative_to(REPO)}")
        elif r == "no frontmatter":
            n_nofm += 1
        else:
            n_skipped += 1
    print(f"\npatched={n_patched}  skipped={n_skipped}  no-frontmatter={n_nofm}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
