# Module 2.1.4 – Intelligence Requirements

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.4 B / C / C ; 2.1.4.1 3c / 4c / 4d ; 2.1.4.2 3c / 4c / 4d ; 2.1.4.3 3c / 4c / 4c  
- Hunter: 2.1.4 A / B / B ; 2.1.4.1 1a / 2b / 3c ; 2.1.4.2 1a / 2b / 3c ; 2.1.4.3 1a / 2b / 3c  
- SOC: 2.1.4 A / A / B ; 2.1.4.1 1a / 1a / 1a ; 2.1.4.2 1a / 1a / 1a ; 2.1.4.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain why intelligence requirements exist and distinguish a **Priority Intelligence Requirement (PIR)** from other requirements.
2. Refine a stakeholder question into a clear intelligence requirement and explain how that requirement directs collection and analysis.

**Mapped Proficiency Items:**
- K: 2.1.4 – Intelligence requirements and Priority Intelligence Requirements (PIRs)
- T: 2.1.4.1 – Develop or refine intelligence requirements
- T: 2.1.4.2 – Translate stakeholder questions into clear intelligence requirements
- T: 2.1.4.3 – Explain how a given requirement drives analytic work

## 1. Key Concepts

An intelligence requirement gives the work a **purpose**. It tells the analyst what question needs to be answered so collection and analysis can be focused on the evidence that matters.

Without a clear requirement, analysts can easily collect everything that looks interesting, follow every possible pivot, and still have no reliable way to know when the original need has been answered.

A useful requirement therefore connects three things:

1. **The question** — what needs to be known.
2. **The decision or need** — why the answer matters to the stakeholder.
3. **The scope** — what subject, environment, and time window the work should cover.

A requirement should be specific enough to guide work while leaving room for the analyst to determine what evidence is needed. It normally should not dictate a particular tool or source unless the source itself is part of the requirement.

### Priority is not the same as duration

A **Priority Intelligence Requirement (PIR)** is an intelligence requirement that leadership or the program has identified as especially important. The word *priority* describes its relative importance.

Other labels describe different characteristics of a requirement:

- A **standing requirement** remains active over time until it is changed or retired.
- An **ad-hoc requirement** addresses a one-time or event-driven need, often created by an incident or Request for Information (RFI).

These labels are not mutually exclusive. A standing requirement can also be a PIR if leadership prioritizes it. An ad-hoc requirement can also become a priority if the situation warrants it.

The key point is that **not every requirement is a PIR**. Use the organization's published priorities rather than inventing PIR numbers or labels.

### Refining a stakeholder question

Stakeholders often begin with a question that makes sense conversationally but is too broad to guide analysis.

For example:

> “Are we seeing them?”

That question leaves several things unclear. Who is “them”? What activity counts as “seeing” them? In what environment and during what period?

In the A12 context, a more useful requirement might be:

> **What role did the update domain play in the activity on WS-JLEE during A12?**

This version gives the analyst an object to investigate, a defined case, and a relationship to establish. It is still broad enough for the analyst to determine what evidence is needed.

A more narrowly scoped follow-on requirement could ask:

> **Was the update domain used to deliver `/update.exe` to WS-JLEE during the A12 time window?**

The right level of specificity depends on the stakeholder's actual need. The analyst's job is to make the question clear enough that the team knows what evidence would answer it.

### How requirements drive collection and analysis

Once the question is clear, it shapes the work.

For the A12 requirement, the analyst might need:

- network records showing WS-JLEE's requests to the domain;
- DNS records connecting the domain to an address;
- host evidence showing whether the requested file appeared; and
- incident context needed to interpret those observations.

The requirement also helps control scope. A sibling domain discovered during enrichment may be interesting, but if it does not help answer the current question, it can be documented for later rather than allowed to derail the analysis.

That does not mean analysts ignore unexpected evidence. It means they can distinguish **evidence needed for the current requirement** from **new information that may justify a separate or refined requirement**.

### Requirements and intelligence types

Module 2.1.3 introduced strategic, operational, tactical, and technical intelligence. A requirement can be classified the same way because the requirement defines the type of answer the stakeholder needs.

For example, “What should IR do now with WS-JLEE?” is a tactical requirement. “Does this threat materially change organizational risk?” is strategic. The requirement sets the direction before collection begins.

### Connect the requirement to local priorities

Before starting real collection, consult the current local priorities described in [2.8.1](../../08-site-specific/01-local-priorities/student-guide.md). Identify the mission, assets, and decision that make the question relevant. This early relevance check bounds the work; the fuller applicability and impact assessment follows the evidence in 2.6.

## 2. Knowledge Check

1. Every intelligence requirement is a PIR. True or false? Explain what makes a PIR different.
2. A stakeholder asks, “Are we seeing them?” Identify two things you would clarify before treating that as an intelligence requirement.
3. Using A12, write a clearer requirement for the update domain and name one piece of evidence that would help answer it and one interesting pivot that could reasonably be deferred if it does not help answer the question.

## 3. Summary

An intelligence requirement defines the question the work exists to answer. A clear requirement identifies the information need, connects it to a decision, and provides enough scope to guide collection and analysis.

A PIR is a requirement that has been **prioritized** by leadership or the program. Standing and ad-hoc describe how a requirement persists or arises; they do not automatically determine priority.

Good requirements focus the work without prescribing every analytical step. They help the analyst decide what evidence matters now, what can wait, and when the answer is sufficient for the stakeholder's need.


## 4. Related Modules

- 2.1.3 – Intelligence types (previous)
- 2.1.6 – Ensuring intelligence is actionable
- 2.1.9 – Collection sources and methods
- 2.8.1 – Local intelligence requirements and PIRs

**Next:** [2.1.5 – RFI Intake and Prioritization](../05-rfi-intake/student-guide.md).
