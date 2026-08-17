# Instructor Guide – Module 3.4.2 – Extracting Hunt Leads from CTI

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.2 B / C / C ; 3.4.2.1–3.4.2.3 3c / 4c / 4d  
- SOC: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
- CTI: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Keep searchable TTPs and artifacts. Drop noise. State one hunt question.

**Context (plain language):**

- What this hour is for: After the gate, hunters pull only what they can search internally.
- How it hooks to the hour before: 3.4.1 labeled hunt / don’t hunt / hand off.
- How it hooks to the hour after: 3.4.3 reads the same leftovers in STIX.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c + three extract tasks. Not 3.5.
- What we are *not* doing this hour: Navigator. Full four-field card unless the question needs a scope hook. No lab.
- Extra step: none.

**Key Teaching Points:**
- Appendix dump is not extract.
- Question must be able to fail.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 3.4.2 ; T 3.4.2.1–3.4.2.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | After the gate |
| Key Concepts            | 12 min    | Keep / drop / A12 question |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write TTP / IOC / behavior. Walk the drop list. Walk the A12 keep + question.

If they invent T1547.001 the report never printed: “Record only if given. Map is 3.5.”  
If they write the full card: “3.2.2.”

---

## Knowledge Check – Answer Key

1. **Copying the appendix is extract. True or false?**  
   **Answer:** False.  
   **Explanation:** Outline a–b.

2. **One reason to drop?**  
   **Answer:** No telemetry, expired IOC, or noise (any one).  
   **Explanation:** Outline b.

3. **A12 keep + question?**  
   **Answer:** TTP: Run **`Updater`**. Artifact: `:8080` `/update.exe` (or more `invoice.vbs`). Question: if more persistors exist, we see those.  
   **Explanation:** Tasks 1–3 / story bible.

---

## Additional Instructor Resources

- Next: 3.4.3 STIX as hunt input
