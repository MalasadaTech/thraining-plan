# Registry Activity

**Path:** `modules/01-soc/01-endpoint/05-registry-activity`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.1.5.1 | K | Registry activity concepts | 1.1.5 a–e | A / B / C | A / B / B | A / A / A |
| 1.1.5.2 | T | Analyze a registry event (Sysmon or MDE) and accurately describe what occurred | 1.1.5.1 task 1 | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.5.3 | T | Create a SIEM query to detect specific registry operations | 1.1.5.1 task 2 | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |

The teaching-unit ID is **1.1.5**. Host-network is **1.1.4**. Image/driver load is **1.1.6**. Persistence *how-to* is **2.6**. Not Sysmon install. No lab.

## Concepts taught

- registry activity
- hives and key → value
- registry set / delete / rename
- common persistence locations (Run, Services)
- initiating process (registry events)
- Sysmon 12 / 13 / 14 and DeviceRegistryEvents

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty
