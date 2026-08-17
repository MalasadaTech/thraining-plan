# Module 1.1.2 – Process Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.2.1 A / B / C ; 1.1.2.2 2b / 3c / 4c ; 1.1.2.3 2b / 3c / 4c  
- Hunter: 1.1.2.1 A / B / B ; 1.1.2.2 1a / 2b / 3c ; 1.1.2.3 1a / 2b / 3c  
- CTI: 1.1.2.1 A / A / A ; 1.1.2.2 1a / 1a / 1a ; 1.1.2.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a process row: create / terminate, parent-child, command line, user, hashes, and process access.
2. Describe what a Sysmon or MDE process event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.2.1 – Process activity concepts
- T: 1.1.2.2 – Analyze a process event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.2.3 – Create a SIEM query to detect specific process activity

---

## 1. Key Concepts

SOC analysts read **host** process rows to see who ran what. **1.1.1** was the map. This hour is the **process** row. It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Process activity** is endpoint telemetry about a running program: it **started**, it **ended**, or one process **touched** another.

| Idea | What to read |
|------|----------------|
| **Create / terminate** | Sysmon **1** / **5**. MDE create is `ActionType` **ProcessCreated**. Terminate is Sysmon 5 — do not assume `ProcessTerminated` on this table. |
| **PID, name, command line** | `ProcessId`, image/name, `CommandLine` / `ProcessCommandLine`. Name can lie. Command line is often the story. |
| **Parent-child** | PPID, parent name, parent command line; MDE `InitiatingProcess*` |
| **Integrity / user** | Integrity level; `User` / account (where logged). Empty is a gap, not “not admin.” |
| **Hash / original filename** | SHA256; `OriginalFileName` (PE resource — can disagree with the on-disk name) |
| **Process access** | Sysmon **10**: source → target (who touched whom). Not a create. |

**How this shows up:** Sysmon **1** / **5** / **10**; MDE `DeviceProcessEvents` (`ActionType`, `InitiatingProcess*`, `ProcessCommandLine`, SHA256). MDE **initiating** process = parent. Same story, different names.

MDE `ActionType` values on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **ProcessCreated** | A process launched | Event **1** |
| **OpenProcess** | A process opened a handle to another (who touched whom) | Event **10** |

The full set is in the Defender portal schema. Do not invent a value. **Terminate** is Sysmon **5**. Do not assume a `ProcessTerminated` row in `DeviceProcessEvents`.

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — who ran what, from whom, as whom. Create, terminate, or access. Do not jump to file, DNS, or registry (**1.1.3**–**1.1.5**).
- Given: `wscript.exe` (Temp `invoice.vbs`) → `powershell.exe -enc …` as `jlee`. **What occurred:** script host launched hidden encoded PowerShell. The hash of `powershell.exe` can still be fine. The parent + command line is the story.
- Query: names a **specific** pattern (parent + command-line fragment), not “all processes.”

File, host-network, registry, and image-load rows are the next **1.1** lessons.

---

## 2. Knowledge Check

1. Sysmon Event 10 is a process start. True or false?
2. `wscript.exe` (Temp `.vbs`) creates `powershell.exe -enc …`. In one sentence, what occurred?
3. A SIEM query that matches every process is a good “specific process activity” query. True or false?

---

## 3. Summary

A process row is who ran what, from whom, as whom. Create, terminate, or access. Command line and parent tell the story. A query names a specific pattern.

**Next:** **1.1.3** File system activity.

---

## 4. Related modules

- 1.1.1 – Endpoint activity (the map)
- 1.1.3 – File system activity
- 1.1.4 – Network activity (endpoint)
- 1.2 – Zeek
