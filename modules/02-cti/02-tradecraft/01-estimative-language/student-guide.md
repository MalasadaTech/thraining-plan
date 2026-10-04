# Module 2.2.1 – Estimative language

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.1 B / C / C ; 2.2.1.1 3c / 4c / 4c  
- Hunter: 2.2.1 A / B / B ; 2.2.1.1 1a / 2b / 3c  
- SOC: 2.2.1 A / A / A ; 2.2.1.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain why estimative language is used and interpret the classroom likelihood terms.
2. Write an analytic judgment using a likelihood term and distinguish likelihood from confidence in the supporting evidence.

**Mapped Proficiency Items:**
- K: 2.2.1 – Estimative language
- T: 2.2.1.1 – Use and interpret estimative language in analytic judgments

## 1. Key Concepts

Analysts often have to make a judgment before every uncertainty has been resolved. Estimative language gives the reader a consistent way to understand **how probable the analyst believes a claim is**. Instead of leaving the reader to interpret vague phrases such as “could be” or “we believe,” the analyst uses a term with an agreed meaning.

This course uses the following classroom scale:

| Term | Meaning in this lesson |
|---|---|
| **Almost certainly** | Near certain; you would be surprised if it were not true. |
| **Highly likely** | Very probable. |
| **Likely** | More probable than not. |
| **Even chance** | About as likely as not. |
| **Unlikely** | More probable that it is not true. |
| **Highly unlikely** | Very improbable. |
| **Remote** | Very little chance. |

These terms are a teaching scale for this course. An organization may publish its own terminology or probability ranges; when it does, analysts should use that standard consistently rather than inventing their own percentages.

### Likelihood and confidence answer different questions

A likelihood term describes **the probability of the judgment**. Confidence describes **how strongly the available evidence and reasoning support that judgment**. They can appear together because they communicate different things.

For example:

> We assess that the update domain was **likely** used for attempted payload delivery in A12, with **medium confidence**.

“Likely” tells the reader how probable the analyst judges the delivery role to be. “Medium confidence” tells the reader how much weight to place on that judgment given the quality, quantity, and consistency of the supporting evidence.

A judgment can therefore have a relatively high likelihood while still carrying limited confidence if the evidence base is thin. Keeping the two ideas separate prevents the reader from treating strong wording as a substitute for strong evidence.

### Why vague possibility words are not enough

Words such as *could*, *may*, and *might* can be useful in ordinary writing, but by themselves they usually say only that something is possible. They do not tell the reader whether the analyst sees the explanation as remote, evenly balanced, or likely.

Suppose the analyst writes:

> The update domain could be the payload host for A12.

The reader still has to guess how strongly the analyst favors that explanation. Compare it with:

> The update domain is **likely** the payload host for A12.

The second sentence communicates the judgment more precisely. If the evidence is still limited, the analyst can express that separately through confidence and by explaining the gaps.

### Interpreting the term in context

An estimative term modifies the claim it is attached to. In the statement “It is **remote** that the traffic represents ordinary browsing,” *remote* means the analyst judges ordinary browsing to have very low likelihood. It does not mean the analyst has no evidence or has refused to make a judgment.

The underlying reasoning still matters. Estimative language communicates the strength of the judgment; it does not replace the evidence and analysis that support it.

## 2. Knowledge Check

1. Why are “likely” and “high confidence” not interchangeable?
2. A report says, “The update domain could be related to A12.” What important information is missing from that wording?
3. Write one A12 judgment using a classroom likelihood term and, if appropriate, a separate confidence statement.

## 3. Summary

Estimative language makes analytic uncertainty easier for readers to understand and compare. A likelihood term communicates how probable the analyst judges a claim to be. Confidence communicates how strongly the evidence and reasoning support that judgment. Using both deliberately gives the reader more information than vague possibility language alone.


## 4. Related Modules

- 2.1.8 – Attribution confidence
- 2.1.9 – Collection sources (previous)
- 2.2.2 – Structured analytic techniques
- 2.2.3 – Admiralty Code

## Supporting Reference

[ODNI, ICD 203 — Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf): supports clear expression of uncertainty, likelihood, and confidence in analytic judgments. The classroom scale above is an instructional scale rather than a quoted ODNI probability table.

**Next:** [2.2.2 – Structured Analytic Techniques](../02-structured-techniques/student-guide.md).
