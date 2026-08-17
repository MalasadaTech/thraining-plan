# Instructor Guide – Module 2.8.3 – IOC Handling and Enrichment Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.3 B / C / C ; 2.8.3.1 3c / 4c / 4d ; 2.8.3.2 3c / 4c / 4d  
- Hunter: 2.8.3 B / C / C ; 2.8.3.1 3c / 4c / 4d ; 2.8.3.2 1a / 2b / 3c  
- SOC: 2.8.3 A / B / B ; 2.8.3.1 1a / 2b / 3c ; 2.8.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Keep / expire / enrich / link. Same set only on shared objects. Vendor name is not a link.

**Context (plain language):**

- What this hour is for: CTI analysts handle observables as objects.
- How it hooks to the hour before: 2.8.2 was TTPs.
- How it hooks to the hour after: 2.8.4 is so-what here.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–d. Name the tool, do not re-teach it.
- What we are *not* doing this hour: VT Relations class. Actor profile. No lab.
- Extra step: none.

**Key Teaching Points:**
- /24 expires.
- Same NS / same A can link. PDF name cannot.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.8.3 ; T 2.8.3.1 ; T 2.8.3.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Object, not TTP |
| Key Concepts            | 12 min    | Keep/expire; link |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write keep/expire/enrich/link. Walk TIP then VT. Walk sibling link. Fail APT-name link.

If they open Relations: “2.9.1.”  
If they write T1059: “2.8.2.”

---

## Knowledge Check – Answer Key

1. **IOC = TTP. True or false?**  
   **Answer:** False. Observable vs behavior.  
   **Explanation:** Outline a.

2. **/24 keep or expire?**  
   **Answer:** **Expire** as shared-infra noise.  
   **Explanation:** Outline b.

3. **Domain + sibling same NS. Set? Vendor name?**  
   **Answer:** **Same set** — shared NS/A. “PRD APT” is **not** a link.  
   **Explanation:** Task 2.

---

## Additional Instructor Resources

- Next: 2.8.4 Relevance and impact
