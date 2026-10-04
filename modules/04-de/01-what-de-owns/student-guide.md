# Module 4.1 – What Detection Engineering Owns

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.1 B / C / C ; 4.1.1 3c / 4c / 4c  
- SOC: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
- Hunter: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
- CTI: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain what Detection Engineering owns across the lifecycle of a detection.
2. Route a piece of work to **DE**, a **nominator**, **rule-authoring instruction (1.3)**, or the locally authorized **enforcement/control owner**.

**Mapped Proficiency Items:**
- K: 4.1 – What DE owns
- T: 4.1.1 – Sort work to DE, nominator, 1.3, or block/control owner

## 1. Key Concepts

Detection Engineering turns recurring defensive needs into **maintained detection capability**.

That is broader than writing a query. A detection only provides lasting value when someone owns what happens after the first draft: review, validation, deployment, tuning, change, health checks, and retirement.

For this course, DE owns the **detection lifecycle**:

- create or accept new detection work;
- change and tune existing detections;
- validate behavior and data requirements;
- deploy through the local process;
- maintain coverage as data and adversary behavior change;
- retire or replace detections that no longer provide value.

### Four adjacent kinds of work

| Work | Primary responsibility in this course |
|---|---|
| **Detection lifecycle** | DE evaluates, validates, deploys, maintains, changes, and retires detection logic. |
| **Nomination** | SOC, hunt, or CTI identifies a need and gives DE enough context to review it. |
| **Rule-authoring mechanics (1.3)** | How a Sigma, SIEM, IDS, YARA, or other rule is expressed and interpreted. |
| **Enforcement / blocking / containment** | The locally authorized owner of firewall, EDR-prevention, isolation, or other control action. |

The fourth boundary is an **operating-model decision**, not a universal law. Some organizations give DE authority over prevention controls; others separate detection from enforcement. In this course, treat a request such as “block this IP at the firewall” as an enforcement request and route it to the authorized control owner unless the local policy says DE owns that action.

### A nomination does not need to arrive production-ready

SOC, hunters, and CTI often see the defensive need before they know the final detection logic.

A useful nomination can begin as:

> We observed encoded PowerShell during A12 and want durable visibility for similar execution.

DE then evaluates:
- what behavior should be detected;
- which telemetry can support it;
- whether an existing analytic already covers it;
- what implementation and testing are required.

A rough nomination is not “bad DE work.” It is **input to DE work**.

### Detection Engineering is not only syntax

Module 1.3 teaches how a rule works.

The 4.x track is about **operating detections as a capability**:
- intake;
- design;
- validation;
- deployment;
- monitoring;
- tuning;
- lifecycle decisions;
- feedback to the nominator.

That distinction prevents the team from treating a syntactically valid query as a finished detection.

### A12 examples

**“We need durable detection for encoded PowerShell similar to A12.”**  
→ **Nomination / DE lifecycle work**

**“How do I express this condition in Sigma?”**  
→ **1.3 rule-authoring mechanics**

**“This live analytic is firing on our backup process.”**  
→ **DE tune/change work**

**“Block `203.0.113.88` at the firewall.”**  
→ **Enforcement/control-owner request under the course operating model**

## 2. Knowledge Check

1. Why is Detection Engineering broader than writing a rule?
2. A hunter sends a rough behavior description with hunt evidence but no rule. Is that enough to enter DE review?
3. Why should “block this IP” be routed according to the local control-ownership model rather than treated automatically as a DE deployment?

## 3. Summary

Detection Engineering owns **maintained detection capability**, not just rule syntax.

SOC, hunt, and CTI can nominate work before the final analytic exists. DE turns the need into a validated, deployable, maintainable detection—or explains why a new detection is not the right answer.

Enforcement actions follow the organization's control-ownership model.

**Next:** **4.2 – Making a Detection Sound and Meeting Shop Requirements**.
