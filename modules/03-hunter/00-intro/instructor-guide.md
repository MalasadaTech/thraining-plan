# Instructor Guide – Module 3.0 – Threat Hunting: How the 3.x Block Fits Together

**Estimated Time:** 10–15 minutes  
**Delivery Method:** Instructor-led orientation and discussion  
**Module Type:** Orientation — no proficiency mapping

## Purpose

Give learners a mental model for the entire 3.x threat-hunting block before they begin the detailed modules.

Keep this loop visible:

**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

The learner should understand that hunting is not “run a query until something suspicious appears.” It is a bounded analytical process whose conclusions depend on the scope and telemetry tested.

## Learning Objectives

By the end of the introduction, learners should be able to:

1. Explain what each 3.x unit contributes to the hunt process.
2. Follow the hunt loop from initiating question to handoff.
3. Explain why a negative hunt result must be qualified by scope and visibility.

## Suggested Timing

| Part | Time |
|---|---:|
| Why hunting begins | 2 min |
| Walk through 3.1–3.7 | 4 min |
| Hypothetical A12-based hunt loop | 4–5 min |
| Orientation check and transition | 2–3 min |

## Core Teaching Model

Write or display:

**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

Then map the track beneath it:

- **3.1 Purpose** → why hunt
- **3.2 Methodology** → define the test
- **3.3 Online Tools** → enrich leads
- **3.4 CTI for Hunters** → convert intelligence into huntable inputs
- **3.5 Framework Application** → organize behavior with ATT&CK
- **3.6 Attacker Techniques** → perform technique-focused reasoning/searches
- **3.7 Site-Specific** → control, document, complete, and route the hunt

## Teaching Notes

**A12 boundary:** canonical A12 provides the hunt package/lead but not a completed hunt result. Treat any host counts, visibility-gap counts, or coverage findings in the orientation as **hypothetical practice conditions**, not facts to add to the case.

### Begin with the question

Use:

> Are there additional workstations with A12-style persistence?

Contrast it with:

> Hunt persistence.

Ask which one makes scope and evidence easier to define.

The lesson should establish early that hunting is question-driven rather than tool-driven.

### Show how CTI becomes a hunt input

CTI may provide:
- a procedure;
- indicator;
- behavior;
- infrastructure clue;
- STIX object.

The hunter converts that input into a local question and query plan.

Do not imply that an external observation proves a local event.

### Reinforce visibility

This is one of the most important themes in the track.

If the hunt depends on registry telemetry and seven hosts do not collect it, the hunter cannot include those hosts in a strong “not found” conclusion.

Use:

> Not found within tested scope and available visibility.

Avoid:

> The enterprise is clean.

### Distinguish finding types

Use the **hypothetical practice output**:

- two additional affected hosts;
- a detection gap;
- a visibility gap;
- a new CTI lead.

Ask learners whether one team should own all four.

The expected answer is no: the hunt produces knowledge that different defensive functions may need to act on.

### Hunt types are starting signals

Do not front-load the detailed taxonomy, but preview that hunts can begin from:
- intelligence;
- a hypothesis;
- an incident;
- an anomaly.

These can overlap. 3.2.1 teaches the course labels in detail.

### ATT&CK supports the hunt; it does not replace the hypothesis

ATT&CK can help name and organize behavior.

It does not answer:
- which population;
- which time window;
- which telemetry;
- which exclusions;
- what result would support the hypothesis.

That distinction prepares learners for 3.5.

## Orientation Check – Expected Answers

1. A bounded question identifies what is being tested and makes scope/evidence definable; “hunt persistence” is only a topic.
2. A lead or evidence source that can sharpen an internal hypothesis/query—not proof of local occurrence.
3. The behavior was not found on the 18 hosts with adequate visibility; the seven unobservable hosts remain an explicit visibility gap.
4. Different outcomes have different operational owners: compromise response, intelligence development, detection improvement, and telemetry remediation.

## Transition

End with:

> In 3.0 you learned the hunt loop. In 3.1, we begin with the reason hunting exists alongside alerts and incident response.

**Next:** **3.1 – Purpose of Threat Hunting**.
