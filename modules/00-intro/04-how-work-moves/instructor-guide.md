# Instructor Guide – Module 0.4 – How work can move

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- Hunter: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- CTI: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- DE: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

An investigation can create several kinds of follow-on work. Some work addresses the incident already in progress, while other work improves understanding or future detection. Following one possible workflow helps you identify who receives a request and what they are expected to produce.

Teach this as a shared introductory lesson using the supplied examples and discussion. Match the depth to the proficiency levels above. The focus is the mapped knowledge and task; operational procedures are developed in the later role tracks.

## Learning Objectives

1. Describe one possible workflow after an alert is triaged.
2. Explain how intelligence findings can support blocking, hunting, and detection work.
3. Given a step in the workflow, identify the receiving role and the product it owns.

**Mapped Proficiency Items:**
- K: 0.4 – How work can move
- T: 0.4.1 – Given a step in the flow, name the next hand-off and whose product it is

## Preparation

Read the [student guide](student-guide.md) and use [slides.md](slides.md) to support the explanation. Review the answer key before teaching so the discussion and feedback reinforce the same concepts. This lesson uses discussion and worked examples; no lab is required.

## Suggested Timing

| Section | Time | Teaching purpose |
|---|---|---|
| Opening and purpose | 2 min | Connect this lesson to the previous topic. |
| Explanation and worked examples | 14 min | Use the three teaching sections below. |
| Knowledge check and feedback | 4 min | Ask for reasoning as well as an answer. |
| Summary and transition | 2 min | Consolidate the lesson and introduce the next topic. |
| **Total** | **22 min** | |

## Detailed Teaching Notes

### 1. From an alert to response and a question

Walk learners from evidence to the reason for each handoff. The example is an escalated case; it does not imply every alert requires IR or leadership notification. Emphasize that responding to harm and answering an intelligence question can happen at the same time.

**Student-facing emphasis:** Triage establishes what attention the alert requires. In this example, IR receives the incident, leadership is notified, and CTI receives an RFI.

### 2. How the intelligence work branches

Explain the branches by the outcome expected. A domain can appear in more than one product. The reason for a blocking handoff is an evaluated control need, not merely discovering another name. Keep the same-package relationship between Hunt and DE explicit.

**Student-facing emphasis:** CTI develops an answer and supporting context. Findings can support blocking review, a hunt, and detection work. The same intelligence package can serve Hunt and DE.

### 3. Naming the next handoff

Ask learners to explain what the recipient still has to do. Receiving a package does not mean the hunt or rule is already complete. Tool names illustrate possible downstream implementations and are not requirements to author anything in this lesson.

**Student-facing emphasis:** Name the recipient, the requested outcome, and the product they own. Hunt returns findings and gaps. DE assesses coverage and develops or tunes detections.

## Knowledge Check — Answer Key

### 1. In the escalated course example, what can the analyst do after triage while CTI works on an RFI?

**Expected answer:** Hand the incident to IR and notify leadership according to the applicable procedure. Those activities can proceed while CTI develops an answer.

**Feedback and assessment:** Check that learners understand parallel work and the example’s escalation context.

### 2. CTI has evidence supporting consideration of a domain block. Who receives that work, and what product does that function own?

**Expected answer:** The function responsible for blocking, described here as firewall / IA, evaluates and implements an authorized control change.

**Feedback and assessment:** Accept the local function’s equivalent name. Discovery of a candidate alone is not sufficient support for a block.

### 3. The same intelligence package goes to Hunt and DE. What result should each produce?

**Expected answer:** Hunt searches for relevant activity and returns findings and visibility gaps. DE assesses existing coverage and decides whether to develop or tune detections.

**Feedback and assessment:** The answer should distinguish the search result from the detection outcome and allow existing coverage to satisfy the need.

## Closing and Transition

A single alert can lead to response, notification, intelligence analysis, hunting, and detection work. Identify each handoff by its purpose and the product the receiving role owns. The example explains how the responsibilities connect while leaving local routing and approval procedures to the organization.

Previous: [0.3 – Jobs in one sentence](../03-jobs-in-one-sentence/student-guide.md)

Next: [0.5 – Where the jobs lightly overlap](../05-where-jobs-overlap/student-guide.md)

## References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.
