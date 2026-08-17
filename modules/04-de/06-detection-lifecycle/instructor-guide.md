# Instructor Guide – Module 4.6 – Detection lifecycle

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.6 B / C / C ; 4.6.1 3c / 4c / 4d ; 4.6.2 3c / 4c / 4d  
- SOC: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
- Hunter: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
- CTI: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Call modify, retire, or leave on a live rule, cite the reason, and refuse to treat a block as automatic retire.

**Context (plain language):**

- What this hour is for: Regular DE work — manage the detections you already own. Review whether they still earn their keep, need an update, or should come out. Then the three calls and a block is not automatic retire.
- How it hooks to the hour before: 4.5 was a package (add / change / no new rule). This hour is a rule you already own.
- How it hooks to the hour after: 4.7 is sensors — lighter. “Sensor gone” is only a reason here.
- Why we are doing it this way: You wanted a plain opener so this hour is normal DE work, not only a ticket from SOC. “We blocked it” is not automatically retire.
- What we are *not* doing this hour: Writing a rule (1.3). The tune inbox (4.4). Sensor checks (4.7). No lab. No DYA tickets.
- Extra step: none.

Say **modify**, **retire**, and **leave** the way the student guide does. **4.4** used tune / exception / replace / leave / retire — that is the tune inbox. This hour is the lifecycle call with a reason.

**Key Teaching Points:**
- This is regular work on the set you own, not only inbound tickets.
- Three calls. Cite the reason from the list.
- Block ≠ retire. Ask if the rule still earns its keep.
- Sensor gone is a reason, not a 4.7 lesson.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 4.6 ; T 4.6.1 ; T 4.6.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | After 4.5 packages |
| Key Concepts            | 10 min    | Three calls; block ≠ retire |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write modify / retire / leave. Then the reason list. Then: block is not automatic retire.

If they say “blocked, so retire”: “Does it still earn its keep?”  
If they start a 4.4 five-answer tune: “Different hour. This is the standing call.”  
If they start vendor sensor admin: “That is 4.7.”  
If they invent a ticket: “Call and reason, not the ticket.”

---

## Knowledge Check – Answer Key

1. **Three lifecycle calls?**  
   **Answer:** Modify, retire, leave.  
   **Explanation:** Outline a–c.

2. **Blocked means you must retire. True or false?**  
   **Answer:** False. Decide whether the matching rule still earns its keep.  
   **Explanation:** Outline d and 4.6.1 task 2.

3. **Still catches the intended activity; SOC is busy. Modify, retire, or leave?**  
   **Answer:** Leave. Reason: still useful.  
   **Explanation:** Outline c–d and 4.6.1 task 1.

---

## Additional Instructor Resources

- Next: 4.7 Sensor availability and performance
