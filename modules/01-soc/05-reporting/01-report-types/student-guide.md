# Module 1.5.1 – Report Types

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.1.1 A / B / C ; 1.5.1.2 2b / 3c / 4c  
- Hunter: 1.5.1.1 B / C / C ; 1.5.1.2 2b / 3c / 4c  
- CTI: 1.5.1.1 B / C / C ; 1.5.1.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Describe incident reports, RFIs, and local report types.
2. Select the type suited to a supplied reporting purpose.
3. Explain why a plausible alternative serves a different purpose.

**Mapped Proficiency Items:**
- K: 1.5.1.1 – Report types
- T: 1.5.1.2 – Identify the correct report type for a given situation and why it is not the adjacent type

## Why This Matters

Report selection begins with the purpose of the communication. An incident report records a case and supports response, while an RFI asks a question needed by the work. The same incident can require both products.

## 1. Choosing the product by purpose

| Type | Primary purpose | Useful comparison |
|---|---|---|
| Incident report | Records an incident or supported suspected incident for handling under local criteria. | An RFI asks for information rather than replacing the incident record. |
| Request for Information (RFI) | States a question and needed information or analysis, with relevant context. | It can link to an existing case without creating a duplicate incident. |
| Other (local) | Meets a reporting purpose defined by the organization. | Use the actual type and instructions applicable to that purpose. |

An RFI may go to CTI or another responsible function. In this course, a question requiring intelligence analysis provides the connection into the CTI track. The type describes the requested product, while routing procedures determine the recipient and channel.

## 2. Working through the course case

For this example, assume the investigation of case `A12` on `WS-JLEE` has met the organization's criteria for a suspected incident and IR handoff. The supporting case record includes the Script Host/PowerShell activity and the evidence for that escalation decision. The command pattern alone is not the incident determination.

The product recording the case for response is an incident report. If the analyst also needs CTI to assess the role of a related domain or file, an RFI can state that question and link to A12. The RFI has a separate purpose even if the system stores it within the same case record.

## 3. Explaining the choice

State the selected type and explain the purpose that makes it appropriate. For example: “RFI: A12 already records the incident, and this product asks CTI to assess the domain's role. It should link to A12 so CTI can use the existing evidence.”

Conversely, when the task is to record and hand off the supported incident itself, select the incident report. The presence of unanswered questions does not prevent reporting a suspected incident under local criteria. This lesson focuses on choosing the product; the next lessons connect it to a deadline and an approved route.

## Knowledge Check

1. How do an incident report and an RFI differ?
2. A12 is already open and CTI is asked to assess a related domain. Which type fits, and why?
3. If a suspected incident meets reporting criteria but attribution is unknown, should the incident record wait for the RFI answer?

## Summary

Select the report type by the work it must accomplish. Record the supported incident and use linked RFIs for additional questions, following the organization’s definitions for other products.

## Course Connections

Previous: [1.4.5 – SLA / Response Time Goals](../../04-alerts/05-sla-response-times/student-guide.md)

Next: [1.5.2 – Reporting Timeline Requirements](../02-reporting-timelines/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center)
