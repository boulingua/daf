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
