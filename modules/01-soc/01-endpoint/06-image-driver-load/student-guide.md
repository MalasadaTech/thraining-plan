# Module 1.1.6 – Image and Driver Load Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.6.1 A / B / C ; 1.1.6.2 2b / 3c / 4c ; 1.1.6.3 2b / 3c / 4c  
- Hunter: 1.1.6.1 A / B / B ; 1.1.6.2 1a / 2b / 3c ; 1.1.6.3 1a / 2b / 3c  
- CTI: 1.1.6.1 A / A / A ; 1.1.6.2 1a / 1a / 1a ; 1.1.6.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a load row: user-mode image vs kernel driver, path, hash, signed vs unsigned (where logged), and who loaded it.
2. Describe what a Sysmon or MDE image or driver load event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.6.1 – Image and driver load activity concepts
- T: 1.1.6.2 – Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.6.3 – Create a SIEM query to detect specific image or driver load activity

---

## 1. Key Concepts

SOC analysts read **host** load rows to see that a module entered a process, or that a driver entered the kernel. **1.1.5** was the registry row. This hour is the **load** row — last child in **1.1**. It is **not** a file create (**1.1.3**). It is **not** a process create (**1.1.2**). It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Image and driver load activity** is endpoint telemetry that a **user-mode image** (usually a DLL) was mapped into a process, or that a **kernel driver** was loaded.

| Idea | What to read |
|------|----------------|
| **User-mode vs kernel** | User-mode = a process loaded a module (Sysmon **7** / MDE). Kernel = a driver entered the kernel (Sysmon **6**). Not a process start. |
| **Path, hashes, signed vs unsigned** | Path is where it loaded from. SHA256 is the loaded bytes when present. `Signed` / signature fields **where logged**. Empty ≠ unsigned. |
| **Initiating process** | Sysmon 7 `Image`; MDE `InitiatingProcess*`. Which process loaded the module. Event **6** is kernel-wide — do not invent a user-mode parent. |

**How this shows up:** Sysmon **6** (driver) / **7** (image load); MDE `DeviceImageLoadEvents`. Same story, different names. Event **7** is noisy and often sampled or off. If you have no 7 / no `DeviceImageLoadEvents`, write “image load not logged.” Do not invent a load from a file-create row.

MDE `ActionType` on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **ImageLoaded** | A process loaded a module | Event **7** |

Driver load on the endpoint is Sysmon **6**. The full MDE `ActionType` set is in the Defender portal schema. Do not invent a value.

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — what was loaded, into whom (or into the kernel), from where, signed or not if logged. Do not jump to a file create (**1.1.3**) or a persistence / BYOVD lecture (**2.6**).
- Given: Sysmon **7**, `Image` `powershell.exe`, `ImageLoaded` Temp `update.dll`, `Signed=false`. **What occurred:** PowerShell loaded an unsigned DLL from Temp. The file create of that DLL, if you have one, is a different row.
- Query: names a **specific** pattern (path or loader + `.dll` / `.sys`), not “all image loads.”

This closes **1.1**. Protocol deep-dive is **1.2**.

---

## 2. Knowledge Check

1. Sysmon Event 6 is a DLL load into a process. True or false?
2. `powershell.exe` loads Temp `update.dll` (`Signed=false`). In one sentence, what occurred?
3. A SIEM query that matches every `DeviceImageLoadEvents` row is a good “specific image or driver load” query. True or false?

---

## 3. Summary

A load row is a module entering a process, or a driver entering the kernel. Path and initiator tell the story. Signed empty is a gap. A file create is not a load. A query names a specific pattern.

**Next:** **1.2.1** Zeek concepts.

---

## 4. Related modules

- 1.1.5 – Registry activity (previous)
- 1.2.1 – Zeek concepts
- 1.1.3 – File system activity
- 2.6 – Persistence techniques (later)
