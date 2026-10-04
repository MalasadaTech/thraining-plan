# Module 4.7 – Sensor and Data Availability
## Slide Deck Content

**Total Suggested Slides:** 9

### Slide 1 – Title
**Why Didn't the Detection Fire?**

### Slide 2 – No alert has multiple explanations
Behavior absent  
Logic missed  
Data missing  
Coverage missing  
Parsing changed  
Data late

### Slide 3 – Trace the path
Source  
→ ingestion  
→ parsing  
→ coverage  
→ timing  
→ logic

### Slide 4 – “Healthy” is not always usable
Required fields missing?  
Wrong population?  
Late data?  
Schema changed?

### Slide 5 – Current ATT&CK
ATT&CK v18 deprecated old **Data Sources** objects.

Current model: **Detection Strategies + Analytics + Log Sources**

Reference: [ATT&CK Analytics](https://attack.mitre.org/analytics/)

### Slide 6 – Sigma makes the dependency explicit
Rule effectiveness depends on the correct logs/fields.

Reference: [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html)

### Slide 7 – A12 replay
Event absent → data/visibility issue

Event present + correct fields + no match → logic issue

### Slide 8 – Evidence boundary
Missing telemetry means:

**cannot determine**

Not:

**did not happen**

### Slide 9 – Knowledge Check
1. Three data-path failures?  
2. Sensor healthy vs usable data?  
3. ATT&CK deprecation = telemetry irrelevant?

**Next:** 4.8 – Local DE Knowledge
