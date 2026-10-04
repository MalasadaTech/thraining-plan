# Module 2.1.7 – Tailoring Output to the Audience  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.1.7 – Tailoring Output to the Audience  
**Subtitle:** Same assessment, different consumer  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Connect this lesson to actionability: a product has to be usable by a particular consumer, not by an abstract “reader.”

---

### Slide 2 – Begin with the audience
**Title:** Who will use this, and what do they need to decide?

Before writing, ask:
- Who is the **consumer**?
- What decision or action do they own?
- What do they already know?
- What evidence and caveats do they need to use the assessment correctly?

**Speaker Notes:**  
This is audience analysis. Make it a reasoning step, not a formatting afterthought.

---

### Slide 3 – What changes
**Title:** Content, format, and level of detail

**Content** — which facts and implications are foregrounded.  
**Format** — how the product is structured or presented.  
**Level of detail** — how much technical evidence and context is included.

**What stays:** the evidence and supported analytic judgment.

**Speaker Notes:**  
Tailoring can substantially change wording and order without changing the conclusion.

---

### Slide 4 – The common A12 assessment
**Title:** Start from the same supported judgment

> We assess that the update domain likely supported attempted payload delivery during A12. WS-JLEE requested `/update.exe` during the suspicious activity. Successful download and execution remain unresolved.

Two audiences will need different versions of this same assessment.

**Speaker Notes:**  
Use this as the shared source for the next two slides.

---

### Slide 5 – Leadership version
**Title:** Lead with implication, ownership, and the key gap

**A12 involved suspicious PowerShell activity on WS-JLEE and an external domain that likely supported attempted payload delivery. IR has the affected host; the immediate evidence gap is whether the requested file was successfully delivered or executed.**

Leadership usually does not need raw request fields or every artifact in the main line.

**Speaker Notes:**  
Ask what leadership can decide or support from this version.

---

### Slide 6 – IR / SOC version
**Title:** Preserve the details needed to investigate

**WS-JLEE requested `/update.exe` from the update domain during A12. CTI assesses the domain likely supported attempted payload delivery. Review the related network, file, and process evidence to determine whether transfer and execution occurred.**

Technical consumers need the host, behavior, artifacts, and evidence gap.

**Speaker Notes:**  
Compare the evidence and judgment with the leadership version. They are consistent; the emphasis differs.

---

### Slide 7 – Two opposite mistakes
**Title:** Too much detail can obscure; too little can disable

**Overloaded leadership product:** the decision point disappears inside hashes, paths, and raw logs.

**Under-detailed technical product:** IR receives a polished one-liner but not enough evidence to investigate.

Good tailoring balances **relevance and sufficiency**.

**Speaker Notes:**  
Tailoring is not simply making one version shorter.

---

### Slide 8 – Knowledge Check
**Title:** Knowledge Check

1. Tailoring means changing the judgment so leadership is more comfortable with it. True or false? Why?  
2. What three elements of the product can you adjust?  
3. Write a short leadership version of the A12 assessment and name two details you would retain or add for IR / SOC.

**Speaker Notes:**  
Use the instructor answer key. Accept multiple defensible products.

---

### Slide 9 – Summary
**Title:** Tailor the presentation, preserve the analysis

Know the **consumer** and their **decision** first.

Adjust **content**, **format**, and **detail**.  
Keep the evidence, judgment, and important uncertainty consistent.

The goal is the same supported assessment in a form each reader can use correctly.


**Speaker Notes:**  
Transition from how an assessment is communicated to how attribution claims are calibrated to evidence.

**Next:** [2.1.8 – Attribution](../08-attribution/student-guide.md).
