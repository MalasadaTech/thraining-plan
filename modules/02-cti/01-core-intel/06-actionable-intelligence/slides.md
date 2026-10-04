# Module 2.1.6 – Ensuring Intelligence Is Actionable  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.1.6 – Ensuring Intelligence Is Actionable  
**Subtitle:** Can the recipient use this assessment?  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Connect this lesson to 2.1.4: the requirement defined the question; now evaluate whether the product helps the intended recipient act on the answer.

---

### Slide 2 – Actionable means usable
**Title:** Interesting is not the same as actionable

Intelligence is actionable when the recipient can use it to make a **timely decision** or take a **meaningful next step**.

The test is not simply:
- Is it detailed?
- Does it contain indicators?
- Does it tell someone to do something?

The test is whether it supports the **right decision for the requirement**.

**Speaker Notes:**  
Start with decision support rather than a checklist.

---

### Slide 3 – Five questions to ask
**Title:** Evaluate the relationship between product and recipient

1. Does it **answer the requirement**?  
2. Is the **recipient** clear?  
3. Is the next decision or action **specific enough**?  
4. Is it **timely**?  
5. Are the **judgment and limits** clear?

**Speaker Notes:**  
These are a course heuristic, not a local compliance form.

---

### Slide 4 – Actionable does not require a command
**Title:** Sometimes the next step is investigation or collection

A useful product may support a recipient in deciding to:
- preserve evidence;
- investigate a host or domain;
- collect missing data;
- reprioritize work; or
- take no immediate action.

The value comes from improving the decision, not from adding an imperative sentence.

**Speaker Notes:**  
Prevent learners from equating actionability with command language.

---

### Slide 5 – Common failure modes
**Title:** Why a product may not be usable

- It answers a different question.
- It provides facts without explaining their significance.
- The next step is vague: “be aware” or “monitor as needed.”
- It arrives after the decision window.
- It hides important uncertainty.

**Speaker Notes:**  
For “monitor,” emphasize that the problem is lack of specificity, not the word itself.

---

### Slide 6 – A12: actionable assessment
**Title:** The assessment supports a next step

**Requirement:** What role did the update domain play in A12?

**Assessment:** The domain likely supported attempted payload delivery. WS-JLEE requested `/update.exe` during the suspicious activity.

**Next step:** IR preserves and reviews network, file, and process evidence to determine whether transfer and execution occurred.

**Limit:** Successful download and execution remain unresolved.

**Speaker Notes:**  
Walk requirement, recipient, next step, timing, and uncertainty.

---

### Slide 7 – Compare the vague product
**Title:** “Be aware” does not explain what the recipient should do

> New malicious activity has been reported. Be aware and monitor as needed.

Ask:
- Which requirement does this answer?
- What should be monitored?
- In which environment?
- What decision will the monitoring support?

**Speaker Notes:**  
Use questions to reveal why the product is not actionable as written.

---

### Slide 8 – Knowledge Check
**Title:** Knowledge Check

1. “Be aware and monitor as needed” is actionable because it tells the recipient to monitor. True or false? Why?  
2. Name three questions you can ask when evaluating actionability.  
3. In the A12 assessment, identify the requirement, recipient, next step, and one remaining uncertainty.

**Speaker Notes:**  
Use the instructor answer key. Require reasoning rather than pass/fail only.

---

### Slide 9 – Summary
**Title:** Actionable intelligence improves a real decision

A usable product:
- answers the requirement;
- gives the right recipient enough specificity;
- arrives in time; and
- makes the judgment and its limits clear.

Actionability is about **decision support**, not just detail or directive language.


**Speaker Notes:**  
Transition to how the same underlying assessment must be shaped for different consumers.

**Next:** [2.1.7 – Tailoring Output to the Audience](../07-tailoring-audience/student-guide.md).
