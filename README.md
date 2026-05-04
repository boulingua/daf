# DaF — Deutsch als Fremdsprache (Goethe-Formate, A1–C1)

Ein Kurscurriculum für **Deutsch als Fremdsprache** entlang des
Gemeinsamen Europäischen Referenzrahmens (GER / CEFR), mit
Goethe-Modellprüfungen pro Einheit. Fünf GER-Stufen **A1, A2, B1,
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
- Goethe-Modellprüfungsaufgabe pro Einheit als eigenständiges PDF.
- Platzhalter-Arbeitsblatt-PDF pro Einheit (echte Inhalte folgen).
- Hell/Dunkel-Toggle. Lucide-Icons. Keine urheberrechtlich
  geschützten Medien.

Deploy via **GitHub Actions** (`actions/deploy-pages@v4`).

## Pädagogisches Modell

Fünfstufig (mit deutscher Terminologie):
**Einstieg → Input → Üben → Anwenden → Reflexion**.

Bei Prüfungsvorbereitungs-Einheiten:
**Aufgabe → Modell → Strategie → Versuch → Feedback**.

## Goethe-Prüfungsformate

Pro GER-Stufe wird das offizielle Goethe-Prüfungsformat
(verbatim aus Goethe-Institut-Publikationen) im Ordner
`_resources/goethe_format_<stufe>.yml` dokumentiert. Diese YAML-
Dateien sind die autoritative Quelle für Aufgabentyp, Itemzahl,
Zeitvorgaben, Punkteverteilung und Bewertungskriterien jeder
Prüfungssimulation auf der Site.

| Stufe | Zertifikat                    | Prüfung             | Bestehensgrenze |
|-------|-------------------------------|---------------------|-----------------|
| A1    | Start Deutsch 1               | ca. 80 Min, 100 P.  | 60 P. (60 %)    |
| A2    | Goethe-Zertifikat A2          | 105 Min, 100 P.     | 60 P. (60 %)    |
| B1    | Zertifikat B1 (modular)       | je Modul 100 P.     | 60 P. pro Modul |
| B2    | Goethe-Zertifikat B2 (modular)| je Modul 100 P.     | 60 P. pro Modul |
| C1    | Goethe-Zertifikat C1 (modular)| je Modul 100 P.     | 60 P. pro Modul |

**Keine** Reproduktion echter Goethe-Modellsatz-Texte. Alle
Stimulustexte original von S. Le Boulanger verfasst, formal am
Goethe-Format orientiert.

## Lizenz

Zweiteiliger Lizenzsplit:

- **MIT** (`LICENSE`) — Website-Code (Quarto-Konfig, Lua-Shortcodes,
  Python-Helfer, SCSS).
- **CC-BY-SA 4.0** (`LICENSE-content`) — didaktische und
  kuratorische Inhalte (Einheiten, Prüfungsbeispiele,
  Lernziele).

`© S. Le Boulanger · MIT / CC-BY-SA 4.0` auf jedem Footer und
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
