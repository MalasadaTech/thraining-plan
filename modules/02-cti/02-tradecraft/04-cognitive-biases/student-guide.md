# Module 2.2.4 – Cognitive Biases and Mitigation

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.4 B / C / C ; 2.2.4.1 3c / 4c / 4d  
- Hunter: 2.2.4 A / B / B ; 2.2.4.1 1a / 2b / 3c  
- SOC: 2.2.4 A / A / A ; 2.2.4.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Recognize **confirmation bias**, **anchoring**, and **availability bias** in an analytic judgment and explain how each can distort the product.
2. Select and apply a structured mitigation that gives the judgment a meaningful opportunity to change.

**Mapped Proficiency Items:**
- K: 2.2.4 – Cognitive biases and mitigation
- T: 2.2.4.1 – Identify cognitive bias in a judgment and apply a mitigation technique

## 1. Key Concepts

Cognitive biases are predictable shortcuts in human judgment. Analysts cannot eliminate them by simply deciding to “be objective.” The practical goal is to recognize where a judgment is vulnerable and use a process that forces the reasoning to encounter evidence or alternatives it might otherwise ignore.

This lesson focuses on three biases:

| Bias | What happens | Risk to the product |
|---|---|---|
| **Confirmation bias** | The analyst gives more attention to evidence that fits the favored explanation and discounts evidence that does not. | Alternatives receive an unfair test and the judgment becomes harder to revise. |
| **Anchoring** | An early label, number, or explanation has too much influence on later reasoning. | New evidence is interpreted around the first frame instead of being allowed to change it. |
| **Availability bias** | Recent, vivid, or memorable examples come to mind more easily and feel more representative than they are. | A new event is treated like the last memorable incident without enough shared evidence. |

The task is to identify the **effect on the judgment**, not diagnose the personality or motives of the person who wrote it.

### Confirmation bias

Suppose an analyst already favors the idea that the update domain was a payload host. If the analyst records every suspicious detail supporting that idea but ignores evidence of legitimate software activity, confirmation bias can strengthen the conclusion without actually strengthening the analysis.

A useful mitigation is **ACH** because it requires the analyst to compare the same evidence against competing explanations and look deliberately for evidence that is inconsistent with the favored one.

### Anchoring

Suppose the first report calls the cluster “PRD APT.” Later analysis begins with the unstated assumption that the vendor tracking name identifies a government sponsor. The first label has become an anchor.

A **Key Assumptions Check** can expose the dependency: “vendor label = actual sponsor.” Once written down, the analyst can ask what evidence supports that assumption and what would cause it to fail.

### Availability bias

Suppose the analyst recently worked A12 and then sees a new incident involving PowerShell. Because A12 is vivid and easy to recall, the analyst may prematurely treat the new event as related even when there is no shared infrastructure, file, host, or other meaningful linkage.

A useful mitigation is to make the comparison explicit. ACH can compare “related to A12” against “unrelated activity,” while a Key Assumptions Check can test the premise that superficial similarity implies common origin.

### Mitigation is a process, not a pep talk

“Be more objective,” “keep an open mind,” or “avoid bias” are good intentions, but they do not create a repeatable test. A mitigation should change what the analyst **does** with the reasoning.

The two methods already taught in Module 2.2.2 are sufficient for this lesson:

- **Key Assumptions Check:** expose a premise carrying the judgment and test how fragile it is.
- **ACH:** compare competing explanations against the same evidence and seek evidence that discriminates among them.

The goal is not to prove that the first judgment was wrong. The goal is to give it a fair opportunity to change if the evidence does not support it.

## 2. Knowledge Check

1. Why is “be more objective” not a sufficient bias mitigation?
2. A vendor tracking name is introduced early and later evidence is interpreted around it. Which bias is most directly illustrated, and what mitigation would help?
3. A new PowerShell incident is assumed to be A12-related mainly because A12 was the analyst's most recent case. Which bias is illustrated, and how could the analyst test that assumption?

## 3. Summary

Confirmation bias favors evidence that fits the current explanation. Anchoring gives the first frame too much influence. Availability makes vivid or recent examples feel more representative than they are. Effective mitigation changes the analyst's process by exposing assumptions or comparing alternative explanations, giving the judgment a real chance to move when the evidence warrants it.


## 4. Related Modules

- 2.2.2 – Structured analytic techniques
- 2.2.3 – Admiralty Code (previous)
- 2.1.8 – Attribution
- 2.4.1 – Internal threat intelligence platform

**Next:** [2.3.1 – MITRE ATT&CK for CTI Analysis and Reporting](../../03-frameworks/01-attck-cti/student-guide.md).
