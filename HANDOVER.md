# DAF — Handover: conformance audit & roadmap

Audit of `boulingua/daf` against its two governing targets, with a phased,
file-specific roadmap to bring it into conformance.

- **Target 1 — pagegen** (`/pagegen`): the structural / benchmark template every
  boulingua course follows (layout, content model, design system, gates, legal).
- **Target 2 — curriculum** (`/curriculum`): the CEFR descriptor-ID and
  conformance standard (`{LEVEL}.{DOMAIN}.{SCALE}.{SEQ}`, conformance levels,
  machine-readable scope manifest).

Audit date: 2026-07-22. Repo state: 60 units (12 × A1/A2/B1/B2/C1), 60 exam PDFs,
68 registered VG Wort marks, materials + audio committed.

---

## 1. Executive summary

DaF is a **mature, content-complete** course that predates the template and was
built on the Quarto→Hugo migration path. It is **already ahead of pagegen** in
several operational respects (Pagefind search, a materials-network graph with a
JS-budget gate, pa11y accessibility gate, PDF-metadata attribution, 774 committed
audio files). It has **already adopted the current VG Wort partial architecture**
(`vgwort/url.html` resolver + `head`/`body` extensions) and has 68 live marks.

Where it diverges is **structural conformance to the template** and **curriculum
descriptor-ID traceability** — the two things this handover exists to close.

**The 5 biggest gaps, in priority order:**

1. **Content model** — units are single files (`content/kurs_XX/units/unitNN_slug.md`),
   not leaf bundles; there are **no first-class exam HTML pages** (exams are
   PDF-only downloads). Template requires `unitNN-slug/index.md` bundles + sibling
   `-exam/` bundles.
2. **Front-matter schema** — DaF uses the *old* fork (top-level `cefr_level`,
   `cefr_can_do`, German `skills_focus` values, `unit_slug`, no `page_type`, no
   `curriculum:` block). Template mandates the superset schema with a polymorphic
   `curriculum:` block and a `page_type` discriminator.
3. **Curriculum conformance = 0** — DaF references **no** curriculum descriptor
   IDs anywhere. `cefr_can_do` are free-text German "Ich kann…" strings. No
   `conformance.yml`, no scope/coverage manifest, does not participate in
   `id-audit.sh`. This is the single largest curriculum gap.
4. **Design-system / landing shortcodes** — section `_index.md` pages use **raw
   HTML** (`<div class="hero-kicker">`, `<div class="card-grid">`). Template
   requires the shortcode set (`hero`, `kicker`, `lead`, `card`, `card-grid`),
   which DaF does **not** ship (only `callout`, `details`, `downloads`).
5. **Config drift** — `hugo.toml` lacks `[taxonomies]`, `params.code`,
   `params.license`; accent colour is **hardcoded in `custom.css`** rather than
   selected from `data/accents.yaml` by `code` (the daf accent `#1D87A7` *is*
   already in the shared registry, so this is a wiring fix, not a design change).

**Overall effort:** ~**M–L**. The mechanical config/shortcode alignment is small.
The content-model migration (60 units → bundles) and exam-page creation (60 new
pages) are the bulk. Curriculum ID mapping (60 units × ~3–5 can-dos ≈ 200–300
statements → descriptor IDs) is the intellectually heaviest but is
front-matter-only. No content rewriting is required — only restructuring,
re-keying, and mapping.

---

## 2. Audit — template (pagegen) conformance

| Dimension | CURRENT (daf) | TARGET (pagegen) | GAP |
|---|---|---|---|
| **Repo layout** | `content/kurs_a1…c1/`, `content/anhaenge/`, stray `kurs_*/units/_metadata.yml` (Quarto leftovers), `recovery/`, `_materials/`, `_scripts` merged into `scripts/` | `content/<course>/units/<bundle>/`, `content/appendices/`, `archetypes/`, `i18n/` | Rename/relayout; delete Quarto `_metadata.yml`; add `archetypes/`, `i18n/en.yaml` equivalent |
| **hugo.toml** | No `[taxonomies]`; no `params.code`; no `params.license`; menu uses `kurs_*` URLs; Plausible block correctly last | Declared `[taxonomies]` (tag/skill/level/topic); `params.code="daf"`; `params.license="CC BY-SA 4.0"` | Add the three keys + taxonomy declarations |
| **go.mod** | `module …/daf`, hugo-coder pinned identically | same pin | ✅ conformant |
| **Content model** | 60 **single-file** units; 12/level; PDF-only exams | leaf **bundles** `unitNN-slug/index.md` + sibling `…-exam/index.md` | Convert 60 units → bundles; create 60 exam bundles |
| **Front-matter** | `cefr_level`, `cefr_can_do`, `skills_focus:[lesen,sprechen]`, `pruefungs_module`, `unit_slug`, `aliases`; **no** `page_type`, **no** `curriculum:` block | superset schema: `page_type`, English `skills_focus` enum, polymorphic `curriculum:{framework:cefr,…}` | Rewrite front matter of all 60 units + new exams |
| **Design system** | Accent **hardcoded** in `assets/css/custom.css` (`#1D87A7`) | accent from `data/accents.yaml` keyed by `params.code` | Wire `code`; delete hardcoded hex; add `data/accents.yaml` (or vendor the shared one) |
| **Shortcodes** | `callout`, `details`, `downloads` only | + `hero`, `kicker`, `lead`, `card`, `card-grid` | Add 5 shortcodes; convert raw-HTML landings |
| **Section landings** | `_index.md` use raw `<div>` HTML | shortcode-driven landings | Rewrite 6 `_index.md` (5 levels + materials) |
| **Layouts/partials** | Has `home.html`, `header`, `footer`, `page`, `material-links`, `audio-block`, **both** `vgwort/url.html` and a legacy `vgwort-pixel.html`; extra `materials/materials-list.html` | canonical partial set; single `vgwort/` tree | Remove legacy `vgwort-pixel.html`; reconcile `materials/` layouts |
| **Scripts** | One `scripts/` dir ✅; superset incl. `verify_cefr`, `verify_pdf_metadata`, `verify_qa_basics`, `verify_author_meta`, `pull_exam_pdfs`, `make_materials`, `inject_tags_topics` | canonical gate set incl. `verify_vgwort_coverage`, `verify_all_pixels`, `verify_rendered_pixels`, `verify_legal_placeholders`, `pdf_attribution` | Add the 5 missing VG Wort / legal / attribution scripts (see §5) |
| **CI** | Bespoke `hugo.yml` (Pagefind, network graph, JS budget, pa11y, LibreOffice) + `link-check.yml` — **more** than template but not aligned to `build-deploy.yml` gate-battery shape | `build-deploy.yml` discrete gate battery | Fold missing VG Wort/legal gates into `hugo.yml`; keep daf's extra gates |
| **Materials/audio** | 60 worksheets PDF + 60 presentations PDF + 774 audio, **committed** ✅; branded LaTeX via `build_materials_latex.py` ✅ | committed materials; CI verifies only ✅ | ✅ conformant (verify `pdf_attribution.py` parity) |
| **VG Wort** | Current resolver + extensions ✅; 68 marks by `path:` key ✅; legacy partial still present | shared resolver; `url:`/`path:` keyed | Delete legacy partial; add coverage/render gates (§5) |
| **Legal** | `impressum`, `datenschutz`, `haftungsausschluss`, `ueber`, `formate`, `literatur`, `danksagung` present | 3 legal + `about/` | ✅ substantially; verify no unfilled placeholders; align `about`↔`ueber` |

**Net:** DaF is **operationally superior** but **structurally pre-template**.
The mechanical items (config keys, shortcodes, accent wiring, legacy-partial
removal) are hours. The content-model migration and exam pages are the real work.

---

## 3. Audit — curriculum conformance

**Current state: non-conforming (level 0).** DaF does not reference a single
curriculum descriptor ID. Concretely:

- `grep` for `{LEVEL}.{DOMAIN}.{SCALE}.{SEQ}` across `content/` returns **nothing**.
- Units carry free-text `cefr_can_do:` German strings (e.g. *"Ich kann über
  eigene Berufserfahrungen … erzählen"*) with **no** `implements:` / `implements_id:`.
- No `conformance.yml`, no scope manifest, no coverage table.
- DaF does not run `curriculum/scripts/id-audit.sh` and publishes nothing that
  script (or `docs/verification.md`) could check.

**The worked example that applies directly:** `curriculum/examples/de-a1/`
(`conformance.yml` + `README.md`) is *the* template for what DaF must produce —
it is explicitly the German-A1 stand-in "until `daf`'s structure is mapped."
Its `realizations:` list maps German "Kann…" strings to
`implements_id: A1.REC.overall-oral-comprehension.01` etc. DaF must generalise
this to A1–C1.

**Which conformance level DaF can credibly declare:** DaF spans A1–C1, so its
ceiling is **`full`** (A1–C1: every in-scope scale with a descriptor at those
levels). Realistically, DaF's 60 thematic units do **not** currently cover every
in-scope scale (mediation and plurilingual are thin, as the framework's *honest
note* anticipates). **Recommended declaration: `core` (A1–B1) first**, mapping
the 36 A1/A2/B1 units, then extend toward `full` as B2/C1 units are mapped and
gaps are filled with explicit `no-official-descriptor` where the CV is empty.
Declare gaps; do not lower the claim to hide them (per `docs/conformance.md`).

**Machine-readable artifacts DaF must publish:**

1. **`conformance.yml`** at repo root (mirroring `examples/de-a1/conformance.yml`):
   `framework: boulingua-curriculum`, `framework_version`, `language: de`,
   `declared_conformance: core` (initially), and a `realizations:` list mapping
   every unit can-do to an `implements_id`.
2. **A scope/coverage manifest** — per the mandate in `docs/conformance.md §
   "Scope declaration"`: the set of in-scope scales DaF implements and, per scale,
   which levels are covered vs. `no-official-descriptor`. This is what makes
   coverage *auditable rather than asserted*.
3. **Per-unit descriptor IDs in front matter** — add `curriculum.cefr_can_do`
   entries keyed to IDs (or a parallel `implements:` list), so each unit page is
   itself traceable.

**Does it pass `id-audit.sh`?** N/A today — that script audits
`curriculum/levels/*.md`, not consumer repos. DaF's obligation is the **inverse**:
every `implements_id` it declares MUST *resolve to* an existing statement in
`curriculum/levels/`. The verification hook is `docs/verification.md`'s
"German A1 example passes conformance" item. DaF should ship a small validator
(or reuse the curriculum one) that loads `conformance.yml`, extracts every
`implements_id`, and asserts each exists in the curriculum level files.

**Mapping task (the core intellectual work):** for each of 60 units, take its
3–5 `cefr_can_do` strings (≈ 200–300 total) and bind each to the correct
`{LEVEL}.{DOMAIN}.{SCALE}.{SEQ}` from `curriculum/levels/{a1,a2,b1,b2,c1}.md`.
The units already declare `skills_focus` and `pruefungs_module`, which narrow the
DOMAIN (reception/production/interaction) and speed the mapping. Unmappable
can-dos signal either a needed curriculum statement (raise upstream) or a
reformulation.

---

## 4. Task roadmap

Effort tags: **S** ≤ ½ day · **M** ½–2 days · **L** > 2 days. Ordered by
dependency and value.

### Phase 1 — quick structural wins (config + design system)

- **1.1 (S)** Add to `hugo.toml`: `[taxonomies]` (tag/skill/level/topic),
  `params.code = "daf"`, `params.license = "CC BY-SA 4.0"`.
  *Accept:* `hugo` builds; taxonomy term pages render.
- **1.2 (S)** Vendor `data/accents.yaml` (or symlink the shared one); delete the
  hardcoded `#1D87A7`/`#7ECEE7` hex in `assets/css/custom.css`; drive the accent
  from `params.code`. *Accept:* daf renders identical teal accent, now sourced
  from the registry.
- **1.3 (S)** Add the 5 missing shortcodes (`hero`, `kicker`, `lead`, `card`,
  `card-grid`) from pagegen verbatim. *Accept:* shortcodes resolve in a test page.
- **1.4 (M)** Convert the 6 raw-HTML landings (`content/kurs_a1…c1/_index.md`,
  `content/materials/_index.md`) to shortcode form. *Accept:* no raw `<div
  class="hero-kicker|card-grid">` remains under `content/`.
- **1.5 (S)** Delete legacy `layouts/_partials/vgwort-pixel.html`; confirm all
  rendering flows through `vgwort/url.html`. *Accept:* grep finds no reference to
  the old partial; render-verify gate (1.9/§5) still passes.
- **1.6 (S)** Delete Quarto residue: `kurs_*/units/_metadata.yml`, `recovery/`,
  any `.qmd` refs in prose. *Accept:* no `_metadata.yml`/`.qmd` under repo.

### Phase 2 — curriculum descriptor-ID mapping (highest curriculum value)

- **2.1 (M)** Add a `curriculum:` block to all 60 units, migrating `cefr_level` →
  `curriculum.cefr_level`, adding `curriculum.framework: cefr`, moving
  `pruefungs_module` under it. Keep `cefr_can_do` for now. *Accept:*
  `verify_cefr.py` (updated to read the nested field) passes.
- **2.2 (L)** Map every unit can-do (≈ 200–300) to a curriculum `implements_id`
  from `curriculum/levels/`. Start with the 36 A1/A2/B1 units (`core`).
  *Accept:* each mapped can-do has a resolvable ID.
- **2.3 (M)** Author root `conformance.yml` (shape = `examples/de-a1/conformance.yml`):
  `declared_conformance: core`, full `realizations:` list. *Accept:* file parses.
- **2.4 (M)** Publish the scope/coverage manifest (scales × levels, with explicit
  `no-official-descriptor`). *Accept:* satisfies `docs/conformance.md` scope-declaration mandate.
- **2.5 (S)** Add a `scripts/verify_curriculum_refs.py` gate that loads
  `conformance.yml`, resolves every `implements_id` against the curriculum level
  files, and fails on any unresolved ID; wire into CI. *Accept:* green gate; a
  deliberately broken ID fails it.

### Phase 3 — content-model migration (units → bundles)

- **3.1 (L)** Convert 60 single-file units to leaf bundles:
  `content/kurs_XX/units/unitNN_slug.md` → `…/unitNN-slug/index.md` (note: `_`→`-`
  in slug to match template). Update `presentation`/`worksheet`/`aliases` paths.
  *Accept:* `hugo` builds; old URLs 301 via `aliases`.
- **3.2 (M)** Re-key all 68 VG Wort entries in `data/vgwort.yaml` from
  `path: content/…/unitNN_slug.md` to the new bundle path
  `content/…/unitNN-slug/index.md` (or switch to `url:` keys). **No new codes** —
  same works, new locations. *Accept:* render-verify gate finds every mark on its
  (new) page, once site-wide.
- **3.3 (S)** Rename `page_type` discriminator onto every page (`unit`/`section`/
  `appendix`). Rename `content/anhaenge/` → `content/appendices/` (or keep German
  with alias). *Accept:* every page has a `page_type`.
- **3.4 (S)** Normalise `skills_focus` from German (`lesen`, `sprechen`) to the
  standard enum (`reading`, `speaking_production`, …). *Accept:* only enum values
  present; taxonomy pages consistent.

### Phase 4 — first-class exam pages (largest new-content item)

- **4.1 (L)** Create 60 sibling exam bundles `…-exam/index.md` (`page_type: exam`,
  shared `unit_nr`, `exam.file` pointing at the existing
  `static/downloads/<level>/…_exam.pdf`, `duration_min`/`total_points`/
  `notenschluessel`). Author the exam-task HTML body (the PDFs already exist as
  the download artifact). *Accept:* each exam renders; PDF download resolves;
  unit↔exam linked by `unit_nr`.
- **4.2 (S)** Update the 5 level `_index.md` to link exams alongside units.
- **4.3 (REQUIRED) (M)** Assign a VG Wort Zählmarke to **every** new exam page
  that clears the 1800-char Mindestumfang — see §5. This is non-skippable.

### Phase 5 — CI + gate battery parity

- **5.1 (M)** Port the missing gates from pagegen: `verify_vgwort_coverage.py`,
  `verify_all_pixels.py`, `verify_rendered_pixels.py`,
  `verify_legal_placeholders.py`, `pdf_attribution.py`. Wire into `hugo.yml`
  keeping DaF's superior extras (Pagefind, graph, JS-budget, pa11y). *Accept:*
  all gates green on a clean build.
- **5.2 (S)** Add archetypes (`unit.md`, `exam.md`, `section.md`, `appendix.md`)
  from pagegen so `hugo new … --kind unit|exam` works. *Accept:* scaffolding a
  new unit produces conformant front matter.

### Phase 6 — extend curriculum claim

- **6.1 (L)** Map the 24 B2/C1 units; raise `declared_conformance` toward `full`;
  fill/record gaps (mediation, plurilingual) as `no-official-descriptor` where
  the CV is empty. *Accept:* coverage manifest shows every in-scope A1–C1 scale
  accounted for.

---

## 5. VG Wort — pixel assignment for all new content pages (REQUIRED)

**Binding, per `pagegen/docs/vgwort-standard.md`.** Every new content page the
roadmap introduces that is an original creative Sprachwerk **≥ 1800 rendered
characters** MUST carry exactly one Zählmarke, on exactly one URL.

**How many new pages the roadmap creates, and their VG Wort disposition:**

| Roadmap output | Count | New mark needed? |
|---|---|---|
| Migrated unit bundles (Phase 3) | 60 | **No new codes** — same works; **re-key** the 68 existing entries to the new bundle path/URL (task 3.2) |
| New exam pages (Phase 4.1) | 60 | **Yes** — up to 60 fresh public codes, for every exam page that clears 1800 chars of original task prose |
| Section `_index` landings (Phase 1.4) | 6 | **No** — navigation surfaces; marks are forbidden on hubs/indexes |
| Materials hub | 1 | **No** — hub-guard gate asserts `met.vgwort.de` is absent there |
| `conformance.yml` / manifests | n/a | **No** — not rendered reader-facing prose |

**So the roadmap introduces up to ~60 pages needing fresh Zählmarken** (the exam
pages), plus a **re-keying** of the 68 existing marks (no new codes). Procedure
for each new exam page — first-class, non-skippable:

1. **Draw fresh public codes** (32-hex "Öffentlicher Identifikationscode") — one
   per new exam work — from the author's VG Wort **T.O.M.** account. Never invent
   codes; never expose the private identification code.
2. **Register** each in `data/vgwort.yaml`, keyed by the exam page's `url:`
   (base-stripped `RelPermalink`) or `path:` (`content/…/…-exam/index.md`), with
   the token in `pixel_url`/`public_id`, `min_chars: 1800`, `author`,
   `registered_at`.
3. **Render** via the shared resolver — `layouts/_partials/vgwort/url.html` +
   the `head` preload + eager body `<img>` (already in daf). No per-page bespoke
   markup; no JS; no consent gate; `loading="eager"`; hide off-screen, never
   `display:none`.
4. **Record** each new code in the **usage registry** (§8 of the standard) —
   `Used`, `Projekt=daf`, `Sprache=de`, `Niveau (GER)`, `Kurstitel`, `URL`,
   `Pixel_URL` — kept **outside** the repo (private author data), never reused.
5. **Verify** through the gates ported in task 5.1: the **coverage audit**
   (warns on any ≥1800-char editorial page without a mark — must show 0 after
   assignment), the **render-verify** (every registered `pixel_url` appears on its
   page, once site-wide), and the **hub guard** (no pixel on `/materials/`).

**Do not** mark: legal pages (Impressum/Datenschutz/Haftungsausschluss), the home
page, materials hub, taxonomy indexes, or `/page/2/` continuations — the resolver's
pagination guard and the hub gate enforce this. Exams that are largely
short-answer grids under 1800 chars of original prose do not qualify; assess each.

---

## 6. Risks & open decisions

- **Exam migrate-vs-keep-PDF (mirrors FLE's stranded `.qmd` exams).** DaF's exams
  are download-only today. Decision: create 60 first-class HTML exam pages (Phase
  4) *and keep* the PDFs as the `exam.file` artifact — the template wants both
  (HTML page + PDF download), not one or the other. Risk: authoring 60 exam bodies
  is real content work; some may fall under 1800 chars and not qualify for a mark.
  **Open:** confirm each exam clears Mindestumfang before drawing its code.
- **DaF VG Wort authorship.** 68 marks already registered (2026-07-22) as
  S. Le Boulanger. New exam-page marks must come from the *same* author's T.O.M.
  account and never reuse an assigned code. **Open:** confirm sufficient free
  codes exist in T.O.M. for ~60 new exam works before Phase 4.
- **URL churn from bundle migration.** Slug `unit01_slug` → `unit01-slug` changes
  every unit URL, breaking existing marks and inbound links. Mitigation:
  `aliases:` (301) on every bundle **and** re-key `data/vgwort.yaml` in the same
  PR (task 3.2) so no mark is orphaned mid-deploy. **Risk:** if 3.1 and 3.2 land
  separately, the render-verify gate fails. Ship them together.
- **CI divergence (daf's extras vs template).** DaF's `hugo.yml` is materially
  richer than pagegen's `build-deploy.yml` (Pagefind, network graph, JS budget,
  pa11y, PDF metadata). **Decision:** do **not** downgrade to the template
  workflow — *add* the missing template gates into daf's workflow. **Open:**
  whether these daf-only gates should be promoted upstream into pagegen so all
  courses inherit them (recommended).
- **Conformance ambition.** Declaring `full` (A1–C1) up front risks a silently
  missing scale (a hard failure per `docs/conformance.md`). **Decision:** declare
  `core` first (task 2.3), extend to `full` only once the coverage manifest proves
  every in-scope A1–C1 scale is accounted for (Phase 6).
- **Materials committed vs CI-generated (parallels the efl question).** DaF
  commits 60+60 PDFs + 774 audio. This matches the standard (generate locally,
  commit, CI verifies) — **keep committed**; do not move TeX Live / Piper into the
  deploy path. **Open:** confirm `pdf_attribution.py` parity so committed PDFs
  carry the same attribution metadata the template gate checks.
- **`anhaenge` vs `appendices` naming.** Renaming breaks URLs of the 5 appendix
  pages (two already carry VG Wort marks: `bewertungsraster`, `glossar`).
  **Decision:** either keep German `anhaenge/` (cosmetic divergence, add alias) or
  rename with `aliases:` + vgwort re-key. Lower priority than units.
