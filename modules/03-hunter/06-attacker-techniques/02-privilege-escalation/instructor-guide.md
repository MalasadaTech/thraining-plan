# Instructor Guide – Module 3.6.2 – Privilege Escalation Techniques

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.2 B / C / C ; 3.6.2.1 3c / 4c / 4c  
- SOC: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
- CTI: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.6.2 – Privilege escalation techniques
- T: 3.6.2.1 – Recognize privilege escalation techniques in logs or telemetry

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Correct the old inference that user→SYSTEM without consent proves token theft.
- Separate elevation outcome from method attribution.
- Require method-specific evidence for UAC bypass and token manipulation.
- Services and scheduled tasks can produce elevated execution depending on prerequisites; context determines tactic.
- A12 Run key is persistence, not evidence of elevation.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. SYSTEM child: what is proven vs unresolved?

**Expected answer:** You can say a higher context was observed if the lineage is reliable; the technique/method remains unresolved without mechanism evidence.

### 2. What supports token manipulation?

**Expected answer:** Token duplication/impersonation or process-with-token telemetry, source/target security contexts, and linkage to a privileged token source.

### 3. Why isn't fodhelper.exe alone proof?

**Expected answer:** fodhelper is an auto-elevated component, but its presence alone does not show the associated bypass mechanism or prove adversary-caused elevation.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.

## Supporting References

- [T1548.002 Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002/)
- [T1134 Access Token Manipulation](https://attack.mitre.org/techniques/T1134/)
- [T1543.003 Windows Service](https://attack.mitre.org/techniques/T1543/003/)
- [T1068 Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)
