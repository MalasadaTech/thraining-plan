# Instructor Guide – Module 4.3 – Nominations from SOC, hunt, and CTI

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.3 B / C / C ; 4.3.1 3c / 4c / 4d  
- SOC: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
- Hunter: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
- CTI: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Who can nominate, what the nomination must contain, and how DE reviews: accept, send back, or reject — plus who still owes what.

**Context (plain language):**

- What this lesson is for: SOC, hunt, and CTI send Detection Engineering work. That hand-off is a nomination. DE reviews it because a rough ask is still detection work, but only if it is clear enough to review. This lesson is who can send one, what it must contain, and how you accept, send back, or reject it.
- How it hooks to the lesson before: 4.2 was sound, the shop list, and the close-the-loop note.
- How it hooks to the lesson after: 4.4 is a tune request on a live rule. Same desk, different inbox.
- Why we are doing it this way: a nomination that is only a vibe cannot be reviewed. Name the need and point at an investigation or intel report first, then decide. A drafted rule is extra, not the bar.
- What we are *not* doing in this lesson: Writing a rule (1.3). Testing (4.2). Tunes (4.4). Packages (4.5). No lab. No tickets or forms.
- Extra step: none.

Use the same names as the student guide: **need**, **pointer**, **accept for work**, **send back**, and **reject**. **Report** means intel report. **Sent back** in 4.2 is the close-the-loop *note*. Here **send back** is the review.

**Key Teaching Points:**
- Only SOC, hunt, and CTI nominate.
- Clear enough means need + pointer. A drafted rule is optional.
- Always say who still owes what.

**Common Student Challenges:**
- Treat a nomination without a drafted rule as incomplete. Why: they think DE cannot start without syntax. Example: sending back encoded PowerShell plus a report URL because there is no SIGMA.
- Reject when they should send back. Why: a missing pointer looks like “not DE work.” Example: rejecting “encoded PowerShell on workstations” with no report, instead of sending it back for the pointer.
- Invent a ticket or form. Why: they want a named artifact before they will review. Example: refusing to review until there is a shop ticket number.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 4.3 – Nominations from SOC, hunt, and CTI
- T: 4.3.1 – Review a nomination: accept, send back, or reject, and say who finishes what

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | After 4.2 sound |
| Key Concepts            | 10 min    | Need + pointer; three reviews |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: other desks send detection ideas, and DE reviews them so work that is clear enough gets finished.
- Write who can nominate. Stop. A SOC analyst, a hunter, or a CTI analyst.
- Write the bar: need + pointer. A drafted rule is optional. The bar is clear enough to review, not ready to deploy.
- Walk the three “given” lines from the student guide. The product is accept / send back / reject, plus who still owes what.
- If they require a drafted rule to accept: it is not required. DE finishes the rule.
- If they invent a ticket or form: pointer *kinds* — investigation number, or report title and URL. Not a form.
- If they start writing a rule: that is 1.3.
- If they start a tune on a live rule: that is 4.4.

---

## Knowledge Check – Answer Key

1. **Who can nominate?**  
   **Answer:** A SOC analyst, a hunter, or a CTI analyst.  
   **Explanation:** Only those three desks send this hand-off. A block is not a nomination.

2. **A nomination names the need and points at a report, but has no drafted rule. Accept or send back?**  
   **Answer:** Accept. A drafted rule is not required. DE finishes the rule.  
   **Explanation:** Clear enough is need + pointer. Production-ready is not the bar.

3. **A nomination names the activity but has no investigation or report pointer. Accept, send back, or reject? Who still owes what?**  
   **Answer:** Send back. The nominator still owes the investigation number, or the report title and URL.  
   **Explanation:** Missing a pointer is incomplete, not “not DE work.” Reject is for a block, an investigation, or “write me SIGMA.”

---

## Additional Instructor Resources

- Next: 4.4 Tune requests from SOC
