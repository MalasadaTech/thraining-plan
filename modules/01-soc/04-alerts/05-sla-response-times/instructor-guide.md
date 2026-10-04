# Instructor Guide – Module 1.4.5 – SLA / Response Time Goals

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.5.1 A / B / C ; 1.4.5.2 2b / 3c / 4c ; 1.4.5.3 2b / 3c / 4c  
- Hunter: 1.4.5.1 A / B / B ; 1.4.5.2 1a / 2b / 3c ; 1.4.5.3 1a / 2b / 3c  
- CTI: 1.4.5.1 A / A / A ; 1.4.5.2 1a / 1a / 1a ; 1.4.5.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Response-time goals help ensure an alert receives attention and reaches an appropriate next state. Keeping each goal’s start point and completion event explicit makes overdue work visible without encouraging premature closure.

## Learning Objectives

1. Explain the start and close/escalate clocks and their origins.
2. Calculate which response-time goal is at risk or breached.
3. Record a supported closure or escalation against the correct clock.

**Mapped Proficiency Items:**
- K: 1.4.5.1 – Service Level Agreements / Response Time Goals
- T: 1.4.5.2 – Given timestamps, identify whether the start clock or the close/escalate clock is at risk
- T: 1.4.5.3 – Close or escalate an alert and record it against the correct clock

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

### 1. Understanding the two classroom clocks

Ask learners to identify the origin and completion event before doing arithmetic. Keep all classroom times in a single stated time zone.

**Key point to reinforce:** Classroom clocks: creation to investigation start, 15 minutes; investigation start to close/escalate, 45 minutes.

### 2. Calculating status from timestamps

Walk both calculations and distinguish overdue from a forecasted risk. Highlight the added creation time needed to establish that start was met.

**Key point to reinforce:** Calculate due times first. Preserve the result of the start goal while tracking the second clock.

### 3. Recording the appropriate action

Have learners write the action line and explain why it reflects the actual work state. Completion of a timing task must not change the evidence-based finding.

**Key point to reinforce:** Record the supported action, actual time, reason, and owner. A later action does not erase a breach.

## Knowledge Check — Answer Key

### 1. Created 14:00 and untouched at 14:18: which clock applies, when was it due, and what is the first action?

**Expected answer:** Start clock, due 14:15 and breached by 3 minutes. Begin investigation and record the actual start time and breach.

### 2. Created 13:20, started 13:28, and open at 14:20: calculate both clock results.

**Expected answer:** Start met in 8 minutes. Close/escalate was due 14:13 and is breached by 7 minutes.

### 3. Write an appropriate record for the second case if the investigation still needs the duty lead’s help.

**Expected answer:** Record escalation at 14:20 against the breached close/escalate clock, including the unresolved issue and receiving owner. Do not record unsupported closure or erase the breach.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Identify the applicable clock, calculate its due time, and record the action actually taken. Preserve both timing status and investigation state, using the organization’s definitions outside the classroom.

Previous: [1.4.4 – Common Alert Categorizations](../04-categorizations/student-guide.md)

Next: [1.5.1 – Report Types](../../05-reporting/01-report-types/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
