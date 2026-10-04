# Defensive Cyber Operations — Ebook Review Project

This project is a derived learner publication of the current MalasadaTech training curriculum. It uses the live `/thraining-plan/` source snapshot retrieved on 2026-10-02 and was built on 2026-10-03. **The canonical curriculum remains the source of truth.** No module, instructor guide, slide deck, or canonical story was changed by this project.

## Read and Review

Start with [ebook-manuscript.md](ebook-manuscript.md). It contains the complete book, including all 107 student-facing chapters, front matter, the full A12 narrative, proficiency mappings, glossary, acronym list, and consolidated references. The manuscript is approximately 100,000 whitespace-delimited words, including the reference and mapping material.

Use [manifest.md](manifest.md) to trace each chapter to its source and identify its references and A12 passages. Read [qa-report.md](qa-report.md) for the checks performed and unresolved source conflicts. This is **v0.1 Review Draft**, not a publication-ready final edition.

## What Was Assembled

| Part | Content | Chapters |
|---|---|---:|
| I | Shared Foundations: 0.1–0.8 and 0.9 summary | 11 |
| II | SOC: 1.0 introduction, 1.1–1.5 lessons, 1.6 summary | 28 |
| III | CTI: 2.0 introduction, current 2.1–2.8 units, 2.9 summary | 41 |
| IV | Threat Hunting: 3.0 introduction, 3.1–3.7 lessons, 3.8 summary | 16 |
| V | Detection Engineering: 4.0 introduction, 4.1–4.8 lessons, 4.9 summary | 10 |
| VI | Unnumbered course conclusion | 1 |

The CTI track retains requirements and RFI intake, tradecraft, frameworks, platform selection and orientation, enrichment, assessment, production, dissemination, and local application in that order. The platform chapters retain their two-pass learning model and combined time estimates.

Student guides supply the teaching body. README files were used for structural checks. Instructor guides, slides, old exports, and development notes do not become learner chapters. No DOCX, PDF, EPUB, or print layout was produced. A separate set of chapter copies was not necessary: one deterministic builder assembles the single manuscript directly from the canonical sources.

## Editorial Treatment

The book adds a title page in Markdown, a spoiler-light case introduction, a linked contents list, Part openings, brief unit bridges, glossary, and acronym list. Headings use one book H1, Part H2s, chapter H3s, and lesson sections at H4–H6. Chapter numbers retain their curriculum identities; local section numbers are removed from headings so they do not compete with chapter numbers.

Existing purpose sections move before learning objectives when both are present. Technical explanations, learning objectives, knowledge checks, examples, tables, and all fenced code remain. Detailed ratings, target-audience metadata, and task mappings move to Appendix B. The ten introductions and summaries explicitly marked as unmapped remain unmapped.

Standalone Previous/Next lines and repeated module-index links are removed. Useful related reading remains, with book links. A small number of stale navigation labels are corrected; full details are in [editorial-audit.json](editorial-audit.json). Provided-report wording supports independent reading without implying that this ebook includes a separate lab dataset. Deliberate repetition of evidence boundaries and role responsibilities remains because those concepts support different decisions in different tracks.

The voice pass is intentionally conservative. Newly written connections use explanatory prose. Source passages are not broadly paraphrased or simplified where doing so could change evidence, uncertainty, task requirements, or technical meaning. The canonical story’s stronger claims are preserved and flagged rather than rewritten.

## A12 at Three Levels

1. **Front matter:** organization, workstation, account, and the reason the case recurs. It does not reveal the outcome or later findings.
2. **Course chapters:** the existing progressive evidence and exercises remain in their original teaching positions. Sparse Appendix A links orient the learner at role-track openings.
3. **Appendix A:** the complete narrative from `/thraining-plan/docs/companion-story/story.md`, with its nine original stages and close.

The companion-story README identifies `story.md` as the finished retelling and `/thraining-plan/docs/story-bible.md` as the governing fact ledger. The bible was used for the consistency review, not substituted for the narrative. Appendix A removes only the final maintainer-only instruction, repairs nested emphasis, and updates book cross-references. The RFI reference now distinguishes intake in 2.1.5 from response in 2.7.4; the obsolete “0.3 f” reference links to 0.3. It adds no resolution, attribution, host count, or deployment result.

**A12 substantive discrepancies remain unresolved.** The QA report identifies them for a later canonical editorial decision. Review the relevant source lessons and story together before accepting a revised case narrative.

## Rebuild

Requires Python 3.9 or newer and its standard library. Work from a fresh local copy of the current canonical curriculum, preserving its directory tree. The source root must contain `modules/` and `docs/`. Retrieve current source files again for a later edition; do not rebuild from old exports.

With this project placed at `thraining-plan/ebook/`, run:

```bash
python3 build_ebook.py --source-root .. --date 2026-10-03
```

If a current full file inventory is available, retain the source identities by providing it:

```bash
python3 build_ebook.py --source-root .. --inventory /path/to/current-inventory.json --date 2026-10-03
```

The inventory is the complete file-list JSON with an `items` array. Without it, the build still records source paths and SHA-256 hashes, but Library identity fields will be null. The present build retains available identities, modification times, and hashes in [source-provenance.json](source-provenance.json); no source version number was invented when the listing returned none.

The builder writes only beside itself. It regenerates:

- `ebook-manuscript.md`
- `manifest.md`
- `source-provenance.json`
- `editorial-audit.json`
- `build-results.json`

`README.md` and `qa-report.md` are editorial documents and must be reviewed after each rebuild. The current build date can be supplied with `--date`; the source-snapshot date in the builder must also be updated after retrieving a new snapshot. A deliberate 107-chapter/count check will stop the build if the curriculum changes; review the inventory and Part counts before updating that expectation.

The builder contains the book-only front matter, Part openings, unit bridges, glossary, acronym list, and presentation transformations. Make publication-only edits there so a rebuild preserves them. Make substantive curriculum corrections in the canonical project through a separate approved task, then rebuild. Direct changes to the generated manuscript will be overwritten by the next build.

## Validation and Next Review

The build checks chapter counts and uniqueness, mapping status, internal heading targets, external-link occurrence preservation, exact fenced-code preservation, normalized source-line coverage, story-line coverage, and unchanged source text. [build-results.json](build-results.json) records the latest structural totals. The audit identifies explicitly moved or edited content; normalization changes Markdown presentation rather than the underlying lesson statements.

Automated coverage checks support, but do not replace, editorial review. For this draft, also review the A12 discrepancies, check whether the remaining source voice should be revised more broadly, and decide how supplied reports and local-environment exercises will be packaged. External URLs were preserved but not checked for live availability. Platform screens and documentation may change independently of this snapshot.

Markdown is the review deliverable. Export and final layout work remain a later phase.
