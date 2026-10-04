# Instructor Guide – Module 1.4.3 – Common False Positive Causes

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.3.1 A / B / C ; 1.4.3.2 2b / 3c / 4c  
- Hunter: 1.4.3.1 B / C / C ; 1.4.3.2 2b / 3c / 4c  
- CTI: 1.4.3.1 A / A / B ; 1.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Once an alert is assessed as a false positive, the explanation can help reduce repeated unnecessary work. A useful recommendation connects the benign activity to the logic that matched and proposes a specific change with an understood effect on coverage.

## Learning Objectives

1. Recognize analyst/tool activity and overly broad logic as common causes.
2. Identify a supported cause for a supplied false positive.
3. Propose a specific change and explain its coverage tradeoff.

**Mapped Proficiency Items:**
- K: 1.4.3.1 – Common false positive causes
- T: 1.4.3.2 – Given a false positive, identify the cause class and what you would change

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required.

Use the proficiency levels above to adjust prompting and explanation depth. The module focuses on its mapped knowledge and tasks; the linked next lesson develops the next step.

## Suggested Timing

| Section | Minutes | Focus |
|---|---|---|
| Opening | 2 | Connect the lesson to its purpose. |
| Explanation and worked example | 12 | Read the supplied evidence and demonstrate the reasoning. |
| Knowledge check and feedback | 6 | Complete the interpretation or modification tasks. |
| Summary and transition | 2 | Consolidate the result and connect the next lesson. |
| **Total** | **22** | |

## Detailed Teaching Notes

### 1. Recognizing two common causes

Keep the prior classification visible so cause analysis does not become an unsupported benignness assumption. Discuss overlap between the two classes.

**Key point to reinforce:** Common causes include analyst/tool activity and overly broad logic. They can overlap.

### 2. Working through a recommendation

Ask which requirement the added predicates serve. More predicates are useful only if they preserve the intended coverage.

**Key point to reinforce:** Tie proposed predicates or test-traffic handling to a verified cause and the intended requirement.

### 3. Making the change reviewable

Have learners name a match and nonmatch after the change. Specificity makes the recommendation reviewable; “tune it” alone does not.

**Key point to reinforce:** Name the exact change, expected match/nonmatch, and coverage tradeoff for review.

## Knowledge Check — Answer Key

### 1. What are the two cause classes taught here, and can they overlap?

**Expected answer:** Analyst/tool activity and untuned/overly broad logic. They can overlap and are not exhaustive.

### 2. For verified Get-Help noise on an any-PowerShell threat rule, propose a change tied to the Script Host requirement.

**Expected answer:** Classify overly broad logic and propose the relevant parent and encoded-command tests; explain the narrower scope and its remaining blind spots.

### 3. Why is excluding every event from a scanner a weak recommendation?

**Expected answer:** It can hide unexpected or unauthorized activity from that system. Use verified authorization and a narrowly scoped change or separate test path, then assess coverage.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Explain why the benign activity matched, then propose a concrete change tied to the detection requirement. Review its effect on expected matches and missed activity before it is applied.

Previous: [1.4.2 – Alert Classification](../02-classification/student-guide.md)

Next: [1.4.4 – Common Alert Categorizations](../04-categorizations/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)
