# Gemini Notebook export

A **Gemini Notebook** (formerly NotebookLM) source for this course. Upload an export. Do not treat an export as the syllabus.

The files under [exports/gemini-notebook/](../exports/gemini-notebook/) are **exports**. Edit `docs/story-bible.md`, `modules/**/student-guide.md`, or `docs/companion-story/story.md`, then **rebuild the whole tree** in the same change. Do not surgical-edit a lesson inside a blob.

## Sets

| Set | Path | One file is | Count |
|-----|------|-------------|-------|
| Whole course | [student-corpus.md](../exports/gemini-notebook/student-corpus.md) | Bible + every student guide + companion story | 1 |
| Layer 1 — track | [by-track/](../exports/gemini-notebook/by-track/) | First digit (`00` … `04`) | 5 |
| Layer 2 — unit | [by-unit/](../exports/gemini-notebook/by-unit/) | First two ID segments (`1.1`, `2.8`, `4.1`) | 40 |
| Layer 3 — lesson | [by-lesson/](../exports/gemini-notebook/by-lesson/) | Full lesson ID (`1.1.1`, `2.4.1`, `4.1`) | 94 |
| Fiction (shared) | [fiction/](../exports/gemini-notebook/fiction/) | Bible; companion story | 2 |

Grouping uses the ID on the student-guide `# Module` line, not the folder name.

**Depth as available:** if the lesson ID is only `X.X` (`0.1`, `3.1`, `4.1`–`4.8`), the layer-3 file **is** that `X.X`. Do not invent `4.1.1`. If the only child is already `X.X.X` (`2.4.1`), layer 2 is `2.4.md` and layer 3 is `2.4.1.md`.

Track and unit files concatenate their lessons in teach order. Each lesson keeps a `Source:` path.

Fiction is **not** copied into every unit or lesson file (that would pollute flashcards). Attach the two fiction files as extra sources on any notebook that needs names and A12.

## When you must rebuild

Rebuild **the whole** `exports/gemini-notebook/` tree (corpus, by-track, by-unit, by-lesson, fiction copies) in the same change if you touch any of:

- a **student-guide**
- the **story bible**
- the **companion story**

Instructor-only, slides-only, and matrix-only changes do not require a rebuild.

This is a Gate 2 requirement: [contributing.md](contributing.md), [generate-module.md](generate-module.md).

After a rebuild, **re-upload** the files you use. Gemini Notebook keeps a static copy. It does not watch git.

## Flashcards and the 50-source cap

Gemini Notebook accepts Markdown. Free plan: **50 sources** per notebook, 500,000 words or 200 MB per source.

| Notebook grain | What to upload | Fits free plan? |
|----------------|----------------|-----------------|
| Whole course | `student-corpus.md` | Yes (1 source) |
| Track flashcards | `by-track/` (5) + `fiction/` (2) | Yes |
| Unit flashcards | `by-unit/` (40) + `fiction/` (2) | Yes (42 ≤ 50) |
| Lesson flashcards | **one** `by-lesson/NN/` folder + `fiction/` (2) | Yes |

Layer 3 is **94** files. That is over 50. Upload **one track** at a time:

| Folder | Lessons |
|--------|---------|
| `by-lesson/00/` | 10 |
| `by-lesson/01/` | 26 |
| `by-lesson/02/` | 36 |
| `by-lesson/03/` | 14 |
| `by-lesson/04/` | 8 |

Google AI Pro (300 sources) can take all 94 in one notebook. The tree still works.

Not in these exports: instructor guides, slides, matrices, this file, labs.

## Names

Lessons may still say **Night Owl** and **Harbor**. Canonical names are **Pink River Dolphin (PRD)** and **Dixon, Yamada, & Associates (DYA)**. If a lesson and the bible disagree, **the bible wins**.

## Suggested notebook instructions

Paste in the notebook, not in the export:

- Answer from these sources only.
- If the bible and a lesson disagree, the bible wins.
- Night Owl / Harbor in a lesson means PRD / DYA.
- Do not invent DYA hunt tickets, PIR lists, approval chains, or a site architecture card.
- Extra adversary infrastructure is a block for firewall / IA (`0.3 f`), not Detection Engineering.
- The companion story is the same incident after the lessons, not a second plot. Plant and use facts in desk order (do not dump the Run key into the first alert).
- Flashcards: one idea per card, from the sources. Stay in this track / unit / lesson.
