# Instructor Guide – Module 1.1.2 – File System Activity

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.2.1 A / B / C · 1.1.2.2 2b / 3c / 4c · 1.1.2.3 2b / 3c / 4c  
- Hunter: 1.1.2.1 A / B / B · 1.1.2.2 1a / 2b / 3c · 1.1.2.3 1a / 2b / 3c  
- CTI: 1.1.2.1 A / A / A · 1.1.2.2 1a / 1a / 1a · 1.1.2.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read host file telemetry (Sysmon 11 / 23 / 26 and MDE `DeviceFileEvents`), describe what occurred, and write a SIEM query for a specific file operation.

**Key Teaching Points:**
- Endpoint file rows, not Zeek (**1.2**), not Sysmon install, not process create (**1.1.1**).
- Create vs rename-move vs delete vs modify vs read (where logged).
- Sysmon 11 / 23 / 26 cover create and delete. Rename, modify, and read are MDE `ActionType` when present.
- Path + name + extension; hash when present; initiating process is who touched the file.
- Stay out of host-network / registry / image-load (1.1.3–1.1.5) and persistence how-to (2.6).

**Common Student Challenges:**
- Treating every `.exe` under Temp as an incident (describe first).
- Calling Event 11 a rename, or Event 26 a create.
- Writing `DeviceFileEvents` with no filter.
- Rewriting the file row as a **1.1.1** process-create card.
- Asking how to deploy Sysmon or why read is not in the Sysmon feed.
- Calling AppData `svchost.exe` persistence without a Run-key story.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for Sysmon 11 / 23 / 26 vs MDE `ActionType` names
- Optional: one sanitized Event 11 and `FileRenamed` screenshot
- Answer key (this guide)

---

## Learning Objectives

1. Explain file create, rename-move, delete, modify, and read (where logged), plus path/name/extension, hashes, and initiating process.
2. Analyze a Sysmon or MDE file event and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* file operation — not “all file events.”

**Mapped Items:**
- K: 1.1.2.1 – File system activity concepts
- T: 1.1.2.2 – Analyze a file event (Sysmon or MDE)
- T: 1.1.2.3 – Create a SIEM query to detect specific file operations

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Host vs Zeek; not install; not 1.1.1 |
| What a file event is           | 8 min    | Five operations; “where logged” |
| Fields + how logged            | 16 min   | a–e on the board; MDE name map |
| Walkthrough Examples           | 14 min   | Students describe first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~70 min** | Stretch Example 3 if they call rename a create |

---

## Detailed Teaching Notes

### 1. What a file event is

**Talking Points:**
- SOC 3 is facts (A / 2b). Push field names and “what occurred” in one sentence.
- SOC 5/7: initiator + path + action story and a query a teammate can run (B/C, 3c/4c).
- Hunter secondary: A / B / B and 1a / 2b / 3c — recognize the row, not own the query bar.
- CTI: A / A / A and 1a / 1a / 1a — nomenclature only. Do not grade them as SOC 5.

**What to emphasize:**
- Empty hash / no `FileRead` = say “not logged,” not “clean” or “never read.”
- Do not install Sysmon in this hour.

**Questions to ask:**  
“What happened to the file, and which process did it?”  
“Is this a create, a rename, or a delete?”

### 2. Fields and logging shape

**Talking Points:**
- Walk outline a–e once. Rename-move / modify / read stay in this lesson as “where logged.”
- Dual-map Sysmon `TargetFilename` ↔ MDE `FolderPath` + `FileName` live. Dual-map `Image` ↔ `InitiatingProcessFileName`.
- Hash = file bytes when present. Event 11 often has none; 23 / 26 and MDE creates more often do.
- Extension and on-disk name can lie. Path is half the story.
- Do not open Event 2 / 15 / 29 as extra obligations. Park them if someone names them.

**What to emphasize:**
- `InitiatingProcess*` on a file row is the actor, not a child process.
- Next activity types are later 1.1.x. Park them on the board.

**Question to ask:**  
“If I only give you `svchost.exe` and a hash, do you have a story yet?”

### 3. Examples

Work through all three interactively. Students say create/rename-move/delete and expected/lead before you read the interpretation.

**Extra point for Example 1:**  
Baseline. Word + Documents + `.docx`.

**Extra point for Example 2:**  
Create, not a process start. Hash missing is a visibility note, not a pass.

**Extra point for Example 3:**  
`FileRenamed` ≠ Event 11. Double extension → trusted name in AppData. Event 26 is a separate delete. Not a 2.6 lab.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 14–16 minutes.
- Allow use of the Student Guide.
- Grade description + specific queries. Do not grade Sysmon config.
- Review as a group. Do not collect a grade.
- Park process, Zeek, registry, and 2.6 labs.

**What good answers look like:**

**Summaries:**
- Example 1: Create; Word → Documents `.docx`; expected.
- Example 2: Create; wscript → Temp `update.exe`; lead. Hash not on Event 11.
- Example 3: Rename-move; PowerShell `invoice.pdf.exe` → AppData `svchost.exe`; lead. Event 26 is a delete of the `.vbs`.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Sysmon 11 wscript → Temp `update.exe` | **Create** | Event 11 |
| Sysmon 26 wscript deleted `invoice.vbs` | **Delete** | Event 26 |
| MDE FileCreated Word → Documents `.docx` | **Create** | MDE create |
| MDE FileRenamed `invoice.pdf.exe` → AppData `svchost.exe` | **Rename-move** | `FileRenamed` |
| DeviceProcessEvents ProcessCreated wscript → powershell | **Not a file event** | **1.1.1** |
| Zeek `files` or `conn` | **Not a file event** | **1.2** |

**Pseudo-queries (equivalent is fine):**

```
DeviceFileEvents
| where ActionType == "FileCreated"
| where FileName endswith ".exe"
    or FileName endswith ".dll"
    or FileName endswith ".ps1"
    or FileName endswith ".vbs"
| where FolderPath has_any (@"\Temp\", @"\AppData\")
| where InitiatingProcessFileName in (
    "wscript.exe", "cscript.exe", "powershell.exe",
    "winword.exe", "excel.exe", "outlook.exe")
```

```
DeviceFileEvents
| where ActionType == "FileRenamed"
| where FileName in ("svchost.exe", "rundll32.exe", "explorer.exe")
| where FolderPath !startswith @"C:\Windows\"
    and FolderPath !startswith @"C:\Program Files\"
```

Fail a query with no initiator/path/name filter, a `DeviceProcessEvents` query, or a Zeek `files` / `conn` query.

**Analysis card (example — Example 2):**  
Create (Sysmon 11). Object: `C:\Users\jlee\AppData\Local\Temp\update.exe`. Initiator: `wscript.exe`. Hash not logged. Lead because of initiator + user-writable path + `.exe`. Not an incident by itself. The matching Sysmon 1 is a different row.

Fail the card if they only write “malicious dropper,” call Event 11 a rename, treat Event 26 as a create, or add a Run-key hunt.

---

## Knowledge Check – Answer Key

1. **Create vs rename-move vs delete? Which Sysmon IDs?**  
   **Answer:** Create (Sysmon 11 / MDE `FileCreated`) = a file appeared or was overwritten. Rename-move (MDE `FileRenamed`) = same object, new name or folder; not Sysmon 11 / 23 / 26. Delete (Sysmon 23 / 26 / MDE `FileDeleted`) = the file is gone.  
   **Explanation:** 11 is create. 23/26 are delete. Rename is MDE when logged.

2. **Why path, name, and extension together?**  
   **Answer:** Name and extension can lie (`invoice.pdf.exe`, `svchost.exe` in AppData). Path tells you whether the location is expected (`Documents` / `Program Files` vs `Temp` / `AppData`).  
   **Explanation:** One field is not a story.

3. **MDE `InitiatingProcess*` on a file event vs a process event?**  
   **Answer:** On `DeviceFileEvents` it is **who performed the file operation**. On `DeviceProcessEvents` it is the **parent** of the created process (**1.1.1**).  
   **Explanation:** Same names, different job.

4. **Event 23 vs 26? What 11 often omits?**  
   **Answer:** Both are deletes. **23** archived a copy; **26** only detected/logged the delete. Event **11** often has **no hash**; **23 / 26** more often include hashes.  
   **Explanation:** Do not call 23/26 a create. Do not invent a hash on 11.

5. **Missing SHA256 / no FileRead?**  
   **Answer:** Write “not logged” (visibility). Still use action type, path/name/extension, and initiating process.  
   **Explanation:** Do not invent fields. Absence of read rows is not proof the file was never read.

---

## Additional Instructor Resources

- Local expected Word / browser / installer paths if you have a list
- Escalation: process → 1.1.1; host network → 1.1.3; Zeek → 1.2; persistence → 2.6
- Next recommended module: Network activity (endpoint) (1.1.3)
