# Instructor Guide – Module 1.5.3 – Notification and Distribution

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C · 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 A / B / B · 1.5.3.2 2b / 3c / 4c  
- CTI: 1.5.3.1 B / C / C · 1.5.3.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the chart, leadership flag, and approved channels. Force a **route line** plus a rejected channel. Close **1.5**.

**Key Teaching Points:**
- Classroom chart is a stand-in. Overlay the site matrix if you have one.
- Leadership = duty SOC lead, not “email the CISO” unless the chart says so.
- SMS / private chat is the usual wrong channel.
- Hunter K is A/B/B. CTI task 3c at 3-level.

**Common Student Challenges:**
- Right people, unofficial path.
- Incident with no IR and no lead.
- Using 1.7’s log location as the channel.
- Scoring the 1.5.2 clock.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site notification matrix
- Answer key (this guide)

---

## Learning Objectives

1. Read the chart.
2. Leadership yes/no.
3. Approved vs rejected channel.
4. Route line.

**Mapped Items:** K 1.5.3.1 · T 1.5.3.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & chart           | 12 min   | a–c |
| Route line                     | 8 min    | |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | Close 1.5 |
| **Total**                      | **~62 min** | Stretch Ex 2 if they defend SMS |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: copy the chart row + name one rejected channel.
- Overlay site names (IR queue, “CIRT”, etc.) if you can.

**Question:**  
“If the ticket system is down, which *approved* fallback does the chart allow?” (If none, they escalate that as blocked — **1.5.2** — they do not invent SMS.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail WhatsApp as approved. Fail hunter-chat-only for incidents.

**Summaries:**
- Ex 1: IR + lead, ticket; reject personal email only.
- Ex 2: CTI, leadership no, form/ticket; reject SMS.
- Ex 3: missing IR + lead; hunter chat not enough.

**Cases:**

| Item | Recipients | Lead | Channel | Reject |
|------|------------|------|---------|--------|
| A | SOC queue + IR | Yes | Ticket | Chat-only |
| B | IT | No | Ticket / RFI form | SMS |
| C | soc-aware distro | Yes | Approved email | IR ticket (wrong type path) |
| D | Leadership *and* IR still need **ticket**; WhatsApp is **rejected** even if “faster” | Yes (but via approved path) | Ticket | WhatsApp |

---

## Knowledge Check – Answer Key

1. **Chart tells you?**  
   **Answer:** Who receives which type, whether leadership gets awareness, which channel is approved.  
   **Explanation:** Outline a–c.

2. **Leadership in classroom?**  
   **Answer:** **Yes** for incident and informational. **No** for RFI unless the chart says so. Duty SOC lead.  
   **Explanation:** Outline b.

3. **Approved vs not?**  
   **Answer:** Approved: ticket, RFI form, named distro. Not: personal SMS, private chat, off-domain mail.  
   **Explanation:** Outline c.

4. **Hunter chat not enough?**  
   **Answer:** Incident chart requires IR + leadership via **ticket**. Chat is not the approved channel.  
   **Explanation:** Example 3.

5. **Changeover record location?**  
   **Answer:** **1.7**, not this chart.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Site notification matrix
- Next recommended module: 1.7.1 Shift changeover process
