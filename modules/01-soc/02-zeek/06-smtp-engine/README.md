# SMTP Engine

**Path:** `modules/01-soc/02-zeek/06-smtp-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** 60–75 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.2.6.1 | K | SMTP engine | 1.2.10 |
| 1.2.6.2 | T | Analyze a Zeek SMTP log and accurately describe what occurred | 1.2.11 |
| 1.2.6.3 | T | Create a SIEM query to detect specific SMTP activity | 1.2.11 |

The teaching-unit ID is **1.2.6** (matrix). Outline headings `1.2.10` / `1.2.11` are the K/T pair. Attachment extract / hashes are **1.2.7**. This lesson does not teach how to write Zeek scripts.

## Concepts taught

- `smtp` log
- mail from
- rcpt to
- SMTP subject
- message ID
- pivoting with `uid` to `conn` (SMTP)

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — lesson-specific images (empty)

Reusable Zeek logs belong in `labs/zeek/`, not here.
