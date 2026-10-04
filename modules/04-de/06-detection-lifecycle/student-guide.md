# Module 4.6 – Detection Lifecycle

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.6 B / C / C ; 4.6.1 3c / 4c / 4d ; 4.6.2 3c / 4c / 4d  
- SOC: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
- Hunter: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
- CTI: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Review a live detection and choose **modify, retire/replace, or leave** based on value, performance, data availability, and redundancy.
2. Evaluate whether an external block or control change actually removes the detection's remaining value.

**Mapped Proficiency Items:**
- K: 4.6 – Detection lifecycle
- T: 4.6.1 – Call modify / retire / leave and cite the reason
- T: 4.6.2 – Given a block, decide whether the matching rule still earns its keep

## 1. Key Concepts

Detection lifecycle management asks a recurring question:

> Does this analytic still provide enough defensive value, with acceptable operational cost and valid data, to remain in its current form?

A live detection can become less useful because:
- adversary behavior changes;
- the data source changes;
- a replacement analytic provides better coverage;
- benign activity changes;
- the rule becomes redundant;
- a control prevents some of the activity;
- the original threat-specific context expires.

None of those conditions automatically tells you the answer. They trigger a review.

### Three course decisions

| Decision | Meaning |
|---|---|
| **Modify** | Keep the capability, but change logic, data assumptions, context, or implementation. |
| **Retire / replace** | Remove this analytic from active use because a replacement or changed environment makes the old rule unnecessary/unsupported. |
| **Leave** | The current analytic remains useful and its operational burden is acceptable. |

### Evaluate more than “is the threat still active?”

Useful review factors include:

- **Coverage value:** What meaningful behavior does the analytic detect?
- **Performance:** Is alert quality/volume acceptable?
- **Data health:** Are the required logs and fields still available?
- **Redundancy:** Does another analytic now provide equal or better coverage?
- **Durability:** Does the rule depend on a short-lived condition?
- **Operational cost:** Is the analyst burden proportionate to the value?
- **Replacement path:** If retiring, what coverage remains?

A campaign ending does not automatically make a behavioral detection obsolete if the behavior is useful across other threats.

### Data-source change can mean modify—not immediate retirement

If the old sensor/log path disappears but equivalent evidence exists elsewhere, the right answer may be:

> Modify/migrate the analytic to the supported data source.

Retirement is appropriate when the detection can no longer operate and no replacement path justifies keeping it active.

### Lifecycle status in rule formats is not your local lifecycle policy

Sigma defines rule-status values including `stable`, `test`, `experimental`, `deprecated`, and `unsupported`. See [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html).

Those values demonstrate that rules can have explicit lifecycle state, but your organization's production lifecycle may use different statuses and approvals.

### A block does not automatically eliminate detection value

Suppose an IP is blocked at the firewall.

Ask:
- Does the detection recognize only that IP?
- Can the same behavior occur through other infrastructure?
- Does detecting attempted access still provide useful evidence?
- Does the block apply to every path/population?
- Is the rule useful for verifying attempted activity or control bypass?

If the analytic was only a one-to-one alert on that exact object and the object is permanently blocked everywhere, retirement may be reasonable.

If the analytic detects a broader behavior or can reveal attempts around the control, it may still earn its keep.

### Document the reason

A lifecycle decision should be reproducible.

Examples:

> **Modify:** existing encoded-PowerShell analytic remains valuable, but the log schema changed and the field mapping must be updated.

> **Retire/replace:** old hash-only analytic is redundant with the new behavioral analytic and no longer adds useful coverage.

> **Leave:** rule continues to detect a meaningful behavior with acceptable alert quality; the associated IP block does not remove the broader detection value.

## 2. Knowledge Check

1. Why does “campaign ended” not automatically mean “retire the detection”?
2. A required log source disappears but equivalent telemetry now exists elsewhere. What lifecycle action may be appropriate?
3. An IP was blocked. Name two questions you should ask before retiring the matching analytic.

## 3. Summary

Lifecycle decisions balance **coverage value, performance, data, redundancy, durability, and operational cost**.

Modify when the capability still matters but needs change. Retire or replace when the analytic no longer earns its place. Leave it when it remains useful.

A block is one input to that decision—not an automatic retirement command.

**Next:** **4.7 – Sensor Availability and Performance**.

## Supporting Reference

- [Sigma Rules Specification – status and lifecycle metadata](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html)
