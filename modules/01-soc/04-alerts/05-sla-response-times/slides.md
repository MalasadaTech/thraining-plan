# Module 1.4.5 – SLA / Response Time Goals  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 1.4.5 – SLA / Response Time Goals  
**Subtitle:** Start investigation vs close or escalate  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson closes unit 1.4. It names two response-time clocks on an alert. It does not teach report timelines. Those are 1.5.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts keep an alert from sitting **untouched**, and from sitting **open** with no close or escalate.

Name **which** clock is at risk.  
Record **closed** or **escalated** against it.

Not “work faster.” Not a report.

**Speaker Notes:**  
This slide is the student intro. The job is to name the clock and record a disposition. Do not open a live shop SLA. Do not start a report.

---

### Slide 3 – Two clocks
**Title:** Start vs close / escalate

**Start** — created → first touch. Classroom **15 min**.  
**Close / escalate** — first touch → closed or escalated. Classroom **45 min**.

Untouched → only **start** exists.

Those minutes are this lesson only. They are not a live shop policy.

**Speaker Notes:**  
Two origins. Start begins at created. Close/escalate begins at first touch. If nobody has touched the alert, do not talk about the close/escalate clock yet.

---

### Slide 4 – Which clock is at risk
**Title:** Which clock is at risk

**Start at risk** — created `14:00`, no start, now `14:18`.  
Record `started`. Do not close yet.

**Close/escalate at risk** — first touch `13:28`, still open at `14:20`.  
Record `escalated` (or `closed` if the investigation is done).

**Speaker Notes:**  
Walk both givens before the knowledge check. The first has no first touch, so only start can be late. The second already started, so the remaining clock is close/escalate. Do not retell an earlier investigation plot.

---

### Slide 5 – Alert clocks only
**Title:** Alert clocks only

No re-investigate (**1.4.1**).  
No TP / FP or category (**1.4.2** / **1.4.4**).  
No report, and no report clocks (**1.5**).  
No invented shop minutes.

**Speaker Notes:**  
Report timelines are a different lesson. Classroom 15 / 45 stand in so the timestamp task has numbers. A real shop substitutes its own minutes.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. If nobody has touched the alert, which clock can be at risk?  
2. What are the two clocks, and when does each start?  
3. An alert was first touched at `13:28` and is still open at `14:20`. Which clock is at risk, and what do you record?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Start from created. Close/escalate from first touch.  
Name the clock. Record the disposition.

**Next:** **1.5.1** Report types. Unit **1.4** ends.

**Speaker Notes:**  
Do not open 1.5 unless that lesson is scheduled. 1.7 is retired.
