# Alert Context and Investigation

**Path:** `modules/01-soc/04-alerts/01-context-investigation`  
**Primary role:** SOC Analyst  
**Secondary:** Threat Hunter, CTI Analyst  
**Time:** about 30 minutes

## Purpose

An alert is the starting point for an investigation. Before deciding what it means, establish what evidence it contains, what logic produced it, and what related records can add. This makes the eventual finding traceable to observations rather than to the alert title alone.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|-----------|------|------|-----------------|-----------|--------------|-----------|
| 1.4.1.1 | K | Alert context and investigation | 1.4.1 a–e | A / B / C | B / C / C | A / A / B |
| 1.4.1.2 | T | Review an alert and identify which context is present and which is missing (include VirusTotal on a hash, IP, or domain you have) | 1.4.1.1 task 1 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.1.3 | T | Review the alert configuration and explain what would fire | 1.4.1.1 task 2 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.1.4 | T | Trace an alert to its upstream detection logic and name each hop | 1.4.1.1 task 3 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.1.5 | T | Collect related endpoint logs and state what they add (or fail to add) | 1.4.1.1 task 4 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 1a |
| 1.4.1.6 | T | Collect related PCAP and state what it adds versus the alert fields | 1.4.1.1 task 5 | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 1a |

## Concepts taught

- alert context (present vs missing)
- VirusTotal lookup (hash, IP, or domain) as alert context
- alert configuration (what would fire)
- upstream alerting hops
- related endpoint logs for an alert
- related PCAP versus alert fields

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [1.3.4 – SIEM Rules](../../03-detection/04-siem-rules/student-guide.md)

Next: [1.4.2 – Alert Classification](../02-classification/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching)
- [Zeek — http.log](https://docs.zeek.org/en/current/reference/logs/http.html)
