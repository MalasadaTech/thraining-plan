# Instructor Guide – Module 2.2.1 – Estimative language

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.1 B / C / C ; 2.2.1.1 3c / 4c / 4c  
- Hunter: 2.2.1 A / B / B ; 2.2.1.1 1a / 2b / 3c  
- SOC: 2.2.1 A / A / A ; 2.2.1.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Help learners communicate the probability of an analytic judgment with consistent estimative language while keeping likelihood separate from confidence in the supporting evidence.

**Context:** The preceding core-intelligence lessons taught learners how to develop a judgment and discuss attribution confidence. This lesson focuses on one part of how that judgment is communicated: how probable the analyst believes the claim to be.

Use the A12 update-domain assessment to make the distinction concrete. Learners should leave understanding that an estimative term communicates probability, while confidence communicates the strength of the evidentiary foundation. Neither substitutes for the reasoning behind the judgment.

**Lesson scope:** Use the seven classroom likelihood terms in the student guide. If a learner's organization uses a different published scale, acknowledge that operational standards can vary. The goal here is consistent interpretation, not memorization of numeric probability bands.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Explain why estimative language is used and interpret the classroom likelihood terms.
2. Write an analytic judgment using a likelihood term and distinguish likelihood from confidence in the supporting evidence.

**Mapped Proficiency Items:**
- K: 2.2.1 – Estimative language
- T: 2.2.1.1 – Use and interpret estimative language in analytic judgments

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---:|---|
| Introduction | 3 minutes | Explain why probability needs explicit language. |
| Classroom likelihood scale | 6 minutes | Establish the seven terms and their relative meaning. |
| Likelihood vs confidence | 6 minutes | Separate probability from evidentiary strength. |
| A12 examples | 4 minutes | Write and interpret judgments in context. |
| Knowledge check and feedback | 4 minutes | Listen for correct use and interpretation. |
| Summary and transition | 1 minute | Connect wording to the structured methods in 2.2.2. |
| **Total** | **24 minutes** | Adjust discussion time as needed. |

## Detailed Teaching Notes

### 1. Begin with the reader's problem

Explain that vague language forces the reader to supply an interpretation the analyst should have communicated. “Could be” establishes possibility but does not tell the reader whether the analyst regards the explanation as remote, evenly balanced, or likely.

The purpose of an estimative scale is consistency. Two analysts using the same term should be trying to communicate roughly the same level of probability, subject to their organization's published standard.

### 2. Walk the scale as an ordered set

Move from **almost certainly** through **remote** and ask learners to notice the ordering rather than memorize unofficial percentages. The important skill is recognizing the direction and relative strength of each term.

If learners ask for exact numbers, explain that organizations sometimes map terms to ranges, but this course does not invent a numeric policy. The classroom terms are sufficient for the learning objective.

### 3. Separate likelihood from confidence

Use the A12 sentence: “The update domain was **likely** used for attempted payload delivery, with **medium confidence**.” Ask what each phrase contributes.

The answer should be:
- **Likely** = the analyst's judgment about probability.
- **Medium confidence** = the analyst's assessment of the evidentiary and reasoning foundation supporting that judgment.

Learners may initially treat stronger likelihood language as stronger evidence. Emphasize that the two dimensions can move independently.

### 4. Keep reasoning visible

An estimative term is not a substitute for evidence. Return briefly to the A12 observations: the request for `/update.exe` during suspicious activity supports a delivery interpretation, while successful download and execution remain unresolved. The term summarizes the analyst's probability judgment about that interpretation; the reasoning explains why.

### 5. Listen for meaningful interpretation

During the knowledge check, accept different likelihood terms when the learner can defend them from the supplied evidence. The objective is correct use of the language, not forcing every learner to choose the same word when the scenario does not provide a complete probability model.

## Common Student Challenges

| Misunderstanding | Teaching response |
|---|---|
| Likelihood and confidence are synonyms. | Ask the learner to identify which phrase describes probability and which describes the evidentiary foundation. |
| “Could be” is precise enough because it admits uncertainty. | Ask whether it means remote, even chance, or likely. The ambiguity demonstrates the problem. |
| Strong likelihood wording proves the evidence is strong. | Show how a claim can be judged likely on a limited evidence base and therefore still carry lower confidence. |
| The classroom terms require invented percentages. | Explain that the course teaches relative terms; use an organization's published ranges when one exists. |

## Knowledge Check – Answer Key

### 1. Why are “likely” and “high confidence” not interchangeable?

**Expected answer:** “Likely” describes the probability of the claim. “High confidence” describes the strength of the evidence and reasoning supporting the judgment.

### 2. “The update domain could be related to A12.” What important information is missing?

**Expected answer:** The reader cannot tell how probable the analyst considers the relationship. A recognized likelihood term would communicate that judgment more clearly.

### 3. Write one A12 judgment using a classroom likelihood term and, if appropriate, a separate confidence statement.

**Acceptable response:** Any coherent judgment using one classroom likelihood term. If confidence is included, it should be expressed separately rather than used as a synonym for likelihood.

## Summary and Transition

Close by reinforcing that estimative language communicates the probability of a judgment, while confidence communicates the strength of its support. The next lesson focuses on methods analysts can use to test the reasoning behind a judgment before they publish it.

## Instructor References

- [ODNI, ICD 203 — Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf). Use the directive to reinforce clear expression of uncertainty and analytic confidence. The classroom term set is instructional and should not be presented as a quoted ODNI probability table.
