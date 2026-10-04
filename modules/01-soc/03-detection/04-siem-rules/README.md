# SIEM Rules

**Path:** `modules/01-soc/03-detection/04-siem-rules`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 25–30 minutes

## Purpose

A saved detection combines search logic with operating settings that determine when and how an alert is created. Reading both parts explains what an alert represents and helps turn a query into a reviewable detection proposal.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.3.4.1 | K | SIEM rules | 1.3.7 a–c | A / B / C | B / C / C | A / B / B |
| 1.3.4.2 | T | Analyze an existing SIEM rule and describe what it detects | 1.3.8 task 1 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 2b / 3c |
| 1.3.4.3 | T | Create a basic SIEM detection rule from log fields or a SIGMA rule | 1.3.8 task 2 | 1a / 2b / 3c | 2b / 3c / 4c | 1a / 1a / 2b |

## Concepts taught

- SIEM detection rules / correlation searches
- turning log fields into detections
- matching techniques: regex and wildcards (SIEM)
- creating a SIEM rule from log fields or from SIGMA

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.3.3 – YARA Rules](../03-yara-rules/student-guide.md)

Next: [1.4.1 – Alert Context and Investigation](../../04-alerts/01-context-investigation/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
- [Microsoft — Custom detection rules](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules)
- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)
