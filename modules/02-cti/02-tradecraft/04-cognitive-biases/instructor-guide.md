# Instructor Guide – Module 2.2.4 – Cognitive Biases and Mitigation

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.4 B / C / C ; 2.2.4.1 3c / 4c / 4d  
- Hunter: 2.2.4 A / B / B ; 2.2.4.1 1a / 2b / 3c  
- SOC: 2.2.4 A / A / A ; 2.2.4.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Help learners recognize three common cognitive biases in the reasoning visible on the page and apply a structured mitigation that can change the analysis if the evidence warrants it.

**Context:** The earlier tradecraft lessons provided tools for expressing probability, testing reasoning, and evaluating sources. This lesson explains why analysts still need deliberate safeguards: human judgment naturally gives extra weight to favored explanations, early frames, and memorable examples.

Keep the focus on the **product and process** rather than diagnosing the analyst. The lesson teaches confirmation bias, anchoring, and availability bias, with Key Assumptions Check and ACH as the available mitigations.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Recognize confirmation bias, anchoring, and availability bias in an analytic judgment and explain how each can distort the product.
2. Select and apply a structured mitigation that gives the judgment a meaningful opportunity to change.

**Mapped Proficiency Items:**
- K: 2.2.4 – Cognitive biases and mitigation
- T: 2.2.4.1 – Identify cognitive bias in a judgment and apply a mitigation technique

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---:|---|
| Introduction | 3 minutes | Explain why intent alone does not remove bias. |
| Three biases | 7 minutes | Recognize how each changes the reasoning process. |
| Structured mitigation | 6 minutes | Reuse Key Assumptions Check and ACH as practical controls. |
| Worked examples | 4 minutes | Apply the concepts to attribution and A12 similarity. |
| Knowledge check | 4 minutes | Identify bias and choose a mitigation. |
| **Total** | **24 minutes** | Adjust discussion time as needed. |

## Detailed Teaching Notes

### 1. Frame bias as a reasoning risk

Explain that cognitive biases are normal features of human judgment. The course is not asking learners to diagnose colleagues or claim immunity from bias. It is teaching them to notice patterns in an analytic product that suggest the reasoning did not receive a fair test.

### 2. Distinguish the three biases by mechanism

**Confirmation bias:** the preferred explanation affects which evidence receives attention or weight.

**Anchoring:** an early label, number, or frame continues to shape reasoning even after new evidence arrives.

**Availability bias:** a recent or vivid example is easier to recall and therefore feels more representative than the actual evidence justifies.

Use the effect on the product to distinguish them. A single scenario can contain more than one bias, but learners should identify the clearest mechanism first.

### 3. Connect each bias to a process change

For confirmation bias, ACH is often useful because the analyst must compare the same evidence against alternatives and consider inconsistency with the favored explanation.

For anchoring, a Key Assumptions Check can expose what the first frame caused the analyst to treat as given.

For availability, either technique may help. The important step is to force the analyst to state what evidence actually connects the current event to the memorable prior case.

### 4. Use the vendor-label example carefully

“Vendor PDF says PRD APT, so high nation-state” is useful because the first label can act as an anchor and the analyst may then seek confirming evidence. Ask learners what assumption is carrying the conclusion rather than simply asking them to call the author biased.

### 5. Use A12 to teach availability

Present a new PowerShell case with no shared infrastructure, file, host, or other linkage. If the analyst treats it as A12-related because A12 is recent and memorable, availability is the clearest issue. Ask what evidence would actually be required to support a relationship.

## Common Student Challenges

| Misunderstanding | Teaching response |
|---|---|
| “Be more objective” is an adequate mitigation. | Ask what repeatable action changes the analysis. Name a structured method. |
| Bias is a personality flaw in the author. | Redirect to the reasoning visible in the product and the process that can correct it. |
| Every scenario must have exactly one bias. | Explain that biases can overlap; identify the mechanism most directly demonstrated. |
| Mitigation is meant to disprove the original judgment. | Emphasize that mitigation gives the judgment a fair chance to change, not a requirement to reverse it. |

## Knowledge Check – Answer Key

### 1. Why is “be more objective” insufficient?

**Expected answer:** It expresses intent but does not create a repeatable test of the reasoning. A structured method changes what the analyst actually does with the judgment.

### 2. Early vendor tracking name continues to frame later evidence

**Expected answer:** Anchoring is the most direct bias. A Key Assumptions Check can test the premise that the vendor label establishes the actor or sponsor. Confirmation bias may also appear if contradictory evidence is being discounted.

### 3. New PowerShell incident assumed related to A12 because A12 is recent

**Expected answer:** Availability bias. The analyst can compare “related to A12” and “unrelated activity” using ACH or test the assumption that superficial similarity implies linkage with a Key Assumptions Check.

## Summary and Transition

Close by reinforcing that bias mitigation is part of analytic process design. The analyst does not need to eliminate human judgment; they need methods that expose vulnerable reasoning before it becomes a fixed conclusion. The next module applies analytical frameworks to supported activity, starting with ATT&CK.
