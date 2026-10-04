# Module 2.7.1 – Core STIX Objects  
## Slide Deck Content

**Total Suggested Slides:** 9

### Slide 1 – Title
**Core STIX Objects**  
A structured vocabulary for CTI

### Slide 2 – STIX 2.1
STIX expresses cyber threat and observable information.

This course teaches a **selected subset**, not every STIX type.

Reference: [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### Slide 3 – Course object set
Indicator  
Observed Data  
Malware  
Attack Pattern  
Threat Actor  
Intrusion Set  
Campaign  
Course of Action  
Identity  
Relationship  
Sighting

### Slide 4 – STIX has more
Examples outside this lesson:
- Infrastructure
- Tool
- Vulnerability
- Report
- Note
- Incident
- Location
- Grouping

### Slide 5 – Observable vs Indicator
**File/IP/domain SCO** → the raw technical object

**Observed Data** → records that it was seen

**Indicator** → pattern used to detect matching activity

### Slide 6 – Sighting
A Sighting says an SDO was seen.

It can reference:
- what was sighted;
- Observed Data;
- who/where saw it.

### Slide 7 – Identity is neutral
DYA → organization Identity  
WS-JLEE → system Identity, if modeled that way

Not automatically Threat Actor.

### Slide 8 – Tracking name caution
Provider label ≠ automatic Threat Actor.

Evidence may support:
- Threat Actor
- Intrusion Set
- or neither yet

### Slide 9 – Knowledge Check
1. Only eleven STIX types?  
2. File vs Observed Data vs Indicator?  
3. Why not auto-type vendor label as Threat Actor?

**Next:** [2.7.2 – How STIX Objects Are Used in Intelligence Production](../02-stix-production/student-guide.md).
