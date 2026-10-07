# Common Initial Access Paths

**Path:** `modules/00-intro/09-initial-access`  
**Primary role:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared foundations)  
**Time:** about 25–35 minutes

## Purpose

Give every role a common model for how adversaries may first enter an environment and, more importantly, how to reason about an entry-path hypothesis without claiming more than the evidence supports.

## Mapped proficiency items

| Matrix ID | Type | Item | Outline heading |
|---|---|---|---|
| 0.9 | K | Common initial access paths | 0.9 a–h |
| 0.9.1 | T | Identify the most defensible initial-access path from supplied evidence, preserve uncertainty, and name the next evidence needed | 0.9.1 task 1 |

## Concepts taught

- initial access
- phishing / malspam
- exploit public-facing application / exposed service
- drive-by compromise / watering hole
- malvertising and search/SEO poisoning as routes to malicious web content
- valid accounts / external remote services
- trusted relationship / supply-chain compromise
- initial-access evidence progression: exposure or delivery → attempt → successful access → later execution
- choosing the next evidence source for an entry-path hypothesis
- unresolved initial access as a valid analytical conclusion

## Artifacts

- [Student guide](student-guide.md)
- [Instructor guide and answer key](instructor-guide.md)
- [Slides and speaker notes](slides.md)

## Course connections

Previous: [0.8 – Environment / signal flow](../08-environment/01-orientation/student-guide.md)

Next: [0.10 – Shared Foundations Section Summary](../10-summary/student-guide.md)

## References and Further Reading

- [MITRE ATT&CK — Initial Access (TA0001)](https://attack.mitre.org/tactics/TA0001/)
- [CISA — #StopRansomware Guide](https://www.cisa.gov/resources-tools/resources/stopransomware-guide) — Includes common initial-access vectors and advanced social-engineering examples such as SEO/search poisoning.
- [MITRE ATT&CK — Phishing (T1566)](https://attack.mitre.org/techniques/T1566/)
- [MITRE ATT&CK — Drive-by Compromise (T1189)](https://attack.mitre.org/techniques/T1189/)
- [MITRE ATT&CK — Exploit Public-Facing Application (T1190)](https://attack.mitre.org/techniques/T1190/)
- [MITRE ATT&CK — Valid Accounts (T1078)](https://attack.mitre.org/techniques/T1078/)
- [MITRE ATT&CK — External Remote Services (T1133)](https://attack.mitre.org/techniques/T1133/)
- [MITRE ATT&CK — Trusted Relationship (T1199)](https://attack.mitre.org/techniques/T1199/)
- [MITRE ATT&CK — Supply Chain Compromise (T1195)](https://attack.mitre.org/techniques/T1195/)
