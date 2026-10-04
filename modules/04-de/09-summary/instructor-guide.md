# Instructor Guide – Module 4.9 – Detection Engineering Section Summary

**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led synthesis and discussion  
**Module Type:** Section summary — no proficiency mapping

## Purpose

Close the 4.x Detection Engineering block by reconnecting the lessons into the lifecycle introduced in 4.0:

**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

This is not a compressed reteaching of every 4.x module.

The learner should demonstrate that ownership, validation, telemetry, production governance, and lifecycle decisions now fit together.

## Learning Outcomes

By the end of the summary, learners should be able to:

1. Explain how 4.1–4.8 combine into one detection lifecycle.
2. Walk an A12 detection from nomination through production ownership.
3. Distinguish logic, telemetry, coverage, tuning, and governance problems.
4. Identify which 4.x unit to revisit when a DE skill remains weak.
5. Explain how DE closes the defensive feedback loop with SOC, CTI, and hunting.

## Suggested Timing

| Part | Time |
|---|---:|
| Return to the 4.0 lifecycle | 2 min |
| 4.x at a glance | 3 min |
| A12 end-to-end detection lifecycle | 7 min |
| Important distinctions | 3 min |
| Readiness / course close | 3–4 min |

## Teaching Strategy

### Do not turn this into another rule-writing lesson

Avoid:
- writing a full Sigma rule;
- reviewing every SIEM field;
- reteaching all tune outcomes;
- reteaching every local governance field.

Instead, require learners to explain **why each lifecycle decision exists**.

### Use one A12 analytic as the spine

Ask in order:

1. What defensive need exists?
2. Does current coverage already solve it?
3. What behavior and telemetry should the analytic use?
4. What positive test demonstrates the target behavior?
5. What benign control tests specificity?
6. What data test demonstrates operational visibility?
7. Who reviews and approves the deployment?
8. What happens if production data changes?
9. What evidence justifies a tune or exception?
10. When would replacement or retirement make sense?

The learner should tell one complete detection story.

## Important Distinctions to Reinforce

### Nomination vs engineering

A nominator identifies the defensive need and supporting evidence.

DE determines the implementation and lifecycle decision.

### Syntax vs soundness

Ask:

> A query parses and runs. Is it ready?

Expected answer:

> Not necessarily. It still needs behavioral, benign-control, and data validation plus local production requirements.

### Existing coverage vs new rule

Ask learners to justify why adding another analytic is better than reusing or changing current coverage.

### Tuning vs new work

A live-rule problem belongs in tuning/change review.

A behavior with no adequate coverage is new/changed coverage work.

### Exception safety

Require revalidation after adding exclusions.

### Logic vs data-path failure

Use:

> Safe replay occurred; no alert.

Expected troubleshooting:
- source event;
- ingestion;
- parsing;
- population;
- timeliness;
- logic.

### Detection vs enforcement

Reinforce that prevention/blocking authority is local.

### Deployment vs lifecycle completion

A production analytic still needs monitoring, tuning, and ownership.

## Integrated Review – Expected Shape

Use the A12 detection card.

A strong answer should include:

**Need**
> Durable coverage for A12-style encoded PowerShell.

**Coverage decision**
> Evaluate current analytic; modify or replace if partial coverage cannot meet the need safely.

**Validation**
> Positive A12-like replay, representative benign PowerShell, required process/command-line data test.

**Limitation**
> Endpoint group missing command-line telemetry is a visibility/data dependency problem, not solved by rule logic.

**Production**
> Follow verified local review/approval/deploy process with rollback authority identified.

**Follow-up**
> Monitor alert quality, data health, target coverage, and exception behavior; revalidate after changes.

Do not require identical wording. Require the lifecycle reasoning.

## DE Readiness Diagnostic

If a learner cannot:
- explain ownership boundaries → revisit **4.1**;
- explain validation → revisit **4.2**;
- explain nomination intake → revisit **4.3**;
- distinguish tune outcomes → revisit **4.4**;
- turn hunt/CTI findings into coverage decisions → revisit **4.5**;
- explain lifecycle decisions → revisit **4.6**;
- troubleshoot data dependencies → revisit **4.7**;
- explain local review/deploy/rollback paths → revisit **4.8**.

## Course-Level Closing

Use the four-function loop:

**SOC → CTI → Hunt → Detection Engineering → SOC**

Emphasize that the flow is not strictly linear in real operations.

Evidence and questions move in both directions.

A detection produces observations; observations can generate new intelligence or hunt questions; those findings can change detection coverage.

## Instructor Closing

Finish with:

> **A detection is a maintained capability, not a finished query.**

The learner should now understand both the engineering work and the operating discipline required to keep coverage useful.
