# Module 2.1.4 – Intelligence Requirements  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.1.4 – Intelligence Requirements  
**Subtitle:** Define the question before you collect  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Frame requirements as the mechanism that gives collection and analysis a purpose, not as administrative paperwork.

---

### Slide 2 – Why requirements matter
**Title:** A clear question keeps the work focused

Without a requirement, analysts can collect everything interesting and still not know when the stakeholder's need has been answered.

A requirement tells the team:
- **what needs to be known**;
- **why the answer matters**; and
- **what scope the work should cover**.

**Speaker Notes:**  
Connect the requirement to a stopping condition and a reason for each collection step.

---

### Slide 3 – What makes a useful requirement
**Title:** Question, decision need, scope

**Question** — what needs to be known?  
**Decision or need** — what will the stakeholder do with the answer?  
**Scope** — what subject, environment, and time window matter?

The requirement should guide collection without predetermining the answer.

**Speaker Notes:**  
Do not turn this into a mandatory template. The goal is clarity and direction.

---

### Slide 4 – PIR means priority
**Title:** Priority is one characteristic of a requirement

A **Priority Intelligence Requirement (PIR)** is a requirement leadership or the program has identified as especially important.

A **standing** requirement remains active over time.  
An **ad-hoc** requirement addresses a one-time or event-driven need.

These labels can overlap. A standing requirement can also be a PIR.

**Speaker Notes:**  
Correct the common misconception that PIR, standing, and ad-hoc are mutually exclusive categories.

---

### Slide 5 – Refine the stakeholder's question
**Title:** “Are we seeing them?” is a starting point

Before collecting, clarify:
- Who or what is **“them”**?
- What activity counts as **“seeing”** them?
- In what environment?
- During what time window?

**Speaker Notes:**  
Have learners name the ambiguities before showing the A12 refinement.

---

### Slide 6 – A12 requirement
**Title:** Turn the ask into something analysts can work

**Stakeholder ask:** “Are we seeing them?”

**Refined requirement:**  
**What role did the update domain play in the activity on WS-JLEE during A12?**

A narrower follow-on could ask whether the domain delivered `/update.exe` during the A12 window.

**Speaker Notes:**  
Explain that the appropriate specificity depends on the decision the stakeholder actually needs to make.

---

### Slide 7 – The requirement directs the evidence
**Title:** What helps answer this question?

Potentially relevant evidence:
- HTTP and DNS activity;
- host or file evidence;
- incident notes and process context.

A sibling domain may be worth recording, but it can be deferred if it does not help answer the current requirement.

**Speaker Notes:**  
Teach scope control as prioritization, not as discarding unexpected evidence.

---

### Slide 8 – Knowledge Check
**Title:** Knowledge Check

1. Every intelligence requirement is a PIR. True or false? What makes a PIR different?  
2. “Are we seeing them?” What two things would you clarify before collecting?  
3. Write a clearer A12 requirement and name one piece of evidence that would help answer it and one pivot that could reasonably wait.

**Speaker Notes:**  
Use the instructor answer key. Accept equivalent requirements when the learner can explain how they direct the work.

---

### Slide 9 – Summary
**Title:** The requirement gives analysis direction

A clear requirement identifies the **question**, the **need**, and the **scope**.

A PIR is distinguished by **priority**.  
Standing and ad-hoc describe persistence or trigger and can overlap with priority.

The requirement helps analysts decide what evidence matters now and what can wait.


**Speaker Notes:**  
Transition from defining the question to judging whether the resulting product is usable.

**Next:** [2.1.5 – RFI Intake and Prioritization](../05-rfi-intake/student-guide.md).
