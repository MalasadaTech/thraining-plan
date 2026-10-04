# Module 2.2.2 – Structured Analytic Techniques  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.2.2 – Structured Analytic Techniques  
**Subtitle:** Make the reasoning visible and testable  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
The previous lesson focused on wording the judgment. This lesson focuses on testing the reasoning behind it.

---

### Slide 2 – Why structure helps
**Title:** A plausible story can become the default too quickly

Analysts form explanations as they work.

A structured analytic technique slows down a vulnerable part of that reasoning and makes the test visible to someone else.

The goal is not extra paperwork. It is a more inspectable judgment.

**Speaker Notes:**  
Ask learners what could make a conclusion wrong even when it feels plausible. That question sets up both techniques.

---

### Slide 3 – Two reasoning problems
**Title:** Match the method to the problem

**Key Assumptions Check**  
Use it when an important premise is carrying the judgment.

**Analysis of Competing Hypotheses (ACH)**  
Use it when two or more plausible explanations remain live.

**Speaker Notes:**  
The distinction is about the reasoning problem, not which technique appears more sophisticated.

---

### Slide 4 – Key Assumptions Check
**Title:** What must be true for this judgment to hold?

1. State the draft judgment.  
2. Identify the assumptions it depends on.  
3. Ask what supports or weakens each assumption.  
4. Decide how the judgment changes if a critical assumption fails.

**Example:** vendor tracking name = actual sponsor.

**Speaker Notes:**  
Use the PRD APT label to show how an implicit premise becomes testable once it is written down.

---

### Slide 5 – ACH
**Title:** Compare explanations against the same evidence

**H1:** update domain used for A12 payload delivery.  
**H2:** ordinary activity unrelated to the incident.

Compare each important observation against both explanations.

Pay special attention to evidence that **distinguishes** among the hypotheses, not just evidence that seems to support the favorite one.

**Speaker Notes:**  
Explain diagnostic evidence. The `/update.exe` request on port 8080 during suspicious activity is more useful than simply noting that the domain appeared in the case.

---

### Slide 6 – Do not count votes
**Title:** Three supporting facts do not automatically beat one

ACH asks which explanation has difficulty accounting for the evidence.

Evidence consistent with every hypothesis may add little discrimination.

Look deliberately for evidence that could weaken the preferred explanation.

**Speaker Notes:**  
This is the key correction to a common misuse of ACH. The method is not a scorecard for confirming H1.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A conclusion depends on “vendor label = sponsor.” Which technique fits first?  
2. Two plausible explanations remain for an A12 request. Which technique fits?  
3. Why is `/update.exe` over port `8080` during suspicious activity more useful than merely saying the domain appeared?

**Speaker Notes:**  
Listen for selection based on the reasoning problem and for an explanation of diagnostic evidence.

---

### Slide 8 – Summary
**Title:** Test the part of the reasoning most at risk

**Key Assumptions Check:** expose and test critical premises.  
**ACH:** compare competing explanations using the same evidence.

Choose the method that addresses the reasoning problem.

**Next:** [2.2.3 – Admiralty Code](../03-admiralty-code/student-guide.md).
