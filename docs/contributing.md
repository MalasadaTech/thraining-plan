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
- Shared (`modules/shared/`) vs role-specific
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

The module must cover **every** outline knowledge bullet and task that belongs to this teaching unit. Those items go in the student guide and in **Concepts taught**.

Expansion is allowed when it supports the outline (examples, `uid`, extra context). A new *requirement* (something an analyst must now be signed off on) still goes through Gate 1.

If an outline bullet has no obvious home in this unit, stop and map it. Do not drop it.

### Required

- [ ] Module folder (new modules only): `modules/<role>/<unit>/<nn-short-name>/`
- [ ] `README.md` — mapped matrix IDs, outline headings, roles, time, **Concepts taught**
- [ ] `student-guide.md` from [templates/student-guide.md](../templates/student-guide.md)
- [ ] `instructor-guide.md` from [templates/instructor-guide.md](../templates/instructor-guide.md) (include the exercise answer key here)
- [ ] `slides.md` from [templates/slides.md](../templates/slides.md)
- [ ] [concept-index.md](concept-index.md) — Taught vs Used, aliases, roles; same terms as the README Concepts list
- [ ] [tracker.csv](tracker.csv) — move the row to `Review`, then `Complete` when accepted
- [ ] Review: every outline bullet/task for this unit is in the student guide; Concepts taught matches the index

### Optional / later

- `assets/` for lesson-specific screenshots
- Reusable logs or PCAP in `labs/`
- Standalone `answer-key.md` (not required; answers live in the instructor guide)
- Quiz (tracker column exists; not part of sign-off yet)
- “Related modules” / next-steps links in sibling guides

Shared topics go under `modules/shared/`, not copied into each role.

### Concept index rules

- Index **taught** concepts, not every string in a sample log.
- **Taught** = this module created the obligation.
- **Used** = they saw it again; not where they first owed the knowledge.
- Point at the module folder, not a line number.
- Add the README Concepts list and the index entry in the same change.

---

## After content is accepted

Already-signed-off analysts follow the delta plan from the approved proposal. Adding a matrix row without that plan means “fully trained” is no longer true.
