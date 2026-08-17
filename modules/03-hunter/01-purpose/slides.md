# Module 3.1 – Purpose of Threat Hunting  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC, CTI sit this too  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.1 – Purpose of Threat Hunting  
**Subtitle:** Threat Hunter (SOC / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Missed activity and gaps. Not a rewritten ticket.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Find what **alerts missed**.

Name **gaps** detections cannot see.  
Different product from the SOC ticket.

**Speaker Notes:**  
CTI answered the domain. Hunt looks for more hosts.

---

### Slide 3 – Two jobs
**Title:** Missed activity vs gaps

**Missed** — it happened; no queue row.  
**Gap** — even looking, the detection would not have fired.

**Speaker Notes:**  
Outline a–b.

---

### Slide 4 – What good looks like
**Title:** A12

**Missed** — `GET /update.exe :8080`, no alert.  
**Look for** — HKCU Run **`Updater`**, more `invoice.vbs`, `update.exe` on other hosts.

The first alert did not require the Run key.

**Speaker Notes:**  
Story bible. Tasks 1–2.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No hunt type (**3.2.1**).  
No hunt card (**3.2.2**).  
No invented ticket (**3.7**).

**Speaker Notes:**  
Types next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Hunt rewrites the SOC ticket with a better story. True or false?  
2. What two jobs does hunting exist to do?  
3. Name one **A12** miss, and one hunt look-for that was **not** on the first alert.

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Missed activity. Gaps. A package, not a rewritten ticket.

**Next:** **3.2.1** Hunt types

**Speaker Notes:**  
Do not open types unless scheduled.
