# Instructor Guide – Module 1.1.1 – Process Activity

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.1.1 A / B / C · 1.1.1.2 2b / 3c / 4c · 1.1.1.3 2b / 3c / 4c  
- Hunter: 1.1.1.1 A / B / B · 1.1.1.2 1a / 2b / 3c · 1.1.1.3 1a / 2b / 3c  
- CTI: 1.1.1.1 A / A / A · 1.1.1.2 1a / 1a / 1a · 1.1.1.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read host process telemetry (Sysmon 1 / 5 / 10 and MDE `DeviceProcessEvents`), describe what occurred, and write a SIEM query for a specific process pattern.

**Key Teaching Points:**
- Endpoint process rows, not Zeek (**1.2**), not Sysmon install.
- Create vs terminate vs process access (10 = who touched whom).
- Parent + command line often beat image name and hash.
- MDE `InitiatingProcess*` = parent.
- Stay out of file / host-network / registry / image-load (1.1.2–1.1.5) and persistence how-to (2.6).

**Common Student Challenges:**
- Treating every `powershell.exe` as malicious (hash is often fine).
- Calling Event 10 a process create.
- Writing `DeviceProcessEvents` with no filter.
- Jumping to file, DNS, or Run keys.
- Asking how to deploy Sysmon.
- Calling a SYSTEM child “privesc” without staying on the process description.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for Sysmon 1 / 5 / 10 vs MDE field names
- Optional: one sanitized Event 1 and Event 10 screenshot
- Answer key (this guide)

---

## Learning Objectives

1. Explain process create, terminate, parent-child, command line, integrity/user, hashes/original filename, and process access.
2. Analyze a Sysmon or MDE process event and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* process pattern — not “all processes.”

**Mapped Items:**
- K: 1.1.1.1 – Process activity concepts
- T: 1.1.1.2 – Analyze a process event (Sysmon or MDE)
- T: 1.1.1.3 – Create a SIEM query to detect specific process activity

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Host vs Zeek; not install |
| What a process event is        | 8 min    | Create / terminate / access |
| Fields + how logged            | 16 min   | a–g on the board; MDE name map |
| Walkthrough Examples           | 14 min   | Students describe first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~70 min** | Stretch Example 3 if they call 10 a create |

---

## Detailed Teaching Notes

### 1. What a process event is

**Talking Points:**
- SOC 3 is facts (A / 2b). Push field names and “what occurred” in one sentence.
- SOC 5/7: parent+cmdline story and a query a teammate can run (B/C, 3c/4c).
- Hunter secondary: A / B / B and 1a / 2b / 3c — recognize the row, not own the query bar.
- CTI: A / A / A and 1a / 1a / 1a — nomenclature only. Do not grade them as SOC 5.

**What to emphasize:**
- Empty integrity / original filename = say “not logged,” not “not admin.”
- Do not install Sysmon in this hour.

**Questions to ask:**  
“Who started this, and what is the command line?”  
“Is this a create or a touch?”

### 2. Fields and logging shape

**Talking Points:**
- Walk outline a–g once. Event 10 is *in this lesson*, not a sixth unit.
- Dual-map Sysmon ParentImage ↔ MDE `InitiatingProcessFileName` live.
- Hash = bytes. Original filename = PE resource. On-disk name can lie.
- Process access: source → target. Stop before credential-dump theater.

**What to emphasize:**
- PID is per-host and reused. Do not treat it as a global ID.
- Next activity types are later 1.1.x. Park them on the board.

**Question to ask:**  
“If I only give you `powershell.exe` and a good SHA256, do you have a story yet?”

### 3. Examples

Work through all three interactively. Students say create/terminate/access and expected/lead before you read the interpretation.

**Extra point for Example 1:**  
Baseline. Parent Explorer + matching original filename.

**Extra point for Example 2:**  
Good hash, bad chain. Terminate does not erase the create.

**Extra point for Example 3:**  
Event 10 ≠ Event 1. Source is user-writable. Not a Mimikatz lecture.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 14–16 minutes.
- Allow use of the Student Guide.
- Grade description + specific queries. Do not grade Sysmon config.
- Review as a group. Do not collect a grade.
- Park file, Zeek, registry, and 2.6 labs.

**What good answers look like:**

**Summaries:**
- Example 1: Create; Explorer → Notepad; expected.
- Example 2: Create; wscript Temp vbs → hidden encoded PowerShell; lead. Terminate only closes the PID.
- Example 3: Process access; Temp helpdesk.exe → LSASS; lead, not a create.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Sysmon 1 Explorer → Notepad | **Create** | Event 1 |
| Sysmon 5 powershell PID exit | **Terminate** | Event 5 |
| Sysmon 10 helpdesk → lsass | **Process access** | Event 10 |
| MDE ProcessCreated wscript → powershell -enc | **Create** | MDE create |
| DeviceFileEvents Temp file | **Not a process event** | **1.1.2** |
| Zeek conn 443 | **Not a process event** | **1.2** |

**Pseudo-queries (equivalent is fine):**

```
DeviceProcessEvents
| where ActionType == "ProcessCreated"
| where FileName in ("powershell.exe", "cmd.exe")
| where InitiatingProcessFileName in ("wscript.exe", "cscript.exe", "winword.exe", "excel.exe", "outlook.exe")
```

```
// Sysmon Event ID 10 shape
process_access
| where TargetImage endswith @"\lsass.exe"
| where SourceImage !startswith @"C:\Windows\"
    and SourceImage !startswith @"C:\Program Files\"
```

Fail a query with no parent/command-line/target filter, a file-table query, or a Zeek `conn` query.

**Analysis card (example — Example 2):**  
Create (`ProcessCreated`). Parent: `wscript.exe` + Temp `invoice.vbs`. Child: `powershell.exe -NoP -W Hidden -enc …`. User `jlee`. Hash is stock PowerShell. Lead because of parent + command line. Not an incident by itself.

Fail the card if they only write “malicious PowerShell,” call Event 10 a create, or add a Run-key hunt.

---

## Knowledge Check – Answer Key

1. **Create vs terminate vs access?**  
   **Answer:** Create (Sysmon 1 / MDE `ProcessCreated`) = a process started. Terminate (Sysmon 5 / `ProcessTerminated`) = that PID ended. Process access (Sysmon 10) = one process opened another (who touched whom).  
   **Explanation:** Access is not a start.

2. **Why command line (and parent command line)?**  
   **Answer:** Image name and even hash are often a legitimate binary. Command line and parent tell *how* and *from whom* it ran (`-enc`, Temp script, Office parent).  
   **Explanation:** Name can lie; chain is the story.

3. **MDE `InitiatingProcess*`?**  
   **Answer:** The **parent** (who started the process). The child is `FileName` / `ProcessCommandLine` / process SHA256.  
   **Explanation:** Same as Sysmon Parent* vs Image.

4. **What Event 10 adds vs Event 1?**  
   **Answer:** Event 1 is a create. Event 10 is a handle from SourceImage to TargetImage (e.g. LSASS) without starting the target.  
   **Explanation:** Who touched whom.

5. **Missing integrity / original filename?**  
   **Answer:** Write “not logged” (visibility). Still use parent, command line, user, path, and hash if present.  
   **Explanation:** Do not invent fields.

---

## Additional Instructor Resources

- Local expected parents for `powershell.exe` / `cmd.exe` if you have a list
- Escalation: file → 1.1.2; host network → 1.1.3; Zeek → 1.2; persistence → 2.6
- Next recommended module: File system activity (1.1.2)
