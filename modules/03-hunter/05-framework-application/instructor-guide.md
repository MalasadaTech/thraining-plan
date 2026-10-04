# Instructor Guide – Module 3.5.1 – Using MITRE ATT&CK for Hunt Planning

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 3c / 4c / 4d  
- SOC: 3.5.1 A / B / B ; 3.5.1.1–3.5.1.2 1a / 2b / 3c ; 3.5.1.3 1a / 1a / 2b  
- CTI: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.5.1 – Using MITRE ATT&CK for hunt planning and coverage analysis
- T: 3.5.1.1 – Map a hunt plan or findings to MITRE ATT&CK
- T: 3.5.1.2 – Use ATT&CK to identify detection or visibility gaps
- T: 3.5.1.3 – Use ATT&CK to support hunt prioritization

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Map the hunt behavior, not an actor's entire ATT&CK profile.
- Use the most specific supported technique/sub-technique.
- Explain that ATT&CK techniques can map to multiple tactics; the relevant tactic depends on the procedure's role in this hunt.
- For A12 HKCU Run, Persistence is supported; privilege escalation is not established.
- ATT&CK is not a hunt-priority score.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Why map this hunt instead of actor profile?

**Expected answer:** Map the procedure this hunt tests or found; actor profiles can contain many unrelated techniques.

### 2. Why Persistence for A12 T1547.001?

**Expected answer:** Because the observed HKCU Run behavior establishes recurring user-context execution/persistence but no elevation in this scenario.

### 3. Telemetry exists, no analytic: which gap?

**Expected answer:** Detection gap.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.

## Supporting References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [T1547.001 Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)
