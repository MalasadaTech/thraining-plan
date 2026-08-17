# Module 1.1.6 – Image and Driver Load Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.6 – Image and Driver Load Activity  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Last 1.1 child. Host load rows. Not a file create. Not Zeek.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read **host** load rows: a module entered a process, or a driver entered the kernel.

Not a file create (**1.1.3**).  
Not a process create (**1.1.2**). Not Zeek (**1.2**).

**Speaker Notes:**  
A DLL can be created in one event and loaded in another.

---

### Slide 3 – User-mode vs kernel
**Title:** User-mode vs kernel

**User-mode** — a process loaded a module (usually a DLL). Sysmon **7**.  
**Kernel** — a driver entered the kernel. Sysmon **6**.

Not a process start.

**Speaker Notes:**  
Outline a. Do not call Event 6 a DLL load.

---

### Slide 4 – Path, hash, signed, who loaded it
**Title:** Path, hash, signed, initiator

**Path** — where it loaded from.  
**Hash** — bytes when present.  
**Signed vs unsigned** — where logged. Empty ≠ unsigned.

**Initiating process** — which process loaded the module.  
Event **6**: do not invent a user-mode parent.

**Speaker Notes:**  
Outline b–c. Signed empty = “not logged.”

---

### Slide 5 – How it shows up
**Title:** Sysmon and MDE

Sysmon **6** / **7**.

MDE `DeviceImageLoadEvents` `ActionType`:  
**ImageLoaded** — a process loaded a module.

Event **7** is often sampled or off. No row → “image load not logged.”  
Full `ActionType` list is in the Defender portal — do not invent values.

**Speaker Notes:**  
Outline d. Do not invent a load from a file-create row.

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: what was loaded, into whom, from where.

**Given:** Sysmon **7**, `powershell.exe` → Temp `update.dll`, `Signed=false`.

A query names a **specific** pattern — path or loader + `.dll` / `.sys`.  
Not “all image loads.”

**Speaker Notes:**  
They should see this row before the knowledge check. PowerShell loaded an unsigned DLL from Temp. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Sysmon Event 6 is a DLL load into a process. True or false?  
2. `powershell.exe` loads Temp `update.dll` (`Signed=false`). In one sentence, what occurred?  
3. A SIEM query that matches every `DeviceImageLoadEvents` row is a good “specific image or driver load” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions for the whole lesson. Stop.

---

### Slide 8 – Summary
**Title:** Summary

A module entered a process, or a driver entered the kernel.  
Path and initiator tell the story.  
A file create is not a load.  
A query is specific.

**Next:** **1.2.1** Zeek concepts

**Speaker Notes:**  
1.1 is done. Zeek is network-sensor telemetry.
