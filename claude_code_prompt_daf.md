# ROLLE UND KONTEXT

Du bist Claude Code und agierst als Curriculum-Engineer und
Front-End-Entwicklerin für Sprachlehrmaterial. Baue eine
vollständige, deploybare **kursartige Website** mit Quarto für
**DaF (Deutsch als Fremdsprache)** im Ausland, strukturiert entlang
des Gemeinsamen Europäischen Referenzrahmens (GER / CEFR) von A1
bis C1, mit Modellprüfungen im **Goethe-Zertifikat-Format** pro
Einheit.

Diese Seite ist das **Schwesternsite** eines bereits definierten
EFL-Sites und eines FLE-Sites. Alle drei Sites sollen visuell und
strukturell identisch sein — gleiche Palette, gleiche Navbar,
gleiche Architektur, gleiche Autorin, gleiche CI-Kette. Nur die
Sprache, die Stufenstruktur und die Prüfungsformate unterscheiden
sich.

Das ist KEIN Statistik- oder Programmierkurs. Kein R-Code, keine
Code-Ausführung, kein `renv.lock`, kein `setup_check.R`, keine
R-Pakete in der CI. Jede Einheit ist eine Spracheinheit: Lesen,
Hören, Sprechen, Schreiben, Sprachmittlung, Grammatik, Wortschatz,
Landeskunde. Inhalt wird als Prosa, Tabellen, ikonenreiche Slides,
Sprechernotizen und ausgearbeitete Prüfungsbeispiele geliefert.

Architektur ist vom Dual-Format-Quarto-Scaffold übernommen:

- Mehrkurs-Landingpages mit Hero-Blöcken und Kartenrastern.
- Wochenaufteilung pro Kurs (= pro GER-Stufe).
- Jede Einheit wird ZWEIMAL aus einer einzigen `.qmd`-Quelle
  gerendert — HTML-Artikel UND Reveal.js-Foliensatz.
- Fünfstufiges pädagogisches Modell in jeder Einheit, mit
  deutscher Fachterminologie: **Einstieg → Input → Üben →
  Anwenden → Reflexion**.
  (Prüfungsvariante: **Aufgabe → Modell → Strategie → Versuch →
  Feedback**.)
- Helle + dunkle Palette mit zugänglichem Sonne/Mond-Toggle.
- GitHub-Pages-CI via offizielle `actions/deploy-pages@v4`-Actions.

# AUTORIN

Alle Inhalte stammen von **S. Le Boulanger** (gleiche Autorin wie
bei den Schwesternsites EFL und FLE) und müssen auf jeder Einheit
und jedem Foliensatz als solche erscheinen, einmalig festgelegt via
einer `_metadata.yml`-Datei im `units/`-Ordner jedes Kurses — nie
durch Bearbeitung einzelner Dateien.

# CEFR-STRUKTUR (verbatim)

Fünf parallele GER-Stufen als fünf Kurse:

- **A1 — Anfänger:innen:** absoluter Einstieg, Alltagsphrasen,
  einfaches Präsens, Ich/Du/Er-Grundlagen.
- **A2 — Grundlegende Kenntnisse:** vertraute Themen, Perfekt,
  Modalverben, einfache Nebensätze.
- **B1 — Selbstständige Sprachverwendung (untere Stufe):**
  zusammenhängende Äußerungen zu vertrauten Themen, Präteritum,
  Konjunktiv II für Höflichkeit, Konnektoren.
- **B2 — Selbstständige Sprachverwendung (obere Stufe):**
  differenzierte Meinungen, Passiv, Konjunktiv II für Irrealis,
  Partizipialkonstruktionen, komplexe Hypotaxe.
- **C1 — Kompetente Sprachverwendung:** nuancierte Argumentation,
  stilistische Register, Nominalisierung, Konnotation, Ironie,
  Fachsprache.

Das entspricht dem Standardgerüst für DaF im Ausland und deckt die
Zielstufen der Goethe-Zertifikate A1, A2, B1, B2, C1 ab. **C2 wird
bewusst ausgeklammert** — das überschreitet, was ein strukturiertes
12-Einheiten-Kurscurriculum sinnvoll leisten kann; C2 erreicht man
durch jahrelange authentische Immersion, nicht durch Lehrbucheinheiten.

Gesamt: **5 Kurse**, einer pro GER-Stufe.

# BILDUNGSPLAN-BW ALS SEKUNDÄRE INSPIRATION

Achtung — ein gerader Satz: Der Bildungsplan Baden-Württemberg 2016
(Sek I) und die Oberstufe 2021 sind **für Deutsch als Muttersprache
geschrieben**, nicht für DaF. Er kennt keine A1/A2-Kategorien und
keine Goethe-Formate. Ihn direkt 1:1 auf eine DaF-Seite zu mappen,
wäre unehrlich.

Daher wird der BW-Bildungsplan in dieser Seite **sekundär** genutzt:

- Als **Themeninspiration** (Familie, Schule, Wohnen, Freizeit,
  Beruf, Medien, Literatur, politische Teilhabe) — angepasst für
  jede GER-Stufe.
- Als **Kompetenzkatalog** für die rezeptiven, produktiven,
  interaktiven und sprachmittelnden Fertigkeiten, die auch im
  DaF-Bereich gelten.
- **Nicht** als verbatim zitierte Quelle für Unit-Metadaten. Units
  führen stattdessen `cefr_can_do`-Deskriptoren aus dem
  GER-Begleitband 2020.

Optional: Falls einzelne Einheiten echten Themenparallelismus zum
BW-Bildungsplan haben (z. B. „Berufsorientierung" in Kl. 9
entspricht einem B1-DaF-Thema), kann dies in einem optionalen
`bw_inspiration:`-Feld im Front Matter vermerkt werden — ohne
Anspruch auf offizielle curriculare Übereinstimmung.

# UMFANG

- **12 Einheiten pro GER-Stufe.** Entspricht einem typischen
  Intensivkurs-Semester oder einem Schuljahr im Ausland.
- **60 Einheiten insgesamt** über die fünf Stufen.
- Jede Einheit enthält: HTML-Artikel, Reveal.js-Foliensatz,
  Goethe-Modellprüfungsaufgabe, Arbeitsblatt (Platzhalter).

# GOETHE-PRÜFUNGSFORMATE — AUTORITATIVE QUELLEN

Pro Einheit wird eine **Goethe-Modellprüfungsaufgabe** im Format
der entsprechenden Goethe-Stufe entwickelt. Die Formate sind
öffentlich dokumentiert auf `goethe.de` unter den
Prüfungsbeschreibungen:

- **A1:** Goethe-Zertifikat A1 — Start Deutsch 1 (Erwachsene) bzw.
  Fit in Deutsch 1 (Jugendliche). Module: Lesen, Hören, Schreiben,
  Sprechen.
- **A2:** Goethe-Zertifikat A2 (Erwachsene) bzw. Fit in Deutsch
  (Jugendliche). Gleiche vier Module.
- **B1:** Goethe-Zertifikat B1 — modulare Prüfung. Module: Lesen,
  Hören, Schreiben, Sprechen (einzeln ablegbar).
- **B2:** Goethe-Zertifikat B2 — vier Module. Längere Lesetexte,
  komplexere Schreibaufgaben.
- **C1:** Goethe-Zertifikat C1 — vier Module, argumentative
  Diskussionsaufgabe, literarisch-essayistische Schreibaufgabe.

Bevor irgendeine Einheit geschrieben wird, **holt Claude Code pro
Stufe das offizielle Goethe-Modellprüfungsformat** von
`https://www.goethe.de/de/spr/kup/prf/prf.html` und den
zugehörigen stufenspezifischen Unterseiten und speichert das
extrahierte Format (Aufgabenanzahl, Aufgabentypen, Zeiten,
Punktverteilung) in `_resources/goethe_format_<stufe>.yml`.

**Keine Erfindung von Aufgabentypen.** Falls eine Seite nicht
abrufbar ist: STOP und melden. Nicht aus dem Gedächtnis
paraphrasieren.

**Keine Reproduktion echter Prüfungstexte.** Alle Stimulustexte,
Hörverstehens-Transkripte und Leseaufgaben werden original von der
Autorin verfasst, lehnen sich aber formatmäßig streng an das
Goethe-Format an.

# HARTE EINSCHRÄNKUNGEN

- **Kein R-Code, keine Code-Ausführung, keine Datensimulation.**
  Der `execute:`-Block ist aus `_quarto.yml` entfernt. Keine
  `code/`-Ordner. Keine Chunks.
- **Metasprache ist durchgängig Deutsch** (immersiv). Sogar auf A1
  wird Deutsch verwendet, aber mit massivem Scaffolding:
  parallele Bildikonen, kurze Sätze, Wiederholung, optionale
  englische/französische Worterklärungen in Klappelementen
  (`::: {.callout-tip collapse="true"}`) — niemals dominant.
  Ab B1 kein Fremdsprachen-Scaffolding mehr.
- **Jede Einheit folgt dem fünfstufigen Modell** (oder der
  Prüfungsvariante bei Prüfungsvorbereitungs-Einheiten).
- **Jede Einheit wird als HTML-Artikel UND Reveal.js-Foliensatz
  gerendert** aus einer einzigen Quelle. Front Matter jeder
  Einheit zweimal prüfen.
- **Altersunabhängig, niveauangepasst.** Die Lernenden sind
  Erwachsene oder Jugendliche mit unterschiedlichen
  Bildungshintergründen. Keine kindlichen Ansprachen. Der Ton
  passt sich dem Niveau an, nicht dem Alter:
  - **A1/A2:** sehr konkret, nah am Alltag, kurze Sätze,
    wiederkehrende Figuren, viel Bildmaterial.
  - **B1:** realistische Situationen, Arbeitswelt, Mobilität,
    kulturelle Begegnung.
  - **B2:** Argumentation, Gesellschaftsthemen,
    Meinungsbildung, Medien, Wissenschaft für Laien.
  - **C1:** literarisch-essayistisch, nuancierte Positionen,
    kritische Reflexion, Fachdiskurs.
- **Slides visuell ansprechend.** Nutze Lucide-Icons (via
  `lucide-static`-SVGs in `assets/icons/`) und generische
  Meme-Templates als SVG (z. B. „Drake", „Distracted
  Boyfriend", „Expanding Brain" — geometrische Rekonstruktionen,
  nie getracete oder heruntergeladene echte Memes). Keine
  urheberrechtlich geschützten Popkultur-Bilder. Keine
  Institutionenlogos — insbesondere **kein Goethe-Logo**, auch
  wenn das Format referenziert wird.
- **Hell/Dunkel-Toggle funktioniert beidseitig.** Body, Karten,
  Rahmen, Links und Footer folgen alle `data-bs-theme`.
- **Footer und Landing Pages verlinken echten Inhalt.** Keine
  Stubs.
- **S. Le Boulanger erscheint als Autorin auf jeder Einheit und
  jedem Foliensatz** via `_metadata.yml`.
- Keine Prüfungen außer dem Prüfungsbeispiel pro Einheit. Keine
  Benotung. Keine Emoji.
- Ton: praktisch, warm, immersiv, pädagogisch präzise. Stimme
  einer Lehrenden, nicht die eines Lehrwerkverlags.

# DESIGN-SYSTEM (verbatim, identisch zu EFL- und FLE-Sites)

## Palette

```
Hell:
  --bg #ffffff   --fg #23272b   --fg-alt #555
  --rule #eaeaea --surface #f7f8fa
  --accent #1a73e8 --accent-hover #0b57d0
  --code-bg #f5f5f5

Dunkel:
  --bg #1d1f21   --fg #e8e8e8   --fg-alt #a8a8a8
  --rule #2d3035 --surface #26292c
  --accent #79b8ff --accent-hover #b8d4fd
  --code-bg #2a2d31
```

## Typografie

- Fließtext + Überschriften: **Source Sans 3**
- Mono (Navbar-Brand, Kicker, Prüfungsformat-Labels):
  **JetBrains Mono**

## `styles.css`

Die CSS-Palette knüpft an `data-bs-theme="light"/"dark"` an (das
Attribut, das Quartos Toggle umschaltet), mit Fallback
`@media (prefers-color-scheme: dark) :root:not([data-bs-theme])`
für OS-Erkennung beim Erstbesuch. Bootstraps eigene CSS-Variablen
zur Palette zwingen:

```css
:root, [data-bs-theme="light"], [data-bs-theme="dark"] {
  --bs-body-bg: var(--bg);
  --bs-body-color: var(--fg);
  --bs-border-color: var(--rule);
  --bs-secondary-bg: var(--surface);
  --bs-tertiary-bg: var(--surface);
  --bs-emphasis-color: var(--fg);
  --bs-link-color: var(--accent);
  --bs-link-hover-color: var(--accent-hover);
  --bs-heading-color: var(--fg);
  --bs-primary: var(--accent);
}
```

Ohne dies kaskadieren `darkly`/`flatly` ineinander und der Toggle
funktioniert nur halb. Außerdem `html`, `body`, Navbar und Footer
explizit `background: var(--bg) !important` geben, damit kein
Stock-Theme durchscheint.

Enthält CSS für: Hero-Block (mit Mono-Kicker), Kartenraster
(auto-fit minmax 240px, translate-Y beim Hover), Reveal.js-
kompatible Codeblöcke (erhalten auch wenn keine R-Blöcke
genutzt werden — reiner Text-Code wie Vokabelformen oder
Satzstrukturen profitiert davon), leise Navbar (`var(--bg)` als
Hintergrund, Mono-Brand, `var(--fg-alt)`-Links, `var(--accent)`
beim Hover/Aktiv), Footer wie Body, `.icon-circle`-Helper für
Lucide-SVGs inline in Prosa, `.meme-frame` für generische
SVG-Meme-Platzhalter auf Slides, und ein `.cefr-badge`-Chip
(A1–C1 je nach Stufe unterschiedlich gefärbt: A1 grün, A2
blau-grün, B1 blau, B2 violett, C1 dunkelrot).

## `custom.scss`

```scss
/*-- scss:defaults --*/
$primary: #1a73e8;
$body-color: #23272b;
$link-color: #1a73e8;
$link-hover-color: #0b57d0;
$font-family-sans-serif: "Source Sans 3", -apple-system, BlinkMacSystemFont, sans-serif;
$font-family-monospace: "JetBrains Mono", "Fira Code", monospace;
$headings-font-weight: 600;
$border-radius: 6px;
```

## `assets/slides.scss` (Reveal.js, dunkle Palette)

```scss
/*-- scss:defaults --*/
$body-bg: #1d1f21;
$body-color: #e8e8e8;
$link-color: #79b8ff;
$presentation-font-family: "Source Sans 3", sans-serif;
$presentation-heading-color: #e8e8e8;
$code-block-bg: #2a2d31;
```

# REPOSITORY-STRUKTUR

```
<repo>/
├── daf-goethe.Rproj
├── _quarto.yml
├── index.qmd                 Startseite
├── ueber.qmd
├── start.qmd
├── uebersicht.qmd            vollständiger verlinkter Index
├── literatur.qmd
├── danksagung.qmd
├── goethe_formate.qmd        Übersicht der Prüfungsformate A1–C1
├── impressum.qmd             Rechtshinweis (TMG § 5 / DDG § 5)
├── datenschutz.qmd           Datenschutzerklärung (DSGVO)
├── styles.css
├── custom.scss
├── assets/
│   ├── slides.scss
│   ├── icons/                Lucide-SVGs, lokal abgelegt
│   └── memes/                generische SVG-Meme-Templates
├── _includes/
│   └── _exam.tex             gemeinsamer LaTeX-Header für Prüfungs-PDFs
├── _extensions/
│   └── downloads/            Lua-Shortcode für {{< downloads >}}
├── _scripts/
│   ├── make_placeholder_worksheets.py  erzeugt 60 Platzhalter-PDFs
│   ├── pdf_attribution.py              wiederverwendbarer PDF-Header/Footer/Wasserzeichen-Helper
│   └── organise_downloads.sh           schiebt Prüfungs-PDFs an kanonische Pfade
├── _resources/
│   ├── goethe_format_a1.yml
│   ├── goethe_format_a2.yml
│   ├── goethe_format_b1.yml
│   ├── goethe_format_b2.yml
│   ├── goethe_format_c1.yml
│   └── curriculum_outline.yml
├── downloads/                 (generiert; .gitignored; in CI befüllt)
├── README.md, LICENSE, .gitignore, .nojekyll
├── .github/workflows/publish.yml
├── anhaenge/
│   ├── lernstrategien.qmd
│   ├── kompetenzbaum.qmd
│   ├── glossar.qmd
│   ├── typische_fehler.qmd
│   └── bewertungsraster.qmd
├── kurs_a1/
│   ├── index.qmd
│   ├── uebersicht.qmd
│   └── units/
│       ├── _metadata.yml     author: "S. Le Boulanger"
│       ├── unit01_<slug>.qmd      … unit12_<slug>.qmd
│       └── unit01_<slug>_exam.qmd … unit12_<slug>_exam.qmd
├── kurs_a2/                  (analog)
├── kurs_b1/                  (analog)
├── kurs_b2/                  (analog)
└── kurs_c1/                  (analog)
```

# `_quarto.yml`

```yaml
project:
  type: website
  output-dir: docs

website:
  title: "DaF — S. Le Boulanger"
  description: "Ein DaF-Kursangebot entlang des Gemeinsamen Europäischen Referenzrahmens, A1 bis C1, mit Goethe-Modellprüfungen pro Einheit."
  site-url: "https://<user>.github.io/<repo>/"
  navbar:
    title: "DaF"
    left:
      - href: index.qmd
        text: "Start"
      - href: ueber.qmd
        text: "Über"
      - href: goethe_formate.qmd
        text: "Goethe-Formate"
      - href: uebersicht.qmd
        text: "Übersicht"
      - text: "GER-Stufen"
        menu:
          - href: kurs_a1/index.qmd
            text: "A1 — Anfänger:innen"
          - href: kurs_a2/index.qmd
            text: "A2 — Grundlegende Kenntnisse"
          - href: kurs_b1/index.qmd
            text: "B1 — Selbstständig (untere Stufe)"
          - href: kurs_b2/index.qmd
            text: "B2 — Selbstständig (obere Stufe)"
          - href: kurs_c1/index.qmd
            text: "C1 — Kompetent"
    right:
      - icon: github
        href: https://github.com/<user>/<repo>
  page-navigation: true
  page-footer:
    left: "DaF · © S. Le Boulanger · MIT / CC-BY-SA 4.0"
    center: |
      [Start](/start.qmd) · [Übersicht](/uebersicht.qmd) ·
      [Goethe-Formate](/goethe_formate.qmd) ·
      [Lernstrategien](/anhaenge/lernstrategien.qmd) ·
      [Kompetenzbaum](/anhaenge/kompetenzbaum.qmd) ·
      [Glossar](/anhaenge/glossar.qmd) ·
      [Typische Fehler](/anhaenge/typische_fehler.qmd) ·
      [Bewertungsraster](/anhaenge/bewertungsraster.qmd) ·
      [Literatur](/literatur.qmd) ·
      [Danksagung](/danksagung.qmd) ·
      **[Impressum](/impressum.qmd)** ·
      **[Datenschutz](/datenschutz.qmd)**
    right: "Mit [Quarto](https://quarto.org) gebaut"

format:
  html:
    theme:
      light: [flatly, custom.scss]
      dark:  [darkly, custom.scss]
    css: styles.css
    toc: true
    toc-depth: 3
    toc-location: right
    link-external-newwindow: true
    include-in-header:
      - text: |
          <link rel="preconnect" href="https://fonts.googleapis.com">
          <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
          <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

editor: source
```

Alle Footer-Links MÜSSEN absolut sein (führender `/`).

# AUTORIN ÜBER METADATEN

In jedem `units/`-Ordner eines Kurses eine `_metadata.yml`
ausgeben:

```yaml
author: "S. Le Boulanger"
```

Quarto erbt das in jede `.qmd` des Ordners. Nie einzelne
Einheiten-Dateien anfassen, um die Autorin zu setzen.

# UNIT-FRONT-MATTER (jede Einheit, verbatim)

```yaml
---
title: "Einheit N — <Thema>"
subtitle: "GER-Stufe <A1|A2|B1|B2|C1> · Goethe-Zertifikat <A1|A2|B1|B2|C1>"
cefr_level: "<A1|A2|B1|B2|C1>"
unit_nr: <N>
slug: "<kebab-case-slug>"
cefr_can_do:
  - "<„Ich kann"-Deskriptor aus dem GER-Begleitband 2020>"
  - "<zweiter Deskriptor falls zutreffend>"
bw_inspiration: "<optional: passendes BW-Bildungsplan-Thema als Inspiration>"
skills_focus:
  - hoeren
  - lesen
  - sprechen
  - schreiben
  - sprachmittlung
  - sprachreflexion
goethe_module:
  - lesen
  - hoeren
  - schreiben
  - sprechen
format:
  html:
    toc: true
    toc-depth: 3
  revealjs:
    output-file: "unit<NN>_slides.html"
    theme: [default, ../../assets/slides.scss]
    slide-number: c/t
    progress: true
    scrollable: true
    transition: none
    preview-links: auto
---
```

Der Artikel wird nur als HTML gerendert. Der Foliensatz nur als
HTML. Die Prüfung nur als PDF, aus der separaten
`unit<NN>_<slug>_exam.qmd`-Wrapper-Datei.

Genau eine CEFR-Stufe pro Einheit. Einheiten gehören zu genau
einem Kurs-Ordner.

# UNIT-STRUKTUR (jede Einheit, verbatim)

1. `::: {.callout-note}`, der die Modellvariante nennt
   (Standard = Einstieg → Input → Üben → Anwenden → Reflexion;
   Prüfungsvariante = Aufgabe → Modell → Strategie → Versuch →
   Feedback) UND die GER-Stufe.
2. Aufruf des `{{< downloads >}}`-Shortcodes, um die vier
   Download-Links oben in der Einheit anzuzeigen.
3. `## Lernziele` — 3 „Ich kann"-Aussagen im CEFR-Stil (z. B.
   „Ich kann mich vorstellen und einfache Fragen zu meiner Person
   beantworten.").
4. `## GER-Ausrichtung` — Stichpunktliste mit den Deskriptoren aus
   dem Front Matter plus Verweis auf das entsprechende
   Goethe-Modul (Lesen / Hören / Schreiben / Sprechen), das diese
   Einheit adressiert.
5. `## Einstiegsgeschichte` — kurzer narrativer Aufhänger (80–250
   Wörter je nach Stufe), der die Figuren, den Ort oder die
   kulturelle Verankerung der Einheit einführt. Stufenangepasste
   Stimme.
6. `## 1. Einstieg` (oder Aufgabe) — Aufwärmen, Vorwissen
   aktivieren, Brainstorming oder Bildimpuls.
7. `## 2. Input` (oder Modell) — Zieltext (Lese-/Hörtranskript),
   Grammatikerklärung oder Musterbeispiel. Enthält den
   vollständigen Text oder das Transkript, original verfasst.
8. `## 3. Üben` (oder Strategie) — geführtes Üben: Lückentext,
   Zuordnung, Umformung, Fehlersuche, Substitution. Übungen UND
   Lösungen in einem `::: {.callout-tip collapse="true"}`-Block
   mit dem Titel „Lösungen".
9. `## 4. Anwenden` (oder Versuch) — freie Produktion:
   Sprechimpuls, Schreibaufgabe, Rollenspiel,
   Mini-Sprachmittlung. Enthält eine Mustelösung auf Zielniveau.
10. `## 5. Reflexion` (oder Feedback) — metakognitiver Abschluss,
    Selbsteinschätzungsliste, die an die Lernziele anknüpft.
11. `## Prüfungsbeispiel` — vollständige Goethe-Modellprüfungsaufgabe
    auf dem entsprechenden Niveau. Siehe Abschnitt
    GOETHE-MODELLPRÜFUNG unten. Dieser Abschnitt wird AUCH als
    eigenständiges PDF gerendert (siehe DOWNLOADS).
12. `## Downloads` — Callout-Block mit vier Links, gefüllt durch
    denselben `{{< downloads >}}`-Shortcode (Artikel HTML, Slides
    HTML, Arbeitsblatt PDF Platzhalter, Prüfungs-PDF).
13. `::: {.notes} ... :::` — Sprechernotizen nur für den
    Foliensatz: Zeitschätzung, Übergang, Binnendifferenzierungs-
    hinweise (stärkere/schwächere Lernende innerhalb der Stufe),
    Mikro-Check-Frage zum Verstehen.
14. `## Häufige Stolperfallen` — 2–4 Stichpunkte, auf typische
    Lernerfehler bezogen.
15. `## Weiterführende Materialien` — 1–3 authentische Ressourcen
    (Deutsche Welle „Nicos Weg", „Deutsch lernen" auf DW.com,
    Goethe-Institut kostenlose Übungen, Easy German auf YouTube
    mit Transkript, 3sat/ZDFkultur-Mediatheken für B2/C1, Langer
    Atem Podcast). Keine Paywall-Inhalte. Keine raubkopierten
    Lehrwerksscans.

Jede Einheit 150–350 Zeilen Prosa. Echter, original verfasster
Inhalt. Nicht aus Hueber, Cornelsen, Klett, Schubert, telc oder
Goethe-Modellsätzen paraphrasieren.

# FOLIENSATZ — VISUELLE ANFORDERUNGEN

Jeder Reveal.js-Output einer Einheit enthält:

- Eine **Titelfolie** mit Einheit-Name, GER-Stufen-Badge
  (A1–C1 farbig) und einem großen Lucide-Icon, das das Thema
  repräsentiert (z. B. `coffee` für eine Einheit „Im Café").
- Eine **Einstiegsfolie** mit der Einstiegsgeschichte in 30–50
  Wörtern plus einem großformatigen generischen Meme-SVG als
  Reaktion auf das Thema. Nutzung der `.meme-frame`-Klasse. Das
  Meme stammt aus den generischen Templates in `assets/memes/`
  (Drake, Distracted Boyfriend, Expanding Brain, Success Kid,
  Is This A Pigeon, Two Buttons, Change My Mind), als
  Original-SVG mit Rechtecken und einfachen Formen rekonstruiert
  — nie getracet oder aus den echten Memes heruntergeladen.
  Meme-Beschriftung als pädagogischer Witz.
- **Ikonenreiche Kompetenzfolien.** Pro Schritt des Fünfermodells
  eine Folie mit Schrittnamen, einem Lucide-Icon
  (`brain-circuit` für Einstieg, `book-open` für Input, `dumbbell`
  für Üben, `mic` für Anwenden, `compass` für Reflexion) und drei
  knappen Stichpunkten.
- **Wortschatz-/Grammatikfolien** in Zweispalten-Layout mit Icons
  flankierend zu den Zielitems.
- Eine **Zoom-Folie** für jeden authentischen Text: Reveals
  Zoom-Funktion (`r-stretch`-Klasse auf einem Block) nutzen,
  damit der Text den Bildschirm füllt.
- Eine **Prüfungsvorschau-Folie**, die die Struktur der
  Goethe-Aufgabe zeigt, mit der die Einheit schließt.
- **Abschlussfolie** mit den „Ich kann"-Zielen als vorzulesende
  Checkliste.

Sprechernotizen auf jeder Folie: Zeitschätzung, Übergang,
Differenzierung innerhalb der Stufe (schwächere/stärkere Lernende
auf derselben CEFR-Stufe), Mikro-Verständnisfrage.

# STUFENGERECHTE ERZÄHLWEISE PRO CEFR-STUFE

| Stufe | Stimme | Satzlänge | Humor | Figuren |
|-------|--------|-----------|-------|---------|
| A1    | Sehr konkret, Alltag, Präsens dominant | 5–8 Wörter | Visuell, harmlos | Alltagsensemble (z. B. **Ana**, **Luka**, **Frau Kurz**, **Herr Keks**) |
| A2    | Etwas breiter, Perfekt eingeführt | 7–12 Wörter | Situationskomik | Nachbar:innen + Alltagshelfer:innen |
| B1    | Realistisch, Arbeitswelt, Mobilität | 10–16 Wörter | Beobachtend, trocken | Mobile Erwachsene, Pendler:innen, Studierende |
| B2    | Argumentativ, Gesellschaft, Meinung | 15–22 Wörter | Ironisch, selbstreflexiv | Diskutierende Erwachsene, Journalist:innen |
| C1    | Analytisch, literarisch-essayistisch | 20–30+ Wörter | Zurückhaltend, literarisch | Textstimmen, Autor:innen als Charaktere |

Wiederkehrende Figuren pro Stufe (kleine benannte Besetzung).
Besetzung in der `index.qmd` des Kurses einführen und über die 12
Einheiten wiederverwenden.

**Kulturelle Vielfalt des deutschsprachigen Raums.** Auf allen
Stufen bewusst nicht nur Berlin/München zeigen. Ab A2 Figuren und
Kontexte aus Österreich (Wien, Graz), der Schweiz (Zürich, Bern,
viersprachige Schweiz), Südtirol, und den unterschiedlichen
Dialektregionen Deutschlands. Ab B1 auch Migrations- und
Diasporaperspektiven (deutschsprachige Rumänien-Banat,
Russlanddeutsche, türkisch-deutsche Stimmen, afrikanisch-deutsche
Autor:innen wie May Ayim). Einheitlich-berlinzentriertes DaF ist
eine Lücke, die diese Seite ausdrücklich schließt.

# GOETHE-MODELLPRÜFUNG — FORMAT

Pro Einheit eine **vollständig ausgearbeitete Goethe-Modellaufgabe**
auf der CEFR-Stufe des Kurses. Die Aufgabe orientiert sich streng
am Goethe-Prüfungsformat für die entsprechende Stufe, aber mit
**originalen Stimulustexten** (von der Autorin verfasst, nicht aus
echten Goethe-Prüfungen kopiert).

## Aufbau pro Prüfungsbeispiel

- Header mit CEFR-Stufe, Goethe-Modul (Lesen / Hören / Schreiben /
  Sprechen), Zeitvorgabe gemäß offiziellem Goethe-Format,
  erlaubten Hilfsmitteln.
- Aufgaben gemäß dem in `_resources/goethe_format_<stufe>.yml`
  gespeicherten Format (Anzahl Items, Aufgabentypen,
  Punktverteilung).
- Stimulusmaterial: originale kurze Texte, Transkripte (bei
  Hörverstehen als Volltext verfügbar, mit Hinweis, dass in der
  echten Prüfung nur Audio), Briefvorlagen/E-Mail-Impulse für
  Schreibaufgaben, Bildimpulse für Sprechaufgaben.
- **Erwartungshorizont** in einem eingeklappten Callout, in
  Zielsprache auf Zielniveau verfasst.
- **Bewertungsraster** mit den offiziellen Goethe-Kriterien pro
  Modul (z. B. für Schreiben: Aufgabenerfüllung, kommunikative
  Gestaltung, formale Richtigkeit).

## Pro Einheit nur EIN Modul vertieft

Eine Einheit prüft nicht alle vier Module gleichzeitig wie eine
echte Goethe-Prüfung, sondern fokussiert **das Modul, das den
Schwerpunkt der Einheit bildet** (im `skills_focus` markiert).
Über 12 Einheiten eines Kurses verteilt ergibt das eine
ausgewogene Abdeckung aller vier Module — mindestens 2 Einheiten
pro Modul pro Kurs. Die restlichen Einheiten können
Mischaufgaben sein (z. B. Lesen + Schreiben kombiniert), markiert
mit `exam_combined: true`.

## Quellenrestriktion für Prüfungsbeispiele

Alle Stimulustexte in Prüfungsbeispielen müssen original (von der
Autorin verfasst), gemeinfrei oder eindeutig unter
bildungsfreier Lizenz sein. Unter jedem Stimulus wird die Quelle
genannt. Nie urheberrechtlich geschützte Prüfungstexte aus
offiziellen Goethe-Modellsätzen, Schubert-/Hueber-/Cornelsen-
Prüfungstrainern oder kommerziellen Vorbereitungsbüchern
reproduzieren. Formal orientieren — inhaltlich original.

# DOWNLOADS — VIER LINKS PRO EINHEIT

Jede Einheit zeigt vier Links, präsentiert als prominente
Callout-Karte oben (unter dem Modellvariante-`callout-note`) UND
erneut unten in der `## Downloads`-Sektion. Gleiche vier Links an
beiden Stellen.

Zwei sind Live-Webseiten, zwei sind PDFs.

| Link | Format | Zeigt auf |
|------|--------|-----------|
| Artikel der Einheit | HTML | Die gerenderte Einheit-Seite selbst (Selbstlink). |
| Foliensatz | HTML | Der Reveal.js-Begleiter. |
| Arbeitsblatt | PDF | Handout für Lernende. **Platzhalter-PDF vorläufig.** |
| Prüfungsbeispiel | PDF | Goethe-Modellaufgabe als eigenständige PDF. |

## Dateinamenskonvention (strikt)

```
unit<NN>_<slug>.html                                    (Einheit-Artikel)
unit<NN>_slides.html                                    (Reveal.js)
downloads/<stufe>/unit<NN>_<slug>_worksheet.pdf         (Arbeitsblatt, Platzhalter)
downloads/<stufe>/unit<NN>_<slug>_exam.pdf              (Prüfungs-PDF)
```

Beispiel für Kurs B2, Einheit 3 „Meinungen in den Medien":
```
kurs_b2/units/unit03_meinungen_in_den_medien.html
kurs_b2/units/unit03_slides.html
downloads/b2/unit03_meinungen_in_den_medien_worksheet.pdf
downloads/b2/unit03_meinungen_in_den_medien_exam.pdf
```

## Erzeugung der Prüfungs-PDFs

Ein zweites `.qmd` liegt neben jeder Einheit:
`units/unit<NN>_<slug>_exam.qmd`. Ein dünner Wrapper, der mit
`{{< include >}}` nur den Prüfungsabschnitt (die
`## Prüfungsbeispiel`-Sektion plus Erwartungshorizont- und
Bewertungsraster-Callouts) aus der Einheit zieht. Sein Front
Matter setzt `format: pdf` allein. Eine Quelle der Wahrheit,
sauberes eigenständiges Prüfungs-PDF via Quarto + tinytex
während `quarto render`.

## Erzeugung der Arbeitsblatt-PDFs (Platzhalter-Strategie)

Arbeitsblattinhalte werden später verfasst. Vorerst pro Einheit
ein **einseitiges A4-Platzhalter-PDF** mit dem korrekten
kanonischen Dateinamen ausliefern. So funktionieren alle Links auf
der Live-Seite sofort; das spätere Ausfüllen mit echtem Inhalt
wird zu einem einfachen Datei-Ersatz, ohne Änderung am
Site-Code.

Platzhalter programmatisch mit einem kleinen Python-Skript
`_scripts/make_placeholder_worksheets.py` erzeugen:

```python
# Pseudocode — im Scaffold-Schritt ausformulieren.
# Für jede Einheit im Curriculum-Outline:
#   - stufe, unit_nr, slug berechnen
#   - einseitige A4-PDF erzeugen mit:
#       Kopfzeile:    „S. Le Boulanger · DaF"
#       Titel:        „Arbeitsblatt — Einheit {N}: {titel}"
#       Meta-Zeile:   „GER-Stufe {A1-C1} · Goethe-Zertifikat {A1-C1}"
#       Körper:       „Platzhalter — Arbeitsblattinhalt folgt."
#       Fußzeile:     „© S. Le Boulanger · CC-BY-SA 4.0"
#       Wasserzeichen: „S. Le Boulanger" diagonal 55°
#   - schreiben nach downloads/<stufe>/unit<NN>_<slug>_worksheet.pdf
```

`reportlab` oder `fpdf2` verwenden (in CI neben
pyyaml/pandas installieren). Das Skript liest dasselbe
Curriculum-Outline-YAML wie die thematische Karte, Dateinamen
sind also garantiert konsistent.

Wenn echte Arbeitsblätter existieren, einfach in denselben
kanonischen Pfad mit demselben Dateinamen ablegen. Keine
weiteren Änderungen nötig.

## `{{< downloads >}}`-Shortcode

Quarto-Lua-Shortcode in `_extensions/downloads/` implementieren,
der `cefr_level`, `unit_nr` und `slug` aus dem Front Matter liest
und vier Links ausgibt. Jede Einheit ruft `{{< downloads >}}`
zweimal auf — einmal oben, einmal in `## Downloads`.

Exakt dieses Markup ausgeben:

```markdown
::: {.callout-tip icon=false title="Downloads"}
- [📄 Artikel der Einheit](unit<NN>_<slug>.html)
- [🎞 Foliensatz](unit<NN>_slides.html)
- [📋 Arbeitsblatt (PDF)](/downloads/<stufe>/unit<NN>_<slug>_worksheet.pdf)
- [📝 Prüfungsbeispiel (PDF)](/downloads/<stufe>/unit<NN>_<slug>_exam.pdf)
:::
```

Artikel- und Slides-Links sind relativ (gleicher Ordner).
Arbeitsblatt- und Prüfungs-Links sind absolut ab Site-Wurzel.

## Build-Reihenfolge (CI)

1. `python _scripts/make_placeholder_worksheets.py` → schreibt 60
   Platzhalter-Arbeitsblatt-PDFs direkt nach
   `docs/downloads/<stufe>/`.
2. `quarto render` → erzeugt HTML-Site (Einheiten-Artikel +
   Foliensätze) UND jedes Prüfungs-PDF aus den
   `_exam.qmd`-Wrappern.
3. `_scripts/organise_downloads.sh` schiebt Prüfungs-PDFs nach
   `docs/downloads/<stufe>/` mit kanonischem Dateinamen.
4. `docs/` wird als Pages-Artefakt hochgeladen.

Kein decktape. Kein Chromium. Keine Artikel-PDFs.

## Umgang mit fehlenden PDFs

CI MUSS fehlschlagen, wenn ein erwartetes PDF fehlt:

```bash
EXAMS=$(find docs/downloads -name "*_exam.pdf" | wc -l)
WORKS=$(find docs/downloads -name "*_worksheet.pdf" | wc -l)
test "$EXAMS" -eq 60
test "$WORKS" -eq 60
```

# THEMENPLAN (vorschlagen-und-bestätigen)

Vor der Erstellung irgendeiner Einheit eine einzige große Tabelle
erzeugen, die pro Kurs (5 CEFR-Stufen) die 12 Einheiten-Titel, ihre
primäre Fertigkeit (hören/lesen/sprechen/schreiben/mediation),
ihre thematische Anker (Alltag/Beruf/Gesellschaft/Kultur/
Wissenschaft) und den geplanten Goethe-Modulfokus zeigt. Themen
progressiv zuordnen:

- **A1:** Begrüßung, Name/Herkunft, Familie, Wohnen, Essen,
  Einkaufen, Zeit, Wochenplan, Wetter, Körper/Gesundheit, Beruf
  (einfach), Reisen (Grundbegriffe).
- **A2:** Arbeitssuche, Wohnung mieten, Arzt/Behörden, Reisen
  (konkreter), Hobbys, Feste/Traditionen, Vergangenheit erzählen,
  Pläne machen, Medien (Fernsehen, Radio), Umwelt (einfach),
  Freundschaft, Familiengeschichte.
- **B1:** Arbeitsleben, Bildung, Mobilität, Gesundheitssystem,
  digitale Kommunikation, Umweltthemen, interkulturelle
  Begegnung, Stadt vs. Land, Konsum, Politik (Grundbegriffe),
  persönliche Beziehungen, Zukunftsvisionen.
- **B2:** Medienlandschaft, Wissenschaftskommunikation,
  gesellschaftliche Debatten, Arbeitswelt im Wandel, Kunst und
  Kultur, Migrationsdiskurs, Gesundheitspolitik, Umweltpolitik,
  Bildungsdebatten, Ethik digitaler Technologien, Ökonomie für
  Laien, literarische Perspektiven.
- **C1:** Literatur und literarisches Argumentieren, politische
  Diskursanalyse, Wissenschaftstheorie, Ästhetik,
  Identitätsdiskurse, postkoloniale Perspektiven im
  deutschsprachigen Raum, Historiografie, Philosophie für
  informierte Laien, Fachsprachen (Wirtschaft, Medizin, Recht —
  je ein Beispiel), Stilistik und Rhetorik, literarische
  Moderne, Gegenwartsliteratur.

AUF mein OK WARTEN, bevor Einheiten generiert werden.

# STARTSEITE (`index.qmd`)

Hero-Block mit Kicker (mono, Akzent: „DaF · GER A1–C1"), H1
„Deutsch als Fremdsprache — von A1 bis C1", Lead-Absatz signiert
S. Le Boulanger. Dann:

- *Was diese Seite ist* (~120 Wörter).
- *Für wen diese Seite ist* (~100 Wörter) — Lehrende im Ausland,
  Selbstlernende, DaF-Studierende in Ausbildung.
- *Die fünf GER-Stufen* — Kartenraster mit 5 Karten (A1, A2, B1,
  B2, C1) je Kurs, inklusive Goethe-Zertifikat-Entsprechung.
- *Das fünfstufige Modell* (~100 Wörter) mit inline-Lucide-Icons.
- *Eine Quelle, zwei Formate* (~80 Wörter).
- *Goethe-Prüfungsvorbereitung* (~80 Wörter), die klarmacht, dass
  pro Einheit **ein originales** Goethe-Format-Beispiel geliefert
  wird.
- *Schwesternsites* — kurzer Abschnitt, der die verwandten
  EFL- und FLE-Sites derselben Autorin erwähnt, mit Links.
- *Mehr dazu* — Stichpunktliste mit Links (Start, Goethe-Formate,
  Übersicht, Anhänge, Literatur, Danksagung).

Keine Danksagung inline — auf die volle Seite verlinken.

# KURS-LANDING-PAGE (`kurs_<stufe>/index.qmd`)

- Kicker: „GER-STUFE <A1|A2|B1|B2|C1> · GOETHE-ZERTIFIKAT <...>"
  in Mono/Akzent.
- H1: „<Stufe> Deutsch — <eine Einzeiler-Figurenbeschreibung>".
- Einführung der wiederkehrenden Besetzung (die benannten Figuren
  dieser Stufe) mit je einem Lucide-Icon.
- Kartenraster der 12 Einheiten dieses Kurses, mit Einheit-Nummer,
  Titel, Fertigkeitsfokus und CEFR-Badge.
- Ein kurzer Block „Was Sie am Ende dieser Stufe können werden",
  der die CEFR-Can-Do-Aussagen des Referenzrahmens paraphrasiert
  und mit dem Goethe-Zertifikatsziel verknüpft.
- Link zur `uebersicht.qmd` dieses Kurses.

# GOETHE-FORMATE-SEITE (`goethe_formate.qmd`)

- Übersicht aller fünf Goethe-Prüfungsformate (A1, A2, B1, B2, C1)
  mit Modulaufschlüsselung (Lesen/Hören/Schreiben/Sprechen),
  Zeitvorgaben, Punktverteilung.
- Tabellen pro Stufe, aus `_resources/goethe_format_*.yml`
  generiert.
- Direkte Deep-Links zu den Einheiten, die jedes Modul primär
  adressieren (aus `skills_focus` und `goethe_module` der Unit-
  Front-Matter abgeleitet).

Diese Seite wird **aus den YAML-Ressourcen generiert**, nicht von
Hand geschrieben. Ein kleiner Helper-`.qmd` liest die YAMLs und
rendert eine Tabelle via Python-Chunk mit `yaml` und `pandas`
(via `jupyter: python3`). Abhängigkeiten in CI installieren.

# ANHÄNGE (vom Footer verlinkt)

- `lernstrategien.qmd` — Mermaid-Flussdiagramm + Prosa
  (Bedarfsanalyse → Zielsetzung → Einheitenauswahl → Arbeit mit
  Einheit → Selbsttest → Goethe-Prüfungstermin oder nächste
  Stufe).
- `kompetenzbaum.qmd` — Mermaid-Baum: Start beim
  Fertigkeitsbedarf (Hören / Lesen / Sprechen / Schreiben /
  Sprachmittlung / Sprachreflexion / interkulturelle Kompetenz),
  Blätter verlinken direkt auf Einheiten aller fünf Stufen.
- `glossar.qmd` — DaF-Fachbegriffe (Scaffolding, CLIL, GER,
  Deskriptor, rezeptiv vs. produktiv, Sprachmittlung, i+1,
  Pair-Work) und Goethe-spezifische Begriffe (Modul,
  Bewertungsraster, Teilkompetenz, Kursstufe, Prüfungszentrum),
  alphabetisch, Erstnennung verlinkt mit der Einheit, die den
  Begriff einführt.
- `typische_fehler.qmd` — Lernerfehler pro Stufe, organisiert
  nach typischen L1-Hintergründen:
  - Englischsprachige: falsche Freunde (become/bekommen,
    gift/Gift), Artikelzuweisung, Verbzweit-Stellung,
    Wortschatz-Kongruenz.
  - Romanische Sprachen (FR/ES/IT): Artikelgeschlecht,
    Adjektivdeklination, Wortstellung in Haupt- und
    Nebensätzen.
  - Slawische Sprachen: Artikelsystem (v. a. Englisch-/
    Deutsch-Artikel vs. artikellose slawische Sprachen),
    Perfekt/Präteritum-Unterscheidung, Präpositionen.
  - Arabischsprachige: Verbstellung, feminine/maskuline
    Artikel, Plural.
  - Chinesisch/Japanisch: Konjugation, Deklination,
    Artikel überhaupt.
  Mit Korrekturstrategien pro CEFR-Stufe.
- `bewertungsraster.qmd` — Vollständige Goethe-Bewertungsraster
  pro Stufe und Modul (Schreiben: Aufgabenerfüllung +
  kommunikative Gestaltung + formale Richtigkeit; Sprechen:
  Erfüllung der Aufgabenstellung + kohärenz + Wortschatz +
  Strukturen + Aussprache). Aus öffentlichen Goethe-
  Bewertungskriterien rekonstruiert, mit Quellenangabe zu
  `goethe.de`.

# DANKSAGUNGSSEITE

Eigene `danksagung.qmd`, geordnet:

1. **Didaktik und Pädagogik** — *Teach-the-Teacher*-Quellen (GER
   Begleitband 2020 / Companion Volume, Hans Barkowski und Hans-
   Jürgen Krumm für DaF-Grundlagen, Franz Januschek für
   Fehlerlinguistik, Gerhard Neuner für interkulturelle
   Landeskunde, Karin Aguado für Sprachlernforschung, Rolf
   Koeppel für Phonetik).
2. **Inhaltliche Tiefe** — authentische Textquellen (Deutsche
   Welle, Goethe-Institut freie Ressourcen, Deutschlandfunk,
   BR-Mediathek, 3sat, Project Gutenberg für Literatur,
   Zeno.org, Deutsches Textarchiv der BBAW).
3. **Werkzeuge** — Quarto, Pandoc, Reveal.js, Lucide-Icons,
   Source Sans 3 und JetBrains Mono.
4. **Strukturelle Inspiration** — am Ende.
5. **Persönlich** — Kolleg:innen und Lernende (generisch; keine
   Namen, wenn nicht angegeben).
6. **Lizenz** — MIT für Code; CC-BY-SA 4.0 für Lehrinhalt.

Jeder Eintrag verlinkt auf eine echte URL. Keine generischen
Name-Drops.

# IMPRESSUMSSEITE (`impressum.qmd`)

Deutsches Recht (TMG § 5, seit 2024 DDG § 5) verlangt ein
rechtskonformes Impressum auf jeder Website, die nicht rein
privat ist. Das Curriculum-Site einer Lehrenden gilt als
„geschäftsmäßig" — das Impressum ist also **verpflichtend**,
nicht optional. DSGVO verlangt zusätzlich eine separate
Datenschutzerklärung.

## `impressum.qmd`-Struktur (verbatim Skelett)

Seite mit Platzhalter-Feldern erstellen, die die Autorin
VOR dem Livegang ausfüllen MUSS. Jeder Platzhalter ist in
einem sichtbaren `::: {.callout-warning}`-Block mit dem Titel
„ACHTUNG — AUSFÜLLEN VOR LIVEGANG" eingerahmt, damit nichts mit
einem `<TODO>`-String live geht.

```markdown
---
title: "Impressum"
---

## Angaben gemäß § 5 DDG

**S. Le Boulanger**
<TODO: Anschrift — Straße, Hausnummer>
<TODO: PLZ, Ort>
Deutschland

## Kontakt

E-Mail: <TODO: kontakt@domain.tld>

## Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV

S. Le Boulanger
<TODO: gleiche Anschrift wie oben>

## Haftungsausschluss

**Haftung für Inhalte.** Als Diensteanbieterin bin ich gemäß § 7
Abs. 1 DDG für eigene Inhalte auf diesen Seiten nach den
allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 DDG bin ich
als Diensteanbieterin jedoch nicht verpflichtet, übermittelte
oder gespeicherte fremde Informationen zu überwachen oder nach
Umständen zu forschen, die auf eine rechtswidrige Tätigkeit
hinweisen.

**Haftung für Links.** Diese Website enthält Links zu externen
Websites Dritter, auf deren Inhalte ich keinen Einfluss habe. Für
die Inhalte der verlinkten Seiten ist stets der jeweilige
Anbieter oder Betreiber der Seiten verantwortlich.

## Urheberrecht

Die durch S. Le Boulanger erstellten Inhalte und Werke auf diesen
Seiten unterliegen dem deutschen Urheberrecht. Der Lehrinhalt
(Texte, Aufgaben, Prüfungsbeispiele) steht unter der Lizenz
**CC-BY-SA 4.0**. Der zugrundeliegende Website-Code steht unter
der **MIT-Lizenz**. Zitate Dritter bleiben Eigentum der jeweiligen
Rechteinhaber.

## Hinweis zum Goethe-Format

Die auf dieser Seite bereitgestellten Prüfungsbeispiele orientieren
sich formal an den öffentlich dokumentierten Prüfungsformaten der
Goethe-Zertifikate A1–C1. Sie sind eigene didaktische Adaptionen
der Autorin und stehen in keinem offiziellen Zusammenhang mit dem
Goethe-Institut e. V. Das Goethe-Institut ist nicht an der
Erstellung dieser Materialien beteiligt und zeichnet sie nicht
verantwortlich.
```

## `datenschutz.qmd`-Struktur (verbatim Skelett)

GitHub Pages wird von GitHub Inc. in den USA gehostet; Besucher-
IPs werden dort verarbeitet. Das muss offengelegt werden.

```markdown
---
title: "Datenschutzerklärung"
---

## Verantwortliche Stelle

S. Le Boulanger
<TODO: Anschrift>
E-Mail: <TODO>

## Hosting bei GitHub Pages

Diese Website wird auf GitHub Pages gehostet, einem Dienst der
GitHub Inc., 88 Colin P Kelly Jr St, San Francisco, CA 94107,
USA. Beim Aufruf der Seiten überträgt Ihr Browser technisch
notwendige Daten (IP-Adresse, Datum, Zeit, User-Agent, angefragte
URL) an GitHub. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO
(berechtigtes Interesse an zuverlässiger Auslieferung der
Inhalte). GitHubs Datenschutzerklärung:
<https://docs.github.com/site-policy/privacy-policies/github-privacy-statement>.

## Keine Cookies, kein Tracking

Diese Website setzt keine Cookies, verwendet keine Analyse-Tools
und bindet keine Drittanbieter-Schriftarten, -Videos oder
-Social-Media-Widgets ein. Google Fonts werden vom Browser der
Nutzer geladen, jedoch vom eigenen Repository/CDN ausgeliefert.

## Ihre Rechte

Sie haben nach DSGVO das Recht auf Auskunft, Berichtigung,
Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit
und Widerspruch. Ansprechpartnerin: siehe oben.

## Beschwerderecht

Sie haben das Recht, sich bei einer Aufsichtsbehörde zu
beschweren. Zuständig ist die
Landesbeauftragte für den Datenschutz und die
Informationsfreiheit Baden-Württemberg (LfDI BW).
```

**Die Autorin muss beide Dateien vor dem Livegang von einer
Datenschutz-beauftragten oder einem/einer Jurist:in prüfen
lassen.** Das Scaffold liefert das Skelett; es stellt keine
Rechtsberatung dar.

# PDF-ATTRIBUTION — NAME DER AUTORIN AUF JEDEM DOWNLOAD

Jedes von der Seite produzierte PDF (60 Prüfungs-PDFs + 60
Arbeitsblatt-PDFs) muss „S. Le Boulanger" sowohl als Metadatum
ALS AUCH als sichtbares Wasserzeichen oder Fußzeile tragen. Das
ist nicht verhandelbar: PDFs wandern vom Site weg und müssen die
Autorin auf der Vorderseite ausweisen.

## Prüfungs-PDFs (Quarto + LaTeX)

Attribution in `_includes/_exam.tex` implementieren (der
LaTeX-Header, den jede `unit<NN>_<slug>_exam.qmd`-Wrapper zieht):

```latex
% --- Dokument-Metadaten ---
\usepackage{hyperref}
\hypersetup{
  pdftitle={Prüfungsbeispiel},
  pdfauthor={S. Le Boulanger},
  pdfsubject={DaF — Goethe-Modellprüfung},
  pdfkeywords={DaF, Deutsch als Fremdsprache, Goethe-Zertifikat, GER, CEFR}
}

% --- Fußzeile auf jeder Seite ---
\usepackage{fancyhdr}
\usepackage{lastpage}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[L]{\small © S. Le Boulanger · DaF}
\fancyfoot[C]{\small \thepage\ / \pageref{LastPage}}
\fancyfoot[R]{\small CC-BY-SA 4.0}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0.3pt}

% --- Diagonales Wasserzeichen auf jeder Seite ---
\usepackage{draftwatermark}
\SetWatermarkText{S. Le Boulanger}
\SetWatermarkScale{0.6}
\SetWatermarkLightness{0.92}
\SetWatermarkAngle{55}
```

Tinytex benötigt eventuell Installation von `draftwatermark`;
falls es in CI fehlschlägt, Fallback auf `background`-Paket oder
einfachen `\AddToShipoutPictureBG`-Block mit `\rotatebox{55}{...}`
— das Skript versucht drei Strategien in Reihenfolge und scheitert
laut, wenn alle drei scheitern.

## Arbeitsblatt-PDFs (reportlab)

`_scripts/make_placeholder_worksheets.py` aktualisieren, auf jeder
Platzhalterseite zu rendern:

- **Kopfzeile** (oben links, 9 pt): `„S. Le Boulanger · DaF"`.
- **Titelblock**: Einheit-Titel + CEFR-Chip.
- **Körper**: „Platzhalter — Arbeitsblattinhalt folgt."
- **Fußzeile** (unten zentriert, 8 pt):
  `„© S. Le Boulanger · CC-BY-SA 4.0 · GER-Stufe {A1-C1} · Einheit {N}"`.
- **Diagonales Wasserzeichen** (zentriert, 55° Rotation, 48 pt,
  92 % grau): `„S. Le Boulanger"`.
- PDF-Metadaten via `canvas.setAuthor("S. Le Boulanger")`,
  `setTitle(...)`, `setSubject("DaF — Arbeitsblatt")`.

Wenn echte Arbeitsblätter die Platzhalter später ersetzen, müssen
dieselben Kopf/Fuß/Wasserzeichen erscheinen. Ein wiederverwendbarer
reportlab-Helper `_scripts/pdf_attribution.py`, der
`apply_attribution(canvas, context)` exportiert, damit
Arbeitsblatt-Generator:innen den gleichen Treatment ohne
Code-Duplikation einstecken können.

## Audit-Gate in CI

Nach der PDF-Erzeugung einen Verifikationsschritt hinzufügen:

```bash
# Jedes PDF muss S. Le Boulanger als Autor in Metadaten ausweisen.
python -c "
import sys, pathlib
from pypdf import PdfReader
bad = []
pdfs = list(pathlib.Path('docs/downloads').rglob('*.pdf'))
for p in pdfs:
    r = PdfReader(str(p))
    author = (r.metadata or {}).get('/Author', '')
    if 'Le Boulanger' not in author:
        bad.append(str(p))
if bad:
    print('ATTRIBUTION FEHLT:', *bad, sep='\n')
    sys.exit(1)
print(f'Alle {len(pdfs)} PDFs mit Autorin ausgewiesen.')
"
```

`pypdf` neben `reportlab` im CI-pip-Schritt installieren. Schlägt
dieser Check fehl, wird nicht deployt.

# CI (`.github/workflows/publish.yml`)

Offizielle GitHub-Pages-Actions verwenden, NICHT
`peaceiris/actions-gh-pages`. Pages-Quelle muss im Repo auf
„GitHub Actions" gesetzt sein. Kein R. Python nur für den
kleinen Goethe-Formate-Rendering-Helper und den Platzhalter-
Arbeitsblatt-Generator.

```yaml
name: Rendern und deployen
on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: quarto-dev/quarto-actions/setup@v2
        with:
          tinytex: true
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install pyyaml pandas jupyter reportlab pypdf
      - uses: actions/cache@v4
        with:
          path: _freeze
          key: ${{ runner.os }}-quarto-freeze-${{ hashFiles('**/*.qmd') }}
          restore-keys: ${{ runner.os }}-quarto-freeze-
      - name: Platzhalter-Arbeitsblatt-PDFs erzeugen
        run: python _scripts/make_placeholder_worksheets.py
      - name: Site rendern (HTML-Einheiten + Reveal.js-Slides + Prüfungs-PDFs)
        run: quarto render
      - name: Prüfungs-PDFs in kanonische Pfade schieben
        run: bash _scripts/organise_downloads.sh
      - name: Verifizieren, dass alle PDFs vorhanden sind
        run: |
          EXAMS=$(find docs/downloads -name "*_exam.pdf" | wc -l)
          WORKS=$(find docs/downloads -name "*_worksheet.pdf" | wc -l)
          echo "Prüfungs-PDFs: $EXAMS (erwartet 60)"
          echo "Arbeitsblatt-PDFs: $WORKS (erwartet 60)"
          test "$EXAMS" -eq 60
          test "$WORKS" -eq 60
      - name: Verifizieren, dass jedes PDF S. Le Boulanger ausweist
        run: |
          python -c "
          import sys, pathlib
          from pypdf import PdfReader
          bad = []
          pdfs = list(pathlib.Path('docs/downloads').rglob('*.pdf'))
          for p in pdfs:
              r = PdfReader(str(p))
              author = (r.metadata or {}).get('/Author', '')
              if 'Le Boulanger' not in author:
                  bad.append(str(p))
          if bad:
              print('ATTRIBUTION FEHLT:', *bad, sep='\n')
              sys.exit(1)
          print(f'Alle {len(pdfs)} PDFs mit Autorin ausgewiesen.')
          "
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: docs
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

# STRATEGIE ZUR INHALTSGENERIERUNG — SCHRITTWEISE, INKREMENTELL, WIEDERAUFNEHMBAR

Dieses Curriculum umfasst 60 Einheiten × 300 Zeilen ≈ 18 000
Zeilen origineller pädagogischer Prosa. Ein Ein-Pass-Versuch wird
scheitern: Kontext überläuft, Qualität degradiert in
Kursmitte, Fehler kumulieren lautlos und ein einziger
Render-Fehlschlag kostet Stunden.

Site in **sieben streng geordneten Phasen** generieren. Jede Phase
produziert einen committbaren Meilenstein. Nach jeder Phase
stoppen, validieren, committen bevor fortgefahren wird. Eine
Mensch kann an jeder Phasengrenze wieder einsteigen, ohne Arbeit
zu verlieren.

## Phase 0 — Vorflug (eine Session, ~15 Min)

**Ziel:** Umfang bestätigen, autoritative Quellen holen,
Konventionen festziehen.

1. Drei Kontextfragen stellen: (a) genaue GitHub-Org/Repo/User,
   (b) Bestätigung der wiederkehrenden Figurenbesetzung pro Stufe
   oder Erlaubnis zum Erfinden, (c) Bestätigung, dass MIT (Code)
   + CC-BY-SA 4.0 (Inhalt) als Lizenzierung akzeptabel sind.
   Antworten abwarten.
2. Für jede CEFR-Stufe das offizielle Goethe-Prüfungsformat von
   `goethe.de` abrufen und in
   `_resources/goethe_format_<stufe>.yml` parsen: Anzahl
   Aufgaben pro Modul, Aufgabentypen, Zeiten, Punktverteilung,
   Bewertungskriterien. Schlägt ein Abruf fehl: STOP und melden.
   Nichts erfinden.
3. Den GER-Begleitband 2020 (Can-Do-Deskriptoren) als Referenz
   vermerken. Die Deskriptoren selbst werden pro Einheit zitiert;
   nicht alle im Voraus ablegen, sondern bei der Themenplan-Phase
   pro Einheit auswählen.
4. Commit: `chore(preflight): Goethe-Formate erfasst`.

**Ausstiegskriterium:** 5 YAML-Dateien existieren, jede nicht
leer, jede verweist auf eine live im File-Header zitierte URL.

## Phase 1 — Scaffold (eine Session, ~30 Min)

**Ziel:** eine deploybare leere Site.

1. Top-Level-Scaffold ausgeben (Configs, Styles, CI, Extensions,
   Scripts).
2. Die 5 leeren Kursordner mit Stub-`index.qmd`, `uebersicht.qmd`
   und `units/_metadata.yml` ausgeben.
3. Die 5 Anhänge als Stubs (Titel + ein `TODO`-Absatz) ausgeben.
4. Die Top-Level-Seiten (`index.qmd`, `ueber.qmd`, `start.qmd`,
   `uebersicht.qmd`, `literatur.qmd`, `danksagung.qmd`,
   `goethe_formate.qmd`, `impressum.qmd`, `datenschutz.qmd`) mit
   echtem Inhalt ausgeben, da sie nicht von Einheit-Outputs
   abhängen. Impressum und Datenschutzerklärung mit expliziten
   `<TODO>`-Platzhaltern in sichtbaren
   `::: {.callout-warning title="ACHTUNG — AUSFÜLLEN VOR LIVEGANG"}`-
   Blöcken.
5. `quarto render` lokal laufen lassen. Fehler beheben. Pushen.
   Bestätigen, dass GitHub-Pages-Deploy mit dem leeren Gerüst
   funktioniert.
6. Commit: `feat(scaffold): deploybares leeres Gerüst`.

**Ausstiegskriterium:** Live-URL löst auf; Navigation
funktioniert; Hell/Dunkel-Toggle funktioniert; keine 404s in
der Navigation.

## Phase 2 — Themenplan (eine Session, ~45 Min)

**Ziel:** die volle 5×12-Karte der Einheit-Titel und
Can-Do-Anker.

1. Ein konsolidiertes YAML in `_resources/curriculum_outline.yml`
   erzeugen, das für jeden der 5 Kurse alle 12 Einheiten listet
   mit:
   - `unit_nr`, `slug`, `title`
   - `skills_focus` (aus den sechs DaF-Fertigkeiten)
   - `cefr_can_do` (verbatim GER-Begleitband-Deskriptoren)
   - `bw_inspiration` (optional; passendes Bildungsplan-Thema)
   - `goethe_module` (welches der vier Module diese Einheit
     vertieft)
   - `exam_combined` (true wenn Mischaufgaben)
   - `theme_arc_position` (1 von 12, für Progression)
2. Dieses YAML in eine große Tabelle rendern und präsentieren.
   **Mein OK abwarten.** Laut meinem Feedback iterieren.
3. Commit: `feat(outline): 60-Einheit-Curriculum-Karte
   genehmigt`.

**Ausstiegskriterium:** Outline-YAML existiert, Nutzer:in hat
genehmigt, jedes Goethe-Modul wird pro Kurs mindestens zweimal
primär adressiert (Abdeckungsprüfung), und jede Stufe hat
mindestens 10 von 12 Einheiten mit eindeutigem Schwerpunktmodul
(die 2 übrigen dürfen `exam_combined: true` sein).

## Phase 3 — Einen Kurs End-to-End prototypen (eine Session, ~2 h)

**Ziel:** das Einheit-Modell entrisiken vor Skalierung.

1. EINEN Kurs als Prototyp wählen: **B1**. Diese Stufe liegt in
   der Kurvenmitte — nicht Anfängerinnen-A1, nicht
   Hochniveau-C1 — und offenbart die meisten strukturellen
   Probleme. B1 ist außerdem die Stufe mit der höchsten
   Goethe-Prüfungsfrequenz weltweit, also am prägendsten für
   Qualität.
2. Alle 12 Einheiten UND 12 Prüfungs-Wrapper dieses einzigen
   Kurses in Folge schreiben, eine Einheit pro Modelltrain. Noch
   nicht parallelisieren.
3. `python _scripts/make_placeholder_worksheets.py` nur für
   diesen Kurs laufen lassen (ein `--course kurs_b1`-Flag zum
   Skript hinzufügen).
4. Lokal rendern. Bestätigen:
   - Alle 12 Einheit-Artikel als HTML gerendert.
   - Alle 12 Reveal.js-Slides gerendert.
   - Alle 12 Prüfungs-PDFs gerendert, Wasserzeichen sichtbar.
   - Alle 12 Platzhalter-Arbeitsblatt-PDFs existieren und sind
     ausgewiesen.
   - Der `{{< downloads >}}`-Shortcode produziert funktionierende
     Links an beiden Positionen auf jeder Einheit.
   - Das GER-Can-Do-Feld passt zum GER-Begleitband.
   - Das Goethe-Format jeder Prüfungsaufgabe passt zum
     `goethe_format_b1.yml`.
5. Commit: `feat(b1): Prototyp-Kurs komplett`.

**Ausstiegskriterium:** 48 Dateien deploybar; Mensch hat
mindestens drei Einheiten gesichtet und der Inhalt passt zur
Prompt-Absicht.

## Phase 4 — Parallele Ausbreitung auf Kurse (Multi-Session)

**Ziel:** die verbleibenden 4 Kurse, 48 Einheiten.

**Ein Subagent pro Kurs** starten. Jeder Subagent erhält:

- Das genehmigte Curriculum-Outline für seinen Kurs.
- Das `goethe_format_<stufe>.yml` des Kurses.
- Den Prototyp-Kurs (B1) als kanonisches Beispiel.
- Den vollständigen Instruktionsblock (Modell, Front Matter,
  Downloads, Erzählstimme für seine Stufe, Prüfungsformat,
  deutschsprachige Vielfalt).
- Explizite Verbote (keine Paraphrase von Lehrwerken, keine
  erfundenen Goethe-Aufgabentypen, kein R, keine
  urheberrechtlich geschützten Bilder, kein Berlin/München-
  Monopol).

**Batching.** Nicht alle 4 auf einmal starten. In Zweier-Batches:

- **Batch A:** A1, A2. (Beide Anfängerstufen — teilen massives
  Scaffolding-Bedarf, profitieren von paralleler Bearbeitung.)
- **Batch B:** B2, C1. (Beide Fortgeschrittenstufen — teilen
  komplexere Textanforderungen.)

Nach jedem Batch committen, rendern, Zählungen verifizieren,
systemische Probleme beheben vor dem nächsten Batch.

**Fehlerhandling.** Produziert ein Subagent weniger als 12
Einheiten oder scheitert eine Einheit an der Validierung (Front
Matter fehlt, Goethe-Format-Missmatch, Render-Fehler), NUR diesen
einen Kurs erneut abspielen und dem Subagent die Liste fehlender
oder defekter Einheiten geben. Nie einen ganzen Batch wegen eines
Teilausfalls erneut abspielen.

**Wiederaufnahme.** Ein `_resources/generation_log.yml` nach
jedem fertigen Kurs aktualisieren, mit `course_id`,
`units_written`, `units_verified`, `commit_sha`. Ein erneuter
Lauf liest diese Datei und überspringt bereits fertige Kurse.

**Ausstiegskriterium:** 60 Einheit-`.qmd`-Dateien, 60
Prüfungs-Wrapper-Dateien, vollständiger Render passt durch CI mit
allen PDFs vorhanden und ausgewiesen (120 PDFs gesamt).

## Phase 5 — Übergreifendes Politur (eine Session, ~1 h)

**Ziel:** Dinge, die nur nach Existenz aller Einheiten geprüft
werden können.

1. **Glossar-Erstnennung-Links.** Jede Einheit durchgehen,
   Erstnennung jedes Glossarbegriffs identifizieren,
   Anker-Links zurück zu `glossar.qmd` einfügen.
2. **Kompetenzbaum-Blätter.** Den Mermaid-Baum in
   `anhaenge/kompetenzbaum.qmd` mit direkten Links zu den
   Einheiten bestücken, die jede Fertigkeit-pro-Stufe-Zelle am
   besten exemplifizieren.
3. **Übersichts-Seite.** `uebersicht.qmd` aus dem Curriculum-
   Outline-YAML neu generieren — eine einzige sortierbare Tabelle
   aller 60 Einheiten mit Stufe, Einheit-Nummer, Titel,
   Fertigkeiten, Goethe-Modulfokus, Prüfungskombination, Deep-
   Link.
4. **Goethe-Modul-Abdeckungsmatrix.** Überprüfen, dass jedes
   der vier Module pro Kurs mindestens zweimal primär adressiert
   wird. Lücken melden.
5. **Wiederkehrende Figurenkonsistenz.** Pro Stufe bestätigen,
   dass die benannte Besetzung in ≥ 4 Einheiten auftaucht.
   Lücken melden.
6. **Deutschsprachige Vielfalt.** Pro Kurs bestätigen, dass
   mindestens 25 % der Einheiten ihren Kontext außerhalb
   Deutschlands (Österreich/Schweiz/Südtirol) oder in
   diasporischen/migrantischen Stimmen verankern. Zu
   Berlin-/München-lastige Kurse melden.
7. Commit: `feat(politur): übergreifende Links + Konsistenz`.

**Ausstiegskriterium:** Abdeckungsmatrix zeigt 100 %; keine
kaputten internen Links; Übersichts-Seite rendert; Vielfalts-
balance erfüllt.

## Phase 6 — Finales Rendering, Deploy, Übergabe (eine Session, ~30 Min)

1. CI komplett lokal laufen lassen, wenn möglich (`act` oder
   sauberes venv).
2. Pushen. Actions beobachten. Nur-CI-Fehler beheben (häufig
   LaTeX-Enkodierungsprobleme bei Umlauten in ungewöhnlichen
   Kontexten — eckige Anführungszeichen, deutsche Anführungen „",
   scharfes ß in Flussdiagrammen).
3. 10 zufällig ausgewählte Einheit-URLs besuchen und bestätigen:
   - Alle vier Download-Links lösen auf.
   - Foliensatz öffnet sich.
   - Prüfungs-PDF öffnet sich, sauber, Wasserzeichen sichtbar.
   - Arbeitsblatt-PDF öffnet sich (Platzhalter OK), ausgewiesen.
4. Ein HANDOVER.md erstellen mit:
   - Dateizahl pro Stufe
   - Goethe-Modul-Abdeckungsmatrix
   - Verteilung deutschsprachiger Herkunft (Prozent je Region)
   - Liste zu ersetzender Platzhalter-Arbeitsblätter
   - jegliche nicht gemappten Can-Do-Deskriptoren
   - **RECHTLICH — Impressum-Adresse + Kontakt ausfüllen,
     Datenschutzerklärung von Datenschutz-beauftragter oder
     Jurist:in prüfen lassen VOR öffentlichem Livegang**
   - nächste Schritte für Autorin (echte Arbeitsblatt-Inhalte,
     echtes Autorinnen-Foto, Korrekturdurchgang pro Kurs)
5. Commit: `docs(uebergabe): Generierung abgeschlossen`.

**Ausstiegskriterium:** Live-Site hat alle 60 Einheiten
funktionierend, CI ist grün, HANDOVER.md existiert.

## Operative Prinzipien durch alle Phasen

- **Ein Commit pro sinnvollem Meilenstein.** Scaffold-Änderungen
  nie mit Inhaltsänderungen mischen. Der Git-Log liest sich wie
  ein Kursplan.
- **Nie stillschweigend überspringen.** Kann eine Einheit nicht
  geschrieben werden (Goethe-Format-Daten fehlen, Outline-
  Eintrag mehrdeutig), die `.qmd` mit einem sichtbaren
  `::: {.callout-important}`-TODO-Block schreiben und im
  `generation_log.yml` eintragen. Nicht eine leere Datei
  produzieren und weitermachen.
- **Freeze bewahren.** Quartos `_freeze/`-Verzeichnis über
  Phasen erhalten — unveränderte Einheiten erneut rendern kostet
  Stunden.
- **Kein Heldentum.** Benötigt eine einzelne Einheit mehr als
  einen Modell-Train zum guten Schreiben, stoppen und nachfragen.
  Eine schlechte Einheit kostet mehr als eine pausierte Session.
- **Die Stimme der Autorin zuerst.** S. Le Boulanger ist die
  einzige Autorin — der drei Schwesternsites EFL, FLE und DaF.
  Jede Einheit soll sich lesen wie von derselben Lehrenden
  geschrieben. Keine stilistische Drift zwischen Subagents — die
  Prototyp-Einheit (B1) ist die Stilreferenz.
- **Deutschsprachige Vielfalt als Dauerverpflichtung.** Jeder
  Subagent muss die geografische/kulturelle Verankerung seiner
  12 Einheiten vor Abgabe prüfen. Berlin-Monopol = Ablehnung
  und Neufassung.

# AUSFÜHRUNGSREIHENFOLGE

Die sieben in **STRATEGIE ZUR INHALTSGENERIERUNG** oben
definierten Phasen in Reihenfolge befolgen, ohne Phasengrenzen zu
überspringen. Jede Phase endet mit einem Commit und einer
Validierungsprüfung. Phase N+1 nicht beginnen, solange das
Ausstiegskriterium der Phase N nicht erfüllt ist.

Schnell-Index:

- **Phase 0 — Vorflug:** Kontextfragen, Goethe-Formate-Abruf.
- **Phase 1 — Scaffold:** deploybares leeres Gerüst.
- **Phase 2 — Outline:** 5×12-Einheit-Karte, nutzergenehmigt.
- **Phase 3 — Prototyp:** B1 End-to-End als Stilreferenz.
- **Phase 4 — Ausbreitung:** 4 verbleibende Kurse in Batches von 2.
- **Phase 5 — Politur:** Glossar-Links, Abdeckungsmatrix,
  Übersicht, deutschsprachige Vielfalt.
- **Phase 6 — Übergabe:** finales Rendering, Deploy, HANDOVER.md.

# HARTER STOPP

Keine Goethe-Formate paraphrasieren, umschreiben oder erfinden.
Kann eine Goethe-Quelle nicht abgerufen werden: stoppen und
melden. Keine urheberrechtlich geschützten Memes, Fotos oder
Lehrwerksinhalte verwenden. Kein Goethe-Institut-Logo verwenden
— auch wenn das Format zitiert wird. Kein
`peaceiris/actions-gh-pages` verwenden. Nicht committen ohne
vorheriges lokales `quarto render`, falls verfügbar. Keinen Pull
Request erstellen, außer ausdrücklich angefragt. Keinen R-Code
oder R-angrenzendes Tooling hinzufügen — dies ist eine
nicht-codeunterstützte Curriculum-Site. Berlin-/München-Monopol
nicht dulden: der deutschsprachige Raum ist Deutschland +
Österreich + Schweiz + Südtirol + diasporische Stimmen.
