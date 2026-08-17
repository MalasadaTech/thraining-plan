# Instructor Guide – Module 3.3.1 – Tool Capabilities for Hunting

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.3.1 B / C / C ; 3.3.1.1–3.3.1.3 3c / 4c / 4d  
- SOC: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 1a / 2b / 3c ; 3.3.1.3 1a / 2b / 3c  
- CTI: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 2b / 3c / 4c ; 3.3.1.3 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Hunt strength/limit per tool. Convert a card lead to a precise internal query. No /24. No live account.

**Context (plain language):**

- What this hour is for: Hunters turn an external finding into something they can search *here*.
- How it hooks to the hour before: 3.2.2 wrote the card.
- How it hooks to the hour after: 3.4.1 is triaging a CTI report.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–d + convert task. Not 0.7 or 2.9 redo.
- What we are *not* doing this hour: Live vendor lab. Relations class. /24 query.
- Extra step: none.

**Key Teaching Points:**
- Count / tag / screenshot ≠ query.
- Precise: IP + port + URI.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 3.3.1 ; T 3.3.1.1–3.3.1.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Convert, not survey |
| Key Concepts            | 12 min    | Four limits; query |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write four limits. Walk the Zeek/HTTP convert. Fail dest=*.

If they redo Relations: “2.9.1.”  
If they /24: “Noise.”

---

## Knowledge Check – Answer Key

1. **VT count is a hunt query. True or false?**  
   **Answer:** False.  
   **Explanation:** Outline a / task 2.

2. **Silent Push hunt limit?**  
   **Answer:** Whole /24 is noise (or PDNS without a precise name).  
   **Explanation:** Outline d.

3. **Convert :8080 /update.exe?**  
   **Answer:** Query dest IP + port 8080 + URI `/update.exe` (Zeek or SIEM). Not a /24.  
   **Explanation:** Task 3.

---

## Additional Instructor Resources

- Next: 3.4.1 Assessing CTI for hunting value
