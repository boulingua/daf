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
| `scripts/build_graph.py` — 5 graph/topic/tag CI gates | active in `hugo.yml` |
| Pagefind index built post-Hugo | active |
| Plausible snippet present on `/` | active |
| Plausible snippet present on `/materials/` | active |
| VG Wort hub-page exclusion | active |
| Bundle-size budget (≤90 KB gz glue JS) | active |
| pa11y/axe a11y audit on `/materials/` (zero errors) | active |
| `verify_downloads.py` — every frontmatter file path resolves | active |
| `render_thumbs.py` — PDF/PPTX thumbnails regenerated | active |

### Outstanding (this verification pass adds)

| # | Item | Status |
|---|---|---|
| 1 | Author + date frontmatter on every page | done — `scripts/inject_author_date.py`, 83 files patched |
| 1' | Author-attribution build gate | done — `scripts/verify_author_meta.py` (84 pages, 0 violations) |
| 2 | Plausible parameterisation | done — `params.plausible.{domain,src}` in hugo.toml |
| 3 | CEFR enforcement | done — `verify_cefr.py` (60/60 pass) |
| 4 | PDF metadata audit | done — `verify_pdf_metadata.py` (120/120 pass) |
| 4' | VG Wort data-file lookup + Mindestumfang audit | done — `data/vgwort.yaml` registry header-only; `vgwort_audit.py` warns on 70 long-form pages without tokens |
| 5 | `lychee` link audit + weekly schedule | done — `.github/workflows/link-check.yml` |
| 6 | RSS / sitemap / robots / 404 sanity | done — `verify_qa_basics.py` (108 sitemap URLs, 74 RSS items, robots.txt enabled, 404 styled) |
| 6' | `html5validator` + Lighthouse | deferred — pa11y/axe already gates a11y; html5validator + lhci require Java + Chrome + tend to be flaky in CI; will re-evaluate after first CI run with all current gates green |

### Outstanding for the author / Raban

- **VG Wort Zählmarken** — 70 long-form pages have no token. They surface as `::warning::` in every CI run via `vgwort_audit.py`. Tokens are issued from the T.O.M. portal and cannot be generated in CI. Add entries to `data/vgwort.yaml` as marks are registered.
- **Materials placeholders** — 60 PPTX + 60 PDF files are stamped *Platzhalter*; replacing them with real content is editorial.
- **Hand-curated content tags** — Phase-1 of the network gave each unit 4 deterministic tags (level + module + skill + topic). Adding 2–3 author-chosen content tags per unit (e.g. `passé-composé`, `wohnen`) would densify the discovery graph meaningfully.

---

## Per-phase log

### 2026-05-06 — Verification pass complete

8 commits today on top of the network MVP. CI pipeline now runs:

```
build_graph.py → render_thumbs.py → verify_downloads.py
  → verify_cefr.py → verify_pdf_metadata.py
  → check legal placeholders
  → hugo --minify
  → pagefind index + verify
  → verify_author_meta.py → verify_qa_basics.py
  → Plausible-on-/ → Plausible-on-/materials/
  → VG Wort hub-page exclusion → vgwort_audit.py
  → verify-vgwort.sh
  → bundle size budget → pa11y audit
  → upload-pages-artifact → deploy
```

Every step is reproducible via `python scripts/<script>.py` from the repo root.

---
