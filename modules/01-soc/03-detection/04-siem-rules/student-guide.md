# Module 1.3.4 – SIEM Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.4.1 A / B / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 1a / 2b / 3c  
- Hunter: 1.3.4.1 B / C / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 2b / 3c / 4c  
- CTI: 1.3.4.1 A / B / B ; 1.3.4.2 1a / 2b / 3c ; 1.3.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the pieces of a SIEM detection, and how log fields (or a SIGMA rule) become one.
2. Read an existing SIEM rule and say what it detects; propose a **basic** create from fields or from SIGMA.

**Mapped Proficiency Items:**
- K: 1.3.4.1 – SIEM rules
- T: 1.3.4.2 – Analyze an existing SIEM rule and describe what it detects
- T: 1.3.4.3 – Create a basic SIEM detection rule from log fields or a SIGMA rule

---

## 1. Key Concepts

SOC analysts **read** a saved detection and **propose** a basic one. **1.3.3** was YARA (bytes). This hour is the SIEM object that can create an **alert**. You do **not** deploy it. Opening the alert is **1.4**. How detections run as a service is **4.x**.

A **SIEM rule** (analytics / correlation search) runs on ingested logs.

| Idea | What to read |
|------|----------------|
| **Structure** | Name, **table**, **logic**, **window**, **output** fields. A table with no `where` is not a detection. A join or count in a window is correlation — optional for a basic rule |
| **Fields → detection** | Name the table. Pick fields you already know (`FileName`, `ProcessCommandLine`, `uri`, …). Add a parent, token, or dest so it is not “all PowerShell” |
| **Wildcards / regex** | Wildcard / `has` for a path or substring (`*\\Temp\\*`). Regex when the token actually varies (`-e` / `-enc` / `-EncodedCommand`). Do not regex an empty field into existence |

**From SIGMA (task 2, second path):** logsource → table, selectors → `where`, condition → boolean. Then name it, give it a window, list output fields. You are not required to run a converter.

**What good looks like:**

- Analyze: name table, logic, window, and what would fire.
- Given (from the **1.3.1** SIGMA):

```
Name: Encoded PowerShell from script host
Source: DeviceProcessEvents
Window: 5 minutes
Logic:
  FileName =~ "powershell.exe"
  and ProcessCommandLine has "-enc"
  and InitiatingProcessFileName == "wscript.exe"
Output: Timestamp, DeviceName, ProcessCommandLine, InitiatingProcessCommandLine
```

**What it detects:** the **1.1.2** process create. Mapped from SIGMA, not freehand.

- Create: a **basic** proposed rule from those fields **or** from that SIGMA. An unfiltered `DeviceProcessEvents` is not a create. SOC **proposes**. DE reviews.

---

## 2. Knowledge Check

1. A SIEM table with no filter is a detection. True or false?
2. The given rule above — what does it detect, in one sentence?
3. When do you use a wildcard instead of a regex?

---

## 3. Summary

A SIEM rule is named logic on a table, in a window, with outputs. Build it from fields you know, or translate SIGMA. You propose. You do not deploy. This closes **1.3**.

**Next:** **1.4.1** Alert context and investigation.

---

## 4. Related modules

- 1.3.3 – YARA rules (previous)
- 1.3.1 – SIGMA rules
- 1.4.1 – Alert context and investigation
- 4.x – How detections run as a service
