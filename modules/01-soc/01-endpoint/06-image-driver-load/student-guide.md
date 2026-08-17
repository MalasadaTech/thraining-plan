# Module 1.1.6 – Image and Driver Load Activity

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.6.1 A / B / C · 1.1.6.2 2b / 3c / 4c · 1.1.6.3 2b / 3c / 4c  
- Hunter: 1.1.6.1 A / B / B · 1.1.6.2 1a / 2b / 3c · 1.1.6.3 1a / 2b / 3c  
- CTI: 1.1.6.1 A / A / A · 1.1.6.2 1a / 1a / 1a · 1.1.6.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain user-mode image load vs kernel driver load, plus path, hashes, signed vs unsigned (where logged), and initiating process.
2. Analyze a Sysmon or MDE image or driver load event and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* image or driver load pattern — not “all image loads.”

**Mapped Proficiency Items:**
- K: 1.1.6.1 – Image and driver load activity concepts
- T: 1.1.6.2 – Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.6.3 – Create a SIEM query to detect specific image or driver load activity

---

## 1. Key Concepts

### 1.1 What an image or driver load event is

**Image and driver load activity** is host telemetry that a **module was mapped into a process** (user-mode image, usually a DLL) or that a **kernel driver** was loaded.

This unit is **endpoint** telemetry (Sysmon / Microsoft Defender for Endpoint). It is **not** Zeek (**1.2**). It is **not** how to install or configure Sysmon. It is **not** a file-create row (**1.1.3**) and **not** a process-create row (**1.1.2**). A DLL can be created in one event and loaded in another.

| This lesson | Later / other |
|-------------|---------------|
| What was loaded, into whom, signed or not (where logged) | Persistence / BYOVD *how-to* (**2.6**) |
| Sysmon Event IDs and MDE table names as they appear in a SIEM | Sysmon XML / “should we enable Event 7?” |
| Path, hash, signature fields on the load row | Registry (**1.1.5**) already taught |

**Most critical distinction for daily work:**  
A load event is **this image entered that process (or the kernel)**. A file create of the same `.dll` / `.sys` is a different row.

If a field is empty in your tenant (no Signed, no hash, no Event 7), say so. Do not invent it.

### 1.2 User-mode vs driver, path/hash/signature, initiator, and how it is logged

| Idea | What to read | Why it matters |
|------|----------------|----------------|
| **User-mode image load** | Sysmon **7**; MDE `DeviceImageLoadEvents` | A process loaded a module (almost always a DLL). High volume when logged. |
| **Kernel driver load** | Sysmon **6** | A driver (`.sys`) entered the kernel. Not “a process started.” |
| **Path** | Sysmon `ImageLoaded`; MDE `FolderPath` + `FileName` | `Program Files` vs `Temp` / `AppData` is half the story. Name can lie. |
| **Hash** | SHA256 (and MD5/SHA1 if present) | Bytes of the **loaded** image, when present. Empty ≠ clean. |
| **Signed vs unsigned** | Sysmon `Signed` / `Signature` / `SignatureStatus`; MDE signature fields **where logged** | Unsigned in a user-writable path is a lead. Empty signature field = “not logged.” |
| **Initiating process** | Sysmon 7 `Image` (the loading process); MDE `InitiatingProcess*` | Who loaded the user-mode image. Event **6** is kernel-wide — there is no user-mode parent in the same sense. |

**How this shows up (outline d)**

| Source | Events / table | Key fields |
|--------|----------------|------------|
| Sysmon | **6** Driver loaded; **7** Image loaded | **6:** `ImageLoaded`, `Hashes`, `Signed`, `Signature`, `SignatureStatus`. **7:** `Image` (process), `ImageLoaded` (module), hashes, signature fields |
| MDE | `DeviceImageLoadEvents` | `ActionType` (typically `ImageLoaded`), `FolderPath`, `FileName`, SHA256, `InitiatingProcess*`, signature fields when the tenant has them |

MDE image-load rows use **initiating** process = the process that loaded the module and **FileName / FolderPath** = what was loaded. Sysmon 7 uses `Image` / `ImageLoaded`. Same story, different names.

Event **7** is noisy. Many tenants log it only for some processes, or not at all. If you have no 7 / no `DeviceImageLoadEvents`, write “image load not logged” — do not invent a load from a file-create row.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| `WINWORD.EXE` loads a signed Office DLL from `Program Files` | Office / `powershell.exe` / script host loads a DLL from `Temp` or `AppData` |
| Signed driver from `C:\Windows\System32\drivers\` | Driver from a user-writable path, or `Signed=false` (where logged) |
| Hash matches a catalogued Office / Windows module | Hash unknown **and** unexpected path |
| Signature fields present and valid | Signature fields empty — say so — plus a bad path |

**User-mode vs kernel:** Event **7** / `DeviceImageLoadEvents` = a **process** loaded a module. Event **6** = the **kernel** loaded a driver. Do not call Event 6 a DLL load. Do not call Event 7 a process create.

**Path, hashes, signed vs unsigned:** Read them together. A signed `helper.dll` under Temp is still a path lead. An unsigned DLL under `Program Files` is a signature lead (where logged). A catalogued hash does not make a Temp load “expected.”

**Initiating process:** On a **7** / MDE image-load row, `Image` / `InitiatingProcess*` is **which process loaded the module**. On Event **6**, describe the driver path and signature; do not invent a user-mode parent.

Stay on the load row. File create of the DLL is **1.1.3**. Persistence and BYOVD methodology are **2.6**.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Word Loads a Signed Office DLL)

**MDE `DeviceImageLoadEvents` (`ImageLoaded`)**

| Field | Value |
|-------|--------|
| FileName / FolderPath | `mso.dll` / `C:\Program Files\Microsoft Office\root\Office16\` |
| ActionType | `ImageLoaded` |
| InitiatingProcessFileName | `WINWORD.EXE` |
| InitiatingProcessFolderPath | `C:\Program Files\Microsoft Office\root\Office16\` |
| SHA256 | *(matches catalogued Office mso.dll)* |
| Signed / Signature | `true` / `Microsoft Corporation` *(where logged)* |
| AccountName | `jlee` |

**What occurred:** Word loaded a signed Office DLL from its own Program Files directory. Path, initiator, hash, and signature agree. Expected.

**Not done:** Did not call it an incident. Did not hunt persistence. Did not rewrite this as a process-create lesson on `WINWORD.EXE` (**1.1.2**).

### Example 2: Office Loads Unsigned DLL from Temp (Lead)

**Sysmon Event ID 7 (Image loaded)**

| Field | Value |
|-------|--------|
| Image | `C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE` |
| ImageLoaded | `C:\Users\jlee\AppData\Local\Temp\helper.dll` |
| Signed | `false` |
| Signature | *(empty)* |
| SignatureStatus | `Unavailable` |
| Hashes | SHA256=*(not in catalog)* |
| User | `BUILDINGC\jlee` |

Compare a file row that is *not* this event:

> Sysmon **11**: `WINWORD.EXE` created `C:\Users\jlee\AppData\Local\Temp\helper.dll`. That is a **file create** (**1.1.3**). This row is the **image load**.

**What occurred:** Word **loaded** an unsigned `helper.dll` from Temp. The file create is a different event. Signature is present and false — not “not logged.”

**Interpretation:** Lead, not an automatic incident. Describe loader + path + unsigned. Do not teach DLL search-order methodology as a hunt unit (**2.6**). Do not pivot into Zeek.

### Example 3: Unexpected Driver Load (Lead)

**Sysmon Event ID 6 (Driver loaded)**

| Field | Value |
|-------|--------|
| ImageLoaded | `C:\Users\jlee\AppData\Local\Temp\helpdesk.sys` |
| Signed | `false` |
| Signature | *(empty)* |
| SignatureStatus | `Unavailable` |
| Hashes | SHA256=*(not in catalog)* |

Compare a user-mode load that is *not* this event:

> Sysmon **7**: `helpdesk.exe` loaded `helpdesk.dll` from the same Temp folder. That is a **user-mode image load**. This row is a **kernel driver**.

**What occurred:** An unsigned driver was **loaded from Temp**. That is Event **6**, not Event 7, and not a process create of `helpdesk.exe`.

**Interpretation:** Lead. Name driver vs user-mode image. Write unsigned and the path. Do not teach BYOVD or how to write a driver (**2.6**). If signature fields are missing in your tenant, write “signed not logged” and still use the path.

---

## 3. Hands-On Exercise

**Objective:** Practice describing image/driver load events and writing queries that find a specific pattern.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (user-mode image vs driver; expected vs lead).
2. For each item below, say **user-mode image load**, **driver load**, or **not an image/driver load event**. Give one reason.
   - Sysmon 7: `WINWORD.EXE` → `Program Files\...\mso.dll`, signed
   - Sysmon 7: `WINWORD.EXE` → `Temp\helper.dll`, unsigned
   - Sysmon 6: `Temp\helpdesk.sys`, unsigned
   - MDE `DeviceImageLoadEvents` `ImageLoaded`: Word → `mso.dll`
   - MDE `DeviceFileEvents` `FileCreated` of `helper.dll` under Temp
   - MDE `DeviceProcessEvents` `ProcessCreated`: `explorer.exe` → `WINWORD.EXE`
3. Write **two SIEM-style pseudo-queries**:
   - One for **user-mode image load** of a `.dll` under `Temp` or `AppData` (use path + loader if you have it; add `Signed == false` only if that field is logged).
   - One for **driver load** where `ImageLoaded` / path is **not** under `C:\Windows\` (Sysmon 6 shape).
4. Write **one analysis card** (small table or four sentences) for Example 2 *or* Example 3: load type, path, initiator (or “kernel driver”), signed/hash (or “not logged”), expected vs lead. Do not install Sysmon. Do not write a file or process query.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- Two specific load queries (not `DeviceImageLoadEvents` with no filter)
- One card that describes *this* event, not a slogan

---

## 4. Knowledge Check

1. What is the difference between a **user-mode image load** and a **kernel driver load**? Which Sysmon Event IDs map to each?
2. Why must you read **path, hash, and signed vs unsigned** together?
3. On MDE `DeviceImageLoadEvents`, what do `InitiatingProcess*` fields represent? What do you do with Event **6** for “parent”?
4. You have no Event 7 and no `DeviceImageLoadEvents`. A Sysmon 11 shows `helper.dll` created under Temp. Can you say it was loaded? What do you write?
5. `Signed` is empty. What do you write, and what do you still use?

---

## 5. Summary

- Image/driver load = a module entered a process, or a driver entered the kernel — on the **host**.
- Read path, hash if present, signed vs unsigned if present, and initiating process (user-mode).
- Sysmon **6 / 7** and MDE `DeviceImageLoadEvents` are the same story in different shapes. 7 is often missing or sampled.
- Event 7 is user-mode. Event 6 is a driver. A file create is **1.1.3**.
- A missing signature field is a visibility note. A signed binary in Temp is still a path lead.
- This closes unit **1.1**. Protocol deep-dive is **1.2**.

---

## 6. References & Further Reading

- Related modules:
  - 1.1.2 – Process activity
  - 1.1.3 – File system activity
  - 1.1.4 – Network activity (endpoint)
  - 1.1.5 – Registry activity (previous)
  - 1.2.1 – Zeek concepts (next unit)
  - 2.6.1 – Persistence techniques
- Local Sysmon / MDE field guide used in class (optional)
- Sysmon Event ID reference (6 / 7) and MDE `DeviceImageLoadEvents` schema — as deployed, not as a config lesson
