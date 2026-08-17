# Module 3.6.1 – Persistence Techniques
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC, CTI sit this too  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.6.1 – Persistence Techniques  
**Subtitle:** Threat Hunter (SOC / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Runs again. Not a one-off. Not privesc.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Name the **class**. Name the **field that proves it**.

**Speaker Notes:**  
Hunt the named technique in 3.6.3.

---

### Slide 3 – Four classes
**Title:** Registry · startup · task · other

**Registry** — Run / RunOnce value set.  
**Startup folder** — file or `.lnk` in Startup.  
**Scheduled task** — created / updated.  
**Other** — service, WMI, logon script. Say which.

**Speaker Notes:**  
Outline a–d.

---

### Slide 4 – What good looks like
**Title:** A12

HKCU Run **`Updater`** → `%TEMP%\update.exe`.  
**Class** — registry.  
**Proof** — value name + path.

The first alert did not require this key.

**Speaker Notes:**  
Story bible. Task 1.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No “hunt persistence” (**3.6.3**).  
No token theft (**3.6.2**).  
No invented ticket (**3.7**).

**Speaker Notes:**  
Privesc next.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A one-off `wscript invoice.vbs` is persistence. True or false?  
2. Name the four persistence classes.  
3. Class + proof for HKCU Run **`Updater`**.

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Four classes. Class + proof. Not a tactic hunt.

**Next:** **3.6.2** Privilege escalation techniques

**Speaker Notes:**  
Do not open privesc unless scheduled.
