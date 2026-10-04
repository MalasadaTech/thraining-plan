# Instructor Guide – Module 2.2.2 – Structured Analytic Techniques

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.2 B / C / C ; 2.2.2.1 3c / 4c / 4d  
- Hunter: 2.2.2 A / B / B ; 2.2.2.1 1a / 2b / 3c  
- SOC: 2.2.2 A / A / A ; 2.2.2.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Help learners select and apply a structured analytic technique that addresses the reasoning problem in front of them. The lesson uses a Key Assumptions Check for hidden premises and ACH for competing explanations.

**Context:** Module 2.2.1 taught learners how to communicate the probability of a judgment. This lesson moves behind the wording and asks how the analyst tests the reasoning that supports the judgment.

The emphasis should be practical. Learners do not need a large ACH spreadsheet or a catalog of techniques. They should be able to recognize the difference between an untested assumption and competing hypotheses, then apply the appropriate method to a small A12 example.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Explain why structured analytic techniques are useful and choose between a Key Assumptions Check and ACH for a given problem.
2. Apply the selected technique to a short analytic problem and explain what it reveals about the judgment.

**Mapped Proficiency Items:**
- K: 2.2.2 – Structured analytic techniques
- T: 2.2.2.1 – Apply a structured analytic technique and select the right one for a scenario

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---:|---|
| Introduction | 3 minutes | Explain why analysts externalize and test reasoning. |
| Key Assumptions Check | 6 minutes | Identify and test premises carrying a judgment. |
| ACH | 7 minutes | Compare competing explanations using discriminating evidence. |
| Technique selection | 3 minutes | Choose the method that fits the problem. |
| Knowledge check | 4 minutes | Apply both concepts to short scenarios. |
| Summary and transition | 1 minute | Connect reasoning quality to source evaluation. |
| **Total** | **24 minutes** | Adjust discussion time as needed. |

## Detailed Teaching Notes

### 1. Start with the reason for structure

Explain that analysts naturally form explanations as they work. A structured technique does not eliminate judgment; it slows down a vulnerable part of the reasoning and records what was tested.

The useful teaching question is: **What could make this conclusion wrong even if it currently feels plausible?**

### 2. Teach the Key Assumptions Check as a dependency test

Use the vendor-label example. The draft conclusion treats “PRD APT” as proof of identity or sponsorship. Ask learners what must be true for that leap to work.

Once they identify “vendor label = actual sponsor,” ask what evidence supports it and what evidence would weaken it. The goal is to show that assumptions are not automatically bad; they become dangerous when a critical one remains invisible and untested.

### 3. Teach ACH as comparison, not evidence counting

Use H1 payload delivery versus H2 ordinary activity. List a few pieces of evidence and ask which ones actually help distinguish between the hypotheses.

Emphasize that ACH is not “H1 has three supporting facts and H2 has one.” Evidence that both hypotheses predict is less useful than evidence that one has difficulty explaining. Encourage learners to look for inconsistency and disconfirming evidence, particularly against the favored explanation.

### 4. Choose based on the reasoning problem

Give two quick prompts:
- One conclusion rests on an untested premise → Key Assumptions Check.
- Two explanations plausibly account for the same event → ACH.

Acknowledge that mature analyses may use several techniques, but the classroom task is selection and application, not maximum technique count.

## Common Student Challenges

| Misunderstanding | Teaching response |
|---|---|
| More techniques always means better analysis. | Ask which specific reasoning risk each technique is addressing. |
| ACH means counting supporting evidence. | Redirect attention to evidence that is inconsistent with, or diagnostic among, the hypotheses. |
| An assumption is automatically an error. | Explain that analysis necessarily uses assumptions; the task is to identify critical ones and test their fragility. |
| A full ACH matrix is required for any comparison. | Use the compact classroom version to demonstrate the reasoning principle before introducing heavier documentation elsewhere. |

## Knowledge Check – Answer Key

### 1. Vendor tracking name assumed to identify a government sponsor

**Expected answer:** Key Assumptions Check. The problem is an untested premise carrying the attribution judgment.

### 2. Two plausible explanations for an A12 network request

**Expected answer:** ACH. The analyst should compare the same evidence against both explanations and focus on evidence that distinguishes between them.

### 3. Why `/update.exe` on port `8080` during suspicious activity is useful

**Expected answer:** It is more diagnostic than the mere presence of the domain because it is harder for the ordinary-activity hypothesis to explain in the incident context. Learners should still identify what evidence could weaken the payload-delivery hypothesis.

## Summary and Transition

Close by reinforcing that structured techniques make reasoning inspectable. The next lesson turns to a different analytic problem: separately evaluating the reliability of a source and the credibility of a particular piece of information.
