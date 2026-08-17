# Adding or changing a requirement

Two gates. The board approves the **requirement** first. Content is written only after that.

Do not write a full module and then ask to put it on the matrix.

| File | Job |
|------|-----|
| [training-outlines.md](outlines/training-outlines.md) | Syllabus. Every `a/b/c` and numbered task is the **floor** of the lesson. |
| Combined / role matrices | Contract. Item IDs, roles, and 3/5/7 codes. |
| Module | Teaches the outline (and may expand). Does not invent a new obligation. |

Use [templates/requirement-proposal.md](../templates/requirement-proposal.md) for Gate 1. Open it as an issue or a pull request.

---

## Gate 1 — Propose the requirement

A 7-level (or equivalent) proposes the change. The review board approves or rejects the **matrix** change.

### Required in the proposal

- Concept or topic in one sentence
- Why it is required now (gap, incident, tool change, inspection finding)
- Roles and 3/5/7 codes (`A/B/C`, `2b/3c/4c`, or `—`) — see [proficiency-legend.md](proficiency-legend.md)
- **New module** vs **add to an existing module**
- Suggested teaching-unit ID and outline headings, or “assign on approval”
- Shared (`modules/00-intro/`) vs role-specific
- What already-signed-off analysts must do (delta lesson, brief, or next recert)

### On approval, update these files before any guides

- [outlines/training-outlines.md](outlines/training-outlines.md)
- [matrices/combined.md](matrices/combined.md) and the affected role matrices
- [tracker.csv](tracker.csv) — new or extended module row, status `Not Started`
- [tracker.md](tracker.md) folder map, if a new module ID was issued

IDs follow the [README numbering rules](../README.md#numbering). Teaching-unit IDs are canonical. Do not reuse an outline K/T heading as a module folder name.

No student guide, instructor guide, or slides at this gate.

---

## Gate 2 — Build the lesson

Only after Gate 1. If Gate 1 said “add to an existing module,” amend that module. Do not create a new folder.

### Coverage (required)

The module must cover **every** outline knowledge bullet and task that belongs to this teaching unit. Those items go in the student guide and in **Concepts taught**. Follow the outline’s **stay-in-this-lesson** note for that ID. How to write the files is [generate-module.md](generate-module.md).

Length follows the outline, not a clock. **Do not add optional content to fill.** If a section is marked optional and this lesson does not need it, omit it.

**Knowledge check is required: 1–3 questions per lesson** that has slides. Not per concept. Not more than 3.

**No new labs, demos, or hands-on exercises** until we decide to add them (after the concept baseline). Outline **tasks stay** — teach what the task is. Existing labs stay until that section is reviewed.

Expansion is allowed when it supports the outline (examples, `uid`, extra context). A new *requirement* (something an analyst must now be signed off on) still goes through Gate 1.

If an outline bullet has no obvious home in this unit, stop and map it. Do not drop it.

### Required

- [ ] Module folder (new modules only): `modules/<role>/<unit>/<nn-short-name>/`
- [ ] `README.md` — mapped matrix IDs, outline headings, roles, time, **Concepts taught**
- [ ] `student-guide.md` from [templates/student-guide.md](../templates/student-guide.md). Must have an **Intro** as the first paragraph of Key Concepts: why this hour exists in the job, in ordinary words. Not only “last hour was X.”
- [ ] `instructor-guide.md` from [templates/instructor-guide.md](../templates/instructor-guide.md). Must have **Context (plain language)** as one block at the top of the overview. “What this hour is for” must match the student Intro. **Common Student Challenges** is optional. If you list any, each bullet needs a short why and one example. Do not invent challenges to fill a quota. Do not add a new lab or demo unless asked.
- [ ] `slides.md` from [templates/slides.md](../templates/slides.md). On-slide text stays short and readable without extra briefing. Every slide has **Speaker Notes** in plain language (why this slide, how it connects — not a recap of the bullets).
- [ ] [concept-index.md](concept-index.md) — Taught vs Used, aliases, roles; same terms as the README Concepts list
- [ ] [tracker.csv](tracker.csv) — move the row to `Review`, then `Complete` when accepted
- [ ] Review: every outline bullet/task for this unit is in the student guide; Concepts taught matches the index; Context is present; student Intro is present; any challenges have examples; slide notes are plain language
- [ ] Review: names match the outline and student guide. A shop nickname (e.g. “bulletin”) is either the same word the student already has, or it is defined on first use in ordinary words. Do not leave the instructor saying a word the student guide never explained.
- [ ] **Fluff review (required):** hunt for content that is only there to fill. Cut examples, slides, tables, labs, or extra questions that do not teach a new outline fact. If you cannot say what outline bullet a piece serves, remove it.

### Optional / later

- `assets/` for lesson-specific screenshots
- Reusable logs or PCAP in `labs/`
- Standalone `answer-key.md` (not required; answers live in the instructor guide)
- Quiz (tracker column exists; not part of sign-off yet)
- “Related modules” / next-steps links in sibling guides

Front door and shared hours live under `modules/00-intro/` and are taught before SOC: `0.1`–`0.5`, `0.6`, `3.3.2`, `1.8.1`. SOC ends at `1.5`. Do not copy those lessons into each role. **Retired:** `1.7`, `1.8.2`–`1.8.5`.

### Concept index rules

- Index **taught** concepts, not every string in a sample log.
- **Taught** = this module created the obligation.
- **Used** = they saw it again; not where they first owed the knowledge.
- Point at the module folder, not a line number.
- Add the README Concepts list and the index entry in the same change.

---

## After content is accepted

Already-signed-off analysts follow the delta plan from the approved proposal. Adding a matrix row without that plan means “fully trained” is no longer true.
