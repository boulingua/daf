# Phase 1 — Discovery (read-only) · DaF / boulingua-daf

## 1.1 Repo identity

| Check | Result |
|---|---|
| `git remote -v` | `origin → https://github.com/boulingua/daf.git` |
| Config files at root | `hugo.toml` (no `_quarto.yml`, no `config.toml`) |
| Language site | **DaF Goethe** — German curriculum, CEFR A1–C1 |
| Content root | `content/` |

## 1.2 Pre-Hugo content search

### Branches / log / stash / reflog

- Branches: `main`, `backup/pre-author-rewrite-20260506`, `origin/migration/hugo-coder` (post-migration housekeeping branch — not a pre-Hugo branch).
- No branches named `quarto`, `pre-hugo`, `legacy`, `migration-quarto`, `main-old` — anywhere.
- `git stash list`: empty.
- `git reflog --all` head: every entry is from this session's verification work.
- `git log --all --diff-filter=D --summary | grep -iE "track|spur|niveau|gym|haupt|real|G\+M|track-e"` — **0 matches.**
- `git log --all -- '**/*.qmd' '**/*.Rmd'` — only the migration-Phase-4 commit `edd12a6` ("chore(migration): remove quarto + add aliases, exam pdfs, parity audit") which removed all 145 `.qmd` files. Pre-migration history shows the `.qmd` files were CEFR units (`kurs_a1/units/...`), never tracked under G+M / E.

### Working-tree leftovers

- No directories named `_archive*`, `backup*`, `old*`, `_legacy*`, `.trash*`, `track*`, `spur*`, `niveau*`.
- No `.qmd`, `.Rmd`, or `.ipynb` files anywhere.
- No `_site/`, `public_old/`, `_book/`.
- `.gitignore` has no entries for any track-related path.

### Active-file references

- `grep -rIn -E "(track[ -]?(g\+m|e)|spur|niveau|gymnasium|hauptschule|realschule|werkreal)" content layouts hugo.toml`:
  - 2 incidental hits, both legitimate German prose, neither a track reference:
    - `kurs_b1/units/unit01_neuanfang-in-basel.md:228` → "**Beispiel-Antwort auf Zielniveau (B1):**" (German for "target level B1")
    - `kurs_c1/units/unit09_fachsprachen-wirtschaft-medizin-recht.md:155` → "Ich sprachmittle eine Fachaussage auf **Alltagsniveau**." (German for "everyday level")
  - **No genuine track-G+M / track-E references** in content, layouts, or config.

### Backup branch

- `git ls-tree -r --name-only backup/pre-author-rewrite-20260506 | grep -iE 'track|spur'` → **0 hits.**

## 1.3 Inventory

| Location (commit/branch/path) | Track | Klassen covered | File types | Approx. unit count | Notes |
|---|---|---|---|---|---|
| _(none found)_ | — | — | — | — | DaF was never a BW Bildungsplan / Gesamtschule site; it has always been organised by CEFR levels A1–C1, not by Bildungsplan tracks. |

For reference, the units that **do** exist in the current Hugo tree:

| CEFR level | Units present | Convention |
|---|---:|---|
| `kurs_a1` | 12 | A1 — Anfänger:innen |
| `kurs_a2` | 12 | A2 — Grundlegende Kenntnisse |
| `kurs_b1` | 12 | B1 — Selbstständig (untere Stufe) |
| `kurs_b2` | 12 | B2 — Selbstständig (obere Stufe) |
| `kurs_c1` | 12 | C1 — Kompetent |
| **Total** | **60** | — |

All 60 unit articles, 5 course landings, 5 anhänge, 9 top-level pages, and the materials network are in place. None of them is a stub or `draft: true`.

## 1.4 Conclusion

**No track G+M or track E content exists, was lost, or could be lost in this repo.**

DaF Goethe is the CEFR-organised sister site of the boulingua family. The Track G+M / Track E division belongs to the BW-Gesamtschule sites (`boulingua/efl`, `boulingua/fle`). The track-recovery prompt — explicitly repo-agnostic on the discovery side — finds nothing here because there was never anything of that kind to begin with.

Phases 2–6 of the recovery prompt do not apply to this repo. No staging directory needs to be created, no source-of-truth selection is required, no mapping needs to be authored, no conversion is needed, no coverage / gap reports need to be filed beyond this one.

If the prompt was meant to run only against `boulingua/efl` and `boulingua/fle`, run it there. Stopping here per the prompt's "stop and confirm" rule before any change is made.
