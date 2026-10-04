# Instructor Guide – Module 3.7.2 – Hunt Documentation Standards

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.2 B / C / C ; 3.7.2.1 3c / 4c / 4c  
- SOC: 3.7.2 A / A / B ; 3.7.2.1 1a / 1a / 2b  
- CTI: 3.7.2 A / A / B ; 3.7.2.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.7.2 – Hunt documentation standards
- T: 3.7.2.1 – Document a hunt according to local standards

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Differentiate the generic hunt-development card from the official local hunt record.
- Emphasize reproducibility: query/version, population, window, telemetry, filters, findings, limitations.
- Scratch notes are not automatically the authoritative record.
- Use the local standard as source of truth; capture specific onboarding gaps when missing.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Hunt card vs official record?

**Expected answer:** The 3.2.2 card teaches generic hunt reasoning; the official record is the site's required, authoritative documentation.

### 2. Four reproducibility elements?

**Expected answer:** Any four: population, time window, telemetry, query/version, filters/exclusions, evidence/results, limitations, scope changes.

### 3. Unknown repository: what record?

**Expected answer:** Local authoritative hunt repository not yet verified; identify the owner/source needed.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.
