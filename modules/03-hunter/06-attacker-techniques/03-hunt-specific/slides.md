# Module 3.6.3 – Hunt for a Specific Persistence or Privilege-Escalation Technique  
## Slide Deck Content

**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title
**Title:** 3.6.3 – Hunt for a Specific Persistence or Privilege-Escalation Technique  
**Subtitle:** Mentor-style, evidence-bound hunting tradecraft

---

### Slide 2 – Technique vs procedure
T1547.001 is the technique; Updater→Temp update.exe is the observed procedure.

---

### Slide 3 – Exact-observed hunt
High specificity: exact value/path/artifact.

---

### Slide 4 – Behavior-broadened hunt
Find variants: rare Run values launching from user-writable Temp paths.

---

### Slide 5 – Trade-off
Exact = precise/may miss variants | broadened = more coverage/more benign review.

---

### Slide 6 – Scope
User workstations | 14 days | registry + file telemetry.

---

### Slide 7 – Wrong-class check
SYSTEM outcome alone does not name a privilege-escalation technique.

---

### Slide 8 – Knowledge Check
Technique vs pattern? Trade-off? A12 line?

---

### Slide 9 – Summary
Named technique + procedure pattern + scope + telemetry.


**References:** [T1547.001 Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)
