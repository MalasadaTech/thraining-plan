# Module 1.4.4 – Common Alert Categorizations  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 1.4.4 – Common Alert Categorizations  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Site bucket plus rejected neighbor. Not TP/FP. Not ATT&CK.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Put a **site bucket** on a working alert.

Pick a category.  
Say why the **neighbor** is wrong.

**Speaker Notes:**  
Next desk needs the kind of activity, not the label again.

---

### Slide 3 – Five names
**Title:** Scan, root, user, unsuccessful, other

**Scanning / reconnaissance** — wide probe, no access attempt.  
**Root-level** — SYSTEM / admin / service control.  
**User-level** — normal user token.  
**Unsuccessful** — a failed access attempt.  
**Other** — a name your shop already uses.

**Speaker Notes:**  
Outline a–e. Other is not a new DYA list.

---

### Slide 4 – What good looks like
**Title:** Category + not the neighbor

**User-level, not root** — `wscript` + `-enc` as Medium `jlee`.  
Encoded does not upgrade the token.

**Scanning, not unsuccessful** — many unanswered SYN, no login.  
A sweep is not a failed logon.

**Speaker Notes:**  
Two sentences. Same command as SYSTEM would be root.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No TP / FP (**1.4.2**).  
No FP cause (**1.4.3**).  
No ATT&CK ID as the category (**0.6**).  
No SLA clocks (**1.4.5**).

**Speaker Notes:**  
If they write T1059, send it back to 0.6.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. This hour is for deciding TP vs FP. True or false?  
2. Name the four syllabus categories plus **other**.  
3. `wscript` + `-enc` as Medium `jlee`. Category, and why not the adjacent one?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Site bucket + rejected neighbor.  
Scan is not failed auth. User token is not root.

**Next:** **1.4.5** Service Level Agreements / Response Time Goals

**Speaker Notes:**  
Do not open the clocks unless that hour is scheduled.
