# Ebook manuscript build

This folder contains the derived learner publication for the training plan. The canonical curriculum remains under `modules/`, and the canonical A12 case sources remain under `docs/`.

## Primary learner artifact

- [ebook-manuscript.md](ebook-manuscript.md) — complete reviewable learner manuscript in teaching order
- [manifest.md](manifest.md) — lesson, wrapper, source, reference, and A12-use inventory
- [qa-report.md](qa-report.md) — structural/content QA for the current build
- [source-provenance.json](source-provenance.json) — source hashes and available Library metadata
- [editorial-audit.json](editorial-audit.json) — editorial/link transformations performed by the builder
- [build-results.json](build-results.json) — machine-readable build counts

## Build model

The manuscript contains **108 existing lesson/conclusion chapters** plus **36 skim-first subunit wrappers** (18 introductions and 18 summaries). It also embeds **3 learner practicals** and **3 controlled lab assets** under their owning lessons. These additions do not create new numbered proficiency chapters.

The complete reconciled A12 story is inserted as **Appendix A** from `docs/companion-story/story.md`. Detailed proficiency mappings move to **Appendix B** so they remain available without interrupting normal reading.

## Rebuild

From this directory:

```bash
python build_ebook.py --source-root .. --date YYYY-MM-DD --snapshot-date YYYY-MM-DD
```

An optional inventory JSON can be supplied with `--inventory` when Library identifiers and modified/version metadata should be embedded in `source-provenance.json`. `--snapshot-date` records retrieval separately from the build date. The builder verifies each meaningful grouping has exactly one intro/summary pair and that its lessons fall between them in order. It preserves the canonical story, adapting only headings and links. External references from lessons, wrappers, and the story are consolidated.

[editorial-review.json](editorial-review.json) records the source hashes covered by the [canonical reconciliation review](../docs/a12-reconciliation-review.md). Changed or newly included sources mark editorial QA as needing review instead of repeating an old all-resolved claim. The builder never updates that review record automatically; refresh it only after an actual content/voice/skim review. Structural QA and editorial QA are reported separately.

## Gemini / NotebookLM use

The ebook manuscript is now the intended single learner upload for NotebookLM/Gemini notebook workflows. The older `exports/gemini-notebook/` split-export tree is deprecated and does not need to be rebuilt when the curriculum changes.

## Publishing status

This is still a Markdown review manuscript. DOCX/PDF/EPUB publication should be generated only after the content, structure, and editorial treatment are approved.
