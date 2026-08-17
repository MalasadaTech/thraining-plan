# Instructor Guide – Module 2.8.1 – Identifying Additional Adversary Infrastructure

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4d  
- Hunter: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4d  
- SOC: 2.8.1 A / B / B ; 2.8.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Write a hop sentence from a seed. No P-ID. Reject shared /24.

**Context (plain language):**

- What this hour is for: CTI analysts say what they shared and what they found.
- How it hooks to the hour before: 2.7.4 was the DTF ID.
- How it hooks to the hour after: 2.8.2 is TTPs that apply *here*.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–b. No tool redo.
- What we are *not* doing this hour: RDAP class. SOA parse. PDNS. DTF IDs. No lab.
- Extra step: none.

**Key Teaching Points:**
- Four-part sentence.
- /24 is coincidence.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.8.1 ; T 2.8.1.1

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Sentence, not P-ID |
| Key Concepts            | 12 min    | Sibling hop; reject /24 |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the sentence shape. Walk sibling NS. Fail /24.

If they write P0101.010: “2.7.4. This hour is the sentence.”  
If they open RDAP: “Name it. Do not teach it.”

---

## Knowledge Check – Answer Key

1. **Must write a P-ID. True or false?**  
   **Answer:** False. That is 2.7.4.  
   **Explanation:** Stay-in.

2. **Four parts?**  
   **Answer:** Seed, shared characteristic, candidate, why not coincidence.  
   **Explanation:** Outline a / task 1.

3. **Hop to login-prd.net?**  
   **Answer:** Seed update domain; shared NS; candidate login-prd.net; distinctive NS, not a public resolver. /24 is reject.  
   **Explanation:** Task 1.

---

## Additional Instructor Resources

- Next: 2.8.2 Applicable TTPs
