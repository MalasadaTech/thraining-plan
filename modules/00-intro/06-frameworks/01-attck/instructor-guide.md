# Instructor Guide – Module 1.5.1 – MITRE ATT&CK

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 1.5.1.1 A / B / C ; 1.5.1.2 2b / 3c / 4c  
- Hunter: 1.5.1.1 B / C / C ; 1.5.1.2 3c / 4c / 4c  
- CTI: 1.5.1.1 B / C / C ; 1.5.1.2 3c / 4c / 4c  
- DE: 1.5.1.1 A / B / B ; 1.5.1.2 1a / 2b / 2b  
**Estimated Time:** 20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Context (plain language):**

- What this hour is for: Give every role one language for “what the adversary was trying to do” and “how,” and show what a map with evidence looks like.
- How it hooks to the hour before: overlap said same evidence, different product. This hour is a shared label, not a product.
- How it hooks to the hour after: Diamond (four vertices), then Kill Chain (stage).
- Why we are doing it this way: Frameworks sit before SOC so hunt, CTI, and DE are not learning ATT&CK as a SOC-only trick. Hunt planning stays later.
- What we are *not* doing this hour: Hunt coverage. Actor profiles. DTF. Alert categories. No lab.

**Key Teaching Points:**
- Tactic = why. Technique / sub-technique = how.
- Map = tactic + ID + name + one cited field.
- Neighbor ID without a second row is a lead, not a better map.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.5.1.1 ; T 1.5.1.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Shared language |
| Key Concepts            | 10 min    | Structure + one map |
| Knowledge Check         | 5 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write tactic vs technique on the board. Walk the encoded-PowerShell line. Fail “C2” with no beacon row.

DE sits this at awareness. Do not start them at hunt-planning depth.

---

## Knowledge Check – Answer Key

1. **Tactic vs technique?**  
   **Answer:** Tactic is the goal (why). Technique is a named how.  
   **Explanation:** Outline b–c.

2. **ID with no cited field?**  
   **Answer:** A slogan, not a map.  
   **Explanation:** Outline d / task.

3. **Encoded PowerShell from a script — map and cite?**  
   **Answer:** Execution / `T1059.001` (or `T1059`). Cite the encoded command line. Not C2.  
   **Explanation:** Task 1.

---

## Additional Instructor Resources

- Next: 1.5.2 Diamond Model
