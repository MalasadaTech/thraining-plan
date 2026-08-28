# Module 1.4.2 – Alert Classification  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.4.2 – Alert Classification  
**Subtitle:** Whether the detection was right  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is the four classification labels and a cite of evidence. It is not why a false positive fired, and it is not scan / root / user.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

After you have looked at a case, you **classify** it.

A classification says whether the detection was right. You **cite the evidence**.

This lesson is the four labels.

**Speaker Notes:**  
This slide is the student intro. Without a label, the next person cannot tell a real hit from a miss. Without a cite, “malicious” is a slogan. Context gathering was the previous lesson. Why a false positive fired waits.

---

### Slide 3 – Four labels
**Title:** TP, FP, TN, FN

**True Positive** — a fired alert, and the activity is what the rule is for.  
**False Positive** — a fired alert, and the activity is benign.  
**True Negative** — no alert, ordinary activity.  
**False Negative** — no alert, bad activity that should have fired.

Fired alerts sit in an **alert queue**. TN and FN usually do not.

**Speaker Notes:**  
Walk detection-said versus reality. Stop on true negative and false negative so they do not assume every case is a queue item. Do not open cause class or category.

---

### Slide 4 – A miss, and a cite
**Title:** A miss, and a cite

A **false negative** is not a fired alert you dislike. It is a **miss**.

**Evidence** is a short cite — parent plus `-enc`, destination plus URI, “no alert on that GET.”  
A slogan is not a cite.

**Speaker Notes:**  
This is the task extension: cite the field or log. If they call a disliked queue alert an FN, send them back to the table. Why the false positive fired is the next lesson.

---

### Slide 5 – Four cases
**Title:** Classify and cite

**TP** — alert `Encoded PowerShell from script host`; `wscript` plus `-enc`.  
**FP** — any-PowerShell alert on interactive `Get-Help`.  
**TN** — ordinary browse, no alert.  
**FN** — `GET /update.exe` to `203.0.113.88:8080`, no alert.

Do not invent an alert so you can classify it.

**Speaker Notes:**  
Show these givens before the knowledge check. The product is the label plus the cite. Do not tell the course-fiction plot. Do not explain why the PowerShell rule is broad.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. FN is a bad alert sitting in the queue. True or false?  
2. Alert `Encoded PowerShell from script host`, `wscript` + `-enc` confirmed. Classify and cite.  
3. `GET /update.exe` to `203.0.113.88:8080`, no alert. Classify and cite.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Four labels.  
Cite the evidence.  
True negatives and false negatives usually have no alert in the queue.

**Speaker Notes:**  
The next lesson is why a false positive fired — the cause class, not another label.

---

### Slide 8 – Next
**Title:** Next

**1.4.3** Common false positive causes

**Speaker Notes:**  
1.4.3 is why this false positive happened and what you would change. Stay off the four labels when you get there.
