# Instructor Guide – Module 3.4.3 – STIX as Hunt Input

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.3 B / C / C ; 3.4.3.1 3c / 4c / 4c ; 3.4.3.2 3c / 4c / 4d  
- SOC: 3.4.3 A / A / B ; 3.4.3.1 1a / 1a / 2b ; 3.4.3.2 1a / 1a / 2b  
- CTI: 3.4.3 A / B / B ; 3.4.3.1 1a / 2b / 3c ; 3.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.4.3 – STIX as hunt input
- T: 3.4.3.1 – Identify hunt-relevant objects in a report or bundle
- T: 3.4.3.2 – Turn those objects into hunt leads

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Correct the old claim that Malware objects inherently provide hashes.
- Teach Indicator pattern, Observed Data/SCOs, Attack Pattern, Sighting and Relationship as distinct hunt inputs.
- Bundle membership does not create semantic relationships.
- Context objects can prioritize a hunt without being directly queryable.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Why no automatic hash in Malware?

**Expected answer:** STIX Malware is a threat-domain object describing malware; hashes are represented through SCOs, Indicators, Observed Data, or related objects.

### 2. Which object carries a detection pattern?

**Expected answer:** Indicator.

### 3. Why inspect Relationships?

**Expected answer:** Bundle membership has no semantic meaning; explicit Relationships/Sightings/references establish why objects are connected.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.

## Supporting References

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
