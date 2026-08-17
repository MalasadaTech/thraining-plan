# Instructor Guide – Module 1.1.6 – Image and Driver Load Activity

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.6.1 A / B / C · 1.1.6.2 2b / 3c / 4c · 1.1.6.3 2b / 3c / 4c  
- Hunter: 1.1.6.1 A / B / B · 1.1.6.2 1a / 2b / 3c · 1.1.6.3 1a / 2b / 3c  
- CTI: 1.1.6.1 A / A / A · 1.1.6.2 1a / 1a / 1a · 1.1.6.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read host image- and driver-load telemetry (Sysmon 6 / 7 and MDE `DeviceImageLoadEvents`), describe what occurred, and write a SIEM query for a specific load pattern.

**Key Teaching Points:**
- Endpoint load rows, not Zeek (**1.2**), not Sysmon install, not file create (**1.1.3**).
- User-mode image (7 / `DeviceImageLoadEvents`) vs kernel driver (6).
- Path + hash + signed vs unsigned (where logged).
- Initiating process is the **loader** on user-mode rows. Event 6 has no user-mode parent.
- Stay out of BYOVD / persistence how-to (**2.6**) and “how to enable Event 7.”

**Common Student Challenges:**
- Calling Event 6 a DLL load, or Event 7 a process create.
- Treating a Sysmon 11 file create as proof of load.
- Writing `DeviceImageLoadEvents` with no filter (Event 7 is noisy).
- Inventing `Signed=false` when the field is missing.
- Asking how to enable Event 7 or deploy Sysmon.
- Opening a DLL-sideload / BYOVD lecture.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for 6 vs 7 vs MDE field names
- Optional: one sanitized Event 7 and Event 6 screenshot
- Answer key (this guide)

---

## Learning Objectives

1. Explain user-mode image load vs kernel driver load, plus path, hashes, signed vs unsigned (where logged), and initiating process.
2. Analyze a Sysmon or MDE image or driver load event and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* image or driver load pattern — not “all image loads.”

**Mapped Items:**
- K: 1.1.6.1 – Image and driver load activity concepts
- T: 1.1.6.2 – Analyze an image or driver load event (Sysmon or MDE)
- T: 1.1.6.3 – Create a SIEM query to detect specific image or driver load activity

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Last 1.1 unit; not install |
| What a load event is           | 8 min    | 7 vs 6; not file create |
| Fields + how logged            | 16 min   | a–d on the board |
| Walkthrough Examples           | 14 min   | Students describe first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | Close unit 1.1 |
| **Total**                      | **~70 min** | Stretch Example 3 if they call 6 a DLL |

---

## Detailed Teaching Notes

### 1. What a load event is

**Talking Points:**
- SOC 3 is facts (A / 2b). Push 6 vs 7 and “what occurred” in one sentence.
- SOC 5/7: loader + path + signature story and a query a teammate can run (B/C, 3c/4c).
- Hunter secondary: A / B / B and 1a / 2b / 3c — recognize the row, not own the query bar.
- CTI: A / A / A and 1a / 1a / 1a — nomenclature only. Do not grade them as SOC 5.

**What to emphasize:**
- Empty Signed / no Event 7 = say “not logged,” not “unsigned” or “never loaded.”
- Do not install Sysmon. Do not debate Event 7 policy in this hour.

**Questions to ask:**  
“Did a process load a module, or did the kernel load a driver?”  
“Is this the load row or the file-create row?”

### 2. Fields and logging shape

**Talking Points:**
- Walk outline a–d once.
- Dual-map Sysmon `ImageLoaded` ↔ MDE `FolderPath` + `FileName`. Dual-map Event 7 `Image` ↔ `InitiatingProcessFileName`.
- Hash = bytes of the loaded image. Signed is only usable when the field exists.
- Event 6: no user-mode parent. Do not invent one.

**What to emphasize:**
- Event 7 volume. Queries need a path or signature or loader filter.
- Next unit is Zeek **1.2**. Park protocol questions.

**Question to ask:**  
“If I only give you `helper.dll` and a good SHA256, do you have a story yet?”

### 3. Examples

Work through all three interactively. Students say user-mode vs driver and expected/lead before you read the interpretation.

**Extra point for Example 1:**  
Baseline. Word + signed Office path.

**Extra point for Example 2:**  
Load ≠ create. Unsigned is present and false. Not a sideload lecture.

**Extra point for Example 3:**  
Event 6 ≠ Event 7. Temp `.sys` + unsigned. Not BYOVD theater.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 14–16 minutes.
- Allow use of the Student Guide.
- Grade description + specific queries. Do not grade Sysmon config.
- Review as a group. Do not collect a grade.
- Park file, process, Zeek, registry, and 2.6 labs.

**What good answers look like:**

**Summaries:**
- Example 1: User-mode image; Word → signed `mso.dll` under Program Files; expected.
- Example 2: User-mode image; Word → unsigned `Temp\helper.dll`; lead. File create is a different row.
- Example 3: Driver; unsigned `Temp\helpdesk.sys`; lead. Not a DLL load.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Sysmon 7 Word → signed mso.dll | **User-mode image load** | Event 7 |
| Sysmon 7 Word → Temp helper.dll | **User-mode image load** | Event 7 |
| Sysmon 6 Temp helpdesk.sys | **Driver load** | Event 6 |
| MDE ImageLoaded Word → mso.dll | **User-mode image load** | MDE image load |
| DeviceFileEvents Temp helper.dll | **Not an image/driver load event** | **1.1.3** |
| DeviceProcessEvents explorer → WINWORD | **Not an image/driver load event** | **1.1.2** |

**Pseudo-queries (equivalent is fine):**

```
DeviceImageLoadEvents
| where FileName endswith ".dll"
| where FolderPath has_any (@"\Temp\", @"\AppData\")
```

```
// Sysmon Event ID 6 shape
driver_load
| where ImageLoaded !startswith @"C:\Windows\"
```

A `Signed == false` clause on the first query is fine **only** if they also keep the path filter or note the field may be empty.

Fail a query with no path/signature/loader filter, a `DeviceFileEvents` query, a process-create query, or a Zeek query.

**Analysis card (example — Example 2):**  
User-mode image load (Sysmon 7). Loader: `WINWORD.EXE`. Image: `...\Temp\helper.dll`. Signed=false. Hash not in catalog. Lead because of path + unsigned. Not an incident by itself. The matching Event 11 is a different row.

Fail the card if they only write “DLL sideload,” call Event 6 a DLL, or treat Event 11 as the load.

---

## Knowledge Check – Answer Key

1. **User-mode vs driver? Sysmon IDs?**  
   **Answer:** User-mode image load (Sysmon **7** / MDE `DeviceImageLoadEvents`) = a **process** mapped a module (usually a DLL). Kernel driver load (Sysmon **6**) = a **driver** entered the kernel.  
   **Explanation:** 7 ≠ process create. 6 ≠ DLL load.

2. **Why path + hash + signed together?**  
   **Answer:** Path tells you whether the location is expected. Hash is the bytes when present. Signed/unsigned is only usable when logged. One field is not a story (signed Temp DLL; unsigned with no path).  
   **Explanation:** Same rule as file and process rows.

3. **MDE `InitiatingProcess*`? Event 6 parent?**  
   **Answer:** On `DeviceImageLoadEvents` / Event 7 it is the **process that loaded the module**. Event **6** is kernel-wide — do not invent a user-mode parent.  
   **Explanation:** Same names, different job; 6 is not a process row.

4. **No Event 7 / no DeviceImageLoadEvents, only Event 11?**  
   **Answer:** No. A file create is not a load. Write “image load not logged” and describe the file row as **1.1.3**.  
   **Explanation:** Do not invent a load.

5. **Empty Signed?**  
   **Answer:** Write “signed not logged.” Still use load type, path, initiator (user-mode), and hash if present. Do not write “unsigned.”  
   **Explanation:** Empty ≠ false.

---

## Additional Instructor Resources

- Local note on whether Event 7 / `DeviceImageLoadEvents` exists in the student tenant
- Escalation: file → 1.1.3; persistence / BYOVD → 2.6; protocol → 1.2
- Next recommended module: Zeek concepts (1.2.1)
