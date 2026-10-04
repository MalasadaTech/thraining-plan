# Instructor Guide – Module 3.7.3 – Hunt Outputs and Hand-off

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.3 B / C / C ; 3.7.3.1 3c / 4c / 4c  
- SOC: 3.7.3 A / A / B ; 3.7.3.1 1a / 1a / 2b  
- CTI: 3.7.3 A / A / B ; 3.7.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.7.3 – Hunt outputs and hand-off
- T: 3.7.3.1 – Produce required hunt outputs and perform proper hand-off

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Reframe completion around local done criteria, not merely query completion.
- Teach generic output categories as examples, not invented local policy.
- Different findings can have different consumers; local hand-off map decides.
- Preserve searched scope and visibility limitations so negative results are interpretable.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Why isn't query completion hunt completion?

**Expected answer:** A finished hunt also needs the locally required findings, evidence, gaps, limitations, outputs, status/hand-off—not just a completed search.

### 2. Which gap types?

**Expected answer:** Detection gap and visibility gap.

### 3. Why different consumers for compromise/detection/telemetry?

**Expected answer:** Active compromise needs response ownership, a detection gap needs analytic improvement, and missing telemetry needs a telemetry owner; the local hand-off map assigns the actual teams/channels.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.
