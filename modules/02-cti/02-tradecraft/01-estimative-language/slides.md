# Module 2.2.1 – Estimative language  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.2.1 – Estimative language  
**Subtitle:** Communicating how probable a judgment is  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Introduce estimative language as a way to communicate probability consistently. The goal is not simply to memorize a word list; learners should understand what the terms tell the reader and what they do not.

---

### Slide 2 – Why estimative language matters
**Title:** Do not make the reader guess

Analysts often have to make judgments before every uncertainty is resolved.

A phrase such as **“could be”** tells the reader something is possible, but not how strongly the analyst favors that explanation.

Estimative language makes the analyst's probability judgment explicit.

**Speaker Notes:**  
Ask learners what “could be” means numerically or comparatively. Their different answers demonstrate why a more consistent vocabulary is useful.

---

### Slide 3 – Classroom likelihood scale
**Title:** From almost certainly to remote

**Almost certainly** → **Highly likely** → **Likely** → **Even chance** → **Unlikely** → **Highly unlikely** → **Remote**

The terms move from very high probability to very low probability.

Use an organization's published scale when one exists; this course does not invent operational percentages.

**Speaker Notes:**  
Walk the order and relative meaning. The learning objective is interpretation and use, not memorizing unofficial numeric bands.

---

### Slide 4 – Likelihood and confidence
**Title:** Two different questions

**Likelihood:** How probable is the claim?

**Confidence:** How strongly do the available evidence and reasoning support the judgment?

Both can appear in one assessment:

**Likely, medium confidence.**

**Speaker Notes:**  
Make the distinction explicit. Stronger likelihood wording does not automatically mean stronger evidence.

---

### Slide 5 – Apply it to A12
**Title:** Make the judgment visible

Vague:

“The update domain **could be** the payload host for A12.”

More precise:

“The update domain is **likely** the payload host for A12.”

If useful, add confidence separately and explain the remaining evidence gaps.

**Speaker Notes:**  
Connect the statement to the earlier A12 assessment. The estimative term summarizes the probability judgment; it does not replace the supporting reasoning.

---

### Slide 6 – Interpret the term in context
**Title:** Remote does not mean “we have no idea”

“It is **remote** that this was ordinary browsing.”

The analyst is making a judgment: ordinary browsing has very low likelihood.

The statement still needs evidence and reasoning behind it.

**Speaker Notes:**  
Use this to separate low probability from low confidence or absence of analysis.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Why are **likely** and **high confidence** not interchangeable?  
2. What is missing from “the update domain could be related to A12”?  
3. Write one A12 judgment using a classroom likelihood term.

**Speaker Notes:**  
Listen for probability versus evidentiary strength. Accept defensible wording when the learner uses the term consistently.

---

### Slide 8 – Summary
**Title:** Communicate probability deliberately

A likelihood term tells the reader **how probable** the analyst judges a claim to be.

Confidence tells the reader **how strongly the evidence and reasoning support** that judgment.

Use clear terms so the reader does not have to infer either one.

**Next:** [2.2.2 – Structured Analytic Techniques](../02-structured-techniques/student-guide.md).
