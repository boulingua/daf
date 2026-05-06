# DaF — Post-Migration Verification & Integration Notes

Repo: `boulingua/daf` (DaF Goethe — German curriculum, CEFR A1–C1).
Author of all content: **S. Le Boulanger.**

This file is the running log for the post-migration verification prompt.
Older prose-style migration plans live in `MIGRATION_PLAN.md` (Quarto→Hugo)
and `MATERIALS_NETWORK_PLAN.md` (discovery network); they are kept for
historical reference but are no longer load-bearing.

---

## Phase 0 — CI gates inventory: pre-migration vs post-migration

### Source — pre-migration `publish.yml` (now removed)

The pre-migration Quarto workflow enforced:

| # | Gate | Mechanism | Status post-migration |
|---|---|---|---|
| 1 | Impressum/Datenschutz unfilled `<TODO>` placeholder check | `grep <TODO impressum.qmd datenschutz.qmd` | **kept** (`hugo.yml` step "Check legal placeholders") |
| 2 | PDF count gate (60 exam + 60 worksheet) | `find docs/downloads -name '*_exam.pdf' \| wc -l` | **replaced** by `verify_downloads.py` (per-unit existence + frontmatter cross-check) |
| 3 | PDF author-attribution gate (`/Author` must contain "Le Boulanger") | inline Python with `pypdf` | **lost in migration — must restore (Phase 6.6 below)** |

### Repo classification per prompt

DaF Goethe → these gates apply:

- ✓ Impressum/Datenschutzerklärung placeholder check (kept).
- ✗ Bildungsplan BW live-fetch (not applicable to DaF/CEFR site).
- — CEFR-level metadata enforcement (must add — Phase 6.3).
- ✗ Commercial source exclusion (no Ressourcen-Hub here).
- — Author-attribution gate site-wide (must add — Phase 6.7).
- — PDF attribution audit (must restore — Phase 6.6).

### Carried over from the network prompt (Phase 5 of the previous run)

| Gate | Status |
|---|---|
| `_scripts_phase5/build_graph.py` — 5 graph/topic/tag CI gates | active in `hugo.yml` |
| Pagefind index built post-Hugo | active |
| Plausible snippet present on `/` | active |
| Plausible snippet present on `/materials/` | active |
| VG Wort hub-page exclusion | active |
| Bundle-size budget (≤90 KB gz glue JS) | active |
| pa11y/axe a11y audit on `/materials/` (zero errors) | active |
| `verify_downloads.py` — every frontmatter file path resolves | active |
| `render_thumbs.py` — PDF/PPTX thumbnails regenerated | active |

### Outstanding (this verification pass adds)

1. Author + date frontmatter on every unit + author-attribution build gate (Phase 1, Phase 6.7).
2. Plausible parameterisation (`params.plausible.{domain,src}`) (Phase 3).
3. CEFR-level enforcement gate in CI (Phase 6.3).
4. PDF metadata gate restored (Phase 6.6).
5. `lychee` site-wide link audit + weekly schedule (Phase 5).
6. `html5validator` + Lighthouse + RSS/sitemap/robots/404 final QA (Phase 7).

---
