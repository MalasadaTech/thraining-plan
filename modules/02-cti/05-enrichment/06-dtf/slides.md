# Module 2.5.6 – Defender's ThreatMesh Framework (DTF)  
## Slide Deck Content

**Total Suggested Slides:** 9

### Slide 1 – Title
**Title:** Defender's ThreatMesh Framework  
**Subtitle:** Record how you discovered candidate infrastructure

### Slide 2 – Purpose
DTF organizes **infrastructure discovery pivots**.

It is inspired by ATT&CK's matrix structure, but it describes discovery—not behavior.

Reference: [DTF repository](https://github.com/MalasadaTech/defenders-threatmesh-framework)

### Slide 3 – Four Pivot Tactics
**PTA0001** Domain  
**PTA0002** IP  
**PTA0003** SSL  
**PTA0004** Application

Reference: [DTF Matrix](https://github.com/MalasadaTech/defenders-threatmesh-framework/blob/main/matrix.md)

### Slide 4 – Name Server pivot
Same NS with seed:

**PTA0001 / P0101.010 – Registration: Name Server**

Candidate relationship. Strength depends on how distinctive the NS is.

### Slide 5 – Same-IP pivot
Same A address:

**PTA0001 / P0103.003 – DNS: IP Address**

Candidate relationship.

Shared hosting may weaken it.

### Slide 6 – Proximity needs context
**P0202 – Proximity** is valid.

Dedicated range → may be useful.  
Busy shared-cloud `/24` → weak by itself.

### Slide 7 – Name the next lookup
P0101.010 → other domains using NS  
P0103.003 → passive DNS on IP  
P0103.004 → other zones using RNAME  
P0202 → nearby IPs when context justifies it

### Slide 8 – Frameworks answer different questions
ATT&CK → behavior  
Diamond → event relationships  
Kill Chain → progression  
DTF → infrastructure discovery

### Slide 9 – Knowledge Check
1. Same NS: PTA/P-ID and strength test?  
2. Same IP: pivot and next lookup?  
3. Why can shared-cloud `/24` be rejected while P0202 remains valid?

**Next:** [2.5.7 – Correlation, Link Analysis, and Campaign Tracking](../07-correlation/student-guide.md).
