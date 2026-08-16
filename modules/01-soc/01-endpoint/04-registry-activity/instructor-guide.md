# Instructor Guide – Module 1.1.4 – Registry Activity

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.4.1 A / B / C · 1.1.4.2 2b / 3c / 4c · 1.1.4.3 2b / 3c / 4c  
- Hunter: 1.1.4.1 A / B / B · 1.1.4.2 1a / 2b / 3c · 1.1.4.3 1a / 2b / 3c  
- CTI: 1.1.4.1 A / A / A · 1.1.4.2 1a / 1a / 1a · 1.1.4.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read host registry telemetry (Sysmon 12 / 13 / 14 and MDE `DeviceRegistryEvents`), describe what occurred, and write a SIEM query for a specific registry operation.

**Key Teaching Points:**
- Endpoint registry rows, not Zeek (**1.2**), not Sysmon install, not 1.1.1–1.1.3.
- Hive + key → value. Set vs delete vs rename.
- Run and Services are **example locations**, not a **2.6** dump.
- Initiating process is who changed the registry.
- Stay out of image-load (**1.1.5**) and persistence how-to (**2.6**).

**Common Student Challenges:**
- Treating every Run write as a closed incident.
- Calling Event 12 a SetValue, or Event 14 a create.
- Writing `DeviceRegistryEvents` with no filter.
- Reciting Winlogon / IFEO / AppInit — park it for **2.6.1**.
- Asking how to deploy Sysmon.
- Mixing the file-create of `update.exe` into the registry card.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for hive prefixes and 12 / 13 / 14 vs MDE `ActionType`
- Optional: one sanitized Event 13 Run screenshot
- Answer key (this guide)

---

## Learning Objectives

1. Explain registry hives, key → value, set / delete / rename, initiating process, and how Run / Services appear as examples.
2. Analyze a Sysmon or MDE registry event and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* registry operation — not “all registry events.”

**Mapped Items:**
- K: 1.1.4.1 – Registry activity concepts
- T: 1.1.4.2 – Analyze a registry event (Sysmon or MDE)
- T: 1.1.4.3 – Create a SIEM query to detect specific registry operations

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Not 2.6; not install |
| What a registry event is       | 8 min    | Hive / key / value |
| Fields + how logged            | 16 min   | a–e; 12/13/14 map |
| Walkthrough Examples           | 14 min   | Students describe first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~70 min** | Stretch Example 2 if they start a 2.6 lecture |

---

## Detailed Teaching Notes

### 1. What a registry event is

**Talking Points:**
- SOC 3 is facts (A / 2b). Push hive/key/value and “what occurred” in one sentence.
- SOC 5/7: initiator + location + action story and a query a teammate can run (B/C, 3c/4c).
- Hunter secondary: A / B / B and 1a / 2b / 3c — recognize the row, not own the query bar.
- CTI: A / A / A and 1a / 1a / 1a — nomenclature only. Do not grade them as SOC 5.

**What to emphasize:**
- Empty `Details` / value data = say “not logged,” not “empty value.”
- Do not install Sysmon. Do not teach the persistence catalog.

**Questions to ask:**  
“What changed, under which key, and which process did it?”  
“Is this a set, a delete, or a rename?”

### 2. Fields and logging shape

**Talking Points:**
- Walk outline a–e once. c is examples only — write Run and Services on the board, then stop.
- Dual-map `\REGISTRY\MACHINE\` ↔ `HKLM`, `\REGISTRY\USER\<SID>\` ↔ that user’s `HKCU`.
- Dual-map `TargetObject` ↔ `RegistryKey` + `RegistryValueName`. `Details` ↔ `RegistryValueData`.
- 13 = SetValue. 12 = CreateKey / DeleteKey. 14 = rename. Students collapse these.

**What to emphasize:**
- A Run value pointing at Temp is a **described lead**, not a 2.6 sign-off.
- Image load is **1.1.5**. Park it.

**Question to ask:**  
“If I only give you the string `Run`, do you have a story yet?”

### 3. Examples

Work through all three interactively. Students say set/delete/rename and expected/lead before you read the interpretation.

**Extra point for Example 1:**  
Baseline. Explorer writing its own preference key.

**Extra point for Example 2:**  
SetValue + HKCU Run + Temp path. File create is a different row. Not a 2.6 lecture.

**Extra point for Example 3:**  
CreateKey ≠ SetValue. Rename is Event 14. Services is an example location. Not 2.6.2.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 14–16 minutes.
- Allow use of the Student Guide.
- Grade description + specific queries. Do not grade Sysmon config or a persistence paper.
- Review as a group. Do not collect a grade.
- Park file, Zeek, image-load, and 2.6 labs.

**What good answers look like:**

**Summaries:**
- Example 1: Set; Explorer → HKCU Explorer\Advanced; expected.
- Example 2: Set; PowerShell → HKCU Run `Updater` = Temp `update.exe`; lead.
- Example 3: Create (key); Temp `helpdesk.exe` → HKLM Services\HelpdeskSvc; lead. Event 14 is a rename.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Sysmon 13 PowerShell Run\Updater | **Set** | Event 13 SetValue |
| Sysmon 12 helpdesk Services key | **Create** | Event 12 CreateKey |
| Sysmon 14 RenameValue Run\Updater → OneDrive | **Rename** | Event 14 |
| MDE RegistryValueSet Explorer preference | **Set** | MDE set |
| DeviceFileEvents Temp `update.exe` | **Not a registry event** | **1.1.2** |
| Zeek `conn` 443 | **Not a registry event** | **1.2** |

If a student marks Event 12 as “delete,” correct them: 12 is create **or** delete; this row is `CreateKey`.

**Pseudo-queries (equivalent is fine):**

```
DeviceRegistryEvents
| where ActionType == "RegistryValueSet"
| where RegistryKey has_any (@"\CurrentVersion\Run", @"\CurrentVersion\RunOnce")
| where InitiatingProcessFileName in (
    "powershell.exe", "wscript.exe", "cscript.exe",
    "winword.exe", "excel.exe", "outlook.exe")
```

```
DeviceRegistryEvents
| where ActionType in ("RegistryKeyCreated", "RegistryValueSet")
| where RegistryKey has @"\CurrentControlSet\Services\"
| where InitiatingProcessFolderPath !startswith @"C:\Windows\"
    and InitiatingProcessFolderPath !startswith @"C:\Program Files\"
```

Fail a query with no key/initiator filter, a file-table query, a Zeek query, or a 2.6 hunt write-up instead of a query.

**Analysis card (example — Example 2):**  
Set (Sysmon 13 SetValue). Hive/key: that user’s `...\Run`. Value `Updater` = `...\Temp\update.exe`. Initiator: `powershell.exe`. Lead because of initiator + Run location + Temp data. Not an incident by itself. Not a 2.6 sign-off.

Fail the card if they only write “persistence,” call Event 13 a rename, or list five other autorun keys.

---

## Knowledge Check – Answer Key

1. **Set vs delete vs rename? Sysmon IDs?**  
   **Answer:** Set (Sysmon **13** SetValue / MDE `RegistryValueSet`, and **12** CreateKey / MDE key created) = something was written. Delete (Sysmon **12** DeleteKey / MDE *Deleted) = it is gone. Rename (Sysmon **14** / MDE *Renamed) = new name; read `NewName` / Previous*.  
   **Explanation:** 13 is value set. 12 is key create or delete. 14 is rename.

2. **Hive, key, value? MACHINE vs USER?**  
   **Answer:** Hive = the tree (`HKLM` / `HKCU`). Key = the path. Value = name + data under that key. `\REGISTRY\MACHINE\` is `HKLM`. `\REGISTRY\USER\<SID>\` is that user’s `HKCU`.  
   **Explanation:** Same locations, two spellings.

3. **MDE `InitiatingProcess*` on a registry event?**  
   **Answer:** **Who performed the registry operation.** The object is `RegistryKey` / `RegistryValueName` / data.  
   **Explanation:** Same names as 1.1.1–1.1.3, different job.

4. **Why Run / Services as examples?**  
   **Answer:** They are locations that often appear on important rows. This lesson is how to **read the event**. Persistence techniques and how to hunt them are **2.6.1**.  
   **Explanation:** Outline c, not a 2.6 dump.

5. **Empty Details?**  
   **Answer:** Write “value data not logged.” Still use EventType/ActionType, `TargetObject` / key + value name, and initiating process.  
   **Explanation:** Do not invent the data.

---

## Additional Instructor Resources

- Local expected installer / `msiexec` service-key patterns if you have a list
- Escalation: file → 1.1.2; host network → 1.1.3; persistence hunt → 2.6.1
- Next recommended module: Image and driver load (1.1.5)
