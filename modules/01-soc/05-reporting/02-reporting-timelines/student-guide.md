# Module 1.5.2 – Reporting Timeline Requirements

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.2.1 A / B / C ; 1.5.2.2 2b / 3c / 4c  
- Hunter: 1.5.2.1 A / B / B ; 1.5.2.2 2b / 3c / 4c  
- CTI: 1.5.2.1 B / C / C ; 1.5.2.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Describe submission and blocker-escalation clocks.
2. Calculate applicable deadlines from supplied timestamps.
3. Distinguish an at-risk deadline from one already breached.

**Mapped Proficiency Items:**
- K: 1.5.2.1 – Reporting timeline requirements
- T: 1.5.2.2 – Given timestamps, identify which report timeline applies and whether it is at risk

## Why This Matters

Reporting deadlines keep useful information moving while an investigation continues. A submission deadline and a blocker-escalation deadline can run at the same time, so recording their separate start points helps you act on both.

## 1. Understanding the classroom reporting clocks

The following times are classroom assumptions, separate from the alert-response clocks in 1.4.5. Operational and contractual requirements must come from the organization's current procedures.

| Clock | Origin | Classroom limit |
|---|---|---|
| Submit incident report | Decision that an incident report is required. | 30 minutes. |
| Submit RFI | The information question arises. | 60 minutes. |
| Escalate for more information | A blocker prevents completion without help from another function. | 15 minutes. |

A blocker does not pause the submission clock in this example. Escalating the blocker and submitting an available preliminary report may both be needed, according to the applicable process. Other local report types may have their own deadlines.

## 2. Calculating overlapping deadlines

| Supplied situation | Due time and status |
|---|---|
| RFI question at 13:30; unsent at 14:40. | RFI due 14:30; breached by 10 minutes. |
| Incident-report decision at 14:00; blocked at 14:10; still blocked at 14:28. | Blocker escalation due 14:25; breached by 3 minutes. Incident report due 14:30; 2 minutes remain. |

In the second example, the submission deadline has not passed, but it is at risk because the blocker remains with little time available. Name both clocks and their status. The overdue escalation deserves immediate action while the submission obligation remains visible.

## 3. Recording the timing decision

Use a record that makes the report type, origin, due time, current state, and next action clear. For the blocked incident example: “Incident report due 14:30; blocker escalation due 14:25 and overdue at 14:28. Escalate the missing-information need now and coordinate the available submission under the reporting procedure.”

Keep actual timestamps when actions occur. An escalation does not retroactively meet a missed deadline, and completing an alert does not automatically submit its report. Use a consistent time zone and dates when the work crosses midnight.

## Knowledge Check

1. When does each classroom reporting clock begin?
2. Calculate the RFI status for a 13:30 question still unsent at 14:40.
3. At 14:28, an incident report was required at 14:00 and blocked at 14:10. Identify both deadlines and the next action.

## Summary

Track submission by report type and escalation from the time a blocker arises. When both apply, retain both due times and act on the blocker without losing the submission requirement.

## Course Connections

Previous: [1.5.1 – Report Types](../01-report-types/student-guide.md)

Next: [1.5.3 – Notification and Distribution](../03-notification-distribution/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
