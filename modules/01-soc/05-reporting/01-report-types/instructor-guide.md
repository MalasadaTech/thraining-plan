# Instructor Guide – Module 1.5.1 – Report Types

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.1.1 A / B / C ; 1.5.1.2 2b / 3c / 4c  
- Hunter: 1.5.1.1 B / C / C ; 1.5.1.2 2b / 3c / 4c  
- CTI: 1.5.1.1 B / C / C ; 1.5.1.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Report selection begins with the purpose of the communication. An incident report records a case and supports response, while an RFI asks a question needed by the work. The same incident can require both products.

## Learning Objectives

1. Describe incident reports, RFIs, and local report types.
2. Select the type suited to a supplied reporting purpose.
3. Explain why a plausible alternative serves a different purpose.

**Mapped Proficiency Items:**
- K: 1.5.1.1 – Report types
- T: 1.5.1.2 – Identify the correct report type for a given situation and why it is not the adjacent type

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required.

Use the proficiency levels above to adjust prompting and explanation depth. The module focuses on its mapped knowledge and tasks; the linked next lesson develops the next step.

## Suggested Timing

| Section | Minutes | Focus |
|---|---|---|
| Opening | 2 | Connect the lesson to its purpose. |
| Explanation and worked example | 12 | Read the supplied evidence and demonstrate the reasoning. |
| Knowledge check and feedback | 6 | Complete the interpretation or modification tasks. |
| Summary and transition | 2 | Consolidate the result and connect the next lesson. |
| **Total** | **22** | |

## Detailed Teaching Notes

### 1. Choosing the product by purpose

Focus on product purpose rather than team names. Explain that one system can contain linked products without duplicate paperwork.

**Key point to reinforce:** Choose the product by purpose: incident record, information question, or an actual local type.

### 2. Working through the course case

Make the supplied incident-handling determination explicit. Avoid treating encoded PowerShell alone as the criterion for an incident.

**Key point to reinforce:** A12 supplies the incident context. A linked CTI RFI asks the additional intelligence question.

### 3. Explaining the choice

Ask learners to give the type and its reason in connected prose. Their explanation should distinguish the case record from the unanswered question.

**Key point to reinforce:** Explain why the chosen product serves the request. Unanswered questions do not automatically delay incident reporting.

## Knowledge Check — Answer Key

### 1. How do an incident report and an RFI differ?

**Expected answer:** The incident report records the case and supports response; the RFI states a question or information need and can link to the case.

### 2. A12 is already open and CTI is asked to assess a related domain. Which type fits, and why?

**Expected answer:** RFI, because the product is the intelligence question; the existing incident record supplies linked context rather than requiring a duplicate case.

### 3. If a suspected incident meets reporting criteria but attribution is unknown, should the incident record wait for the RFI answer?

**Expected answer:** No. Record and route the suspected incident under local procedures, state the uncertainty, and use an RFI for the additional question as needed.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Select the report type by the work it must accomplish. Record the supported incident and use linked RFIs for additional questions, following the organization’s definitions for other products.

Previous: [1.4.5 – SLA / Response Time Goals](../../04-alerts/05-sla-response-times/student-guide.md)

Next: [1.5.2 – Reporting Timeline Requirements](../02-reporting-timelines/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center)
