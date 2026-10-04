# Instructor Guide – Module 3.4.1 – Assessing CTI for Hunting Value

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.1 B / C / C ; 3.4.1.1 3c / 4c / 4d  
- SOC: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
- CTI: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.4.1 – Assessing CTI for hunting value
- T: 3.4.1.1 – Triage a CTI report: hunt / don't hunt / hand off, and say why

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Use applicability, testability, visibility, scope and incremental value as the triage lens.
- Correct the old rule that 'IR already owns it' always means hand-off; a reactive hunt may broaden scope during an incident.
- Hand-off/coordination applies to immediate containment or a task better owned by another function.
- Threat severity or actor fame is not hunt-worthiness.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Five hunt-worthiness checks?

**Expected answer:** Applicability, testability, visibility, scope, incremental value.

### 2. Why can hunting continue during IR?

**Expected answer:** IR may own containment on known hosts while hunting searches the wider estate for related activity; coordinate to avoid conflict.

### 3. A12 procedure + telemetry + coverage gap: disposition?

**Expected answer:** Hunt. It is locally applicable, testable, visible, bounded, and can expose a detection gap or additional hosts.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.
