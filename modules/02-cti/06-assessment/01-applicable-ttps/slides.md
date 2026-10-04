# Module 2.6.1 – Extracting Applicable TTPs  
## Slide Deck Content

**Total Suggested Slides:** 8

### Slide 1 – Title
**Title:** Applicable TTPs  
**Subtitle:** Can it happen here? Can we see it?

### Slide 2 – Extract the behavior
Keep the **how**:
- command
- procedure
- technique
- workflow

Do not confuse:
- hash
- IP
- domain
with a TTP.

### Slide 3 – Applicability
Ask:
- platform present?
- access/path possible?
- required preconditions present?

### Slide 4 – Visibility
Only after applicability:

**Visible**  
**Partially visible**  
**Visibility gap**

No telemetry ≠ not applicable.

### Slide 5 – PowerShell example
Encoded PowerShell / **T1059.001**

DYA has Windows → **applicable**

Telemetry status → assess separately

Reference: [MITRE T1059.001](https://attack.mitre.org/techniques/T1059/001/)

### Slide 6 – Platform mismatch
OT historian wipe  
DYA has no OT historian environment

→ **not applicable**

No need to turn it into a local crisis.

### Slide 7 – Knowledge Check
1. Applicability vs visibility?  
2. Windows + no PowerShell command-line telemetry: what result?  
3. ESXi-only behavior + no ESXi: what result?

### Slide 8 – Summary
**Behavior → applicability → visibility**

Keep telemetry gaps visible.

**Next:** [2.6.2 – Threat Relevance and Organizational Impact](../02-relevance-impact/student-guide.md).
