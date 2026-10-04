# Module 1.4.5 – SLA / Response Time Goals

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.5.1 A / B / C ; 1.4.5.2 2b / 3c / 4c ; 1.4.5.3 2b / 3c / 4c  
- Hunter: 1.4.5.1 A / B / B ; 1.4.5.2 1a / 2b / 3c ; 1.4.5.3 1a / 2b / 3c  
- CTI: 1.4.5.1 A / A / A ; 1.4.5.2 1a / 1a / 1a ; 1.4.5.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the start and close/escalate clocks and their origins.
2. Calculate which response-time goal is at risk or breached.
3. Record a supported closure or escalation against the correct clock.

**Mapped Proficiency Items:**
- K: 1.4.5.1 – Service Level Agreements / Response Time Goals
- T: 1.4.5.2 – Given timestamps, identify whether the start clock or the close/escalate clock is at risk
- T: 1.4.5.3 – Close or escalate an alert and record it against the correct clock

## Why This Matters

Response-time goals help ensure an alert receives attention and reaches an appropriate next state. Keeping each goal’s start point and completion event explicit makes overdue work visible without encouraging premature closure.

## 1. Understanding the two classroom clocks

An SLA can contain several commitments. This lesson focuses on two response-time goals, called clocks for convenience. The numbers and start points below are classroom assumptions, not workplace requirements.

| Clock | Starts at | Completed by | Classroom goal |
|---|---|---|---|
| Start | Alert creation. | Recorded beginning of investigation. | 15 minutes. |
| Close / escalate | Beginning of investigation. | Supported closure or documented escalation. | 45 minutes. |

Before investigation begins, the start clock is running and the second clock has not started in this model. Afterward, preserve whether the start goal was met or breached while tracking close/escalate. Real procedures may use different origins, severity tiers, pauses, or deadlines; consult them rather than transferring these numbers directly.

## 2. Calculating status from timestamps

Use one stated time zone and a complete date where needed. Compute the due time from the defined origin before deciding which clock needs attention.

| Supplied facts | Calculation | Status |
|---|---|---|
| Created 14:00; untouched at 14:18. | Start due 14:15; elapsed 18 minutes. | Start breached by 3 minutes. |
| Created 13:20; started 13:28; open at 14:20. | Start took 8 minutes. Close/escalate due 14:13; elapsed 52 minutes since start. | Start met; close/escalate breached by 7 minutes. |

A goal is breached after its deadline. Before the deadline, it may be at risk if the remaining work is unlikely to finish in time. State the evidence for that forecast. If only the start timestamp is supplied, the earlier start-goal result cannot be reconstructed without creation time.

## 3. Recording the appropriate action

For the first example, begin the investigation and record `started | start breached | 14:18`, with the creation time and due time retained. For the second, record a supported closure if the work is complete, or document escalation, the reason, receiving owner, and time if further handling is needed.

A classroom escalation line could be `escalated | close/escalate breached | 14:20 | unresolved investigation; duty lead notified`. Escalation records a transfer or request for attention; local procedure determines whether acceptance is also required. A breached goal remains breached after the action. Keep the investigation finding and the timing record consistent.

## Knowledge Check

1. Created 14:00 and untouched at 14:18: which clock applies, when was it due, and what is the first action?
2. Created 13:20, started 13:28, and open at 14:20: calculate both clock results.
3. Write an appropriate record for the second case if the investigation still needs the duty lead’s help.

## Summary

Identify the applicable clock, calculate its due time, and record the action actually taken. Preserve both timing status and investigation state, using the organization’s definitions outside the classroom.

## Course Connections

Previous: [1.4.4 – Common Alert Categorizations](../04-categorizations/student-guide.md)

Next: [1.5.1 – Report Types](../../05-reporting/01-report-types/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
