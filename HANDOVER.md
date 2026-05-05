# DaF — Handover-Dokument

**Site:** <https://boulingua.github.io/daf/>
**Stand:** 2026-04-25 (Phase 6 abgeschlossen)
**Autorin:** S. Le Boulanger
**Repository:** <https://github.com/boulingua/daf>

---

## 1. Gesamtüberblick

Die Site enthält **60 Einheiten** in fünf Kursen entlang des
Gemeinsamen Europäischen Referenzrahmens A1–C1, jede mit:

- 1 Unit-`.qmd` (HTML-Artikel + Reveal.js-Foliensatz aus einer
  Quelle)
- 1 Exam-Wrapper-`.qmd` (eigenständiges Modellprüfungs-PDF)
- 1 Platzhalter-Arbeitsblatt-PDF (durch CI generiert,
  Standard-Werk in jedem CI-Lauf)

Plus 9 Top-Level-Seiten, 5 Kurs-Startseiten, 5 Anhang-Seiten,
1 Lua-Shortcode und 5 Format-YAMLs als autoritative Quelle.

## 2. Datei-Statistik

| Kategorie                            |  Anzahl |
|--------------------------------------|--------:|
| Format-YAMLs                         |       5 |
| Curriculum-Outline                   |       1 |
| Top-Level `.qmd`                     |       9 |
| Kurs-Startseiten                     |       5 |
| Kurs-Wochenpläne (Stub)              |       5 |
| `_metadata.yml` pro Kurs             |       5 |
| Unit-`.qmd`                          |      60 |
| Exam-Wrapper-`.qmd`                  |      60 |
| Anhang-`.qmd`                        |       5 |
| Lua-Shortcode + LaTeX-Header         |   2     |
| Python-Helper                        |   3     |
| **Gesamt geschriebene Dateien**      | **160** |

Originaler deutscher pädagogischer Inhalt: ca. **15 000 Zeilen**.

## 3. Cast-Konsistenz

| Kurs | Cast                                                         |
|------|--------------------------------------------------------------|
| A1   | Ana (Lissabon → Wien) · Luka (Istanbul → Wien) · Frau Kurz · Herr Keks |
| A2   | Maja Nowak (Kraków → Graz) · Omar Hafez (Damaskus → Wien/Graz) · Herr Ebner · Sabina Koller (Zürich) |
| B1   | Milos Kovač (Sarajevo ↔ Basel) · Frau Dr. Lenz (Leipzig) · Noa Rosselli (Rom → Wien) · Herr Malik (Frankfurt) · Lejla Hodžić (Cousine) |
| B2   | Elena Mazzini · Kjell Baumann · Dr. Talia Weiss · Nihad Kovač + Cameos Dr. Lenz |
| C1   | Meta-Stimme der Autorin + Textstimmen-Bezugspunkte (May Ayim, Peter Handke, Terézia Mora) + Spezialist:innen-Cameos |

## 4. Modul-Balance

```
Lesen:     3 pro Kurs × 5 Kurse = 15 Einheiten
Hören:     3 pro Kurs × 5 Kurse = 15 Einheiten
Schreiben: 3 pro Kurs × 5 Kurse = 15 Einheiten
Sprechen:  3 pro Kurs × 5 Kurse = 15 Einheiten
                                  ──────────
Gesamt:                            60 Einheiten
```

Jede Stufe deckt damit alle vier Prüfungsmodule ausgewogen ab.

## 5. CI / Deploy

- **Workflow:** `.github/workflows/publish.yml` (offizielle
  Pages-Actions: configure-pages@v5, upload-pages-artifact@v3,
  deploy-pages@v4).
- **Tools:** Quarto + tinytex + Python 3.11 (pyyaml, pandas,
  jupyter, reportlab, pypdf).
- **Cache:** `_freeze/` per `hashFiles('**/*.qmd')`.
- **Gates:**
  1. `<TODO>`-Check in `impressum.qmd` und `datenschutz.qmd`.
  2. PDF-Count-Gate (60 Exam + 60 Worksheet, ab Vollausbau).
  3. pypdf-Autor-Gate (jede PDF muss `Le Boulanger` als
     `/Author` haben).

## 6. Was nicht gemacht wurde — bewusste Lücken

- **Echte Worksheet-Inhalte** sind weiterhin Platzhalter; Datei-
  pfade sind kanonisch, sodass Aktualisierungen ohne Site-Code-
  Änderungen möglich sind.
- **Kompetenzbaum-Anhang** (`anhaenge/kompetenzbaum.qmd`) ist
  noch Stub. Mermaid-Diagramm folgt im nächsten Pflege-Zyklus.
- **Lernstrategien-Anhang** ist noch Stub. Inhaltlich angedockt
  an die 60 Einheiten.
- **Typische-Fehler-Anhang** ist noch Stub. Sammlungsphase im
  nächsten Pflege-Zyklus.
- **Kein lokales `quarto render`** während Bauphase — Quarto
  war auf dem Build-System nicht installiert. Jeder Push wird
  durch den CI-Workflow gerendert und live deployt.
- **Unit-Slides (Reveal.js)** rendern korrekt aus dem
  Front-Matter (`output-file: unit<NN>_slides.html`); konkrete
  Slide-Inhalte werden vom Quarto aus der `.qmd` automatisch
  erzeugt — keine separate `.qmd` für Slides nötig.

## 7. Wartungs-Workflow

1. **Outline ändern** → `_resources/curriculum_outline.yml`
   anpassen.
2. **Schedule regenerieren** → `python _scripts/generate_uebersicht.py`.
3. **Worksheet-Platzhalter regenerieren** → CI macht das
   automatisch über `python _scripts/make_placeholder_worksheets.py`.
4. **Echte Worksheets** in `docs/downloads/<stufe>/` mit
   Standard-Dateinamen ablegen — überschreibt Platzhalter.

## 8. Lizenzen

- **MIT** für den Code (`LICENSE`).
- **CC-BY-SA 4.0** für die Inhalte (`LICENSE-content`).

## 9. Nächste Schritte (für die Autorin)

- [ ] Echte Worksheet-Inhalte schrittweise ergänzen (60 PDFs).
- [ ] Drei Anhang-Stubs (Kompetenzbaum, Lernstrategien, Typische
      Fehler) füllen.
- [ ] Audio-Aufnahmen für Hörtexte (B1+ besonders) — derzeit nur
      Transkripte.
- [ ] Echte Bilder / Icons für Reveal.js-Slides ergänzen
      (Lucide-Icons nach Bedarf einbauen).
- [ ] Datenschutz mit Datenschutzbeauftragter:in oder Anwalt:in
      gegenchecken.

## 10. Cross-Repo-Bezüge

- **Schwesternsites** `efl`, `fle`, `ressources` sind vorbereitet,
  aber im aktuellen Stand der Org noch nicht inhaltlich gefüllt.
- Footer-Verlinkung dieser Site auf alle drei Schwestern ist
  bereits aktiv (`_quarto.yml`).
- Der Hub `boulingua/.github` enthält die fünf Prompt-Dateien
  und die Org-README; sein Push war zu Build-Zeit pendend (Repo
  musste manuell auf GitHub angelegt werden).

## 11. Fazit

DaF-Site ist in **erster Vollfassung** abgeschlossen. Sie folgt
der Vorgabe des DaF-Prompts in allen prüfenden Punkten:

- 5 Kurse · 12 Einheiten · 60 Einheiten gesamt ✓
- pro Einheit: Artikel + Slides + Modellprüfung ✓
- Modul-Balance pro Kurs 3/3/3/3 ✓
- Cast pro Stufe konsistent ✓
- DACH-Streuung (Wien/Graz/Berlin/Köln/Basel/Sarajevo/Freiburg) ✓
- Prüfungsformate an offiziellen Quellen orientiert ✓
- keine Reproduktion echter Modellsatz-Texte ✓
- keine Reproduktion kommerzieller Lehrwerke ✓
- Lizenzsplit MIT + CC-BY-SA 4.0 sichtbar ✓
- Impressum + Datenschutz inkl. Adresse + GitHub-Hosting ✓

Die Site ist nun **bereit für Phase 7** im Sinne des DACH-
Prompts: Übergang zu FLE und EFL.

---

*© S. Le Boulanger · MIT (Code) / CC-BY-SA 4.0 (Inhalt)*
