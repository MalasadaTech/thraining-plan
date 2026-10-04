# Instructor Guide – Module 3.2.1 – Hunt Types

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.1 B / C / C ; 3.2.1.1–3.2.1.4 3c / 4c / 4c  
- SOC: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
- CTI: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.2.1 – Hunt types
- T: 3.2.1.1 – Execute an intel-driven hunt
- T: 3.2.1.2 – Execute a hypothesis-driven hunt
- T: 3.2.1.3 – Execute a reactive hunt
- T: 3.2.1.4 – Execute an anomaly-based hunt

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- State that the four labels are a course taxonomy, not a universal industry standard.
- Classify by the primary initiating signal; allow overlap.
- Emphasize that all hunts should mature into a testable question even if they did not begin as hypothesis-driven.
- Reactive hunting expands or tests scope around a known incident; it is not a rewrite of the incident ticket.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Why can hunt types overlap?

**Expected answer:** Because the labels describe starting signals and real hunts can have multiple motivations; classify the primary initiating signal.

### 2. CTI-supplied procedure: which primary type?

**Expected answer:** Intel-driven.

### 3. A12 estate-wide expansion: which type and question?

**Expected answer:** Reactive; ask whether the same or related A12 artifacts/behavior exist on additional systems.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.
