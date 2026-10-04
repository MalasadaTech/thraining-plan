# Common False Positive Causes

**Path:** `modules/01-soc/04-alerts/03-false-positive-causes`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 20–25 minutes

## Purpose

Once an alert is assessed as a false positive, the explanation can help reduce repeated unnecessary work. A useful recommendation connects the benign activity to the logic that matched and proposes a specific change with an understood effect on coverage.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.4.3.1 | K | Common false positive causes | 1.4.3 a–b | A / B / C | B / C / C | A / A / B |
| 1.4.3.2 | T | Given a false positive, identify the cause class and what you would change | 1.4.3.1 task 1 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |

## Concepts taught

- false positive cause: analyst or tool activity
- false positive cause: untuned or overly broad logic
- identifying the cause class and what you would change

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.4.2 – Alert Classification](../02-classification/student-guide.md)

Next: [1.4.4 – Common Alert Categorizations](../04-categorizations/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)
