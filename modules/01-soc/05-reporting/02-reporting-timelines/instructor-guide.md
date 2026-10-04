# Instructor Guide – Module 1.5.2 – Reporting Timeline Requirements

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.2.1 A / B / C ; 1.5.2.2 2b / 3c / 4c  
- Hunter: 1.5.2.1 A / B / B ; 1.5.2.2 2b / 3c / 4c  
- CTI: 1.5.2.1 B / C / C ; 1.5.2.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Reporting deadlines keep useful information moving while an investigation continues. A submission deadline and a blocker-escalation deadline can run at the same time, so recording their separate start points helps you act on both.

## Learning Objectives

1. Describe submission and blocker-escalation clocks.
2. Calculate applicable deadlines from supplied timestamps.
3. Distinguish an at-risk deadline from one already breached.

**Mapped Proficiency Items:**
- K: 1.5.2.1 – Reporting timeline requirements
- T: 1.5.2.2 – Given timestamps, identify which report timeline applies and whether it is at risk

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

### 1. Understanding the classroom reporting clocks

Write each origin next to its duration. Explain that these are teaching assumptions rather than externally mandated reporting times.

**Key point to reinforce:** Classroom limits: incident submission 30 minutes; RFI submission 60; blocker escalation 15, each from its own origin.

### 2. Calculating overlapping deadlines

Have learners calculate due times first, then elapsed time. Distinguish a missed escalation from a submission deadline that is still approaching.

**Key point to reinforce:** The blocker and submission clocks can overlap. Escalation does not pause the submission goal in this example.

### 3. Recording the timing decision

Ask for a record that preserves both obligations. Avoid implying a blocker automatically suspends reporting.

**Key point to reinforce:** Record type, origin, due time, status, and next action. Distinguish at risk from already breached.

## Knowledge Check — Answer Key

### 1. When does each classroom reporting clock begin?

**Expected answer:** Incident submission begins at the report-required decision, RFI submission at the question, and blocker escalation when the analyst becomes blocked.

### 2. Calculate the RFI status for a 13:30 question still unsent at 14:40.

**Expected answer:** Due 14:30 under the 60-minute goal; breached by 10 minutes.

### 3. At 14:28, an incident report was required at 14:00 and blocked at 14:10. Identify both deadlines and the next action.

**Expected answer:** Escalation was due 14:25 and is overdue by 3 minutes. Submission is due 14:30 with 2 minutes remaining and is at risk. Escalate the blocker and address submission under the applicable process.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Track submission by report type and escalation from the time a blocker arises. When both apply, retain both due times and act on the blocker without losing the submission requirement.

Previous: [1.5.1 – Report Types](../01-report-types/student-guide.md)

Next: [1.5.3 – Notification and Distribution](../03-notification-distribution/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
