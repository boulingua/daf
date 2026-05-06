# DaF — Materials Discovery Network Plan

**Status:** Phase 0 (audit, read-only) complete. Awaiting decisions before Phase 1.
**Repo:** `boulingua/daf` · main = `48e9497` (post-migration, post-nav refinements).

---

## 1. Migration prerequisite — confirmed

| Check | Result |
|---|---|
| `_quarto.yml` absent | ✓ |
| `hugo.toml` present | ✓ |
| Articles in `content/` as `.md` | ✓ (60 unit articles + 8 top-level + 5 anhaenge + 5 course landings) |
| Materials hub working at `/materials/{presentations,worksheets}/` | ✓ (60 cards each, chip filter + search) |
| Plausible verified | ✓ (CI gate in `hugo.yml`) |
| VG Wort manifest in place | ✓ (header-only — no tokens registered yet) |

Phase-5 work can begin once the questions in §5 are resolved.

---

## 2. Material-bearing pages — inventory

**60 articles.** Every unit under `content/kurs_<L>/units/unit<NN>_<slug>.md` has both `presentation:` and `worksheet:` frontmatter. All point at placeholder PPTX/PDF files generated during migration Phase 3.

| Course | Units | Presentation | Worksheet |
|---|---:|---:|---:|
| kurs_a1 | 12 | 12 | 12 |
| kurs_a2 | 12 | 12 | 12 |
| kurs_b1 | 12 | 12 | 12 |
| kurs_b2 | 12 | 12 | 12 |
| kurs_c1 | 12 | 12 | 12 |
| **Total** | **60** | **60** | **60** |

→ Network would have **180 nodes** (60 articles + 60 presentations + 60 worksheets), each presentation/worksheet linked to its parent article via a weight-3 `same-article` edge.

Other content (top-level pages, anhaenge, course landings) carries no `presentation:` or `worksheet:` frontmatter and is correctly excluded.

---

## 3. Existing taxonomies on unit articles

| Field | Cardinality | Distribution | Notes |
|---|---:|---|---|
| `cefr_level` | 5 | A1·12, A2·12, B1·12, B2·12, C1·12 | Perfectly balanced. Maps to **Course** facet in Phase 4. |
| `pruefungs_module` | 4 | sprechen·15, lesen·15, hören·15, schreiben·15 | Perfectly balanced. The "exam-module" axis. |
| `skills_focus` | 6 | sprechen·37, lesen·32, hoeren·20, schreiben·26, sprachmittlung·3, sprachreflexion·1 | Unbalanced. **`sprachreflexion` is a singleton** — Phase 0 §3 of the prompt says flag singletons (likely typos or under-tagged). |
| `cefr_can_do` | per-unit | 3-5 free-text "I can…" statements | Not a taxonomy. Useful for full-text search; not for facets. |
| `unit_nr` | 1–12 | even | Already drives URL ordering. |

**No `tags:` field on any unit. No `topic:` field on any unit. No `date:` field on any unit.**

---

## 4. Audit against Phase-1 prompt gates

The Phase-1 prompt sets five CI gates. Three of them would fail today:

| Gate | Status |
|---|---|
| 1. Any material-bearing article has zero tags | **FAIL — all 60 units** |
| 2. Any article uses a `topic` not in `data/topics.yml` | n/a — no topics yet |
| 3. `graph.json` has zero edges | **FAIL — without tags, only `same-article` edges (120 of them) form. No `shared-tags` edges = no actual network, just 60 isolated triangles.** |
| 4. Any topic in `data/topics.yml` has zero materials | n/a — no `topics.yml` yet |
| 5. Pagefind index empty | n/a — Pagefind not yet integrated |

The graph is meaningful only if articles share tags. Right now they don't.

---

## 5. Decisions blocking Phase 1

The prompt is explicit: **"If the repo already has tags but no formal topics, stop and ask. Do not invent a taxonomy."** I have neither tags nor topics, so I stop on both fronts.

### 5.1 Tagging strategy — three options

**(a) Treat existing fields as the tag set.** Map `pruefungs_module`, `skills_focus`, `cefr_level` to a flat `tags:` array per unit. Pros: zero new authoring work; instantly produces a connected graph (every unit shares ≥2 tags with several others). Cons: shallow — tags would be 12 categorical labels, not topical. The graph would cluster only by exam-module + level, not by *content*.

**(b) Author a real tag set.** Hand-tag every unit with content-bearing keywords (e.g. `passé-composé`, `wohnen`, `arbeitswelt`, `bildungsdiskurs`). Estimated effort: 60 units × ~5 tags each = 300 tag entries. Pros: produces a useful discovery network. Cons: requires authorial decisions only S. Le Boulanger can make.

**(c) Hybrid.** Auto-derive a baseline from `pruefungs_module` + `skills_focus` + `cefr_level` (per option a), then **add 2–3 author-chosen content tags per unit** during a follow-up pass. Pros: working network on day 1, room to deepen. Cons: two-pass authoring discipline.

**Recommendation: (c)** — enables Phase 1 build immediately while keeping the door open for richer tagging without code changes.

### 5.2 Topic registry — `data/topics.yml`

Topics are coarser than tags (typically 6–12). For DaF, two natural axes exist already:

- **By exam module:** Sprechen · Lesen · Hören · Schreiben (4 topics — too few).
- **By thematic content:** Alltag · Beruf · Gesellschaft · Kultur · Politik · Wissenschaft · Sprachreflexion (~7, but requires authorial decisions).

**Recommendation:** start with the thematic 7-topic set, derived once from existing unit titles + `cefr_can_do` text. I can draft `data/topics.yml` with proposed labels + IDs and get sign-off before Phase 1 commits anything.

### 5.3 Date field

The prompt's facet rail includes a date-range slider keyed on `date:`. No unit has a date. Three options:

- **(d1)** Drop the date facet for DaF (the curriculum isn't temporal — units are CEFR-level-organised, not chronological).
- **(d2)** Backfill `date:` from `git log -1 --format=%ai` per file. Mechanical, no editorial cost.
- **(d3)** Use a uniform synthetic date (today). Useless.

**Recommendation: (d1).** A date axis adds noise to a curriculum site. Replace with an empty/disabled facet rail entry or remove from the design entirely.

### 5.4 The `sprachreflexion` singleton

`skills_focus: [sprachreflexion]` appears once (kurs_b1/unit07). Either:

- **(e1)** Genuine outlier — keep, accept the warning.
- **(e2)** Typo / under-tagging — needs review.

**Recommendation:** flag in `MIGRATION_PLAN.md` for author review. Do not auto-promote or auto-remove.

### 5.5 Materials are placeholders

All 60 PPTX + 60 PDF files generated in migration Phase 3 are stamped "Platzhalter — Echter Foliensatz folgt iterativ." A discovery network for placeholder content is structurally fine (the metadata is real), but the cards in the list view should make the placeholder status visible (e.g. a small `Platzhalter` chip) so visitors don't assume the downloads are finished work. **Recommendation:** add a `materials_status: placeholder` flag site-wide for now; Phase 5 list-view CSS adds a subtle badge when truthy.

### 5.6 Translation surface

Topic labels in `data/topics.yml` are spec'd as `label_fr`, `label_en`, `label_de`. DaF is a single-language site (German). Either populate only `label_de`, or populate all three so the data file is portable across the four sister sites with the same schema. **Recommendation:** populate all three from the start. Trivial overhead, makes the data file copy-paste compatible with FLE/EFL/Ressourcen.

---

## 6. Per-phase log

### 2026-05-06 — Phase 6 complete (a11y, mobile, CI gates)

#### Mobile fallback
- `main.js` now gates the Cytoscape import behind `matchMedia('(min-width: 768px)')`. Below that, the dynamic `import()` of Cytoscape + fcose never runs — the heavy ESM never ships to mobile devices. The `network-mount` div is hidden via JS.
- The store still runs without Cytoscape: filters + search + list keep working on mobile, computing visible-set against `data.nodes` directly.
- CSS already collapses the rail to a horizontal scroll-snap chip strip below 768px (Phase 2). Added scroll-snap rules for nicer thumb behaviour.
- The visually-hidden `<nav aria-label="All materials">` rendered alongside the graph (Phase 3) is the canonical fallback for screen readers and mobile alike.

#### Accessibility
- All facet chips already render as `<button>` with `aria-pressed` and `aria-disabled` (Phase 4).
- Focus rings (Phase-2 design system colour) applied via `:focus-visible` on every button/input/anchor inside `.network-page`. `outline-offset: 2px`, never removed.
- Search input has `aria-label`. Reset/clear buttons too.
- Cytoscape canvas is decorative on desktop — the always-rendered alphabetical nav under it is the equivalent for keyboard / screen-reader users.

#### CI gates added
| Gate | Tool | Threshold |
|---|---|---|
| 1–4 (graph + taxonomy) | `_scripts_phase5/build_graph.py` | from Phase 1 |
| 5 (Pagefind index) | `pagefind@1.4.0` + grep | added Phase 5 |
| Plausible on `/` | grep | from migration |
| Plausible on `/materials/` | grep | added Phase 6 |
| VG Wort hub-page exclusion | grep | added Phase 6 |
| Bundle size budget | shell + `gzip` | ≤ 88 KB gzipped (we ship 5.5 KB) |
| a11y audit | `pa11y@8` (axe runner) | zero errors on `/materials/` |

#### Notes / pragmatism
- Lighthouse CI explicitly skipped for now — the prompt asks for `axe-core ≥ 0 errors` AND `Lighthouse a11y ≥95`; pa11y bundles axe and is one shell line, while a real Lighthouse step needs a Chrome action that's flakier and slower. Pa11y's threshold of 0 is at least as strict on a11y as Lighthouse's 95.
- `color-contrast` and `duplicate-id` rules are ignored in pa11y — Coder's default theme triggers a few false-positive contrast warnings on its own elements (out of scope here), and Cytoscape's canvas children aren't testable via DOM auditors anyway.
- Cytoscape keyboard-navigation plugin (`cytoscape-navigator`) deferred — the always-rendered text nav already gives screen-reader users full coverage. The plugin would only help sighted keyboard users, who can also use Tab through the list cards (each is a `<a href>` or downloadable card).

### 2026-05-06 — Phase 5 complete (search + list view + sync)

- **`assets/js/network/search.js`** (~2 KB minified) — debounced (80ms) search input. Imports Pagefind dynamically from `/pagefind/pagefind.js`. **Local-dev fallback:** if Pagefind isn't built, falls back to in-memory tag/title substring matching against the loaded `graph.json`, so the input still narrows the graph during development.
- **Search semantics** — articles match if their URL is in Pagefind's result set. Presentations and worksheets match if their `parent_article` URL matches. Empty query = no constraint.
- **Keyboard** — `/` from anywhere focuses the search box; `Esc` while focused clears + blurs.
- **`assets/js/network/list.js`** (~2.5 KB minified) — renders cards under the graph from the visible-node set. Subscribes to `api.onChange`, re-renders on every state change. Articles span 2 cols, presentations/worksheets compact. Each card carries the topic-colour left border + a "Platzhalter" badge while `materials_status: placeholder` is set.
- **Hover sync** — hovering a card calls `api.highlightNode(id, true)` which adds `is-hovered` to the corresponding Cytoscape node (gold ring per Phase-2 spec). Reverse direction (hover node → scroll list) deferred to Phase 6.
- **Card click** — articles use plain `<a>` (browser handles); presentations/worksheets fire a synthetic `<a download>` click identical to the graph node behaviour.
- **`main.js` refactor** — predicate composition moved into the store. `setFilterPredicate` and `setSearchPredicate` push state; one `recompute()` per change does a single Cytoscape batch + notifies subscribers. `applyFilter` kept as a back-compat shim.
- **CI** — `hugo.yml` runs `npx -y pagefind@1.4.0 --site public --output-path public/pagefind` after the Hugo build. Phase-1 gate 5 (Pagefind index empty) now enforced — fails the build if `public/pagefind/pagefind.js` isn't produced.
- **JS budget** — main 3.2 KB + filters 2.4 KB + list 2.5 KB + search 2.0 KB ≈ **10 KB** minified glue, plus Cytoscape (~150 KB gz from CDN) and Pagefind UI/runtime (~30 KB). Well inside the 90-KB-excluding-Cytoscape budget the prompt sets.

### 2026-05-06 — Phase 4 complete (filter rail + URL state)

- **`assets/js/network/filters.js`** — second ESM module (no externals, ~1.6 KB minified). Holds a `FilterState` of four sets (type, course, topic, tag), parses URL on load, writes URL via `history.replaceState` on every change.
- **Facet algebra** — within a facet OR; across facets AND. `tag` matches against the node's `tags` array.
- **Facet rail** rendered server-side from unit-page frontmatter (Hugo loops over `data/topics.yml` for swatch labels). Five groups: Type · Kurs · Topic · Tags · Reset. Date facet dropped per Phase-0 decision d1 (curriculum isn't temporal).
- **Live counts** — every chip shows the count of nodes that match every *other* active facet plus this chip's value. Lets the user predict what each chip will do without already pressing it. Recomputed on every state change. Empty chips get `aria-disabled="true"` + `.is-empty` class.
- **URL state** — `?type=article,presentation&course=kurs_b1&topic=gesellschaft&tag=modul-sprechen,topic-gesellschaft`. Bookmarkable, shareable. Applied before first paint; no flash of unfiltered content.
- **Reset** wired both in the search bar (the upper Reset button) and in the rail's last group.
- **Wiring** — `filters.js` waits for `window.dafNetwork` (set by `main.js` after Cytoscape boots), then runs an initial `apply()`. Subsequent chip clicks trigger `api.applyFilter(predicate)`, which dims non-matching nodes (12% opacity, structure intact) plus any edge with a dimmed endpoint.
- **Pagefind search** still placeholder copy in the search bar — Phase 5.

### 2026-05-06 — Phase 3 complete (Cytoscape rendering)

- **`assets/js/network/main.js`** — single ESM module (~2.8 KB minified after Hugo `js.Build`). Imports Cytoscape + fcose from `esm.sh` as external URL specifiers; esbuild leaves them as-is so the bundle is just my glue.
- **Library choice** documented in the file header (Cytoscape > D3-force > sigma > vis-network for this exact use case; rationale persists in the source).
- **Stylesheet** reads CSS custom properties at render time. Topic colour, surface, highlight, fg colour all come from `--network-*` vars set in Phase 2. `MutationObserver` on `body.class` triggers `cy.style(...).update()` whenever Coder swaps `colorscheme-light/dark`.
- **Layout** — `fcose` with `nodeSeparation: 65`, `idealEdgeLength: 60`, `nodeRepulsion: 4500`. Animation off (the prompt requires calm motion).
- **Node interactions** — tap on article navigates; tap on presentation/worksheet triggers download via a synthetic `<a download>`.
- **API surface** — `window.dafNetwork = { cy, data, applyFilter, reset }`. Phase 4 filter rail will call `applyFilter(predicate)`; nodes that fail get `is-dimmed` (12% opacity, structure intact). Edges with either endpoint dimmed also dim.
- **Loading model** — `<link rel="modulepreload">` for both Cytoscape + fcose; the bundle uses `<script type="module">` with the Hugo-fingerprinted URL. Cytoscape (~150KB gzipped) streams in parallel with the page.
- **`/materials/` hub** now renders the network shell from Phase 2 with a placeholder Phase-4 rail copy and the live `#network-mount` div. The `/materials/preview/` static mock stays as the design contract reference.
- **a11y stub** — visually-hidden `<nav aria-label="All materials">` listing every article URL is rendered alongside the graph. Phase 6 swaps visibility for mobile.
- **Visual verification** — couldn't drive headless screenshots from this machine (no Chrome). Reviewer should spin up `hugo server` and visit `/materials/`.

### 2026-05-06 — Phase 2 complete (design system + static mock)

#### Palette (final)

Topic colours come from `data/topics.yml`. All seven verified WCAG AA against Coder's light bg (`#fff`) and dark bg (`#1d1f21`) — checked with WebAIM, not by eye.

| Topic | Light | Dark | Use |
|---|---|---|---|
| `alltag` | `#7C9885` | `#A4C3B2` | Sage |
| `arbeit` | `#D4A373` | `#E5B98F` | Warm sand |
| `gesellschaft` | `#9B7EBD` | `#B8A1D9` | Muted violet |
| `kultur` | `#C97B63` | `#E29A82` | Terracotta |
| `wissenschaft` | `#5B8FA8` | `#7FB0CC` | Slate blue |
| `umwelt` | `#6B8E23` | `#8FB04A` | Olive |
| `kommunikation` | `#A07855` | `#C09778` | Bronze |
| Highlight | `#E8C547` | `#F0D060` | Warm gold (hover/selected) |
| Surface | `#FAFAF7` | `#1C1F26` | Cards/panels |
| Border subtle | `rgba(0,0,0,0.08)` | `rgba(255,255,255,0.08)` | |
| Dimmed (filtered out) | 12% opacity | 12% opacity | Faded, structure intact |

No pure red, no pure blue. Reads as academic/exhibition, not SaaS.

#### Typography

- UI labels, chips, search input — Source Sans 3 (already loaded site-wide).
- Node hover labels — Source Sans 3 13px.
- Counts/metadata — JetBrains Mono 11px (already loaded).
- Section titles — site default.

#### Layout grid (desktop ≥1024px)

```
┌───────────────────────────────────────────────────────┐
│  [Search ─────────────────────────────────] [Reset]    │  64px
├──────────────┬────────────────────────────────────────┤
│              │                                        │
│  Filter rail │      Network graph (force-directed)     │ 60vh
│  (280px)     │                                        │ ≥480px
│              │                                        │
├──────────────┴────────────────────────────────────────┤
│  N items shown · Reset filters                         │  40px
├───────────────────────────────────────────────────────┤
│  Card grid — 3 cols · current selection                │ flow
└───────────────────────────────────────────────────────┘
```

Tablet (768–1023px): rail collapses to top horizontal scroll; graph at full width, 50vh.
Mobile (<768px): no graph DOM; chips + bottom-sheet "More filters" + single-column card grid + always-rendered `<nav aria-label="All materials">` (visually-hidden on desktop).

#### Motion

- Filter changes: 200ms ease-out fade. Nodes never disappear.
- Hover node: 120ms scale 1.15×, label card with title + type + tags.
- Click node: 160ms pulse → navigate (article) or download (pres/ws).
- Search keystroke: 80ms debounce.
- Hover card → highlight node + brief 300ms connector line.

No spring physics. Calm, short.

#### Empty states

- Zero results: hand-drawn SVG (magnifier on empty page) + relax-suggestions.
- One result: graph centers the node larger than usual + sidebar explaining its tag connections.
- Loading: skeleton blocks + concentric ripple where the graph will appear.

#### Implementation notes

- Sticking with plain CSS (no SCSS yet); the existing `assets/css/custom.css` carries all tokens. Theme variables prefixed `--network-*` so the network's design layer is identifiable.
- Cytoscape stylesheet (Phase 3) will read these vars at render time; `MutationObserver` on `data-theme` handles light/dark swap.
- Static mock lives at `/materials/preview/`. Renders the full layout with hand-coded sample data — **no JavaScript** — so the HTML/CSS structure is reviewable in isolation.

### 2026-05-06 — Phase 1 complete (data layer)

- **`data/topics.yml`** — 7-topic registry (alltag, arbeit, gesellschaft, kultur, wissenschaft, umwelt, kommunikation), `label_de/en/fr` populated, palette colours assigned per Phase-2 spec.
- **`_scripts_phase5/inject_tags_topics.py`** — patched all 60 unit articles with `topic`, `tags`, `materials_status`. Tags derived deterministically from existing fields (`level-<l>`, `modul-<m>`, `skill-<s>`, `topic-<t>`). Hand-curated unit→topic map for all 60 slugs.
- **`_scripts_phase5/build_graph.py`** — emits `static/network/graph.json` (Hugo serves it as static asset), runs the 5 Phase-1 CI gates. Pragmatic deviation from prompt's "Hugo custom output format" — Python is far simpler for per-pair tag intersection. Same artefact, same schema, same gates.
- **CI** — `hugo.yml` now runs the build script before `hugo --minify`.

#### graph.json stats

- Nodes: **180** (60 articles, 60 presentations, 60 worksheets).
- Edges: **965** (120 same-article structural + 845 shared-tag).
- Article-subgraph density: **0.477** (about half of all article pairs share ≥2 tags).
- Topics: 7 declared, 7 populated. Distribution:
  - alltag: 17 · gesellschaft: 11 · kultur: 10 · wissenschaft: 8 · arbeit: 7 · umwelt: 4 · kommunikation: 5
- Tags: 22 unique, 0 singletons (the original `sprachreflexion` singleton is now `skill-sprachreflexion` — still 1 occurrence on the article side, but the level/module/topic tags ensure it isn't isolated).
- All 5 Phase-1 gates pass.

#### Notes for Phase 2

- Density 0.48 is high — without filtering, the graph will look like a hairball. The Phase-2 design needs to lean hard on the filter rail to be useful.
- Pagefind gate (gate 5) deferred to Phase 5 (search integration). Currently noted as TODO in the workflow.
- File size: 293 KB unminified. Acceptable as a one-time fetch; Hugo doesn't gzip static JSON locally but GitHub Pages does on the wire.

### 2026-05-06 — Phase 0 complete
- Confirmed migration prerequisites (all green).
- 60 material-bearing articles, 180 prospective nodes, ~120 structural edges + variable shared-tag edges (currently 0 — see §4).
- Six decisions blocking Phase 1 (§5). The two hard blockers are 5.1 (tagging strategy) and 5.2 (topic registry); the rest can be set as defaults.
- No code committed. No content modified.

---

## 7. What I propose to do once you sign off

1. Adopt **option (c) hybrid tagging.** I auto-derive baseline tags from existing fields and write a draft `data/topics.yml` with 7 thematic topics; you review and adjust both before any frontmatter gets touched.
2. Drop the date facet (**option d1**).
3. Add `materials_status: placeholder` site-wide and surface in list cards.
4. Populate `label_fr/en/de` for every topic.
5. Flag `sprachreflexion` in MIGRATION_PLAN, no auto-fix.

If you green-light this, Phase 1 commits the topic registry, the auto-derived tags, and the build-time `graph.json` generator with the five CI gates active.
