# Module 0.6.1 – MITRE ATT&CK  
## Slide Deck Content

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Estimated Delivery Time:** 15–20 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 0.6.1 – MITRE ATT&CK  
**Subtitle:** Shared language for adversary behavior  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This is the shared frameworks block. This lesson is ATT&CK as a shared language for behavior. It is not hunt planning and not a CTI product.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

People on different desks will look at the same host or log.

They need one name for **what the adversary was trying to do** and **how**.

This lesson is that shared language. Label what you saw. Cite a field.

**Speaker Notes:**  
This slide is the student intro. Four desks can look at the same host. They still need one name for the goal and the how. Do not plan hunt coverage today.

---

### Slide 3 – Shared language for behavior
**Title:** Shared language for behavior

ATT&CK is a knowledge base of adversary **behavior**.

You use it to name what you saw.  
You do not use it to decorate a ticket.

**Speaker Notes:**  
Purpose first. Structure is the next slide. Stay off Diamond vertices and Kill Chain stages.

---

### Slide 4 – Tactic and technique
**Title:** Enterprise matrix

**Tactics** are columns. **Techniques** and **sub-techniques** are cells.

**Tactic** = why (the goal).  
**Technique** = how (`T1059` Command and Scripting Interpreter).  
**Sub-technique** = a more specific how (`T1059.001` PowerShell).

You do not memorize every cell.

**Speaker Notes:**  
Write why versus how on the board. Execution is a tactic. `T1059.001` is a how. Do not list every tactic.

---

### Slide 5 – A finished map
**Title:** A finished map

Read the line of activity.

Name the **tactic** and the **technique** or **sub-technique**. Cite **one field**.

If two IDs fit, pick the **primary** and reject the neighbor.

An ID with no cited field is not a map.

**Speaker Notes:**  
Map means that label, not a SIEM table. The outline may still say row; here it is the log in front of you. One field. Not the rest of the incident.

---

### Slide 6 – Encoded PowerShell
**Title:** Encoded PowerShell

**Given:** `wscript` launched encoded PowerShell.

**Label:** Execution / `T1059.001` PowerShell.  
**Cite:** the encoded command line.  
**Not:** Command and Control. This line does not show a beacon.

**Speaker Notes:**  
This is the task. One line of activity. Not an alert queue, not a hunt plan, and not a CTI product.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. What is a tactic, and what is a technique?  
2. An ATT&CK ID with no cited field is a finished map. True or false?  
3. Encoded PowerShell ran from a script. Name a tactic and a technique (or sub-technique) and what you would cite.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

ATT&CK labels behavior.  
A tactic is why. A technique is how.  
Name both for the line in front of you and cite the field.

**Next:** **0.6.2** Diamond Model

**Speaker Notes:**  
Diamond is four vertices and the weakest one. It is not another ATT&CK column.
