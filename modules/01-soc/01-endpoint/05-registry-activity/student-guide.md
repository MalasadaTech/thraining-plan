# Module 1.1.5 – Registry Activity

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.5.1 A / B / C ; 1.1.5.2 2b / 3c / 4c ; 1.1.5.3 2b / 3c / 4c  
- Hunter: 1.1.5.1 A / B / B ; 1.1.5.2 1a / 2b / 3c ; 1.1.5.3 1a / 2b / 3c  
- CTI: 1.1.5.1 A / A / A ; 1.1.5.2 1a / 1a / 1a ; 1.1.5.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a registry row: hive, key → value, set / delete / rename, and who changed it.
2. Describe what a Sysmon or MDE registry event shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.1.5.1 – Registry activity concepts
- T: 1.1.5.2 – Analyze a registry event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.5.3 – Create a SIEM query to detect specific registry operations

---

## 1. Key Concepts

SOC analysts read **host** registry rows to see what changed in the registry, and by which process. **1.1.4** was the host-network row. This hour is the **registry** row. It is **not** a persistence catalog (**2.6**). It is **not** Zeek (**1.2**). It is **not** how to install Sysmon.

**Registry activity** is endpoint telemetry about a **key or value** that was **set**, **deleted**, or **renamed**.

| Idea | What to read |
|------|----------------|
| **Hive and key → value** | Hive (`HKLM` / `HKCU`, or `\REGISTRY\MACHINE\` / `\REGISTRY\USER\`). The **key** is the path. The **value** is the named slot plus **data**. |
| **Set / delete / rename** | Set = something was written. Delete = it is gone. Rename = same object, new name. |
| **Example locations** | Run / RunOnce; `...\Services\<name>`. Places you will see. Not a **2.6** dump. |
| **Initiating process** | Sysmon `Image`; MDE `InitiatingProcess*`. Who changed the key. Not a process-create write-up (**1.1.2**). |

**How this shows up:** Sysmon **12** (create/delete key), **13** (SetValue), **14** (rename); MDE `DeviceRegistryEvents`. Same story, different names.

MDE `ActionType` values you will use on **this** table:

| `ActionType` | What it is | Sysmon cousin |
|--------------|------------|---------------|
| **RegistryValueSet** / **RegistryKeyCreated** | Something was written or a key appeared | Event **13** / **12** |
| **RegistryKeyDeleted** / **RegistryValueDeleted** | It is gone | Event **12** |
| **RegistryKeyRenamed** / **RegistryValueRenamed** | Same object, new name | Event **14** |

The full set is in the Defender portal schema. Do not invent a value. If value data is empty, write “data not logged,” not “empty on purpose.”

If a field is empty in your tenant, say so. Do not invent it.

**What good looks like:**

- Describe: one sentence — what happened to which key/value, by whom. Set, delete, or rename. Name Run or Services as a **location** if that is where it sat. Do not deliver a persistence hunt (**2.6**).
- Given: Sysmon **13**, `powershell.exe`, `\REGISTRY\USER\…\Run\Updater` = Temp `update.exe`. **What occurred:** PowerShell set HKCU Run value `Updater` to that Temp path. The file create of `update.exe` is a different row (**1.1.3**).
- Query: names a **specific** pattern (initiator + key path), not “all registry events.”

Image and driver load is the last **1.1** child.

---

## 2. Knowledge Check

1. A Run-key row is a finished persistence hunt. True or false?
2. `powershell.exe` SetValue on HKCU `Run\Updater` = Temp `update.exe`. In one sentence, what occurred?
3. A SIEM query that matches every `DeviceRegistryEvents` row is a good “specific registry operation” query. True or false?

---

## 3. Summary

A registry row is what changed in the hive, by whom. Key, value, and initiator tell the story. Run and Services are locations, not a hunt course. A query names a specific pattern.

**Next:** **1.1.6** Image and driver load.

---

## 4. Related modules

- 1.1.4 – Network activity (endpoint) (previous)
- 1.1.6 – Image and driver load
- 1.1.3 – File system activity
- 2.6 – Persistence techniques (later)
