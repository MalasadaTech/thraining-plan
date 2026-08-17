# Instructor Guide – Module 3.4.1 – Assessing CTI for Hunting Value

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.1 B / C / C ; 3.4.1.1 3c / 4c / 4d  
- SOC: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
- CTI: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Gate a report: hunt / don’t hunt / hand off, plus why. Not a TTP extract.

**Context (plain language):**

- What this hour is for: Hunters decide whether a report is worth a hunt before they pull leads.
- How it hooks to the hour before: 3.3.1 converted a tool lead to a precise query.
- How it hooks to the hour after: 3.4.2 extracts leads from reports that passed the gate.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c + triage task. Not 3.4.2 or 3.5.
- What we are *not* doing this hour: Extract every TTP. Author STIX. Map Navigator. No lab.
- Extra step: none.

**Key Teaching Points:**
- Interesting ≠ hunt.
- Actionable = question + telemetry + scope.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 3.4.1 ; T 3.4.1.1

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Gate, not extract |
| Key Concepts            | 12 min    | Three labels; A12 card |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the three dispositions. Walk question / telemetry / scope. Walk the A12 bulletin as hunt-worthy.

If they copy every MITRE ID: “3.4.2 / 3.5.”  
If they invent a hunt ticket: “3.7.”

---

## Knowledge Check – Answer Key

1. **Interesting actor profile is a hunt. True or false?**  
   **Answer:** False. Awareness unless you can name question, telemetry, and scope.  
   **Explanation:** Outline a / c.

2. **Three things?**  
   **Answer:** Hunt question. Telemetry that could answer it. Bound scope.  
   **Explanation:** Outline c.

3. **Label the classroom card?**  
   **Answer:** **Hunt-worthy** — named objects, data exists, no analytic, no open IR.  
   **Explanation:** Task 1.

---

## Additional Instructor Resources

- Next: 3.4.2 Extracting hunt leads
