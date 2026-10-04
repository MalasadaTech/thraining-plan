# Module 1.5.3 – Notification and Distribution

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C ; 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 A / B / B ; 1.5.3.2 2b / 3c / 4c  
- CTI: 1.5.3.1 B / C / C ; 1.5.3.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret a notification chart’s recipients, awareness requirements, and channels.
2. Route a supplied report using the chart.
3. Explain why an alternative route does not meet the stated requirements.

**Mapped Proficiency Items:**
- K: 1.5.3.1 – Notification and distribution
- T: 1.5.3.2 – Route a report: name recipients, leadership awareness, and the approved channel

## Why This Matters

A report becomes useful when it reaches the responsible people through a channel that supports the work. A notification chart connects the product to recipients, leadership awareness, and the approved means of delivery.

## 1. Reading a notification chart

The chart below is a classroom example, not a universal routing policy.

| Product | Work recipients | Leadership awareness | Approved classroom channel |
|---|---|---|---|
| Incident report | SOC queue and IR. | Yes, through the duty SOC lead. | The case-system ticket. |
| RFI | The named responsible team, such as CTI, Hunt, or IT. | No routine separate notification unless requested or required. | Ticket or approved RFI form. |

“Leadership awareness” identifies the relevant leadership role and purpose; it does not automatically mean contacting the most senior executive. Real routing may depend on severity, incident type, sensitivity, and local agreements. Use the actual chart and escalation path when applying the lesson.

## 2. Routing the course examples

For the first IR handoff of supported case A12, route the incident record to the SOC queue and IR through the case-system ticket and provide awareness to the duty SOC lead. Include a clear link or reference to the evidence and work being handed off.

For an RFI asking CTI to assess the related domain, name CTI as the recipient and use the ticket or approved RFI form. Under this classroom chart, no separate leadership notification is routinely required. If leadership requested the answer or another policy applies, record that requirement.

Personal SMS, private chat, and personal email are outside the approved classroom routes. The issue is whether the chosen path provides the required access, record, and handling—not the mere fact that a tool is called chat or email.

## 3. Making the handoff traceable

A concise routing record names the recipients, leadership-awareness decision, approved channel, and reason a proposed alternative does not satisfy the chart. For example: “A12 incident report → SOC queue and IR; duty SOC lead informed; case-system ticket. A private message to one responder does not place the case in the required queue.”

Follow local requirements for acceptance, acknowledgement, or urgent supplementary notification. Keep the official record aligned with the action taken so another analyst can see who owns the next step. This completes the SOC reporting sequence; the CTI track develops how an intelligence question becomes an answer.

## Knowledge Check

1. What does a notification chart tell you?
2. Route the first A12 incident handoff using the classroom chart and reject an unsuitable alternative.
3. Route the CTI RFI and explain when the leadership decision could change.

## Summary

Use the notification chart to route the product, provide appropriate leadership awareness, and preserve a traceable handoff. The approved route connects the completed SOC work to the next responsible function.

## Course Connections

Previous: [1.5.2 – Reporting Timeline Requirements](../02-reporting-timelines/student-guide.md)

Next: [2.1.1 — Data, information, and intelligence](../../../02-cti/01-core-intel/01-data-info-intel/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center)
