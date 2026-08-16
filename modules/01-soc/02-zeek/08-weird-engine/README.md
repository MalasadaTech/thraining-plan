# Weird Engine

**Path:** `modules/01-soc/02-zeek/08-weird-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** 60–75 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.2.8.1 | K | Weird engine | 1.2.14 |
| 1.2.8.2 | T | Analyze a Zeek weird log and accurately describe what occurred | 1.2.15 |
| 1.2.8.3 | T | Create a SIEM query to detect specific weird activity | 1.2.15 |

The teaching-unit ID is **1.2.8** (matrix). Outline headings `1.2.14` / `1.2.15` are the K/T pair. This is the `weird` log (`name`, optional `notice` flag), not a `notice` log course and not Zeek script authoring. This lesson closes unit **1.2**.

## Concepts taught

- `weird` log
- weird activity type (`name`)
- weird `notice` flag
- source and destination (weird)
- pivoting with `uid` to `conn` (weird)

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — lesson-specific images (empty)

Reusable Zeek logs belong in `labs/zeek/`, not here.
