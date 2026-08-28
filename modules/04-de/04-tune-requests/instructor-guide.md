# Instructor Guide – Module 4.4 – Tune requests from SOC

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.4 B / C / C ; 4.4.1 3c / 4c / 4d ; 4.4.2 3c / 4c / 4c  
- SOC: 4.4 A / B / B ; 4.4.1 1a / 2b / 3c ; 4.4.2 1a / 2b / 2b  
- Hunter: 4.4 A / A / B ; 4.4.1 1a / 1a / 2b ; 4.4.2 1a / 1a / 2b  
- CTI: 4.4 A / A / B ; 4.4.1 1a / 1a / 2b ; 4.4.2 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the tune inbox, require which live rule plus a pointer, pick one of five answers, and reject investigation, block, or IR dressed as a tune.

**Context (plain language):**

- What this lesson is for: After a detection is live, SOC lives with the alerts. When that rule is noisy, brittle, or missing context, they ask DE to change it. That ask is a tune request, not a new nomination. Name the live rule, point at the investigation or intel report, then pick an answer — or reject work that is not a detection change.
- How it hooks to the lesson before: 4.3 was a nomination (something new, with a need and a pointer). This lesson is a rule that is already live.
- How it hooks to the lesson after: 4.5 is hunt and intel packages.
- Why we are doing it this way: A tune request needs the same kind of pointer as a nomination — an investigation or intel report — so you can cite why you pick an answer.
- What we are *not* doing in this lesson: Writing a rule (1.3). Nomination accept / send-back depth (4.3). Packages (4.5). Full lifecycle (4.6). No lab. No DYA tickets or forms.
- Extra step: none.

Use the same names as the student guide: **tune**, **exception**, **replace**, **leave**, and **retire**. **Inbox** means the pile of work, not a ticket name. **Missing context** on the rule is not the same as the **pointer**.

**Key Teaching Points:**
- A tune is a live rule. It is a different inbox from nominations.
- Clear enough means which rule plus a pointer. No pointer means send it back.
- Five answers. Cite why. Investigation, block, and IR are not tunes.

**Common Student Challenges:**
- Mix “the rule is missing context” with “the request has no pointer.” Why: both use the word context. Example: sending the request back because the rule is noisy, instead of because the investigation number is missing.
- Pick a tune answer with no pointer. Why: they want to fix the noise. Example: choosing exception on a named live rule with no investigation or report.
- Treat “go look at the host” as a tune. Why: the ask mentions a live rule. Example: picking tune when SOC asked you to investigate the host.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 4.4 – Tune requests from SOC
- T: 4.4.1 – Pick tune / exception / replace / leave / retire and cite why
- T: 4.4.2 – Reject a request that is investigation, a block, or IR containment

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | After 4.3 nominations |
| Key Concepts            | 10 min    | Pointer; five answers; three rejects |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: after a rule is live, SOC asks DE to change it. That is a tune request, not a new nomination.
- Write noisy, brittle, and missing context. Missing context is what is wrong with the live rule. It is not the pointer.
- Same desk, different inbox. Inbox means the pile of work, not a ticket name.
- Clear enough is which live rule plus a pointer. If the pointer is missing, send it back. You cannot cite why without it.
- Then the five answers and the three rejects. Walk the three “given” lines from the student guide.
- If they mix “the rule is missing context” with “no pointer”: one is the rule. One is the ask.
- If they pick tune with no pointer: send it back. You cannot cite why.
- If they start writing SIGMA: that is 1.3.
- If they treat “go look at the host” as a tune: that is investigation. Reject.

---

## Knowledge Check – Answer Key

1. **A tune request and a nomination are the same inbox. True or false?**  
   **Answer:** False. Same desk. Different inbox.  
   **Explanation:** A nomination is something new. A tune is a live rule. The work sits in a different pile.

2. **A tune request names the live rule but has no investigation or report pointer. Pick a tune answer, or send it back?**  
   **Answer:** Send it back. SOC owes the investigation number, or the report title and URL.  
   **Explanation:** Clear enough to review means which live rule plus a pointer. You cannot cite why without the pointer.

3. **SOC says a live rule is noisy and asks you to investigate the host. Tune or reject?**  
   **Answer:** Reject. That is an investigation, not a tune.  
   **Explanation:** A tune changes a live detection. “Go look at the host” is SOC investigation work. The same reject applies to a block or IR containment.

---

## Additional Instructor Resources

- Next: 4.5 Hunt and intel packages
