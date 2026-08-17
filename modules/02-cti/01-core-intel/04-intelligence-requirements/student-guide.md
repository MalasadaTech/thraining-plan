# Module 3.1.4 – Intelligence Requirements

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.1.4 A / A / B · 3.1.4.1 1a / 1a / 1a · 3.1.4.2 1a / 1a / 1a · 3.1.4.3 1a / 1a / 1a  
- Hunter: 3.1.4 A / B / B · 3.1.4.1 1a / 2b / 3c · 3.1.4.2 1a / 2b / 3c · 3.1.4.3 1a / 2b / 3c  
- CTI: 3.1.4 B / C / C · 3.1.4.1 3c / 4c / 4d · 3.1.4.2 3c / 4c / 4d · 3.1.4.3 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain **why** intelligence requirements exist and what a **PIR** is.
2. **Develop or refine** a basic requirement.
3. **Translate** a messy stakeholder question into a clear requirement.
4. Explain **how** a given requirement drives collection and analysis.

**Mapped Proficiency Items:**
- K: 3.1.4 – Intelligence requirements and PIRs
- T: 3.1.4.1 – Develop or refine intelligence requirements
- T: 3.1.4.2 – Translate stakeholder questions into clear intelligence requirements
- T: 3.1.4.3 – Explain how a given requirement drives analytic work

---

## 1. Key Concepts

A requirement is the **question the work exists to answer**. Types (**3.1.3**) name the *kind* of answer. This hour is the *question*. Actionable criteria are **3.1.5**. Local standing PIRs are **3.12.1**.

**Classroom requirement line (this lesson only):**

`decision-maker | question | time window | what would change if we knew | type (from 3.1.3)`

| Piece | Outline | Meaning |
|-------|---------|---------|
| **Purpose** | a | Focus collection and analysis on a decision, not “everything interesting” |
| **PIR / types of requirements** | b | A **PIR** is a *priority* requirement — leadership or the program ranked it. Standing IRs and ad-hoc IRs are still requirements; they are not all PIRs |
| **Drives work** | c | The requirement names what you collect, what you analyze, and what you will *not* chase |

If your site publishes a PIR list, use those IDs. The obligation is **clear question + drive work**, not this template.

| This lesson | Other |
|-------------|-------|
| Write / refine the question | Classify the *type* — **3.1.3** |
| How the question drives *this* analysis | Which *source class* (OSINT / commercial / internal) — **3.1.8** |
| Not the local standing list / ticket | **3.12** |
| Not “is the product actionable?” | **3.1.5** |

The tasks extend the K: you **write**, **translate**, and **trace work** — you do not only define “PIR.”

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| “Are we seeing Night Owl SNI internally this week?” + what you will query | “Tell me about APTs” left as-is |
| Translate “are we good?” into a yes/no decision question | Collecting random blogs with no link to the question |
| Name what the PIR *stops* you from doing | Shipping a hash dump because a PIR exists somewhere |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Draft a Usable PIR (Expected)

**Stakeholder:** SOC lead. “Are we seeing that Night Owl fake-update thing?”

**Requirement line:**  
SOC lead | Are we seeing `nightowl-updates.net` / JA3 `a0e9f5…` on Harbor hosts **this week**? | 7 days | If yes → Sev2 IR path on those hosts; if no → no fleet isolate | **Tactical** (technical layer)

**Drives:** Internal Zeek/SIEM for that SNI/JA3 (collection). Analyze hits vs scanner/FP (**1.4.3**). Do **not** write a nation-state paper.

### Example 2: “Tell Me About APTs” (Lead)

**Stakeholder:** “I need everything on APTs for the board Friday.”

**Not a requirement yet.** No decision, no window, no “what would change.”  
**Translate:** Leadership | Does the Night Owl *cluster* change whether we fund extra TLS sensors **this quarter**? | this quarter | fund / defer | **Strategic**  
**Lead:** Do not accept the original as 3.1.4.1. Task 2 is the rewrite.

### Example 3: Good PIR, Random Collection (Lead)

**Requirement:** Example 1 (Night Owl this week).  
**Work shipped:** Three vendor blogs on “APT of the week,” no internal query.

**Drive test fails.** The PIR required *internal presence*. Blogs can *inform* a strategic question; they do not answer this one.  
**Lead:** The PIR was fine. The *work* did not follow it (task 3).

---

## 3. Hands-On Exercise

**Objective:** Write, translate, and trace.

**Instructions:**

1. One sentence each for Examples 1–3: requirement vs what failed.
2. For each item, write the **requirement line** and **what work it drives** (collect / analyze / do not chase).

   - A. Hunt lead: “Should we spend the next ten days on Night Owl or on the scanner FP pile?”
   - B. Executive: “Are we safe?”
   - C. SOC: “If `WS-JLEE` is Night Owl, what do I do tonight?”
   - D. Someone files PIR-7 as “collect all OSINT on ransomware” with no decision.

3. Do not evaluate actionability (**3.1.5**). Do not pick OSINT vs TIP as the *lesson* (**3.1.8** — you may *name* internal vs public as what the question drives).
4. If B is unusable until translated, say so and write the translation.

**Expected Outcome:**
- Three example summaries
- Four requirement lines + drive notes
- No actionable checklist, no 3.11 product

---

## 4. Knowledge Check

1. What problem does a requirement prevent?
2. What makes a requirement a **PIR** vs just an IR?
3. Why is “tell me about APTs” not a requirement yet?
4. How does Example 1’s PIR change what you **do not** collect?
5. Where do **standing local** PIRs live in this syllabus?

---

## 5. Summary

- Requirement = the decision question. PIR = a ranked one.
- Write it, translate the messy ask, trace the work.
- Next: whether the *product* is actionable (**3.1.5**).

---

## 6. References & Further Reading

- Related modules:
  - 3.1.3 – Intelligence types (previous)
  - 3.1.5 – Ensuring intelligence is actionable (next)
  - 3.1.8 – Collection sources and methods
  - 3.12.1 – Local intelligence requirements
- Local PIR list (optional — substitutes classroom lines)
