# Instructor Guide – Module 0.10 – Shared Foundations Section Summary

**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led synthesis and discussion  
**Module Type:** Section summary — no proficiency mapping

## Purpose

Close the shared 0.x block before learners enter role-specific instruction.

This summary should reconnect:

**Course map → Roles → Handoffs → Frameworks → Tools → Environment → Initial Access**

It is not a second pass through every introductory lesson.

The objective is to verify that learners understand the common mental model that the rest of the course assumes.

## Learning Outcomes

By the end of the summary, learners should be able to:

1. Explain how the four defensive roles relate without collapsing them into one job.
2. Follow a reasonable cross-role handoff using the A12 scenario.
3. Explain the different purposes of ATT&CK, Diamond, and Kill Chain.
4. Treat external-tool observations and environmental visibility with appropriate evidence boundaries.
5. Explain why an initial-access path may remain unresolved and what evidence would test common hypotheses.
6. Explain how the 0.x foundations prepare them for 1.x SOC work.

## Suggested Timing

| Part | Time |
|---|---:|
| Revisit the shared-foundation map | 2 min |
| Roles and handoffs | 4 min |
| Framework distinctions | 3 min |
| Tools and environment | 3 min |
| A12 integrated review / transition | 4–5 min |

## Teaching Strategy

### Do not reteach the full introductory block

Avoid:
- repeating every course-navigation detail;
- redefining every role from scratch;
- teaching framework mechanics in depth;
- reviewing every external tool feature.

Instead, ask learners to explain how the pieces relate.

### Use A12 to connect the roles

Start with the spoiler-light A12 state:

> Suspicious activity involving `WS-JLEE` will enter the SOC track. A12's initial-access mechanism is unresolved, and the detailed process, network, and registry observations are intentionally introduced later in 1.x.

Then ask:

- What does SOC need to determine first?
- If later evidence raises an external-threat-context question, which role should answer it?
- If CTI later develops a supported behavior or infrastructure lead, what might move to hunting?
- If a later hunt or intelligence package identifies reusable behavior, what question belongs to DE?
- How could a future detection output return to SOC?

Do not reveal the later A12 evidence in this summary. If you want to illustrate a completed SOC → CTI → Hunt → DE → SOC loop, use a **separate classroom example — not A12**.

The point is not one mandatory enterprise workflow.

The point is recognizing **question changes and product changes**.

### Reinforce “same evidence, different product”

Ask learners to use one domain and describe how each role might use it.

Expected pattern:

- SOC → case evidence/context;
- CTI → assessed infrastructure/threat context;
- Hunt → internal search lead;
- DE → candidate detection input.

### Framework comparison

Ask one question per framework.

**ATT&CK**
> What behavior is occurring?

**Diamond**
> What relationships among adversary, capability, infrastructure, and victim can we support?

**Kill Chain**
> Where in intrusion progression does the evidence fit?

Require learners to leave unsupported pieces unresolved.

### External tools

Ask:

> VirusTotal, ANY.RUN, Silent Push, or urlscan shows something suspicious. What does that prove internally?

Expected answer:

> It provides evidence/context/a lead. Local occurrence still requires internal evidence.

### Environment / signal flow

Ask:

> Traffic crosses an edge firewall. Does that prove we have the needed packet or log detail?

Expected answer:

> No. Path, collection point, and usable visibility are separate.

## Integrated Review – Expected Shape

A strong learner response should identify:

- SOC for immediate investigation;
- CTI for assessed external/threat context;
- hunting for broader internal search;
- DE for maintained analytic coverage;
- ATT&CK for behavior;
- Diamond for entity/relationship structure;
- Kill Chain for intrusion progression;
- external-platform results as source observations/leads until validated;
- sensor/log availability as the basis for claims about visibility;
- A12 initial access as unresolved because no canonical mail, browser, public-facing exploit, authentication, or trusted-third-party evidence establishes the entry path.

Do not require identical wording.

Require correct reasoning about role, framework, and evidence boundaries.

## Readiness Diagnostic

If a learner cannot:
- explain course sequence → revisit **0.1**;
- explain SOC purpose → revisit **0.2**;
- distinguish role products → revisit **0.3**;
- follow cross-role work movement → revisit **0.4**;
- explain overlapping evidence/products → revisit **0.5**;
- distinguish frameworks → revisit **0.6**;
- explain external-tool limits → revisit **0.7**;
- distinguish environment path from visibility → revisit **0.8**;
- reason about common initial-access paths without inventing evidence → revisit **0.9**.

## Transition to SOC

Use:

> The shared lessons taught how defensive work fits together. The SOC block now begins by asking what the evidence actually shows.

Then move into:

**1.0 – SOC Analyst Fundamentals**

and the 1.x evidence-to-handoff model.

## Instructor Closing

Finish with:

> **Follow the evidence, know which question you are answering, and know which product the next defender needs.**

That principle should remain visible across every role track.
