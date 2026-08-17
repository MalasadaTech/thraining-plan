# Module 1.1.5 – Registry Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.1.5 – Registry Activity  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Host registry telemetry. Sysmon 12 / 13 / 14 and MDE DeviceRegistryEvents. Not install. Not 2.6.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain hives, key → value, set / delete / rename, initiating process, and Run / Services as examples
2. Analyze a Sysmon or MDE registry event and describe what occurred
3. Write a SIEM query for *specific* registry operations

**Mapped Items:**  
K: 1.1.5.1 | T: 1.1.5.2 | T: 1.1.5.3

**Speaker Notes:**  
SOC 3 is A / 2b. CTI is nomenclature only (A / 1a).

---

### Slide 3 – Agenda
**Title:** Agenda

- What a registry event is
- Hives and key → value
- Set / delete / rename (12 / 13 / 14)
- Run and Services as examples
- Three worked examples
- Identification + two queries
- Knowledge check

**Speaker Notes:**  
2.6 is later. Stay on the registry row.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Sysmon install / XML  
Persistence catalog (Winlogon, IFEO, …) (**2.6.1**)  
File create of `update.exe` (**1.1.3**)  
Zeek `conn` (**1.2**)  
“Every Run write is an incident”

**Key Point:** Describe *this* registry row.

**Speaker Notes:**  
Park 2.6 extras on the board.

---

### Slide 5 – Hive, Key, Value
**Title:** Hive → Key → Value

**Hive** — the tree (`HKLM` / `HKCU`)  
**Key** — the path  
**Value** — name + data

`\REGISTRY\MACHINE\` = `HKLM`  
`\REGISTRY\USER\<SID>\` = that user’s `HKCU`

**Speaker Notes:**  
Write both spellings once. Students mix them up.

---

### Slide 6 – Three Operations
**Title:** Set, Delete, Rename

| Action | Sysmon | MDE |
|--------|--------|-----|
| Written | **13** SetValue; **12** CreateKey | `RegistryValueSet` / `RegistryKeyCreated` |
| Removed | **12** DeleteKey | `Registry*Deleted` |
| Renamed | **14** | `Registry*Renamed` |

**Analyst Tip:** 13 is not a rename. 14 is not a create.

**Speaker Notes:**  
Ask: “Was it written, removed, or renamed?”

---

### Slide 7 – Example Locations
**Title:** Run and Services — Examples Only

`...\Windows\CurrentVersion\Run` and `RunOnce`  
`HKLM\SYSTEM\CurrentControlSet\Services\<name>`

**This lesson:** read the event at that path.  
**2.6.1:** how attackers persist and how to hunt it.

**Speaker Notes:**  
Two paths on the board. Stop. Do not inventory autoruns.

---

### Slide 8 – Initiating Process
**Title:** Who Changed the Registry

Sysmon: `Image`  
MDE: `InitiatingProcess*` = **actor of the registry operation**

**Expected:** `explorer.exe` → its own preference key  
**Lead:** `powershell.exe` / Temp `.exe` → Run or Services

**Speaker Notes:**  
Same field family, different job.

---

### Slide 9 – How It Is Logged
**Title:** Sysmon 12 / 13 / 14 ↔ DeviceRegistryEvents

| Need | Look at |
|------|---------|
| Set | **13** / `RegistryValueSet` |
| Key create/delete | **12** |
| Rename | **14** / Previous* + `NewName` |
| Object | `TargetObject` or `RegistryKey` + value name |
| Data | `Details` / `RegistryValueData` |

**Speaker Notes:**  
Map TargetObject live.

---

### Slide 10 – Example 1: Expected Set
**Title:** Example 1 – Explorer Preference

- MDE `RegistryValueSet`
- HKCU `Explorer\Advanced\Hidden`
- Initiator `explorer.exe`

**Interpretation:**  
Set. Expected. Not persistence.

**Speaker Notes:**  
Students describe the row before you reveal.

---

### Slide 11 – Example 2: Run Set
**Title:** Example 2 – PowerShell → HKCU Run

- Sysmon **13** SetValue
- `...\Run\Updater` = Temp `update.exe`
- Matching Sysmon **11** is a **different** row

**Interpretation:**  
Set **lead**. Name the location. Not a 2.6 lecture.

**Speaker Notes:**  
Force: file create ≠ registry set.

---

### Slide 12 – Example 3: Services Create + Rename
**Title:** Example 3 – Event 12 vs Event 14

**12:** Temp `helpdesk.exe` CreateKey `Services\HelpdeskSvc`  
**14:** same process RenameValue `Run\Updater` → `OneDrive`

**Interpretation:**  
Create-key lead. Rename is a second action.

**Speaker Notes:**  
Park 2.6.1 / 2.6.2.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- Event 14 = set
- Event 12 always = delete
- Query with no filter
- Reciting the persistence catalog
- File or Zeek row as “registry”
- Asking how to deploy Sysmon

**Speaker Notes:**  
Then the exercise.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide.
3. Two queries: script/Office/PowerShell set on Run/RunOnce; Services create/set from outside Windows/Program Files.
4. One analysis card (Example 2 or 3).

**Speaker Notes:**  
Park 2.6, file, Zeek. Review with the Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Set vs delete vs rename? Which Sysmon IDs?
2. Hive vs key vs value? MACHINE vs USER?
3. What is MDE `InitiatingProcess*` on this row?
4. Why are Run / Services only examples here?
5. Empty `Details` — what do you write?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Host registry row: set, delete, or rename.
- Hive + key → value + initiator; data when present.
- Sysmon 12 / 13 / 14 ↔ `DeviceRegistryEvents`.
- Run / Services = example locations. Hunt techniques = **2.6**.
- Next: image and driver load (**1.1.6**).

**Speaker Notes:**  
Do not open a 1.1.6 image-load lab.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Registry Activity — Quick Reference

| Need | Look at |
|------|---------|
| SetValue | Sysmon 13 / `RegistryValueSet` |
| Key create/delete | Sysmon 12 |
| Rename | Sysmon 14 / Previous* |
| Object | `TargetObject` or `RegistryKey` |
| Actor | `Image` / `InitiatingProcess*` |

**Coming next:** Module 1.1.6 – Image and driver load

**Footer:** SOC / Hunter / CTI Training Program
