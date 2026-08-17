# DNS Engine

**Path:** `modules/01-soc/02-zeek/03-dns-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.2.3.1 | K | DNS engine | 1.2.4 a–d | A / B / C | B / C / C | A / B / B |
| 1.2.3.2 | T | Analyze a Zeek DNS log and accurately describe what occurred | 1.2.5 task 1 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 2b / 3c |
| 1.2.3.3 | T | Create a SIEM query to detect specific DNS activity | 1.2.5 task 2 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 2b / 3c |

This folder is **not** outline item `1.2.3` (that heading is Conn engine tasks). Matrix IDs `1.2.3.*` are the canonical references. Conn is **1.2.2**. TLS is **1.2.4**. Host-observed DNS is **1.1.4**. No lab.

## Concepts taught

- `dns` log
- DNS query (question)
- DNS response (answer)
- common DNS record types
- source and destination fields in DNS logs

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty
