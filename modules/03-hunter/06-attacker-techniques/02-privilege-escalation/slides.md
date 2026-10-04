# Module 3.6.2 – Privilege Escalation Techniques  
## Slide Deck Content

**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 10

---

### Slide 1 – Title
**Title:** 3.6.2 – Privilege Escalation Techniques  
**Subtitle:** Mentor-style, evidence-bound hunting tradecraft

---

### Slide 2 – Privilege escalation
Higher effective privilege than the context previously controlled.

---

### Slide 3 – Outcome ≠ method
SYSTEM child can show elevation; it does not identify how.

---

### Slide 4 – UAC bypass
Auto-elevation plus mechanism evidence + elevated result; process name alone is insufficient.

---

### Slide 5 – Access Token Manipulation
Token operations/impersonation evidence + security-context transition.

---

### Slide 6 – Windows Service
Service creation/modification + account/context can support SYSTEM elevation.

---

### Slide 7 – Exploitation
Exploit/vulnerable component evidence + resulting higher privilege.

---

### Slide 8 – A12 boundary
HKCU Run Updater = persistence; no privilege change shown.

---

### Slide 9 – Knowledge Check
What is proven by SYSTEM? Token evidence? fodhelper limitation?

---

### Slide 10 – Summary
Name the elevation outcome first; earn the method.


**References:** [T1548.002 Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002/) | [T1134 Access Token Manipulation](https://attack.mitre.org/techniques/T1134/) | [T1543.003 Windows Service](https://attack.mitre.org/techniques/T1543/003/) | [T1068 Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)
