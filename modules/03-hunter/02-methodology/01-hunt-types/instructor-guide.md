# Instructor Guide – Module 3.2.1 – Hunt Types

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.1 B / C / C ; 3.2.1.1–3.2.1.4 3c / 4c / 4c  
- SOC: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
- CTI: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the type and what execute looks like. No lab. No hunt card format.

**Context (plain language):**

- What this hour is for: Hunters pick why they are searching.
- How it hooks to the hour before: 3.1 was why hunt exists.
- How it hooks to the hour after: 3.2.2 is the written hypothesis / scope.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–d. Execute = product line.
- What we are *not* doing this hour: Hunt card. SIEM session. Invented ticket. No lab.
- Extra step: none.

**Key Teaching Points:**
- Four starts.
- Hypothesis ≠ intel-driven.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 3.2.1 ; T 3.2.1.1–3.2.1.4

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Why this search |
| Key Concepts            | 12 min    | Four types; A12 |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the four. Walk Run Updater as hypothesis-driven. Walk CTI domain as intel-driven.

If they write the card: “3.2.2.”  
If they open SIEM: “Product line this hour.”

---

## Knowledge Check – Answer Key

1. **All four start from CTI. True or false?**  
   **Answer:** False. Only intel-driven does.  
   **Explanation:** Outline a–d.

2. **Four types?**  
   **Answer:** Intel-driven, hypothesis-driven, reactive, anomaly-based.  
   **Explanation:** Outline a–d.

3. **If they persist, Run Updater. Type and search?**  
   **Answer:** **Hypothesis-driven.** Search HKCU Run `Updater` on other hosts.  
   **Explanation:** Task 2.

---

## Additional Instructor Resources

- Next: 3.2.2 Hunt development
