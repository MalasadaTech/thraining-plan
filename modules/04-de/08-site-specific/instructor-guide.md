# Instructor Guide – Module 4.8 – Site-specific DE knowledge

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.8.1 B / C / C ; 4.8.1.1 3c / 4c / 4c ; 4.8.2 B / C / C ; 4.8.2.1 3c / 4c / 4c ; 4.8.2.2 3c / 4c / 4c  
- SOC: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1 1a / 1a / 1a ; 4.8.2.2 1a / 1a / 1a  
- Hunter: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1 1a / 1a / 1a ; 4.8.2.2 1a / 1a / 1a  
- CTI: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1 1a / 1a / 1a ; 4.8.2.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Local policy exists and varies by shop. Obtain the requirements list and the review / deploy / retire path. Follow only what you were shown. Reject inventing policy.

**Context (plain language):**

- What this lesson is for: A detection engineer ships, changes, or retires a rule against this shop’s rules. Those rules are local. They are not in this course. Obtain the current list and the path, then follow only what you were shown, so you do not invent policy to make a nomination look complete.
- How it hooks to the lesson before: 4.7 was sensors. 4.2 already said the field *list* is local. 4.6 already said you retire and deploy. This lesson is obtain-and-follow for both the list and the path.
- How it hooks to the lesson after: Section 4 is complete. There is no 4.9.
- Why we are doing it this way: 4.8.1 and 4.8.2 are one teaching unit. Local policy exists. The analyst obtains it. This course does not publish a shop handbook.
- What we are *not* doing in this lesson: Publishing a DYA field list. Naming a change board or ticket. Writing a rule (1.3). Testing soundness (4.2). Lifecycle calls (4.6). Sensor checks (4.7). No lab.
- Extra step: none.

Use the same names as the student guide: **list**, **path**, **obtain**, **obtain-and-follow**, **I do not have it yet**, and **policy**. **4.2** named kinds (meta fields, naming, IDs, tags, logging). Do not turn those kinds into a fake DYA list on the board. **DYA** is the classroom firm. This course does not publish its policy.

**Key Teaching Points:**
- Local policy exists. It varies by shop.
- Have it / do not have it. Align only to a list you were shown.
- Inventing a change board or ticket name is a fail.

**Common Student Challenges:**
- Invent fields so the nomination is not blank. Why: 4.2 named the kinds of shop requirements, and this lesson asks for the current list. Example: writing a classroom meta-field list and treating it as shop policy.
- Name a change board or ticket so a deploy looks official. Why: 4.6 said you retire and deploy, and this lesson asks for the local path. Example: “send it to change board X” when no path was shown.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 4.8.1 – Local detection requirements
- T: 4.8.1.1 – Identify whether you have the local list and align only to a list you were shown
- K: 4.8.2 – Local review, deploy, and retire paths
- T: 4.8.2.1 – Follow the local path you were shown (or record that you do not have it yet)
- T: 4.8.2.2 – Reject inventing a change board or ticket name as policy

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Local policy exists; obtain it |
| Key Concepts            | 10 min    | List + path; do not invent |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: shipping, changing, or retiring a detection has to match this shop’s rules, and those rules are not in this course.
- Local policy has two parts: the requirements list, and the review / deploy / retire path. Both vary by shop.
- 4.2 named the kinds of checks (meta fields, naming, IDs, tags, logging). Today is obtaining the current list, not writing one on the board.
- 4.6 said you retire and deploy. Today is obtaining how this shop reviews a change, deploys it, and records a retire.
- Walk obtain-and-follow. Get the list and path from the role or place the lead names. Use only that. If you overlay a real shop list or path, name it as overlay, not DYA policy.
- Walk the three givens from the student guide. “I do not have it yet” is a pass. Inventing fields, a change board, or a ticket name is a fail.
- If they start a field list on the board: those are kinds, not a DYA list. Stop.
- If they name a ticket or a change board: reject. That is invented policy.
- If they have no list or path: record that. Do not fill the gap.
- If they start writing a rule: that is 1.3.

---

## Knowledge Check – Answer Key

1. **This course publishes the DYA field list and deploy path. True or false?**  
   **Answer:** False. Local policy varies by shop. Obtain it. This course does not publish DYA’s.  
   **Explanation:** Required meta fields, naming, deploy checks, and the review / deploy / retire path are local. The analyst obtains the current list and path. Inventing a classroom handbook is not the product.

2. **You do not have the local requirements list. Do you invent the fields?**  
   **Answer:** No. Record that you do not have the list. Do not invent fields.  
   **Explanation:** Identify whether you have the list. Alignment is only to a list you were shown. “I do not have it yet” is a pass.

3. **You invent a change board or ticket name and treat it as policy. Follow it, or reject?**  
   **Answer:** Reject.  
   **Explanation:** Follow only the path you were shown. A made-up change board or ticket name is not policy.

---

## Additional Instructor Resources

- Section 4 is complete. There is no 4.9.
