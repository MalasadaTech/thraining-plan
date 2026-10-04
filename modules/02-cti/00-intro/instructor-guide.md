# Instructor Guide – Module 2.0 – Cyber Threat Intelligence: How the 2.x Block Fits Together

**Estimated Time:** 10–15 minutes  
**Delivery Method:** Instructor-led orientation and discussion  
**Module Type:** Orientation — no proficiency mapping

## Purpose

Give learners a mental model for the reorganized 2.x CTI block before they enter detailed intelligence tradecraft.

Keep this sequence visible:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

The learner should leave understanding that CTI is not a collection of tools. It is an evidence-based process for answering a requirement.

## Learning Objectives

By the end of the introduction, learners should be able to:

1. Explain what each 2.x unit contributes to the intelligence workflow.
2. Follow an A12 RFI from intake through response.
3. Explain why platform observations and enrichment pivots require analysis before becoming intelligence judgments.

## Suggested Timing

| Part | Time |
|---|---:|
| Start with the requirement | 2 min |
| Walk through 2.1–2.8 | 4 min |
| Explain platform two-pass model | 2 min |
| A12 CTI flow | 4–5 min |
| Orientation check / transition | 2 min |

## Core Teaching Model

Display:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

Then map:

- **2.1 Foundations** → define the question and customer
- **2.2 Tradecraft** → reason about incomplete evidence
- **2.3 Frameworks** → organize evidence
- **2.4 Platforms** → retrieve question-relevant evidence
- **2.5 Enrichment** → discover/test technical relationships
- **2.6 Assessment** → determine local significance
- **2.7 Production** → answer and deliver
- **2.8 Local Application** → follow the actual shop process

## Teaching Notes

### Start with an RFI, not a tool

Use the A12 question:

> What is known about the update domain, and does available evidence support payload delivery?

Ask learners what they would need to know before deciding which platform to open.

The expected answer should include the requirement, existing evidence, and remaining question.

### Explain the two-pass platform design

2.4 teaches:
- source/platform selection;
- retrieval;
- platform-specific evidence boundaries.

2.5 teaches:
- how to use retrieved data in file, registration, DNS, infrastructure, and correlation methods.

Emphasize:

> Platform capability and analytic method are related, but they are not the same thing.

### Candidate relationship is the default early state

A pivot usually produces a lead, not a conclusion.

Require learners to say:
- what was shared;
- when;
- which source observed it;
- what alternative explanation remains.

### Keep assessment terms separate

Preview:
- applicability;
- visibility;
- relevance;
- impact.

These become explicit in 2.6.

### Production closes the original question

The track intentionally splits:
- **RFI intake** in 2.1.5;
- **RFI response/closure** in 2.7.4.

Use the same A12 requirement at both ends.

## Orientation Check – Expected Answers

1. Platform selection comes first so lookups are driven by an unresolved question rather than tool availability.
2. A platform result is a sourced observation/input; finished intelligence is the assessed answer supported by those inputs.
3. Record a candidate relationship and its evidence/limitations, not common control or attribution.
4. A behavior can apply to the environment even when current telemetry cannot observe it.
5. The finished product must return to and answer the original requirement/customer need.

## Transition

End with:

> In 2.0 you learned the intelligence workflow. In 2.1, we begin by separating data, information, and intelligence—and by defining the requirement that makes collection purposeful.

**Next:** **2.1.1 – Difference Between Data, Information, and Intelligence**.
