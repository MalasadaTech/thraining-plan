# Module 4.0 – Detection Engineering: How the 4.x Block Fits Together

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Estimated Time:** 10–15 minutes  
**Module Type:** Orientation — no proficiency mapping

## Learning Objectives

By the end of this introduction, you will be able to:

1. Explain the purpose of the 4.x Detection Engineering block and how its eight units fit together.
2. Follow the detection lifecycle from a defensive need to maintained production coverage.
3. Explain why a detection is more than rule syntax and why its effectiveness depends on both logic and telemetry.

## 1. What the Detection Engineering Block Is Building Toward

Detection Engineering turns recurring defensive needs into **maintained detection capability**.

A SOC analyst may notice a noisy alert.  
A threat hunter may discover behavior that no analytic covers.  
CTI may identify a procedure worth monitoring.  
An existing analytic may stop working because the data changed.

Detection Engineering takes those needs and decides what durable coverage should exist.

A simple mental model for the 4.x block is:

**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

The goal is not simply to write a query.

The goal is to maintain a detection that:
- addresses a real defensive need;
- uses telemetry that actually exists;
- behaves as intended;
- reaches production through the local process;
- remains useful as the environment changes.

## 2. The Eight Units

| Unit | Main question | What you learn |
|---|---|---|
| **4.1 – What DE Owns** | Which work belongs to Detection Engineering? | Detection lifecycle ownership, nominations, rule-authoring boundaries, and enforcement/control ownership |
| **4.2 – Sound Detections** | How do we know the analytic is actually good? | Logic, data requirements, positive testing, benign controls, and validation |
| **4.3 – Nominations** | How does new detection work enter the lifecycle? | Turning SOC, hunt, and CTI needs into reviewable DE inputs |
| **4.4 – Tune Requests** | What do we do when a live analytic needs attention? | Tune, exception, replace, leave, or retire decisions |
| **4.5 – Hunt and Intel Packages** | How do findings become coverage decisions? | Reuse existing coverage, modify it, or create new detection work |
| **4.6 – Detection Lifecycle** | How does coverage stay useful over time? | Deployment, monitoring, maintenance, change, replacement, and retirement |
| **4.7 – Sensors and Data** | Can the detection actually see what it needs? | Collection, ingestion, parsing, population coverage, timeliness, and logic dependencies |
| **4.8 – Site-Specific DE** | How does this organization run DE in production? | Local requirements, review, approval, deployment, rollback, and authoritative repositories |

Each unit addresses a different part of the same lifecycle.

## 3. Start With the Defensive Need

Detection work should begin with a problem worth solving.

For the A12 scenario:

> **We need durable visibility for encoded PowerShell behavior similar to what occurred on `WS-JLEE`.**

That is enough to begin DE review.

The nominator does not need to arrive with:
- a production-ready Sigma rule;
- a final KQL query;
- the exact exclusion list;
- deployment instructions.

Those are engineering decisions.

The first DE question is:

> **What behavior needs coverage, and do we already cover it adequately?**

## 4. Reuse Coverage Before Creating More

A new rule is only one possible answer.

When a nomination arrives, DE should consider:

1. Does an existing analytic already cover this behavior?
2. Could an existing analytic be safely expanded or tuned?
3. Is a new analytic justified?
4. Is the need better handled by another control or workflow?
5. Is the required telemetry even available?

This prevents the detection library from becoming a pile of overlapping rules that all try to solve the same problem.

## 5. A Rule Is Not Yet a Detection Capability

Writing valid syntax is only one step.

A production detection also needs evidence that:

- the target behavior causes the analytic to match;
- representative benign activity does not match unnecessarily;
- required fields and telemetry are present;
- the analytic works on the intended population;
- changes and exclusions do not remove the target behavior;
- the rule can be maintained after deployment.

That is why 4.x follows the 1.3 rule lessons rather than duplicating them.

**1.3** teaches how rules work.

**4.x** teaches how detections are operated as a capability.

## 6. Validation Tests Both Logic and Data

Suppose DE builds an analytic for encoded PowerShell.

A useful validation asks:

### Positive test

> Does known target behavior match?

### Benign-control test

> Does representative normal PowerShell activity remain outside the detection when appropriate?

### Data test

> Does the production data path actually provide the process and command-line fields the analytic expects?

A rule can be perfectly written and still be ineffective if the required data is absent or mapped differently.

## 7. Deployment Is Not the End

A detection changes once it enters production.

You may discover:
- benign software generates large alert volume;
- adversary behavior changes;
- field mappings change;
- a sensor stops covering part of the population;
- another analytic makes the old one redundant;
- a narrow exception suppresses something it should not.

That is why the lifecycle continues:

**Deploy → Monitor → Tune/Change → Revalidate → Replace/Retire when appropriate**

A detection that nobody maintains is not durable coverage.

## 8. A Silent Detection Has More Than One Possible Explanation

If a rule does not fire, several explanations are possible:

- the target behavior did not occur;
- the logic does not match it;
- the event was not collected;
- the event never reached the platform;
- parsing changed;
- the required field is empty;
- the relevant host population is not covered;
- the event arrived outside the analytic's time window.

The engineer therefore asks:

> **Did the behavior occur, did the data arrive correctly, and would the logic match that data?**

This prevents a silent rule from being interpreted automatically as proof that the environment is clean.

## 9. Detection Engineering Has Adjacent Owners

Detection Engineering works closely with:
- SOC;
- threat hunting;
- CTI;
- telemetry/platform owners;
- incident response;
- control/enforcement owners.

The course keeps those responsibilities visible.

For example:

> **Create durable analytic coverage** → Detection Engineering

> **Investigate this host** → SOC / IR

> **Block this IP at the firewall** → locally authorized enforcement/control owner

> **Fix missing process telemetry** → telemetry/platform owner

The exact team names and approval paths are local and are taught in 4.8.

## 10. The A12 Detection Lifecycle

One A12 example can show the entire 4.x block.

### Need

Threat hunting identifies recurring encoded PowerShell and a persistence pattern.

### Coverage Decision

DE checks whether existing analytics already cover the behavior.

### Build / Change

DE creates or modifies the appropriate analytic.

### Validate

Test:
- target behavior;
- benign controls;
- required data;
- intended host population.

### Deploy

Use the local review, approval, and release process.

### Monitor

Review alert quality, data health, and whether the analytic continues to provide the intended coverage.

### Improve

Tune narrow benign conditions, update logic when behavior changes, or replace the analytic when a better design exists.

### Retire

Remove or supersede the analytic when it no longer provides enough value.

That is a complete detection-engineering story.

## 11. What You Need to Remember Before 4.1

You do not need to know every rule format, deployment pipeline, or local approval process yet.

Remember the lifecycle:

> **Start with the need.**  
> **Decide what coverage should exist.**  
> **Build or change the analytic.**  
> **Validate the behavior and the data.**  
> **Deploy through the local process.**  
> **Monitor and maintain it.**  
> **Replace or retire it when that becomes the better defensive choice.**

## Orientation Check

1. Why is a syntactically valid rule not automatically a production-ready detection?
2. A hunter provides a strong behavior description but no rule. Can DE begin work from that?
3. A detection does not fire during a replay. Name two explanations other than “the behavior did not happen.”
4. Why might DE modify or reuse an existing analytic instead of creating a new one?

## Summary

The 4.x block teaches the full lifecycle of **maintained detection capability**:

**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

Detection Engineering is not only rule authoring. It connects defensive needs to reliable, tested, maintainable coverage—and keeps that coverage working as behavior, telemetry, and the environment change.

**Next:** **4.1 – What Detection Engineering Owns**.
