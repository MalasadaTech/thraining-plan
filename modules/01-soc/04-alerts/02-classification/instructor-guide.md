# Instructor Guide – Module 1.4.2 – Alert Classification

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.2.1 A / B / C ; 1.4.2.2 2b / 3c / 4c  
- Hunter: 1.4.2.1 B / C / C ; 1.4.2.2 2b / 3c / 4c  
- CTI: 1.4.2.1 A / A / B ; 1.4.2.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Classify a case as TP, FP, TN, or FN and cite the evidence. Include one miss as FN.

**Context (plain language):**

- What this hour is for: SOC analysts label the case they just investigated and say why, in one cite.
- How it hooks to the hour before: 1.4.1 gathered context on the encoded-PowerShell alert.
- How it hooks to the hour after: 1.4.3 is *why* an FP fired — not the label.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–d. FN is a missed detection. No lab.
- What we are *not* doing this hour: FP cause class. Categories. Hunt. Invented alerts so they can classify. No lab.
- Extra step: none.

TP = the first alert. FN = GET /update.exe with no queue row. Do not tell the PRD plot.

**Key Teaching Points:**
- Four labels. TN/FN usually have no queue row.
- Cite, not a slogan.
- FN is a miss, not a disliked alert.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.4.2.1 ; T 1.4.2.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Label + cite |
| Key Concepts            | 12 min    | Four labels; four givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the four-cell table. Walk TP then FN so they do not call a miss an FP.

If they start “untuned rule”: “1.4.3. Label only.”  
If they invent an alert for the GET: “No alert. That is the FN.”  
If they say “malicious” with no cite: “Cite the field.”

---

## Knowledge Check – Answer Key

1. **FN is a bad alert in the queue. True or false?**  
   **Answer:** False. FN is a miss — no alert on bad activity.  
   **Explanation:** Outline d.

2. **Encoded PS alert, wscript + -enc. Classify and cite.**  
   **Answer:** TP. The activity the rule is for occurred.  
   **Explanation:** Outline a / task 1.

3. **GET /update.exe, no alert. Classify and cite.**  
   **Answer:** FN. The download occurred; nothing fired.  
   **Explanation:** Outline d / task 1 (include a miss).

---

## Additional Instructor Resources

- Next: 1.4.3 Common false positive causes
