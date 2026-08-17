# Module 0.6.1 – MITRE ATT&CK  
## Slide Deck Content

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Estimated Delivery Time:** 20 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 0.6.1 – MITRE ATT&CK  
**Subtitle:** Shared floor (everyone)  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Last hour was overlap. This hour is a shared label for behavior, not a product.

---

### Slide 2 – What this hour is
**Title:** What this hour is

One language for what the adversary was trying to do, and how.  
Map a row. Cite a field.

**Speaker Notes:**  
They need this because four desks will look at the same host. Hunt planning is later.

---

### Slide 3 – Structure
**Title:** Matrix

**Tactic** = why (the goal).  
**Technique** = how (`T1059`).  
**Sub-technique** = a more specific how (`T1059.001`).

**Speaker Notes:**  
Do not memorize the whole matrix. Columns and cells.

---

### Slide 4 – A map
**Title:** A finished map

Tactic + ID + name + **one cited field**.

An ID with no field is a slogan.

**Speaker Notes:**  
If two IDs fit, pick the primary for this row.

---

### Slide 5 – Example
**Title:** Encoded PowerShell

`wscript` launched encoded PowerShell.

**Map:** Execution / `T1059.001`.  
**Cite:** the encoded command line.  
**Not:** Command and Control (no beacon row).

**Speaker Notes:**  
This is the task. One line of activity. Not an alert queue.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. What is a tactic, and what is a technique?  
2. Why is an ATT&CK ID with no cited field not a finished map?  
3. Encoded PowerShell ran from a script. Name a tactic and a technique and what you would cite.

**Speaker Notes:**  
Answers only in the instructor guide.

---

### Slide 7 – Next
**Title:** Next

**0.6.2** Diamond Model

**Speaker Notes:**  
Four vertices. Not another ATT&CK column.
