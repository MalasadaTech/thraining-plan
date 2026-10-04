# Instructor Guide – Module 1.4.2 – Alert Classification

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.2.1 A / B / C ; 1.4.2.2 2b / 3c / 4c  
- Hunter: 1.4.2.1 B / C / C ; 1.4.2.2 2b / 3c / 4c  
- CTI: 1.4.2.1 A / A / B ; 1.4.2.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

Classification compares a detection result with an assessed condition. Keeping those two questions separate helps you distinguish a useful alert, a false alarm, and activity that was missed. Each label needs evidence about both the activity and the detection outcome.

## Learning Objectives

1. Define TP, FP, TN, and FN against an explicit target condition.
2. Classify supplied cases and cite activity evidence and detection outcome.
3. Recognize uncertainty and the evidence needed to establish a false negative.

**Mapped Proficiency Items:**
- K: 1.4.2.1 – Alert classification (TP/FP/TN/FN)
- T: 1.4.2.2 – Classify given cases as TP, FP, TN, or FN and cite the evidence

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

### 1. Defining what counts as positive

State the target condition before presenting the matrix. Explain how a behavior match can be technically accurate yet benign.

**Key point to reinforce:** State the target condition, then compare its assessed presence with the detection result: TP, FP, TN, or FN.

### 2. Classifying evidence-supported examples

Require the additional supplied evidence in every case. Avoid teaching that a filename or encoding flag establishes maliciousness.

**Key point to reinforce:** Technical pattern matches alone do not establish maliciousness. The examples supply independent activity assessments.

### 3. Writing the classification and evidence

For the FN, ask whether the data reached the rule. Distinguish a coverage failure from a conclusion about the specific cause.

**Key point to reinforce:** Cite activity and alert evidence. A miss needs a coverage expectation and a reliable scoped check.

## Knowledge Check — Answer Key

### 1. Classify the four supplied cases and cite both sides of each decision.

**Expected answer:** They are TP, FP, TN, and FN respectively. Cite the independently assessed activity and whether the relevant detection alerted.

### 2. Does confirmed wscript-to-encoded-PowerShell behavior alone establish a malicious true positive?

**Expected answer:** No. It establishes the technical pattern. The target condition and authorization or maliciousness assessment still matter; the local system may use a benign-positive category.

### 3. What is needed before calling an unalerted download a false negative?

**Expected answer:** Evidence that the target condition occurred, that it was within the expected detection requirement, and a reliable check showing no relevant alert; assess telemetry availability and the evaluation period.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

Classify the detection outcome against an explicit, evidence-supported target condition. Preserve uncertainty, use local disposition definitions, and investigate misses using both activity evidence and the expected coverage.

Previous: [1.4.1 – Alert Context and Investigation](../01-context-investigation/student-guide.md)

Next: [1.4.3 – Common False Positive Causes](../03-false-positive-causes/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [Microsoft — Alert classification playbooks](https://learn.microsoft.com/en-us/defender-xdr/alert-classification-playbooks)
