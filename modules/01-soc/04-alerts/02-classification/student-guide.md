# Module 1.4.2 – Alert Classification

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.2.1 A / B / C ; 1.4.2.2 2b / 3c / 4c  
- Hunter: 1.4.2.1 B / C / C ; 1.4.2.2 2b / 3c / 4c  
- CTI: 1.4.2.1 A / A / B ; 1.4.2.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Define TP, FP, TN, and FN against an explicit target condition.
2. Classify supplied cases and cite activity evidence and detection outcome.
3. Recognize uncertainty and the evidence needed to establish a false negative.

**Mapped Proficiency Items:**
- K: 1.4.2.1 – Alert classification (TP/FP/TN/FN)
- T: 1.4.2.2 – Classify given cases as TP, FP, TN, or FN and cite the evidence

## Why This Matters

Classification compares a detection result with an assessed condition. Keeping those two questions separate helps you distinguish a useful alert, a false alarm, and activity that was missed. Each label needs evidence about both the activity and the detection outcome.

## 1. Defining what counts as positive

First state the condition being evaluated. For this lesson, the target condition is malicious or unauthorized activity within the stated detection requirement. A positive result means the relevant detection alerted; a negative result means it did not alert within the defined scope and time.

| Label | Detection result | Assessed target condition |
|---|---|---|
| True positive (TP) | Alerted. | Present. |
| False positive (FP) | Alerted. | Absent. |
| True negative (TN) | Did not alert. | Absent. |
| False negative (FN) | Did not alert. | Present and within the expected detection requirement. |

A rule can correctly match a technical behavior that is authorized. Some products label this “informational/expected activity” or a benign positive. Apply the local platform's definitions and explain your basis. When evidence is insufficient, record an unresolved assessment instead of forcing a benign or malicious label.

## 2. Classifying evidence-supported examples

| Supplied classroom case | Classification and reason |
|---|---|
| The Script Host/PowerShell rule alerts; follow-up evidence confirms the command performed unauthorized activity within the rule's intended scope. | TP: the alert and assessed target condition are both present. |
| An overly broad threat rule alerts on interactive `Get-Help`; the activity is verified as authorized helpdesk use. | FP against this lesson's threat condition: an alert occurred but the target condition is absent. |
| Verified ordinary browsing is within the evaluation sample and the relevant detector produces no alert. | TN: the target condition and alert are both absent. |
| A download is independently confirmed malicious and within required coverage; relevant logs show it occurred, but a checked alert record shows no alert during the evaluated period. | FN: the required target condition occurred without the expected alert. |

The command-line pattern alone does not confirm maliciousness. Likewise, `/update.exe` plus an empty queue does not by itself establish an FN: you need the maliciousness assessment, coverage expectation, and a reliable check for the relevant alert.

## 3. Writing the classification and evidence

Record the label, the condition being assessed, the evidence supporting that assessment, and the detection outcome. For an FN, include the checked rule/source, time range, and whether the necessary telemetry reached the detection system. If the source was absent, identify the visibility failure rather than automatically blaming rule logic.

TN and FN usually arise from reviewing activity beyond fired alerts, such as a scoped test, related evidence, or a hunt. An alert queue alone cannot establish that all unalerted activity was benign. Classification should remain revisable when new evidence changes the assessment.

## Knowledge Check

1. Classify the four supplied cases and cite both sides of each decision.
2. Does confirmed wscript-to-encoded-PowerShell behavior alone establish a malicious true positive?
3. What is needed before calling an unalerted download a false negative?

## Summary

Classify the detection outcome against an explicit, evidence-supported target condition. Preserve uncertainty, use local disposition definitions, and investigate misses using both activity evidence and the expected coverage.

## Course Connections

Previous: [1.4.1 – Alert Context and Investigation](../01-context-investigation/student-guide.md)

Next: [1.4.3 – Common False Positive Causes](../03-false-positive-causes/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [Microsoft — Alert classification playbooks](https://learn.microsoft.com/en-us/defender-xdr/alert-classification-playbooks)
