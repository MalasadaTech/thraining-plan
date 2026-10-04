# Instructor Guide – Module 4.7 – Sensor and Data Availability for Detection

**Estimated Time:** 20–25 minutes

## Purpose

Teach the learner to trace detection dependencies through the data path without turning the module into vendor administration.

## Troubleshooting Path

Source/sensor  
→ transport/ingestion  
→ parsing/normalization  
→ population coverage  
→ timeliness  
→ detection logic

## Current ATT&CK Note

ATT&CK v18 (October 2025) deprecated the old Data Sources objects. Current ATT&CK uses Detection Strategies and Analytics with log-source information.

References:
- [ATT&CK Analytics](https://attack.mitre.org/analytics/)
- [ATT&CK Data Sources deprecation](https://attack.mitre.org/datasources/)

Keep using “data source” in the ordinary engineering sense when describing telemetry, but explain that it is no longer the current ATT&CK object model.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| “Sensor dashboard says green, so data is fine.” | Check field completeness, parsing, coverage, and timeliness. |
| “No alert means nothing happened.” | Missing evidence limits the conclusion. |
| Jumps straight to rule logic. | Trace the data path first. |
| Tries to become vendor admin. | DE must understand dependencies; administration may belong elsewhere. |

## Knowledge Check – Answer Key

1. Examples: collection, transport, parsing, population coverage, timeliness.
2. Sensor health may not guarantee the right fields/population/timing required by the analytic.
3. No. The object model changed; telemetry dependencies remain fundamental.
