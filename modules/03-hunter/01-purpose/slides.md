# Module 3.1 – Purpose of Threat Hunting  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.1 – Purpose of Threat Hunting  
**Subtitle:** Why hunters look past the alert queue  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This is the start of the hunter track. This lesson names why hunting exists. It does not pick a hunt type or write a hunt card.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC works the **alerts that already fired**.

Some malicious or suspicious activity **never appears** in that list.

Hunters look for that missed activity, and they name the **holes** that let it hide.

**Speaker Notes:**  
This slide is the student intro. Hunting exists next to the queue and the intel note, not instead of them. Do not pick a hunt type today.

---

### Slide 3 – Missed activity
**Title:** Missed activity

Malicious or suspicious activity happened.

**No** alert fired. That is a **false negative**.

It is not a fired alert you dislike.

**Speaker Notes:**  
They already classified false negatives in 1.4.2. Hunting is one place you go looking for those misses. Stay off hunt types.

---

### Slide 4 – Detection gaps and visibility gaps
**Title:** Detection gaps and visibility gaps

**Detection gap** — the logs exist; no detection would have caught it.

**Visibility gap** — you cannot see it even if you look. The telemetry is not there.

Name the hole. Do not pretend the hunt ran.

**Speaker Notes:**  
Both are holes. They are not the same hole. ATT&CK mapping of a hunt waits for 3.5.1. Today is only the names.

---

### Slide 5 – Examples existing controls missed
**Title:** Examples existing controls missed

The first **A12** alert is the process create. It did **not** require the Run key.

**Missed** — `GET /update.exe` to `203.0.113.88:8080`, no alert.

**Look for** — HKCU Run **`Updater`**, `update.exe`, or another `invoice.vbs` on other hosts.

The product is a **package**, not a rewritten SOC ticket.

**Speaker Notes:**  
Show this given before the knowledge check. The download is the miss. The Run key is a look-for the first alert did not require. If they retell the process chain, that is still the SOC ticket.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Threat hunting rewrites the SOC ticket with a better story. True or false?  
2. What two jobs does hunting exist to do in the security program?  
3. HTTP shows `GET /update.exe` to `203.0.113.88:8080`, and no alert fired. The first process alert did not require the HKCU Run value `Updater`. Name the missed activity, and name one thing a hunt should look for that was not on that first alert.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Find what the alerts missed.  
Name detection and visibility gaps.  
The product is a package, not a rewritten ticket.

**Next:** **3.2.1** Hunt types

**Speaker Notes:**  
Hunt types are next. Do not open that lesson unless it is scheduled.
