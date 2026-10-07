# Generate a module (AI instructions)

Use this file when asked to generate or revise module content for an **existing** teaching-unit ID (Gate 2). Humans follow [contributing.md](contributing.md). You follow this file.

This is a procedure for **every** lesson. Stay-in-this-lesson notes live in [training-outlines.md](outlines/training-outlines.md) under that ID. Do not invent requirements or IDs. Learner-facing structure and voice follow [skim-first-authoring-standard.md](skim-first-authoring-standard.md) and the templates; student-facing text must stand alone. Specification files may be terse, but their maintenance language is **not** a voice model for learner prose.

**Caller prompt (either tool):**  
`Follow docs/generate-module.md and generate teaching-unit <ID> (<Title>) for me to review. Do not invent IDs.`

---

## 0. Preconditions

Stop and say what is missing if any of these fail:

- The ID already exists as a combined.md heading **or** a `#` cell (for example `1.2.5`, `3.1`, `2.1.1`).
- You were given that ID, not a vague topic and not an old display number (`section 7`, `section 8`).
- Gate 1 is done. You are not proposing a new matrix row.

**Teach order:** `0` → shared floor → SOC `1` → **CTI `2`** → hunt `3` → DE `4`. Folders: `modules/02-cti/`, `modules/03-hunter/`.

**Assign work by ID prefix:** `0.x` and shared-floor IDs live under `modules/00-intro/` and are taught **before SOC**: `0.1`–`0.5`, then `0.6`, `0.7`, `0.8`, `0.9`; the `0.10` summary is synthesis-only. `1.x` SOC content is `1.1`–`1.4` and `1.5` (`modules/01-soc/`). `2.x` = CTI (`modules/02-cti/`). `3.x` = Hunt (`modules/03-hunter/`). `4.x` = Detection Engineer (`modules/04-de/`). **Retired — do not generate:** `1.7`, `1.8.2`, `1.8.3`, `1.8.4`, `1.8.5`.

**How big is one lesson**

| Caller ID | What to generate |
|-----------|------------------|
| A **cluster** heading with several distinct K topics | **Stop.** List the child K items and ask which one. Do **not** write the whole cluster unless the human asks for those children together. |
| A **child item** | That K row plus its child T row(s) only. |
| A **unit** that is already one lesson | That heading’s rows (K and matching T). |

**Subunit-wrapper exception:** when the human explicitly asks for an introduction and/or summary around an **existing meaningful instructional grouping**, create synthesis/navigation content rather than treating the grouping as a new proficiency lesson. Use [subunit-intro.md](../templates/subunit-intro.md) and [subunit-summary.md](../templates/subunit-summary.md). Do not invent matrix IDs or new requirements for these wrappers. Apply the hierarchy rule in [skim-first-authoring-standard.md](skim-first-authoring-standard.md): instructional hierarchy, not every filesystem directory.

If the user wants a **new** requirement, stop and point them at [templates/requirement-proposal.md](../templates/requirement-proposal.md).

---

## 1. Read, in this order

1. The [training-outlines.md](outlines/training-outlines.md) block for **this lesson** — the K heading, its tasks, and any stay-in-this-lesson note under that heading or its unit. Not the whole cluster.
2. The matching combined.md **rows** (the K item and its T pair), plus 3/5/7 codes for every role that has a column.
3. The matching role matrix (`soc.md` / `hunter.md` / `cti.md` / `de.md`).
4. [proficiency-legend.md](proficiency-legend.md)
5. For any Task (`T`) row, [qualification-demonstration-signoff-standard.md](qualification-demonstration-signoff-standard.md) and the matching row in [qualification-evidence-map.md](qualification-evidence-map.md)
6. [contributing.md](contributing.md) Gate 2
7. [skim-first-authoring-standard.md](skim-first-authoring-standard.md)
8. When the lesson uses A12, [a12-scenario-governance-standard.md](a12-scenario-governance-standard.md) and [story-bible.md](story-bible.md)
9. [templates/student-guide.md](../templates/student-guide.md), [instructor-guide.md](../templates/instructor-guide.md), [slides.md](../templates/slides.md); for wrappers also read [subunit-intro.md](../templates/subunit-intro.md) and [subunit-summary.md](../templates/subunit-summary.md)
10. A **voice sibling** — see below

Also open [concept-index.md](concept-index.md) and [tracker.csv](tracker.csv) before you write.

**Voice sibling:** use a nearby revised lesson to understand established terminology, expected depth, and stay-in-lesson discipline. **Do not copy its prose rhythm blindly.** Learner voice comes from the skim-first standard and current templates, especially the explanatory mentor-like style. Older cue-card, slogan-heavy, or prohibition-heavy wording is not a voice source. Use the previous module in the same unit mainly for names already taught and boundaries already established.

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
| Student guide | **Why This Matters / advance organizer** → objectives → descriptive concept/decision headings → mapped task/workflow guidance → **knowledge check (1–3 questions for the lesson)** → **end-state summary**. Examples/callouts only when they improve comprehension. Readable with no live instructor. |
| Instructor guide | Learning-arc context → preview emphasis → teaching notes → answer key → **skim-first instructor check**. Timing table lists only sections actually taught. Notes should help a substitute understand the teaching logic; they should not supply explanations missing from learner materials. |
| Slides | **Why this matters** → optional `What to watch for` roadmap → concept/decision slides → **knowledge check (1–3 questions for the lesson)** → **By this point, you should be able to…**. Slide titles should expose the learning structure during a skim. Speaker notes explain why the idea matters and how it connects. |
| Answers | Only in the instructor guide. No standalone `answer-key.md`. No quiz. |

Outline **tasks stay**, including their approved verbs. Teach what the task is, why it matters, what good looks like, and the reasoning needed to perform it.

**Lesson completion is not automatically task qualification.** Use [qualification-demonstration-signoff-standard.md](qualification-demonstration-signoff-standard.md): **Taught / Prepared → Demonstrated → Qualified / Signed Off**. Do not redefine **execute**, **perform**, **test**, **produce**, **disseminate**, or **follow** into a weaker planning/discussion activity.

**Do not automatically write a lab, demo, or hands-on exercise for every task.** If a separate practical demonstration is required, preserve that requirement in [qualification-evidence-map.md](qualification-evidence-map.md) and only author the practical when the human asks or the implementation plan reaches that step. Existing labs stay until that section is reviewed.

Examples: use them when they help. Do not invent fail-stories to hit a count.

**“This lesson / other” table** and **“expected vs lead” table:** optional. Add one only if it prevents a real mix-up. Do not add both by default. Do not add them to fill.

**Knowledge check:** **1–3 questions per lesson** that has slides. Required. Not per concept. Do not write a fourth question to fill. Do not ask about the next lesson just to have more items.

### Voice and skim-first structure

Learner-facing prose should sound like an **experienced analyst coaching a junior analyst**. Use explanatory paragraphs and natural connective reasoning. Explain why a distinction matters and how the evidence supports the conclusion. Prefer positive guidance over chains of prohibitions.

Avoid using slogan fragments or compressed contrasts as the main explanation, such as `X ≠ Y`, “Information describes. Intelligence judges.”, or repeated “This is not…” / “Do not…” statements. A short contrast can reinforce an explanation, but it should not replace one.

A useful reasoning pattern is:

**Evidence → Reasoning → Bounded Conclusion → Action**

A reader with no live instructor must understand the student guide and slide faces. Define unfamiliar shop/SIEM language in ordinary words on first use.

**Student introduction (required):** begin with **Why This Matters** or equivalent natural prose. It should activate useful prior knowledge, preview the main ideas, point out an important distinction/decision to watch for, and give the learner a sense of the expected end state. Do not mechanically answer four prompts if prose works better. Put the same mental model on the opening slides.

**Summary (required):** write it as an **end-state check**, preferably with `By this point, you should be able to…`. It should tell the learner what they can now explain, distinguish, decide, or do. Do not simply restate section headings.

**Context for instructors (required):** explain the learning arc in ordinary prose: what prior knowledge is activated, what new capability is developed, and where the learner goes next. State a scope boundary only when it prevents a likely misunderstanding; do not make “what we are not doing” a mandatory teaching pattern.

**Common Student Challenges:** include only real, predictable misunderstandings. Each one should explain why it happens and give a concrete example.

**Slides:** the deck should support **Preview → Predict → Read → Confirm**. Slide titles should name concepts, decisions, or workflow stages so the deck is useful during a skim. The final summary slide should state the learner end state. Speaker notes explain why the idea matters and how it connects; they are not a second student guide or planning-chat residue.

**Words:** use established curriculum terminology. If a shop nickname is useful, define it in ordinary words on first use. Specification/outlining shorthand may remain in maintainer files, but translate it into learner language rather than copying its terse style.

**Stay in this lesson:** the outline note under this ID (or its unit) is the fence. Do not pull in the next child or another unit.

---

## 4. Teach at least the outline

- Outline knowledge bullets (`a`, `b`, `c`…) become the field/idea sections. None may be skipped.
- Outline tasks are taught as *what good looks like*, not as a lab (until the human asks for labs).
- Combined.md / role-matrix rows are the **qualification requirements** and IDs. Put them in the README map. Lesson coverage prepares the learner; observable performance and evaluator sign-off are governed separately by [qualification-demonstration-signoff-standard.md](qualification-demonstration-signoff-standard.md).
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
- [ebook/ebook-manuscript.md](../ebook/ebook-manuscript.md) — **rebuild the ebook** with [ebook/build_ebook.py](../ebook/build_ebook.py) when a student guide, subunit `intro.md`/`summary.md`, the story bible, or the companion story changes. The ebook is derived output: fix the canonical source and rebuild rather than surgical-editing the compiled manuscript. Instructor-only / slides-only / matrix-only changes normally skip this. The retired `exports/gemini-notebook/` tree is not rebuilt; use the complete ebook as the learner upload for NotebookLM/Gemini.

Do not set tracker status to human-accepted (`Complete` on the whole package). Use the per-artifact columns: student/instructor/slides complete, then tell the user it is ready to review.

---

## 6. Do not

- Generate a whole cluster when asked for one child (unless the human asked for those children together)
- Skip an outline bullet because the matrix row is shorter
- Invent matrix IDs, outline headings, or proficiency codes
- Collapse or invent 3/5/7 codes
- Invent local policy, tickets, field lists, approval chains, or PIR lists
- Add or strengthen an A12 fact inside a lesson without first changing [story-bible.md](story-bible.md); use the canonical/hypothetical/separate-example labels in [a12-scenario-governance-standard.md](a12-scenario-governance-standard.md)
- Treat a knowledge check or lesson-completion status as qualification sign-off for a Task (`T`) row
- Weaken a mapped task verb (for example, call planning an “executed hunt”) to make it fit a concept-only lesson
- Index sample IPs, `example.com`, or passing name-drops
- Copy shared frameworks into a role folder
- Mark the module human-accepted — stop for review
- Write Gate 1 proposal files unless asked
- Skip the learner **Why This Matters** / advance-organizer introduction or the instructor learning-arc context
- Invent Common Student Challenges to fill a quota, or leave a listed challenge as a label with no example
- Leave a slide without plain-language speaker notes
- Write student-facing text that only makes sense with a live instructor
- Say “this hour” when you mean this lesson
- Use unexplained SIEM slang (row, map, encoding) as the headline word for an idea
- Leave planning-chat residue (“You wanted…,” “Outline a. Stop.”)
- Use specification/checklist language as the learner-facing voice
- Use slogan fragments or repeated `X ≠ Y` / “This is not…” contrasts instead of explanatory reasoning
- Write a summary that merely repeats headings rather than checking the learner end state
- Jump ahead of what the human asked without saying why in Context
- Pad a short lesson, or add optional sections only to fill
- Copy a sibling’s table of contents, timing, or example set
- Write more than 3 knowledge-check questions for the lesson, or skip the 1–3 when the lesson has slides
- Write a new lab, demo, or hands-on exercise unless the human asked for one
- Skip the fluff review when you finish
- Use a shop nickname in the instructor guide or slides without the student-guide word or a one-line gloss
- Skip rebuilding the [ebook manuscript](../ebook/ebook-manuscript.md) when a learner-facing canonical source used by the ebook changed

---

## 7. When you finish

List the paths you wrote and the outline ↔ matrix map. Remind the reviewer to confirm: (1) every outline bullet/task is in the student guide, (2) stay-in-this-lesson notes were followed, (3) Concepts taught matches the index, (4) instructor context explains the learning arc, (5) the student introduction works as an advance organizer, (6) the summary works as an end-state check, (7) any challenges have examples or are omitted, (8) every slide has plain speaker notes, (9) **skim test done**, (10) **fluff review done**, (11) 1–3 knowledge-check questions for the lesson, (12) no new lab/demo unless asked, (13) student guide and slide faces stand alone, (14) status stays at review until the human accepts the lesson, and (15) the ebook is rebuilt when a learner-facing canonical source used by it changed.

**Skim test (required):** read only the introduction, headings, tables, emphasized concepts/callouts, and summary. Confirm that the learner can see the structure, important distinctions, and expected end state before reading the detailed prose. Use the full checklist in [skim-first-authoring-standard.md](skim-first-authoring-standard.md).

**Fluff review (required, you and the human):** For each extra example, table, slide, lab step, or question, say which outline bullet it serves. If you cannot, delete it.
