# Instructor Guide – Module 1.3.4 – SIEM Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.4.1 A / B / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 1a / 2b / 3c  
- Hunter: 1.3.4.1 B / C / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 2b / 3c / 4c  
- CTI: 1.3.4.1 A / B / B ; 1.3.4.2 1a / 2b / 3c ; 1.3.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a SIEM detection and propose a basic create from log fields or from SIGMA. Do not deploy it.

**Context (plain language):**

- What this hour is for: SOC analysts turn fields they already know into a named rule that can fire an alert.
- How it hooks to the hour before: 1.3.1 wrote the SIGMA; 1.3.3 was bytes. This hour is the SIEM object.
- How it hooks to the hour after: 1.4.1 is the alert that object creates — context and investigation, not more syntax.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c only. SOC create is 1a/2b/3c. This closes 1.3.
- What we are *not* doing this hour: Deploy. Alert queue. Converter lab. Invented SIEM product names as policy. No lab.
- Extra step: none.

Use the encoded PowerShell + wscript translation. Do not tell the PRD plot.

**Key Teaching Points:**
- Name, table, logic, window, output.
- Fields → where. SIGMA → the same mapping, then wrap it.
- Wildcard vs regex.
- Empty table is not a detection.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.3.4.1 ; T 1.3.4.2 ; T 1.3.4.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | The object that fires the alert |
| Key Concepts            | 16 min    | Structure, fields, SIGMA path |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Walk name / table / logic / window / output. Translate the 1.3.1 SIGMA in one breath.

If they open the alert console: “1.4.”  
If they want to deploy: “4.x / DE.”  
If they put `uri` on DeviceProcessEvents: “Wrong table.”

---

## Knowledge Check – Answer Key

1. **A SIEM table with no filter is a detection. True or false?**  
   **Answer:** False. You need logic (and a name, window, outputs).  
   **Explanation:** Outline a.

2. **The given rule — what does it detect?**  
   **Answer:** Process create of PowerShell with -enc and parent wscript.  
   **Explanation:** Outline b and 1.3.8 task 1.

3. **When wildcard instead of regex?**  
   **Answer:** When a substring or path is enough. Regex when the token actually varies.  
   **Explanation:** Outline c.

---

## Additional Instructor Resources

- Next: 1.4.1 Alert context and investigation
