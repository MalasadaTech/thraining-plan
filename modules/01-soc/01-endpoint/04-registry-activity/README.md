# Registry Activity

**Path:** `modules/01-soc/01-endpoint/04-registry-activity`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** 60–75 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.1.4.1 | K | Registry activity concepts | 1.1.4 a–e |
| 1.1.4.2 | T | Analyze a registry event (Sysmon or MDE) and accurately describe what occurred | 1.1.4.1 task 1 |
| 1.1.4.3 | T | Create a SIEM query to detect specific registry operations | 1.1.4.1 task 2 |

The teaching-unit ID is **1.1.4**. Process activity is **1.1.1**. File system activity is **1.1.2**. Host-observed network is **1.1.3**. Image/driver load is **1.1.5**. Persistence *how-to* is **2.6**. This lesson does not teach Sysmon install or config.

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
- `assets/` — lesson-specific images (empty)
