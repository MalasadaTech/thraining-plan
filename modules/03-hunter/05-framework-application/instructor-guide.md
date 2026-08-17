# Instructor Guide – Module 3.5.1 – Using MITRE ATT&CK for Hunt Planning

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 3c / 4c / 4d  
- SOC: 3.5.1 A / B / B ; 3.5.1.1–3.5.1.2 1a / 2b / 3c ; 3.5.1.3 1a / 1a / 2b  
- CTI: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Map this hunt. Name detection vs visibility gaps. Use ATT&CK to support priority.

**Context (plain language):**

- What this hour is for: Hunters put *this* hunt on the ATT&CK map so they can see holes and rank work.
- How it hooks to the hour before: 3.4.3 seeded leads from STIX.
- How it hooks to the hour after: 3.6.1 is how persistence looks in a log.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c + three tasks. Not 0.6.1 redo. Not 2.7.1.
- What we are *not* doing this hour: Whole-enterprise Navigator layer. Scoring model. Technique how-to (**3.6**). No lab.
- Extra step: none.

**Key Teaching Points:**
- Copied ID ≠ map.
- Do not hunt a visibility gap.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 3.5.1 ; T 3.5.1.1–3.5.1.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | This hunt, not the matrix |
| Key Concepts            | 12 min    | Map + two gaps + A12 |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write map vs copy. Walk detection vs visibility. Walk A12 T1547.001.

If they shade every Persistence cell: “This hunt only.”  
If they invent an ID: “Don’t. Name the method or say unknown.”

---

## Knowledge Check – Answer Key

1. **Copying T1547.001 is coverage analysis. True or false?**  
   **Answer:** False. That is a label from 3.4.2.  
   **Explanation:** Outline a.

2. **Detection vs visibility gap?**  
   **Answer:** Detection: you can see it, no analytic. Visibility: you cannot see it.  
   **Explanation:** Outline b.

3. **A12 map + gap?**  
   **Answer:** TA0003 / T1547.001. Registry logs exist + no analytic = **detection gap**.  
   **Explanation:** Tasks 1–2.

---

## Additional Instructor Resources

- Next: 3.6.1 Persistence techniques
