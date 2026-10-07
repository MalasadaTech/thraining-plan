# Gemini Notebook split exports — retired

The older `exports/gemini-notebook/` tree was a **legacy derived export**. It is retired from the required publishing workflow because the complete ebook manuscript now serves as the portable learner source. Historical copies, if retained elsewhere, need neither deletion nor regeneration.

## Current learner workflow

Use the complete learner manuscript:

[ebook/ebook-manuscript.md](../ebook/ebook-manuscript.md)

A reader can upload that single Markdown file into NotebookLM / Gemini notebook tools instead of maintaining separate by-track, by-unit, by-lesson, and fiction export sets. The manuscript already includes the course in teaching order, skim-first subunit introductions and summaries, the reconciled A12 appendix, and learner reference material.

## Source of truth

The ebook remains a **derived publication**. Canonical course content lives in:

- `modules/**/student-guide.md`;
- meaningful subunit `intro.md` and `summary.md` wrappers;
- `docs/story-bible.md`;
- `docs/companion-story/story.md` and its supporting canonical story files.

When learner-facing canonical sources change, fix those sources and rebuild the ebook with:

```bash
python ebook/build_ebook.py --source-root . --date YYYY-MM-DD
```

Do not patch `ebook/ebook-manuscript.md` as a second source of truth.

## Retired workflow

Normal curriculum changes rebuild the ebook manuscript instead of recreating by-track, by-unit, by-lesson, or fiction export sets. This retirement pass does not delete historical files.

If an instructor eventually needs a purpose-built instructor corpus, generate that as a separate derived publication rather than reviving the old learner split-export tree.

## Publishing sequence

Canonical modules, subunit wrappers, and reconciled A12 sources → ebook build → `ebook/ebook-manuscript.md` → later approved DOCX/PDF/EPUB. Keep source corrections in the canonical files and verify the rebuilt manuscript after saving.
