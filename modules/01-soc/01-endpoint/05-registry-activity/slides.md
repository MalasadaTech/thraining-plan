# Module 1.1.5 – Registry Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.5 – Registry Activity  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Host registry rows. Not a persistence catalog. Not Sysmon install.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read **host** registry rows: what changed, by whom.

Not a persistence hunt (**2.6**).  
Not Zeek. Not how to install Sysmon.

**Speaker Notes:**  
Describe the set. Hunt techniques wait.

---

### Slide 3 – Hive, key, value
**Title:** Hive, key → value

**Hive** — `HKLM` / `HKCU`, or `\REGISTRY\MACHINE\` / `\REGISTRY\USER\`.  
**Key** — the path.  
**Value** — the named slot plus data.

**Speaker Notes:**  
Outline a. Native prefix and friendly name are the same tree.

---

### Slide 4 – Set, delete, rename, who did it
**Title:** Set, delete, rename, initiator

**Set** — something was written.  
**Delete** — it is gone.  
**Rename** — same object, new name.

**Initiating process** — who changed the key.

**Run / Services** — example **locations**. Not **2.6**.

**Speaker Notes:**  
Outline b–d. Do not inventory every persistence method.

---

### Slide 5 – How it shows up
**Title:** Sysmon and MDE

Sysmon **12** / **13** / **14**.

MDE `DeviceRegistryEvents` `ActionType`:  
**RegistryValueSet**. **RegistryKeyCreated**.  
**Registry*Deleted**. **Registry*Renamed**.

Same story. Different names. Full `ActionType` list is in the Defender portal — do not invent values.

**Speaker Notes:**  
Outline e. Event 13 is SetValue.

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: what happened to which key/value, by whom.

**Given:** Sysmon **13**, `powershell.exe`, `Run\Updater` = Temp `update.exe`.

A query names a **specific** pattern — initiator + key path.  
Not “all registry events.”

**Speaker Notes:**  
They should see this row before the knowledge check. PowerShell set HKCU Run Updater to the Temp path. File create is 1.1.3. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A Run-key row is a finished persistence hunt. True or false?  
2. `powershell.exe` SetValue on HKCU `Run\Updater` = Temp `update.exe`. In one sentence, what occurred?  
3. A SIEM query that matches every `DeviceRegistryEvents` row is a good “specific registry operation” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions for the whole lesson. Stop.

---

### Slide 8 – Summary
**Title:** Summary

What changed in the hive, by whom.  
Key, value, and initiator tell the story.  
Run and Services are locations, not a hunt course.  
A query is specific.

**Next:** **1.1.6** Image and driver load

**Speaker Notes:**  
Last 1.1 child. Then Zeek.
