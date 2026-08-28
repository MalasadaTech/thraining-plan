# Instructor Guide – Module 4.2 – Making a detection sound and meeting shop requirements

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.2 B / C / C ; 4.2.1 3c / 4c / 4d ; 4.2.2 3c / 4c / 4c ; 4.2.3 3c / 4c / 4c  
- SOC: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
- Hunter: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
- CTI: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the ship bar for a detection: sound, the test you state before it goes live, the shop list you were shown, and the close-the-loop note.

**Context (plain language):**

- What this lesson is for: A detection on DE’s desk does not ship because someone asked. It ships when it is sound and when it meets the shop list you were shown. This lesson is that ship bar: test what must fire and what must not, check the list you were shown, and tell the nominator what happened.
- How it hooks to the lesson before: 4.1 named what DE owns. This lesson is what good enough to ship looks like.
- How it hooks to the lesson after: 4.3 is how you review a nomination (accept, send back, or reject).
- Why we are doing it this way: sound, the kinds of shop requirement, and the four notes are the bar you can teach without a local field list. The actual list is 4.8.
- What we are *not* doing in this lesson: Writing a rule (1.3). Inventing DYA fields or tickets. Nomination accept/reject depth (4.3). Tune inbox (4.4). No lab.
- Extra step: none.

Use the same names as the student guide: **sound**, **shop requirements**, and **close the loop**. The list is the one they were shown — not a list you invent on the board. **Sent back** here is the close-the-loop *note*. The accept / send back / reject *review* is 4.3.

**Key Teaching Points:**
- Sound means it fires on the intended activity and does not fire on what it must not.
- Test a draft or a change before it goes live. State both lines.
- Check the list you were shown, or say you do not have it. Do not invent fields.
- The note is shipped, changed, sent back, or retired.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 4.2 – Making a detection sound and meeting shop requirements
- T: 4.2.1 – Test a draft or change: what must fire and what must not
- T: 4.2.2 – Mark which shop requirements are met and which are still missing
- T: 4.2.3 – Write the close-the-loop note to the nominator

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | After 4.1 owns |
| Key Concepts            | 10 min    | Sound, list, four notes |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a detection does not ship because someone asked. It ships when it is sound and meets the list you were shown.
- Write must-fire and must-not-fire. Stop. Do not write a rule. A draft and a change both get those two lines.
- Name the kinds of shop requirement: meta fields, naming, IDs, tags, logging. Do not put a fake DYA field list on the board. If they invent a field: only the list you were shown. No list? Say so.
- The note is four words: shipped, changed, sent back, retired. If they start an accept/reject speech: that review depth is 4.3. **Sent back** here is the close-the-loop note.

---

## Knowledge Check – Answer Key

1. **A detection is sound when it does what two things?**  
   **Answer:** It fires on the intended activity, and it does not fire on what it must not.  
   **Explanation:** Sound is both facts. Firing on the intended activity alone is not enough.

2. **You were not shown a shop list. Do you invent the fields?**  
   **Answer:** No. Mark against a list you were shown, or say you do not have the list. Do not invent fields.  
   **Explanation:** The kinds of requirement are named in this lesson. The actual list is local (4.8).

3. **Name the four close-the-loop notes.**  
   **Answer:** Shipped, changed, sent back, retired.  
   **Explanation:** That is the note to the nominator (and SOC). It is not a ticket name, and it is not the 4.3 review.

---

## Additional Instructor Resources

- Next: 4.3 Nominations from SOC, hunt, and CTI
