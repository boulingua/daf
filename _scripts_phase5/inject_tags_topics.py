#!/usr/bin/env python3
"""
inject_tags_topics.py — write `topic:`, `tags:` and `materials_status:`
into every DaF unit article's frontmatter.

Tags are derived deterministically from existing fields so the operation
is idempotent and reviewable:

  - level-<a1..c1>            from cefr_level
  - modul-<sprechen|lesen|...> from pruefungs_module (1..n)
  - skill-<x>                  from skills_focus (1..n)
  - topic-<x>                  from the topic table below

Unit→topic mapping is hand-curated once here (60 entries). Sister sites
will need their own mapping; the helper structure is identical.

Run from repo root:  python _scripts_phase5/inject_tags_topics.py
"""
from __future__ import annotations

import re
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)

# Hand-curated unit_slug → topic_id. Curated from unit titles + cefr_can_do.
UNIT_TOPIC: dict[str, str] = {
    # A1 — almost entirely Alltag, with one Arbeit unit
    "begruessung-und-name": "alltag",
    "meine-familie": "alltag",
    "woher-kommst-du": "alltag",
    "meine-wohnung": "alltag",
    "essen-und-trinken": "alltag",
    "einkaufen-und-preise": "alltag",
    "uhrzeit-und-wochenplan": "alltag",
    "wetter-und-jahreszeiten": "alltag",
    "koerper-und-gesundheit": "alltag",
    "mein-beruf": "arbeit",
    "meine-freizeit": "alltag",
    "reisen-und-unterwegs": "alltag",
    # A2
    "arbeitssuche-und-stellenanzeige": "arbeit",
    "wohnung-mieten": "alltag",
    "beim-arzt": "alltag",
    "im-amt": "gesellschaft",
    "reiseplanung": "alltag",
    "hobbys-und-vereine": "kultur",
    "feste-und-traditionen": "kultur",
    "gestern-und-vergangenheit": "alltag",
    "plaene-und-zukunft": "alltag",
    "medien-im-alltag": "kommunikation",
    "umwelt-und-alltag": "umwelt",
    "freundschaft-und-familiengeschichte": "alltag",
    # B1
    "neuanfang-in-basel": "alltag",
    "der-bewerbungsweg": "arbeit",
    "weiterbildung-und-studium": "arbeit",
    "gesundheitssystem-dach": "gesellschaft",
    "digitale-kommunikation": "kommunikation",
    "umwelt-und-mobilitaet": "umwelt",
    "interkulturelle-begegnung": "kommunikation",
    "stadt-und-land": "gesellschaft",
    "konsum-und-verbraucherschutz": "umwelt",
    "politik-und-teilhabe": "gesellschaft",
    "persoenliche-beziehungen": "alltag",
    "zukunftsvisionen": "gesellschaft",
    # B2
    "medienlandschaft-heute": "kommunikation",
    "wissenschaft-kommunizieren": "wissenschaft",
    "gesellschaftliche-debatten": "gesellschaft",
    "arbeitswelt-im-wandel": "arbeit",
    "kunst-und-kultur": "kultur",
    "migrationsdiskurs": "gesellschaft",
    "gesundheitspolitik": "gesellschaft",
    "umweltpolitik": "umwelt",
    "bildungsdebatten": "arbeit",
    "ethik-digitaler-technologien": "wissenschaft",
    "oekonomie-fuer-laien": "gesellschaft",
    "literarische-perspektiven": "kultur",
    # C1
    "literarisches-argumentieren": "kultur",
    "politische-diskursanalyse": "gesellschaft",
    "wissenschaftstheorie": "wissenschaft",
    "aesthetik-und-urteil": "kultur",
    "identitaet-und-sprache": "wissenschaft",
    "postkoloniale-perspektiven": "kultur",
    "historiografie": "kultur",
    "philosophie-fuer-informierte-laien": "wissenschaft",
    "fachsprachen-wirtschaft-medizin-recht": "wissenschaft",
    "stilistik-und-rhetorik": "wissenschaft",
    "literarische-moderne": "kultur",
    "gegenwartsliteratur": "kultur",
}


def derive_tags(fm: dict, slug: str) -> list[str]:
    tags: list[str] = []
    if lvl := fm.get("cefr_level"):
        tags.append(f"level-{str(lvl).lower()}")
    for m in fm.get("pruefungs_module") or []:
        tags.append(f"modul-{str(m).lower()}")
    for s in fm.get("skills_focus") or []:
        tags.append(f"skill-{str(s).lower()}")
    if topic := UNIT_TOPIC.get(slug):
        tags.append(f"topic-{topic}")
    # Deduplicate but preserve order so diffs stay readable.
    seen: set[str] = set()
    out: list[str] = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def patch(md: Path) -> bool:
    text = md.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        print(f"  skip  {md.relative_to(REPO)} (no frontmatter)")
        return False
    fm = yaml.safe_load(m.group(1)) or {}
    slug = fm.get("unit_slug") or md.stem.split("_", 1)[-1]
    if slug not in UNIT_TOPIC:
        print(f"  WARN  {md.relative_to(REPO)} ({slug}) not in UNIT_TOPIC")
        return False

    fm["topic"] = UNIT_TOPIC[slug]
    fm["tags"] = derive_tags(fm, slug)
    fm["materials_status"] = "placeholder"

    new_fm = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    md.write_text(f"---\n{new_fm}\n---\n{text[m.end():]}", encoding="utf-8")
    return True


def main() -> int:
    n = 0
    for md in sorted(CONTENT.glob("kurs_*/units/unit*.md")):
        if patch(md):
            n += 1
    print(f"\n{n} unit articles patched.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
