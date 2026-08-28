# Module 1.1.6 – Image and Driver Load Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.6 – Image and Driver Load Activity  
**Subtitle:** A module or driver loaded on the host  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.1.5 was registry activity. This lesson is the image and driver load kind. It is not a file create, not Zeek, and not how to install Sysmon.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read **image and driver load** events to see that a module entered a process, or that a driver entered the kernel.

What was loaded. Into whom. From where.  
Not a file create. Not Zeek. Not how to install Sysmon.

**Speaker Notes:**  
This is daily alert work: describe the load event. Creating a DLL is a file event. Loading it is this lesson. Persistence and BYOVD wait.

---

### Slide 3 – User-mode vs kernel
**Title:** User-mode vs kernel

**User-mode** — a process loaded a module (usually a DLL). Sysmon **7**.  
**Kernel** — a driver entered the kernel. Sysmon **6**.

Not a process start.

**Speaker Notes:**  
Walk this split first. Event 6 is not a DLL load into a process, and it has no user-mode parent. Event 7 `Image` is the process; `ImageLoaded` is the module.

---

### Slide 4 – Path, hash, signed, who loaded it
**Title:** Path, hash, signed, initiator

**Path** — where it loaded from.  
**Hash** — loaded bytes when present.  
**Signed vs unsigned** — where logged. Empty is a gap, not “unsigned.”

**Initiating process** — which process loaded the module.  
Event **6**: do not invent a user-mode parent.

**Speaker Notes:**  
Path and initiator are what you write down. If Signed is empty, say it was not logged. Do not call that unsigned.

---

### Slide 5 – How it shows up
**Title:** Sysmon and MDE

Sysmon **6** / **7**.

MDE `DeviceImageLoadEvents` `ActionType`:  
**ImageLoaded** — a process loaded a module.

That MDE table is DLL loads, not kernel drivers.  
Event **7** is often sampled or off. No event → “image load not logged.”  
Full `ActionType` list is in the Defender portal — do not invent values.

**Speaker Notes:**  
Do not invent a load from a file-create event. Do not treat a `.sys` path on `DeviceImageLoadEvents` as Event 6. Driver load is Sysmon 6. Do not teach Sysmon install.

---

### Slide 6 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: what was loaded, into whom, from where.

**Given:** Sysmon **7**, `powershell.exe` → Temp `update.dll`, `Signed=false`.

A query names a **specific** pattern — process + path, or Event **6** + driver path.  
Not every image or driver load.

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: PowerShell loaded an unsigned DLL from Temp. Path and initiator are what you write down. Do not tell the intro plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Sysmon Event 6 is a DLL load into a process. True or false?  
2. `powershell.exe` loads Temp `update.dll` (`Signed=false`). In one sentence, what occurred?  
3. A SIEM query that matches every image or driver load event is a good “specific image or driver load” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

A module entered a process, or a driver entered the kernel.  
Path and initiator tell the story.  
A file create is not a load.  
A query is specific.

**Next:** **1.2.1** Zeek concepts

**Speaker Notes:**  
1.1 host activity is done. Zeek is network-sensor telemetry, not another host event.
