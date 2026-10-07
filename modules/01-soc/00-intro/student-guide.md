# Module 1.0 – SOC Analyst Fundamentals: How the 1.x Block Fits Together

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Time:** 10–15 minutes  
**Module Type:** Orientation — no proficiency mapping

## Learning Objectives

By the end of this introduction, you will be able to:

1. Explain the purpose of the 1.x SOC block and how its five units fit together.
2. Follow the basic SOC evidence flow from an observation to an alert decision and a handoff.
3. Recognize what each unit is responsible for teaching before you begin the detailed lessons.

## 1. What the SOC Block Is Building Toward

The SOC analyst's job begins with **evidence**.

A host runs a process. A file appears. A workstation connects to an address. A network sensor records a request. A detection fires because some part of that activity matched logic someone wrote.

The analyst's job is to turn those separate observations into a defensible answer:

> **What happened, what does the evidence support, and what should happen next?**

The 1.x block teaches that process in layers.

You will start by learning how to read the evidence itself. Then you will learn how detections describe what they are looking for. After that, you will investigate alerts, classify what the detection did, and turn the result into a report or handoff another team can use.

A simple mental model is:

**Observe → Detect → Investigate → Communicate**

## 2. The Five Units

| Unit | Main question | What you learn |
|---|---|---|
| **1.1 – Endpoint** | What happened on the host? | Process, file, host-network, registry, and image/driver activity |
| **1.2 – Zeek** | What happened on the wire? | Connections, DNS, TLS, HTTP, SMTP, files, and protocol anomalies |
| **1.3 – Detection** | What activity was the detection logic designed to match? | Sigma, Suricata, YARA, and SIEM rule fundamentals |
| **1.4 – Alerts** | What does this alert mean after we investigate it? | Context, classification, false-positive causes, categorization, and response-time goals |
| **1.5 – Reporting** | How does the result leave the SOC? | Report type, reporting timelines, notification, and distribution |

Each unit answers a different question. Together they form one workflow.

## 3. Start With the Evidence

The most important habit in this block is to separate **what the sensor recorded** from **what you conclude from it**.

For example:

> **Scenario status: Separate classroom example — not A12.**

- Endpoint telemetry may show a script interpreter launching PowerShell.
- Network telemetry may show the same workstation making an HTTP request.
- A detection may alert on one of those patterns.

Those observations can support an investigation, but each source tells you something different.

The endpoint event can tell you **which process** acted.

The network event can tell you **what crossed the wire**.

The detection tells you **which pattern matched**.

The analyst combines those pieces without making any one source say more than it actually recorded.

That evidence discipline will repeat throughout the course.

## 4. One Activity, Several Views

The classroom A12 scenario is intentionally reused across the 1.x block, but its detailed evidence is revealed progressively.

At this orientation point, keep only the case frame:

1. Suspicious activity involving `WS-JLEE` enters the SOC track.
2. 1.1 will introduce the relevant host observations.
3. 1.2 will add network observations.
4. 1.3 will show how detection logic describes what it is designed to match.
5. 1.4 will investigate and assess the resulting alert context.
6. 1.5 will turn the supported result into a usable report or handoff.

Do not fill in later A12 process, network, or registry facts before the lesson that introduces them. Different lessons will revisit the same case from different viewpoints as the evidence becomes available.

### In 1.1

You may ask:

> Which process ran?  
> Which file was created?  
> Which process opened the network connection?

### In 1.2

You may ask:

> Which host initiated the connection?  
> What DNS name was requested?  
> What URI appeared in HTTP?  
> Was a file observed on the wire?

### In 1.3

You may ask:

> What exactly would this rule match?  
> Which fields or byte patterns make the rule fire?

### In 1.4

You may ask:

> What context is still missing?  
> Was the detection correct?  
> If it was noisy, why?  
> What kind of activity was this?

### In 1.5

You may ask:

> Is this an incident report or a request for information?  
> When is it due?  
> Who receives it, and through which approved path?

The incident has not changed. The **question** has.

## 5. Host Evidence and Network Evidence Complement Each Other

Two evidence sources appear repeatedly in 1.x:

**Endpoint telemetry** sees activity from the host's point of view.

It can often tell you:
- which process ran;
- which user context was involved;
- which process created a file;
- which process initiated a network connection.

**Network telemetry** sees activity from the wire's point of view.

It can often tell you:
- which addresses communicated;
- which DNS name was requested;
- which HTTP method or URI appeared;
- which TLS properties were visible;
- which file or protocol artifact crossed the monitored connection.

Neither view is automatically better. They answer different questions.

A strong investigation uses the source that can actually support the statement you need to make.

## 6. Detections Are Leads Into Evidence

A detection alert is not the entire investigation.

A rule says:

> **This pattern matched.**

The analyst still needs to determine:
- what the underlying events show;
- what context is missing;
- whether the activity is actually the behavior the rule was intended to identify;
- whether the result should be escalated, closed, tuned, or handed to another team.

That is why the course teaches raw evidence before alert classification.

You should understand the event before deciding what the alert means.

## 7. The SOC Produces a Usable Handoff

The final SOC product is not simply “I looked at the alert.”

Someone else may need the result:
- incident response;
- CTI;
- threat hunting;
- detection engineering;
- a local operational or leadership customer.

A useful SOC handoff preserves:
- the important observations;
- the analyst's conclusion;
- the evidence that supports it;
- important gaps or uncertainty;
- the question or action the next team needs to address.

The 1.x block therefore ends with reporting and distribution rather than with the alert itself.

## 8. What You Need to Remember Before 1.1

You do not need to memorize Sysmon event IDs, Zeek fields, Sigma syntax, or alert categories yet.

For now, remember the flow:

> **1.1:** Read the host.  
> **1.2:** Read the wire.  
> **1.3:** Read the detection.  
> **1.4:** Investigate and assess the alert.  
> **1.5:** Communicate the result.

Each later module will add the detail needed to perform that step.

## Orientation Check

1. Which unit teaches you which **process** opened a network connection?
2. Which unit teaches you what an HTTP request looked like **on the wire**?
3. Why does the course teach endpoint and network evidence before alert classification?
4. What is the final purpose of 1.5?

## Summary

The 1.x SOC block teaches a complete evidence-to-handoff workflow.

You will learn to read host and network evidence, understand what detection logic matched, investigate the resulting alert, and communicate a defensible result.

The recurring discipline is simple:

> **Describe what the evidence shows first. Then decide what it means.**

**Next:** [1.1 – Endpoint Evidence Preview](../01-endpoint/intro.md).
