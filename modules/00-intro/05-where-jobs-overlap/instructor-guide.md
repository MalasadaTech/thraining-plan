# Instructor Guide – Module 0.5 – Where the jobs lightly overlap

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.5 A / B / B  
- Hunter: 0.5 A / B / B  
- CTI: 0.5 A / B / B  
- DE: 0.5 A / B / B  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Several analysts may examine the same host, log, or domain while working toward different outcomes. Understanding those outcomes helps you collaborate without losing track of who is responsible for the remaining work. In this lesson, a **product** means the result a role is expected to deliver.

Teach this as a shared introductory lesson using the supplied examples and discussion. Match the depth to the proficiency levels above. The focus is the mapped knowledge and task; operational procedures are developed in the later role tracks.

## Learning Objectives

1. Explain how shared evidence can support different role-specific products.
2. Distinguish a handoff request from the work needed to complete it.
3. Explain why responsibilities remain distinct when one person performs several roles.

**Mapped Proficiency Items:**
- K: 0.5 – Where the jobs lightly overlap

## Preparation

Read the [student guide](student-guide.md) and use [slides.md](slides.md) to support the explanation. Review the answer key before teaching so the discussion and feedback reinforce the same concepts. This lesson uses discussion and worked examples; no lab is required.

## Suggested Timing

| Section | Time | Teaching purpose |
|---|---|---|
| Opening and purpose | 2 min | Connect this lesson to the previous topic. |
| Explanation and worked examples | 10 min | Use the three teaching sections below. |
| Knowledge check and feedback | 4 min | Ask for reasoning as well as an answer. |
| Summary and transition | 2 min | Consolidate the lesson and introduce the next topic. |
| **Total** | **18 min** | |

## Detailed Teaching Notes

### 1. Shared evidence and different products

Walk through the domain example without adding a second incident plot. Reuse is useful: the purpose is to avoid unnecessary reinvestigation while making each remaining responsibility clear. A product can be a finding or decision as well as a file.

**Student-facing emphasis:** The same evidence can support several products. Identify the outcome: alert finding, intelligence answer, hunt findings, or detection coverage.

### 2. What a request contributes

Use the RFI and hunt-package examples to separate preparation from completion. Learners should be able to name what the request enables and what the recipient must still contribute. Keep local forms out of the example unless supplied by the organization.

**Student-facing emphasis:** A handoff should explain what is known and what work remains. The receiving role develops the answer, findings, or change requested.

### 3. When one person fills several roles

Explain that the distinction does not require duplicate paperwork. A shared record can contain several products if each result and its purpose are understandable. The lesson concerns responsibility and completion, not staffing levels or mandatory document counts.

**Student-facing emphasis:** One person may perform several roles. Keep the purpose and completion of each product clear so others can follow the work.

## Knowledge Check — Answer Key

### 1. SOC and CTI examine the same domain. How could their products differ?

**Expected answer:** SOC may document what the host contacted and the alert disposition. CTI may assess the domain’s role to answer an intelligence question.

**Feedback and assessment:** Look for a difference in intended result while allowing the evidence to be shared.

### 2. What remains to be done when CTI receives an RFI?

**Expected answer:** CTI must evaluate the question and evidence, conduct the needed analysis, and develop an answer.

**Feedback and assessment:** A request starts or scopes work; the learner should identify the analytical contribution that remains.

### 3. Why distinguish roles when one person performs both alert investigation and hunting?

**Expected answer:** The responsibilities have different purposes and completion criteria. Clear findings show what the alert investigation established and what the broader search established.

**Feedback and assessment:** Accept an explanation of accountability and clarity without requiring separate teams or duplicate records.

## Closing and Transition

Collaboration works best when shared evidence is paired with clear responsibilities. A request prepares the next task, and each role develops a result suited to its purpose. Those distinctions remain useful when a single person performs several roles.

Previous: [0.4 – How work can move](../04-how-work-moves/student-guide.md)

Next: [0.6.1 – MITRE ATT&CK](../06-frameworks/01-attck/student-guide.md)

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.
