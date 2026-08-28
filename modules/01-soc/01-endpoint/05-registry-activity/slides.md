# Module 1.1.5 – Registry Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.5 – Registry Activity  
**Subtitle:** What changed in a key or value  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.1.1 named the five kinds of host activity. This lesson is the registry kind. It is not a persistence catalog, not Zeek, and not how to install Sysmon.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read **registry** events to see what changed in a key or value, and which process changed it.

Set. Delete. Rename.  
Not a persistence catalog. Not Zeek. Not how to install Sysmon.

**Speaker Notes:**  
This is daily alert work: describe the registry event. Persistence techniques wait for a later lesson. File and process write-ups wait too.

---

### Slide 3 – Hive, key, value
**Title:** Hive, key, value

**Hive** — `HKLM` / `HKCU`, or `\REGISTRY\MACHINE\` / `\REGISTRY\USER\`.  
**Key** — the path.  
**Value** — the named slot plus data.

Sysmon often writes `HKU\<SID>` for the user hive. That is the same tree as HKCU.

**Speaker Notes:**  
Walk hive vs key vs value first. Native prefix and friendly name are the same tree. Do not teach every hive in Windows.

---

### Slide 4 – Set, delete, rename, who did it
**Title:** Set, delete, rename, initiator

**Set** — something was written.  
**Delete** — it is gone.  
**Rename** — same object, new name.

**Initiating process** — who changed the key.

**Run / Services** — example **locations**. Not a persistence catalog.

**Speaker Notes:**  
Name Run or Services when that is where the change sat. Do not inventory every persistence method. Who changed the key is this event, not a process-create write-up.

---

### Slide 5 – How it shows up
**Title:** Sysmon and MDE

Sysmon **12** / **13** / **14**.

MDE `DeviceRegistryEvents` `ActionType`:  
**RegistryValueSet**. **RegistryKeyCreated**.  
**RegistryKeyDeleted** / **RegistryValueDeleted**. **RegistryKeyRenamed**.

Same activity. Different field names.  
The full `ActionType` list is in the Defender portal — do not invent values.

**Speaker Notes:**  
Event 13 is SetValue. Event 12 is create or delete. Event 14 is rename. Do not invent `RegistryValueRenamed` on this MDE table. Do not teach Sysmon install.

---

### Slide 6 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: what happened to which key/value, by whom.

**Given:** Sysmon **13**, `powershell.exe`, `Run\Updater` = Temp `update.exe`.

A query names a **specific** pattern — initiator + key path.  
Not “all registry events.”

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: PowerShell set HKCU Run value Updater to that Temp path. The file create of update.exe is a different event. Do not tell the intro plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A Run-key event is a finished persistence hunt. True or false?  
2. `powershell.exe` SetValue on HKCU `Run\Updater` = Temp `update.exe`. In one sentence, what occurred?  
3. A SIEM query that matches every registry event is a good “specific registry operation” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

What changed in the hive, by whom.  
Set, delete, or rename.  
Key, value, and initiator are what you write down.  
Run and Services are locations, not a hunt course.  
A query is specific.

**Next:** **1.1.6** Image and driver load

**Speaker Notes:**  
1.1.6 is the load event on the same host telemetry. Stay off this registry event when you get there.
