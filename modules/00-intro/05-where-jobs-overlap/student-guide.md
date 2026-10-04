# Module 0.5 – Where the jobs lightly overlap

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.5 A / B / B  
- Hunter: 0.5 A / B / B  
- CTI: 0.5 A / B / B  
- DE: 0.5 A / B / B  
**Estimated Time:** 15–20 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain how shared evidence can support different role-specific products.
2. Distinguish a handoff request from the work needed to complete it.
3. Explain why responsibilities remain distinct when one person performs several roles.

**Mapped Proficiency Items:**
- K: 0.5 – Where the jobs lightly overlap

## Why This Matters

Several analysts may examine the same host, log, or domain while working toward different outcomes. Understanding those outcomes helps you collaborate without losing track of who is responsible for the remaining work. In this lesson, a **product** means the result a role is expected to deliver.

## 1. Shared evidence and different products

| Role | Product developed from the evidence |
|---|---|
| SOC analyst | A finding that supports closing or escalating an alert. |
| CTI analyst | An intelligence answer that explains the evidence's significance for a question. |
| Threat hunter | Search findings, their scope, and relevant gaps or limitations. |
| Detection engineer | A tested detection or a justified change to detection coverage. |

For example, a domain found in an alert may help SOC establish what the host contacted. CTI may examine the domain's role in the activity. A hunter may search for other hosts that contacted it, while DE considers whether the associated behavior warrants a detection. Each role can reuse the earlier evidence and reasoning while developing the product it owes.

## 2. What a request contributes

An RFI communicates a question and the context needed to begin answering it. The CTI analyst still has to evaluate the evidence and develop the answer. Similarly, an intelligence package can prepare a hunter to search, while the hunter still needs to execute the search and explain the results.

When passing work, be clear about what has already been established and what the recipient is being asked to do. This prevents a request from being mistaken for completed analysis and helps the receiving role build on work already done.

## 3. When one person fills several roles

In a smaller organization, the same person may investigate an alert and later perform intelligence or detection work. The responsibilities still matter because the purpose and completion criteria change as that person moves between tasks.

For example, documenting why an alert was escalated does not answer every intelligence question about the activity. The analyst can use the same evidence, but should make the additional question, reasoning, and result clear. Distinguishing the products helps others understand what is complete and what still needs attention.

## Knowledge Check

1. SOC and CTI examine the same domain. How could their products differ?
2. What remains to be done when CTI receives an RFI?
3. Why distinguish roles when one person performs both alert investigation and hunting?

## Summary

Collaboration works best when shared evidence is paired with clear responsibilities. A request prepares the next task, and each role develops a result suited to its purpose. Those distinctions remain useful when a single person performs several roles.

## Course Connections

Previous: [0.4 – How work can move](../04-how-work-moves/student-guide.md)

Next: [0.6.1 – MITRE ATT&CK](../06-frameworks/01-attck/student-guide.md)

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.
