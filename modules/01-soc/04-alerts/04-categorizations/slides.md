# Module 1.4.4 – Common Alert Categorizations  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 6

---

### Slide 1 – Title Slide
**Title:** Module 1.4.4 – Common Alert Categorizations  
**Subtitle:** Category plus why the neighbor is wrong  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson names alert categories. It is not true positive versus false positive, and it is not ATT&CK.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts put a **category** on an alert so the next desk can see what kind of activity it was.

A true-positive or false-positive label is not that name.

This lesson names the category and rejects the neighbor.

**Speaker Notes:**  
This slide is the student intro. A label says whether the detection was right. A category tells the next desk the kind of activity. Do not teach clocks today.

---

### Slide 3 – Five alert categories
**Title:** Five alert categories

**Scanning / reconnaissance** — wide probe, no access attempt.  
**Root-level** — SYSTEM / admin / service control.  
**User-level** — a normal user account.  
**Unsuccessful** — a failed access attempt.  
**Other** — a name your shop already uses.

**Speaker Notes:**  
One line each. Stop. Other is a name the shop already uses, not an ATT&CK ID and not a new DYA list.

---

### Slide 4 – Category plus why not the neighbor
**Title:** Category plus why not the neighbor

**User-level, not root** — `wscript` + `-enc` as Medium `jlee`.  
Encoded does not upgrade the account.

**Scanning, not unsuccessful** — many unanswered SYN, no login.  
A sweep is not a failed logon.

**Speaker Notes:**  
Show both givens before the knowledge check. Two sentences: the category, then why the neighbor is wrong. The same command as SYSTEM would be root.

---

### Slide 5 – Knowledge Check
**Title:** Knowledge Check

1. A category is the same thing as a true-positive or false-positive label. True or false?  
2. Name the four syllabus categories plus **other**.  
3. `wscript` + `-enc` as Medium `jlee`. Category, and why not the adjacent one?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 6 – Summary
**Title:** Summary

A category names the kind of activity and rejects the neighbor.  
A scan is not failed authorization. A user account is not root.

**Next:** **1.4.5** Service Level Agreements / Response Time Goals

**Speaker Notes:**  
Clocks are next. Stay off this category when you get there.
