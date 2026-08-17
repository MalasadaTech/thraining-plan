# Module 3.6.2 – Privilege Escalation Techniques
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC, CTI sit this too  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.6.2 – Privilege Escalation Techniques  
**Subtitle:** Threat Hunter (SOC / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Lower to higher. Not autorun.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Recognize the **elevation**.

Method + indicator. Not the Run key.

**Speaker Notes:**  
A12 Updater is persist.

---

### Slide 3 – Methods
**Title:** Token · UAC · service · other

**Token** — user parent → SYSTEM child.  
**UAC bypass** — auto-elevate parent, no consent.  
**Service abuse** — SYSTEM image in a user-writable path.  
**Other** — say which.

**Speaker Notes:**  
Outline a–b.

---

### Slide 4 – What good looks like
**Title:** Classroom row

User `helpdesk.exe` → `cmd.exe` SYSTEM, no consent.  
**Method** — token theft.  
**Not** — HKCU Run **`Updater`**.

**Speaker Notes:**  
Classroom only. Not an A12 fact.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No persist how-to (**3.6.1**).  
No “hunt privesc” (**3.6.3**).  
No invented ticket (**3.7**).

**Speaker Notes:**  
Named hunt next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. HKCU Run **`Updater`** is privilege escalation. True or false?  
2. Name two privilege-escalation methods.  
3. User parent → SYSTEM `cmd.exe`, no consent: method + indicator.

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Elevation, not autorun. Method + indicator.

**Next:** **3.6.3** Hunt one named technique

**Speaker Notes:**  
Do not open 3.6.3 unless scheduled.
