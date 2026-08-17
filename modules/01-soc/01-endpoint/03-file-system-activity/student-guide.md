# Module 1.1.3 – File System Activity

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.3.1 A / B / C · 1.1.3.2 2b / 3c / 4c · 1.1.3.3 2b / 3c / 4c  
- Hunter: 1.1.3.1 A / B / B · 1.1.3.2 1a / 2b / 3c · 1.1.3.3 1a / 2b / 3c  
- CTI: 1.1.3.1 A / A / A · 1.1.3.2 1a / 1a / 1a · 1.1.3.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain file create, rename-move, delete, modify, and read (where logged), plus path/name/extension, hashes, and initiating process.
2. Analyze a Sysmon or MDE file event and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* file operation — not “all file events.”

**Mapped Proficiency Items:**
- K: 1.1.3.1 – File system activity concepts
- T: 1.1.3.2 – Analyze a file event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.3.3 – Create a SIEM query to detect specific file operations

---

## 1. Key Concepts

### 1.1 What a file event is

**File system activity** is host telemetry about a file: it was **created**, **renamed or moved**, **deleted**, **modified**, or **read** (where that action is logged).

This unit is **endpoint** telemetry (Sysmon / Microsoft Defender for Endpoint). It is **not** Zeek (**1.2**), including Zeek’s `files` log. It is **not** how to install or configure Sysmon. Process create / terminate / access is **1.1.2** — a different row.

| This lesson | Later |
|-------------|-------|
| What happened to a file, where, by which process | Host network (**1.1.4**), registry (**1.1.5**), image load (**1.1.6**) |
| Fields on the file event | Persistence *how-to* (**2.6**) |
| Sysmon Event IDs and MDE table names as they appear in a SIEM | Sysmon XML / deployment |

**Most critical distinction for daily work:**  
A file event is **what happened to which file, by whom**. A process start, a DNS name, or a Run key is a different row.

If a field is empty in your tenant (no hash, no read events), say so. Do not invent it.

### 1.2 Operations, path, hash, initiator, and how it is logged

| Idea | What to read | Why it matters |
|------|----------------|----------------|
| **Create** | Sysmon **11**; MDE `ActionType` `FileCreated` | A file appeared or was overwritten. Most common file row. |
| **Rename / move** | MDE `FileRenamed` (`FileName` / `FolderPath` vs `PreviousFileName` / `PreviousFolderPath`) | Same object, new name or folder. Sysmon **11 / 23 / 26** do not log this as their own event. |
| **Delete** | Sysmon **23** (archived) / **26** (detected); MDE `FileDeleted` | The file is gone. **23** kept a copy; **26** only logged the delete. |
| **Modify / read** | MDE `FileModified` / `FileRead` **where logged** | Content or timestamp change; a read. Often missing. Not Sysmon 11 / 23 / 26. |
| **Path / name / extension** | `TargetFilename` (Sysmon); `FolderPath` + `FileName` (MDE) | Path is where. Name can lie. Extension can lie (`.txt`, `invoice.pdf.exe`). |
| **Hash** | SHA256 (and MD5/SHA1 if present) | Bytes of *this* file, when the event carries them. Empty ≠ clean. |
| **Initiating process** | Sysmon `Image`; MDE `InitiatingProcess*` | Who performed the file operation. Same field family as **1.1.2**, different job. |

**How this shows up (outline e)**

| Source | Events / table | Key fields |
|--------|----------------|------------|
| Sysmon | **11** FileCreate, **23** FileDelete (archived), **26** FileDeleteDetected | `Image`, `TargetFilename`, `ProcessId`, `User`, `Hashes` (often on **23 / 26**; often missing on **11**) |
| MDE | `DeviceFileEvents` | `ActionType`, `FolderPath`, `FileName`, SHA256, `InitiatingProcess*`, `PreviousFileName` / `PreviousFolderPath` on rename |

MDE file rows use **initiating** process = who touched the file and **FileName / FolderPath** = the object. Sysmon 11 uses `Image` / `TargetFilename`. Same story, different names.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| `WINWORD.EXE` → `.docx` under `Documents` | Script host / Office / `powershell.exe` → `.exe` / `.dll` / `.ps1` / `.vbs` under `Temp` or `AppData` |
| Browser → `.pdf` under `Downloads` | Double extension (`invoice.pdf.exe`) or a Windows binary name (`svchost.exe`) in a user-writable path |
| Installer writing under `Program Files` | Rename from a dropper name to a trusted-looking name outside `Windows` / `Program Files` |
| Hash matches a known document or installer; or hash not logged and you say so | Hash unknown **and** unexpected path + initiator |
| Delete of a user’s own Temp scratch file by that user app | Unexpected initiator deleting `.evtx`, Prefetch, or the dropper script after a create |

**Path + name + extension:** `update.exe` under `Temp` is a different story than `update.exe` under `Program Files`. `notes.txt` that is an executable, or `invoice.pdf.exe`, is a name/extension problem — not a separate module.

**Hashes:** SHA256 is the file bytes when present. Sysmon **11** often has no hash; **23 / 26** and MDE `FileCreated` more often do. A catalogued hash does not make an unexpected initiator + user-writable path “expected.”

**Initiating process:** On a file row, `InitiatingProcess*` / Sysmon `Image` is **who did this to the file**. It is not a process-create parent-child story. Do not turn the file row into a **1.1.2** write-up.

**Where logged:** Rename-move, modify, and read are MDE `ActionType` values when the tenant records them. If your Sysmon feed is only 11 / 23 / 26, you will not see those actions there. Write “not logged,” not “did not happen.”

Process creates, host DNS, registry Run keys, and DLL loads are other **1.1** / **1.2** lessons. Stay on the file row.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Word → Documents)

**MDE `DeviceFileEvents` (`FileCreated`)**

| Field | Value |
|-------|--------|
| FileName / FolderPath | `Q3-notes.docx` / `C:\Users\jlee\Documents\` |
| ActionType | `FileCreated` |
| InitiatingProcessFileName | `WINWORD.EXE` |
| InitiatingProcessFolderPath | `C:\Program Files\Microsoft Office\root\Office16\` |
| AccountName | `jlee` |
| SHA256 | *(document written by Word — expected save)* |

**What occurred:** User `jlee` saved a Word document in Documents. Initiator, path, and name agree. Expected.

**Not done:** Did not call it an incident. Did not hunt persistence. Did not rewrite this as a process-create lesson on `WINWORD.EXE` (**1.1.2**).

### Example 2: Script Host → Temp Executable (Lead)

**Sysmon Event ID 11 (FileCreate)**

| Field | Value |
|-------|--------|
| Image | `C:\Windows\System32\wscript.exe` |
| TargetFilename | `C:\Users\jlee\AppData\Local\Temp\update.exe` |
| ProcessId | 6640 |
| User | `BUILDINGC\jlee` |
| Hashes | *(not present on this Event 11)* |

Compare a process row that is *not* this event:

> Sysmon **1**: `wscript.exe` created from `explorer.exe` running `invoice.vbs`. That is a **process create** (**1.1.2**). This row is the **file create**.

**What occurred:** `wscript.exe` created `update.exe` under Temp. No hash on the Event 11. User-writable path. The process create is a different event.

**Interpretation:** Lead, not an automatic incident. Describe the file row. Write “hash not logged.” Do not write a persistence hunt (**2.6**). Do not pivot into Zeek (**1.2**).

### Example 3: Rename Masquerade and Script Delete (Lead)

**MDE `DeviceFileEvents` (`FileRenamed`)**

| Field | Value |
|-------|--------|
| PreviousFileName / PreviousFolderPath | `invoice.pdf.exe` / `C:\Users\jlee\Downloads\` |
| FileName / FolderPath | `svchost.exe` / `C:\Users\jlee\AppData\Roaming\` |
| ActionType | `FileRenamed` |
| InitiatingProcessFileName | `powershell.exe` |
| InitiatingProcessCommandLine | `powershell.exe -NoP -W Hidden -enc SQBFAFgA...` |
| SHA256 | *(same bytes as the download — unknown catalog)* |

Compare a delete on the same host:

> Sysmon **26** FileDeleteDetected: `Image` `wscript.exe`, `TargetFilename` `C:\Users\jlee\AppData\Local\Temp\invoice.vbs`. Hashes present on the **26**. The script is gone; the renamed payload is not.

**What occurred:** `powershell.exe` **renamed/moved** a double-extension download to `svchost.exe` under AppData\Roaming. That is not a create and not a delete. The Event **26** is a **delete** of the `.vbs`. Neither row is a process create.

**Interpretation:** Lead. Name `FileRenamed` and the previous vs new path/name. The delete is a separate action. Do not call it persistence without a Run-key / startup story (**1.1.5** / **2.6**). Do not treat `svchost.exe` in AppData as the real `svchost` under `C:\Windows\System32\`.

---

## 3. Hands-On Exercise

**Objective:** Practice describing file events and writing queries that find a specific operation.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (create, rename-move, or delete; expected vs lead).
2. For each item below, say **create**, **rename-move**, **delete**, **modify**, **read**, or **not a file event**. Give one reason.
   - Sysmon 11: `wscript.exe` → `C:\Users\jlee\AppData\Local\Temp\update.exe`
   - Sysmon 26: `wscript.exe` deleted `invoice.vbs`
   - MDE `DeviceFileEvents` `FileCreated`: `WINWORD.EXE` → `Documents\Q3-notes.docx`
   - MDE `DeviceFileEvents` `FileRenamed`: `invoice.pdf.exe` → `AppData\Roaming\svchost.exe`
   - MDE `DeviceProcessEvents` `ProcessCreated`: `wscript.exe` → `powershell.exe -enc ...`
   - Zeek `files` or `conn` row
3. Write **two SIEM-style pseudo-queries**:
   - One for **script-host, Office, or PowerShell** creating `.exe`, `.dll`, `.ps1`, or `.vbs` under `Temp` or `AppData` (use initiator + path + extension).
   - One for **rename** where the new `FileName` is a well-known Windows binary name (`svchost.exe`, `rundll32.exe`, `explorer.exe`) and `FolderPath` is **not** under `C:\Windows\` or `C:\Program Files\`.
4. Write **one analysis card** (small table or four sentences) for Example 2 *or* Example 3: action type, path/name, initiating process, hash (or “not logged”), expected vs lead. Do not install Sysmon. Do not write a process or Zeek query.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- Two specific file-operation queries (not `DeviceFileEvents` with no filter)
- One card that describes *this* event, not a slogan

---

## 4. Knowledge Check

1. What is the difference between a file **create**, a **rename-move**, and a **delete**? Which of those do Sysmon **11 / 23 / 26** cover?
2. Why must you read **path, name, and extension** together?
3. On MDE `DeviceFileEvents`, what do `InitiatingProcess*` fields represent? How is that different from `InitiatingProcess*` on `DeviceProcessEvents`?
4. What does Sysmon Event ID **23** tell you that Event ID **26** does not? What does Event **11** often omit that **23 / 26** often include?
5. You have no SHA256 and no `FileRead` rows. What do you write, and what do you still use?

---

## 5. Summary

- File system activity = create, rename-move, delete, modify, or read (where logged) — on the **host**.
- Read path, name, extension, hash if present, and initiating process (`Image` / `InitiatingProcess*`).
- Sysmon **11 / 23 / 26** and MDE `DeviceFileEvents` are the same story in different shapes. Rename, modify, and read are MDE `ActionType` values when logged.
- Event 11 is create, not rename. Event 23/26 are delete. A process create is **1.1.2**.
- A missing hash is a visibility note. A good hash does not make a Temp drop + script-host initiator “expected.”
- Next: network activity on the endpoint (**1.1.4**). Zeek is **1.2**.

---

## 6. References & Further Reading

- Related modules:
  - 1.1.2 – Process activity (previous)
  - 1.1.4 – Network activity (endpoint) (next)
  - 1.1.5 – Registry activity
  - 1.1.6 – Image and driver load
  - 1.2.1 – Zeek concepts
- Local Sysmon / MDE field guide used in class (optional)
- Sysmon Event ID reference (11 / 23 / 26) and MDE `DeviceFileEvents` schema — as deployed, not as a config lesson
