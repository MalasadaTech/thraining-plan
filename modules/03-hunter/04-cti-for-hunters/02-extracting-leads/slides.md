# Module 3.4.2 – Extracting Hunt Leads from CTI
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC, CTI sit this too  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.4.2 – Extracting Hunt Leads from CTI  
**Subtitle:** Threat Hunter (SOC / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
After the gate. Not the appendix dump.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Pull only what you can **search here**.

Keep / drop / one **question**.

**Speaker Notes:**  
Awareness or full hand-off: stop.

---

### Slide 3 – Keep vs drop
**Title:** TTP, IOC, behavior

**Keep** — searchable method, current object, scoped pattern.  
**Drop** — no telemetry, expired, noise.  
Copy ATT&CK IDs **only if the report printed them**.

**Speaker Notes:**  
Outline a–c. Map is 3.5.

---

### Slide 4 – What good looks like
**Title:** A12 slice

**Keep** — Run **`Updater`**; `:8080` `/update.exe`; more `invoice.vbs`.  
**Drop** — “persistence”; a /24; a 2019 hash.  
**Question** — if more persistors exist, we see those.

**Speaker Notes:**  
Tasks 1–3.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No Navigator (**3.5**).  
No STIX authoring (**2.10**).  
No invented ticket (**3.7**).

**Speaker Notes:**  
STIX input next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Copying the IOC appendix is extract. True or false?  
2. Name one reason to drop an object.  
3. From the A12 slice: one keep TTP, one keep artifact, and the hunt question.

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Keep searchable leftovers. One question that can fail.

**Next:** **3.4.3** STIX as hunt input

**Speaker Notes:**  
Do not open STIX unless scheduled.
