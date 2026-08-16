# Instructor Guide – Module 2.6.1 – Persistence Techniques

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.6.1 B / C / C · 2.6.1.1 3c / 4c / 4c  
- SOC: 2.6.1 A / B / B · 2.6.1.1 1a / 2b / 3c  
- CTI: 2.6.1 A / B / B · 2.6.1.1 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on identification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach hunters to name common persistence methods and recognize them in logs or telemetry. Recognition is the task. A full hunt for a named technique is 2.6.3.

**Key Teaching Points:**
- Persistence = runs again (boot, logon, schedule).
- Four outline classes: registry, startup folder, scheduled tasks, other (2.6.1 a–d).
- Recognize with class + proof field (2.6.1.1).
- Expected autoruns are still persistence *mechanisms*.
- Stay out of privilege escalation (2.6.2), hunt-for-specific (2.6.3), ATT&CK remapping (2.5.1), local hunt control (2.7), execute (2.2.1).

**Common Student Challenges:**
- Calling any SYSTEM activity persistence or any SYSTEM task “privesc.”
- Treating a one-off script as persistence.
- Slogan: “they use persistence” with no class.
- Dumping the entire ATT&CK Persistence tactic.
- Writing a hunt plan instead of a recognition card.
- Inventing a method when registry/task logging is missing (visibility gap).

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for a four-row class table
- Optional: one sanitized 4698 / registry / Startup-folder screenshot
- Answer key (this guide)

---

## Learning Objectives

1. Explain common persistence methods: registry, startup folder, scheduled tasks, and a short “other” set.
2. Recognize those methods in logs or telemetry (not a one-off execution, not privilege escalation).
3. Say whether a row looks expected, a lead, or untestable because you cannot see the mechanism.

**Mapped Items:**
- K: 2.6.1 – Persistence techniques
- T: 2.6.1.1 – Recognize persistence techniques in logs or telemetry

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Map (2.5) vs recognize mechanism |
| What persistence is            | 8 min    | Runs again vs one-off vs privesc |
| Four classes                   | 14 min   | a–d on the board; one proof field each |
| Walkthrough Examples           | 14 min   | Students score each card first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~68 min** | Stretch Example 3 if they still call UAC persistence |

---

## Detailed Teaching Notes

### 1. What persistence is

**Talking Points:**
- Ask for last week’s leftover Persistence cell. Name the *mechanism*, not the tactic color.
- Hunter 3 is already at principles (B / 3c). Push class + proof a teammate can check.
- Hunter 2.6.1.1 tops at **4c**, not 4d. Do not invent a 4d on recognition.
- SOC/CTI: K is **A / B / B**; task is **1a / 2b / 3c**. Recognize a real class vs a slogan.

**What to emphasize:**
- Expected vendor Run keys are still registry persistence.
- No log for that class = visibility gap. Do not guess.

**Questions to ask the class:**
- “Will this run again without the operator?”
- “Which class, and which field proves it?”

### 2. Four classes

**Talking Points:**
- Outline a–c get their own rows. Outline d is a *short* other list: service, WMI, logon script. Stop there.
- Registry: hive + key + value + data.
- Startup folder: path + file/lnk + target. User vs All Users.
- Scheduled task: name, run-as, trigger, command. 4698 is a recognition event, not a hunt.
- Other: they must say which other.

**What to emphasize:**
- Same goal, different telemetry. Do not treat all four as “Run keys.”
- ATT&CK IDs are labels if already mapped. This lesson is not 2.5.1.

**Question to ask:**  
“If we only have process-create, which classes can we actually recognize?”

### 3. Examples

Work through all three interactively. Students mark class / expected / lead / not persistence before you read the interpretation.

**Extra point for Example 1:**  
Expected ≠ “not persistence.” Recognition still names the class.

**Extra point for Example 2:**  
4698 is the persistence object. `whoami` is not. SYSTEM on the task is not automatically 2.6.2.

**Extra point for Example 3:**  
UAC / token = park to 2.6.2. WMI consumer = other. Force the word “other” plus the subtype.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 14–16 minutes.
- Allow use of the Student Guide.
- Grade recognition, not a hunt card or a Navigator layer.
- Review as a group. Do not collect a grade.
- Park privesc labs, 2.6.3 execute, and SIEM run.

**What good answers look like:**

**Summaries:**
- Example 1: Registry Run key; expected vendor updater; still that class.
- Example 2: Scheduled-task lead (SYSTEM + Public path); `whoami` not persistence.
- Example 3: A is privesc mislabeled; B is other (WMI) with proof.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| `HKCU\...\Run` → `%APPDATA%\dbg.vbs` | **Registry** | Run key + payload path |
| New `invoice.lnk` in All Users Startup | **Startup folder** | Autorun folder object |
| 4698 SYSTEM + `C:\Users\Public\update.bat` | **Scheduled task** | Task will fire again |
| New WMI EventConsumer CommandLine | **Other** | WMI subscription |
| Single `wscript.exe`, no autorun | **Not persistence** | One-off |
| Token impersonation / UAC bypass | **Not persistence** | **2.6.2** |

**Pseudo-queries (equivalent is fine):**

```
registry
| where (key has @"\CurrentVersion\Run" or key has @"\CurrentVersion\RunOnce")
| where action == "value_set"
| where data !has @"C:\Program Files\"
```

```
windows_events
| where event_id == 4698
| where run_as == "SYSTEM" or command !has @"C:\Program Files\"
```

Fail a query that hunts “all of Persistence,” alerts on every 4698 with no filter, or looks for UAC bypass.

**Recognition card (example answer — Example 2):**  
Class: scheduled-task persistence. Proof: 4698 + `\Microsoft\Windows\UpdateCheck` + SYSTEM + `C:\Users\Public\update.bat` + daily 02:15. Lead: no ticket, user-writable command. Not an incident by itself. Not privesc. Not a hunt plan.

Fail the card if they only write “persistence,” call it 2.6.2, or write a scoped hunt hypothesis as the deliverable.

---

## Knowledge Check – Answer Key

1. **Persistence vs one-off?**  
   **Answer:** Persistence is a method that will run again after reboot, logon, or a time trigger. A one-off process or connection will not.  
   **Explanation:** Will it come back without the operator?

2. **One registry location + field?**  
   **Answer (equivalent):** `HKLM` or `HKCU` `...\CurrentVersion\Run` (or `RunOnce` / Winlogon). Recognize with the **value data** (command/path), plus hive/key.  
   **Explanation:** Key name alone is not proof of the payload.

3. **Startup folder vs Run key?**  
   **Answer:** Same goal (start at logon). Telemetry differs: folder file/`.lnk`/target vs registry value set. User Startup ≠ All Users.  
   **Explanation:** Class follows the object, not the slogan.

4. **What makes a scheduled-task log a lead?**  
   **Answer:** New or changed task plus trigger, run-as, and command you cannot account for (odd name, SYSTEM, user-writable path). Not “tasks exist.”  
   **Explanation:** 4698 is recognition input, not an automatic incident.

5. **One other method; one non-persistence?**  
   **Answer (equivalent):** Other = service, WMI subscription, or logon script. Not persistence here = one-off execution, or privilege escalation (UAC/token) — **2.6.2**.  
   **Explanation:** Outline d is short. Do not swallow 2.6.2.

---

## Additional Instructor Resources

- Same Building C leftover as 2.5 if they still have the task aside
- Escalation: map/coverage → 2.5.1; privesc → 2.6.2; hunt-for-specific → 2.6.3; card format → 2.2.2
- Next recommended module: Privilege escalation techniques (2.6.2)
