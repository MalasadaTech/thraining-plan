# A12 Scenario Governance Standard

**Status:** Governing course-maintenance decision  
**Applies to:** all A12 uses in Shared Foundations, SOC, CTI, Threat Hunting, Detection Engineering, companion-story sources, and derived publications.

## 1. Purpose

A12 is the recurring course case. It should help learners connect the role tracks without allowing an illustrative exercise to become a new case fact by accident.

This standard defines what counts as canonical A12, what counts as an A12-based practice extension, what counts as a separate classroom example, how facts are revealed through the course, and how new A12 facts are approved and propagated.

The governing principle is:

> **A lesson may simplify or extend an exercise, but it may not silently strengthen the canonical A12 evidence.**

## 2. Four scenario states

### A. Canonical A12 fact
A fact recorded in `docs/story-bible.md`.

### B. Canonical A12 assessment
A bounded analytic conclusion explicitly supported by the story bible. An assessment does not become a fact merely because it is repeated.

### C. Hypothetical A12 practice extension
A teaching exercise that begins from canonical A12 but adds supplied conditions that are **not** canonical facts.

Use this exact label prominently:

> **Scenario status: Hypothetical A12 practice extension — supplied exercise conditions are not additional canonical A12 facts.**

Added exercise conditions must never flow into the story bible, companion story, another role lesson, or a downstream handoff as if they actually occurred.

### D. Separate classroom example
A teaching example that is **not A12**.

When confusion is plausible, use:

> **Scenario status: Separate classroom example — not A12.**

Prefer distinct identifiers when A12 continuity is unnecessary. Do not call a separate example an “A12 classroom example.”

## 3. Canonical boundaries that remain locked

Until the story bible is intentionally changed:

- **PRD** is a vendor/tracking label, not independently established actor identity.
- A12 establishes **encoded PowerShell**, not a hidden PowerShell window unless separate supporting evidence is added.
- `/update.exe` is a **requested path / candidate payload name**.
- Successful transfer of `/update.exe` is unresolved.
- Creation of `%TEMP%\update.exe` from the HTTP request is unresolved.
- Execution of that file is unresolved.
- A literal file hash and a VirusTotal verdict are not published A12 facts.
- An existing ANY.RUN report may be searched by hash when available; a new detonation requires supported submission input.
- A12 reaches a **hunt package**; additional affected-host counts remain unspecified.
- A12 reaches a **Detection Engineering coverage review**; add/change/no-rule, deployment, and later lifecycle outcomes remain unspecified.
- A protective-control owner may receive candidate infrastructure for review; no completed block/monitor action is canonical.
- The A12 initial-access mechanism remains unresolved.

When a teaching need conflicts with one of these boundaries, create a hypothetical extension or separate example. Do not add evidence merely to preserve older wording.

## 4. Progressive disclosure decision

The course uses **spoiler-light progressive disclosure**.

A fact should first appear in the lesson where the learner is expected to interpret or operationally use that evidence.

Earlier orientations, shared-foundation lessons, and advance organizers may preview:
- the question the learner will eventually answer;
- the evidence class they will encounter;
- the role handoff;
- the fact that uncertainty exists.

They should not reveal detailed A12 observations that the story-bible timing map reserves for a later evidence lesson.

A summary may synthesize facts already introduced earlier in the reading order. It should not introduce a new canonical fact for the first time.

## 5. Practice-example design rules

When a lesson needs evidence not present in A12:

1. Decide whether A12 continuity materially helps the learning objective.
2. If yes, use the **Hypothetical A12 practice extension** label.
3. If no, use a **Separate classroom example** and change enough identifiers to prevent accidental blending.
4. State the evidence supplied by the exercise.
5. State the conclusion that evidence supports.
6. Do not import the exercise result into later A12 products unless the story bible is intentionally changed first.

Prefer a separate example when teaching successful file transfer/execution, sandbox behavior, confirmed actor identity, additional affected-host counts, completed detection deployment, or completed blocking/containment.

## 6. Cross-role handoff rule

A downstream role receives only:
- canonical facts already revealed in the reading order;
- canonical bounded assessments;
- explicitly supplied hypothetical conditions when the downstream lesson is part of the same labeled practice extension.

A downstream role does not inherit an unlabeled practice result merely because it appeared upstream.

## 7. Change control for a new A12 fact

When a new canonical fact is intentionally needed:

1. Add/change it in `docs/story-bible.md` first.
2. Define its evidence boundary and what it still does **not** establish.
3. Update the “How A12 facts enter the course” timing map.
4. Update the first lesson that introduces it.
5. Update later lessons that reuse it.
6. Update companion-story planning and finished story.
7. Rebuild the ebook.
8. Re-run A12 reconciliation/coherence checks.

Do not begin with a lesson edit and backfill the story bible later.

## 8. Reviewer test

Before accepting an A12 example, ask:

- Is every asserted fact in the story bible?
- If not, is the example clearly labeled hypothetical or separate?
- Does the conclusion stay within the supplied evidence?
- Is this fact being revealed at the correct point in the course?
- Could a learner carry this practice-only fact into another role as though it happened?
- If the example changes a canonical outcome, was the story bible changed first?

## 9. Relationship to the story bible

`docs/story-bible.md` remains the **fact ledger**.

This standard governs **how the curriculum uses that ledger**.

When the two disagree, reconcile them deliberately before publication.
