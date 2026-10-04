# Instructor Guide – Course Summary: Bringing the Defensive Workflow Together

**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led synthesis and discussion  
**Module Type:** Course synthesis — no proficiency mapping

## Purpose

Close the course by reconnecting the role tracks into one defensive feedback loop:

**Observe → Understand → Search → Improve Coverage → Observe Again**

This is not a compressed reteaching of the entire curriculum.

The learner should demonstrate that they understand:

- which question each role is answering;
- how evidence changes as it moves between functions;
- where uncertainty and scope boundaries must be preserved;
- how one team's output becomes another team's input.

## Learning Outcomes

By the end of the course summary, learners should be able to:

1. Explain the central question and product of 0.x through 4.x.
2. Walk A12 across SOC, reorganized CTI, hunting, and Detection Engineering.
3. Preserve important cross-course evidence boundaries.
4. Distinguish visibility, coverage, applicability, relevance, and impact.
5. Explain how defensive findings create a feedback loop rather than a one-way workflow.

## Suggested Timing

| Part | Time |
|---|---:|
| Course-wide model | 2 min |
| A12 across all tracks | 10 min |
| Cross-course distinctions | 5 min |
| Readiness checklist | 3 min |
| Closing discussion | 3–5 min |

## Core Teaching Model

Keep visible:

**SOC → CTI → Threat Hunting → Detection Engineering → SOC**

Then ask what changes at each handoff:

- the question;
- the evidence needed;
- the product;
- the downstream consumer.

## Teaching Notes

### 0.x – Context Before Specialization

Ask learners why role boundaries, frameworks, tools, and environment orientation were taught first.

Expected answer:

> Later technical work only makes sense when analysts know which question they are answering and what visibility they actually have.

### 1.x – SOC

Ask:

> What can the SOC state from the evidence, and what remains unresolved?

Require observation before conclusion.

### 2.x – CTI

Use the reorganized workflow:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

Ask learners to explain:

1. Why the RFI comes before platform selection.
2. Why 2.4 teaches retrieval before 2.5 applies the enrichment methods.
3. Why a pivot normally begins as a candidate relationship.
4. Why applicability, visibility, relevance, and impact remain separate.
5. Why the RFI response must return to the original question.

The key teaching point is:

> CTI is not an enrichment dump. It is an evidence-based answer to a requirement.

### 3.x – Threat Hunting

Ask:

> What must change before CTI becomes a hunt?

Expected:

> The intelligence lead becomes a bounded local question, hypothesis, scope, and telemetry plan.

### 4.x – Detection Engineering

Ask:

> What must change before a hunt finding becomes a production detection?

Expected:

> DE evaluates coverage, telemetry, validation, local deployment requirements, and lifecycle ownership.

## Cross-Course Distinctions to Reinforce

### Observation vs assessment

What happened in the data versus what the analyst concludes.

### Tool output vs intelligence

A platform returns evidence. The analyst produces the judgment.

### Candidate link vs campaign vs attribution

Stronger claims require stronger evidence.

### Applicability vs visibility

The behavior may apply even when telemetry cannot observe it.

### Relevance vs impact

Why the finding matters versus what plausible consequence follows.

### Detection gap vs visibility gap

Existing telemetry without adequate analytic coverage versus missing/insufficient telemetry.

### Negative result vs absence

“No evidence within tested scope” is not “does not exist.”

### Detection match vs maliciousness

The analytic matched; investigation still determines meaning.

## Integrated A12 Discussion

Have learners narrate the entire flow in their own words.

A strong answer should include:

**SOC**
> Establish local observations and create the unresolved intelligence question.

**CTI**
> Define the RFI, apply tradecraft, select question-relevant platforms, enrich/correlate, assess applicability/visibility/relevance/impact, and return an evidence-based answer with gaps.

**Hunt**
> Convert the intelligence into a scoped internal hypothesis and search.

**DE**
> Evaluate whether the resulting behavior should become maintained coverage, validate it, and manage its production lifecycle.

**SOC again**
> Receive better future alerts/visibility from the improved analytic.

## Readiness Diagnostic

Do not use the course checklist as a pass/fail exam unless local training policy requires it.

Use it to identify where the learner should revisit:

- shared foundations;
- SOC evidence and alert work;
- CTI requirement-to-answer tradecraft;
- hunt development;
- detection lifecycle.

## Instructor Closing

Finish with:

> **Follow the evidence. Answer the question in front of you. Preserve what remains uncertain. Give the next defender something they can use.**

The learner should leave seeing the four role tracks as specialized parts of one learning defensive system.
