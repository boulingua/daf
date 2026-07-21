# DaF — Deutsch als Fremdsprache (A1–C1)

<img src="brand/icon.png" alt="German icon" width="64" align="right">

Ein Kurscurriculum für **Deutsch als Fremdsprache** entlang des
Gemeinsamen Europäischen Referenzrahmens (GER / CEFR), mit
GER-Modellprüfungen pro Einheit. Fünf GER-Stufen **A1, A2, B1,
B2, C1** zu je **12 Einheiten** — **60 Einheiten insgesamt**.

Autorin: **S. Le Boulanger**. Live-Site:
<https://boulingua.github.io/daf/>

## Schwesternsites

Die DaF-Site ist Teil eines vierteiligen Schwesternsite-Projekts
unter der GitHub-Organisation `boulingua`:

- **[EFL BW](https://boulingua.github.io/efl/)** — English, Gesamtschule BW, Kl. 5–13
- **[FLE BW](https://boulingua.github.io/fle/)** — Français, Gesamtschule BW, Kl. 6–13
- **DaF** — Deutsch als Fremdsprache, A1–C1 (diese Site)
- **[Ressourcen](https://boulingua.github.io/ressources/)** — kuratierter Ressourcen-Hub

Visuelle und strukturelle Entscheidungen sind über alle vier
Sites hinweg identisch (Palette, Typografie, Navbar-Architektur,
Fünf-Schritt-Didaktik).

## Architektur

- Gebaut mit **[Quarto](https://quarto.org)**.
- Jede Einheit rendert **zweimal** aus einer einzigen `.qmd`-Quelle:
  HTML-Artikel + Reveal.js-Foliensatz.
- GER-Modellprüfungsaufgabe pro Einheit als eigenständiges PDF.
- Platzhalter-Arbeitsblatt-PDF pro Einheit (echte Inhalte folgen).
- Hell/Dunkel-Toggle. Lucide-Icons. Keine urheberrechtlich
  geschützten Medien.

Deploy via **GitHub Actions** (`actions/deploy-pages@v4`).

## Pädagogisches Modell

Fünfstufig (mit deutscher Terminologie):
**Einstieg → Input → Üben → Anwenden → Reflexion**.

Bei Prüfungsvorbereitungs-Einheiten:
**Aufgabe → Modell → Strategie → Versuch → Feedback**.

## Prüfungsformate

Pro GER-Stufe wird ein Prüfungsformat im Ordner
`_resources/format_<stufe>.yml` dokumentiert. Diese YAML-
Dateien sind die autoritative Quelle für Aufgabentyp, Itemzahl,
Zeitvorgaben, Punkteverteilung und Bewertungskriterien jeder
Prüfungssimulation auf der Site. Die Formate sind an den im
[Literaturverzeichnis](literatur.qmd) genannten Modellsätzen
orientiert, ohne deckungsgleich zu sein.

| Stufe | Prüfungsmodell           | Prüfung             | Bestehensgrenze |
|-------|--------------------------|---------------------|-----------------|
| A1    | 4 Module in 1 Block      | ca. 80 Min, 100 P.  | 60 P. (60 %)    |
| A2    | 4 Module in 1 Block      | 105 Min, 100 P.     | 60 P. (60 %)    |
| B1    | 4 Module modular         | je Modul 100 P.     | 60 P. pro Modul |
| B2    | 4 Module modular         | je Modul 100 P.     | 60 P. pro Modul |
| C1    | 4 Module modular         | je Modul 100 P.     | 60 P. pro Modul |

**Keine** Reproduktion offizieller Modellsatz-Texte. Alle
Stimulustexte original von S. Le Boulanger verfasst, formal an
den GER-Stufen orientiert.

## Lizenz

Zweiteiliger Lizenzsplit:

- **MIT** (`LICENSE`) — Website-Code (Quarto-Konfig, Lua-Shortcodes,
  Python-Helfer, SCSS).
- **CC-BY 4.0** (`LICENSE-content`) — didaktische und
  kuratorische Inhalte (Einheiten, Prüfungsbeispiele,
  Lernziele).

`© S. Le Boulanger · MIT / CC-BY 4.0` auf jedem Footer und
jedem PDF.

## Build lokal

```
quarto render
```

CI reproduziert denselben Build und pusht nach `gh-pages` über
die offiziellen GitHub-Pages-Actions. Details in
`.github/workflows/publish.yml` (folgt).

## Beiträge

Siehe [CONTRIBUTING](https://github.com/boulingua/.github/blob/main/CONTRIBUTING.md)
im Org-Meta-Repo. Kurzfassung: persönliches Projekt, Pull
Requests werden in der Regel nicht angenommen; Fehler bitte als
Issue melden.

## Zitation

Maschinenlesbare Metadaten in [`CITATION.cff`](CITATION.cff).
Empfohlene Zitierform:

> Le Boulanger, S. (2026). *DaF — Deutsch als Fremdsprache (A1–C1).*
> boulingua. <https://boulingua.github.io/daf/>

BibTeX:

```bibtex
@misc{leboulanger_daf_2026,
  author       = {Le Boulanger, S.},
  title        = {{DaF — Deutsch als Fremdsprache (A1--C1)}},
  year         = {2026},
  howpublished = {boulingua},
  url          = {https://boulingua.github.io/daf/},
  note         = {CC BY 4.0 (Inhalte) / MIT (Code)}
}
```

## Lizenz

Die Inhalte dieses Curriculums stehen unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); der gesamte Code (Skripte, Code-Blöcke, Beispiele) steht unter der [MIT-Lizenz](LICENSE-CODE.md).

## Einsatz von LLM-Werkzeugen

Teile dieses Projekts wurden mit Unterstützung von Large-Language-Model-Werkzeugen für eng umrissene, nicht-autorschaftliche Aufgaben erstellt: Lektorat, sprachliche Glättung, Markdown-/LaTeX-Formatierung, Gerüstbau von Boilerplate-Dateien (CI-Konfigurationen, Build-Skripte), Code-Refactoring. Verwendet wurden Chat AI, der LLM-Dienst von KISSKI (GWDG), sowie ein selbst gehostetes Mistral Small (24B, Apache-2.0), lokal betrieben über Ollama und das R-Paket ollamar — ausschließlich lokale Inferenz, ohne Übermittlung von Daten an Dritte beim selbst gehosteten Modell.

## Signature colour & icon

This project's signature accent is **`#1D87A7`** (light theme) / **`#7ECEE7`** (dark theme), paired with the **hexagon** mark (`brand/icon.svg`). The accent is *flag-safe* — the hue does not appear in the German flag — is distinct from every other boulingua language, and is kept clear of the boulingua hub blue. The whole colour system lives in the [boulingua hub](https://github.com/boulingua/website#per-language-accent-colours).
