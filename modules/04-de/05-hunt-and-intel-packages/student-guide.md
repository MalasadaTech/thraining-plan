# Module 4.5 – Hunt and Intel Packages

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.5 B / C / C ; 4.5.1 3c / 4c / 4d ; 4.5.2 3c / 4c / 4c  
- SOC: 4.5 A / A / B ; 4.5.1 1a / 1a / 2b ; 4.5.2 1a / 1a / 2b  
- Hunter: 4.5 A / B / B ; 4.5.1 1a / 2b / 3c ; 4.5.2 1a / 2b / 2b  
- CTI: 4.5 A / B / B ; 4.5.1 1a / 2b / 3c ; 4.5.2 1a / 2b / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Review a hunt or CTI package as engineering input and decide whether it supports **reuse**, **change**, **add**, or **no new rule**.
2. Separate durable detection opportunities from time-bounded indicators and enforcement/blocking actions.

**Mapped Proficiency Items:**
- K: 4.5 – Hunt and intel packages
- T: 4.5.1 – Review a package: one add, one change, or no new rule
- T: 4.5.2 – Reject turning the package into a block list

## 1. Key Concepts

A hunt or CTI package is evidence and analysis that can inform Detection Engineering.

It is **not automatically a finished detection**.

DE's first question should be:

> What durable defensive capability, if any, does this package justify?

### Start with existing coverage

Before creating a new analytic, determine whether the need is already covered.

Possible outcomes:

1. **Reuse existing coverage** – the package maps to an analytic that already addresses the behavior.
2. **Change existing coverage** – a live analytic is close but needs improvement.
3. **Add new coverage** – a meaningful gap exists and a new analytic is justified.
4. **No new rule** – the package is useful but does not justify a detection change.

The original task mapping groups this as add/change/no-new-rule; **reuse** is the check that can lead to “no new rule” because coverage already exists.

### Package evidence can include several layers

A package may contain:
- observed procedures;
- ATT&CK techniques;
- IOCs;
- behavioral artifacts;
- affected platforms;
- scope and timing;
- hunt findings;
- known visibility gaps;
- supporting sources.

DE should use the **behavioral and environmental context**, not only the IOC list.

### Exact indicators can be useful without being durable

A hash, domain, IP, or URL can support:
- retrospective search;
- short-lived monitoring;
- correlation;
- an enforcement action by the appropriate control owner.

But an exact IOC is not automatically a durable detection.

Ask:
- How long is this indicator likely to remain useful?
- Can the adversary rotate it easily?
- Does it reveal a more durable procedure?
- Is an existing behavioral analytic already stronger?

For A12, `203.0.113.88` may be useful as evidence or short-term context. A behavioral analytic around suspicious encoded PowerShell or unusual user-level autorun creation may survive infrastructure rotation better.

### Do not turn the whole infrastructure set into a detection or block list

A package may contain candidate related infrastructure.

That does not mean:
- every related IP/domain should become a detection rule;
- every candidate should be blocked;
- a shared cloud range should be treated as malicious.

Enforcement decisions go through the locally authorized control process.

Detection Engineering should focus on what the package says about **detectable behavior and defensible context**.

### Feedback to the package producer

A useful DE response can say:

> **Change existing coverage:** The package's Run-key procedure is partially covered, but the current analytic does not distinguish user-writable payload paths. We will test a change around that behavioral condition. Exact infrastructure remains short-lived context rather than the primary detection logic.

That closes the loop and explains what DE learned from the package.

## 2. Knowledge Check

1. Why should DE check existing coverage before creating a new rule?
2. Does an exact IOC automatically deserve a durable detection?
3. A package contains a broad shared-hosting `/24`. Should DE convert the whole range into a detection or block list?

## 3. Summary

Treat hunt and CTI packages as **engineering input**.

Start with existing coverage, then decide whether to reuse, change, add, or make no detection change.

Use exact indicators when they are operationally useful, but prefer durable behavior when the evidence supports it. Enforcement/blocking follows the local control process.

**Next:** **4.6 – Detection Lifecycle**.
