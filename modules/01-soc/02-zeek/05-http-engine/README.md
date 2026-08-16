# HTTP Engine

**Path:** `modules/01-soc/02-zeek/05-http-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** 60–75 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.2.5.1 | K | HTTP engine | 1.2.8 |
| 1.2.5.2 | T | Analyze a Zeek HTTP log and accurately describe what occurred | 1.2.9 |
| 1.2.5.3 | T | Create a SIEM query to detect specific HTTP activity | 1.2.9 |

The teaching-unit ID is **1.2.5** (matrix). Outline headings `1.2.8` / `1.2.9` are the K/T pair. File extract / `fuid` depth is **1.2.7**. This lesson does not teach HTTP body content or Zeek scripts.

## Concepts taught

- `http` log
- HTTP method
- HTTP `host`
- URI / URL
- User-Agent
- HTTP status code
- pivoting with `uid` to `conn` (HTTP)

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — lesson-specific images (empty)

Reusable Zeek logs belong in `labs/zeek/`, not here.
