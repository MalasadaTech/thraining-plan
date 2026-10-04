# Module 0.9 – Shared Foundations Section Summary

**Target Audience:** SOC Analyst, CTI Analyst, Threat Hunter, Detection Engineer  
**Estimated Time:** 15–20 minutes  
**Module Type:** Section summary — no proficiency mapping

## Purpose

The 0.x block gave every learner the same foundation before the role-specific tracks begin.

You learned:

- how the course is organized;
- what a SOC is;
- what the major defensive roles produce;
- how work can move between those roles;
- where responsibilities overlap;
- how ATT&CK, the Diamond Model, and the Cyber Kill Chain help organize activity;
- what external research tools can and cannot tell you;
- how the local environment and signal flow affect what evidence is available.

This summary reconnects those topics before you begin 1.x.

A simple way to remember the 0.x block is:

**Course map → Roles → Handoffs → Frameworks → Tools → Environment**

These foundations support every later track.

## 1. What You Can Now Do

You should now be able to:

- explain how the course progresses from shared foundations into SOC, CTI, hunting, and Detection Engineering;
- describe the purpose of a SOC without reducing it to one tool or queue;
- state the primary product expected from each defensive role;
- identify a reasonable next handoff when one role reaches the limit of its current task;
- explain why two roles can examine the same evidence while producing different outputs;
- use ATT&CK, the Diamond Model, and the Cyber Kill Chain for different analytic purposes;
- treat external platform results as evidence or leads rather than automatic truth;
- describe major environment paths and recognize that traffic path, collection point, and actual visibility are different concepts.

The goal is shared language.

Later tracks will add depth.

## 2. The 0.x Block at a Glance

| Unit | Core idea retained |
|---|---|
| **0.1 – Course Layout** | Understand the teaching sequence and why shared foundations come first. |
| **0.2 – What a SOC Is** | Understand the SOC as a defensive function that receives, investigates, coordinates, and communicates security work. |
| **0.3 – Jobs in One Sentence** | Recognize the primary purpose and product of SOC, CTI, hunting, and Detection Engineering roles. |
| **0.4 – How Work Can Move** | Follow a piece of defensive work from one role to another when the question changes. |
| **0.5 – Where Jobs Overlap** | Understand that several roles may inspect the same evidence while producing different products. |
| **0.6 – Frameworks** | Use ATT&CK, the Diamond Model, and the Cyber Kill Chain as different ways to organize what you know. |
| **0.7 – External Tools** | Understand the broad capabilities and limits of public/external research platforms. |
| **0.8 – Environment / Signal Flow** | Relate hosts, users, network paths, critical assets, access paths, and sensors to the evidence you can actually observe. |

## 3. One A12 Story Across the Shared Foundations

The A12 scenario can show why the 0.x material matters before any role-specific lesson begins.

Suppose the SOC receives an alert involving `WS-JLEE`.

Available evidence includes:
- encoded PowerShell;
- external communication;
- a request for `/update.exe`;
- a persistence-related registry change.

At this point, several defensive roles may become involved.

### SOC

The SOC asks:

> What happened on this system, how serious is it, and what needs to happen now?

Its product may be:
- an investigated alert;
- an incident record;
- an escalation;
- an RFI to another team.

### CTI

CTI may ask:

> What is known about the infrastructure, behavior, malware, campaign, or threat activity connected to this case?

Its product is an assessed intelligence answer or package—not simply a list of search results.

### Threat Hunting

Hunting may ask:

> Does this same or related behavior exist elsewhere in the environment?

Its product is a bounded hunt result, including findings, limitations, and follow-on gaps.

### Detection Engineering

Detection Engineering may ask:

> Should this behavior become maintained automatic coverage, and if so, how?

Its product is maintained detection capability rather than only a query.

The same A12 evidence can appear in all four workflows.

The **question and product** are what change.

## 4. Follow the Question When Work Moves

A handoff should happen because the next question belongs to another function—not merely because another team exists.

For example:

> SOC confirms suspicious activity and asks whether the external domain is known.

That becomes an intelligence question.

> CTI identifies a distinctive procedure and asks whether it appears elsewhere internally.

That can become a hunt lead.

> Hunting finds the procedure on additional hosts and discovers that no analytic covers it.

That can become Detection Engineering work.

> Detection Engineering deploys a validated analytic.

Future activity may generate a SOC alert.

The workflow can become a loop.

The course teaches the roles separately so you can understand their responsibilities, but real defensive work often moves back and forth.

## 5. Same Evidence, Different Product

This is one of the most important ideas from 0.x.

A domain such as `example-update.test` might appear in:

- a SOC case;
- a CTI infrastructure assessment;
- a hunt query;
- a detection rule.

That does not make the four products interchangeable.

Similarly, one analyst may wear two roles.

The analyst still needs to know which product they are producing at that moment.

A useful question is:

> **What decision or downstream action is this product supposed to support?**

That often tells you which role's work you are doing.

## 6. Keep the Frameworks Distinct

The frameworks introduced in 0.6 help organize different kinds of reasoning.

### MITRE ATT&CK

ATT&CK helps describe **adversary behavior**.

Ask:

> What behavior or technique does the evidence support?

### Diamond Model

The Diamond Model helps organize relationships among:

- adversary;
- capability;
- infrastructure;
- victim.

Ask:

> Which vertices are supported, and what relationships can we investigate?

An incomplete diamond is still useful. Missing information should remain missing until evidence supports it.

### Cyber Kill Chain

The Cyber Kill Chain helps reason about **progression through an intrusion**.

Ask:

> Which stage does the available evidence support?

Do not force every stage to be present.

### One event can support more than one framework view

The frameworks are not competing answers.

They organize the same evidence for different analytic purposes.

## 7. External Tools Provide Evidence, Not Authority

External research platforms can help with:

- file relationships;
- sandbox behavior;
- passive DNS;
- infrastructure context;
- URL or web observations;
- reputation and prior reporting.

But a platform result should still be interpreted.

Examples:

> A sandbox observed a process behavior.

This means the behavior was observed in that sandbox execution.

It does not automatically mean every copy behaves the same way or that the behavior occurred locally.

> Passive DNS shows a historical domain-to-IP relationship.

This provides historical infrastructure context.

It does not by itself prove common ownership or malicious operation.

> A vendor labels infrastructure as malicious.

That is a source claim to evaluate, not a substitute for analysis.

Later CTI and hunt lessons will develop these distinctions in more depth.

## 8. Environment Path ≠ Visibility

Module 0.8 introduced the environment because evidence depends on where sensors and systems actually sit.

Keep these concepts separate:

**Traffic path**
> Where activity travels.

**Collection point**
> Where a sensor or log source can observe part of that activity.

**Visibility**
> What evidence is actually collected, retained, parsed, and available to analysts.

A connection may pass through a network segment without a sensor recording the detail you need.

A sensor may exist but not capture the relevant field.

A host may be important but outside a particular telemetry population.

This distinction becomes essential in SOC investigation, hunting, and Detection Engineering.

## 9. Distinctions Worth Keeping

### Role ≠ tool

A SOC is not a SIEM.

CTI is not a TIP.

Hunting is not a query language.

Detection Engineering is not Sigma.

Tools support the function.

### Shared evidence ≠ shared responsibility

Two roles can inspect the same log without owning the same decision or product.

### Handoff ≠ abandonment

Passing a question to the correct function does not mean the original team stops caring about the case.

It means the question has moved to the role best positioned to answer it.

### Framework ≠ evidence

ATT&CK, Diamond, and Kill Chain organize evidence.

They do not create evidence that is not present.

### External result ≠ local occurrence

Research platforms can generate leads.

Internal occurrence still requires internal evidence.

### Network path ≠ sensor visibility

Knowing where traffic travels is not the same as knowing what your tools recorded.

## 10. Integrated Review Exercise

Use this A12 starting card:

> **Host:** `WS-JLEE`  
> **Observed:** encoded PowerShell, external communication, `/update.exe` request, suspicious persistence-related registry activity  
> **Known:** the initial alert does not answer every downstream question

For each item below, state the most appropriate role or concept.

### Immediate host/case investigation
Who owns the first operational investigation?

### External infrastructure question
Which function should assess what is known about the domain/IP and related threat context?

### Enterprise-wide search
Which function should search for similar activity elsewhere?

### Durable analytic coverage
Which function should evaluate whether the behavior becomes maintained detection?

### Behavior framework
Which framework is best suited to naming the adversary behavior?

### Relationship framework
Which framework helps organize adversary, capability, infrastructure, and victim relationships?

### Intrusion progression
Which framework helps reason about stages of an intrusion?

### External platform result
What should you call it before internal evidence confirms local occurrence?

### Missing sensor coverage
Why can the existence of a network path not prove you had visibility into the activity?

A strong answer should explain **why**, not only name the role or framework.

## 11. Shared-Foundations Readiness Checklist

Before beginning 1.x, you should be comfortable saying:

- [ ] I understand the course sequence and the purpose of each major role track.
- [ ] I can explain what a SOC does at a high level.
- [ ] I can distinguish the primary products of SOC, CTI, hunting, and Detection Engineering.
- [ ] I can identify when a question should become a handoff.
- [ ] I understand that the same evidence can support different role-specific products.
- [ ] I can explain the different purposes of ATT&CK, Diamond, and Kill Chain.
- [ ] I can preserve uncertainty when a framework element is unsupported.
- [ ] I treat external-tool results as evidence or leads that require interpretation.
- [ ] I can distinguish network/data flow from actual sensor visibility.
- [ ] I understand that later lessons will deepen these concepts rather than replace them.

If one of these is weak, revisit the corresponding 0.x module.

## 12. Bridge Into 1.x SOC

The shared foundation is now complete.

The course next narrows from:

> **How does defensive work fit together?**

to:

> **What does the evidence actually show?**

The SOC track begins with the observations closest to daily alert investigation:

- endpoint activity;
- network activity;
- detection logic;
- alert investigation;
- reporting and handoff.

The shared role, framework, tool, and environment concepts from 0.x remain in the background throughout that work.

## Summary

The 0.x block created the common language used by every later role:

**Course map → Roles → Handoffs → Frameworks → Tools → Environment**

The most important idea to carry forward is:

> **Follow the evidence, know which question you are answering, and know which product the next defender needs.**

**Next:** **1.0 – SOC Analyst Fundamentals**.
