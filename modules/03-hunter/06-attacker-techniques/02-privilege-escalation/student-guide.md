# Module 3.6.2 – Privilege Escalation Techniques

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.2 B / C / C ; 3.6.2.1 3c / 4c / 4c  
- SOC: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
- CTI: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Recognize evidence that a process or actor obtained a higher security context than it previously had.
2. Distinguish the **elevation outcome** from the specific technique used to achieve it.

## Mapped Proficiency Items

- K: 3.6.2 – Privilege escalation techniques
- T: 3.6.2.1 – Recognize privilege escalation techniques in logs or telemetry

## 1. Key Concepts

Privilege escalation occurs when an actor obtains a higher level of effective privilege than the context it previously controlled.

Seeing a process run as **SYSTEM** may establish an elevated outcome. It does **not automatically tell you how the elevation happened**.

That method/evidence distinction is the core of this lesson.

### UAC bypass

MITRE ATT&CK: [T1548.002 – Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002/)

Evidence should support the bypass mechanism—for example:

- use of an auto-elevated component;
- associated registry/protocol/COM abuse or other known bypass mechanism;
- high-integrity child/result;
- absence of normal consent where that matters to the technique.

`fodhelper.exe` followed by an elevated child can be suspicious, but the process name alone is not enough to prove a UAC bypass.

### Access Token Manipulation

MITRE ATT&CK: [T1134 – Access Token Manipulation](https://attack.mitre.org/techniques/T1134/)

Useful evidence can include:

- token duplication or impersonation operations from EDR/API telemetry;
- source and target security contexts;
- creation of a process using a manipulated token;
- linkage to a privileged token source.

A user process followed by a SYSTEM child does **not by itself prove token theft**. It proves that the child ran in a higher context; the method remains unresolved until token-manipulation evidence supports it.

### Windows Service abuse

MITRE ATT&CK: [T1543.003 – Windows Service](https://attack.mitre.org/techniques/T1543/003/)

Services can execute as SYSTEM. If an adversary with sufficient rights creates/modifies a service and uses it to move from a lower effective context to SYSTEM, the service activity can contribute to privilege escalation.

Preserve:
- who created/modified it;
- image path;
- service account;
- resulting process context.

### Exploitation for Privilege Escalation

MITRE ATT&CK: [T1068 – Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)

Evidence should connect:
- vulnerable component/driver or exploit behavior;
- exploitation activity;
- resulting higher privilege.

A SYSTEM process appearing after a crash or driver load is not enough by itself to name a specific exploit.

### Outcome first, method second

A useful analytic sequence is:

1. What was the original security context?
2. What higher context appeared?
3. What telemetry explains **how** the transition occurred?
4. Is the technique specific enough to name, or is the method unresolved?

### A12 boundary

The A12 HKCU Run value is evidence of user-context persistence. It does not establish a privilege change.

## 2. Knowledge Check

1. A user-context process launches a SYSTEM child. What can you say immediately, and what remains unresolved?
2. What additional evidence would help support Access Token Manipulation?
3. Why is `fodhelper.exe` alone insufficient to prove UAC bypass?

## 3. Summary

Recognize the privilege change, then require method-specific evidence before naming the escalation technique.

High privilege is an **outcome**. Token manipulation, UAC bypass, service abuse, and exploitation are **methods**.

**Next:** **3.6.3 – Hunt for a Specific Persistence or Privilege-Escalation Technique**.

## Supporting References

- [T1548.002 – Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002/)
- [T1134 – Access Token Manipulation](https://attack.mitre.org/techniques/T1134/)
- [T1543.003 – Windows Service](https://attack.mitre.org/techniques/T1543/003/)
- [T1068 – Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)
