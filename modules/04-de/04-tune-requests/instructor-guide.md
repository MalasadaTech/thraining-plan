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

- What this hour is for: After rules are live, SOC asks DE to change them. That is a tune request, not a new nomination. Which rule + pointer. Five answers. Reject the three mixes.
- How it hooks to the hour before: 4.3 was a nomination (something new, with a need + pointer). This hour is a rule that is already live — same kind of pointer.
- How it hooks to the hour after: 4.5 is hunt and intel packages.
- Why we are doing it this way: You wanted a tune request to include context, the same idea as a nomination: point at an investigation or intel report.
- What we are *not* doing this hour: Writing a rule (1.3). Nomination accept/send back depth (4.3). Packages (4.5). Full lifecycle (4.6). No lab. No DYA tickets or forms.
- Extra step: none.

Say **tune**, **exception**, **replace**, **leave**, and **retire** the way the student guide does. **Inbox** means the pile of work, not a ticket name. **Missing context** on the rule is not the same as the **pointer**.

**Key Teaching Points:**
- Live rule. Different inbox from nominations.
- Clear enough = which rule + pointer. No pointer → send back.
- Five answers. Cite why. Investigation, block, and IR are not tunes.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 4.4 ; T 4.4.1 ; T 4.4.2

---

## Suggested Timing

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

Write which rule + pointer first. Then the five answers and the three rejects. Walk the three “given” lines.

If they mix “the rule is missing context” with “no pointer”: “One is the rule. One is the ask.”  
If they pick tune with no pointer: “Send it back. You cannot cite why.”  
If they start writing SIGMA: “That is 1.3.”  
If they treat “go look at the host” as a tune: “That is investigation. Reject.”

---

## Knowledge Check – Answer Key

1. **Same inbox as nominations. True or false?**  
   **Answer:** False. Same desk. Different inbox.  
   **Explanation:** Outline b.

2. **Live rule, no pointer — pick a tune or send it back?**  
   **Answer:** Send it back. SOC owes the investigation number, or the report title and URL.  
   **Explanation:** Outline d.

3. **Noisy rule — investigate the host. Tune or reject?**  
   **Answer:** Reject. That is an investigation, not a tune.  
   **Explanation:** 4.4.1 task 2.

---

## Additional Instructor Resources

- Next: 4.5 Hunt and intel packages
