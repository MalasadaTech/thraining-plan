# Instructor Guide – Module 2.6.3 – Hunt for a Specific Persistence or Privilege-Escalation Technique

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.6.3 3c / 4c / 4d  
- SOC: 2.6.3 1a / 1a / 2b  
- CTI: 2.6.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Turn a technique they can already **recognize** into a **scoped hunt** for that named method. Fail tactic sweeps and wrong-class hunts.

**Key Teaching Points:**
- Hunter task is **3c / 4c / 4d**. 4d = why *this* pattern is testable and the tactic sweep is not.
- SOC/CTI stay **1a / 1a / 2b** — they should see a named hunt vs a slogan.
- Recognition is done (**2.6.1** / **2.6.2**). Do not re-run those cards.
- Park **2.2.1** execute-all-types, **2.5** remap, **2.7** local ticket.

**Common Student Challenges:**
- “Hunt persistence” as the product.
- Hunting privesc off the SYSTEM task.
- Rewriting the 2.2.2 card instead of a hunt line.
- Opening a fake Harbor hunt ticket.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Named technique → scoped hunt.
2. Unique pattern.
3. Reject unbounded and wrong-class.

**Mapped Items:** T 2.6.3

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not recognition; not 2.7 |
| Hunt line                      | 14 min   | Named + pattern + scope |
| Walkthrough Examples           | 14 min   | Students write first |
| Hands-On Exercise              | 18 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep the tactic |

---

## Detailed Teaching Notes

**Talking Points:**
- Hold the Run-key row from **2.6.1**. Ask: “What would you *search for* next week, not what did you *see*?”
- 4d is the unique pattern (`Updater` + `%TEMP%\update.exe`), not a second ATT&CK column.
- The SYSTEM task is a persistence hunt if they name the task. It is never a privesc hunt on *this* card.

**Question:**  
“What would make ‘hunt persistence’ legal on this card?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail B (tactic). Fail D (wrong class). Fail E (**2.7**). Accept A and C as two legal hunts. Product is one of them.

**Hunt lines:**

| Item | Result |
|------|--------|
| A | **Hunt** Run `Updater` / `%TEMP%\update.exe` — persist |
| B | **Reject** — unbounded tactic |
| C | **Hunt** user → SYSTEM token theft — privesc |
| D | **Reject** — task is persist, not privesc |
| E | **Refuse** — **2.7** |

---

## Knowledge Check – Answer Key

1. **What must be named?**  
   **Answer:** One persistence or privilege-escalation **method**, not the tactic.  
   **Explanation:** Outline task 3.

2. **Hunt line besides the name?**  
   **Answer:** Class, unique pattern, scope, query idea, why not the whole tactic.  
   **Explanation:** Product.

3. **Why not “hunt persistence”?**  
   **Answer:** No unique pattern. It is a tactic sweep.  
   **Explanation:** Example 2.

4. **Why not privesc on the SYSTEM task?**  
   **Answer:** No elevation. That row is persistence (**2.6.1**).  
   **Explanation:** Example 3.

5. **Local process?**  
   **Answer:** **2.7**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Classroom facts (student guide)
- Next recommended module: 2.7.1 Hunt control and lead management
