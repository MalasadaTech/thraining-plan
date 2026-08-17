# Instructor Guide – Module 1.4.4 – Common Alert Categorizations

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.4.1 A / B / C ; 1.4.4.2 2b / 3c / 4c  
- Hunter: 1.4.4.1 B / C / C ; 1.4.4.2 2b / 3c / 4c  
- CTI: 1.4.4.1 A / A / A ; 1.4.4.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
On a working alert, name the site category and say why the neighbor is wrong.

**Context (plain language):**

- What this hour is for: SOC analysts bucket the activity so the next desk can see what kind of thing it was — not the TP/FP label again, and not an ATT&CK ID.
- How it hooks to the hour before: 1.4.3 was why an FP fired and what you would change.
- How it hooks to the hour after: 1.4.5 is the start clock and the close/escalate clock.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–e. Assign plus reject the neighbor. CTI names the words (A / 1a).
- What we are *not* doing this hour: Reclassify. Name an FP cause. Map ATT&CK. Invent a DYA category list. No lab.
- Extra step: none.

Do not invent Harbor or DYA architecture as policy. Do not tell the PRD plot. The first alert is still `wscript` → encoded PowerShell as `jlee`.

**Key Teaching Points:**
- Five names: scan / recon, root, user, unsuccessful, other (shop list).
- Adjacent pairs: scan ↔ unsuccessful; user ↔ root.
- Token, not “looks scary.” Failed auth is not a sweep.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.4.4.1 ; T 1.4.4.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Bucket, not label |
| Key Concepts            | 12 min    | Five names; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the five names. Walk `jlee` Medium `-enc` as **user, not root**. Walk the unanswered SYN sweep as **scan, not unsuccessful**.

If they write TP/FP: “Label is 1.4.2. This hour is the bucket.”  
If they write T1059: “0.6. Not a category.”  
If they upgrade encoded to root: “Token is Medium. Encoded does not change the bucket.”  
If they call a 401 burst a scan: “One app, failed auth — unsuccessful.”  
If they invent a DYA list: “Other is a name their real shop already uses.”

---

## Knowledge Check – Answer Key

1. **This hour is TP vs FP. True or false?**  
   **Answer:** False. The label is a different hour. This hour is category + rejected neighbor.  
   **Explanation:** Stay-in / vs 1.4.2.

2. **Four syllabus categories plus other?**  
   **Answer:** Scanning / reconnaissance; root-level access; user-level access; unsuccessful activity; other (as the shop uses it).  
   **Explanation:** Outline a–e.

3. **`wscript` + `-enc` as Medium `jlee`. Category and why not adjacent?**  
   **Answer:** **User-level.** Not root: the token is a standard user. Encoded does not upgrade it.  
   **Explanation:** Outline c / task 1. Adjacent pair is user ↔ root.

---

## Additional Instructor Resources

- Next: 1.4.5 Service Level Agreements / Response Time Goals
