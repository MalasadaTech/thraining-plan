# Instructor Guide – Module 2.1.8 – Collection Sources and Methods

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.8 B / C / C ; 2.1.8.1 3c / 4c / 4c ; 2.1.8.2 3c / 4c / 4d  
- Hunter: 2.1.8 A / B / B ; 2.1.8.1 1a / 1a / 2b ; 2.1.8.2 1a / 1a / 2b  
- SOC: 2.1.8 A / A / B ; 2.1.8.1 1a / 1a / 1a ; 2.1.8.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Pick OSINT / commercial / internal and write a short plan: order, first action, what you will not collect.

**Context (plain language):**

- What this hour is for: CTI analysts choose *where* to collect so they do not skip internals when the question is “are we seeing this?”
- How it hooks to the hour before: 2.1.7 was who you claim. This hour is where you look.
- How it hooks to the hour after: 2.2.1 is how you word a judgment. Not the ticket to request collection.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c. No invented request form.
- What we are *not* doing this hour: VT Relations. TIP nav. Local ticket. Rewrite the PIR. No lab.
- Extra step: none.

**Key Teaching Points:**
- Three classes. Stack. Order follows the requirement.
- Internals first when the question is *our* presence.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.1.8 ; T 2.1.8.1 ; T 2.1.8.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Where, not the stage |
| Key Concepts            | 12 min    | Three classes; A12 plan |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the three classes. Walk A12 as **internal first**.

If they open VT Relations: “2.9 / 0.7.”  
If they write a Jira: “2.12.2.1.”  
If they rewrite the question: “2.1.4 is done.”

---

## Knowledge Check – Answer Key

1. **Stage and class are the same. True or false?**  
   **Answer:** False. Stage is the job. Class is where you collect.  
   **Explanation:** Stay-in / vs 2.1.2.

2. **Three classes?**  
   **Answer:** OSINT, commercial, internal.  
   **Explanation:** Outline a–c.

3. **A12 “payload host *here*.” Plan?**  
   **Answer:** First class **internal**. First action: Zeek A record / host file you have. Do not collect a sibling domain or a live vendor account you do not have.  
   **Explanation:** Tasks 1–2.

---

## Additional Instructor Resources

- Next: 2.2.1 Estimative language
