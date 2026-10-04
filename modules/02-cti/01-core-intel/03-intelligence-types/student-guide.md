# Module 2.1.3 – Intelligence Types

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.3 B / C / C ; 2.1.3.1 3c / 4c / 4c  
- Hunter: 2.1.3 A / B / B ; 2.1.3.1 1a / 2b / 3c  
- SOC: 2.1.3 A / A / A ; 2.1.3.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the four intelligence types used in this course: **strategic**, **operational**, **tactical**, and **technical**.
2. Classify an intelligence product or requirement by type and explain the decision need that makes that classification appropriate.

**Mapped Proficiency Items:**
- K: 2.1.3 – Intelligence types (strategic, operational, tactical, technical)
- T: 2.1.3.1 – Classify an intelligence product or requirement by type

## 1. Key Concepts

Intelligence types help describe the **kind of decision or understanding** a product is intended to support. Two products can discuss the same threat and still be different types because their readers are trying to answer different questions.

The useful starting point is therefore not the length of the report or the amount of technical detail. Ask: **What question is this product trying to answer, and what decision will the recipient make with the answer?**

This course uses four types:

| Type | Primary decision need | Typical focus |
|---|---|---|
| **Strategic** | How should leadership understand or change organizational risk, priorities, or posture? | Longer-term implications, trends, business or mission risk, resource and policy decisions |
| **Operational** | How should defenders understand and manage an operation, campaign, incident set, or hunt over time? | Campaign activity, sequencing, targeting patterns, operational priorities, coordination across days or weeks |
| **Tactical** | What should a defender do about the activity in front of them? | Immediate defensive decisions, response actions, techniques, and near-term handling |
| **Technical** | What concrete artifacts or technical characteristics can analysts detect, validate, or pivot on? | Domains, IP addresses, hashes, paths, protocol details, malware characteristics, and other observables |

These categories are a teaching model. In practice, organizations and vendors sometimes use the labels differently. When you work in a specific environment, use its definitions consistently. The important skill is recognizing the **decision level** the product is serving.

### Type follows the question

A requirement and the product that answers it usually share the same primary type because the requirement defines the decision need.

Consider several possible questions related to A12:

- **Technical:** What domains, IP addresses, file names, and request paths are associated with the activity?
- **Tactical:** What should SOC or IR do now with WS-JLEE and the update domain?
- **Operational:** How is the A12 activity unfolding, and what should defenders prioritize across the investigation over the next several days?
- **Strategic:** Does the broader threat represented by this activity materially change organizational risk, defensive priorities, or investment decisions?

The same incident can contribute evidence to all four questions, but the questions require different analysis. A single A12 observation may be enough to support a technical or tactical answer while being only one input to a broader strategic assessment.

### Technical and tactical are related, but not interchangeable

This is a common source of confusion. A technical observable tells you **what can be identified or detected**. A tactical product tells a defender **how to respond to or handle activity**.

For example:

- `203.0.113.88` and `GET /update.exe` are technical observations.
- “Investigate connections from WS-JLEE to the update domain and preserve the associated file and process evidence” is tactical guidance.

The technical evidence may enable the tactical decision, but the observable itself is not the response action.

### Operational and strategic differ in the decision horizon

Operational intelligence helps a team manage an ongoing body of activity: a campaign, incident set, hunt, or adversary operation. It is concerned with how the activity is unfolding and what defenders should prioritize across that effort.

Strategic intelligence steps farther back. It helps leadership understand implications for risk, posture, resources, or policy. A lengthy report is not automatically strategic, and a short assessment can still be strategic if it answers a leadership-level risk question.

Time horizon can be a useful clue, but it is not the definition. The **decision being supported** is the stronger indicator.

### Relationship to the lifecycle

Module 2.1.2 described the stages of intelligence work. A lifecycle **stage** tells you what kind of work is happening; an intelligence **type** tells you what kind of decision the resulting requirement or product supports.

You can collect technical observables while working on a tactical or operational requirement. Likewise, a strategic product still passes through planning, collection, processing, analysis, dissemination, and feedback.

## 2. Knowledge Check

1. A 40-page report containing mostly domains, hashes, and malware configuration details is automatically strategic because it is long. True or false? Explain.
2. A requirement asks, “What should IR do now with WS-JLEE and the update domain?” Which intelligence type best fits the requirement, and why?
3. Explain the difference between a **technical** product that lists the A12 observables and a **tactical** product that uses those observables to guide a responder.

## 3. Summary

Intelligence type is determined primarily by the **question and decision need**, not by report length or technical complexity. Strategic intelligence supports leadership-level risk and posture decisions; operational intelligence supports management of campaigns and ongoing activity; tactical intelligence supports near-term defensive action; and technical intelligence describes concrete artifacts and characteristics analysts can detect or pivot on.

When the boundary is unclear, ask what the recipient needs to decide. That usually reveals the type more reliably than the format of the product.


## 4. Related Modules

- 2.1.2 – Intelligence lifecycle (previous)
- 2.1.4 – Intelligence requirements
- 2.1.7 – Tailoring output to the audience
- 2.7 – Finished intelligence products

**Next:** [2.1.4 – Intelligence Requirements](../04-intelligence-requirements/student-guide.md).
