# Module 1.4.3 – Common False Positive Causes  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 1.4.3 – Common False Positive Causes  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Already an FP. Class + change. Do not deploy.

---

### Slide 2 – What this hour is
**Title:** What this hour is

The case is **already an FP**.

Pick a **cause class** and **one change**.  
Do **not** re-argue TP vs FP.

**Speaker Notes:**  
1.4.2 was the label.

---

### Slide 3 – Two classes
**Title:** Analyst/tool vs overly broad

**a** — tested a live rule; replay; shop-owned scanner.  
Change: exclude that identity or window.

**b** — any PowerShell; GET on any TCP; MZ-only.  
Change: add a selector. Hand it to DE.

**Speaker Notes:**  
Outline a–b. No third official class.

---

### Slide 4 – What good looks like
**Title:** Class + one sentence

**b** — `Get-Help` on any-PowerShell.  
Change: require `-enc` and parent `wscript`.

**a** — replay of `GET /update.exe` into production.  
Change: exclude the replay. Do not delete the signature.

**Speaker Notes:**  
“Tune it” is not a change. Do not tell the PRD plot.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No reclassify.  
No deploy.  
No scan/root/user category (**1.4.4**).

**Speaker Notes:**  
Categories next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. This hour is for deciding TP vs FP. True or false?  
2. What are the two syllabus cause classes?  
3. FP: any-PowerShell on `Get-Help`. Class and one change sentence.

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

After FP: class + change.  
Analyst/tool vs overly broad.  
Name the change. You do not deploy it.

**Next:** **1.4.4** Common alert categorizations

**Speaker Notes:**  
Category is not cause.
