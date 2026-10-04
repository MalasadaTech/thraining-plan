# Module 2.3.3 – Cyber Kill Chain in Intelligence Analysis  
## Slide Deck Content

**Total Suggested Slides:** 8

### Slide 1 – Title
**Title:** Cyber Kill Chain for CTI  
**Subtitle:** Describe progression without inventing stages

### Slide 2 – Seven stages
Reconnaissance  
Weaponization  
Delivery  
Exploitation  
Installation  
Command and Control  
Actions on Objectives

Reference: [Lockheed Martin](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)

### Slide 3 – The product is not a seven-box checklist
Only list stages you can support with evidence.

Unobserved stages are intelligence gaps.

### Slide 4 – Delivery vs Installation
Successful download of `/update.exe` → **Delivery** can be supported.

Installation requires evidence that the payload was installed or established.

### Slide 5 – Execution needs context
`wscript.exe` → `powershell.exe -enc`

Execution is visible.

Kill Chain stage depends on the role:
- trigger malicious code → Exploitation
- establish implant/persistence → Installation

### Slide 6 – Command and Control
Outbound traffic is not automatically C2.

Look for evidence of an adversary control/communication channel.

### Slide 7 – Knowledge Check
1. Why not list all seven?  
2. Download without execution/persistence: stage?  
3. Why does PowerShell alone not prove Installation?

### Slide 8 – Summary
Stage the role the evidence supports.

**Next:** [2.4.1 – Internal Threat Intelligence Platform](../../04-platforms/01-internal-tip/student-guide.md).
