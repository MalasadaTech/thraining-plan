# Instructor Guide – Module 1.5.3 – Notification and Distribution

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C ; 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 A / B / B ; 1.5.3.2 2b / 3c / 4c  
- CTI: 1.5.3.1 B / C / C ; 1.5.3.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Route a report from the chart: who, leadership yes/no, approved channel, rejected channel. Closes **1.5**. SOC ends.

**Context (plain language):**

- What this hour is for: SOC analysts put the case and the CTI question on an approved path so IR and leadership actually see them.
- How it hooks to the hour before: 1.5.2 was when it is due. This hour is who and how.
- How it hooks to the hour after: CTI starts at 3.1.1. The RFI is the door. Do not open 1.7.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–c. Classroom chart so the route task has a stand-in. Not a live DYA matrix. Hunter K is A / B / B. CTI works the task at 3-level (3c).
- What we are *not* doing this hour: Pick the type. Score the clock. Write the body. Invent an informational row. Invent DYA distro names. Open **1.7** (retired). No lab.
- Extra step: none.

Do not invent a Harbor or DYA notification card. Do not tell the PRD plot. Do not dump the Run key. IR has the host (**Sam** is the classroom IR name if you need one). Leadership gets a short awareness flag, not the hash.

**Key Teaching Points:**
- Chart: who, leadership yes/no, approved channel.
- Right people, wrong path still fails.
- Incident needs IR + lead via ticket. RFI needs the named team via ticket or form, not SMS.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.5.3.1 ; T 1.5.3.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Who and how; SOC ends |
| Key Concepts            | 12 min    | Chart; two routes |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | Close 1.5; next is 3.1.1 |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the two classroom rows. Walk **A12** as **IR + lead + ticket**. Walk the domain RFI as **CTI + no lead + form**, reject SMS.

If they score 30 / 60: “1.5.2.”  
If they rewrite the type: “1.5.1 is done.”  
If they defend SMS: “Right team, wrong path.”  
If they send the incident only to hunter chat: “IR and lead via ticket.”  
If they invent a DYA distro: “Other is a shop row. Overlay their real chart if they have one.”  
If they ask where the changeover log lives: “1.7 is retired. Not this hour.”

If the ticket system is down: they escalate that as blocked (**1.5.2**). They do not invent SMS.

---

## Knowledge Check – Answer Key

1. **This hour is when the report is due. True or false?**  
   **Answer:** False. That is 1.5.2. This hour is who and how.  
   **Explanation:** Stay-in / vs 1.5.2.

2. **What three things does the chart tell you?**  
   **Answer:** Who receives which type. Whether leadership gets awareness. Which channel is approved.  
   **Explanation:** Outline a–c.

3. **First IR handoff for A12. Route and one rejected channel?**  
   **Answer:** Recipients **SOC + IR**. Leadership **yes**. Channel **ticket**. Reject personal email, SMS, or private chat.  
   **Explanation:** Outline a–c / task 1.

---

## Additional Instructor Resources

- Next: 3.1.1 Data, information, and intelligence
