# Gemini Notebook export

A **Gemini Notebook** (formerly NotebookLM) source for this course. Upload the corpus. Do not treat the corpus as the syllabus.

| File | What it is |
|------|------------|
| [exports/gemini-notebook/student-corpus.md](../exports/gemini-notebook/student-corpus.md) | Student-facing snapshot: bible, every student guide in teach order, companion story last |

The corpus is an **export**. Edit `docs/story-bible.md`, `modules/**/student-guide.md`, or `docs/companion-story/story.md`, then **rebuild the whole corpus** in the same change. Do not surgical-edit one lesson inside the blob.

## When you must rebuild

Rebuild `exports/gemini-notebook/student-corpus.md` in the same change if you touch any of:

- a **student-guide**
- the **story bible**
- the **companion story**

Instructor-only, slides-only, and matrix-only changes do not require a rebuild.

This is a Gate 2 requirement: [contributing.md](contributing.md), [generate-module.md](generate-module.md).

After a rebuild, **re-upload** the file to Gemini Notebook. The notebook keeps a static copy. It does not watch git.

## What is in the corpus

Teach order: bible → `0` → SOC `1` → CTI `2` → hunt `3` → DE `4` → companion story.

Not in the corpus: instructor guides, slides, matrices, this file, labs.

## Names

Lessons may still say **Night Owl** and **Harbor**. Canonical names are **Pink River Dolphin (PRD)** and **Dixon, Yamada, & Associates (DYA)**. If a lesson and the bible disagree, **the bible wins**.

## Upload

Gemini Notebook accepts Markdown. Free plan: 50 sources, 500,000 words or 200 MB per source. This corpus is one source and sits well under those caps.

Suggested notebook instructions (paste in the notebook, not in the corpus):

- Answer from these sources only.
- If the bible and a lesson disagree, the bible wins.
- Night Owl / Harbor in a lesson means PRD / DYA.
- Do not invent DYA hunt tickets, PIR lists, approval chains, or a site architecture card.
- Extra adversary infrastructure is a block for firewall / IA (`0.3 f`), not Detection Engineering.
- The companion story is the same incident after the lessons, not a second plot. Plant and use facts in desk order (do not dump the Run key into the first alert).
