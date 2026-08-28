# Module 2.7.1 – MITRE ATT&CK for CTI Analysis and Reporting  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.7.1 – MITRE ATT&CK for CTI Analysis and Reporting  
**Subtitle:** Map a report or activity set for a CTI product  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is the CTI application of ATT&CK. It puts IDs on a report or activity set. It is not a second copy of the shared floor, and it is not hunt planning.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts put ATT&CK IDs on a **product** so hunt and detection can reuse the same names.

You extract named behaviors from a **report or activity set**.

Write only the IDs this product can support.

**Speaker Notes:**  
This slide is the student intro. The job is a mapped line other desks can trust. Do not open hunt coverage, DTF, or Diamond on this slide.

---

### Slide 3 – A CTI ATT&CK line
**Title:** A CTI ATT&CK line

**Tactic** — why (the goal).  
**Technique or sub-technique** — how (the named way).  
**Evidence** — the field or sentence in this product.  
**Neighbor** — a nearby ID this product does not show. Reject it.

A finished line is tactic + ID + cite. An ID with no evidence is a slogan.

**Speaker Notes:**  
Define the four pieces so this lesson stands alone. Do not teach Enterprise matrix columns. TTP here means a named behavior you extract onto those IDs.

---

### Slide 4 – Two givens
**Title:** What good looks like

**`wscript` launched encoded PowerShell (`-enc`).**  
Execution / **T1059.001**. Cite `-enc` and parent. Not Command and Control — no beacon.

**GET `/update.exe` on port 8080, product is the download.**  
Command and Control / **T1105**. Cite the URI. Not **T1059** — that ID is a command interpreter, not a GET.

Do not collapse process and download into one ID.

**Speaker Notes:**  
Walk both givens before the knowledge check. T1105 is a technique under Command and Control, not a second tactic. If they jump to “it might beacon,” stay on what this product shows.

---

### Slide 5 – Knowledge Check
**Title:** Knowledge Check

1. An ATT&CK ID with no cited evidence is a finished CTI map. True or false?  
2. What three things must a CTI ATT&CK line have?  
3. `wscript` launched encoded PowerShell (`-enc`). Name the tactic, the ID, and why it is not Command and Control?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 6 – Summary
**Title:** Summary

Extract TTPs from a report or activity set onto ATT&CK IDs.  
Tactic, technique or sub-technique, and evidence.  
Reject the neighbor this product does not show.

**Speaker Notes:**  
Hunt planning, DTF, SOC categories, and which TTPs apply here are other lessons. Diamond is next if that lesson is scheduled.

---

### Slide 7 – Next
**Title:** Next

**2.7.2** Diamond Model for CTI

**Speaker Notes:**  
2.7.2 fills vertices from a report or activity set. It does not assign ATT&CK IDs. Do not open Diamond unless that lesson is scheduled.
