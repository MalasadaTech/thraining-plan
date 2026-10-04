# Module 0.8 – Environment / signal flow

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.8 A / B / C ; 0.8.1 2b / 3c / 4c  
- Hunter: 0.8 B / C / C ; 0.8.1 2b / 3c / 4c  
- CTI: 0.8 A / B / B ; 0.8.1 1a / 2b / 3c  
- DE: 0.8 A / B / B ; 0.8.1 2b / 3c / 4c  
**Estimated Time:** 15–20 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Describe the seven environment areas used for orientation.
2. Identify which areas are relevant to a simple investigation question.
3. Distinguish the environment area relevant to a question from a related area, including traffic paths versus sensor coverage.

**Mapped Proficiency Items:**
- K: 0.8 – Environment / signal flow
- T: 0.8.1 – Identify which kind of fact applies and why it is not the adjacent kind

## Why This Matters

An event becomes easier to interpret when you understand where it occurred and how activity normally moves through the organization. Environment orientation connects a host or account to its role, its access paths, and the evidence available along those paths.

## 1. Building a useful environment picture

| Area | What to establish | Why it matters |
|---|---|---|
| Egress | How systems reach external networks, including proxies and other gateways. | Helps locate outbound activity and the controls it crosses. |
| Segments and data flow | Major network or workload boundaries and expected paths between them. | Helps distinguish expected communication from activity needing explanation. |
| Email | How messages enter, are processed, and reach users. | Helps locate delivery evidence and relevant email controls. |
| Edge firewalls and chokepoints | Where traffic is filtered or concentrated. | Identifies useful control and observation points. |
| Third-party access and federation | How external organizations or identities receive access and what that access permits. | Helps explain access paths and responsibility for relevant records. |
| Crown jewels | Systems, services, or information whose loss would have high impact. | Helps prioritize investigation according to organizational consequence. |
| PCAP and sensors | Where packet capture or other sensors exist and what they actually retain. | Establishes which activity may be observable and at what detail. |

These categories organize questions for the local environment. Use maintained diagrams, service documentation, and system owners to establish the actual design. The fictional course setting does not supply a complete production architecture.

## 2. Tracing an event through the environment

Suppose an alert reports that a workstation contacted an external domain. Begin by establishing the workstation's segment and the expected egress path. Then identify the relevant gateway or proxy and ask what records are available for the time in question. If packet capture is needed, confirm whether a sensor covered that path and retained the traffic.

This sequence separates three questions: where traffic could travel, where it could be observed, and what evidence is actually available. A diagram may show a gateway even when its logs were not enabled or retained. A sensor may cover one segment without seeing another.

## 3. Recording useful gaps and next questions

If the expected evidence is missing, record the visibility gap and identify the owner or documentation needed to resolve it. An absence of logs does not establish that the activity did not occur. It may reflect routing, collection, access, or retention limits.

Also connect the affected system to its purpose and importance. A third-party account accessing a critical service raises questions about the authorized access method, scope, and responsible owner. Understanding those relationships helps you ask a focused question and choose an appropriate next step.

## Knowledge Check

1. Which environment areas would help you investigate a workstation contacting an external domain?
2. You know the expected egress path but need to determine whether packet-level evidence exists. Which environment area should you check, and how does it differ from egress?
3. How do third-party access and crown jewels help orient an investigation?

## Summary

Environment orientation helps you connect an event to expected paths, organizational importance, and available evidence. Use the seven areas to ask focused questions, verify the actual environment, and make visibility gaps clear.

## Course Connections

Previous: [0.7 – External tools](../../07-tool-survey/01-external-tools/student-guide.md)

Next: the SOC analyst track, beginning with observations and detections.

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.
