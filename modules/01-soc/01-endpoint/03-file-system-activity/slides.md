# Module 1.1.3 – File System Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.3 – File System Activity  
**Subtitle:** What happened to the file  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.1.1 named the five kinds of host activity. This lesson is the file kind. It is not Zeek, not how to install Sysmon, and not a process-create write-up.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read **file** events to see what happened to a file.

Where it sat. Which process touched it.  
Not Zeek. Not how to install Sysmon. Not a process create.

**Speaker Notes:**  
This is daily alert work: describe the file event. Host-network waits for later lessons.

---

### Slide 3 – Create, rename-move, delete
**Title:** Create, rename-move, delete, modify, read

**Create** — a file appeared. Sysmon **11**. MDE create is `FileCreated`.

**Rename-move** — same object, new name or folder. MDE `FileRenamed` when logged. Not Event 11.

**Delete** — Sysmon **23** / **26**. MDE `FileDeleted`.

**Modify / read** — where logged. Do not assume a `FileRead` value on this table.

**Speaker Notes:**  
Walk the actions first. Event 11 is create, not rename. Read is where that action is logged — do not invent `FileRead`.

---

### Slide 4 – Path, hash, who touched it
**Title:** Path, hash, initiating process

**Path / name / extension** — where it sits. The name can lie.

**Hash** — file bytes when present. Event **11** often has none. Empty is a gap, not “clean.”

**Initiating process** — who did this *to the file*. Not a process-create parent-child write-up.

**Speaker Notes:**  
Path and initiator are what you write down. Do not turn this into a 1.1.2 parent-child write-up.

---

### Slide 5 – How it shows up
**Title:** Sysmon and MDE

Sysmon **11** / **23** / **26**.

MDE `DeviceFileEvents` `ActionType`:  
**FileCreated** (create). **FileRenamed** (rename-move). **FileDeleted** (delete). **FileModified** (where logged).

Same activity. Different field names.  
The full `ActionType` list is in the Defender portal — do not invent values.

**Speaker Notes:**  
Read is where that action is logged. Do not invent `FileRead` on this MDE table. Write “not logged,” not “did not happen.” Do not teach Sysmon install.

---

### Slide 6 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: what happened to which file, by whom.

**Given:** Sysmon **11**, `wscript.exe` → Temp `update.exe`, no hash.

A query names a **specific** pattern — initiator + path + extension.  
Not “all file events.”

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: script host created update.exe under Temp. Hash not logged. Do not tell the intro plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Sysmon Event 11 is a rename. True or false?  
2. `wscript.exe` creates Temp `update.exe` (Sysmon 11, no hash). In one sentence, what occurred?  
3. A SIEM query that matches every file event is a good “specific file operation” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

What happened to which file, by whom.  
Path and initiator are what you trust.  
A missing hash is a gap.  
A query is specific.

**Next:** **1.1.4** Network activity (endpoint)

**Speaker Notes:**  
1.1.4 is the host-network event on the same host telemetry. Stay off this file event when you get there.
