# Module 1.1.1 – Process Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.1.1 – Process Activity  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Host process telemetry. Sysmon 1 / 5 / 10 and MDE DeviceProcessEvents. Not install. Not Zeek.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain create, terminate, parent-child, command line, integrity/user, hash/original filename, and process access
2. Analyze a Sysmon or MDE process event and describe what occurred
3. Write a SIEM query for *specific* process activity

**Mapped Items:**  
K: 1.1.1.1 | T: 1.1.1.2 | T: 1.1.1.3

**Speaker Notes:**  
SOC 3 is A / 2b. CTI is nomenclature only (A / 1a).

---

### Slide 3 – Agenda
**Title:** Agenda

- What a process event is
- Fields (outline a–f)
- Sysmon 1 / 5 / 10 and DeviceProcessEvents
- Three worked examples
- Identification + two queries
- Knowledge check

**Speaker Notes:**  
1.1.2 file and 1.2 Zeek are later. Stay on the process row.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Sysmon install / XML  
File create under Temp (**1.1.2**)  
Zeek `conn` to 443 (**1.2**)  
Registry Run keys (**1.1.4** / **2.6**)  
“All PowerShell is bad”

**Key Point:** Describe *this* process row.

**Speaker Notes:**  
Park deploy questions on the board.

---

### Slide 5 – Three Actions
**Title:** Create, Terminate, Access

| Action | Sysmon | MDE |
|--------|--------|-----|
| Started | **1** | `ProcessCreated` |
| Ended | **5** | `ProcessTerminated` |
| Touched another | **10** | *(process access — Sysmon-shaped)* |

**Analyst Tip:** Event 10 is not a create of the target.

**Speaker Notes:**  
Ask: “Did it start, stop, or open a handle?”

---

### Slide 6 – Identity Fields
**Title:** PID, Name, Command Line

**PID** — this host, this window of time  
**Name** — can lie  
**Command line** — often the story (`-enc`, hidden, Temp path)

**Key Point:** A good SHA256 on `powershell.exe` is not a full description.

**Speaker Notes:**  
Write a stock vs `-enc` command line on the board.

---

### Slide 7 – Parent-Child
**Title:** Who Launched It

Sysmon: `ParentImage` / `ParentCommandLine`  
MDE: `InitiatingProcess*` = **parent**

**Expected:** `explorer.exe` → `notepad.exe`  
**Lead:** `wscript.exe` / Office → `powershell.exe`

**Speaker Notes:**  
Map the MDE names live. Students mix them up.

---

### Slide 8 – Context and Hashes
**Title:** User, Integrity, Hash, Original Filename

**User / integrity** — who, and Medium vs High / SYSTEM (if logged)  
**SHA256** — the bytes  
**OriginalFileName** — PE resource; can disagree with the file name

Empty field → write “not logged.” Do not invent.

**Speaker Notes:**  
Original filename vs on-disk name is the rename trick. One example only.

---

### Slide 9 – Event 10
**Title:** Process Access = Who Touched Whom

SourceImage → TargetImage  
Example: Temp `helpdesk.exe` → `lsass.exe`

**Not:** LSASS was created  
**Not:** Automatic credential dump  
**Not:** A separate teaching unit

**Speaker Notes:**  
Do not demo dump tools.

---

### Slide 10 – Example 1: Expected Create
**Title:** Example 1 – Explorer → Notepad

- Sysmon **1**
- User `jlee`, Medium
- OriginalFileName `NOTEPAD.EXE`
- Hash matches catalog

**Interpretation:**  
Create. Expected. Not an incident.

**Speaker Notes:**  
Students describe the row before you reveal.

---

### Slide 11 – Example 2: Encoded PowerShell
**Title:** Example 2 – wscript → powershell -enc

- MDE `ProcessCreated`
- Parent: Temp `invoice.vbs`
- Child: `-NoP -W Hidden -enc …`
- Hash is stock PowerShell
- Event **5** later only ends the PID

**Interpretation:**  
Create **lead** because of parent + command line.

**Speaker Notes:**  
Force: good hash ≠ expected chain.

---

### Slide 12 – Example 3: Access
**Title:** Example 3 – Event 10 vs Event 1

**10:** Temp `helpdesk.exe` → `lsass.exe`  
**1:** `explorer.exe` → `helpdesk.exe` (create — different row)

**Interpretation:**  
Access lead. Name source → target.

**Speaker Notes:**  
Park 2.6.2 unless they invent an elevation.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- Event 10 = create
- Query with no filter
- Hash-only verdict
- File or Zeek row as “process”
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
3. Two queries: parent→shell; access to LSASS from outside Windows/Program Files.
4. One analysis card (Example 2 or 3).

**Speaker Notes:**  
Park file, Zeek, install. Review with the Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Create vs terminate vs access?
2. Why command line (and parent command line)?
3. What is MDE `InitiatingProcess*`?
4. What does Event 10 add vs Event 1?
5. Missing integrity / original filename — what do you write?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Host process row: create, terminate, or access.
- Parent + command line + user; hash / original filename when present.
- Sysmon 1 / 5 / 10 ↔ `DeviceProcessEvents`.
- Event 10 = who touched whom.
- Next: file system activity (**1.1.2**).

**Speaker Notes:**  
Do not open a 1.1.2 file lab.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Process Activity — Quick Reference

| Need | Look at |
|------|---------|
| Started | Sysmon 1 / `ProcessCreated` |
| Ended | Sysmon 5 / `ProcessTerminated` |
| Touched | Sysmon 10 Source → Target |
| Parent (MDE) | `InitiatingProcess*` |
| Story | Parent + `ProcessCommandLine` |

**Coming next:** Module 1.1.2 – File system activity

**Footer:** SOC / Hunter / CTI Training Program
