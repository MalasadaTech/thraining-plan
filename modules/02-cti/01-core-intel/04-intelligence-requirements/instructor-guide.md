# Instructor Guide – Module 3.1.4 – Intelligence Requirements

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.1.4 A / A / B · 3.1.4.1 1a / 1a / 1a · 3.1.4.2 1a / 1a / 1a · 3.1.4.3 1a / 1a / 1a  
- Hunter: 3.1.4 A / B / B · 3.1.4.1 1a / 2b / 3c · 3.1.4.2 1a / 2b / 3c · 3.1.4.3 1a / 2b / 3c  
- CTI: 3.1.4 B / C / C · 3.1.4.1 3c / 4c / 4d · 3.1.4.2 3c / 4c / 4d · 3.1.4.3 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach purpose, PIR vs IR, and force **write / translate / trace**. Do not open the actionable checklist or source-class plan.

**Key Teaching Points:**
- Classroom line is a stand-in. Overlay site PIR IDs if you have them.
- “Everything on APTs” is the usual fail — task 2 is the rewrite.
- Drive work includes what you will **not** chase.
- SOC 3-level tasks are **1a**. Hunter 3-level is **1a**. CTI 3-level is already **3c**. Do not collapse those.

**Common Student Challenges:**
- Defining PIR and never writing one.
- Leaving “are we safe?” untranslated.
- Collecting blogs against an internal-presence PIR.
- Opening 3.1.5 / 3.1.8 / 3.12.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional local PIR list
- Answer key (this guide)

---

## Learning Objectives

1. Purpose + PIR vs IR.
2. Develop or refine.
3. Translate a messy ask.
4. Trace how it drives work.

**Mapped Items:** K 3.1.4 · T 3.1.4.1 · T 3.1.4.2 · T 3.1.4.3

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 3.1.5 / 3.1.8 / 3.12 |
| Purpose, PIR, drive            | 14 min   | a–c |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Three tasks |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~64 min** | Stretch Ex 2 if they accept “APTs” |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they should *write* a line, not recite a definition.
- Type (3.1.3) is a field on the line, not this lesson’s classify drill.

**Question:**  
“If the PIR is internal presence this week, is a vendor APT blog *collection* or a *distraction*?” (Distraction unless it changes the *question*.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail untranslated “are we safe?” Fail blogs-only against an internal PIR.

**Summaries:**
- Ex 1: usable tactical PIR; drives internal query.
- Ex 2: must translate; original is not a requirement.
- Ex 3: PIR good; work did not follow it.

**Cases:**

| Item | Requirement (accept paraphrase) | Drives | Reject |
|------|--------------------------------|--------|--------|
| A | Hunt lead \| Night Owl 10-day series vs scanner FP pile \| this window \| where hunt time goes \| **Operational** | Scope hunt; do not write a board paper | “Hunt everything” |
| B | **Must translate.** e.g. Leadership \| Does Night Owl change extra TLS spend this quarter? \| **Strategic** | Posture evidence, not a host list | Leaving “are we safe?” |
| C | SOC \| If WS-JLEE is Night Owl, isolate tonight? \| **Tactical** | Host evidence + IR concurrence (**1.8.5**) | Nation-state essay |
| D | Not a PIR — no decision. Refine or reject | — | “Collect all OSINT on ransomware” as PIR-7 |

---

## Knowledge Check – Answer Key

1. **What problem does a requirement prevent?**  
   **Answer:** Collection and analysis that do not support a decision (“everything interesting”).  
   **Explanation:** Outline a.

2. **PIR vs IR?**  
   **Answer:** A PIR is an IR that leadership or the program **ranked**. Not every IR is a PIR.  
   **Explanation:** Outline b.

3. **Why not “tell me about APTs”?**  
   **Answer:** No decision, window, or “what would change.” Translate it (task 2).  
   **Explanation:** Example 2.

4. **What does Ex 1 stop you collecting?**  
   **Answer:** Nation-state papers and unrelated APT blogs. The question is internal presence this week.  
   **Explanation:** Outline c / task 3.

5. **Standing local PIRs?**  
   **Answer:** **3.12.1**, not this classroom line.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Local PIR list
- Next recommended module: 3.1.5 Ensuring intelligence is actionable
