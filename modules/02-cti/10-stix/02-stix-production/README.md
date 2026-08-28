# How STIX Objects Are Used in Intelligence Production

**Path:** `modules/02-cti/10-stix/02-stix-production`  
**Primary role:** CTI Analyst  
**Secondary:** Threat Hunter, SOC Analyst  
**Time:** about 20–25 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 2.10.2 | K | How STIX objects are used in intelligence production | 2.10.2 a–b | A / B / B | B / C / C | B / C / C |
| 2.10.2.1 | T | Create STIX-aligned relationships and explain a threat scenario | 2.10.2.1 tasks 1–2 | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4d |
| 2.10.2.2 | T | Create and validate STIX objects | 2.10.2.2 task 1 | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4d |
| 2.10.2.3 | T | Use TAXII for sharing and consumption of intelligence | 2.10.2.3 task 1 | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4c |

The teaching-unit ID is **2.10.2**. Spec is **STIX 2.1**. Classroom collection only. No TAXII server. Do not write lumped **2.10.3**. Hunt STIX input is **3.4.3**. Finished narrative is **2.11**. No lab.

## Concepts taught

- structuring STIX for sharing and automation (also: STIX bundle, payload vs channel)
- linking STIX objects to represent threat activity (also: STIX `relationship_type`, explain a STIX scenario)
- validating a STIX object (also: valid STIX pattern, missing `relationship_type`, unearned Threat Actor)
- TAXII sharing and consumption (also: TAXII collection, consume STIX, `harbor-cti` classroom collection)

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty
