# Generate a module (AI instructions)

Use this file when asked to generate module content for an **existing** teaching-unit ID (Gate 2). Humans follow [contributing.md](contributing.md). You follow this file.

This is a procedure. Clone the sibling module. Do not invent requirements, IDs, or a new voice.

**Caller prompt (either tool):**  
`Follow docs/generate-module.md and generate teaching-unit <ID> (<Title>) for me to review. Do not invent IDs.`

---

## 0. Preconditions

Stop and say what is missing if any of these fail:

- The teaching-unit ID already exists as a heading or `#` prefix on the [combined matrix](matrices/combined.md) (for example `1.2.5`, `2.1`, `3.1`).
- You were given that ID, not a vague topic and not an old display number (`section 7`, `section 8`).
- Gate 1 is done. You are not proposing a new matrix row.

**Assign work by ID prefix:** `1.x` = SOC (`modules/01-soc/`), `2.x` = Hunt (`modules/02-hunter/`), `3.x` = CTI (`modules/03-cti/`).

**IDs and ratings come from the matrix. Content floor is the outline.** Combined.md headings match [soc.md](matrices/soc.md) / [hunter.md](matrices/hunter.md) / [cti.md](matrices/cti.md). Teach at least every outline `a/b/c` and task for this unit. Expand only to support that syllabus. Do not invent a new matrix obligation.

**CTI `3.1`:** matrix `3.1` is the teaching-unit ID (PIRs / direction). Outline `3.1` is Core Intelligence Concepts (lifecycle, types, requirements, actionable, audience, attribution, …). Until the board splits it, generate **one** module `3.1` that covers **all** of outline `3.1`. Do not teach PIRs only.

If the user wants a **new** requirement, stop and point them at [templates/requirement-proposal.md](../templates/requirement-proposal.md).

---

## 1. Read, in this order

1. The [training-outlines.md](outlines/training-outlines.md) block for this unit — every `a/b/c` and numbered task (the content floor).
2. The [combined.md](matrices/combined.md) heading for this teaching-unit ID and every row under it (IDs, roles, codes).
3. The matching role matrix (`soc.md` / `hunter.md` / `cti.md`).
4. [proficiency-legend.md](proficiency-legend.md)
5. [contributing.md](contributing.md) Gate 2
6. [templates/student-guide.md](../templates/student-guide.md), [instructor-guide.md](../templates/instructor-guide.md), [slides.md](../templates/slides.md)
7. The **previous sibling module** in the same unit — full `README.md`, `student-guide.md`, `instructor-guide.md`, `slides.md`

Sibling for the current Zeek series: `1.2.4` at `modules/01-soc/02-zeek/04-tls-engine/`. For a first Hunt or CTI module, clone TLS for package shape only (not content). Use the latest written sibling in that prefix if one exists.

Also open [concept-index.md](concept-index.md) and [tracker.csv](tracker.csv) before you write.

---

## 2. Resolve IDs (do not invent)

| You need | Where it comes from |
|----------|---------------------|
| Teaching-unit ID | Combined.md heading / tracker (examples: `1.2.5`, `2.1`, `3.1`) |
| Matrix item IDs | Combined matrix `#` column as written. SOC is often four parts (`1.2.5.1`). Hunt and CTI are often three (`2.1.1`, `3.1.2`). Do not add a `.1` to force four parts. |
| Outline block | Syllabus for this unit. SOC/Hunt usually share the prefix. For CTI `3.1`, use **all** of outline `3.1`, not only outline `3.1.4`. |
| Folder | `modules/<role>/<unit>/<nn-short-name>/` |
| Roles | Module primary/secondary from outline + matrix |

Record the outline ↔ matrix map in the module `README.md`, same table shape as TLS.

If Gate 1 said “add to an existing module,” amend that folder. Do not create a new one.

---

## 3. Clone this shape

Match the sibling. Typical engine module:

| Artifact | Shape |
|----------|--------|
| Time | 60–75 minutes (~72 in the timing table) |
| Audience | Primary + secondary roles from the matrix |
| Student guide | Objectives → key concepts (fields + 1–2 idea sections) → 3 walkthrough examples → hands-on exercise → 5 knowledge-check questions → summary → references |
| Instructor guide | Purpose, teaching points, pitfalls, timing, notes per section, exercise key (pseudo-queries), knowledge-check answers |
| Slides | ~17 slides: title, objectives, agenda, concepts, 3 examples, `uid` pivot if network logs, hunts, exercise, check, summary, next steps, optional quick-reference |
| Answers | Only in the instructor guide. No standalone `answer-key.md`. No quiz. |

Exercise pattern (engine modules): one-sentence summary of each example; two SIEM-style **pseudo-queries**; explain the `uid` pivot when the log has a `uid`.

Examples: one normal, two leads. Leads are not automatic incidents.

Voice: direct, instructional, short paragraphs, tables for fields. Do not lecture about decrypting traffic, writing Zeek scripts, or other later modules.

---

## 4. Teach at least the outline

- Outline knowledge bullets (`a`, `b`, `c`…) become the field/idea sections. None may be skipped.
- Outline tasks become the analysis exercise and the two pseudo-queries (or equivalent practice).
- Combined.md / role-matrix rows are the **sign-off** items and IDs. Put them in the README map.
- Expansion is allowed when it supports the outline (Zeek `uid` / `ts`, extra examples). New obligations need Gate 1.
- If an outline bullet has no home in this teaching-unit, **stop** and say so. Do not drop it.
- Stay out of the *next* unit’s topic. Point to it under Related modules.

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

- [concept-index.md](concept-index.md) — every README concept; **Taught** here; **Used** on this module for terms taught earlier (`uid`, `conn` log, …); aliases people will search; link the folder, not a line number
- [tracker.csv](tracker.csv) — add or update the row; guides/slides `Complete`; exercise/quiz as in the sibling (usually exercise `Not Started`, answer key `Complete` if answers are in the instructor guide)
- [tracker.md](tracker.md) — folder map row if this ID is new
- README numbering table in the repo root if this ID is new

Do not set tracker status to `Complete` for the module as a whole if that column exists as a single status — leave content at **Review** for the human. Use the per-artifact columns like the Zeek rows: student/instructor/slides complete, then tell the user it is ready to review.

---

## 6. Do not

- Skip an outline bullet because the matrix row is shorter
- Invent matrix IDs, outline headings, or proficiency codes
- Treat combined.md `## 7` / `## 8` / `## 9` as real (those headings are gone; use `2.x` / `3.x` / `1.8`)
- Index sample IPs, `example.com`, or passing name-drops
- Put JA3-style depth in a survey module, or HTTP bodies in a TLS module
- Copy shared frameworks into a role folder
- Mark the module human-accepted (`Complete` on the whole package) — stop for review
- Write Gate 1 proposal files unless asked

---

## 7. When you finish

List the paths you wrote and the outline ↔ matrix map. Remind the reviewer to confirm: (1) every outline bullet/task is in the student guide, (2) Concepts taught matches the index, (3) status stays at review until they accept the lesson.
