# Instructor Guide – Module 2.1.4 – Intelligence Requirements

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.4 B / C / C ; 2.1.4.1 3c / 4c / 4d ; 2.1.4.2 3c / 4c / 4d ; 2.1.4.3 3c / 4c / 4c  
- Hunter: 2.1.4 A / B / B ; 2.1.4.1 1a / 2b / 3c ; 2.1.4.2 1a / 2b / 3c ; 2.1.4.3 1a / 2b / 3c  
- SOC: 2.1.4 A / A / B ; 2.1.4.1 1a / 1a / 1a ; 2.1.4.2 1a / 1a / 1a ; 2.1.4.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Teach learners to turn a stakeholder's need into a clear question that directs collection and analysis, while understanding that a PIR is a prioritized requirement rather than a synonym for every intelligence question.

**Context:** Module 2.1.3 classified the kind of answer a stakeholder needs. This lesson moves one step earlier in the work: defining the question clearly enough that analysts know what evidence to pursue and what would count as an answer.

Use the A12 stakeholder question to demonstrate refinement. The emphasis should be on improving the question and explaining how that improvement changes the work, not on memorizing a particular requirement template.

**Important distinction:** Priority and duration are separate characteristics. A standing requirement can also be a PIR; an ad-hoc requirement can also be prioritized. Do not teach PIR, standing, and ad-hoc as mutually exclusive categories.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Explain why intelligence requirements exist and distinguish a **Priority Intelligence Requirement (PIR)** from other requirements.
2. Refine a stakeholder question into a clear intelligence requirement and explain how that requirement directs collection and analysis.

**Mapped Proficiency Items:**
- K: 2.1.4 – Intelligence requirements and Priority Intelligence Requirements (PIRs)
- T: 2.1.4.1 – Develop or refine intelligence requirements
- T: 2.1.4.2 – Translate stakeholder questions into clear intelligence requirements
- T: 2.1.4.3 – Explain how a given requirement drives analytic work

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---|---|
| Introduction | 2 minutes | Explain why requirements prevent unfocused collection. |
| Requirement characteristics | 5 minutes | Question, decision need, scope, and answerability. |
| PIR / standing / ad-hoc | 4 minutes | Separate priority from duration or trigger. |
| A12 refinement exercise | 7 minutes | Translate a vague stakeholder ask into a useful requirement. |
| Knowledge check | 4 minutes | Evaluate clarity and explain how the requirement drives work. |
| Summary | 1 minute | Reinforce question-driven analysis. |
| **Total** | **23 minutes** | Allow minor flexibility for discussion. |

## Detailed Teaching Notes

### 1. Explain why the requirement matters

Open with a familiar failure mode: analysts collect every interesting indicator, pivot, and report but cannot say when they have answered the stakeholder's need. A requirement gives the work a stopping condition and a reason for each collection step.

A useful requirement should tell the team what needs to be known and why it matters. It should provide enough scope to keep the effort coherent without predetermining the answer.

### 2. Teach the components of a useful requirement

Use three elements:

- **Question:** What needs to be known?
- **Decision or need:** What will the stakeholder do with the answer?
- **Scope:** What subject, environment, and time window are relevant?

Avoid presenting these as a mandatory form unless the local organization has one. The teaching goal is clarity and direction.

Explain that a requirement should generally avoid over-specifying the collection method. “Check VirusTotal for X” is an analytical task or collection action, not the requirement itself, unless the stakeholder specifically needs information from that source.

### 3. Clarify PIR, standing, and ad-hoc

A **PIR** is distinguished by priority. Leadership or the program has identified it as especially important relative to other requirements.

A **standing requirement** describes persistence. It remains active over time.

An **ad-hoc requirement** describes how the need arose: one-time or event-driven.

Make the overlap explicit. A standing requirement may be a PIR. An ad-hoc requirement may become a PIR. The course should not imply that these labels form one mutually exclusive list.

### 4. Refine the A12 question

Start with: **“Are we seeing them?”**

Ask learners what is ambiguous. Good answers include the actor or activity being referenced, the environment, the observable behavior, and the time window.

Then use the course example:

**What role did the update domain play in the activity on WS-JLEE during A12?**

Discuss why this version is more useful. It gives the analyst an object, an incident context, and a relationship to establish. Then show how a follow-on question can be narrower if the stakeholder specifically needs to know whether `/update.exe` was delivered.

### 5. Show how the requirement drives work

Ask what evidence could answer the question. Accept multiple defensible sources: DNS, HTTP, EDR or file evidence, incident notes, and process activity.

Then ask what might be interesting but not necessary for the current question. Use the sibling-domain example. Explain that deferring a pivot is not the same as discarding it; it can be preserved as a possible follow-on requirement.

This is an important analytical habit: separate **scope control** from **curiosity suppression**.

## Common Student Challenges

| Misunderstanding | Why it occurs | Teaching response |
|---|---|---|
| Every requirement is a PIR. | PIR is the most memorable requirement term. | Ask who prioritized it and where that priority is documented. |
| Standing, ad-hoc, and PIR are three mutually exclusive types. | They are often listed together in simplified training. | Separate priority from duration/trigger; show that the labels can overlap. |
| A broad conversational question is already sufficient. | It sounds meaningful to the stakeholder. | Ask what object, environment, or time window the analyst would actually collect against. |
| A requirement should name the exact tool to use. | Learners want a concrete first action. | Keep the requirement focused on the information need; source selection comes later. |
| Scope control means ignoring unexpected evidence. | “Stay on requirement” can sound rigid. | Preserve useful pivots and create or refine a requirement when they matter. |

## Knowledge Check – Answer Key

### 1. Every intelligence requirement is a PIR. True or false? Explain what makes a PIR different.

**Expected answer:** False. A PIR is an intelligence requirement that leadership or the program has prioritized.

**Reasoning:** Priority is the distinguishing characteristic. Other requirements can still be valid and important without being PIRs.

### 2. A stakeholder asks, “Are we seeing them?” Identify two things you would clarify before treating that as an intelligence requirement.

**Expected answer:** Any two defensible clarifications such as who or what “them” refers to, what activity counts as seeing them, the environment, the time window, or the stakeholder's decision need.

**Reasoning:** The original question is too ambiguous to direct collection consistently.

### 3. Using A12, write a clearer requirement and name one piece of evidence plus one pivot that could be deferred.

**Expected answer:** Example requirement: “What role did the update domain play in the activity on WS-JLEE during A12?” Evidence could include HTTP/DNS records or host/file evidence. A sibling domain could be deferred if it does not help answer the current question.

**Acceptable response:** Other clearly bounded A12 requirements are acceptable if the learner can explain how the evidence relates to the question.

## Summary and Transition

Close by emphasizing that a requirement is not paperwork added before analysis; it is the mechanism that gives analysis direction. The next lesson, **2.1.5 – RFI Intake and Prioritization**, applies this requirement discipline to an incoming request.
