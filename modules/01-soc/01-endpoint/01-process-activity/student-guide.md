# Module 1.1.1 – Process Activity

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.1.1 A / B / C · 1.1.1.2 2b / 3c / 4c · 1.1.1.3 2b / 3c / 4c  
- Hunter: 1.1.1.1 A / B / B · 1.1.1.2 1a / 2b / 3c · 1.1.1.3 1a / 2b / 3c  
- CTI: 1.1.1.1 A / A / A · 1.1.1.2 1a / 1a / 1a · 1.1.1.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain process create, terminate, parent-child, command line, integrity/user, hashes/original filename, and process access.
2. Analyze a Sysmon or MDE process event and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* process pattern — not “all processes.”

**Mapped Proficiency Items:**
- K: 1.1.1.1 – Process activity concepts
- T: 1.1.1.2 – Analyze a process event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.1.3 – Create a SIEM query to detect specific process activity

---

## 1. Key Concepts

### 1.1 What a process event is

**Process activity** is host telemetry about a running program: it **started**, it **ended**, or one process **touched** another.

This unit is **endpoint** telemetry (Sysmon / Microsoft Defender for Endpoint). It is **not** Zeek (**1.2**). It is **not** how to install or configure Sysmon.

| This lesson | Later |
|-------------|-------|
| Create / terminate / who spawned whom / who opened whom | File create (**1.1.2**), host network (**1.1.3**), registry (**1.1.4**), image load (**1.1.5**) |
| Fields on the process event | Persistence *how-to* (**2.6**) |
| Sysmon Event IDs and MDE table names as they appear in a SIEM | Sysmon XML / deployment |

**Most critical distinction for daily work:**  
A process event is **who ran what, from whom, as whom**. A file event, a DNS name, or a Run key is a different row.

If a field is empty in your tenant (no integrity, no original filename), say so. Do not invent it.

### 1.2 Fields, parent-child, and how it is logged

| Idea | What to read | Why it matters |
|------|----------------|----------------|
| **Create / terminate** | Sysmon **1** / **5**; MDE `ActionType` `ProcessCreated` / `ProcessTerminated` | Start vs stop. Terminate without a matching create can still be useful (you saw the exit). |
| **PID / name / command line** | `ProcessId`, image/name, `CommandLine` / `ProcessCommandLine` | PID is unique *on that host for a while*. Name can lie. Command line is often the story. |
| **Parent-child** | `ParentProcessId` / PPID, parent name, parent command line; MDE `InitiatingProcess*` | Who launched it. Office → `cmd` is a different story than `explorer` → `notepad`. |
| **Integrity / user** | Integrity level; `User` / account (where logged) | Medium user vs High / SYSTEM. Empty = visibility gap, not “not admin.” |
| **Hash / original filename** | SHA256 (and MD5/SHA1 if present); `OriginalFileName` | Hash is the bytes. Original filename is the PE resource — can disagree with the on-disk name. |
| **Process access** | Sysmon **10** (`SourceImage` → `TargetImage`, granted access) | **Who touched whom** (often LSASS). Not a create. Not a separate module. |

**How this shows up (outline g)**

| Source | Events / table | Key fields |
|--------|----------------|------------|
| Sysmon | **1** Process Create, **5** Process Terminate, **10** Process Access | Image, CommandLine, ProcessId, ParentImage, ParentCommandLine, User, Hashes, SourceImage, TargetImage |
| MDE | `DeviceProcessEvents` | `ActionType`, `InitiatingProcess*`, `ProcessCommandLine`, SHA256, `AccountName`, `FileName`, `FolderPath` |

MDE create rows use **initiating** process = parent and **process** = child. Sysmon 1 uses Parent* / Image. Same story, different names.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| `explorer.exe` → `notepad.exe`, user, signed path under `Program Files` or `Windows` | Office / browser / `wscript.exe` → `powershell.exe` / `cmd.exe` with encoded or temp-path command line |
| `svchost.exe` as the service account doing its job | User process → SYSTEM child (elevation is **2.6.2**; here you only *describe* the process row) |
| Hash matches a catalogued binary; original filename matches the image | Hash unknown **or** `OriginalFileName` is `powershell.exe` while the file is named `update.exe` |
| No Event 10, or expected AV touching LSASS | Unexpected `SourceImage` opening `lsass.exe` |

**Command line vs name:** `powershell.exe` is common. `-enc` / `-EncodedCommand` plus a parent that is not a console you expect is the lead.

**Process access:** Event 10 is not “a process started.” It is a handle. Describe **source → target** and the access mask if you have it. Do not turn this hour into a credential-dump lab.

File drops, DNS, registry Run keys, and DLL loads are the next **1.1** lessons. Stay on the process row.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Explorer → Notepad)

**Sysmon Event ID 1 (create)**

| Field | Value |
|-------|--------|
| Image | `C:\Windows\System32\notepad.exe` |
| CommandLine | `notepad.exe C:\Users\jlee\Notes\todo.txt` |
| ProcessId | 4520 |
| ParentImage | `C:\Windows\explorer.exe` |
| ParentCommandLine | `C:\Windows\explorer.exe` |
| User | `BUILDINGC\jlee` |
| Integrity | Medium |
| SHA256 | *(matches catalogued notepad)* |
| OriginalFileName | `NOTEPAD.EXE` |

**What occurred:** User `jlee` launched Notepad from Explorer to open a text file. Parent-child, path, original filename, and hash agree. Expected.

**Not done:** Did not call it an incident. Did not hunt persistence. Did not open a file-activity lesson on `todo.txt` (**1.1.2**).

### Example 2: Script Host → Encoded PowerShell (Lead)

**MDE `DeviceProcessEvents` (`ProcessCreated`)**

| Field | Value |
|-------|--------|
| FileName / FolderPath | `powershell.exe` / `C:\Windows\System32\WindowsPowerShell\v1.0\` |
| ProcessCommandLine | `powershell.exe -NoP -W Hidden -enc SQBFAFgA...` |
| InitiatingProcessFileName | `wscript.exe` |
| InitiatingProcessCommandLine | `wscript.exe C:\Users\jlee\AppData\Local\Temp\invoice.vbs` |
| AccountName | `jlee` |
| SHA256 | *(powershell.exe — expected binary)* |
| ActionType | `ProcessCreated` |

Compare a terminate on the same host:

> Sysmon **5**: `powershell.exe` PID 8812 exited 12 seconds later. Same user. No new create for `notepad`.

**What occurred:** `wscript.exe` running a Temp `.vbs` created a **hidden, encoded** PowerShell. The binary hash is fine; the **parent + command line** is the lead. The Event 5 only says that PID ended — it does not clear the create.

**Interpretation:** Lead, not an automatic incident. Describe the chain. Do not write a persistence hunt (**2.6.3**). Do not pivot into Zeek (**1.2**).

### Example 3: Process Access to LSASS (Lead)

**Sysmon Event ID 10**

| Field | Value |
|-------|--------|
| SourceImage | `C:\Users\jlee\AppData\Local\Temp\helpdesk.exe` |
| SourceUser | `BUILDINGC\jlee` |
| TargetImage | `C:\Windows\System32\lsass.exe` |
| GrantedAccess | `0x1010` (example) |
| SourceProcessId / TargetProcessId | 9100 / 748 |

Compare a create that is *not* this event:

> Sysmon **1**: `helpdesk.exe` created from `explorer.exe`. That is a **create**. The LSASS row is **access**.

**What occurred:** A user-writable `helpdesk.exe` **opened** LSASS. That is process access (who touched whom). It is not a create of LSASS, not a terminate, and not proof of a dump by itself.

**Interpretation:** Lead. Name Event 10 and source → target. Do not teach Mimikatz. Do not call it privilege escalation without an elevation story (**2.6.2**).

---

## 3. Hands-On Exercise

**Objective:** Practice describing process events and writing queries that find a specific pattern.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (create, terminate, or access; expected vs lead).
2. For each item below, say **create**, **terminate**, **process access**, or **not a process event**. Give one reason.
   - Sysmon 1: `explorer.exe` → `notepad.exe`
   - Sysmon 5: `powershell.exe` PID 8812 exited
   - Sysmon 10: `helpdesk.exe` → `lsass.exe`
   - MDE `DeviceProcessEvents` `ProcessCreated`: `wscript.exe` → `powershell.exe -enc ...`
   - MDE `DeviceFileEvents` file create under Temp
   - Zeek `conn` row to 443
3. Write **two SIEM-style pseudo-queries**:
   - One for **script-host or Office parent** creating `powershell.exe` or `cmd.exe` (use parent name + child command line).
   - One for **process access** where `TargetImage` ends with `\lsass.exe` and `SourceImage` is **not** under `C:\Windows\` or `C:\Program Files\`.
4. Write **one analysis card** (small table or four sentences) for Example 2 *or* Example 3: action type, parent/source, child/target, command line or access, expected vs lead. Do not install Sysmon. Do not write a file or Zeek query.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- Two specific process queries (not `DeviceProcessEvents` with no filter)
- One card that describes *this* event, not a slogan

---

## 4. Knowledge Check

1. What is the difference between a process **create**, a **terminate**, and a **process access** event?
2. Why is **command line** (and parent command line) often more useful than the image name alone?
3. In MDE `DeviceProcessEvents`, what do `InitiatingProcess*` fields represent?
4. What does Sysmon Event ID **10** tell you that Event ID **1** does not?
5. You have no integrity field and no original filename. What do you write, and what do you still use?

---

## 5. Summary

- Process activity = create, terminate, or who touched whom — on the **host**.
- Read PID, name, command line, parent (`InitiatingProcess*` / Parent*), user/integrity if present, hash / original filename.
- Sysmon **1 / 5 / 10** and MDE `DeviceProcessEvents` are the same story in different shapes.
- Event 10 is access, not create. Name source → target.
- A matching hash does not make a bad parent + encoded command line “expected.”
- Next: file system activity (**1.1.2**). Host network is **1.1.3**. Zeek is **1.2**.

---

## 6. References & Further Reading

- Related modules:
  - 1.1.2 – File system activity (next)
  - 1.1.3 – Network activity (endpoint)
  - 1.1.4 – Registry activity
  - 1.1.5 – Image and driver load
  - 1.2.1 – Zeek concepts
- Local Sysmon / MDE field guide used in class (optional)
- Sysmon Event ID reference (1 / 5 / 10) and MDE `DeviceProcessEvents` schema — as deployed, not as a config lesson
