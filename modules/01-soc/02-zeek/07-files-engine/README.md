# Files Engine

**Path:** `modules/01-soc/02-zeek/07-files-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** 60–75 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.2.7.1 | K | Files engine | 1.2.12 |
| 1.2.7.2 | T | Analyze a Zeek files log and accurately describe what occurred | 1.2.13 |
| 1.2.7.3 | T | Create a SIEM query to detect specific file transfer activity | 1.2.13 |

The teaching-unit ID is **1.2.7** (matrix). Outline headings `1.2.12` / `1.2.13` are the K/T pair. This is **network-sensor** file transfer, not host file activity (**1.1.2**). Connection linking uses `conn_uids` (and `uid` on the related protocol log).

## Concepts taught

- `files` log
- filename (files log)
- MIME type (`mime_type`)
- files-log hashes (MD5, SHA1, SHA256)
- `tx_hosts` / `rx_hosts`
- `conn_uids` (link to other Zeek logs)

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — lesson-specific images (empty)

Reusable Zeek logs belong in `labs/zeek/`, not here.
