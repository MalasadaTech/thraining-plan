# Module 1.8.5 – Incident Response Processes  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.8.5 – Incident Response Processes  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Closes 1.8. Overlay site playbook if you have one.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Follow the site IR card
2. Next step + who owns containment
3. Reject freelance

**Mapped Items:**  
T: 1.8.5.1

**Speaker Notes:**  
CTI 3-level is 1a. Hunter is 3c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Harbor IR card + Sev
- Three examples
- Four process lines
- Knowledge check — close 1.8

**Speaker Notes:**  
Unit complete after this.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Who gets the **report** (**1.6.3**)  
Where **notes** live (**1.8.4**)  
Which host is a **jewel** (**1.8.1.f**) — you already have that

**Key Point:** Follow the card.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Steps
**Title:** Harbor IR Steps

1. Confirm incident + ticket  
2. Page IR (ticket + duty lead)  
3. Read **Sev** — that row owns containment  
4. Record actions (**1.8.4**)  
5. No wipe. No OT/jewel isolate without IR

**Speaker Notes:**  
Classroom only.

---

### Slide 6 – Severity
**Title:** Who Owns Containment

**Sev1** jewel / OT / widespread → **IR lead**  
**Sev2** single user host → SOC **with IR concurrence**  
**Sev3** no live host → SOC documents

**Speaker Notes:**  
Overlay site names.

---

### Slide 7 – Process Line
**Title:** Five Fields

`situation | Sev | next | owner | rejected freelance`

**Speaker Notes:**  
Task.

---

### Slide 8 – Freelance
**Title:** Not These

Unplug `pay-db-01`  
Isolate OT “to be safe”  
Take a DC offline on an informational

**Speaker Notes:**  
Usual leads.

---

### Slide 9 – Example 1: A12
**Title:** Example 1 – Sev2

Page IR. Isolate only with concurrence.  
Not unplug-first.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Payroll Cable
**Title:** Example 2 – Sev1 Freelance

Instinct ≠ process.  
IR owns the jewel.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3: OT
**Title:** Example 3 – One Host, Still Sev1

OT is Sev1 on this card.  
SOC does not isolate it.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Cable first  
- OT as Sev2  
- Isolate DC on informational  
- Rewriting 1.6.3  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use the site playbook if posted.  
Keep: next step + owner + no freelance.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize Ex 1–3.
2. A–D: process line.
3. No notes-location redo.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Sev rows — who owns containment?
2. Next step after confirm incident?
3. Why not unplug pay-db-01?
4. How is this not 1.6.3?
5. Who owns the live playbook?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Next step + owner. Reject freelance.
- Unit **1.8** ends.

**Speaker Notes:**  
Do not open 2.1 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** IR — Quick Reference

| Sev | Harbor | Owner |
|-----|--------|-------|
| 1 | Jewel / OT / widespread | IR lead |
| 2 | Single user host | SOC + IR concurrence |
| 3 | No live host | SOC documents |

**Coming next:** Outline unit 2.1 – Purpose of Threat Hunting

**Footer:** SOC / Hunter / CTI Training Program
