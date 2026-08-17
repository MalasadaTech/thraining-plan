# Files Engine

**Path:** `modules/01-soc/02-zeek/07-files-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.2.7.1 | K | Files engine | 1.2.12 a–e | A / B / C | B / C / C | A / A / B |
| 1.2.7.2 | T | Analyze a Zeek files log and accurately describe what occurred | 1.2.13 task 1 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.7.3 | T | Create a SIEM query to detect specific file transfer activity | 1.2.13 task 2 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |

The teaching-unit ID is **1.2.7**. Outline headings `1.2.12` / `1.2.13` are the K/T pair. SMTP is **1.2.6**. Weird is **1.2.8**. Host file activity is **1.1.3**. No lab.

## Concepts taught

- `files` log
- filename (files log)
- MIME type
- files-log hashes (MD5, SHA1, SHA256)
- `tx_hosts` / `rx_hosts`
- `conn_uids` (link to other Zeek logs)

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty
