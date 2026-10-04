# Module 2.3.1 – MITRE ATT&CK for CTI Analysis and Reporting  
## Slide Deck Content

**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

### Slide 1 – Title
**Title:** MITRE ATT&CK for CTI  
**Subtitle:** Evidence first, ID second

### Slide 2 – What a CTI mapping does
A good ATT&CK mapping tells another analyst:

- **why** the behavior fits a tactic;
- **how** it maps to a technique or sub-technique; and
- **what evidence** supports that choice.

Reference: [MITRE ATT&CK](https://attack.mitre.org/)

### Slide 3 – Four pieces
**Tactic** — why  
**Technique** — general method  
**Sub-technique** — specific implementation  
**Evidence / procedure** — what this case actually shows

### Slide 4 – PowerShell example
`wscript.exe` → `powershell.exe -enc`

**Execution / T1059.001 – PowerShell**

Evidence: PowerShell process + encoded command line.

Reference: [T1059.001](https://attack.mitre.org/techniques/T1059/001/)

### Slide 5 – File-transfer example
A confirmed download of `/update.exe` from an external system can support:

**Command and Control / T1105 – Ingress Tool Transfer**

A request name alone is weaker than evidence showing the file actually transferred.

Reference: [T1105](https://attack.mitre.org/techniques/T1105/)

### Slide 6 – Choose the most specific supported mapping
Specific evidence → specific sub-technique.  
General evidence → broader technique.

More detail is useful only when the evidence earns it.

### Slide 7 – Knowledge Check
1. PowerShell `-enc`: tactic, ID, evidence?  
2. What strengthens a T1105 mapping?  
3. Why not always choose the most detailed ID available?

### Slide 8 – Summary
**Evidence → behavior → ATT&CK mapping**

Keep the evidence beside the ID.

**Next:** [2.3.2 – Diamond Model Application in CTI](../02-diamond-cti/student-guide.md).
