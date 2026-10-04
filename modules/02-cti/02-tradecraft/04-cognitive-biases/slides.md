# Module 2.2.4 – Cognitive Biases and Mitigation  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.2.4 – Cognitive Biases and Mitigation  
**Subtitle:** Give the judgment a fair chance to change  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Frame bias as a normal reasoning risk. The task is to recognize vulnerable reasoning in the product and use a process that can correct it.

---

### Slide 2 – Why mitigation matters
**Title:** Good intentions are not a control

Analysts cannot remove cognitive bias simply by deciding to “be objective.”

A useful mitigation changes what the analyst **does** with the reasoning.

The goal is to expose assumptions and alternatives before the judgment becomes fixed.

**Speaker Notes:**  
Keep the discussion on analytic process, not personality or motives.

---

### Slide 3 – Confirmation bias
**Title:** The favored explanation gets the easier test

**Confirmation bias:** evidence that fits the current explanation receives more attention or weight than evidence that challenges it.

**Risk:** alternatives never receive a fair comparison.

**Useful mitigation:** ACH.

**Speaker Notes:**  
Connect ACH to its purpose from 2.2.2: compare the same evidence against competing explanations and look for inconsistency with the favorite one.

---

### Slide 4 – Anchoring
**Title:** The first frame keeps pulling the analysis back

**Anchoring:** an early label, number, or explanation has too much influence on later reasoning.

**Example:** “PRD APT” appears first, and later evidence is interpreted as though the label already proves sponsorship.

**Useful mitigation:** Key Assumptions Check.

**Speaker Notes:**  
Ask what premise the early label caused the analyst to treat as given.

---

### Slide 5 – Availability bias
**Title:** The memorable case feels more representative than it is

**Availability bias:** recent or vivid examples come to mind easily and feel more relevant than the evidence supports.

**Example:** a new PowerShell case is assumed to be A12-related even though no meaningful linkage has been established.

**Speaker Notes:**  
Ask what actual evidence would connect the new case to A12. This turns a vague similarity into a testable question.

---

### Slide 6 – Mitigation is a process
**Title:** Change the reasoning, not the attitude

**Key Assumptions Check:** expose a premise carrying the judgment and test its fragility.

**ACH:** compare competing explanations against the same evidence and seek evidence that distinguishes among them.

The goal is not to force the first judgment to lose. It is to make sure it received a fair test.

**Speaker Notes:**  
This slide deliberately reuses the two methods rather than introducing another technique list.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Why is “be more objective” not a sufficient mitigation?  
2. A vendor label appears first and continues to frame later evidence. Bias and mitigation?  
3. A new case is assumed to be A12-related mainly because A12 is recent. Bias and mitigation?

**Speaker Notes:**  
Accept overlapping bias answers when the learner can explain the mechanism. Require a concrete process change for the mitigation.

---

### Slide 8 – Summary
**Title:** Protect the reasoning process

**Confirmation:** favored evidence gets the easier test.  
**Anchoring:** the first frame keeps too much influence.  
**Availability:** memorable examples feel more representative than they are.

Use a structured method so the judgment can change when the evidence warrants it.

**Next:** [2.3.1 – MITRE ATT&CK for CTI Analysis and Reporting](../../03-frameworks/01-attck-cti/student-guide.md).
