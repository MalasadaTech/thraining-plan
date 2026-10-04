# Module 0.3 – Jobs in one sentence

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.3 A / B / B  
- Hunter: 0.3 A / B / B  
- CTI: 0.3 A / B / B  
- DE: 0.3 A / B / B  
**Estimated Time:** 15–20 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Summarize each role’s responsibility in one sentence.
2. Identify IR and firewall / IA as supporting functions introduced for handoffs.

**Mapped Proficiency Items:**
- K: 0.3 – Jobs in one sentence

## Why This Matters

Security work often begins with an alert or a question, then involves people with different responsibilities. Knowing the purpose of each role helps you recognize who can carry the work forward and what result to expect. This lesson gives you a short description of each role used in the course.

## 1. The roles and their responsibilities

| Role | Core responsibility in this course |
|---|---|
| **SOC analyst** | Investigates an alert, records the finding, and starts the appropriate handoffs. |
| **Incident response (IR)** | Coordinates containment and recovery when incident handling is required. |
| **CTI analyst** | Answers intelligence questions, adds context, and examines related adversary activity or infrastructure. |
| **Threat hunter** | Searches for relevant activity that existing alerts may have missed, using an intelligence package or a hypothesis. |
| **Detection engineer (DE)** | Develops, tests, and maintains detections using identified needs and findings. |
| **Firewall / Information Assurance (IA) function** | Evaluates and implements blocking changes through the organization's authorized process. |

These descriptions identify the main contribution of each role. An organization may assign those responsibilities to teams with different names or combine several responsibilities in one position.

## 2. Recognizing the work being requested

A **Request for Information (RFI)** asks for information or analysis needed to answer a question. In this course's workflow, it is directed to CTI. A question arising from an alert is one reason for an RFI; other intelligence needs can also produce requests.

Consider a question about the role of a suspicious domain. CTI may develop an answer about that role. If the organization decides to restrict access to the domain, the function responsible for blocking evaluates and carries out that change. If the finding reveals activity worth detecting in the future, DE considers the detection need. The shared domain connects the work, while the requested outcome identifies the responsibility.

## 3. What the course develops

The four role tracks develop SOC analysis, CTI, hunting, and detection engineering. Incident response and firewall / IA responsibilities are included so learners understand the handoffs, while detailed training for those functions sits outside this course.

For now, aim to explain each role clearly in one sentence. That short description should convey the responsibility and intended result. The following lessons show how those results connect and how responsibilities can overlap.

## Knowledge Check

1. Describe each of the six roles in one sentence.
2. Which two supporting functions are introduced for handoffs rather than developed as full tracks, and what does each contribute?
3. How does a detection engineer’s responsibility differ from a request to block a domain?

## Summary

Identify a responsibility by the work requested and the result it should produce. The six roles introduced here support connected parts of security operations; the course develops four of them in depth and explains the other two as handoff destinations.

## Course Connections

Previous: [0.2 – What a SOC is](../02-what-a-soc-is/student-guide.md)

Next: [0.4 – How work can move](../04-how-work-moves/student-guide.md)

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.
