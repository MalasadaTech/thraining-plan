# Module 3.5.1 – Using MITRE ATT&CK for Hunt Planning

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 3c / 4c / 4d  
- SOC: 3.5.1 A / B / B ; 3.5.1.1–3.5.1.2 1a / 2b / 3c ; 3.5.1.3 1a / 1a / 2b  
- CTI: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Map the behavior a hunt will test—or has found—to the most specific ATT&CK technique/sub-technique supported by evidence.
2. Use that mapping to describe detection/visibility gaps and support hunt priority without treating ATT&CK as a scoring system.

## Mapped Proficiency Items

- K: 3.5.1 – Using MITRE ATT&CK for hunt planning and coverage analysis
- T: 3.5.1.1 – Map a hunt plan or hunt findings to MITRE ATT&CK
- T: 3.5.1.2 – Use ATT&CK to identify detection or visibility gaps
- T: 3.5.1.3 – Use ATT&CK to support hunt prioritization

## 1. Key Concepts

ATT&CK gives the hunt a shared behavioral vocabulary.

Reference: [MITRE ATT&CK](https://attack.mitre.org/)

### Map the behavior this hunt is testing

Do not map every technique associated with a named actor.

Map:

> the procedure or behavior this hunt is searching for

to:

> the most specific ATT&CK technique/sub-technique the evidence supports.

### Technique and tactic are related but not identical

One ATT&CK technique can support more than one tactic.

For example, [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/) is currently associated with both **Persistence** and **Privilege Escalation**.

The A12 HKCU Run value executes in the logged-on user's context. In that scenario, the supported use is **Persistence**. Nothing in the Run-key observation by itself establishes higher privileges.

So the hunt mapping is:

> **Persistence / T1547.001 – Registry Run Keys / Startup Folder**

The same technique could support a different tactic in another context when the evidence demonstrates that role.

### Use ATT&CK for coverage analysis

After mapping the hunt, ask:

**Visibility**
> Do we collect telemetry that can observe this procedure on the in-scope systems?

**Detection**
> If the telemetry exists, does an analytic meaningfully cover the behavior?

Examples:

- registry data absent on a host class → **visibility gap**;
- registry data present but no analytic covers suspicious Run-key changes → **detection gap**.

### ATT&CK supports priority; it does not determine it

Hunt priority also depends on:

- active incident/mission relevance;
- strength and freshness of the lead;
- local applicability;
- visibility;
- current detection coverage;
- expected defensive value;
- analyst/search cost.

A technique being mapped to Persistence does not make it automatically higher priority than another hunt.

## 2. Knowledge Check

1. Why should you map the behavior being hunted instead of every technique associated with an actor?
2. T1547.001 is associated with more than one tactic. Why is **Persistence** the relevant tactic for the A12 HKCU Run example?
3. Registry telemetry exists but no analytic covers suspicious Run-key changes. Which gap is that?

## 3. Summary

Map the hunt's **actual behavior** to ATT&CK.

Use context to choose the relevant tactic when a technique spans more than one. Then use the mapping to reason about visibility and detection coverage.

ATT&CK informs priority; it does not replace operational judgment.

**Next:** **3.6.1 – Persistence Techniques**.

## Supporting References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)
