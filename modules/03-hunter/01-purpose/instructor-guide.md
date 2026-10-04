# Instructor Guide – Module 3.1 – Purpose of Threat Hunting

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.1.1 B / C / C ; 3.1.1.1 3c / 4c / 4c ; 3.1.1.2 3c / 4c / 4d  
- SOC: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
- CTI: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.1.1 – Purpose of Threat Hunting
- T: 3.1.1.1 – Explain the purpose of threat hunting in the context of the security program
- T: 3.1.1.2 – Identify examples of activity that existing controls might miss

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Frame hunting as deliberate search beyond already-surfaced alerts, not as a second SOC queue.
- Make the false-negative correction explicit: no alert does not automatically mean a control failed.
- Use A12 to distinguish detection gap, visibility gap, and potential false negative.
- Negative hunt results are bounded by scope and telemetry; they do not prove enterprise-wide absence.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Why does hunting exist alongside the SOC?

**Expected answer:** Threat hunting deliberately searches for relevant activity not already adequately surfaced by controls and feeds findings/gaps back into response, CTI, telemetry, and detection.

### 2. Detection gap vs visibility gap?

**Expected answer:** Detection gap: needed telemetry exists but analytic coverage is absent/insufficient. Visibility gap: needed telemetry is missing/insufficient.

### 3. No analytic exists for the unalerted HTTP event: false negative or coverage gap?

**Expected answer:** No. If no analytic was expected to detect it, it is uncovered activity/coverage gap. A false negative requires an expected control that failed.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.
