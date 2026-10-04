# Module 2.1.9 – Collection Sources and Methods  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.1.9 – Collection Sources and Methods  
**Subtitle:** Choose evidence sources because they answer the requirement  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Connect the lesson to 2.1.4: requirements define what needs to be known; collection planning decides where to seek the evidence.

---

### Slide 2 – Stage vs source class
**Title:** Collection is the work; source class is where you look

**Collection stage** — the lifecycle activity of gathering relevant material.

**Source class** — the broad class of source from which that material is obtained.

This course uses three source classes: **OSINT, commercial, internal**.

**Speaker Notes:**  
Make this distinction early because the shared word “collection” causes confusion.

---

### Slide 3 – Three source classes
**Title:** OSINT, commercial, internal

**OSINT** — public reporting, public data, open research.  
**Commercial** — licensed intelligence, enrichment, sandboxing, vendor datasets.  
**Internal** — SIEM, EDR, network telemetry, tickets, incident records, hunt output.

No class is always best. The requirement determines what evidence matters.

**Speaker Notes:**  
Describe the questions each class tends to answer well.

---

### Slide 4 – Order follows the question
**Title:** Start where the uncertainty can actually be reduced

**Question:** What happened with the update domain on WS-JLEE during A12?  
→ Internal evidence is an early priority.

**Question:** What public reporting exists about this delivery technique?  
→ OSINT or commercial reporting may come first.

**Speaker Notes:**  
This prevents both “OSINT first” and “internal first” from becoming universal rules.

---

### Slide 5 – A short collection plan
**Title:** Requirement, order, first action, limit

A useful plan states:
1. the **requirement**;
2. the **source class and order**;
3. the **first collection action**; and
4. the **scope limit or stop condition**.

The plan should explain what evidence is needed—not just which tool will be opened.

**Speaker Notes:**  
Keep the planning method lightweight and transferable.

---

### Slide 6 – A12 plan
**Title:** Build the plan from the requirement

**Requirement:** Determine the update domain's role in A12.  
**First class:** Internal.  
**First action:** Review relevant HTTP, DNS, host, and incident evidence.  
**Follow-on:** OSINT or commercial sources if external context would reduce remaining uncertainty.  
**Limit:** Defer unrelated infrastructure pivots unless they help answer the requirement or justify a follow-on.

**Speaker Notes:**  
Explain why each choice follows from the question.

---

### Slide 7 – Plan for evidence, not for a favorite tool
**Title:** The analytical purpose should survive a tool change

Weak plan: **“Open the TIP and search the domain.”**

Stronger plan: **“Use internal telemetry to determine whether WS-JLEE resolved and contacted the domain during A12; use external sources if broader context is still needed.”**

The second plan says what the collection is intended to establish.

**Speaker Notes:**  
Tool operation comes later. This lesson is source selection and collection logic.

---

### Slide 8 – Knowledge Check
**Title:** Knowledge Check

1. The Collection lifecycle stage and a source class are the same thing. True or false? Explain.  
2. “What happened with this domain on our network during A12?” Which class should usually be an early priority, and why?  
3. Build a short A12 plan: first class, first action, possible follow-on class, and one scope limit.

**Speaker Notes:**  
Use the instructor answer key. Accept alternative plans when they follow a clearly stated requirement.

---

### Slide 9 – Summary
**Title:** Collect against the question, not against habit

**OSINT, commercial, internal** are source classes.  
The requirement determines their order and purpose.

A good collection plan explains:
- what evidence is needed;
- where to seek it first; and
- when to stop or create a follow-on requirement.


**Speaker Notes:**  
Close the 2.1 sequence by connecting requirements, evidence, analysis, and communication.

**Next:** [2.2.1 – Estimative language](../../02-tradecraft/01-estimative-language/student-guide.md).
