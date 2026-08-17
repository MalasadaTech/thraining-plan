# Instructor Guide – Module 2.7.4 – Defender’s ThreatMesh Framework (DTF)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.4 B / C / C ; 2.7.4.1 3c / 4c / 4d ; 2.7.4.2 3c / 4c / 4d ; 2.7.4.3 3c / 4c / 4c  
- Hunter: 2.7.4 A / B / B ; 2.7.4.1 1a / 2b / 3c ; 2.7.4.2 1a / 2b / 3c ; 2.7.4.3 1a / 2b / 3c  
- SOC: 2.7.4 A / A / B ; 2.7.4.1 1a / 1a / 2b ; 2.7.4.2 1a / 1a / 2b ; 2.7.4.3 1a / 1a / 2b  
**Estimated Time:** 25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Pick a real PTA/P, cite the characteristic, reject shared cloud, name the next lookup. DTF does not replace ATT&CK / Diamond / Kill Chain.

**Context (plain language):**

- What this hour is for: CTI analysts record a defender discovery pivot from a known-bad seed.
- How it hooks to the hour before: 2.7.3 was progression. This hour is infra discovery.
- How it hooks to the hour after: 2.8.1 is the hop *without* P-IDs.
- Why we are doing it this way: Short 0.x / 4.x voice. Official DTF IDs only. No score. No invented P-codes.
- What we are *not* doing this hour: Re-teach RDAP/SOA/PDNS. T-IDs. Lumped 2.7.5. No lab.
- Extra step: none.

Use `login-prd.net` and `ns1.cdn-test.net`. Do not invent P-codes.

**Key Teaching Points:**
- Four tactics. Real IDs.
- /24 is reject. Same NS / same A can take.
- Next lookup is a name, not a tool class.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.7.4 ; T 2.7.4.1 ; T 2.7.4.2 ; T 2.7.4.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Discovery, no score |
| Key Concepts            | 15 min    | Four PTA; take/reject; complement |
| Knowledge Check         | 5 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write four PTA. Walk same NS / same A as take. Walk /24 as reject. Complement table in one pass.

If they invent P9999: “Not in DTF.”  
If they score: “No scoring.”  
If they assign T1059: “2.7.1.”

---

## Knowledge Check – Answer Key

1. **DTF replaces ATT&CK. True or false?**  
   **Answer:** False. Discovery vs behavior.  
   **Explanation:** Outline e / task 3.

2. **Same NS. ID?**  
   **Answer:** **PTA0001 / P0101.010** (take if distinctive).  
   **Explanation:** Task 1.

3. **/24 take or reject? Next lookup if same-A?**  
   **Answer:** **Reject** P0202. If same-A (P0103.003): next lookup is PDNS / other names on that A (**0.7** / **2.9.3**).  
   **Explanation:** Tasks 1–2.

---

## Additional Instructor Resources

- Next: 2.8.1 Infrastructure hop sentence
- https://github.com/MalasadaTech/defenders-threatmesh-framework
