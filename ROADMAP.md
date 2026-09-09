# DaF — roadmap to completion

**Audited 2026-09-09** against `curriculum` v1.1.0 and the `pagegen` template.
The July `HANDOVER.md` remains as the historical record.

**Status: the smallest of the three mature courses, and the only one whose exams
exist as material but not as pages.** 60 exam PDFs and 60 exam PNGs are committed
and a pull script is in the repo — the publishing step was never taken.

---

## 1. Measured state

| | |
|---|---|
| Unit bundles | **60** across `kurs_a1` … `kurs_c1` |
| Exam bundles | **0** |
| Exam PDFs committed | **60** (`static/downloads/*/unitNN_slug_exam.pdf`) |
| Exam preview PNGs committed | **60** |
| `page_type` discriminator | on all 60 pages |
| `curriculum:` front-matter block | on all 60 pages |
| Naming convention | `unitNN_slug` — **non-conformant** (template mandates `unitNN-slug`) |
| Forbidden `slug:` in front matter | none |
| Raw HTML section markup | none |
| Quarto remnants | none |
| Materials | 379 PDF |
| Audio | 714 files |
| `conformance.yml` | **missing** |
| `[taxonomies]` in `hugo.toml` | **missing** |
| `navTitle` | present |

DaF organises by CEFR level (`kurs_a1` … `kurs_c1`) rather than by
Bildungsplan track, which is correct for a course aimed at adult and
newcomer learners rather than at a single Land's syllabus.

## 2. What "finished" means here

`declared_conformance: core` (A1–B1) proven by `conformance_audit.py resolve`,
with the A2–C1 content that already exists mapped and, where it reaches, declared
as `full`. Sixty units across five levels is thin — twelve per level — so the
honest first claim is `core` with the higher levels recorded as partial.

## 3. Roadmap

### Phase 1 — publish the exams that already exist (M, highest value here)

- [ ] Generate 60 sibling exam bundles `unitNN-slug-exam/index.md` with
      `page_type: exam`, each linking the committed PDF and PNG.
- [ ] Follow the `efl` exam bundle as the template — it is the only conformant
      example of this page type in the organisation.
- [ ] Confirm `scripts/pull_exam_pdfs.py` still reflects where the PDFs live, or
      retire it if the pull is no longer needed.

**Why first:** the material is bought and paid for. Sixty exams are committed and
reach no reader. This is the largest gap between what DaF *has* and what DaF
*publishes*, and it is a generation task, not an authoring one.

### Phase 2 — converge on the template naming (S, scriptable)

- [ ] Rename 60 bundle directories `unitNN_slug` → `unitNN-slug`, and publish
      redirects for the changed URLs.
- [ ] Do this **before** Phase 1 if the exam bundles are generated from the unit
      names, so the exams are born with the right names rather than renamed twice.

### Phase 3 — declare conformance (S)

- [ ] Copy the `conformance.yml` shape from `efl` once it exists (see the suite
      roadmap — EFL is the pilot).
- [ ] Populate `realizations` from the `curriculum:` blocks already on all 60
      pages.
- [ ] Gate on `conformance_audit.py resolve` in CI.
- [ ] Read the coverage report honestly: with twelve units per level, expect many
      `core` cells to come back unpopulated. Record them as gaps.

### Phase 4 — close the template gaps and fill the level (S, then L)

- [ ] Declare `[taxonomies]` in `hugo.toml`.
- [ ] Decide the target unit count per level. Twelve units for a whole CEFR level
      is a syllabus outline, not a course; `efl` carries 180 units for a
      comparable span.

## 4. Gaps declared, not hidden

- **Sixty units across A1–C1 is thin.** The repo declares A1–C1 but the density
  will not support a `full` claim. Declare `core`, publish the coverage report,
  and let the gaps be visible rather than implied.
- Audio (714 files) is dense relative to the unit count, which suggests the audio
  pipeline is ahead of the authoring. Worth confirming that every clip is
  referenced by a page.

## 5. Dependencies

- `efl` Phase 1 for the manifest shape and the exam bundle template.
- `curriculum` ≥ 1.1.0, `kit` v1.21.0, `boulingua/.github` for CI.
