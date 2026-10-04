# Module 2.1.8 – Attribution  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.1.8 – Attribution  
**Subtitle:** Make the strongest claim the evidence can support  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Introduce attribution as claim calibration rather than a race to name a country.

---

### Slide 2 – Why attribute?
**Title:** Attribution connects activity to a defensible body of evidence

Useful attribution can help analysts:
- connect related reporting;
- compare behaviors and infrastructure;
- focus collection and hunting; and
- prioritize defensive work.

The goal is not the most specific name possible. It is the most specific claim the evidence can support.

**Speaker Notes:**  
Ask whether defenders can act on a cluster even without a sponsor name. They can.

---

### Slide 3 – Two levels in this lesson
**Title:** Activity cluster vs nation-state sponsorship

**Activity group / cluster**  
Observations judged to belong to the same body of activity.

**Nation-state sponsorship**  
A stronger claim that a government sponsors, directs, or conducts the activity.

Stronger attribution claims require stronger evidence.

**Speaker Notes:**  
A cluster-level assessment can be both useful and appropriately cautious.

---

### Slide 4 – Why attribution is hard
**Title:** Cyber evidence is reusable and sometimes misleading

- shared or rented infrastructure;
- malware and tool reuse;
- false flags and deception;
- vendor naming differences;
- public reports that omit key evidence.

A concrete artifact is not automatically a unique fingerprint.

**Speaker Notes:**  
Explain how each factor creates alternative explanations.

---

### Slide 5 – Confidence describes support
**Title:** How strongly does the evidence support the judgment?

**Low** — limited support or important alternatives.  
**Medium** — multiple relevant lines, with meaningful gaps or alternatives remaining.  
**High** — several strong, substantially independent lines converge and alternatives are limited.

Use your organization's formal confidence standard when one exists.

**Speaker Notes:**  
Keep confidence separate from likelihood words covered in 2.2.1.

---

### Slide 6 – A label is not the evidence
**Title:** Deconstruct the claim

> “The vendor report calls the actor PRD APT, so A12 is a high-confidence nation-state operation.”

**Claimed level:** nation-state sponsorship  
**Claimed confidence:** high  
**Evidence shown:** vendor tracking label

The evidence presented does not justify the conclusion.

**Speaker Notes:**  
Ask what additional independent or sponsor-relevant evidence would be needed.

---

### Slide 7 – Apply claim discipline to A12
**Title:** Say what the current evidence actually supports

A12 includes suspicious PowerShell activity, an update domain, and related network observations.

Those facts may contribute to an **activity cluster**.

They do not, by themselves, establish a government sponsor.

If an external source makes the stronger claim, distinguish **their assessment** from **your own evidentiary basis**.

**Speaker Notes:**  
This is the professional habit the lesson should leave behind.

---

### Slide 8 – Knowledge Check
**Title:** Knowledge Check

1. A vendor “APT” name is sufficient for high-confidence nation-state attribution. True or false? Why?  
2. What is the difference between an activity cluster and a nation-state sponsorship claim?  
3. Assess: “Vendor PDF says PRD APT — high confidence nation-state.” What is claimed, what evidence is shown, and what would be needed to strengthen it?

**Speaker Notes:**  
Use the instructor answer key. Focus on claim, confidence, and evidence.

---

### Slide 9 – Summary
**Title:** Attribute only as far as the evidence allows

Separate:
- **what level is being claimed**;
- **how confident the analyst is**; and
- **what evidence supports the claim**.

A tracking label can be useful without proving sponsorship.


**Speaker Notes:**  
Transition to where analysts gather the information needed to answer requirements and strengthen assessments.

**Next:** [2.1.9 – Collection Sources and Methods](../09-collection-sources/student-guide.md).
