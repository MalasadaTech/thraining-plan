# Module 3.6.1 – Persistence Techniques  
## Slide Deck Content

**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 10

---

### Slide 1 – Title
**Title:** 3.6.1 – Persistence Techniques  
**Subtitle:** Mentor-style, evidence-bound hunting tradecraft

---

### Slide 2 – Persistence
Maintain access or recurring execution across interruptions.

---

### Slide 3 – Run keys / Startup
Path + value + target + creator/user + file context.

---

### Slide 4 – Scheduled Tasks
Task + trigger + action + principal + creator. Role determines tactic.

---

### Slide 5 – Windows Services
Service + image path + start type + account + creator/modifier.

---

### Slide 6 – Other mechanisms
WMI subscriptions, logon scripts, Winlogon and other autostarts.

---

### Slide 7 – Technique ≠ malicious verdict
Legitimate software uses the same mechanisms; context separates expected from suspicious.

---

### Slide 8 – A12
HKCU Updater → %TEMP%\update.exe = user-context persistence.

---

### Slide 9 – Knowledge Check
Evidence fields? Multi-tactic task? Legit updater?

---

### Slide 10 – Summary
Recognize the mechanism, then evaluate the instance.


**References:** [T1547.001 Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/) | [T1053.005 Scheduled Task](https://attack.mitre.org/techniques/T1053/005/) | [T1543.003 Windows Service](https://attack.mitre.org/techniques/T1543/003/)
