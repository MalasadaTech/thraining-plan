# Instructor Guide – Module 2.1.3 – Intelligence Types

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.3 B / C / C ; 2.1.3.1 3c / 4c / 4c  
- Hunter: 2.1.3 A / B / B ; 2.1.3.1 1a / 2b / 3c  
- SOC: 2.1.3 A / A / A ; 2.1.3.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Help learners classify intelligence requirements and products as strategic, operational, tactical, or technical by identifying the decision need each one serves.

**Context:** Module 2.1.2 taught the lifecycle—the kinds of work that move a question toward a usable answer. This lesson introduces another dimension: the level of decision the requirement or product is intended to support.

Use questions rather than report formats to teach the distinction. Learners should leave the lesson able to explain why an item is a given type, not merely associate “long” with strategic or “indicator” with tactical.

**Course-model note:** Organizations and vendors sometimes define these labels differently. Teach the four definitions used in this course, while making clear that the transferable skill is identifying the decision level and using the local taxonomy consistently.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Explain the four intelligence types used in this course: **strategic**, **operational**, **tactical**, and **technical**.
2. Classify an intelligence product or requirement by type and explain the decision need that makes that classification appropriate.

**Mapped Proficiency Items:**
- K: 2.1.3 – Intelligence types (strategic, operational, tactical, technical)
- T: 2.1.3.1 – Classify an intelligence product or requirement by type

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---|---|
| Introduction | 2 minutes | Establish that type follows the decision need. |
| Four types | 6 minutes | Explain the primary question each type answers. |
| A12 question comparison | 7 minutes | Show how one incident can support different decision levels. |
| Boundary discussion | 3 minutes | Distinguish technical/tactical and operational/strategic. |
| Knowledge check | 4 minutes | Classify by reasoning rather than keywords. |
| Summary | 1 minute | Reinforce question-first classification. |
| **Total** | **23 minutes** | Allow minor flexibility for discussion. |

## Detailed Teaching Notes

### 1. Start with the decision, not the document

Ask learners what makes a report “strategic.” If they answer length, senior audience, or lack of indicators, use that as the opening teaching point: those may correlate with strategic products, but they do not define them.

A stronger classification question is: **What decision is the recipient trying to make?** The same threat can be described at several levels, and the product type changes as the decision changes.

### 2. Explain the four types

**Strategic** intelligence supports leadership decisions about organizational risk, priorities, posture, resources, or policy. It normally synthesizes broader patterns rather than centering on one observable.

**Operational** intelligence supports management of an ongoing campaign, incident set, hunt, or adversary operation. The recipient needs to understand how activity is unfolding and what to prioritize across the effort.

**Tactical** intelligence supports near-term defensive action. It helps responders decide what to investigate, contain, block, preserve, or otherwise do about activity in front of them.

**Technical** intelligence describes the concrete artifacts and technical characteristics that analysts can detect, validate, correlate, or pivot on.

Emphasize that time horizon is a clue rather than a strict rule. The decision need remains the better classifier.

### 3. Use A12 to compare questions

Present four questions about A12 rather than four disconnected examples.

- Technical: What observables are associated with the activity?
- Tactical: What should IR do now with WS-JLEE and the update domain?
- Operational: How is A12 unfolding, and what should defenders prioritize across the investigation?
- Strategic: Does the broader threat materially change organizational risk or defensive investment?

Point out that the available A12 evidence may be sufficient for some questions and insufficient for others. This keeps learners from assuming that every incident automatically produces a complete strategic product.

### 4. Make the difficult boundaries explicit

**Technical vs tactical:** Technical describes the thing; tactical uses evidence about the thing to support action. An IP address, hash, or request path is technical. A response recommendation based on those observations is tactical.

**Operational vs strategic:** Operational manages the ongoing body of activity. Strategic assesses implications for organizational risk and posture. A long campaign report can still be operational if it is primarily telling defenders how to manage the campaign.

### 5. Connect type back to lifecycle

A lifecycle stage and an intelligence type answer different questions. A team can be in Collection while gathering technical artifacts for a tactical requirement, or in Analysis while producing a strategic assessment. This distinction is useful because learners just completed the lifecycle module and may otherwise treat the two taxonomies as competing labels.

## Common Student Challenges

| Misunderstanding | Why it occurs | Teaching response |
|---|---|---|
| Long documents are strategic. | Strategic products are often broad and polished. | Ask what decision the report supports; length alone cannot answer that. |
| Indicators are tactical. | Some industry usage treats “tactical” as a synonym for IOC-heavy reporting. | In this course, observables are technical; tactical intelligence supports an immediate defensive action. |
| Operational means “anything the SOC does.” | The word operational sounds like daily work. | Anchor operational intelligence to managing a campaign, incident set, or sustained defensive effort. |
| Type and lifecycle stage are the same classification. | Learners have just studied the lifecycle. | Stage describes the work being done; type describes the decision level being supported. |

## Knowledge Check – Answer Key

### 1. A 40-page report containing mostly domains, hashes, and malware configuration details is automatically strategic because it is long. True or false? Explain.

**Expected answer:** False. The content may be technical if its primary purpose is to provide concrete artifacts and technical characteristics. Length does not determine type.

**Reasoning:** Type follows the decision need. A very long technical reference can remain technical.

### 2. A requirement asks, “What should IR do now with WS-JLEE and the update domain?” Which intelligence type best fits the requirement, and why?

**Expected answer:** Tactical. The question is asking for an immediate defensive decision about current activity.

**Acceptable response:** Learners may mention that technical evidence will support the answer. Reinforce that supporting evidence does not change the primary type of the requirement.

### 3. Explain the difference between a technical product that lists the A12 observables and a tactical product that uses those observables to guide a responder.

**Expected answer:** The technical product identifies artifacts or characteristics that can be detected or pivoted on. The tactical product interprets those observations in support of a near-term response decision or action.

**Assessment guidance:** Credit the learner's reasoning more heavily than use of exact wording. The objective is classification by decision need.

## Summary and Transition

Close with the question-first rule: strategic, operational, tactical, and technical describe different decision needs. The next lesson, **2.1.4 – Intelligence requirements**, teaches how to turn a stakeholder's need into a question that can drive collection and analysis.
