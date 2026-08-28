# Module 1.1.2 – Process Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.2 – Process Activity  
**Subtitle:** Who ran what on the host  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.1.1 named the five kinds of host activity. This lesson is the process kind. It is not Zeek and not how to install Sysmon.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read **process** events to see who ran what.

Create. Terminate. Who touched whom.  
Not Zeek. Not how to install Sysmon.

**Speaker Notes:**  
This is daily alert work: describe the process event. File and DNS wait for later lessons.

---

### Slide 3 – Create, parent, command line
**Title:** Create, terminate, parent, command line

**Create / terminate** — Sysmon 1 / 5. MDE create is `ProcessCreated`. Terminate is Sysmon 5, not an MDE `ProcessTerminated` value on this table.

**PID, name, command line** — the image name can be fake. The command line is often what actually ran.

**Parent-child** — who launched it. MDE `InitiatingProcess*` is the parent.

**Speaker Notes:**  
Walk create, parent, and command line first. `Office` launching `cmd` is a different event than `explorer` launching `notepad`.

---

### Slide 4 – User, hash, who touched whom
**Title:** User, hash, who touched whom

**Integrity / user** — where logged. Empty is a gap, not “not admin.”

**Hash / original filename** — file bytes vs PE resource. They can disagree.

**Process access** — Sysmon **10**. Source → target. Not a create.

**Speaker Notes:**  
Event 10 is who touched whom. Do not turn it into a credential-dump lesson. Do not treat it as a process start.

---

### Slide 5 – How it shows up
**Title:** Sysmon and MDE

Sysmon **1** / **5** / **10**.

MDE `DeviceProcessEvents` `ActionType`:  
**ProcessCreated** (create). **OpenProcess** (who touched whom).

Same activity. Different field names.  
The full `ActionType` list is in the Defender portal — do not invent values.

**Speaker Notes:**  
Terminate is Sysmon 5. Do not invent `ProcessTerminated` on this MDE table. Do not teach Sysmon install.

---

### Slide 6 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: who ran what, from whom, as whom.

**Given:** `wscript.exe` (Temp `invoice.vbs`) → `powershell.exe -enc …` as `jlee`.

A query names a **specific** pattern — parent + command-line fragment.  
Not “all processes.”

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: script host launched hidden encoded PowerShell. Parent and command line are what you write down. Do not tell the intro plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Sysmon Event 10 is a process start. True or false?  
2. `wscript.exe` (Temp `.vbs`) creates `powershell.exe -enc …`. In one sentence, what occurred?  
3. A SIEM query that matches every process is a good “specific process activity” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Who ran what, from whom, as whom.  
Create, terminate, or access.  
Command line and parent are what you trust.  
A query is specific.

**Next:** **1.1.3** File system activity

**Speaker Notes:**  
1.1.3 is the file event on the same host telemetry. Stay off this process event when you get there.
