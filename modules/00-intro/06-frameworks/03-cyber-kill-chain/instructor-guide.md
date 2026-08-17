# Instructor Guide – Module 0.6.3 – Cyber Kill Chain

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.3.1 A / B / C ; 0.6.3.2 2b / 3c / 4c  
- Hunter: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- CTI: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- DE: 0.6.3.1 A / B / B ; 0.6.3.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Context (plain language):**

- What this hour is for: Place this step in time, and refuse the neighbor stage you did not see.
- How it hooks to the hour before: Diamond asked which corner is empty. Kill Chain asks which stage this row is.
- How it hooks to the hour after: tool survey (when to pick VT / AnyRun / Silent Push / URLScan).
- Why we are doing it this way: Shared floor before SOC. One staging model, not every framework at once.
- What we are *not* doing this hour: ATT&CK IDs. Diamond fill. No lab.

**Key Teaching Points:**
- Seven stages, in order.
- Place this row. Reject previous / next if you have no evidence.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:**  
- K: 0.6.3.1 – Cyber Kill Chain  
  SOC A / B / C · Hunter B / C / C · CTI B / C / C · DE A / B / B  
- T: 0.6.3.2 – Identify the Kill Chain stage of observed activity  
  SOC 2b / 3c / 4c · Hunter 3c / 4c / 4c · CTI 3c / 4c / 4c · DE 1a / 2b / 2b

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 2 min     | Where in time |
| Key Concepts            | 8 min     | Stages + one place |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~15 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the seven stages. Walk the `.vbs` in email as Delivery. Fail Exploitation (no run) and C2 (no callback).

---

## Knowledge Check – Answer Key

1. **What is it for?**  
   **Answer:** Staging attack progression. Not a complete model of every intrusion.  
   **Explanation:** Outline a.

2. **Seven stages?**  
   **Answer:** Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Actions on Objectives.  
   **Explanation:** Outline b.

3. **`.vbs` in email — why Delivery, not Exploitation?**  
   **Answer:** You saw it arrive. You did not see it run. Exploitation is the next stage you do not have.  
   **Explanation:** Outline c / task.

---

## Additional Instructor Resources

- Next: 0.7 External tools
