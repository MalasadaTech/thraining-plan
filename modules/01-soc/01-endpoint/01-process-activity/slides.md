# Module 1.1.1 – Process Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.1 – Process Activity  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Start of the SOC analyst block. Host process rows. Not Zeek. Not Sysmon install.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read **host** process rows to see who ran what.

Create. Terminate. Who touched whom.  
Not Zeek. Not how to install Sysmon.

**Speaker Notes:**  
This is daily alert work: describe the process row. File and DNS wait.

---

### Slide 3 – The row
**Title:** Create, terminate, parent, command line

**Create / terminate** — Sysmon 1 / 5; MDE `ProcessCreated` / `ProcessTerminated`.

**PID, name, command line** — name can lie. Command line is often the story.

**Parent-child** — who launched it. MDE `InitiatingProcess*` is the parent.

**Speaker Notes:**  
Walk a–c. Office → cmd is a different story than explorer → notepad.

---

### Slide 4 – User, hash, access
**Title:** User, hash, who touched whom

**Integrity / user** — where logged. Empty is a gap.

**Hash / original filename** — bytes vs PE resource. They can disagree.

**Process access** — Sysmon **10**. Source → target. Not a create.

**Speaker Notes:**  
Outline d–f. Do not turn Event 10 into a credential-dump hour.

---

### Slide 5 – How it shows up
**Title:** Sysmon and MDE

Sysmon **1** / **5** / **10**.

MDE `DeviceProcessEvents` `ActionType`:  
**ProcessCreated** (create). **OpenProcess** (who touched whom).

Same story. Different names. Full `ActionType` list is in the Defender portal — do not invent values.

**Speaker Notes:**  
Outline g. Terminate is Sysmon 5. Do not invent ProcessTerminated on this table. Do not install Sysmon.

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: who ran what, from whom, as whom.

**Given:** `wscript.exe` (Temp `invoice.vbs`) → `powershell.exe -enc …` as `jlee`.

A query names a **specific** pattern — parent + command-line fragment.  
Not “all processes.”

**Speaker Notes:**  
They should see this row before the knowledge check. One sentence: script host launched hidden encoded PowerShell. Parent + command line is the story. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Sysmon Event 10 is a process start. True or false?  
2. `wscript.exe` (Temp `.vbs`) creates `powershell.exe -enc …`. In one sentence, what occurred?  
3. A SIEM query that matches every process is a good “specific process activity” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions for the whole lesson. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Who ran what, from whom, as whom.  
Create, terminate, or access.  
Command line and parent tell the story.  
A query is specific.

**Next:** **1.1.2** File system activity

**Speaker Notes:**  
That hour is the file row on the same host telemetry. Not this process row.
