"""Generate placeholder worksheet PDFs for every Unit in the
`_resources/curriculum_outline.yml` plan.

Usage:
    python _scripts/make_placeholder_worksheets.py

Writes to `docs/downloads/<stufe>/unit<NN>_<slug>_worksheet.pdf`.
Creates intermediate directories as needed.

During the scaffold phase the curriculum outline does not yet exist.
In that case, this script is a safe no-op — CI skips it via
a file-presence check, and this script also exits cleanly if the
outline is absent.
"""

from __future__ import annotations

import pathlib
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("pyyaml not installed — install with `pip install pyyaml`.", file=sys.stderr)
    sys.exit(1)

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas as _canvas
except ImportError:  # pragma: no cover
    print("reportlab not installed — install with `pip install reportlab`.", file=sys.stderr)
    sys.exit(1)

from pdf_attribution import UnitContext, apply_attribution, set_metadata


REPO = pathlib.Path(__file__).resolve().parent.parent
OUTLINE = REPO / "_resources" / "curriculum_outline.yml"
OUTPUT_ROOT = REPO / "docs" / "downloads"


def render_placeholder(out_path: pathlib.Path, ctx: UnitContext) -> None:
    """Render a one-page A4 placeholder worksheet with full attribution."""

    out_path.parent.mkdir(parents=True, exist_ok=True)
    c = _canvas.Canvas(str(out_path), pagesize=A4)
    width, height = A4

    set_metadata(c, ctx, kind="Arbeitsblatt")

    # Title block
    c.setFont("Helvetica-Bold", 16)
    c.drawString(20 * mm, height - 35 * mm, f"Arbeitsblatt — Einheit {ctx.unit_nr}: {ctx.unit_title}")

    # Meta line
    c.setFont("Helvetica", 11)
    c.drawString(
        20 * mm,
        height - 45 * mm,
        f"GER-Stufe {ctx.cefr_level.upper()} · Goethe-Zertifikat {ctx.cefr_level.upper()}",
    )

    # Body
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(20 * mm, height - 65 * mm, "Platzhalter — Arbeitsblattinhalt folgt.")
    c.setFont("Helvetica", 10)
    c.drawString(
        20 * mm,
        height - 75 * mm,
        "Dieses Arbeitsblatt wird in einer späteren Iteration mit Aufgaben gefüllt.",
    )
    c.drawString(
        20 * mm,
        height - 82 * mm,
        "Die kanonische Datei-Ablage und der Link auf der Site bleiben bei der Aktualisierung identisch.",
    )

    # Attribution (header + footer + watermark)
    apply_attribution(c, ctx)

    c.showPage()
    c.save()


def main() -> int:
    if not OUTLINE.exists():
        print(f"{OUTLINE.relative_to(REPO)} nicht gefunden — noch in Scaffold-Phase. Nichts zu tun.")
        return 0

    with OUTLINE.open("r", encoding="utf-8") as f:
        plan = yaml.safe_load(f)

    courses = plan.get("courses", [])
    total = 0

    for course in courses:
        cefr = str(course.get("cefr_level", "")).lower()
        if not cefr:
            continue
        for unit in course.get("units", []):
            ctx = UnitContext(
                cefr_level=cefr,
                unit_nr=int(unit["unit_nr"]),
                slug=str(unit["slug"]),
                unit_title=str(unit["title"]),
            )
            out = (
                OUTPUT_ROOT
                / cefr
                / f"unit{ctx.unit_nr:02d}_{ctx.slug}_worksheet.pdf"
            )
            render_placeholder(out, ctx)
            total += 1

    print(f"Generated {total} placeholder worksheet PDFs under {OUTPUT_ROOT}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
