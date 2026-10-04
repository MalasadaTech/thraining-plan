# Module 2.1.3 – Intelligence Types  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.1.3 – Intelligence Types  
**Subtitle:** Match the answer to the decision  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Introduce type as the decision level a requirement or product supports. The transferable skill is not memorizing labels in isolation; it is recognizing what the recipient needs to decide.

---

### Slide 2 – Type follows the decision need
**Title:** What question is the product trying to answer?

A report's **length**, polish, or amount of technical detail does not determine its type.

Start with two questions:
- **What does the recipient need to understand?**
- **What decision will they make with the answer?**

**Speaker Notes:**  
Use this to break the common shortcut that long equals strategic and indicators equal tactical.

---

### Slide 3 – Four types
**Title:** Strategic, operational, tactical, technical

| Type | Primary decision need |
|---|---|
| **Strategic** | How should leadership understand or change risk, priorities, or posture? |
| **Operational** | How should defenders manage an operation, campaign, incident set, or hunt over time? |
| **Tactical** | What should a defender do about the activity in front of them? |
| **Technical** | What concrete artifacts or characteristics can analysts detect, validate, or pivot on? |

**Speaker Notes:**  
These are the definitions used in this course. Other organizations may label the boundaries differently, so local consistency matters.

---

### Slide 4 – One incident, different questions
**Title:** A12 can support more than one type

**Technical:** What domains, IPs, files, and request paths are associated with A12?  
**Tactical:** What should SOC or IR do now with WS-JLEE and the update domain?  
**Operational:** How is A12 unfolding, and what should defenders prioritize across the investigation?  
**Strategic:** Does the broader threat materially change organizational risk or defensive priorities?

**Speaker Notes:**  
The incident is the evidence source; the question determines the type. A12 may be enough to answer some questions and only one input to others.

---

### Slide 5 – Technical vs tactical
**Title:** The observable is not the response decision

**Technical evidence:**  
`203.0.113.88`  
`GET /update.exe`

**Tactical use:**  
Investigate connections from WS-JLEE to the update domain and preserve the associated file and process evidence.

Technical tells you **what can be identified**. Tactical tells a defender **what to do with that understanding**.

**Speaker Notes:**  
This is the boundary learners are most likely to confuse.

---

### Slide 6 – Operational vs strategic
**Title:** Manage the activity vs change the posture

**Operational** intelligence helps a team manage an ongoing body of activity across days or weeks.

**Strategic** intelligence helps leadership understand broader implications for risk, resources, policy, or posture.

Time horizon can help, but the **decision being supported** is the stronger clue.

**Speaker Notes:**  
A long campaign report may still be operational. A short leadership assessment may be strategic.

---

### Slide 7 – Type is not a lifecycle stage
**Title:** Two different dimensions

A **stage** describes the work being performed: collection, processing, analysis, dissemination, and so on.

A **type** describes the level of decision the requirement or product supports.

You can collect **technical evidence** for a **tactical** requirement.

**Speaker Notes:**  
Connect directly to 2.1.2 so learners do not treat the two frameworks as competing labels.

---

### Slide 8 – Knowledge Check
**Title:** Knowledge Check

1. A 40-page report of domains, hashes, and malware details is automatically strategic. True or false? Why?  
2. “What should IR do now with WS-JLEE and the update domain?” Which type, and why?  
3. How does a technical product differ from a tactical product when both use the same A12 observables?

**Speaker Notes:**  
Use the instructor answer key. Listen for the decision need in the learner's explanation.

---

### Slide 9 – Summary
**Title:** Classify by the decision the answer supports

**Strategic** — risk and posture.  
**Operational** — manage the ongoing activity.  
**Tactical** — near-term defensive action.  
**Technical** — concrete artifacts and characteristics.

When the boundary is unclear, ask: **What does the recipient need to decide?**


**Speaker Notes:**  
Transition to requirements: the next lesson teaches how to write the question that defines that decision need.

**Next:** [2.1.4 – Intelligence Requirements](../04-intelligence-requirements/student-guide.md).
