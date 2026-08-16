# Module 1.1.2 – File System Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.1.2 – File System Activity  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Host file telemetry. Sysmon 11 / 23 / 26 and MDE DeviceFileEvents. Not install. Not Zeek. Not 1.1.1.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain create, rename-move, delete, modify, and read (where logged), plus path/name/extension, hash, and initiating process
2. Analyze a Sysmon or MDE file event and describe what occurred
3. Write a SIEM query for *specific* file operations

**Mapped Items:**  
K: 1.1.2.1 | T: 1.1.2.2 | T: 1.1.2.3

**Speaker Notes:**  
SOC 3 is A / 2b. CTI is nomenclature only (A / 1a).

---

### Slide 3 – Agenda
**Title:** Agenda

- What a file event is
- Operations and fields (outline a–d)
- Sysmon 11 / 23 / 26 and DeviceFileEvents
- Three worked examples
- Identification + two queries
- Knowledge check

**Speaker Notes:**  
1.1.1 process and 1.2 Zeek are other rows. Stay on the file row.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Sysmon install / XML  
Process create of `wscript.exe` (**1.1.1**)  
Zeek `files` / `conn` (**1.2**)  
Registry Run keys (**1.1.4** / **2.6**)  
“Every Temp `.exe` is an incident”

**Key Point:** Describe *this* file row.

**Speaker Notes:**  
Park deploy questions on the board.

---

### Slide 5 – Five Operations
**Title:** Create, Rename-Move, Delete, Modify, Read

| Action | Sysmon | MDE |
|--------|--------|-----|
| Created / overwritten | **11** | `FileCreated` |
| Renamed or moved | *(not 11 / 23 / 26)* | `FileRenamed` |
| Deleted | **23** archived / **26** detected | `FileDeleted` |
| Modified / read | *(not 11 / 23 / 26)* | `FileModified` / `FileRead` where logged |

**Analyst Tip:** Missing ActionType ≠ “did not happen.”

**Speaker Notes:**  
Ask: “Did it appear, change name, or go away?”

---

### Slide 6 – Path, Name, Extension
**Title:** Where It Is, What It Is Called

**Path** — `Documents` vs `Temp` vs `AppData` vs `Program Files`  
**Name** — can lie (`svchost.exe` in AppData)  
**Extension** — can lie (`invoice.pdf.exe`, `.txt` that is an executable)

**Key Point:** Read all three. One field is not a story.

**Speaker Notes:**  
Write a double-extension name on the board.

---

### Slide 7 – Hashes
**Title:** File Bytes, When Logged

**SHA256** — the file, not the process  
Sysmon **11** — often **no** hash  
Sysmon **23 / 26** and MDE creates — more often yes

Empty field → write “not logged.” Do not invent.  
A known hash does not clear a bad path + initiator.

**Speaker Notes:**  
Same rule as 1.1.1: hash is bytes, not a verdict.

---

### Slide 8 – Initiating Process
**Title:** Who Touched the File

Sysmon: `Image`  
MDE: `InitiatingProcess*` = **actor of the file operation**

**Not** the parent of a child process (**1.1.1**). Same names, different job.

**Expected:** `WINWORD.EXE` → Documents `.docx`  
**Lead:** `wscript.exe` / Office / `powershell.exe` → Temp `.exe`

**Speaker Notes:**  
Map the MDE names live. Students reuse the process-create story.

---

### Slide 9 – How It Is Logged
**Title:** Sysmon 11 / 23 / 26 ↔ DeviceFileEvents

| Need | Look at |
|------|---------|
| Create | 11 / `FileCreated` |
| Delete | 23 or 26 / `FileDeleted` |
| Rename-move | `FileRenamed` + Previous* |
| Object | `TargetFilename` or `FolderPath` + `FileName` |
| Actor | `Image` or `InitiatingProcess*` |

**Speaker Notes:**  
23 archived a copy. 26 only logged the delete.

---

### Slide 10 – Example 1: Expected Create
**Title:** Example 1 – Word → Documents

- MDE `FileCreated`
- `Q3-notes.docx` under Documents
- Initiator `WINWORD.EXE`
- Hash present (document save)

**Interpretation:**  
Create. Expected. Not an incident.

**Speaker Notes:**  
Students describe the row before you reveal.

---

### Slide 11 – Example 2: Temp Drop
**Title:** Example 2 – wscript → Temp `update.exe`

- Sysmon **11**
- `TargetFilename` under `AppData\Local\Temp\`
- Hash **not** on this Event 11
- Matching Sysmon **1** is a **different** row

**Interpretation:**  
Create **lead** because of initiator + path + `.exe`.

**Speaker Notes:**  
Force: missing hash ≠ clean. Event 11 ≠ process create.

---

### Slide 12 – Example 3: Rename + Delete
**Title:** Example 3 – FileRenamed vs Event 26

**Renamed:** `invoice.pdf.exe` (Downloads) → `svchost.exe` (AppData\Roaming)  
**26:** `wscript.exe` deleted `invoice.vbs`

**Interpretation:**  
Rename-move lead. Delete is a second action. Not a create of `svchost`.

**Speaker Notes:**  
Park 1.1.4 / 2.6 unless they invent a Run key.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- Event 11 = rename
- Event 26 = create
- Query with no filter
- Hash-only verdict
- Process or Zeek row as “file”
- Asking how to deploy Sysmon
- Persistence hunt instead of description

**Speaker Notes:**  
Then the exercise.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide.
3. Two queries: initiator+path+extension create; rename to a Windows binary name outside Windows/Program Files.
4. One analysis card (Example 2 or 3).

**Speaker Notes:**  
Park process, Zeek, install. Review with the Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Create vs rename-move vs delete? Which Sysmon IDs?
2. Why path, name, and extension together?
3. `InitiatingProcess*` on a file event vs a process event?
4. Event 23 vs 26? What does 11 often omit?
5. Missing SHA256 / no FileRead — what do you write?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Host file row: create, rename-move, delete, modify, or read (where logged).
- Path + name + extension + initiator; hash when present.
- Sysmon 11 / 23 / 26 ↔ `DeviceFileEvents`.
- 11 = create. 23/26 = delete. Rename is MDE.
- Next: host-observed network (**1.1.3**).

**Speaker Notes:**  
Do not open a 1.1.3 network lab.

---

### Slide 17 – Quick Reference (Optional)
**Title:** File System Activity — Quick Reference

| Need | Look at |
|------|---------|
| Created | Sysmon 11 / `FileCreated` |
| Renamed | `FileRenamed` + Previous* |
| Deleted | Sysmon 23 / 26 / `FileDeleted` |
| Actor (MDE) | `InitiatingProcess*` |
| Object | `FolderPath` + `FileName` |

**Coming next:** Module 1.1.3 – Network activity (endpoint)

**Footer:** SOC / Hunter / CTI Training Program
