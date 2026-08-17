# Generate a module (AI instructions)

Use this file when asked to generate or revise module content for an **existing** teaching-unit ID (Gate 2). Humans follow [contributing.md](contributing.md). You follow this file.

This is a procedure for **every** lesson. Stay-in-this-lesson notes live in [training-outlines.md](outlines/training-outlines.md) under that ID. Do not invent requirements, IDs, or a new voice.

**Caller prompt (either tool):**  
`Follow docs/generate-module.md and generate teaching-unit <ID> (<Title>) for me to review. Do not invent IDs.`

---

## 0. Preconditions

Stop and say what is missing if any of these fail:

- The ID already exists as a combined.md heading **or** a `#` cell (for example `1.2.5`, `2.1`, `3.1.1`).
- You were given that ID, not a vague topic and not an old display number (`section 7`, `section 8`).
- Gate 1 is done. You are not proposing a new matrix row.

**Assign work by ID prefix:** `0.x` and shared-floor IDs live under `modules/00-intro/` and are taught **before SOC**: `0.1`–`0.5`, then `1.5`, `3.3.2`, `1.8.1`. `1.x` SOC content is `1.1`–`1.4` and `1.6` (`modules/01-soc/`). `2.x` = Hunt (`modules/02-hunter/`), `3.x` = CTI (`modules/03-cti/`). `4.x` = Detection Engineer (`modules/04-de/`). **Retired — do not generate:** `1.7`, `1.8.2`, `1.8.3`, `1.8.4`, `1.8.5`.

**How big is one lesson**

| Caller ID | What to generate |
|-----------|------------------|
| A **cluster** heading with several distinct K topics | **Stop.** List the child K items and ask which one. Do **not** write the whole cluster unless the human asks for those children together. |
| A **child item** | That K row plus its child T row(s) only. |
| A **unit** that is already one lesson | That heading’s rows (K and matching T). |

If the user wants a **new** requirement, stop and point them at [templates/requirement-proposal.md](../templates/requirement-proposal.md).

---

## 1. Read, in this order

1. The [training-outlines.md](outlines/training-outlines.md) block for **this lesson** — the K heading, its tasks, and any stay-in-this-lesson note under that heading or its unit. Not the whole cluster.
2. The matching combined.md **rows** (the K item and its T pair), plus 3/5/7 codes for every role that has a column.
3. The matching role matrix (`soc.md` / `hunter.md` / `cti.md` / `de.md`).
4. [proficiency-legend.md](proficiency-legend.md)
5. [contributing.md](contributing.md) Gate 2
6. [templates/student-guide.md](../templates/student-guide.md), [instructor-guide.md](../templates/instructor-guide.md), [slides.md](../templates/slides.md)
7. A **voice sibling** — see below

Also open [concept-index.md](concept-index.md) and [tracker.csv](tracker.csv) before you write.

**Voice sibling:** clone **voice** from `modules/00-intro/` or `modules/04-de/` (short, Intro, no pad). Use the previous module in the same unit only for names already taught and to stay out of that hour. **Do not copy** an old hour-long sibling’s length, section list, tables, example count, slide count, or labs.

---

## 2. Resolve IDs (do not invent)

| You need | Where it comes from |
|----------|---------------------|
| Lesson ID | What the user typed. Not a cluster heading unless they asked for those children together. |
| Matrix item IDs | Combined `#` cells for this lesson only. Do not invent a sibling T. |
| Outline block | The outline K heading + tasks that map to those rows, plus the stay-in-this-lesson note. |
| Folder | `modules/<role>/<unit>/<nn-short-name>/` (intro and DE may be `role / module`). |
| Roles | Primary/secondary from the matrix. List every role that has a code on the combined row. |
| Proficiency lines | Copy **3 / 5 / 7** codes from the matrix into **both** the student guide and the instructor guide. Same string in both files. Do not collapse levels. Do not invent a code. |

Record the outline ↔ matrix map in the module `README.md`.

If Gate 1 said “add to an existing module,” amend that folder. Do not create a new one.

---

## 3. Clone this shape

Match the voice sibling (plain words, same names, stay in this lesson). **Do not copy** that sibling’s length, section list, tables, example count, or slide count.

**Do not add optional content to fill.** If the template marks a section optional and this lesson does not need it, omit it.

| Artifact | Shape |
|----------|--------|
| Time | As long as the outline needs. Never stretch a short topic to fill 60–75 minutes. |
| Audience | Primary + secondary roles from the matrix |
| Proficiency | 3/5/7 codes from the matrix, per role, identical in student + instructor headers |
| Student guide | Objectives → **Intro** (why this hour exists in the job) → key concepts that cover the outline, including what each **task** looks like when done well. **No labs, demos, or hands-on exercises** until the human asks. **Knowledge check: 1–3 questions per lesson** that has slides. Short summary. |
| Instructor guide | **Intro required** (Context + what this hour is). No demo or lab write-up until the human asks. Timing table lists only sections you actually teach. Answers for the 1–3 lesson questions. |
| Slides | As many as you need. Intro + concepts + **knowledge check (1–3 questions for the lesson)** are required. No demo or exercise slides until the human asks. Face of each slide is short enough to read alone. **Speaker Notes** on every slide: a few plain sentences (why this slide, how it connects). |
| Answers | Only in the instructor guide. No standalone `answer-key.md`. No quiz. |

Outline **tasks stay**. Teach what the task *is* (the product line, what good looks like). **Do not write labs, demos, or hands-on exercises** unless the human asks. Existing labs stay until that section is reviewed.

Examples: use them when they help. Do not invent fail-stories to hit a count.

**“This lesson / other” table** and **“expected vs lead” table:** optional. Add one only if it prevents a real mix-up. Do not add both by default. Do not add them to fill.

**Knowledge check:** **1–3 questions per lesson** that has slides. Required. Not per concept. Do not write a fourth question to fill. Do not ask about the next lesson just to have more items.

Voice: direct, instructional, short paragraphs, tables for fields.

**Student Intro (required).** First paragraph of Key Concepts, before the outline ideas. Ordinary words. Why this hour exists in the job — what the person actually does, and why they do it. Not outline letters. Not only “last hour was X.” Put the same idea on slide 2. If you cannot finish “in this job they do this because ___,” you do not have an intro.

**Context (required). Challenges (only if real):**

Write **Context (plain language)** as the first block in the instructor overview, before Key Teaching Points. Anyone who was not in the planning chat should still see the connection. Use ordinary words. No outline letters, no matrix codes in this block. The “what this hour is for” line must match the student Intro.

Include:

- What this hour is for (one or two sentences)
- How it hooks to the hour before and the hour after (one line each)
- Why we are doing it this way (the human’s stated reason, not a new rule)
- What we are *not* doing this hour

If you add a step the human did not say, it must appear in Context as “extra, because ___.” If you cannot finish that sentence, do not add the step. Do not jump ahead.

**Common Student Challenges:** omit the whole list when the hour is this simple. Do not invent struggles to satisfy a quota. If you *do* list a challenge, each bullet is one short why + one concrete example.

**Slides:** someone who only reads the deck should still get the point. Speaker notes carry the why; they are not “read the bullets again.”

**Words:** use the word the outline and student guide already use. If you want a shop nickname, define it on first use in ordinary words. Do not invent a second name and assume the reader knows it.

**Stay in this lesson:** the outline note under this ID (or its unit) is the fence. Do not pull in the next child or another unit.

---

## 4. Teach at least the outline

- Outline knowledge bullets (`a`, `b`, `c`…) become the field/idea sections. None may be skipped.
- Outline tasks are taught as *what good looks like*, not as a lab (until the human asks for labs).
- Combined.md / role-matrix rows are the **sign-off** items and IDs. Put them in the README map.
- Expansion is allowed when it supports the outline. New obligations need Gate 1.
- If an outline bullet has no home in this teaching-unit, **stop** and say so. Do not drop it.
- Stay out of the *next* lesson. Point to it under Related modules.

---

## 5. Write these files

New module:

```
modules/<role>/<unit>/<nn-short-name>/
  README.md
  student-guide.md
  instructor-guide.md
  slides.md
  assets/.gitkeep
```

`README.md` must include path, roles, time, mapped proficiency table, **Concepts taught**, artifact links.

Then update:

- [concept-index.md](concept-index.md) — every README concept; **Taught** here; **Used** on this module for terms taught earlier; aliases people will search; link the folder, not a line number
- [tracker.csv](tracker.csv) — add or update the row; mark only the artifacts you actually wrote
- [tracker.md](tracker.md) — folder map row if this ID is new
- README numbering table in the repo root if this ID is new

Do not set tracker status to human-accepted (`Complete` on the whole package). Use the per-artifact columns: student/instructor/slides complete, then tell the user it is ready to review.

---

## 6. Do not

- Generate a whole cluster when asked for one child (unless the human asked for those children together)
- Skip an outline bullet because the matrix row is shorter
- Invent matrix IDs, outline headings, or proficiency codes
- Collapse or invent 3/5/7 codes
- Invent local policy, tickets, field lists, approval chains, or PIR lists
- Index sample IPs, `example.com`, or passing name-drops
- Copy shared frameworks into a role folder
- Mark the module human-accepted — stop for review
- Write Gate 1 proposal files unless asked
- Skip **Context (plain language)** or the student **Intro**
- Invent Common Student Challenges to fill a quota, or leave a listed challenge as a label with no example
- Leave a slide without plain-language speaker notes
- Jump ahead of what the human asked without saying why in Context
- Pad a short lesson, or add optional sections only to fill
- Copy a sibling’s table of contents, timing, or example set
- Write more than 3 knowledge-check questions for the lesson, or skip the 1–3 when the lesson has slides
- Write a new lab, demo, or hands-on exercise unless the human asked for one
- Skip the fluff review when you finish
- Use a shop nickname in the instructor guide or slides without the student-guide word or a one-line gloss

---

## 7. When you finish

List the paths you wrote and the outline ↔ matrix map. Remind the reviewer to confirm: (1) every outline bullet/task is in the student guide, (2) stay-in-this-lesson notes were followed, (3) Concepts taught matches the index, (4) Context is in the instructor guide, (5) the student **Intro** says why this hour exists in the job, (6) any challenges have examples (or the list is omitted), (7) every slide has plain speaker notes, (8) **fluff review done**, (9) 1–3 knowledge-check questions for the lesson, (10) no new lab/demo unless asked, (11) status stays at review until they accept the lesson.

**Fluff review (required, you and the human):** For each extra example, table, slide, lab step, or question, say which outline bullet it serves. If you cannot, delete it.
