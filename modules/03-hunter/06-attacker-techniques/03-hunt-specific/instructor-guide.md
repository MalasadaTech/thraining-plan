# Instructor Guide – Module 3.6.3 – Hunt for a Specific Persistence or Privilege-Escalation Technique

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.3 3c / 4c / 4d  
- SOC: 3.6.3 1a / 1a / 2b  
- CTI: 3.6.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- T: 3.6.3 – Hunt for specific persistence or privilege escalation techniques

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Use the ATT&CK technique name correctly; 'Updater' is a procedure/artifact, not the technique.
- Teach exact-observed vs behavior-broadened hunting as a precision/coverage trade-off.
- Require scope and telemetry in the hunt line.
- Prevent wrong-class hunts by requiring evidence of the technique's role and prerequisites.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Technique vs procedure pattern?

**Expected answer:** The ATT&CK technique is the behavior class; the procedure pattern is the concrete implementation/artifact searched locally.

### 2. Exact vs broadened trade-off?

**Expected answer:** Exact searches are precise but can miss variants; broadened behavior searches improve coverage but increase benign candidates.

### 3. Write A12 T1547.001 hunt line.

**Expected answer:** Example: T1547.001/Persistence; user workstations; last 14 days; registry+file telemetry; exact Updater→%TEMP%\update.exe then broaden to rare Run values launching from user-writable Temp paths.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.

## Supporting References

- [T1547.001 Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)
