# Module 2.6.1 – Persistence Techniques

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.6.1 B / C / C · 2.6.1.1 3c / 4c / 4c  
- SOC: 2.6.1 A / B / B · 2.6.1.1 1a / 2b / 3c  
- CTI: 2.6.1 A / B / B · 2.6.1.1 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain common persistence methods: registry, startup folder, scheduled tasks, and a short “other” set.
2. Recognize those methods in logs or telemetry (not a one-off execution, not privilege escalation).
3. Say whether a row looks expected, a lead, or untestable because you cannot see the mechanism.

**Mapped Proficiency Items:**
- K: 2.6.1 – Persistence techniques
- T: 2.6.1.1 – Recognize persistence techniques in logs or telemetry

---

## 1. Key Concepts

### 1.1 What persistence is

**Persistence** is a method that makes code or a command **run again after a reboot, logon, or time trigger** without the operator sitting at the keyboard.

**2.5.1** mapped a hunt to a Persistence technique. This lesson is the next job: **recognize the mechanism** in telemetry. You are not writing a full hunt for a named technique (**2.6.3**). You are not teaching privilege escalation (**2.6.2**).

| Persistence | Not persistence |
|-------------|-----------------|
| Something will start again on boot, logon, or a schedule | A one-off process, script, or network connection |
| Autorun location, task, service, or subscription you can name | Privilege change by itself (token, UAC bypass) — **2.6.2** |
| Expected updater Run key *and* a new SYSTEM task in `C:\Users\Public` | “They use persistence” with no method |

**Most critical distinction for daily work:**  
Name the **class** (registry / startup folder / scheduled task / other) and the **field that proves it**. A slogan is not recognition.

If you have no telemetry for that class, name a **visibility gap**. Do not invent a method so the card looks complete.

### 1.2 Registry, startup folder, scheduled tasks, other

Four classes. Same goal: survive. Different places, different logs.

| Class | Typical place | What recognition looks like | Common ATT&CK label (if you already mapped it) |
|-------|---------------|-----------------------------|------------------------------------------------|
| **Registry-based** | `HKCU`/`HKLM` `...\Run`, `RunOnce`, Winlogon `Userinit` / `Shell` | Registry value **set** or **changed**; image path is the payload | T1547.001 (Run keys) |
| **Start menu / startup folder** | User or All Users `...\Start Menu\Programs\Startup\` | File create / `.lnk` / script dropped in that folder | T1547.001 (Startup folder) |
| **Scheduled tasks** | Task Scheduler; `schtasks`; XML under `\Microsoft\Windows\...` | Task **created** or **updated**; trigger + command + run-as | T1053.005 |
| **Other common methods** | New/changed **service**; **WMI** event subscription; **logon script** | Service install; permanent WMI consumer; user/GPO logon script path | T1543.003 / T1546.003 / T1037 |

You do not owe every Persistence technique in ATT&CK. These four classes are the floor.

| Class | Expected (usually) | Lead (usually) |
|-------|--------------------|----------------|
| Registry | Known vendor updater under `Program Files` | New Run value to a user-writable path |
| Startup folder | User added a documented shortcut | New `.lnk` or `.vbs` in All Users Startup |
| Scheduled task | Named IT task, signed binary, documented schedule | New SYSTEM task, odd name, command not under `Program Files` |
| Other | Catalogued service / known GPO script | New service or WMI subscription you cannot account for |

**Registry:** look at hive + key + value name + data (command). `HKCU\...\Run` is per-user. `HKLM\...\Run` is machine-wide. `RunOnce` fires once and is still persistence until it runs.

**Startup folder:** same idea as a Run key, different object. User Startup ≠ All Users Startup. A `.lnk` is enough. The target of the shortcut is the payload.

**Scheduled tasks:** look at **task name**, **author**, **run-as** (user vs SYSTEM), **trigger**, and **command**. A 4698 / task-create on a host that had none is a recognition event. “Scheduled tasks exist on Windows” is not.

**Other:** say which other. A **service** that starts automatically. A **WMI** filter/consumer that launches a command. A **logon script** in the user object or GPO. Do not dump the rest of TA0003.

How you *hunt* a named technique end-to-end is **2.6.3**. Local hunt control is **2.7**. Stay here: class + proof in the log.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Expected Run key)

**Telemetry (registry):**

| Field | Value |
|-------|--------|
| Event | Registry value set |
| Key | `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |
| Value | `VendorUpdate` |
| Data | `"C:\Program Files\Vendor\update.exe" /silent` |
| Image | `C:\Program Files\Vendor\update.exe` |
| Host | Laptop-14 (standard build) |
| Note | Same value on the gold image; signed binary |

**Recognition card**

| Field | What they wrote |
|-------|-----------------|
| Class | **Registry-based** persistence (Run key) |
| Proof | `HKLM\...\Run` value `VendorUpdate` → known `Program Files` path |
| Expected vs lead | **Expected** — catalogued updater. Still persistence *as a method* |
| Not done | Did not call it an incident. Did not open a Persistence hunt (**2.6.3**). Did not map the whole tactic (**2.5.1** already done if needed) |

**Interpretation:**  
You recognized the class. Expected autoruns still count as persistence mechanisms. Recognition ≠ escalate.

### Example 2: After-Hours SYSTEM Task (Lead)

A hunt channel paste:

> Building C-12, 02:17. Event 4698. Task `\Microsoft\Windows\UpdateCheck`. Run as **SYSTEM**. Command `C:\Users\Public\update.bat`. Trigger daily 02:15. No matching change ticket.

Compare a one-off on the same host:

> 02:16. `cmd.exe` ran `whoami`. No task create. No Run key. No Startup file.

**Recognition card (the 4698)**

| Field | What they wrote |
|-------|-----------------|
| Class | **Scheduled-task** persistence |
| Proof | New task + trigger + SYSTEM + command on a user-writable path |
| Expected vs lead | **Lead** — odd name, SYSTEM, Public folder. Not an automatic incident |
| Not the `whoami` | One-off execution. Not persistence |

**Interpretation:**  
The task will run again. That is why it is persistence. The `whoami` will not. Do not execute a scoped hunt here (**2.6.3**). Do not call SYSTEM “privilege escalation” just because the task is SYSTEM — the *method* is a scheduled task.

### Example 3: Wrong Class + Other Method (Lead)

**Write-up A**

> UAC bypass and token impersonation. Persistence. Hunt TA0003.

**Write-up B**

> Sysmon: new WMI EventFilter + CommandLine EventConsumer launching `C:\ProgramData\sync.vbs` at logon. Class: **other** (WMI subscription). Lead — permanent consumer, not a one-off `wscript`. Not privesc (**2.6.2**). Not a Startup-folder event (wrong path).

**Interpretation:**  
A names privilege-escalation methods and calls them persistence. B names an **other** common method and the fields that prove it will fire again. Recognition stops at the class and the proof.

---

## 3. Hands-On Exercise

**Objective:** Practice naming persistence classes and recognizing them in telemetry.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (class, expected vs lead, or not persistence).
2. For each item below, say **registry**, **startup folder**, **scheduled task**, **other**, or **not persistence**. Give one reason.
   - `HKCU\...\Run` value `Debug` → `%APPDATA%\dbg.vbs`
   - New `invoice.lnk` in All Users `...\Startup\`
   - Event 4698, SYSTEM, command `C:\Users\Public\update.bat`
   - New WMI EventConsumer CommandLine at logon
   - Single `wscript.exe` launch, no autorun object
   - Token impersonation / UAC bypass
3. Write **two SIEM-style pseudo-queries** that would *surface candidates to recognize* (not a full hunt):
   - One for **registry Run / RunOnce** value set, excluding a short allow-list of known updater paths.
   - One for **scheduled-task create** (e.g. 4698) where run-as is SYSTEM or the command is not under `Program Files`.
4. Write **one recognition card** (small table or four sentences): class, proof field(s), expected vs lead. Use Example 2 or the WMI row. Do not write a hunt plan. Do not explain privilege escalation. Do not execute the search.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- Two recognition-oriented pseudo-queries
- One card that names the class and the proof, not a slogan

---

## 4. Knowledge Check

1. What makes an action **persistence** rather than one-off execution?
2. Name one **registry-based** persistence location and the field you would use to recognize it.
3. How is **startup-folder** persistence the same as a Run key, and how is the telemetry different?
4. What in a **scheduled-task** log makes it a persistence lead, not “Windows has tasks”?
5. Give one **other** common persistence method, and one activity that is **not** persistence in this lesson.

---

## 5. Summary

- Persistence = the method will run again (boot, logon, or schedule).
- Four classes here: registry, startup folder, scheduled task, other (service / WMI / logon script).
- Recognize with a named class and a proof field. Expected autoruns are still that class.
- One-off processes are not persistence. Privilege escalation is **2.6.2**.
- No telemetry for the class → visibility gap, not a guessed method.
- Next: privilege escalation techniques (**2.6.2**). Hunt-for-specific is **2.6.3**.

---

## 6. References & Further Reading

- Related modules:
  - 2.5.1 – Using MITRE ATT&CK for hunt planning (map the hunt)
  - 2.6.2 – Privilege escalation techniques (next)
  - 2.6.3 – Hunt for a specific persistence or privilege-escalation technique
  - 2.2.2 – Hunt development (hypothesis / scope)
- Local Windows logging / EDR field guide used in class (optional)
- MITRE ATT&CK — only as labels for methods you actually recognized
