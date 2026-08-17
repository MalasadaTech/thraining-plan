# Module 1.4.2 – Alert Classification  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 1.4.2 – Alert Classification  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Label plus cite. Not why the FP fired.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Classify the case you just investigated.  
**Cite** the evidence.

Do **not** explain why an FP fired. That is **1.4.3**.

**Speaker Notes:**  
1.4.1 gathered context.

---

### Slide 3 – Four labels
**Title:** TP, FP, TN, FN

**TP** — alert, activity is what the rule is for.  
**FP** — alert, activity is benign.  
**TN** — no alert, ordinary activity.  
**FN** — no alert, bad activity that should have fired.

**Speaker Notes:**  
Outline a–d. TN and FN usually have no queue row.

---

### Slide 4 – FN and evidence
**Title:** A miss, and a cite

**FN** is not a fired alert you dislike. It is a **miss**.

**Evidence** — parent + `-enc`, dest + URI, “no alert on that GET.”  
A slogan is not a cite.

**Speaker Notes:**  
Why the FP fired waits.

---

### Slide 5 – What good looks like
**Title:** Four cases

**TP** — encoded PowerShell from `wscript`.  
**FP** — any-PowerShell on `Get-Help`.  
**TN** — ordinary browse, no alert.  
**FN** — `GET /update.exe` to `203.0.113.88:8080`, no alert.

**Speaker Notes:**  
Do not tell the PRD plot.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. FN is a bad alert sitting in the queue. True or false?  
2. Alert `Encoded PowerShell from script host`, `wscript` + `-enc` confirmed. Classify and cite.  
3. `GET /update.exe` to `203.0.113.88:8080`, no alert. Classify and cite.

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Four labels. Cite the evidence.  
TN and FN usually have no queue row.  
Why an FP fired is next.

**Next:** **1.4.3** Common false positive causes

**Speaker Notes:**  
Cause class next, not another label.
