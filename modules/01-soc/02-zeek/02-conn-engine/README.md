# Conn Engine

**Path:** `modules/01-soc/02-zeek/02-conn-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter  
**Time:** 60–75 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|-----------|------|------|-----------------|
| 1.2.2.1 | K | Conn engine | 1.2.2 |
| 1.2.2.2 | T | Analyze a Zeek conn log and accurately describe what occurred | 1.2.3 |
| 1.2.2.3 | T | Create a SIEM query to detect specific connection activity | 1.2.3 |

## Concepts taught

- `conn` log
- `uid` (Zeek connection identifier)
- 5-tuple (`id.orig_h`, `id.orig_p`, `id.resp_h`, `id.resp_p`, `proto`)
- `service`
- `duration`
- `orig_bytes` / `resp_bytes`
- `conn_state` (`SF`, `S0`, `S1`, `REJ`, `RSTO`, `RSTR`, `OTH`, and related states)
- `history`
- beaconing (long duration, steady bytes)
- scanning (`S0` / `REJ` volume)
- pivoting with `uid`

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — lesson-specific images (empty)

Reusable Zeek logs belong in `labs/zeek/`, not here.
