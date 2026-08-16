# Module 1.1.4 – Registry Activity

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.4.1 A / B / C · 1.1.4.2 2b / 3c / 4c · 1.1.4.3 2b / 3c / 4c  
- Hunter: 1.1.4.1 A / B / B · 1.1.4.2 1a / 2b / 3c · 1.1.4.3 1a / 2b / 3c  
- CTI: 1.1.4.1 A / A / A · 1.1.4.2 1a / 1a / 1a · 1.1.4.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain registry hives, key → value, set / delete / rename, initiating process, and how Run / Services appear as examples.
2. Analyze a Sysmon or MDE registry event and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* registry operation — not “all registry events.”

**Mapped Proficiency Items:**
- K: 1.1.4.1 – Registry activity concepts
- T: 1.1.4.2 – Analyze a registry event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.4.3 – Create a SIEM query to detect specific registry operations

---

## 1. Key Concepts

### 1.1 What a registry event is

**Registry activity** is host telemetry about the Windows registry: a **key or value** was **created/set**, **deleted**, or **renamed**.

This unit is **endpoint** telemetry (Sysmon / Microsoft Defender for Endpoint). It is **not** Zeek (**1.2**). It is **not** how to install or configure Sysmon. It is **not** a persistence-technique catalog (**2.6**). Process, file, and host-network rows are **1.1.1–1.1.3**.

| This lesson | Later |
|-------------|-------|
| What happened to which key/value, by which process | Image / driver load (**1.1.5**) |
| Run and Services as **locations you will see** | Persistence *how-to* and hunt techniques (**2.6.1**) |
| Sysmon Event IDs and MDE table names as they appear in a SIEM | Sysmon XML / deployment |

**Most critical distinction for daily work:**  
A registry event is **what changed in the registry, by whom**. A file drop or a process start is a different row. Seeing a Run key is not by itself a finished persistence hunt.

If a field is empty in your tenant (no value data, no old name), say so. Do not invent it.

### 1.2 Hives, operations, example locations, and how it is logged

| Idea | What to read | Why it matters |
|------|----------------|----------------|
| **Hive and key → value** | Hive (`HKLM` / `HKCU` / `\REGISTRY\MACHINE\` / `\REGISTRY\USER\`); key path; value name; value data | The hive is the tree. The key is the folder. The value is the named slot. Data is what was written. |
| **Set** | Sysmon **13** (`SetValue`); MDE `RegistryValueSet` / `RegistryKeyCreated` | Something was written. Most common registry row you will describe. |
| **Delete** | Sysmon **12** (`DeleteKey`); MDE `RegistryKeyDeleted` / `RegistryValueDeleted` | The key or value is gone. |
| **Rename** | Sysmon **14** (`RenameKey` / `RenameValue`); MDE `RegistryKeyRenamed` / `RegistryValueRenamed` | Same object, new name. Read old vs new. |
| **Example locations** | Run / RunOnce; `...\Services\<name>` | Places that *often* matter. Examples only — the hunt catalog is **2.6**. |
| **Initiating process** | Sysmon `Image`; MDE `InitiatingProcess*` | Who performed the registry operation. |

**Hives (outline a).** Analysts see both the friendly names and the native prefixes:

| Friendly | Common native prefix |
|----------|----------------------|
| `HKLM` | `\REGISTRY\MACHINE\` |
| `HKCU` (that user’s) | `\REGISTRY\USER\<SID>\` |
| `HKU` | `\REGISTRY\USER\` |
| `HKCR` | `\REGISTRY\MACHINE\SOFTWARE\Classes\` (and user Classes) |

A **key** is the path. A **value** is a name under that key plus **data**. Sysmon **13** puts the data in `Details`. MDE uses `RegistryKey`, `RegistryValueName`, `RegistryValueData`.

**How this shows up (outline e)**

| Source | Events / table | Key fields |
|--------|----------------|------------|
| Sysmon | **12** CreateKey / DeleteKey, **13** SetValue, **14** RenameKey / RenameValue | `EventType`, `Image`, `TargetObject`, `Details` (13), `NewName` (14), `User` |
| MDE | `DeviceRegistryEvents` | `ActionType`, `RegistryKey`, `RegistryValueName`, `RegistryValueData`, `InitiatingProcess*`, Previous* on rename |

MDE registry rows use **initiating** process = who changed the registry. Sysmon uses `Image` / `TargetObject`. Same story, different names.

**Common locations as examples (outline c) — not 2.6:**

| Location (examples) | Why you will see it on a row |
|---------------------|------------------------------|
| `...\Windows\CurrentVersion\Run` and `RunOnce` (`HKCU` or `HKLM`) | A value here names a program that runs at logon. Describe the set/delete. Persistence *technique* is **2.6.1**. |
| `HKLM\SYSTEM\CurrentControlSet\Services\<name>` | Service configuration lives here. A create/set by an unexpected process is a lead to describe, not a services-hunt lecture. |

Software also writes thousands of other keys (MRU, user prefs, COM). Those can be expected.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Explorer / Settings / the app itself writing its own preference key | `powershell.exe` / `wscript.exe` / Office `SetValue` under Run / RunOnce |
| Installer (`msiexec.exe`) writing `Services\<product>` during an install you know about | User-writable process creating `Services\<name>` or setting `ImagePath` |
| Delete of a value the same app created | Unexpected initiator deleting a Run value or a service key |
| Rename inside an app’s own key | Rename that hides a Run value or a service name |

**Initiating process:** On a registry row, `InitiatingProcess*` / `Image` is **who changed the key**. It is not a process-create parent and not a file create.

Stay on the registry row. Do not inventory every persistence method. That is **2.6**.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (User Preference Set)

**MDE `DeviceRegistryEvents` (`RegistryValueSet`)**

| Field | Value |
|-------|--------|
| ActionType | `RegistryValueSet` |
| RegistryKey | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced` |
| RegistryValueName | `Hidden` |
| RegistryValueData | `1` |
| InitiatingProcessFileName | `explorer.exe` |
| InitiatingProcessFolderPath | `C:\Windows\` |
| AccountName | `jlee` |

**What occurred:** Explorer set a user Explorer preference under HKCU. Initiator and key agree. Expected.

**Not done:** Did not call it persistence. Did not hunt Run keys. Did not rewrite this as a process-create lesson (**1.1.1**).

### Example 2: PowerShell Sets HKCU Run (Lead)

**Sysmon Event ID 13 (SetValue)**

| Field | Value |
|-------|--------|
| EventType | `SetValue` |
| Image | `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` |
| TargetObject | `\REGISTRY\USER\S-1-5-21-…-1105\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Updater` |
| Details | `C:\Users\jlee\AppData\Local\Temp\update.exe` |
| User | `BUILDINGC\jlee` |

Compare a file row that is *not* this event:

> Sysmon **11**: `wscript.exe` created `C:\Users\jlee\AppData\Local\Temp\update.exe`. That is a **file create** (**1.1.2**). This row is the **registry set**.

**What occurred:** `powershell.exe` **set** HKCU Run value `Updater` to a Temp `.exe`. Hive is that user’s (`\REGISTRY\USER\...`). The file create is a different event.

**Interpretation:** Lead, not an automatic incident. Describe set + key + value data + initiator. Name Run as a **location**. Do not deliver the **2.6.1** persistence catalog. Do not pivot into Zeek.

### Example 3: Unexpected Service Key Create (Lead)

**Sysmon Event ID 12 (CreateKey)** plus a rename compare

| Field | Value |
|-------|--------|
| EventType | `CreateKey` |
| Image | `C:\Users\jlee\AppData\Local\Temp\helpdesk.exe` |
| TargetObject | `\REGISTRY\MACHINE\SYSTEM\CurrentControlSet\Services\HelpdeskSvc` |
| User | `BUILDINGC\jlee` |

Compare a rename that is *not* a create:

> Sysmon **14** `RenameValue`: same `helpdesk.exe`, `TargetObject` `...\Run\Updater`, `NewName` `OneDrive`. That is a **rename**, not a set and not a create.

**What occurred:** A user-writable `helpdesk.exe` **created** a service key under HKLM `Services`. That is Event **12**, not a SetValue. The Event **14** is a separate **rename** of a Run value.

**Interpretation:** Lead. Name CreateKey vs RenameValue. Services and Run are example locations. Do not teach service persistence methodology (**2.6.1**). Do not call it privilege escalation without an elevation story (**2.6.2**).

---

## 3. Hands-On Exercise

**Objective:** Practice describing registry events and writing queries that find a specific operation.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (set, delete, or rename; expected vs lead).
2. For each item below, say **create**, **set**, **delete**, **rename**, or **not a registry event**. Give one reason.
   - Sysmon 13: `powershell.exe` SetValue on HKCU `...\Run\Updater`
   - Sysmon 12: `helpdesk.exe` CreateKey under `...\Services\HelpdeskSvc`
   - Sysmon 14: `helpdesk.exe` RenameValue `Run\Updater` → `OneDrive`
   - MDE `DeviceRegistryEvents` `RegistryValueSet`: `explorer.exe` → `Explorer\Advanced\Hidden`
   - MDE `DeviceFileEvents` `FileCreated` of `update.exe` under Temp
   - Zeek `conn` row to 443
3. Write **two SIEM-style pseudo-queries**:
   - One for **script-host, Office, or PowerShell** **setting** a value under `Run` or `RunOnce` (use initiator + key path).
   - One for **create or set** under `...\Services\` where the initiating process is **not** under `C:\Windows\` or `C:\Program Files\`.
4. Write **one analysis card** (small table or four sentences) for Example 2 *or* Example 3: action type, hive/key/value, initiating process, expected vs lead. Do not install Sysmon. Do not write a 2.6 hunt plan.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- Two specific registry queries (not `DeviceRegistryEvents` with no filter)
- One card that describes *this* event, not a slogan

---

## 4. Knowledge Check

1. What is the difference between a registry **set**, a **delete**, and a **rename**? Which Sysmon Event IDs map to each?
2. What is a **hive**, a **key**, and a **value**? How do `\REGISTRY\MACHINE\` and `\REGISTRY\USER\` relate to `HKLM` / `HKCU`?
3. On MDE `DeviceRegistryEvents`, what do `InitiatingProcess*` fields represent?
4. Why do we treat Run and Services as **examples** in this lesson rather than a persistence course?
5. Sysmon 13 `Details` is empty. What do you write, and what do you still use?

---

## 5. Summary

- Registry activity = set, delete, or rename of a key or value — on the **host**.
- Read hive, key, value name, value data if present, and initiating process.
- Sysmon **12 / 13 / 14** and MDE `DeviceRegistryEvents` are the same story in different shapes.
- Event 13 is SetValue. Event 12 is create/delete of a key. Event 14 is rename.
- Run and Services are locations you will see. Persistence techniques are **2.6**.
- Next: image and driver load (**1.1.5**).

---

## 6. References & Further Reading

- Related modules:
  - 1.1.1 – Process activity
  - 1.1.2 – File system activity
  - 1.1.3 – Network activity (endpoint) (previous)
  - 1.1.5 – Image and driver load (next)
  - 2.6.1 – Persistence techniques
- Local Sysmon / MDE field guide used in class (optional)
- Sysmon Event ID reference (12 / 13 / 14) and MDE `DeviceRegistryEvents` schema — as deployed, not as a config lesson
