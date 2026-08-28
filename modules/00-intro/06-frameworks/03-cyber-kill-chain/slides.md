# Module 0.6.3 – Cyber Kill Chain  
## Slide Deck Content

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Estimated Delivery Time:** 15 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 0.6.3 – Cyber Kill Chain  
**Subtitle:** Where this activity sits in time  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Diamond organized what you know into four corners. This lesson stages the same activity in time. It does not teach ATT&CK IDs, and it is not the later CTI product lesson.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

You often see **one step** of an attack.

Name **where that step sits** in the sequence.

Do not call a first payload the whole intrusion.

**Speaker Notes:**  
This slide is the student intro. Place the activity you have on one stage. Refuse the previous or next stage you did not see. Do not fill the rest of the chain today.

---

### Slide 3 – A staging tool
**Title:** A staging tool

The Cyber Kill Chain stages attack **progression**.

It is a staging tool, not a complete model of every intrusion.

**Speaker Notes:**  
Purpose first, then the names. If they ask whether every intrusion has all seven stages, the answer is no — that is why you only place what you saw.

---

### Slide 4 – Seven stages
**Title:** Seven stages

**Reconnaissance** — research the target  
**Weaponization** — build the payload  
**Delivery** — the weapon arrives  
**Exploitation** — it runs  
**Installation** — implant on the host  
**Command and Control** — a callback  
**Actions on Objectives** — the goal

**Speaker Notes:**  
Lockheed Martin Cyber Kill Chain, in that order. Do not add extra stages. Do not rename these as ATT&CK tactics. If they ask about SIEM tables, the activity in front of you is often one row; here it means the same thing as the one-line activity.

---

### Slide 5 – Place this activity
**Title:** Place this activity

A `.vbs` in email is **Delivery**.

Not **Weaponization** — you did not see them build it.  
Not **Exploitation** — you did not see it run.

Do not invent the rest of the chain.

**Speaker Notes:**  
Previous and next are the reject pair. Command and Control is not the next stage after Delivery, and there is no callback anyway. One line of activity. Not an alert queue, and not an intelligence product that lists every supported stage.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. What is the Cyber Kill Chain for?  
2. Name the seven stages in order.  
3. A user received a `.vbs` in email. Why is that Delivery, and why is it not Exploitation?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Seven stages.  
Place the activity you have.  
Reject the previous or next stage you did not see.

**Next:** **0.7** External tools

**Speaker Notes:**  
0.7 is purpose and when to pick a tool. Stay off VirusTotal Relations and platform depth.
