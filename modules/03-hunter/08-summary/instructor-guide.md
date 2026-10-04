# Instructor Guide – Module 3.8 – Threat Hunting Section Summary

**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led synthesis and discussion  
**Module Type:** Section summary — no proficiency mapping

## Purpose

Close the 3.x Threat Hunting block by reconnecting the lessons into the hunt loop introduced in 3.0:

**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

This is not a compressed reteaching of every 3.x module.

The learner should demonstrate that the major hunt-development, evidence, limitation, and handoff concepts now fit together.

## Learning Outcomes

By the end of the summary, learners should be able to:

1. Explain how 3.1–3.7 combine into one hunt workflow.
2. Walk A12 from initiating signal through findings and handoff.
3. Preserve the most important evidence and scope boundaries.
4. Identify which 3.x unit to revisit when a hunt-development skill remains weak.
5. Explain how hunt findings become inputs to Detection Engineering and other downstream functions.

## Suggested Timing

| Part | Time |
|---|---:|
| Return to the 3.0 hunt loop | 2 min |
| 3.x at a glance | 3 min |
| A12 end-to-end hunt | 7 min |
| Important distinctions | 3 min |
| Readiness / DE transition | 3–4 min |

## Teaching Strategy

### Do not reteach every tool

Avoid turning this into:
- another VirusTotal/ANY.RUN lesson;
- another ATT&CK lecture;
- another persistence technique catalog;
- another local-policy lesson.

Instead, require learners to explain **how each type of information changes the hunt**.

### Use A12 as the spine

Walk one hunt from start to finish.

Ask:

1. What caused this hunt to begin?
2. What is the bounded question?
3. What hypothesis can evidence test?
4. What population, window, and telemetry are required?
5. Which CTI/external inputs sharpen the search?
6. What is the local procedure being searched?
7. What does ATT&CK add?
8. How do you refine candidates?
9. What did the hunt find?
10. What could it not see?
11. Which findings go to which owners?

The objective is one coherent hunt story.

## Important Distinctions to Reinforce

### Starting signal vs hunt design

A hunt may be reactive, intel-driven, anomaly-based, or begin from a hypothesis.

The label does not substitute for the actual hunt question and scope.

### Hypothesis vs topic

Require a proposition that can be supported or not supported by evidence.

### External intelligence vs local evidence

Ask:

> ANY.RUN observed a registry artifact. What does that prove about our enterprise?

Expected answer:

> It provides a hunt lead; local occurrence still requires internal evidence.

### Technique vs procedure

Ask:

> Is an ATT&CK ID the hunt pattern?

Expected answer:

> No. ATT&CK names the behavior category; the hunt needs the actual observable procedure/data relationship.

### Detection gap vs visibility gap

Use the A12 result:
- registry event visible, no analytic → detection gap;
- registry event not collected → visibility gap.

### False negative

Ask:

> No alert fired for a behavior that no rule was designed to detect. False negative?

Expected answer:

> No. That is a coverage/detection gap unless a control was expected to detect it.

### Privilege outcome vs method

Ask learners what SYSTEM execution proves and what it does not.

Expected:
- can support high-privilege execution/outcome with proper context;
- does not identify the escalation method without method-specific evidence.

### Negative findings

Require the phrase or concept:

> Not found within tested scope and available visibility.

## Integrated Review – Expected Shape

Use the provided A12 hunt card.

A strong answer should include:

**Question**
> Are additional managed Windows workstations showing A12-style persistence?

**Hypothesis**
> If present, relevant Run-key modification telemetry should show the payload/path relationship or closely related variants.

**Scope**
> Named population, 14-day window, registry + process/file telemetry.

**Findings**
> Two exact matches and three related candidates.

**Limitations**
> Seven hosts lack required registry visibility.

**Gaps**
> No analytic coverage = detection gap; missing registry telemetry = visibility gap.

**Handoff**
> Exact/credible compromise candidates to SOC/IR; coverage gap to DE; telemetry gap to platform owner; new intel lead to CTI; related pattern may become follow-on hunt.

Do not require identical wording. Require the reasoning structure.

## Hunt Readiness Diagnostic

If a learner cannot:
- explain why hunt → revisit **3.1**;
- identify start signal or develop hypothesis/scope → revisit **3.2**;
- use external tools as leads rather than proof → revisit **3.3**;
- extract huntable CTI/STIX input → revisit **3.4**;
- separate ATT&CK mapping from hunt design → revisit **3.5**;
- preserve technique/procedure evidence boundaries → revisit **3.6**;
- explain documentation/handoff requirements → revisit **3.7**.

## Transition to Detection Engineering

Use:

> Hunting proved that this behavior is searchable and defensively useful. Should it become maintained automatic coverage?

Then:

> Detection Engineering evaluates existing coverage, telemetry requirements, validation, deployment, maintenance, and retirement.

This makes the 3.x → 4.x transition operational rather than merely sequential.

## Instructor Closing

Finish with:

> **A hunt result is only as broad as the scope and visibility that produced it.**

That principle should carry into detection validation and coverage discussions in 4.x.
