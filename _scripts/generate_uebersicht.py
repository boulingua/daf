"""Generate `uebersicht.qmd` from `_resources/curriculum_outline.yml`.

Run from repo root:
    python _scripts/generate_uebersicht.py

Writes the full 60-Unit overview as one sortable Markdown table.
Re-run after every outline change.
"""

from __future__ import annotations

import pathlib
import sys

try:
    import yaml
except ImportError:
    print("pyyaml not installed — pip install pyyaml", file=sys.stderr)
    sys.exit(1)


REPO = pathlib.Path(__file__).resolve().parent.parent
OUTLINE = REPO / "_resources" / "curriculum_outline.yml"
OUTPUT = REPO / "uebersicht.qmd"


HEADER = """---
title: "Übersicht"
---

::: {.hero-kicker}
DAF · 60 EINHEITEN · 5 GER-STUFEN
:::

# Vollständige Übersicht aller 60 Einheiten

Diese Tabelle wird automatisch aus
[`_resources/curriculum_outline.yml`](https://github.com/boulingua/daf/blob/main/_resources/curriculum_outline.yml)
generiert (siehe `_scripts/generate_uebersicht.py`). Jede Zeile
verlinkt direkt auf die Einheit.

| Kurs | Nr | Einheit | Modul | Skills | Thematik |
|------|---:|---------|-------|--------|----------|
"""

FOOTER = """

## Hinweise

- **Modul** = vertieftes GER-Prüfungsmodul der Einheit
  (Lesen / Hören / Schreiben / Sprechen).
- **Skills** = breitere GER-Fertigkeiten der Einheit
  (hoeren · lesen · sprechen · schreiben · sprachmittlung ·
  sprachreflexion).
- Alle Einheiten haben ein eigenes **Prüfungsbeispiel-PDF** und
  ein **Arbeitsblatt-Platzhalter-PDF**.

## Kursstartseiten

- [A1 — Anfänger:innen](kurs_a1/index.qmd) ·
  [A2 — Grundlegende Kenntnisse](kurs_a2/index.qmd) ·
  [B1 — Selbstständig (untere Stufe)](kurs_b1/index.qmd) ·
  [B2 — Selbstständig (obere Stufe)](kurs_b2/index.qmd) ·
  [C1 — Kompetent](kurs_c1/index.qmd)

## Modul-Verteilung gesamt

Jeder Kurs hat 3 Einheiten pro Modul; insgesamt:

| Modul     | Einheiten gesamt |
|-----------|------------------:|
| Lesen     | 15               |
| Hören     | 15               |
| Schreiben | 15               |
| Sprechen  | 15               |
| **Summe** | **60**           |
"""


def slugify_filename(course_id: str, unit_nr: int, slug: str) -> str:
    return f"{course_id}/units/unit{unit_nr:02d}_{slug}.qmd"


def main() -> int:
    if not OUTLINE.exists():
        print(f"{OUTLINE} not found.", file=sys.stderr)
        return 1

    plan = yaml.safe_load(OUTLINE.read_text(encoding="utf-8"))
    rows: list[str] = []

    for course in plan["courses"]:
        cid = course["id"]
        cefr = course["cefr_level"]
        for unit in course["units"]:
            n = unit["unit_nr"]
            slug = unit["slug"]
            title = unit["title"]
            modul = unit["pruefungs_module"]
            skills = " · ".join(unit.get("skills_focus", []))
            link = slugify_filename(cid, n, slug)
            rows.append(
                f"| {cefr} | {n:>2} | [{title}]({link}) | {modul} | {skills} | "
            )

    OUTPUT.write_text(HEADER + "\n".join(rows) + FOOTER, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(REPO)} with {len(rows)} unit rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
