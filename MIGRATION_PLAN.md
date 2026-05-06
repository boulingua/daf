# DaF — Quarto → Hugo (Coder) Migration Plan

**Status:** Phase 0 (orientation, read-only) complete. Awaiting approval to enter Phase 1.
**Branch when work begins:** `migration/hugo-coder` (not yet created).
**Reference site studied:** `github.com/boulingua/website` (Hugo + Coder, modules-based).

---

## 1. Repo identity (auto-detected)

| Field | Value |
|---|---|
| Site title | `DaF — S. Le Boulanger` |
| Description | DaF curriculum A1–C1, 60 units, GER-Modellprüfung per unit |
| Site URL | `https://boulingua.github.io/daf/` |
| Repo URL | `https://github.com/boulingua/daf` |
| Default branch | `main` |
| Content language | `de` (single-language site) |
| Output dir (current) | `docs/` (Quarto convention; will become `public/` under Hugo) |
| Author | `S. Le Boulanger` |
| Licence | MIT (code) / CC-BY-SA 4.0 (content) |

---

## 2. Inventory summary

### 2.1 Content files

| Category | Count | Path pattern |
|---|---:|---|
| Top-level pages | 11 | `index.qmd`, `start.qmd`, `ueber.qmd`, `formate.qmd`, `uebersicht.qmd`, `literatur.qmd`, `danksagung.qmd`, `impressum.qmd`, `datenschutz.qmd`, `haftungsausschluss.qmd` (+ `kurs_a1/uebersicht.qmd` etc.) |
| Course landing pages | 4 | `kurs_a2/index.qmd`, `kurs_b1/index.qmd`, `kurs_b2/index.qmd`, `kurs_c1/index.qmd` (no `kurs_a1/index.qmd` — see risks) |
| Course Übersicht stubs | 5 | `kurs_<level>/uebersicht.qmd` |
| Unit articles | 60 | `kurs_<level>/units/unit<NN>_<slug>.qmd` |
| Unit exam wrappers (PDF only) | 60 | `kurs_<level>/units/unit<NN>_<slug>_exam.qmd` |
| Appendix pages | 5 | `anhaenge/*.qmd` |
| **Total .qmd** | **~145** | |

### 2.2 Static assets

- `assets/_shared.scss`, `assets/dark.scss`, `assets/light.scss`, `assets/slides.scss` — Quarto SCSS (replaced by Hugo Coder + custom.css).
- `custom.scss`, `styles.css` at root — global tweaks.
- `_includes/_exam.tex` — LaTeX header for exam PDFs.
- `_resources/format_<a1..c1>.yml`, `curriculum_outline.yml`, `generation_log.yml` — authoritative YAML for curriculum + format specs.
- `_scripts/vgwort.lua` — Pandoc Lua filter that injects VG Wort pixel from frontmatter `vgwort_pixel` (currently no qmd file sets the key — see §6).
- `_scripts/generate_uebersicht.py`, `_scripts/make_placeholder_worksheets.py`, `_scripts/pdf_attribution.py`, `_scripts/organise_downloads.sh` — build-time helpers.
- `scripts/check-legal-placeholders.sh` — CI guard.
- **No image assets in repo.** All current pages are pure text.

### 2.3 Quarto-specific constructs in use

| Construct | Count / examples | Notes |
|---|---|---|
| Callouts (`::: {.callout-note/tip/warning/important/caution}`) | 221 occurrences across 128 files | Highest-volume conversion. |
| Generic fenced divs (`::: {.hero-block}`, `.card-grid`, `.card`, `.cefr-badge`, `.notes`, `.lead`, `.hero-kicker`) | ~50 across landing pages | Mapped to plain HTML wrappers under Hugo. |
| `::: {.callout-tip collapse="true" title="Lösungen"}` | many | Becomes `<details><summary>` in Hugo. |
| `{{< downloads >}}` shortcode | every unit `.qmd`, twice | **Custom shortcode is referenced but NOT defined in this repo** — see §6 risk #1. |
| Reveal.js slide format (`format.revealjs`) | 60 unit qmds | Currently produces `unit<NN>_slides.html` per unit. **Strategy: drop Reveal.js entirely; the `.pptx` placeholder under "Materials → Presentations" replaces it.** Confirm in Phase 1 that this is acceptable — it loses an existing render path, but the Phase-3 Materials hub is the explicit successor. |
| PDF format (`format.pdf`) — exam wrappers | 60 `_exam.qmd` files | Hugo cannot render LaTeX → PDF. **Strategy: keep the rendered exam PDFs as static assets under `static/downloads/<level>/`. Do not re-render in Hugo CI; treat them as content artefacts. Discard the `_exam.qmd` source files OR keep them in a `quarto-exams/` legacy folder if you want PDF regeneration later. Recommend keeping them — see §3 mapping.** |
| Tables (markdown pipe tables) | many | Pass through unchanged. |
| Frontmatter custom keys (`cefr_level`, `unit_nr`, `slug`, `cefr_can_do`, `skills_focus`, `pruefungs_module`) | 60 unit qmds | Survive verbatim — Hugo accepts arbitrary frontmatter; we use them in templates. |
| Cross-refs (`@sec-…`, `@fig-…`) | none found | n/a. |
| Includes (`{{< include … >}}`) | none | n/a. |
| Parameterised pages | none | n/a. |
| Executable code (`{r}` / `{python}` cells) | none | n/a. Site is pure prose. |

### 2.4 Tracking integrations

- **Plausible Analytics** — `_quarto.yml` lines 78–84, `data-domain="boulingua.github.io/daf"`, src `https://analytics.hellebo.de/js/script.file-downloads.outbound-links.js`. Self-hosted on `analytics.hellebo.de` (DE-server). Identical pattern to reference site's `layouts/_partials/head/extensions.html`.
- **VG Wort Zählpixel** — Lua filter `_scripts/vgwort.lua` reads `vgwort_pixel` from per-page frontmatter. **Grep for `vgwort_pixel`/`vgwort-pixel` across all `.qmd` returns ZERO matches.** No tokens are currently in use. Migration porting is therefore *infrastructural*, not data-preserving — Phase 4's "manifest of pixels per article" is empty. The Hugo equivalent must still be ready for the moment tokens are added. **Confirmed: there is nothing to round-trip.** A `vgwort-manifest.csv` will be created with header only, and the CI verification script will pass-through when empty.

### 2.5 Current CI

`.github/workflows/publish.yml` — single workflow:
1. Quarto + tinytex setup.
2. Python 3.11 + pyyaml/pandas/jupyter/reportlab/pypdf.
3. `_freeze` cache.
4. `<TODO>` gate on impressum/datenschutz.
5. `quarto render`.
6. `bash _scripts/organise_downloads.sh` (move exam PDFs into `docs/downloads/<level>/`).
7. `python _scripts/make_placeholder_worksheets.py`.
8. PDF count gate (60 exam + 60 worksheet, only enforced at full content).
9. pypdf attribution gate (every PDF must list `S. Le Boulanger` as `/Author`).
10. GitHub Pages deploy.

---

## 3. Mapping table (Quarto → Hugo)

| Quarto construct | Hugo equivalent | Implementation notes |
|---|---|---|
| `_quarto.yml` `project.type: website` | `hugo.toml` | TOML, mirror reference site's structure. |
| `output-dir: docs` | `publishDir: public` (Hugo default) | Switch GitHub Pages source to `gh-pages` artefact (Pages action) — matches reference repo. |
| `website.title` / `description` | `title`, `[params].description` | direct. |
| `website.navbar.left/right` (with submenus) | `[[menu.main]]` entries | Coder default does **not** render submenus (the reference site's menu is flat). Two options: (a) flatten the navbar (one entry per GER-level), (b) override `layouts/partials/header.html` to support nested menus. **Recommend (b)** — keeps the existing IA. |
| `website.page-footer` | Coder footer params + `customCSS` | Reproduce footer link list via a custom partial or `layouts/partials/footer.html` override. |
| `format.html.theme` (flatly/darkly + scss) | Coder's auto colour scheme + `assets/css/custom.css` | Mirror reference site's `colorScheme = "auto"`. |
| `format.html.toc-location: right` | Coder has no built-in right-rail TOC | Add a small TOC partial (or use Coder's default top-of-page TOC). Acceptable visual change. |
| `format.html.include-in-header` (Plausible + Google Fonts) | `layouts/partials/head/extensions.html` | Copy verbatim, change `data-domain` to `boulingua.github.io/daf`. |
| Quarto callouts `::: {.callout-note}` | Custom shortcode `{{< callout type="note" >}}…{{< /callout >}}` | Build one shortcode covering note/tip/warning/important/caution. CSS must match Quarto's visual closely enough to be unsurprising. |
| Collapsible callout `::: {.callout-tip collapse="true" title="Lösungen"}` | `<details><summary>` shortcode `{{< details title="Lösungen" >}}` | Most `Lösungen` blocks use this — high-frequency. |
| `::: {.hero-block}` / `.lead` / `.card-grid` / `.card` / `.cefr-badge` / `.hero-kicker` | Plain HTML divs (raw passthrough; `unsafe=true` already needed) + CSS rules in `assets/css/custom.css` | Cleanest path. Goldmark `markup.goldmark.renderer.unsafe = true`. |
| `{{< downloads >}}` (custom, **undefined**) | New Hugo shortcode `layouts/shortcodes/downloads.html` | Reads frontmatter `cefr_level` + `unit_nr` + `slug`, emits links to `/downloads/<level>/unit<NN>_<slug>_exam.pdf` and `…_worksheet.pdf`. **Behavioural fix relative to current Quarto state — see risks.** |
| `format.revealjs` (per-unit slide deck) | Drop. The Phase-3 Materials hub `.pptx` placeholder supersedes it. | Remove the `revealjs` block from each unit's frontmatter. Drop `assets/slides.scss`. |
| `format.pdf` exam wrappers | Move pre-rendered PDFs to `static/downloads/<level>/` and treat as content artefacts. | Quarto-rendered exam PDFs are already on the live site under that path. Pull them into the repo as static (or download them as part of a one-time build), then **delete the `_exam.qmd` files**. Hugo CI cannot rebuild them. **Decision needed in Phase 1** — see risks. |
| `_includes/_exam.tex` | Discarded with the PDF render path | Keep on disk under `legacy/_exam.tex` if you want to re-render later via Quarto manually. |
| `_scripts/vgwort.lua` | Hugo partial `layouts/partials/vgwort-pixel.html` | Reads `.Params.vgwort_pixel`, emits the same `<img …>` (URL-build logic ported one-to-one). Included once near `</body>` in `layouts/_default/single.html` (or a baseof override). |
| Plausible (already covered) | `layouts/partials/head/extensions.html` | Same partial slot the reference site uses — keeps boulingua repos uniform. |
| `filters: [_scripts/vgwort.lua]` | n/a — partial replaces it | drop. |
| Pandoc auto-IDs on headings | Hugo Goldmark auto-IDs | identical for ASCII; verify for German `ä/ö/ü/ß` — Goldmark uses GitHub-style anchors which differ from Pandoc on Umlaute. **Internal-link audit in Phase 4 will catch any mismatches.** |
| `_resources/*.yml` | `data/*.yml` | Read via `site.Data` in templates. The `uebersicht.qmd` regen script becomes a Hugo template that loops over `site.Data.curriculum_outline`. |
| Cross-references like `[…](kurs_a1/units/unit01_…qmd)` | Plain `[…](/kurs_a1/units/unit01_…/)` | Mass rewrite: `.qmd` → `/` (trailing slash) at link-time conversion. |

---

## 4. Navigation plan (Hugo `[[menu.main]]`)

Flat menu does not match the current Quarto IA (which has two submenus: "GER-Stufen" and "Rechtliches"). We override Coder's header partial to support `parent` chaining. New menu:

```toml
[[menu.main]]  weight = 1   name = "Start"        url = "/"
[[menu.main]]  weight = 2   name = "Über"         url = "/ueber/"
[[menu.main]]  weight = 3   name = "Prüfungsformate" url = "/formate/"
[[menu.main]]  weight = 4   name = "Übersicht"    url = "/uebersicht/"

[[menu.main]]  weight = 5   name = "GER-Stufen"
[[menu.main]]  weight = 51  parent = "GER-Stufen"  name = "A1 — Anfänger:innen"             url = "/kurs_a1/"
[[menu.main]]  weight = 52  parent = "GER-Stufen"  name = "A2 — Grundlegende Kenntnisse"    url = "/kurs_a2/"
[[menu.main]]  weight = 53  parent = "GER-Stufen"  name = "B1 — Selbstständig (untere)"     url = "/kurs_b1/"
[[menu.main]]  weight = 54  parent = "GER-Stufen"  name = "B2 — Selbstständig (obere)"      url = "/kurs_b2/"
[[menu.main]]  weight = 55  parent = "GER-Stufen"  name = "C1 — Kompetent"                  url = "/kurs_c1/"

[[menu.main]]  weight = 6   name = "Materialien"                                              # NEW (Phase 3)
[[menu.main]]  weight = 61  parent = "Materialien" name = "Foliensätze"     url = "/materials/presentations/"
[[menu.main]]  weight = 62  parent = "Materialien" name = "Arbeitsblätter"  url = "/materials/worksheets/"

[[menu.main]]  weight = 9   name = "Rechtliches"
[[menu.main]]  weight = 91  parent = "Rechtliches" name = "Impressum"               url = "/impressum/"
[[menu.main]]  weight = 92  parent = "Rechtliches" name = "Datenschutzerklärung"    url = "/datenschutz/"
[[menu.main]]  weight = 93  parent = "Rechtliches" name = "Haftungsausschluss"      url = "/haftungsausschluss/"
```

GitHub icon goes via `[[params.social]]`.

---

## 5. File-by-file migration order (Phase 2)

Batches of ~10 files per commit, low-risk first to surface conversion issues early:

1. **Batch 1 (5 files)** — appendix stubs: `anhaenge/{glossar,kompetenzbaum,lernstrategien,typische_fehler,bewertungsraster}.qmd`. Mostly empty/stub.
2. **Batch 2 (8 files)** — top-level pages: `start`, `ueber`, `formate`, `literatur`, `danksagung`, `impressum`, `datenschutz`, `haftungsausschluss`.
3. **Batch 3 (1 file)** — `index.qmd` (uses hero-block, card-grid — first real test of div wrappers + custom CSS).
4. **Batch 4 (1 file)** — `uebersicht.qmd` (auto-generated table; switch to Hugo template using `site.Data.curriculum_outline`).
5. **Batch 5 (4 files)** — course landing pages (`kurs_<a2..c1>/index.qmd`).
6. **Batch 6 (5 files)** — course Übersicht stubs.
7. **Batches 7–18** — unit articles, 60 files in 6 batches of ~10, level by level (A1 → C1). Each batch = one commit.
8. **Batch 19** — handle exam wrappers: per the Phase-1 decision, either delete or move to `legacy/`.

After every batch, run `hugo --minify`. Word-count diff per file → flag in this doc under §7 if >2% drift.

---

## 6. Risks & required decisions

### Risk 1 — `{{< downloads >}}` shortcode is not defined in this repo
Every unit `.qmd` calls `{{< downloads >}}` twice, but no shortcode definition exists in the codebase. Either:
- (a) The current Quarto build silently no-ops it, OR
- (b) The current published site shows broken render markers, OR
- (c) The shortcode is defined in an `_extensions/` directory that exists on the deployed site but was never committed.

**Action in Phase 1:** check the live site `https://boulingua.github.io/daf/kurs_a1/units/unit01_begruessung-und-name.html` for what it renders. The Hugo replacement shortcode (§3) implements the *intended* behaviour (link to exam + worksheet PDFs by frontmatter convention) — this is **structurally required** under the migration prompt's rules and is therefore allowed.

### Risk 2 — Reveal.js per-unit decks are dropped
Current `_quarto.yml` builds a Reveal.js HTML deck per unit (`unit<NN>_slides.html`). Phase 3 introduces a `.pptx` placeholder per unit for the Materials hub. The two coexist conceptually but only one is the migration target. **Recommendation: drop the Reveal.js render path entirely.** The Materials-hub `.pptx` is the canonical "presentation" artefact going forward.

**Decision needed:** confirm OK to drop `unit<NN>_slides.html` URLs (will need redirects → 301 to `/materials/presentations/<slug>/`).

### Risk 3 — Exam PDFs cannot be re-rendered by Hugo
Hugo has no LaTeX path. Three ways forward:
- (a) Pull the 60 already-rendered PDFs from the live site as a one-time download into `static/downloads/<level>/`, delete `_exam.qmd`, treat as static.
- (b) Keep `_exam.qmd` files in a parallel `quarto-exams/` directory and document a manual `quarto render quarto-exams` step.
- (c) Migrate exam content to plain Hugo Markdown pages (no PDF), and produce PDFs on demand later.

**Recommendation: (a).** Matches the prompt's rule "every word of student-facing content must survive". The PDFs already on the live site are the canonical artefact. Recommend skipping (b) — it's a hybrid, the prompt forbids hybrids ("Quarto is removed at the end").

**Decision needed.**

### Risk 4 — VG Wort manifest is empty
No `.qmd` currently sets `vgwort_pixel`. The migration prompt's "vgwort-manifest.csv" gate becomes a no-op. **Action:** create the manifest header-only, port the Lua filter to a Hugo partial, and add the CI verification step that simply passes when manifest is empty. This is documented behaviour, not a hidden gap.

### Risk 5 — `kurs_a1/index.qmd` is missing
A1 has `kurs_a1/uebersicht.qmd` and units, but no `index.qmd`. Other levels have both. Decide: create one, or make `kurs_a1/uebersicht.md` the section index (`_index.md`). **Recommendation: make `kurs_<level>/_index.md` the section landing page everywhere — fold `index.qmd` + `uebersicht.qmd` into one page per level.** This simplifies the menu and mirrors Hugo idiom. Word-count preserved by concatenation.

**Decision needed.**

### Risk 6 — Goldmark anchor IDs differ for German Umlaute
Pandoc's `slug` for `## Häufige Stolperfallen` is `häufige-stolperfallen`; Goldmark may produce `h-ufige-stolperfallen` (transliteration policy varies). Any internal `[link](#...)` to a heading with Umlauts could break. **Action:** in Phase 2, after each batch, grep migrated content for in-page anchor links and verify against rendered IDs. Phase 4's lychee step is the final gate.

### Risk 7 — Materials hub thumbnails on Windows CI
The migration prompt suggests `libreoffice --headless` or `pdf2image` to generate thumbnails. Linux GitHub Actions runner handles both; Windows local dev does not. **Action:** thumbnail generation is a CI-only step; document a `--skip-thumbs` mode for local dev.

### Risk 8 — Footer "Schwesternsites" link drift
Footer references `boulingua.github.io/ressources/` (singular Latinised), but `_quarto.yml` and `index.qmd` use `ressources` while the migration prompt names the repo `ressourcen`. Confirm canonical URL before reproducing in Hugo footer. **Decision needed.**

---

## 7. Manual review needed (populated during Phase 2)

*(empty — every file ported at 0% word-count drift after the
converter's `:::` markers / shortcode tokens were excluded from
both sides of the diff. No file flagged.)*

---

## 8. Tracking inventory (per Phase 0 §"CRITICAL")

### Plausible script (verbatim from `_quarto.yml` line 83):

```html
<script defer data-domain="boulingua.github.io/daf" src="https://analytics.hellebo.de/js/script.file-downloads.outbound-links.js"></script>
<script>window.plausible = window.plausible || function() { (window.plausible.q = window.plausible.q || []).push(arguments) }</script>
```

Plus Google Fonts preconnect (lines 80–82). All four lines port verbatim into `layouts/partials/head/extensions.html`, identical to the reference site's pattern (only `data-domain` differs).

### VG Wort Zählpixel manifest

Empty. `grep -r 'vgwort_pixel\|vgwort-pixel' . --include='*.qmd'` → no matches. The Lua filter exists but no per-page tokens have been added yet. `vgwort-manifest.csv` will be created header-only in Phase 1 and the CI verification step passes trivially when empty.

---

## 9. Phase log

### 2026-05-06 — Phase 4 complete (cleanup + parity)
- Quarto removed: `_quarto.yml`, all 145 `.qmd` files, `_includes/`,
  `_resources/`, `_scripts/`, `.quarto/`, four Quarto SCSS files at
  `assets/`, root-level `custom.scss` + `styles.css`,
  `scripts/check-legal-placeholders.sh`, and the disabled
  `publish.yml.disabled` workflow.
- Path inconsistency caught and fixed: the `{{< downloads >}}`
  shortcode now points the worksheet link at
  `/materials/worksheets/unit<NN>_<slug>.pdf` (the Phase-3
  placeholder location); the exam link still points at
  `/downloads/<level>/unit<NN>_<slug>_exam.pdf` to match the live
  site URL.
- 60 exam PDFs pulled from the live site into `static/downloads/`
  via `_scripts_migration/pull_exam_pdfs.py`. 2.2 MB total.
- 158 Hugo aliases injected (top-level pages, anhaenge, course
  landings — `index.html` + `uebersicht.html` per level — and per
  unit: `unit<NN>_<slug>.html` + `unit<NN>_slides.html`).
- Parity result: **145 / 147** old sitemap URLs resolve on the new
  build. The remaining two — `HANDOVER.html` and `LEGAL.html` —
  are repository internal docs that should never have shipped to
  the public site; intentional drop, not a regression.
- Internal link audit: **1,966 / 1,966** clean. Hugo
  `--printPathWarnings` clean. 0 broken links.
- Final build: 86 canonical pages, 158 aliases, 307 static files
  (240 materials + 60 exams + 7 theme), 0 errors.

### 2026-05-06 — Phase 2 complete (content port)
- 7 commits across the 19-batch plan: anhaenge (5), top-level (8),
  index (1), uebersicht (1), course landings folded into _index.md
  (5), 60 unit articles in five level commits, plus a follow-up
  commit renaming the unit `slug` frontmatter key to `unit_slug`
  so URL parity with the Quarto site holds.
- 81 markdown files under `content/`. 0% word-count drift on
  every file (after stripping `:::` fences and shortcode tokens
  from both sides of the diff).
- Hugo build clean: 94 pages, 13 aliases, no errors.
- Decisions taken on the four open questions from §10:
  Reveal.js dropped, exam PDFs deferred to Phase 4 (option a:
  pull live PDFs as static), kurs_a1/index.qmd does exist (Phase
  0 was wrong; folded uniformly), Schwesternsite URL kept as
  `ressources` (matches `_quarto.yml`).
- Quarto sources still in place; deletion happens in Phase 4.
- Batch 19 (exam wrappers): not converted — they're LaTeX-only
  source for PDF render and have no role in Hugo. They stay on
  disk and get removed in Phase 4 when the Quarto setup goes.

### 2026-05-06 — Phase 0 complete
- Inventoried repo: 145 `.qmd` files, ~15k lines of original German pedagogical content, no images, 4 SCSS files, 1 Lua filter, 1 LaTeX header.
- Identified 8 risks and 4 explicit decisions required before Phase 1.
- Reference-site clone studied at `C:\Users\raban\AppData\Local\Temp\boulingua-reference`. Hugo 0.147.0, Coder via Hugo Modules (`github.com/luizdepra/hugo-coder`), Plausible in `layouts/_partials/head/extensions.html`, `markup.goldmark.renderer.unsafe = true`, accent `#1a73e8`.
- VG Wort: zero pixels in use; migration is infrastructural only.
- Awaiting decisions on risks 2, 3, 5, 8 before scaffolding.

---

## 10. Decisions still open (please answer before Phase 1)

1. **Reveal.js slide decks** — OK to drop entirely and replace with Materials-hub `.pptx` placeholders? (Adds ~60 redirect entries.)
2. **Exam PDFs** — option (a) pull rendered PDFs from live site as one-time static, or (c) migrate exam content to MD with no PDF for now?
3. **`kurs_a1/index.qmd` missing** — fold `index` + `uebersicht` into a single `_index.md` per level, applied uniformly to all five levels?
4. **Schwesternsite URL for Ressourcen** — `ressources` (current) or `ressourcen` (per migration prompt)? Need confirmation before footer wiring.
