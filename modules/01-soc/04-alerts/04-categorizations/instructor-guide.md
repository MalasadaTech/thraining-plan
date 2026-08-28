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
On a working alert, name the category and say why the adjacent category is wrong.

**Context (plain language):**

- What this lesson is for: SOC analysts put a category on an alert so the next desk can see what kind of activity it was — not the true-positive / false-positive label again, and not an ATT&CK ID.
- How it hooks to the lesson before: 1.4.3 named why a false positive fired and what you would change.
- How it hooks to the lesson after: 1.4.5 is the start clock and the close/escalate clock.
- Why we are doing it this way: After the case is labeled, the next desk still needs the kind of activity. Adjacent names get mixed up, so the product is the category plus why the neighbor is wrong.
- What we are *not* doing in this lesson: Reclassify. Name a false-positive cause. Map ATT&CK as the category. Invent a DYA category list. SLA clocks. No lab.
- Extra step: none.

Use the same names as the student guide: **scanning / reconnaissance**, **root-level access**, **user-level access**, **unsuccessful activity**, and **other**. **Adjacent category** means the neighbor people mix it up with. Do not invent Harbor or DYA architecture as policy. Do not tell the PRD plot. The first alert is still `wscript` → encoded PowerShell as `jlee`.

**Key Teaching Points:**
- Five names: scan / recon, root, user, unsuccessful, other (a name the shop already uses).
- Adjacent pairs: scan ↔ unsuccessful; user ↔ root.
- Privilege of the account, not “looks scary.” A failed login is not a sweep.

**Common Student Challenges:**
- Treat encoded PowerShell as root. Why: it looks more severe than a normal user command. Example: writing root-level for Medium `jlee` `-enc`.
- Call a 401 burst scanning. Why: many failures look like a probe. Example: labeling failed logons on one application as scanning / reconnaissance.
- Write T1059 as the category. Why: ATT&CK is a familiar label. Example: putting Execution / T1059 in the category field.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.4.4.1 – Common alert categorizations
- T: 1.4.4.2 – Assign a category to an alert and justify why it is not the adjacent category

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Category, not TP/FP label |
| Key Concepts            | 12 min    | Five names; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert already has a true-positive or false-positive label, and the next desk still needs the kind of activity.
- Write the five names. Stop. Other is a name their real shop already uses, not an ATT&CK ID.
- Walk `jlee` Medium `-enc` as **user-level, not root**. Encoded does not upgrade the account.
- Walk the unanswered SYN sweep as **scanning, not unsuccessful**. Nothing was presented as credentials or an exploit.
- If they write true positive or false positive: that label is 1.4.2. This lesson is the category.
- If they write T1059: that is 0.6. It is not a category.
- If they upgrade encoded PowerShell to root: the account is Medium. Encoded does not change the category.
- If they call a 401 burst a scan: one application, failed authorization — unsuccessful.
- If they invent a DYA list: other is a name their real shop already uses.

---

## Knowledge Check – Answer Key

1. **A category is the same thing as a true-positive or false-positive label. True or false?**  
   **Answer:** False. The label says whether the detection was right. This lesson is the category plus why the adjacent category is wrong.  
   **Explanation:** True positive / false positive is 1.4.2. A category names the kind of activity.

2. **Name the four syllabus categories plus other.**  
   **Answer:** Scanning / reconnaissance; root-level access; user-level access; unsuccessful activity; other (as the shop uses it).  
   **Explanation:** Those five names are the whole set. Other is not a new invented list.

3. **`wscript` + `-enc` as Medium `jlee`. Category, and why not the adjacent one?**  
   **Answer:** **User-level.** Not root: the account is a standard user. Encoded does not upgrade it.  
   **Explanation:** The adjacent pair is user ↔ root. Privilege of the account is what you write down, not how the command looks.

---

## Additional Instructor Resources

- Next: 1.4.5 Service Level Agreements / Response Time Goals
