# Instructor Guide – Module 1.0 – SOC Analyst Fundamentals: How the 1.x Block Fits Together

**Estimated Time:** 10–15 minutes  
**Delivery Method:** Instructor-led orientation and discussion  
**Module Type:** Orientation — no proficiency mapping

## Purpose

Give learners a mental model for the entire 1.x SOC block before they begin detailed telemetry lessons.

The learner should leave this introduction understanding that 1.x is one connected workflow:

**endpoint evidence → network evidence → detection logic → alert investigation → reporting/handoff**

This is orientation rather than a technical lesson. Avoid front-loading field names or rule syntax that later modules teach in depth.

## Learning Objectives

By the end of the introduction, learners should be able to:

1. Explain what each 1.x unit contributes to SOC work.
2. Follow the evidence-to-handoff progression.
3. Recognize that different sensors and detections answer different questions about the same activity.

## Suggested Timing

| Part | Time |
|---|---:|
| Why the SOC block begins with evidence | 2 min |
| Walk through 1.1–1.5 | 4 min |
| A12 as one activity seen several ways | 4 min |
| Orientation check and transition | 2–3 min |

## Core Teaching Model

Write this on the board or keep it visible:

**Observe → Detect → Investigate → Communicate**

Then map the units beneath it:

- **1.1 Endpoint** → host observations
- **1.2 Zeek** → network observations
- **1.3 Detection** → logic that matches observations
- **1.4 Alerts** → investigation and assessment
- **1.5 Reporting** → handoff and distribution

## Teaching Notes

### Begin with the question, not the technology

The learner does not need to know Sysmon, Zeek, Sigma, or Suricata syntax to understand the structure.

Use questions:

- What happened on the host?
- What happened on the wire?
- Why did the rule fire?
- Was the detection correct?
- Who needs the result?

Those questions explain the curriculum sequence better than a product list.

### Use A12 as spoiler-light connective tissue

At 1.0, do not preview the detailed A12 process, network, or registry observations that are intentionally introduced later.

Keep the example at the level of the course map:

1. Suspicious activity involving `WS-JLEE` enters the SOC track.
2. 1.1 introduces host evidence.
3. 1.2 adds network evidence.
4. 1.3 explains detection logic.
5. 1.4 investigates and assesses the alert context.
6. 1.5 communicates the supported result.

Then show how each unit sees a different slice as new evidence becomes available.

The teaching point is:

> The case does not change; the evidence is revealed progressively and the analytic question changes.

### Reinforce evidence boundaries

A useful early distinction:

- endpoint telemetry may identify the **process**;
- network telemetry may identify the **protocol transaction**;
- the detection explains **what pattern matched**.

Learners should not expect one source to contain every fact.

This prepares them for later lessons where missing fields are treated as evidence gaps rather than filled by assumption.

### Explain why detection comes after raw evidence

The course intentionally teaches 1.1 and 1.2 before 1.3 and 1.4.

A learner who can read the underlying event can interpret a detection more accurately.

A learner who starts with the alert label is more likely to treat the detection's conclusion as ground truth.

### Reporting is part of the analytic task

Close the loop by emphasizing that SOC work must become usable by the next consumer.

The analyst is not finished simply because the alert was reviewed.

The result may need to become:
- an incident handoff;
- an RFI;
- a tuning request or detection-engineering input;
- another locally defined product.

Detailed routing rules remain in 1.5.

## Orientation Check – Expected Answers

1. **1.1 Endpoint** — host-network telemetry can identify the initiating process.
2. **1.2 Zeek** — HTTP/network protocol evidence is read from the network sensor.
3. Because classification should be based on the underlying evidence, not only the alert label.
4. To turn the investigation result into the correct report/handoff and route it to the appropriate recipient through the approved path.

## Transition

End with:

> In 1.0 you learned the map. In 1.1, we begin with the host and learn the five kinds of endpoint activity you will use throughout the SOC block.

**Next:** **1.1.1 – Endpoint Activity (the Map)**.
