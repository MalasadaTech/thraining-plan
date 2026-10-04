# Module 1.4.3 – Common False Positive Causes

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.3.1 A / B / C ; 1.4.3.2 2b / 3c / 4c  
- Hunter: 1.4.3.1 B / C / C ; 1.4.3.2 2b / 3c / 4c  
- CTI: 1.4.3.1 A / A / B ; 1.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Recognize analyst/tool activity and overly broad logic as common causes.
2. Identify a supported cause for a supplied false positive.
3. Propose a specific change and explain its coverage tradeoff.

**Mapped Proficiency Items:**
- K: 1.4.3.1 – Common false positive causes
- T: 1.4.3.2 – Given a false positive, identify the cause class and what you would change

## Why This Matters

Once an alert is assessed as a false positive, the explanation can help reduce repeated unnecessary work. A useful recommendation connects the benign activity to the logic that matched and proposes a specific change with an understood effect on coverage.

## 1. Recognizing two common causes

| Cause class | Example | Direction for a proposal |
|---|---|---|
| Analyst or tool activity | An authorized scanner or documented test/replay produces the observed pattern. | Separate test traffic or narrowly identify the approved activity. |
| Untuned or overly broad logic | A threat rule matches every PowerShell process, including verified helpdesk use. | Align predicates or thresholds with the intended threat condition. |

These two classes organize the lesson; they are not an exhaustive operational taxonomy. They can overlap. A scanner is not automatically benign merely because it is organization-owned, and an accurate behavior match may be classified as expected activity by the local product. Begin with the established assessment and authorization evidence.

## 2. Working through a recommendation

For a threat rule that matches any PowerShell process, verified interactive `Get-Help` is routine activity. If the intended requirement is specifically encoded PowerShell from Script Host, propose the image, parent, and command-line predicates that express that requirement. Explain that this narrows coverage and does not detect every form of PowerShell misuse.

For a documented packet replay that causes production alerts, propose using a designated test path or a narrowly scoped test-traffic treatment tied to the verified source and period. A blanket exclusion of all scanner or analyst activity can hide unexpected activity from those systems.

## 3. Making the change reviewable

A concise recommendation should include the cause class, supporting evidence, the exact proposed change, and an expected match and nonmatch. For example: “Overly broad logic: the rule matched authorized help commands. For the Script Host requirement, add the parent and encoded-argument tests; a matching script-host launch should remain visible, while ordinary interactive help should not match.”

Detection Engineering reviews the proposal, checks representative legitimate and suspicious cases, and manages changes under local procedures. If the evidence does not fit either taught cause, describe the observed cause and uncertainty without forcing a category.

## Knowledge Check

1. What are the two cause classes taught here, and can they overlap?
2. For verified Get-Help noise on an any-PowerShell threat rule, propose a change tied to the Script Host requirement.
3. Why is excluding every event from a scanner a weak recommendation?

## Summary

Explain why the benign activity matched, then propose a concrete change tied to the detection requirement. Review its effect on expected matches and missed activity before it is applied.

## Course Connections

Previous: [1.4.2 – Alert Classification](../02-classification/student-guide.md)

Next: [1.4.4 – Common Alert Categorizations](../04-categorizations/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)
