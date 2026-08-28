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

- What this lesson is for: SOC analysts put the case record and the CTI question on an approved path so IR and leadership actually see them.
- How it hooks to the lesson before: 1.5.2 was when the report is due. This lesson is who receives it and which channel carries it.
- How it hooks to the lesson after: CTI starts at 2.1.1. The RFI is the door. Do not open 1.7.
- Why we are doing it this way: after type and clock, the remaining job is the route. A classroom chart is a stand-in so the route task has something to read. Overlay a real shop chart if they have one. It is not a live DYA matrix.
- What we are *not* doing in this lesson: pick the type. Score the 30 / 60 clock. Write the body. Invent an informational row. Invent DYA distro names. Open **1.7** (retired). No lab.
- Extra step: none.

Use the same names as the student guide: **notification chart**, **leadership awareness**, **approved channel**, **recipients**. Do not invent a Harbor or DYA notification card. Do not tell the PRD plot. Do not dump the Run key. IR has the host (**Sam** is the classroom IR name if you need one). Leadership gets a short awareness flag, not the hash.

**Key Teaching Points:**
- The chart names who, leadership yes/no, and the approved channel.
- Right people on the wrong path still fails.
- Incident needs IR and the duty lead via ticket. RFI needs the named team via ticket or form, not SMS.

**Common Student Challenges:**
- Treat this lesson as the clock. Why: 1.5.2 just taught 30 / 60. Example: answering “when is it due?” instead of who and which channel.
- Send the right team on the wrong path. Why: they already know CTI owns the RFI. Example: texting a CTI friend instead of the ticket or form.
- Send the incident only to a chat. Why: they think IR already saw the host. Example: posting A12 in hunter chat with no IR and no duty-lead ticket.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.5.3.1 – Notification and distribution
- T: 1.5.3.2 – Route a report: name recipients, leadership awareness, and the approved channel

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Approved path; who and how |
| Key Concepts            | 12 min    | Chart; two routes |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | Close 1.5; next is 2.1.1 |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: the case and the CTI question have to travel an approved path, or IR and leadership never see them.
- Write the two classroom rows. Stop there. Do not invent an informational type.
- Walk **A12** as IR plus duty lead plus ticket. Walk the domain RFI as CTI plus no lead plus form or ticket. Reject SMS.
- If they score 30 / 60, that is 1.5.2. This lesson is who and how.
- If they rewrite the type, 1.5.1 is done.
- If they defend SMS, it is the right team on the wrong path.
- If they send the incident only to hunter chat, IR and the duty lead still need the ticket.
- If they invent a DYA distro, **other** is a shop row. Overlay their real chart if they have one.
- If they ask where the changeover log lives, **1.7** is retired. It is not a 1.5 channel.
- If the ticket system is down, they escalate that as blocked (**1.5.2**). They do not invent SMS.

---

## Knowledge Check – Answer Key

1. **This lesson is when the report is due. True or false?**  
   **Answer:** False. That is 1.5.2. This lesson is who and how.  
   **Explanation:** The clock is already taught. This lesson is recipients, leadership, and channel.

2. **What three things does the notification chart tell you?**  
   **Answer:** Who receives which type. Whether leadership gets awareness. Which channel is approved.  
   **Explanation:** Those three columns are the whole chart. The task then adds a rejected channel.

3. **First IR handoff for A12. Recipients, leadership yes/no, channel, and one rejected channel?**  
   **Answer:** Recipients **SOC + IR**. Leadership **yes**. Channel **ticket**. Reject personal email, SMS, or private chat.  
   **Explanation:** The incident row is IR plus the duty lead on the case system, not a side channel to one analyst.

---

## Additional Instructor Resources

- Next: 2.1.1 Data, information, and intelligence
