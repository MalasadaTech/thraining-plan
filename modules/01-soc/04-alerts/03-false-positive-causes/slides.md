# Module 1.4.3 – Common False Positive Causes

- Recognize analyst/tool activity and overly broad logic as common causes.
- Identify a supported cause for a supplied false positive.
- Propose a specific change and explain its coverage tradeoff.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

Once an alert is assessed as a false positive, the explanation can help reduce repeated unnecessary work. A useful recommendation connects the benign activity to the logic that matched and proposes a specific change with an understood effect on coverage.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Recognizing two common causes

Common causes include analyst/tool activity and overly broad logic. They can overlap.

**Speaker notes:** Keep the prior classification visible so cause analysis does not become an unsupported benignness assumption. Discuss overlap between the two classes.

---

## Reference — Recognizing two common causes

| Cause class | Example | Direction for a proposal |
|---|---|---|
| Analyst or tool activity | An authorized scanner or documented test/replay produces the observed pattern. | Separate test traffic or narrowly identify the approved activity. |
| Untuned or overly broad logic | A threat rule matches every PowerShell process, including verified helpdesk use. | Align predicates or thresholds with the intended threat condition. |

**Speaker notes:** Keep the prior classification visible so cause analysis does not become an unsupported benignness assumption. Discuss overlap between the two classes. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through a recommendation

Tie proposed predicates or test-traffic handling to a verified cause and the intended requirement.

**Speaker notes:** Ask which requirement the added predicates serve. More predicates are useful only if they preserve the intended coverage.

---

## Supplied example

For a threat rule that matches any PowerShell process, verified interactive `Get-Help` is routine activity. If the intended requirement is specifically encoded PowerShell from Script Host, propose the image, parent, and command-line predicates that express that requirement. Explain that this narrows coverage and does not detect every form of PowerShell misuse.

**Speaker notes:** Ask which requirement the added predicates serve. More predicates are useful only if they preserve the intended coverage.

---

## Making the change reviewable

Name the exact change, expected match/nonmatch, and coverage tradeoff for review.

**Speaker notes:** Have learners name a match and nonmatch after the change. Specificity makes the recommendation reviewable; “tune it” alone does not.

---

## Knowledge check

1. What are the two cause classes taught here, and can they overlap?
2. For verified Get-Help noise on an any-PowerShell threat rule, propose a change tied to the Script Host requirement.
3. Why is excluding every event from a scanner a weak recommendation?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

Explain why the benign activity matched, then propose a concrete change tied to the detection requirement. Review its effect on expected matches and missed activity before it is applied.

Previous: [1.4.2 – Alert Classification](../02-classification/student-guide.md)

Next: [1.4.4 – Common Alert Categorizations](../04-categorizations/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
