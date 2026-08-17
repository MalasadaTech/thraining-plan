# Module 1.1.3 – File System Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.3 – File System Activity  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Host file rows. Not Zeek. Not Sysmon install. Not the process create from last hour.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read **host** file rows: what happened to a file, where, by whom.

Not a process create (**1.1.2**).  
Not Zeek (**1.2**). Not how to install Sysmon.

**Speaker Notes:**  
Daily alert work: describe the file row. Host-network waits.

---

### Slide 3 – The actions
**Title:** Create, rename-move, delete, modify, read

**Create** — a file appeared. Sysmon **11**.  
**Rename-move** — same object, new name or folder.  
**Delete** — Sysmon **23** / **26**.  
**Modify / read** — where logged.

**Speaker Notes:**  
Outline a. Event 11 is not a rename.

---

### Slide 4 – Path, hash, who touched it
**Title:** Path, hash, initiating process

**Path / name / extension** — where it sits. Name can lie.  
**Hash** — bytes when present. Event **11** often has none.  
**Initiating process** — who did this *to the file*.

**Speaker Notes:**  
Outline b–d. Do not turn this into a 1.1.2 parent-child write-up.

---

### Slide 5 – How it shows up
**Title:** Sysmon and MDE

Sysmon **11** / **23** / **26**.

MDE `DeviceFileEvents` `ActionType`:  
**FileCreated**. **FileRenamed**. **FileDeleted**.  
**FileModified** / **FileRead** where logged.

Same story. Different names. Full `ActionType` list is in the Defender portal — do not invent values.

**Speaker Notes:**  
Outline e. Write “not logged,” not “did not happen.”

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: what happened to which file, by whom.

**Given:** Sysmon **11**, `wscript.exe` → Temp `update.exe`, no hash.

A query names a **specific** pattern — initiator + path + extension.  
Not “all file events.”

**Speaker Notes:**  
They should see this row before the knowledge check. Script host created update.exe under Temp. Hash not logged. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Sysmon Event 11 is a rename. True or false?  
2. `wscript.exe` creates Temp `update.exe` (Sysmon 11, no hash). In one sentence, what occurred?  
3. A SIEM query that matches every `DeviceFileEvents` row is a good “specific file operation” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions for the whole lesson. Stop.

---

### Slide 8 – Summary
**Title:** Summary

What happened to which file, by whom.  
Path and initiator tell the story.  
A missing hash is a gap.  
A query is specific.

**Next:** **1.1.4** Network activity (endpoint)

**Speaker Notes:**  
That hour is host-observed network. Not Zeek.
