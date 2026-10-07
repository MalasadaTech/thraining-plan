# Module 1.6 – SOC Analyst Section Summary

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Time:** 15–20 minutes  
**Module Type:** Section summary — no proficiency mapping

## Purpose

Module 1.0 introduced the SOC block as an evidence-to-handoff workflow.

Module 1.6 closes that loop.

By this point, you have learned how to read endpoint evidence, interpret network evidence, understand what detection logic matched, investigate and assess alerts, and communicate the result through the correct reporting path.

The summary returns to the same model:

**Endpoint evidence → Network evidence → Detection logic → Alert investigation → Reporting / handoff**

Or more simply:

**Observe → Detect → Investigate → Communicate**

## 1. What You Can Now Do

The 1.x block is designed to give you a complete SOC foundation.

You should now be able to:

- describe host activity from endpoint telemetry;
- describe network activity from Zeek without claiming visibility the sensor does not have;
- explain what basic detection logic is designed to match;
- investigate an alert beyond its title;
- classify what the detection did;
- identify likely false-positive causes without confusing cause with classification;
- distinguish activity category from TP/FP/TN/FN;
- track the correct response and reporting timelines;
- choose the correct report or request;
- route the result through the approved handoff path.

The important skill is not memorizing isolated fields.

It is being able to connect the evidence into a defensible operational story.

## 2. The 1.x Block at a Glance

| Unit | Core skill retained |
|---|---|
| **1.1 – Endpoint** | Explain what happened on the host and which process, user, file, registry, network, or image/driver activity was involved. |
| **1.2 – Zeek** | Explain what happened on the wire and what the network sensor can—and cannot—support. |
| **1.3 – Detection** | Read basic Sigma, Suricata, YARA, and SIEM logic and explain what causes the rule to match. |
| **1.4 – Alerts** | Gather context, investigate, classify, identify false-positive causes, categorize activity, and manage response-time goals. |
| **1.5 – Reporting** | Choose the right report or request, identify the applicable timeline, and route it through the approved path. |

These are not separate jobs.

They are stages of one SOC workflow.

## 3. A12 End to End

The A12 scenario shows how the pieces fit together.

### Step 1 – Endpoint evidence

On `WS-JLEE`, endpoint telemetry shows:

- `wscript.exe` launches PowerShell;
- the PowerShell command is encoded;
- additional file, registry, or network activity may appear around the same time.

The endpoint view answers questions such as:

> Which process ran?  
> Which user context was involved?  
> Which process touched the file or registry?  
> Which process initiated a network connection?

The evidence should be described before deciding what it means.

### Step 2 – Network evidence

Zeek or other network telemetry shows activity such as:

- the host communicates with external infrastructure;
- a DNS lookup occurs;
- an HTTP request includes `/update.exe`;
- a TLS or connection record supplies additional context.

The network view answers a different set of questions:

> Which systems communicated?  
> What protocol activity was visible?  
> Which name, URI, or transferred artifact appeared on the wire?

The network sensor normally cannot tell you which local process opened the connection.

That fact comes from endpoint telemetry.

### Step 3 – Detection logic

A rule fires because observed data matches its conditions.

The analyst should be able to explain:

> **What part of the event caused this detection to match?**

For example:
- encoded PowerShell;
- a specific URI;
- a byte/string pattern;
- a field combination in SIEM data.

A detection match tells you that the rule condition was satisfied.

It does not, by itself, prove maliciousness.

### Step 4 – Alert investigation

Now combine the available context.

The analyst asks:

- What actually happened?
- Which observations support the conclusion?
- What evidence is still missing?
- Does the activity fit expected behavior?
- Does the alert need escalation?
- Is there a tuning or coverage issue?

The alert title is the starting point, not the final answer.

### Step 5 – Assessment

Several different labels may be required.

Keep them separate.

**Detection classification**
- True Positive
- False Positive
- True Negative
- False Negative

**Activity category**
- scanning/reconnaissance
- user-level access
- root-level access
- unsuccessful activity
- another locally defined category

**False-positive cause**
- analyst/tool activity
- overly broad or untuned logic
- another locally recognized explanation

These answer different questions.

### Step 6 – Reporting and handoff

The investigation now becomes something another team can use.

For A12, that may include:

**Incident report**
> Record the suspected or confirmed security case and hand it to IR through the approved workflow.

**RFI**
> Ask CTI, hunt, IT, or another team a bounded question needed to continue the case.

The report or request should preserve:
- important observations;
- the analyst's conclusion;
- evidence supporting the conclusion;
- important uncertainty or gaps;
- what the next team needs to do or answer.

## 4. Distinctions That Keep a SOC Assessment Precise

Several SOC concepts sit close together in the workflow. Keeping the question behind each one clear prevents a correct observation from turning into an unsupported conclusion.

### Observations and conclusions require different levels of support

> `wscript.exe` launched encoded PowerShell.

is a direct observation from the process evidence.

> The host is compromised.

is a broader conclusion. It may eventually be justified, but it requires additional evidence and reasoning. A strong investigation shows the path from the observation to the conclusion instead of treating them as equivalent statements.

### Endpoint and network telemetry answer different questions

Endpoint telemetry can often identify the process, user, file, registry activity, and host-local context. Network telemetry can describe the connection or protocol transaction visible to the sensor.

When the two views are correlated, preserve which source supplied each field. That makes the finding reviewable and prevents host-only context from being silently attributed to a network sensor, or vice versa.

### A detection match establishes that the logic matched; investigation establishes what the activity means

When a rule fires, the analyst knows that the event satisfied the rule's conditions. Classification requires the next layer of evidence: whether the assessed target condition was actually present.

This is why a rule match can justify investigation without automatically proving maliciousness.

### Detection classification and activity category answer different questions

**TP / FP / TN / FN** describe the relationship between the detection outcome and the assessed target condition.

A category such as **user-level access**, **root-level access**, or **scanning/reconnaissance** describes the kind of activity observed.

An investigation may need both labels because neither one replaces the other.

### Classification and false-positive cause are separate judgments

Calling an alert a **False Positive** answers whether the alert represented the target condition being evaluated.

Explaining that benign helpdesk activity or overly broad logic caused the match answers **why** the false positive occurred. Separating those questions makes tuning recommendations more useful.

### Alert-response and reporting timelines may start from different events

The alert queue may have a response-time goal while an incident report or RFI has a separate submission clock. Track the trigger, due time, and current state for the specific obligation you are measuring.

### Incident reports and RFIs carry different products

An incident report records and routes the security case. An RFI asks another team a bounded question needed to advance the work.

They can exist beside one another because the case and the unanswered question are related but different products.

### A correct recipient still requires an approved delivery path

Knowing who needs the information is only part of a handoff. Sensitive operational information also needs to move through the approved channel so handling, accountability, and recordkeeping are preserved.

## 5. Integrated Review Exercise

Use this evidence card:

> **Host:** `WS-JLEE`  
> **User:** `jlee`  
> **Endpoint:** `wscript.exe` launches encoded PowerShell  
> **Network:** the host requests `/update.exe` from external infrastructure  
> **Detection:** an analytic fires on the encoded PowerShell pattern  
> **Gap:** available evidence does not yet establish whether `/update.exe` was successfully downloaded and executed

Write a short SOC handoff using this structure:

### Host evidence
What does endpoint telemetry establish?

### Network evidence
What does network telemetry establish?

### Detection
What caused the analytic to match?

### Assessment
What can you defensibly conclude now?

### Remaining gap
What important question remains unanswered?

### Report / handoff
What record or request should carry the result forward?

A strong answer should preserve the difference between **observed behavior** and **what remains unproven**.

## 6. SOC Readiness Checklist

Before moving into 2.x, you should be comfortable saying:

- [ ] I can describe process, file, registry, endpoint-network, and image/driver activity from evidence.
- [ ] I can explain what Zeek observed without assigning it host-process visibility it does not have.
- [ ] I can explain what a basic detection rule is designed to match.
- [ ] I can investigate an alert beyond its title or severity label.
- [ ] I can distinguish TP/FP/TN/FN from activity categorization.
- [ ] I can distinguish a false positive from the reason it occurred.
- [ ] I can identify which alert or reporting timeline applies.
- [ ] I can choose an incident report versus an RFI.
- [ ] I can identify the correct consumer and approved handoff path.
- [ ] I can state what the evidence does **not** establish.

If one of these is weak, return to the corresponding unit before moving forward.

## 7. Bridge Into 2.x CTI

The SOC establishes what happened locally as far as the available evidence allows.

Sometimes that is enough to close or escalate the case.

Other times the SOC reaches a question that needs intelligence work.

For example:

> What is known about this domain?  
> Has this infrastructure appeared in other reporting?  
> Which threat activity uses this behavior?  
> Is this pattern relevant to our environment?

That is where 2.x begins.

The SOC provides the observations and the question.

CTI adds context, evaluates sources, enriches the evidence, answers intelligence requirements, and produces assessed intelligence.

The **RFI** is one practical bridge between the two functions.

## Summary

The 1.x SOC block taught one complete operational flow:

**Observe → Detect → Investigate → Communicate**

You can now move from raw endpoint and network evidence to an investigated alert and a usable handoff.

Keep one principle with you into every later track:

> **Describe what the evidence shows first. Then decide what it means.**

**Next:** [2.0 – Cyber Threat Intelligence Orientation](../../02-cti/00-intro/student-guide.md).
