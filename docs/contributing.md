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
- For any new or changed **Task (`T`)** row, identify how the task will be **demonstrated** for qualification using [qualification-demonstration-signoff-standard.md](qualification-demonstration-signoff-standard.md); do not assume lesson completion is sign-off
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

The module must cover **every** outline knowledge bullet and task that belongs to this teaching unit. For Task (`T`) rows, preserve the matrix verb and distinguish **instruction/preparation** from the separate performance demonstration defined in [qualification-demonstration-signoff-standard.md](qualification-demonstration-signoff-standard.md). The current demonstration crosswalk is [qualification-evidence-map.md](qualification-evidence-map.md). Those items go in the student guide and in **Concepts taught**. Follow the outline’s **stay-in-this-lesson** note for that ID.

When a lesson uses the recurring A12 case, follow [A12 Scenario Governance Standard](a12-scenario-governance-standard.md). Canonical facts come from the story bible; added exercise conditions must be explicitly hypothetical or separate rather than silently becoming A12 facts. How to write the files is [generate-module.md](generate-module.md).

Length follows the outline, not a clock. **Do not add optional content to fill.** If a section is marked optional and this lesson does not need it, omit it.

**Knowledge check is required: 1–3 questions per lesson** that has slides. Not per concept. Not more than 3.

**No new labs, demos, or hands-on exercises** until we decide to add them (after the concept baseline). Outline **tasks stay** — teach what the task is. Existing labs stay until that section is reviewed.

Expansion is allowed when it supports the outline (examples, `uid`, extra context). A new *requirement* (something an analyst must now be signed off on) still goes through Gate 1.

If an outline bullet has no obvious home in this unit, stop and map it. Do not drop it.

### Required

- [ ] Module folder (new modules only): `modules/<role>/<unit>/<nn-short-name>/`
- [ ] `README.md` — mapped matrix IDs, outline headings, roles, time, **Concepts taught**
- [ ] `student-guide.md` from [templates/student-guide.md](../templates/student-guide.md). Its **Why This Matters** opening functions as an advance organizer: activate useful prior knowledge, preview the main ideas and distinctions, and make the expected end state visible. A reader with no live instructor must still understand it.
- [ ] `instructor-guide.md` from [templates/instructor-guide.md](../templates/instructor-guide.md). Its context explains the learning arc: prior knowledge, the capability developed here, and where the learner goes next. Notes must be usable by a substitute and should not compensate for explanations missing from the learner material. **Common Student Challenges** remains optional and should include only real, concrete misunderstandings.
- [ ] `slides.md` from [templates/slides.md](../templates/slides.md). The deck supports **Preview → Predict → Read → Confirm**. Slide titles expose the learning structure during a skim; the opening establishes why the lesson matters and the closing states what the learner should now be able to do. Every slide has plain-language speaker notes.
- [ ] [concept-index.md](concept-index.md) — Taught vs Used, aliases, roles; same terms as the README Concepts list
- [ ] [tracker.csv](tracker.csv) — move the row to `Review`, then `Complete` when accepted
- [ ] Review: every outline bullet/task for this unit is in the student guide; Concepts taught matches the index; the learner introduction works as an advance organizer; the summary works as an end-state check; instructor context explains the learning arc; any challenges have examples; slide notes are plain language; student guide and slide faces stand alone.
- [ ] Review: names match the outline and student guide. A shop nickname (e.g. “bulletin”) is either the same word the student already has, or it is defined on first use in ordinary words. Do not leave the instructor saying a word the student guide never explained.
- [ ] **Skim test (required):** read only the introduction, headings, tables, emphasized concepts/callouts, and summary. Confirm that the learner can see the structure, important distinctions, and expected end state before the detailed read. See [skim-first-authoring-standard.md](skim-first-authoring-standard.md).
- [ ] **Fluff review (required):** hunt for content that is only there to fill. Cut examples, slides, tables, labs, or extra questions that do not teach a new outline fact. If you cannot say what outline bullet a piece serves, remove it.
- [ ] **Ebook rebuild:** if this change touches a **student-guide**, a subunit **`intro.md` / `summary.md`**, the **story bible**, or the **companion story**, rebuild [ebook/ebook-manuscript.md](../ebook/ebook-manuscript.md) with [ebook/build_ebook.py](../ebook/build_ebook.py). Fix source content in the canonical files and rebuild rather than editing the compiled manuscript directly. Instructor-only, slides-only, and matrix-only changes normally skip this.

### Subunit introduction and summary wrappers

A meaningful multi-lesson grouping may have `intro.md` and `summary.md` directly in the subunit directory. These wrappers are synthesis/navigation content and **do not create new matrix requirements**. Use [templates/subunit-intro.md](../templates/subunit-intro.md) and [templates/subunit-summary.md](../templates/subunit-summary.md), and apply the instructional-hierarchy rule in [skim-first-authoring-standard.md](skim-first-authoring-standard.md).

### Optional / later

- `assets/` for lesson-specific screenshots
- Reusable logs or PCAP in `labs/`
- Standalone `answer-key.md` (not required; answers live in the instructor guide)
- Quiz (tracker column exists; not part of sign-off yet)
- “Related modules” / next-steps links in sibling guides

Front door and shared lessons live under `modules/00-intro/` and are taught before SOC: `0.1`–`0.9`, followed by the `0.10` section summary. The SOC instructional units run through `1.5`, followed by the `1.6` section summary. Shared lessons should not be copied into each role. **Retired:** `1.7`, `1.8.2`–`1.8.5`.

### Concept index rules

- Index **taught** concepts, not every string in a sample log.
- **Taught** = this module created the obligation.
- **Used** = they saw it again; not where they first owed the knowledge.
- Point at the module folder, not a line number.
- Add the README Concepts list and the index entry in the same change.

---

## After content is accepted

Already-signed-off analysts follow the delta plan from the approved proposal. Adding a matrix row without that plan means “fully trained” is no longer true.
