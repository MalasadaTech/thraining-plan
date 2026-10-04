# Instructor Guide – Module 1.5.3 – Notification and Distribution

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C ; 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 A / B / B ; 1.5.3.2 2b / 3c / 4c  
- CTI: 1.5.3.1 B / C / C ; 1.5.3.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

A report becomes useful when it reaches the responsible people through a channel that supports the work. A notification chart connects the product to recipients, leadership awareness, and the approved means of delivery.

## Learning Objectives

1. Interpret a notification chart’s recipients, awareness requirements, and channels.
2. Route a supplied report using the chart.
3. Explain why an alternative route does not meet the stated requirements.

**Mapped Proficiency Items:**
- K: 1.5.3.1 – Notification and distribution
- T: 1.5.3.2 – Route a report: name recipients, leadership awareness, and the approved channel

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

### 1. Reading a notification chart

Read the chart across a row so recipient and channel remain connected. Explain the difference between a work owner and someone receiving awareness.

**Key point to reinforce:** Read the product’s work recipients, leadership-awareness requirement, and approved channel together.

### 2. Routing the course examples

Have learners provide all routing elements for each example. Keep channels explicitly tied to the classroom policy rather than declaring all organizational chat invalid.

**Key point to reinforce:** A12 goes to SOC and IR through the case ticket with duty-lead awareness. The CTI RFI follows its own chart row.

### 3. Making the handoff traceable

Ask how another analyst would verify the handoff. Discuss acknowledgement as a local requirement without inventing a new universal gate.

**Key point to reinforce:** Preserve a traceable handoff and any required acknowledgement. Explain why an alternative fails the stated route.

## Knowledge Check — Answer Key

### 1. What does a notification chart tell you?

**Expected answer:** The work recipients, leadership-awareness requirements, and approved channel for the product.

### 2. Route the first A12 incident handoff using the classroom chart and reject an unsuitable alternative.

**Expected answer:** SOC queue and IR receive the case-system ticket; the duty SOC lead gets awareness. A private message to one responder does not satisfy the required queue route.

### 3. Route the CTI RFI and explain when the leadership decision could change.

**Expected answer:** Send it to CTI through a ticket or approved RFI form. No routine separate leadership notification is required by this example, unless leadership requested it or an applicable procedure requires it.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Use the notification chart to route the product, provide appropriate leadership awareness, and preserve a traceable handoff. The approved route connects the completed SOC work to the next responsible function.

Previous: [1.5.2 – Reporting Timeline Requirements](../02-reporting-timelines/student-guide.md)

Next: [2.1.1 — Data, information, and intelligence](../../../02-cti/01-core-intel/01-data-info-intel/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center)
