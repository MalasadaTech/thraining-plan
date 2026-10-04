# Instructor Guide – Module 4.6 – Detection Lifecycle

**Estimated Time:** 20–25 minutes

## Purpose

Teach lifecycle review as a value/coverage decision rather than a simplistic “old threat = old rule” or “blocked IOC = retire” rule.

## Review Factors

- coverage value
- alert quality/performance
- data availability
- redundancy/replacement
- durability
- operational cost

## Technical Nuances

- Campaign relevance can expire while behavior-based coverage remains useful.
- Sensor/log migration may call for analytic migration rather than retirement.
- Blocking one object may not remove the value of detecting the broader behavior or attempted access.
- Public rule status fields are examples, not local approval states.

Reference: [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html)

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Threat report is old → retire. | Ask whether the behavior remains relevant across threats. |
| Sensor gone → retire. | Check whether equivalent data supports migration. |
| IP blocked → retire. | Evaluate remaining behavior/control-monitoring value. |
| Rule is noisy → retire. | Consider tune/modify and compare value vs cost. |

## Knowledge Check – Answer Key

1. The analytic may detect reusable behavior used by other threats.
2. Modify/migrate to the supported data source.
3. Does the rule cover broader behavior? Can attempts still occur via other paths? Is attempted access still useful evidence? Does the block cover all populations?
