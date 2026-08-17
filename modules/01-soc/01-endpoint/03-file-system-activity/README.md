# File System Activity

**Path:** `modules/01-soc/01-endpoint/03-file-system-activity`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.1.3.1 | K | File system activity concepts | 1.1.3 a–e | A / B / C | A / B / B | A / A / A |
| 1.1.3.2 | T | Analyze a file event (Sysmon or MDE) and accurately describe what occurred | 1.1.3.1 task 1 | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.3.3 | T | Create a SIEM query to detect specific file operations | 1.1.3.1 task 2 | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |

The teaching-unit ID is **1.1.3**. Process activity is **1.1.2**. Host-observed network is **1.1.4**. Zeek is **1.2**. Not Sysmon install. No lab.

## Concepts taught

- file system activity
- file create / rename-move / delete / modify / read
- path, name, and extension
- file hashes
- initiating process (file events)
- Sysmon 11 / 23 / 26 and DeviceFileEvents

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty
