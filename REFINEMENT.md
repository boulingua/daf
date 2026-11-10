# Current candidate evidence — 2 November 2026

This review branch is not a full-course release. The dated sections below retain
earlier observations; this section supersedes their material-production and local
validation status. No production deployment or release tag is claimed.

All 60 unit bundles now have 180 independently checked PDFs (1,923 pages)
and 180 matching thumbnails. The deck, learner worksheet and teacher worksheet
preserve source content, symbols, links and answer separation. Publication was
guarded by source/artifact hashes and retains original backups. The repository
receipt is [docs/material-build-2026-10-31.json](docs/material-build-2026-10-31.json),
with actual completion dated 2 November. All 120 active unit/exam review
records now match their current source bytes; exact superseded sources and ledger
revisions are archived. Review states and proposed mappings remain pending.

The 60 standalone assessment pages now have 120 learner/teacher PDFs with separate source-bound receipts. All 60 authored scoring formats pass A13. The site explicitly loads the shared design tokens before course styles.

The strict Hugo build and all configured engineering checks pass except the
blocking D6 historical-audio gate (716 findings). The final browser run
exercised five representative pages and course-specific journeys, including
light/dark accessibility, downloads, search and no-JavaScript access, with zero
accessibility findings, script errors or failed requests. Existing educational
budget and counting-mark warnings remain visible; they have not been waived.

There are 208 separately staged, source-bound candidate voice clips for this
course. Full decode and input/provenance checks pass, but every clip still awaits
real listening review. Production recordings and their truthful failing D6 result
remain unchanged. The suite's `remediation/audio-candidates/index.html` supplies
transcripts, downloads and the pending review queue.

Use the exact prerequisites and commands in [README.md](README.md) with matching
candidate foundations. Release still requires substantive teaching/assessment
repairs, actual native and pedagogical review, timing/grade decisions, accepted
audio, compatible published foundation pins and successful release checks.

## Historical refinement record

# Refinement record — 30 October 2026

This is a local engineering candidate on `refine/2026-10-30`. No hosted CI,
published release or production deployment of these changes has been observed.
The suite strategy and integration order live in the organisation repository,
`docs/refinement-2026-10-30.md` and `docs/release-candidate-2026-10-30.md`.

## Purpose and improvements

The course contains 60 teaching units and 180 committed PDFs. The search index respects the project prefix, shared layouts handle missing material directories, and the materials pages describe available PDFs rather than obsolete PowerPoint placeholders. Course-specific templates use explicit layouts without changing addresses.

Shared kit repairs provide accessible navigation, real search indexing, corrected contrast/text sizing, local asset/link checks and representative browser tests. Local templates are selected by explicit layout independently of frozen URLs. Material templates have been synchronised; existing course PDFs and recordings were preserved.

## Actual validation

Strict Hugo build passed. Desktop/mobile browser journeys, automated WCAG 2.1 AA checks, search, downloads, no-JavaScript content and required local engineering checks passed. A21 now passes after the template migration. D6 remains a **release failure**: historical recordings lack sufficient model/speaker provenance and dated voice approval. A passing website build must not conceal that result. English also retains the recorded C1 mark-registry warning; no mark or published address was changed to silence it.

The strengthened curriculum resolver accepts the in-progress manifest structure, not its proposed educational assertions. Two framework source omissions and native/educational review remain blockers. One representative deck and worksheet were rebuilt and visually reviewed in a disposable copy; the full PDF corpus was not regenerated or pedagogically reapproved.

## Roadmap and acceptance

1. Review the local software candidate with the matching kit, curriculum and organisation checkouts using README.md.
2. Audition the prepared candidate voice or provide human recordings. Record actual reviewer/date/model or recording provenance; regenerate synthetic recordings only after approval, or document verifiable historical provenance. Do not invent approval for existing files.
3. Repair the framework source omissions, independently review the course mappings and assessments, and review regenerated materials before replacing committed PDFs.
4. Publish compatible dependencies and pins, run the hosted gate battery, and deploy only after every blocking gate is green and publication is authorised.

Local engineering improvements are usable for review. This course has not met all educational/audio release criteria.


## 31 October 2026 — keyed unit structure and source preservation

All units now declare the five canonical EQS steps and preserve prior heading
anchors from the rendered site. Original source and before/after hashes are in
`docs/eqs-archive/2026-10-31/`. Course mappings remain proposed; the source-hashed
review ledger is `docs/curriculum-review-2026-10-31.json`. It records actual tasks,
current descriptor statements and remaining coverage cells without fabricated
review decisions. Body/exam length and pedagogical approval remain separate.

The existing activation questions were promoted from each lead-in into their own
step without rewriting the teaching text. Sixty new sibling exam pages retain
the original module tasks. Their scope, timing, input completeness and marking
need review before being presented as complete assessments. The manifest now
tracks 120 pages and 600 proposed realization pairs.


## Analytics notice consistency — 31 October 2026

Plausible remains enabled and now names its self-hosted script URL explicitly. The privacy notice states the actual script URL and site identifier; unsupported assertions about server location, retained data and guaranteed anonymity were removed from the Plausible section.

Privacy pages declare their analytics policy, language and built URL. New kit gate C9 checks actual HTML scripts and visible notices against configuration; it rejects missing, duplicate or mismatched scripts and contradictory notices. Six gate regressions and three scaffold tests passed. Representative strict builds/C9 passed for website, nsf, nvt, gfl, Scriptlibrary and all three resource-hub notice languages; the suite integration run verifies the remaining sites. This is configuration/content evidence, not certification of the remote server or legal compliance.

## Assessment source repairs — 2026-10-31

All60 standalone module exercises received a source review;17 now contain their actual missing stimuli. Explicit teacher blocks, confirmed task/key defects, coherent official-source corrections and preserved originals are documented in [the assessment review](docs/assessment-review-2026-10-31.md). Source validation passed; rendered artifacts and pedagogical acceptance remain separate pending checks.


## Explicit release dependencies — 31 October 2026

The shared workflow caller now names the same immutable org commit in `uses` and
`org_ref`; `release-pins.json` records the actual historical kit/framework pins.
These historical pins are explicitly not the remediated release. The new org
workflow rejects absent/malformed versions, mismatched source commits and schema
bytes, and nonconforming course manifests; hubs pin dependencies without claiming
course conformance. The coordinated updater prepares exact published foundation
sets, updates consumers/checksums together and retains rollback inputs. Separate
read-only candidate CI can validate immutable pre-release commits without release
tags or deployment rights. Hosted execution and new foundation publication remain
unobserved. See the org `docs/release-pins.md`.

## Integration with main — 10 November 2026

This branch was updated by merging `main` before integration. Main's published
foundation set (org v2.0.1, kit v2.0.2, curriculum v1.3.0), its regenerated
lesson recordings and audio manifests (5 November) and the analytics section of
its privacy notice replace the historical pins, the earlier audio manifest
mapping and the 31 October analytics wording recorded above; D6 now passes.

4 units whose recorded input text was revised on this branch no longer match
their recordings: `kurs_a2/units/unit11_umwelt-und-alltag`,
`kurs_b1/units/unit04_gesundheitssystem-dach`,
`kurs_b2/units/unit06_migrationsdiskurs`,
`kurs_b2/units/unit11_oekonomie-fuer-laien`. Before release these need new
recordings of the revised text, or a decision to keep the recorded wording.
