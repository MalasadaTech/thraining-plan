# Module 4.3 – Nominations from SOC, Hunt, and CTI

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.3 B / C / C ; 4.3.1 3c / 4c / 4d  
- SOC: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
- Hunter: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
- CTI: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes

## Learning Objectives

1. Explain what makes a detection nomination **clear enough to review** without requiring the nominator to design the final analytic.
2. Review a nomination as **accept**, **send back**, or **reject/route elsewhere**, and state what the nominator still owes versus what DE will finish.

**Mapped Proficiency Items:**
- K: 4.3 – Nominations from SOC, hunt, and CTI
- T: 4.3.1 – Review a nomination and say who finishes what

## 1. Key Concepts

A nomination is the point where another defensive function says:

> We have evidence of a recurring defensive need. Please evaluate whether detection engineering should address it.

SOC, hunt, and CTI can all nominate.

The nominator does **not** need to arrive with production-ready logic. DE is the team expected to turn a clear defensive need into a sound, maintainable analytic when a new detection is appropriate.

### Minimum: need + evidence pointer

For this course, a nomination is clear enough to review when it names:

1. **The need** – what behavior or gap should be addressed.
2. **The evidence/context pointer** – where DE can inspect the case, hunt package, report, or other source that supports the need.

Helpful additional information may include:
- affected platform/population;
- representative event or observable;
- suspected ATT&CK technique;
- relevant telemetry;
- a draft rule, if the nominator already has one.

Those additions improve the handoff but are not a reason to force SOC, hunt, or CTI to perform DE's design work.

### Three review outcomes

#### Accept for work

Use when the defensive need and supporting context are clear enough to evaluate.

Accept does not mean:

> We promise to deploy the nominator's exact idea.

It means DE owns the next engineering decision:
- reuse an existing detection;
- modify one;
- create a new one;
- determine that no durable analytic is justified.

#### Send back

Use when the request may belong to DE but the evidence is too incomplete to evaluate.

State exactly what is missing.

Example:

> Please add the hunt-package reference and one representative registry event showing the `Updater` value. The need is clear, but we cannot validate the required telemetry from the current nomination.

#### Reject / route elsewhere

Use when the request is not a detection-engineering need.

Examples:
- investigate this host;
- isolate this endpoint;
- block this IP;
- explain Sigma syntax for a training exercise.

Route it to the appropriate local owner rather than treating “reject” as “the problem does not matter.”

### A12 examples

**Nomination:**
> Need durable coverage for suspicious creation of HKCU Run values pointing into user-writable temporary paths. Evidence: A12 hunt package.

→ **Accept for work.**

**Nomination:**
> Need a detection for “something suspicious.” No case/report/hunt reference.

→ **Send back** for clearer need and evidence.

**Request:**
> Isolate `WS-JLEE`.

→ **Route to IR/containment owner**, not DE design work.

## 2. Knowledge Check

1. What two items are the minimum classroom bar for a reviewable nomination?
2. A hunt package states the need and contains representative evidence but no drafted rule. Accept or send back?
3. What is the difference between sending a nomination back and routing it elsewhere?

## 3. Summary

A nomination should be **clear enough to review**, not ready to deploy.

The nominator owes the defensive need and evidence/context. DE owns the engineering work that determines whether the right answer is a new analytic, a change, reuse of existing coverage, or no new rule.

**Next:** **4.4 – Tune Requests from SOC**.
