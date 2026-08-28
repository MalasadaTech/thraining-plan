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

- What this lesson is for: Detection engineers own live detections. You review a detection you already own and call modify, retire, or leave, and you cite the reason. A noisy rule, a gone threat, or a rule that only watched something now blocked should not sit unchanged — and a still-useful rule should not come out just because the queue is busy.
- How it hooks to the lesson before: 4.5 is a hunt or intel package (add, change, or no new rule). This lesson is a live rule you already own.
- How it hooks to the lesson after: 4.7 is sensors. “Sensor gone” is only a reason here.
- Why we are doing it this way: this is regular DE work on detections you already own, not only a ticket from SOC. Write it so a reader can follow without sitting the tune-request or package lessons first. A block is not automatic retire.
- What we are *not* doing in this lesson: writing a rule (1.3). The SOC tune-request inbox (4.4). How to check a dead sensor (4.7). No lab. No tickets. Do not invent an expiry field.
- Extra step: none.

Use the same names as the student guide: **modify**, **retire**, **leave**, **live** rule, and **block**. **Standing call** is the outline phrase for this regular review; say **regular review** with students. **Earn its keep** means the rule still does useful work. **4.4** used tune / exception / replace / leave / retire — that is a SOC request to change a live rule. This lesson is the review of a rule you already own, with a reason.

**Key Teaching Points:**
- This is regular work on the set you own, not only inbound tickets.
- Three calls. Cite the reason from the list.
- A block is not automatic retire. Ask if the rule still earns its keep.
- Sensor gone is a reason, not a 4.7 lesson.

**Common Student Challenges:**
- Treat a block as automatic retire. Why: a block sounds like the problem is solved. Example: retiring the rule the same day the firewall blocked the IP, without asking if the rule still watches other hosts or paths.
- Answer with tune, exception, or replace. Why: leave and retire also appear on a SOC tune request. Example: picking “exception” on a standing review that has no SOC request.
- Change a still-useful rule because SOC is tired of it. Why: volume feels like a reason to take it out. Example: retiring a rule that still catches the intended activity because the queue is busy.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 4.6 – Detection lifecycle
- T: 4.6.1 – Call modify / retire / leave and cite the reason
- T: 4.6.2 – Given a block, decide whether the matching rule still earns its keep

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Review a live rule you already own |
| Key Concepts            | 10 min    | Three calls; block is not automatic retire |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: live rules you already own still have to be reviewed. Call modify, retire, or leave, and cite the reason.
- Write the three calls. Then the reason list. Then: a block is not automatic retire.
- Walk the four “given” lines from the student guide. The product is the call and the reason, not a ticket.
- If they treat a block as retire, ask whether the matching rule still earns its keep.
- If they answer with tune, exception, or replace, stop. Those are answers to a SOC tune request (**4.4**). This lesson is modify, retire, or leave.
- If they start checking or administering a sensor, that is **4.7**. Here “sensor gone” is only a reason.
- If they invent a ticket or an expiry field, the product is the call and the reason, not a form.

---

## Knowledge Check – Answer Key

1. **Name the three lifecycle calls.**  
   **Answer:** Modify, retire, leave.  
   **Explanation:** Those are the three products of a regular review. Tune, exception, and replace are not this lesson.

2. **“We blocked this infrastructure” means you must retire the matching rule. True or false?**  
   **Answer:** False. Decide whether the matching rule still earns its keep.  
   **Explanation:** A block is not automatic retire. Keep the rule if it still watches something else. Retire it only if it existed solely for what is now blocked.

3. **A live rule still catches the intended activity. SOC wants it gone because it is busy. Modify, retire, or leave?**  
   **Answer:** Leave. Reason: still useful.  
   **Explanation:** Volume or a tired queue is not a reason to change or retire a rule that still does its job.

---

## Additional Instructor Resources

- Next: 4.7 Sensor availability and performance
