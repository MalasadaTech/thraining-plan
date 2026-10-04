# Instructor Guide – Module 3.4.2 – Extracting Hunt Leads from CTI

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.2 B / C / C ; 3.4.2.1–3.4.2.3 3c / 4c / 4d  
- SOC: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
- CTI: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.4.2 – Extracting hunt leads from CTI
- T: 3.4.2.1 – Extract hunt-suitable TTPs from a CTI report
- T: 3.4.2.2 – Extract hunt-suitable artifacts
- T: 3.4.2.3 – State the hunt question those leads support

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Correct the old age-based expiration shortcut: age changes priority/yield, not validity by itself.
- Preserve strong but currently invisible leads as visibility gaps.
- Require provenance and context, not just values.
- Whole netblocks and generic TTP labels are weak unless the report establishes a discriminating relationship.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Why isn't an old hash automatically expired?

**Expected answer:** Age alone does not invalidate a hash; validity depends on source/context, ownership, validity window, and the question being asked.

### 2. What happens to a lead with no telemetry?

**Expected answer:** Preserve it as relevant intelligence, mark it not currently executable as a hunt lead, and record the visibility gap.

### 3. Extract A12 procedure, observable and hunt question.

**Expected answer:** Procedure: HKCU Run Updater → %TEMP%\update.exe. Observable: GET /update.exe to 203.0.113.88:8080. Question: are related persistence/delivery artifacts present on additional Windows workstations?

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.
