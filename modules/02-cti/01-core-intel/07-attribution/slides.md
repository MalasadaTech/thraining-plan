# Module 2.1.7 – Attribution  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.1.7 – Attribution  
**Subtitle:** Type, confidence, and evidence  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson names who or what cluster sits behind activity, at a type and a confidence. It is not a finished actor profile and not the estimative word list.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts name **who or what cluster** sits behind activity.

Type. Confidence. Evidence.  
Do not invent a nation-state.

**Speaker Notes:**  
This slide is the student intro. Collection, hunt, and defense need the right cluster. Assess the claim against the evidence. Do not write the actor profile in this lesson.

---

### Slide 3 – Purpose and challenges
**Title:** Purpose and challenges

**Purpose** — focus collection, hunt, and defense on the right cluster.

**Challenges** — shared hosting, false flags, vendor marketing names, one-blog claims.

Shared hosting is not “theirs.” A vendor name is a **label**.

**Speaker Notes:**  
Purpose first, then why it is hard. Shared hosting means more than one customer on the same IP or range. A false flag is planted evidence. One blog is one source. Types come next.

---

### Slide 4 – Activity group vs nation-state
**Title:** Activity group vs nation-state

**Activity group** — a cluster of activity (infra, malware, ops). You can defend it without a country.

**Nation-state** — a government sponsor. Needs more than a vendor name.

**Speaker Notes:**  
These are the two classroom types. A PDF title is not a government. Confidence words come on the next slide.

---

### Slide 5 – Classroom confidence
**Title:** Low, medium, high

**Low** — thin or single-source.  
**Medium** — more than one independent line; alternatives remain.  
**High** — several independent lines; alternatives are weak.

Classroom only. Not a live ODNI card.

**Speaker Notes:**  
This is how good the evidence is, not how probable the event is. Likelihood words such as likely and almost certainly wait for 2.2.1. If they ask about a shop card, use the shop card; do not invent percents as policy.

---

### Slide 6 – Assess the claim
**Title:** Assess the claim

Name the type claimed, the confidence claimed, and whether the evidence earns both.

**Fail** — “Vendor PDF says PRD APT, so high-confidence nation-state.”  
Label ≠ country.

**A12** — encoded PowerShell, an update domain, `203.0.113.88`.  
Those facts can support an **activity cluster**. They do not prove a government.

**Speaker Notes:**  
Show both givens before the knowledge check. Honest read on the PDF: activity group / low until independent evidence supports more. Do not tell the intro plot as proof of a government.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A vendor “APT” name is high-confidence nation-state attribution. True or false?  
2. What is the difference between an activity group and a nation-state?  
3. “Vendor PDF says PRD APT — high confidence nation-state.” Assess the claim.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Attribute the cluster you can defend.  
Name type and confidence.  
A vendor label is not high-confidence nation-state.

**Next:** **2.1.8** Collection sources and methods

**Speaker Notes:**  
2.1.8 is where you collect. Stay off source classes unless that lesson is scheduled.
