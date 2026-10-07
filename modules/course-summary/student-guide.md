# Course Summary – Bringing the Defensive Workflow Together

**Target Audience:** SOC Analyst, CTI Analyst, Threat Hunter, Detection Engineer  
**Estimated Time:** 20–25 minutes  
**Module Type:** Course synthesis — no proficiency mapping

## Purpose

This course began by separating four defensive functions so their questions, methods, and products would remain clear:

- Security Operations
- Cyber Threat Intelligence
- Threat Hunting
- Detection Engineering

The final lesson reconnects them.

A simple course-wide model is:

**Observe → Understand → Search → Improve Coverage → Observe Again**

Mapped to the course:

**0.x – Shared Foundations**  
Understand the environment, roles, handoffs, frameworks, tools, and visibility.

**1.x – SOC**  
Observe and investigate what happened.

**2.x – CTI**  
Turn a requirement and collected evidence into assessed intelligence.

**3.x – Threat Hunting**  
Search deliberately for related or insufficiently surfaced activity.

**4.x – Detection Engineering**  
Turn appropriate defensive knowledge into maintained detection capability.

These functions are not a one-way pipeline. They form a feedback loop.

## 1. The Course at a Glance

| Section | Central question | Primary outcome |
|---|---|---|
| **0.x – Shared Foundations** | How does defensive work fit together? | Common vocabulary and operating context |
| **1.x – SOC** | What happened, and what should happen next? | Investigated alert, case, report, or handoff |
| **2.x – CTI** | What does the evidence mean, why does it matter, and what answer does the requirement support? | Assessed intelligence and an evidence-based response |
| **3.x – Threat Hunting** | Does this or related activity exist elsewhere? | Bounded hunt findings and defensive gaps |
| **4.x – Detection Engineering** | Should this behavior become maintained automatic coverage? | Validated and maintained detection capability |

The roles may overlap in practice, but their questions and products remain different.

## 2. One A12 Story Across the Entire Course

The A12 scenario demonstrates how evidence can move through the whole defensive system.

### 0.x – Establish the Shared Context

Before anyone investigates, the team needs common language.

Learners identify:

- which role owns which question;
- how work can move between roles;
- how ATT&CK, Diamond Model, and Kill Chain organize different parts of the evidence;
- which external tools can provide useful observations;
- where important systems, access paths, and sensors sit in the environment.

This foundation prevents later analysts from confusing a tool with a function or a network path with actual visibility.

### 1.x – SOC: Observe and Investigate

An alert involving `WS-JLEE` leads to evidence such as:

- `wscript.exe` launching encoded PowerShell;
- external communication;
- a request for `/update.exe`;
- persistence-related registry activity.

The SOC establishes what the available endpoint and network evidence supports.

It separates:

- observation from conclusion;
- detection match from maliciousness;
- known facts from unanswered questions.

The SOC may create an incident record and identify a bounded question that requires another function.

### 2.x – CTI: Answer the Intelligence Requirement

The SOC sends an RFI such as:

> **What is known about the update domain, and does available evidence support that it delivered `update.exe` during A12?**

The reorganized CTI workflow begins with that requirement:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

#### Define the requirement

CTI identifies:

- the customer;
- the exact question;
- priority and deadline;
- existing evidence;
- what decision the answer will support.

#### Apply analytical tradecraft

The analyst preserves:

- source and provenance;
- source reliability;
- information credibility;
- uncertainty;
- alternative explanations;
- possible cognitive bias.

Two reports that repeat the same upstream source are not automatically two independent confirmations.

#### Use frameworks to organize the evidence

CTI may use:

- **ATT&CK** to organize behavior;
- **Diamond Model** to organize adversary, capability, infrastructure, and victim relationships;
- **Cyber Kill Chain** to reason about intrusion progression.

The framework organizes what is known. It does not fill missing facts.

#### Select platforms based on the question

The analyst chooses the source that can answer the next unresolved question.

Examples:

- internal TIP for prior context;
- VirusTotal for file relations or behavior;
- ANY.RUN for sandbox execution evidence;
- Silent Push for passive-DNS and infrastructure context;
- urlscan.io for observed web behavior.

The 2.x platform lessons intentionally use two passes:

1. **Retrieve correctly** and understand what the platform result can establish.
2. **Use the result analytically** during the appropriate enrichment method.

The platform is not the analysis.

#### Enrich and discover relationships

CTI may use:

- IOC lifecycle decisions;
- file similarity;
- RDAP/WHOIS;
- advanced DNS;
- infrastructure pivots;
- the infrastructure-focused DTF;
- correlation and link analysis.

An enrichment result usually begins as a candidate relationship.

For example:

> The update domain and `login-prd.net` share an uncommon nameserver and a time-overlapping IP.

That may support a candidate or stronger assessed infrastructure relationship depending on the rest of the evidence.

It does not automatically prove a campaign or actor attribution.

#### Assess organizational significance

The analyst keeps four questions separate:

**Applicability**
> Can this behavior occur in our environment?

**Visibility**
> Can our telemetry observe it?

**Relevance**
> Does this finding meaningfully intersect our mission, assets, technology, or exposure?

**Impact**
> If the finding is true here, what plausible consequence follows?

#### Produce and close the RFI

The final response returns to the original question.

For example:

> We assess that the update domain was likely used for attempted payload delivery in A12. WS-JLEE requested `/update.exe` from that destination during suspicious activity, but current evidence does not establish successful transfer or execution of the file.

The response separates:

- supported evidence;
- analytical judgment;
- uncertainty;
- unresolved gaps;
- agreed follow-up.

CTI then disseminates through the correct local channel and records closure or a new requirement.

### 3.x – Threat Hunting: Search Beyond the Original Case

The intelligence answer can create a new internal question:

> **Does this or related behavior exist elsewhere in the environment?**

The hunter develops:

- a bounded question;
- a testable hypothesis;
- population;
- time window;
- telemetry requirements;
- distinctive patterns.

CTI indicators, procedures, infrastructure, and behavioral artifacts become hunt inputs.

They do not become proof of local occurrence until local evidence supports them.

The hunt may produce:

- additional affected hosts;
- related suspicious candidates;
- a detection gap;
- a visibility gap;
- a new intelligence lead.

A negative result remains bounded:

> The behavior was not found within the tested population, time window, and available telemetry.

### 4.x – Detection Engineering: Create Durable Coverage

A useful hunt or intelligence finding may create a new defensive need:

> **We need durable visibility for this behavior.**

Detection Engineering first asks whether existing coverage already satisfies that need.

If not, DE may:

- modify existing logic;
- create new logic;
- validate target behavior;
- test representative benign activity;
- verify required telemetry;
- deploy through the local process;
- monitor production performance;
- tune, replace, or retire the analytic later.

The result is not merely a query.

It is maintained detection capability.

### Back to the SOC

When the behavior occurs again, the improved analytic may generate an alert.

The SOC now begins with better visibility than it had during the original A12 case.

That completes the defensive feedback loop:

**SOC → CTI → Threat Hunting → Detection Engineering → SOC**

Real operations can enter, skip, repeat, or reverse parts of this loop. The important point is that evidence and questions move between specialized functions.

## 3. The Most Important Principle: Preserve the Evidence Boundary

Every section of this course returned to the same discipline:

> **Describe what the evidence shows before deciding what it means.**

Examples:

**Observation**

> `wscript.exe` launched PowerShell with an encoded command.

**Assessment**

> The activity is suspicious and consistent with the behavior under investigation.

The assessment may be reasonable, but it is not the same thing as the observation.

The same boundary applies across the course:

- SOC should not turn an alert label into proof of maliciousness.
- CTI should not turn a platform result or source claim into established fact.
- Hunting should not turn an external lead into proof of local occurrence.
- DE should not turn a matching condition into proof that the underlying activity is malicious.

Good defensive work preserves the boundary.

## 4. Questions Should Drive Tools

The course introduced many technologies and platforms:

- endpoint and SIEM telemetry;
- Zeek;
- Sigma;
- Suricata;
- YARA;
- threat-intelligence platforms;
- VirusTotal;
- ANY.RUN;
- Silent Push;
- urlscan.io;
- STIX;
- ATT&CK.

Each tool provides a capability.

None replaces the question.

A useful analyst asks:

- What am I trying to determine?
- Which source can answer that question?
- What exactly did the source observe?
- When?
- What are the limitations?
- What other evidence would change the conclusion?

This is why the reorganized CTI track explicitly teaches **platform selection before deep enrichment**.

The goal is not to touch every available tool.

The goal is to retrieve the evidence needed for the next analytical decision.

## 5. Frameworks Organize Evidence; They Do Not Create It

The course used several frameworks for different purposes.

**MITRE ATT&CK** helps describe adversary behavior.

**Diamond Model** helps organize relationships among adversary, capability, infrastructure, and victim.

**Cyber Kill Chain** helps reason about progression through an intrusion.

**DTF** helps organize infrastructure-focused pivots.

**STIX** helps represent and exchange structured CTI.

Each framework has a scope.

For example, file-similarity and behavioral relationships may support an assessment without belonging inside an infrastructure-focused DTF representation.

An incomplete model is preferable to a complete model built on assumptions.

## 6. Claim Strength Should Follow Evidence Strength

This principle is especially visible in the reorganized CTI section.

A shared nameserver may support a **candidate relationship**.

Several distinctive, time-relevant observations may support a **stronger assessed relationship**.

Evidence of coordinated activity over time may support an **activity-set or campaign assessment**.

Actor attribution requires still more evidence.

The analyst should not skip levels simply because the next label is more satisfying.

The same discipline applies elsewhere:

- a rule match is not automatically malicious;
- SYSTEM execution does not automatically prove a privilege-escalation method;
- an unalerted behavior is not automatically a false negative;
- no hunt results do not prove enterprise absence.

## 7. Visibility and Coverage Are Different Problems

This distinction connects SOC, CTI, hunting, and Detection Engineering.

### Applicability

Can the behavior occur in the environment?

### Visibility gap

The behavior can occur, but the evidence needed to observe or test it is missing or insufficient.

Examples:

- registry telemetry is not collected;
- a network segment lacks the required sensor;
- parsing removed a needed field.

### Detection gap

The required telemetry exists, but current analytics do not adequately cover the behavior.

### Relevance

Does the finding matter to the organization's mission, assets, technologies, or exposure?

These questions are related, but they are not interchangeable.

A relevant, applicable behavior can still have poor visibility.

A visibility problem normally requires collection, sensor, ingestion, or data-quality work.

A detection problem requires analytic coverage.

## 8. Negative Results Have Boundaries

Several parts of the course taught the same idea in different forms.

A SOC analyst cannot conclude that an event did not occur simply because the expected log is absent.

A CTI analyst cannot conclude that an object is benign because a TIP returned no match.

A hunter cannot conclude that the enterprise is clean because a query returned zero results.

A detection engineer cannot conclude that behavior did not happen because a rule remained silent.

A stronger statement is:

> **We did not observe the behavior within the scope and visibility available to us.**

Good conclusions state their boundaries.

## 9. Same Evidence, Different Product

One artifact can support several different workflows.

A domain may appear in:

- a SOC investigation;
- a CTI evidence record or assessment;
- a threat-hunt query;
- a detection analytic.

The evidence has not changed.

The **question and product** have.

Ask:

> **What decision is this work supposed to support?**

That question helps identify which role's product you are creating.

## 10. Handoffs Are Part of the Work

No defensive function needs to solve every problem itself.

A useful handoff communicates:

- what was observed;
- what was assessed;
- the supporting evidence;
- important uncertainty;
- what question or action remains.

Examples:

**SOC → CTI**

> What is known about this infrastructure and its relationship to the observed behavior?

**CTI → Hunt**

> This procedure appears applicable and relevant. Determine whether it exists elsewhere internally.

**Hunt → Detection Engineering**

> The behavior is visible and repeatable, but current analytics do not adequately cover it.

**Detection Engineering → SOC**

> This behavior now has validated production coverage and associated triage guidance.

A handoff is not abandonment.

It is how specialized defensive work becomes a coordinated capability.

## 11. Local Process Matters

The course teaches transferable tradecraft, but real organizations determine:

- priorities;
- customers;
- intelligence requirements;
- approval authorities;
- reporting requirements;
- hunt-control processes;
- deployment workflows;
- handling rules;
- authoritative repositories;
- sensor ownership;
- escalation paths;
- dissemination channels.

When local information is unknown, identify the specific missing operating fact.

Do not replace missing organizational knowledge with a plausible classroom workflow.

Generic tradecraft tells you **what questions to ask**.

Local policy tells you **how this organization answers them**.

## 12. Course Readiness Checklist

By the end of the course, you should be comfortable saying:

- [ ] I can distinguish an observation from an analytical judgment.
- [ ] I understand what endpoint and network evidence can and cannot establish.
- [ ] I can explain why a detection matched without treating the alert as automatic proof of maliciousness.
- [ ] I can identify when a SOC question should become an RFI or other handoff.
- [ ] I can distinguish data, information, and intelligence.
- [ ] I can define an intelligence requirement before collecting.
- [ ] I can evaluate source reliability, information credibility, uncertainty, and alternative explanations.
- [ ] I can choose a CTI platform based on the question rather than tool availability.
- [ ] I can distinguish a platform result, enrichment pivot, assessed relationship, campaign assessment, and attribution.
- [ ] I can separate applicability, visibility, relevance, and impact.
- [ ] I can produce an evidence-based RFI response and identify closure or follow-up.
- [ ] I can turn intelligence or an incident into a bounded hunt hypothesis.
- [ ] I can define hunt scope, telemetry, and limitations.
- [ ] I can distinguish a detection gap from a visibility gap.
- [ ] I can express a negative finding within the scope that was actually tested.
- [ ] I can turn a useful defensive finding into a Detection Engineering nomination.
- [ ] I can distinguish rule syntax from production-ready detection capability.
- [ ] I can validate detection behavior, benign controls, and telemetry dependencies.
- [ ] I understand that detections require monitoring, tuning, maintenance, and eventual retirement.
- [ ] I can identify when work belongs to another defensive function and provide a usable handoff.
- [ ] I know when an answer depends on local organizational policy rather than generic tradecraft.

Weakness in one area is not a reason to restart the course.

Use the section summaries to identify which track or lesson to revisit.

## 13. What the Course Was Really Teaching

The course included many technologies, frameworks, and technical details.

Those support a smaller set of durable habits.

### Start with a clear question

Know what you are trying to determine.

### Use evidence appropriate to that question

Different sensors, sources, platforms, and frameworks answer different questions.

### Preserve provenance

Know where the evidence came from, when it was observed, and whether multiple sources are truly independent.

### Preserve uncertainty

Say what is known, what is assessed, and what remains unresolved.

### Keep scope visible

A conclusion is only as strong as the population, time window, visibility, and evidence behind it.

### Keep claim strength proportional

A candidate link should remain a candidate until stronger evidence justifies promotion.

### Produce something another defender can use

Analysis becomes operationally valuable when it supports a decision, action, or next question.

### Improve the system when you learn something

An investigation can produce an intelligence requirement.

Intelligence can produce a hunt.

A hunt can expose a detection or visibility gap.

Detection Engineering can turn that lesson into better future coverage.

That is how defensive operations learn.

# Final Course Model

The course began with separate roles.

It ends with one connected defensive system:

**Observe → Understand → Search → Improve Coverage → Observe Again**

Or, expressed through the role tracks:

**SOC → CTI → Threat Hunting → Detection Engineering → SOC**

The cycle is not rigid and the roles are not silos.

What connects them is disciplined use of evidence, appropriately bounded judgments, and clear handoffs.

> **Follow the evidence. Answer the question in front of you. Preserve what remains uncertain. Give the next defender something they can use.**
