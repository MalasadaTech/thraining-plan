# Instructor Guide – Module 3.2.2 – Hunt Development Concepts

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.2 B / C / C ; 3.2.2.1–3.2.2.3 3c / 4c / 4d  
- SOC: 3.2.2 A / B / B ; 3.2.2.1–3.2.2.3 1a / 1a / 2b  
- CTI: 3.2.2 A / B / B ; 3.2.2.1–3.2.2.3 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.2.2 – Hunt development concepts
- T: 3.2.2.1 – Develop and document a hunt hypothesis
- T: 3.2.2.2 – Scope and prioritize a hunt
- T: 3.2.2.3 – Identify unique patterns or behaviors suitable for hunting

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Teach falsifiability: a hypothesis should permit a meaningful no-findings outcome within scope.
- Scope includes population, time, telemetry and meaningful exclusions.
- Replace literal 'unique' with distinctive/discriminating; uniqueness is rarely knowable in advance.
- Negative results are bounded by visibility; no telemetry means no valid absence claim.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Why isn't 'hunt persistence' a hypothesis?

**Expected answer:** It is a topic/class, not a falsifiable proposition with expected evidence.

### 2. Four development fields?

**Expected answer:** Hypothesis, scope, priority, distinctive/discriminating pattern.

### 3. Write an A12 scoped hypothesis.

**Expected answer:** Example: If A12-style persistence exists on other user workstations, registry/file telemetry in the last 14 days should show Run values pointing to update.exe or related payloads in user-writable paths.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.
