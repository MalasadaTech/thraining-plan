# Instructor Guide – Module 4.0 – Detection Engineering: How the 4.x Block Fits Together

**Estimated Time:** 10–15 minutes  
**Delivery Method:** Instructor-led orientation and discussion  
**Module Type:** Orientation — no proficiency mapping

## Purpose

Give learners a mental model for the entire 4.x Detection Engineering block before they enter the detailed lifecycle lessons.

Keep this lifecycle visible:

**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

The learner should leave understanding that Detection Engineering owns more than rule syntax. It operates detections as maintained defensive capability.

## Learning Objectives

By the end of the introduction, learners should be able to:

1. Explain what each 4.x unit contributes to the detection lifecycle.
2. Follow a defensive need from nomination through maintenance or retirement.
3. Explain why both analytic logic and telemetry/data health determine whether a detection works.

## Suggested Timing

| Part | Time |
|---|---:|
| Why DE exists | 2 min |
| Walk through 4.1–4.8 | 4 min |
| A12 detection lifecycle | 4–5 min |
| Orientation check and transition | 2–3 min |

## Core Teaching Model

Write or display:

**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

Then map the track beneath it:

- **4.1 Ownership** → what DE owns
- **4.2 Soundness** → what makes the analytic defensible
- **4.3 Nominations** → how new work enters
- **4.4 Tune Requests** → how live coverage changes
- **4.5 Hunt/Intel Packages** → how findings become coverage decisions
- **4.6 Lifecycle** → how deployed detections are maintained
- **4.7 Sensors/Data** → whether required evidence reaches the analytic
- **4.8 Site-Specific** → how the local organization reviews, approves, deploys, and retires

## Teaching Notes

### Start with the need, not the rule

Use:

> We need durable visibility for A12-style encoded PowerShell.

Ask whether the hunter or SOC analyst must also provide the final Sigma/KQL rule.

Expected answer: no.

A nomination gives DE enough context to evaluate the defensive need. Engineering turns that need into the correct coverage decision.

### Reuse before adding

Preview that DE can:
- use existing coverage;
- modify existing coverage;
- create new coverage;
- decide that detection is not the right answer.

The goal is defensive value, not maximum rule count.

### Rule syntax vs detection capability

Connect back to 1.3:

- **1.3** = how rules are expressed/interpreted
- **4.x** = how detections are validated, deployed, monitored, tuned, maintained, and retired

This distinction prevents learners from equating “query runs” with “detection ready.”

### Introduce the three validation questions

Use a simple set:

1. **Positive:** Does target behavior match?
2. **Benign control:** Does representative normal activity remain outside the match when appropriate?
3. **Data:** Does the expected telemetry actually exist in the expected fields?

These questions prepare learners for 4.2 and 4.7.

### A silent rule is ambiguous

Ask:

> If the rule did not fire, what could be wrong?

Expected answers can include:
- no target behavior;
- logic issue;
- missing collection;
- ingestion failure;
- parsing/field mismatch;
- population gap;
- timing issue.

The purpose is to establish early that DE must reason across the analytic **and** its data dependencies.

### Detection vs enforcement

Preview the course boundary:

- detection capability → DE
- containment/blocking → locally authorized control owner unless local operating model assigns it to DE

Emphasize that this is an organizational ownership question, not an industry law.

### Deployment does not finish the job

Make the lifecycle circular.

After deployment:
- monitor;
- tune;
- revalidate;
- replace;
- retire.

A live analytic with no owner becomes technical debt rather than maintained coverage.

## Orientation Check – Expected Answers

1. Production readiness requires validated behavior, acceptable benign performance, required telemetry, population coverage, and lifecycle ownership—not just valid syntax.
2. Yes. A reviewable behavior/evidence nomination is enough for DE to begin evaluating coverage.
3. Examples: data not collected, ingestion/parsing failure, field mismatch, host not covered, late data, rule logic miss.
4. Existing coverage may already satisfy the need or may be safer/easier to extend than creating overlapping detection logic.

## Transition

End with:

> In 4.0 you learned the lifecycle. In 4.1, we begin by deciding which parts of that lifecycle belong to Detection Engineering and which belong to adjacent defensive functions.

**Next:** **4.1 – What Detection Engineering Owns**.
