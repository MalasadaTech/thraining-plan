# Module 1.3.1 – SIGMA Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.1.1 A / B / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 1a / 2b / 3c  
- Hunter: 1.3.1.1 B / C / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 2b / 3c / 4c  
- CTI: 1.3.1.1 A / B / B ; 1.3.1.2 1a / 2b / 3c ; 1.3.1.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a SIGMA rule: purpose, structure, field tests (selectors), and how it becomes a SIEM query.
2. Describe what an existing rule detects, and say what a **basic** create or modify looks like.

**Mapped Proficiency Items:**
- K: 1.3.1.1 – SIGMA rules
- T: 1.3.1.2 – Analyze an existing SIGMA rule and describe what it detects
- T: 1.3.1.3 – Create or modify a basic SIGMA rule

---

## 1. Key Concepts

An alert comes from a **detection**. Someone wrote what to look for. SOC analysts **read** that write-up and **propose** a basic create or modify so detection engineering can review it. The shop may not all use the same SIEM, so **SIGMA** lets you write the idea once in YAML. A person or a converter turns it into that SIEM's query. You do **not** deploy the rule. How detections run as a service is **4.x**.

This lesson is SIGMA. It is not Suricata, YARA, or a saved SIEM rule (**1.3.2**–**1.3.4**).

**SIGMA** is a generic detection format. You write what to look for once. A converter or a person turns it into a SIEM query.

| Idea | What to read |
|------|----------------|
| **Purpose / structure** | `title`, `logsource` (which telemetry), `detection` (named selections plus a `condition`). Without those, it is not a detection. |
| **Fields / selectors** | Field tests: `endswith`, `contains`, a list, `re`. Field names must match the logsource. `Image` / `CommandLine` on `process_creation` are process-create fields (**1.1.2**). Tests in one selection are typically **and**. A list under one field is typically **or**. |
| **To SIEM** | `logsource` → table or event type. Selections → `where`. `condition` → and / or / not. Write that in words or a SIEM-shaped sentence. Running a converter is not this lesson. |

**What good looks like:**

- Analyze: name logsource, selectors, condition, and what would fire. Do not invent a Zeek field on a Windows process rule.
- Given:

```yaml
title: Encoded PowerShell from Script Host
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith: '\powershell.exe'
    CommandLine|contains: '-enc'
    ParentImage|endswith: '\wscript.exe'
  condition: selection
```

**What it detects:** process create — PowerShell with `-enc` and parent `wscript`. Same story as **1.1.2**. SIEM shape: `DeviceProcessEvents` / Sysmon 1, those three predicates.

- Modify / create: a **basic** rule with title, logsource, one selection, and a condition. Tightening “any `powershell.exe`” by adding parent or `-enc` is a modify. SOC **proposes**. Detection engineering reviews.

---

## 2. Knowledge Check

1. SIGMA is a SIEM product. True or false?
2. A `process_creation` rule matches `powershell.exe`, CommandLine `-enc`, and parent `wscript`. In one sentence, what does it detect?
3. Why is a rule that matches every `powershell.exe` a poor proposal?

---

## 3. Summary

SIGMA is portable YAML: logsource, selectors, condition. It becomes a SIEM query. You read it and propose a basic one. You do not deploy it.

**Next:** **1.3.2** Suricata rules.

---

## 4. Related modules

- 1.2.8 – Weird engine (previous)
- 1.1.2 – Process activity
- 1.3.2 – Suricata rules
- 1.3.4 – SIEM rules
- 4.x – How detections run as a service
