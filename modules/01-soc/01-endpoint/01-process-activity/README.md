# Process Activity

**Path:** `modules/01-soc/01-endpoint/01-process-activity`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** 60–75 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.1.1.1 | K | Process activity concepts | 1.1.1 a–g |
| 1.1.1.2 | T | Analyze a process event (Sysmon or MDE) and accurately describe what occurred | 1.1.1.1 task 1 |
| 1.1.1.3 | T | Create a SIEM query to detect specific process activity | 1.1.1.1 task 2 |

The teaching-unit ID is **1.1.1**. File activity is **1.1.2**. Host-observed network is **1.1.3**. Registry is **1.1.4**. Image/driver load is **1.1.5**. Zeek is **1.2**. This lesson does not teach Sysmon install or config.

## Concepts taught

- process activity
- process create / terminate
- PID, name, and command line
- parent-child process
- integrity / user context
- hashes and original filename
- process access (Sysmon Event ID 10)
- Sysmon 1 / 5 / 10 and DeviceProcessEvents

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — lesson-specific images (empty)
