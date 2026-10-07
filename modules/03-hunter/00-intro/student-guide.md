# Module 3.0 – Threat Hunting: How the 3.x Block Fits Together

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Time:** 10–15 minutes  
**Module Type:** Orientation — no proficiency mapping

## Learning Objectives

By the end of this introduction, you will be able to:

1. Explain the purpose of the 3.x threat-hunting block and how its seven units fit together.
2. Follow the basic hunt loop from a question to a finding and handoff.
3. Explain why hunt conclusions must remain bounded by the scope and telemetry actually tested.

## 1. What the Threat-Hunting Block Is Building Toward

Threat hunting begins when a security team has a reason to ask a question that existing alerts have not already answered well enough.

That reason may come from:
- an active incident;
- CTI;
- an anomaly;
- a testable hypothesis;
- a known detection or visibility gap.

The hunter turns that starting signal into a bounded search.

A simple mental model for the 3.x block is:

**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

The goal is not simply to run a query.

The goal is to produce a defensible answer:

> **What did we search, what did we find, what could we not see, and what should happen next?**

## 2. The Seven Units

| Unit | Main question | What you learn |
|---|---|---|
| **3.1 – Purpose** | Why hunt at all? | How hunting complements alerts, incident response, CTI, and detection engineering |
| **3.2 – Methodology** | What exactly are we testing? | Hunt types, hypotheses, scope, priority, and distinctive patterns |
| **3.3 – Online Tools** | What external evidence can sharpen the hunt? | Use external tools to develop leads that can become internal searches |
| **3.4 – CTI for Hunters** | Which intelligence is useful for hunting? | Assess CTI, extract hunt leads, and convert structured intelligence into search inputs |
| **3.5 – Framework Application** | How does ATT&CK help organize the hunt? | Map behavior and use ATT&CK to support planning without replacing the hypothesis |
| **3.6 – Attacker Techniques** | How do we hunt a specific behavior? | Build technique-focused searches for persistence, privilege escalation, and related procedures |
| **3.7 – Site-Specific Hunt Operations** | How does this shop control, document, and route hunts? | Local initiation, documentation, completion, and handoff requirements |

Each unit adds something different to the same hunt.

## 3. Hunting Starts With a Question

A hunt is easier to reason about when the question is explicit.

For the A12 scenario, an active incident might create the question:

> **Are there additional workstations with A12-style persistence?**

That is more useful than:

> Hunt persistence.

The first question tells the hunter what problem needs to be tested.

The second only names a topic.

## 4. Turn the Question Into a Testable Hypothesis

The question becomes a hunt when the hunter states what evidence should exist if the activity is present.

For example:

> If A12-style persistence exists on additional Windows user workstations, we expect to observe Run-key values pointing to `update.exe` or closely related payloads in user-writable paths.

Now the hunt can define:
- the population;
- the time window;
- the telemetry required;
- useful exclusions;
- what counts as a meaningful candidate.

This is the core of 3.2.

## 5. Evidence Comes From More Than One Place

A hunt may use:

**Internal telemetry**
- registry events;
- process events;
- file events;
- endpoint network activity;
- Zeek or other network telemetry.

**CTI**
- behaviors;
- procedures;
- infrastructure;
- indicators;
- structured STIX objects.

**External research tools**
- sandbox observations;
- passive DNS;
- file relationships;
- web-scan results.

The hunter's job is to turn those inputs into **internal search logic**.

An external platform result does not prove that the same behavior occurred locally.

It gives the hunter a reason to look.

## 6. Refine the Search as Evidence Appears

A hunt rarely ends with the first query.

Suppose a broad search for Run-key values pointing into `%TEMP%` returns hundreds of results.

The hunter may refine using:
- value name;
- target filename;
- signer information;
- parent process;
- time relationship to other events;
- known-good software exclusions.

That refinement is analysis.

The goal is not to eliminate every benign result before searching. The goal is to make the candidate set specific enough to investigate without filtering away the behavior you are trying to find.

## 7. A Hunt Can Produce Several Kinds of Findings

A hunt does not succeed only when it finds another compromised host.

Useful outcomes include:

- additional affected hosts or accounts;
- suspicious candidates needing incident review;
- a reusable behavioral pattern;
- a **detection gap**;
- a **visibility gap**;
- a new intelligence lead;
- evidence that the searched-for behavior was **not found within the tested scope and available visibility**.

That last phrase matters.

A negative hunt does not prove:

> This behavior does not exist anywhere.

It supports:

> We did not find this behavior in the population, time window, and telemetry that we actually tested.

## 8. Different Findings Go to Different Owners

The hunt output may contain several different problems.

For example:

| Hunt finding | Likely next owner category |
|---|---|
| Additional compromised host | SOC / Incident Response |
| Behavior visible but no analytic covers it | Detection Engineering |
| Required telemetry missing | Telemetry / platform owner |
| New infrastructure or actor question | CTI |
| New suspicious pattern worth another hunt | Hunt lead-management process |

The actual team names and workflows are local and are taught in 3.7.

The important idea is that the hunt does not have to solve every downstream problem itself.

## 9. Hypothetical A12-Based Hunt Loop

Canonical A12 reaches a hunt package, but the case does **not** specify the completed hunt result, additional affected-host count, visibility-gap count, or detection-coverage outcome.

The sequence below is a **hypothetical practice extension based on A12 behavior**. Its result counts are exercise conditions used to show the full 3.x workflow; they are **not canonical A12 facts**.

### Question

> Are there additional hosts with A12-style persistence?

### Hypothesis

> If the persistence exists elsewhere, registry telemetry should show Run values pointing to the same or closely related payload pattern.

### Evidence

Search:
- registry modification telemetry;
- related process/file events;
- CTI-derived artifacts where useful.

### Refine

Separate:
- exact `Updater → %TEMP%\update.exe`;
- related suspicious Run-value patterns;
- approved software/updaters.

### Finding

Hypothetical practice result:

- 2 additional hosts with the exact persistence pattern;
- 7 hosts lack the registry telemetry needed to test the hypothesis;
- no current analytic covers the exact behavior.

### Handoff

- affected hosts → SOC / IR;
- detection gap → Detection Engineering;
- telemetry gap → platform/telemetry owner;
- new infrastructure lead → CTI.

That is a complete **practice** hunt story. Do not carry the invented host counts or coverage result back into canonical A12.

## 10. What You Need to Remember Before 3.1

You do not need to know every ATT&CK technique, query language, or external platform yet.

Remember the loop:

> **Ask a bounded question.**  
> **State what evidence should exist.**  
> **Search the data you actually have.**  
> **Refine without losing the behavior.**  
> **Report what you found and what you could not see.**  
> **Route the outcome to the right owner.**

## Orientation Check

1. Why is “hunt persistence” weaker than a bounded hunt question?
2. What does an external sandbox or passive-DNS result provide to a hunter?
3. A hunt returns no matches on 18 hosts, but 7 additional hosts lack the required telemetry. What can the hunter conclude?
4. Why might one hunt produce handoffs to SOC/IR, CTI, Detection Engineering, and a telemetry owner?

## Summary

The 3.x block teaches a complete hunt workflow:

**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

Threat hunting searches beyond what current alerts have already surfaced, but every conclusion must remain tied to the scope and visibility actually tested.

A good hunt does more than find threats. It creates reusable defensive knowledge and makes gaps visible.

**Next:** **3.1 – Purpose of Threat Hunting**.
