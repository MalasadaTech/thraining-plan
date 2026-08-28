# Conn Engine

**Path:** `modules/01-soc/02-zeek/02-conn-engine`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.2.2.1 | K | Conn engine | 1.2.2 a–e | A / B / C | B / C / C | A / A / B |
| 1.2.2.2 | T | Analyze a Zeek conn log and accurately describe what occurred | 1.2.3 task 1 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.2.3 | T | Create a SIEM query to detect specific connection activity | 1.2.3 task 2 | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |

The teaching-unit ID is **1.2.2**. Outline knowledge is **1.2.2** a–e. Outline tasks are **1.2.3**. Matrix IDs are **1.2.2.1**–**1.2.2.3**. Zeek concepts are **1.2.1**. DNS is teaching-unit **1.2.3** (outline **1.2.4**). Host-observed network is **1.1.4**. No lab.

## Concepts taught

- `conn` log (also: `conn` event, connection log)
- `id.orig_h` / `id.orig_p` (originator / source)
- `id.resp_h` / `id.resp_p` (responder / destination)
- `conn_state` / `history`

## Artifacts

- [instructor-guide.md](instructor-guide.md)
- [student-guide.md](student-guide.md)
- [slides.md](slides.md)
- `assets/` — empty
