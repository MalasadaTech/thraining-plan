# Instructor Guide – Module 3.6.1 – Persistence Techniques

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.1 B / C / C ; 3.6.1.1 3c / 4c / 4c  
- SOC: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
- CTI: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.6.1 – Persistence techniques
- T: 3.6.1.1 – Recognize persistence techniques in logs or telemetry

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Broaden persistence beyond the overly narrow 'runs after reboot/logon/time trigger' definition, while keeping the course's Windows examples.
- Technique recognition does not equal maliciousness; baseline/context matters.
- Scheduled Tasks and Windows Services can map to multiple tactics depending on how they are used.
- A12 HKCU Run supports user-context persistence, not privilege escalation by itself.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Run-key evidence fields?

**Expected answer:** Exact key path, value name, value data/target, creator/user/process, and target file context.

### 2. Why can scheduled task serve multiple tactics?

**Expected answer:** Task Scheduler can be used for Execution, Persistence, or Privilege Escalation depending on trigger, account, prerequisites, and purpose.

### 3. Legitimate updater + Run key: still persistence technique?

**Expected answer:** No. It is still a persistence mechanism; benign/malicious judgment comes from context.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.

## Supporting References

- [T1547.001 Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)
- [T1053.005 Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)
- [T1543.003 Windows Service](https://attack.mitre.org/techniques/T1543/003/)
