# Instructor Guide – Module 2.8.2 – Extracting Applicable TTPs

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.2 B / C / C ; 2.8.2.1 3c / 4c / 4d  
- Hunter: 2.8.2 B / C / C ; 2.8.2.1 3c / 4c / 4d  
- SOC: 2.8.2 A / B / B ; 2.8.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Keep TTPs that apply here. Reject the rest. Real ATT&CK IDs only.

**Context (plain language):**

- What this hour is for: CTI analysts do not copy every T-ID out of a PDF.
- How it hooks to the hour before: 2.8.1 was infra hops.
- How it hooks to the hour after: 2.8.3 is IOC objects, not TTPs.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–b. DYA is a law firm / Windows workstations. OT does not fit.
- What we are *not* doing this hour: ATT&CK map class. Impact paragraph. Invent IDs. No lab.
- Extra step: none.

**Key Teaching Points:**
- Applicable = platform + possible here + defender can use it.
- OT wipe is reject.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.8.2 ; T 2.8.2.1

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Not every T-ID |
| Key Concepts            | 12 min    | Keep T1059.001; reject OT |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write applicable vs not. Walk encoded PS keep. Walk OT reject.

If they write an impact sentence: “2.8.4.”  
If they invent a T-ID: “Real IDs only.”

---

## Knowledge Check – Answer Key

1. **Every T-ID applies. True or false?**  
   **Answer:** False.  
   **Explanation:** Outline b.

2. **What makes a TTP applicable?**  
   **Answer:** We have that platform / path, and a defender here can detect or hunt it.  
   **Explanation:** Outline b.

3. **Encoded PS vs OT wipe?**  
   **Answer:** Keep T1059.001 (seen on WS-JLEE). Reject OT wipe — not this shop.  
   **Explanation:** Task 1.

---

## Additional Instructor Resources

- Next: 2.8.3 IOC handling
