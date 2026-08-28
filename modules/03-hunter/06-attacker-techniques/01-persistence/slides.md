# Module 3.6.1 – Persistence Techniques  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.6.1 – Persistence Techniques  
**Subtitle:** Name the method that will run again  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is persistence recognition for hunters. It is not how to read a registry event, not privilege escalation, and not a hunt of a named technique.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

Hunters name the method that will **run again** after reboot, logon, or a time trigger.

SOC already described the registry set. This lesson names the **class**.  
Not a one-off run. Not privilege escalation. Not “hunt persistence.”

**Speaker Notes:**  
This slide is the student intro. Registry activity reading was 1.1.5. This lesson is hunt persistence — the method. Do not open a hunt package.

---

### Slide 3 – Four classes
**Title:** Four persistence classes

**Registry-based** — Run / RunOnce / Winlogon value set. The data is the payload.  
**Start menu / startup folder** — file or `.lnk` in user or All Users Startup.  
**Scheduled tasks** — created or updated. Trigger, command, account it runs as.  
**Other common methods** — service, WMI subscription, or logon script. Say which.

**Speaker Notes:**  
Walk the four classes. Stop. Do not inventory every persistence technique. Services, WMI, and logon scripts live under other — name the one you see.

---

### Slide 4 – Recognize the method
**Title:** Class plus proof

Name the **class**. Name the **field that proves it**.

A one-off process is not persistence.  
A privilege change by itself is the next lesson.  
If you cannot see the class, name a **visibility gap**. Do not invent a method.

**Speaker Notes:**  
Recognition is the task. The product is class plus proof, or a named gap. Stay off the 1.1.5 field-by-field write-up. Stay off hunting every Run key.

---

### Slide 5 – What good looks like
**Title:** Name the class from the log

**Given:** HKCU Run **`Updater`** → `%TEMP%\update.exe` on **WS-JLEE**.

**Class** — registry-based persistence.  
**Proof** — value name + payload path.

`wscript` running Temp `invoice.vbs` once is **not** this class.  
A vendor Run key under `Program Files` is still persistence *as a method*.

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: that Run value will launch at logon. Do not tell the intro plot. Do not turn this into a hunt of every Run key.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A one-off `wscript invoice.vbs` is persistence. True or false?  
2. Name the four persistence classes.  
3. Class + proof for HKCU Run **`Updater`** → `%TEMP%\update.exe`.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

A method that will run again.  
Four classes. Class plus proof.  
A one-off run is not persistence.

**Next:** **3.6.2** Privilege escalation techniques

**Speaker Notes:**  
3.6.2 is elevation, not autorun. Stay off privilege escalation unless that lesson is scheduled.
