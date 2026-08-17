# Instructor Guide – Module 1.5.2 – Diamond Model

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 1.5.2.1 A / B / C ; 1.5.2.2 2b / 3c / 4c  
- Hunter: 1.5.2.1 B / C / C ; 1.5.2.2 3c / 4c / 4d  
- CTI: 1.5.2.1 B / C / C ; 1.5.2.2 3c / 4c / 4d  
- DE: 1.5.2.1 A / B / B ; 1.5.2.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Context (plain language):**

- What this hour is for: Four corners of what you know, and which corner is empty.
- How it hooks to the hour before: ATT&CK labeled the behavior (capability-ish). Diamond asks who / with what / through what / against whom.
- How it hooks to the hour after: Kill Chain stages the same activity in time.
- Why we are doing it this way: Shared floor before SOC. Attribution products stay later.
- What we are *not* doing this hour: Naming PRD as a fact. Actor profiles. No lab.

**Key Teaching Points:**
- Four vertices. Weakest = least evidence.
- Vendor name on a PDF is not Adversary evidence.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.5.2.1 ; T 1.5.2.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 2 min     | Empty corner |
| Key Concepts            | 8 min     | Four vertices + one fill |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~15 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Walk the `WS-JLEE` + encoded PowerShell + domain fill. Fail “Adversary = PRD” with no evidence.

---

## Knowledge Check – Answer Key

1. **Four vertices?**  
   **Answer:** Adversary, Capability, Infrastructure, Victim.  
   **Explanation:** Outline b.

2. **Weakest vertex?**  
   **Answer:** The one with the least evidence. That is the next question, not a guess.  
   **Explanation:** Outline c / task.

3. **Encoded PowerShell on a workstation to a domain — weakest?**  
   **Answer:** Adversary. You have victim, capability, and infrastructure. No actor evidence.  
   **Explanation:** Task 1.

---

## Additional Instructor Resources

- Next: 1.5.3 Cyber Kill Chain
