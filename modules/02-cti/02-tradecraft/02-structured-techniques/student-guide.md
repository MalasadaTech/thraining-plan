# Module 2.2.2 – Structured Analytic Techniques

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.2 B / C / C ; 2.2.2.1 3c / 4c / 4d  
- Hunter: 2.2.2 A / B / B ; 2.2.2.1 1a / 2b / 3c  
- SOC: 2.2.2 A / A / A ; 2.2.2.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain why structured analytic techniques are useful and choose between a **Key Assumptions Check** and **Analysis of Competing Hypotheses (ACH)** for a given problem.
2. Apply the selected technique to a short analytic problem and explain what it reveals about the judgment.

**Mapped Proficiency Items:**
- K: 2.2.2 – Structured analytic techniques
- T: 2.2.2.1 – Apply a structured analytic technique and select the right one for a scenario

## 1. Key Concepts

Analysts rarely begin with a completely blank mind. A first explanation may already feel plausible, a vendor report may supply a convenient label, or a familiar pattern may shape what the analyst expects to find. Structured analytic techniques provide a deliberate way to examine that reasoning before the preferred explanation becomes the conclusion by default.

The point of a structured technique is not extra paperwork. It is to make part of the reasoning visible and testable so another analyst can understand what was challenged and why the judgment changed—or did not change.

This lesson uses two techniques:

| Technique | Best fit | Core question |
|---|---|---|
| **Key Assumptions Check** | One or more assumptions are carrying the judgment. | What are we treating as true, and what happens if that assumption is weak or false? |
| **Analysis of Competing Hypotheses (ACH)** | Two or more plausible explanations remain live. | Which evidence is most consistent or inconsistent with each explanation, and which evidence actually distinguishes among them? |

### Key Assumptions Check

An assumption is something the analysis relies on without directly establishing it. Some assumptions are reasonable and necessary; the risk comes when an important assumption remains invisible.

A compact Key Assumptions Check can be done in four steps:

1. State the draft judgment.
2. Identify the assumptions that must be true for that judgment to hold.
3. Ask what evidence supports each assumption and what would weaken or break it.
4. Decide whether the judgment still holds if a critical assumption changes.

Consider an attribution claim: a vendor report labels the activity “PRD APT,” and the draft assessment treats that label as proof of who conducted the activity. A Key Assumptions Check makes the hidden step explicit:

**Assumption:** the vendor tracking name identifies the actual sponsor of the activity.

Once stated, the analyst can test it. A tracking label may identify a cluster of activity without establishing government sponsorship. The exercise does not automatically prove the draft wrong; it shows exactly what additional evidence the conclusion depends on.

### Analysis of Competing Hypotheses

ACH is useful when the analyst has multiple plausible explanations and wants to avoid evaluating evidence only through the favorite one.

A compact classroom ACH can be done in four steps:

1. State the competing hypotheses.
2. List the important evidence relevant to them.
3. Compare how well each item fits—or conflicts with—each hypothesis.
4. Give extra attention to **diagnostic evidence**: evidence that helps distinguish one hypothesis from another.

For A12, consider:

- **H1:** the update domain was being used for payload delivery.
- **H2:** the request was ordinary browsing or software activity unrelated to the incident.

The request for `/update.exe` on port `8080` during the suspicious activity is harder to reconcile with H2 than with H1. That makes it useful because it helps discriminate between the explanations. The analyst should still consider what evidence would weaken H1 rather than simply counting how many facts appear to support it.

### Choosing the technique

Use a Key Assumptions Check when the main risk is an untested premise inside the current judgment. Use ACH when the problem is better represented as competing explanations that need to be compared against the same evidence.

The techniques can be used together in real analysis, but the learning objective here is to choose the method that best addresses the immediate reasoning problem and apply it deliberately.

## 2. Knowledge Check

1. A draft judgment depends on the assumption that a vendor tracking name identifies a government sponsor. Which technique is the better first fit, and why?
2. An analyst has two plausible explanations for an A12 network request. Which technique is the better fit, and what kind of evidence should receive the most attention?
3. In the A12 ACH example, explain why `/update.exe` over port `8080` during suspicious activity is more useful than simply saying “the domain appeared in the case.”

## 3. Summary

Structured analytic techniques make important parts of the analyst's reasoning visible and testable. A Key Assumptions Check examines the premises carrying a judgment. ACH compares multiple plausible explanations and pays particular attention to evidence that distinguishes among them. The method should match the reasoning problem the analyst needs to test.


## 4. Related Modules

- 2.2.1 – Estimative language (previous)
- 2.2.3 – Admiralty Code
- 2.2.4 – Cognitive biases
- 2.1.8 – Attribution

**Next:** [2.2.3 – Admiralty Code](../03-admiralty-code/student-guide.md).
