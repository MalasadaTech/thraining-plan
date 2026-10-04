# Module 1.4.2 – Alert Classification

- Define TP, FP, TN, and FN against an explicit target condition.
- Classify supplied cases and cite activity evidence and detection outcome.
- Recognize uncertainty and the evidence needed to establish a false negative.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

Classification compares a detection result with an assessed condition. Keeping those two questions separate helps you distinguish a useful alert, a false alarm, and activity that was missed. Each label needs evidence about both the activity and the detection outcome.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Defining what counts as positive

State the target condition, then compare its assessed presence with the detection result: TP, FP, TN, or FN.

**Speaker notes:** State the target condition before presenting the matrix. Explain how a behavior match can be technically accurate yet benign.

---

## Reference — Defining what counts as positive

| Label | Detection result | Assessed target condition |
|---|---|---|
| True positive (TP) | Alerted. | Present. |
| False positive (FP) | Alerted. | Absent. |
| True negative (TN) | Did not alert. | Absent. |
| False negative (FN) | Did not alert. | Present and within the expected detection requirement. |

**Speaker notes:** State the target condition before presenting the matrix. Explain how a behavior match can be technically accurate yet benign. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Classifying evidence-supported examples

Technical pattern matches alone do not establish maliciousness. The examples supply independent activity assessments.

**Speaker notes:** Require the additional supplied evidence in every case. Avoid teaching that a filename or encoding flag establishes maliciousness.

---

## Reference — Classifying evidence-supported examples

| Supplied classroom case | Classification and reason |
|---|---|
| The Script Host/PowerShell rule alerts; follow-up evidence confirms the command performed unauthorized activity within the rule's intended scope. | TP: the alert and assessed target condition are both present. |
| An overly broad threat rule alerts on interactive `Get-Help`; the activity is verified as authorized helpdesk use. | FP against this lesson's threat condition: an alert occurred but the target condition is absent. |
| Verified ordinary browsing is within the evaluation sample and the relevant detector produces no alert. | TN: the target condition and alert are both absent. |
| A download is independently confirmed malicious and within required coverage; relevant logs show it occurred, but a checked alert record shows no alert during the evaluated period. | FN: the required target condition occurred without the expected alert. |

**Speaker notes:** Require the additional supplied evidence in every case. Avoid teaching that a filename or encoding flag establishes maliciousness. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Writing the classification and evidence

Cite activity and alert evidence. A miss needs a coverage expectation and a reliable scoped check.

**Speaker notes:** For the FN, ask whether the data reached the rule. Distinguish a coverage failure from a conclusion about the specific cause.

---

## Knowledge check

1. Classify the four supplied cases and cite both sides of each decision.
2. Does confirmed wscript-to-encoded-PowerShell behavior alone establish a malicious true positive?
3. What is needed before calling an unalerted download a false negative?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

Classify the detection outcome against an explicit, evidence-supported target condition. Preserve uncertainty, use local disposition definitions, and investigate misses using both activity evidence and the expected coverage.

Previous: [1.4.1 – Alert Context and Investigation](../01-context-investigation/student-guide.md)

Next: [1.4.3 – Common False Positive Causes](../03-false-positive-causes/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [Microsoft — Alert classification playbooks](https://learn.microsoft.com/en-us/defender-xdr/alert-classification-playbooks)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
