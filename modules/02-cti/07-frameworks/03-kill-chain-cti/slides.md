# Module 2.7.3 – Cyber Kill Chain in Intelligence Analysis  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.7.3 – Cyber Kill Chain in Intelligence Analysis  
**Subtitle:** Progression on the intelligence product  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is how a CTI product uses the seven Kill Chain names. It is not the shared-floor staging lesson, not ATT&CK, and not DTF.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts put attack **progression** on a product so the reader sees what was observed — and what was not.

Hunt and IR use that list. A stage you invent becomes work on a step that is not in the evidence.

**Speaker Notes:**  
This slide is the student intro. The job is the product list, not filling seven blanks. Do not teach ATT&CK IDs or Diamond vertices today.

---

### Slide 3 – Seven stages
**Title:** Seven stages

**Reconnaissance** — target research. Not “they must have looked.”  
**Weaponization** — building the payload. Victim logs almost never show this.  
**Delivery** — the weapon arrived.  
**Exploitation** — it ran as the exploit.  
**Installation** — code or an implant is on the host.  
**Command and Control** — a callback or control channel.  
**Actions on Objectives** — the goal.

**Speaker Notes:**  
They need the names to write the product. This is not a recopy of the floor lesson. One line each. Stop. The next slide is the product rule.

---

### Slide 4 – Only supported stages
**Title:** Only supported stages

A **supported** stage is one you can cite from the report or the activity.

The product lists **only** those stages.

Reject the previous or next stage you did not see.  
Reject an **unobserved** stage.

**Speaker Notes:**  
This is the CTI application. The chain is not a form. Invented Reconnaissance is the usual unobserved stage. Walk the two givens on the next slide.

---

### Slide 5 – Name the stage. Reject the neighbor.
**Title:** Name the stage. Reject the neighbor.

**Given:** `wscript.exe` (Temp `invoice.vbs`) → `powershell.exe -enc …`  
**Installation.** Cite the process. Not Command and Control — no beacon.

**Given:** `GET /update.exe` on port 8080  
**Installation** of the payload, or **Command and Control** if that GET is the channel. Not Reconnaissance.

The product lists **only** cited stages.

**Speaker Notes:**  
Show these givens before the knowledge check. Delivery of the vbs only if arrival is in the evidence. Do not tell the intro plot. Do not map ATT&CK IDs.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. You should list all seven stages on every product. True or false?  
2. `GET /update.exe` on port 8080. Is that Reconnaissance? Why or why not?  
3. `wscript` → `-enc`. Stage, and why not the neighbor?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Seven stages. Only what you can cite.  
Reject the previous or next stage you did not see.  
Do not invent Reconnaissance.

**Next:** **2.7.4** Defender’s ThreatMesh Framework (DTF)

**Speaker Notes:**  
DTF is discovery pivots, not Kill Chain stages. Stay off DTF unless that lesson is scheduled.
