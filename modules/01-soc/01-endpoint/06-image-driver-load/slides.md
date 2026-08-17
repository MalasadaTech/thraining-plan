# Module 1.1.6 – Image and Driver Load Activity  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.1.6 – Image and Driver Load Activity  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Host image/driver load. Sysmon 6 / 7 and MDE DeviceImageLoadEvents. Not install. Not file create.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain user-mode image load vs kernel driver load, plus path, hash, signed vs unsigned (where logged), and initiating process
2. Analyze a Sysmon or MDE image or driver load event and describe what occurred
3. Write a SIEM query for *specific* image or driver load activity

**Mapped Items:**  
K: 1.1.6.1 | T: 1.1.6.2 | T: 1.1.6.3

**Speaker Notes:**  
SOC 3 is A / 2b. CTI is nomenclature only (A / 1a). Last 1.1 unit.

---

### Slide 3 – Agenda
**Title:** Agenda

- What a load event is
- User-mode vs kernel driver
- Path, hash, signed vs unsigned
- Sysmon 6 / 7 and DeviceImageLoadEvents
- Three worked examples
- Identification + two queries
- Knowledge check

**Speaker Notes:**  
1.2 Zeek is the next unit. Stay on the load row.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Sysmon install / “enable Event 7”  
File create of `helper.dll` (**1.1.3**)  
Process create of Word (**1.1.2**)  
BYOVD / sideload hunt methodology (**2.6**)  
Zeek `files` / `conn` (**1.2**)

**Key Point:** Describe *this* load row.

**Speaker Notes:**  
Park deploy and 2.6 questions on the board.

---

### Slide 5 – Two Load Types
**Title:** User-Mode Image vs Kernel Driver

| Load | Sysmon | MDE |
|------|--------|-----|
| Module into a process (DLL) | **7** | `DeviceImageLoadEvents` |
| Driver into the kernel | **6** | *(driver row — Sysmon-shaped)* |

**Analyst Tip:** 6 is not a DLL. 7 is not a process create.

**Speaker Notes:**  
Ask: “Process loaded a module, or kernel loaded a driver?”

---

### Slide 6 – Path, Hash, Signature
**Title:** Where, Bytes, Signed (If Logged)

**Path** — `Program Files` vs `Temp` / `AppData`  
**SHA256** — the loaded image, when present  
**Signed / Signature / SignatureStatus** — only if the field exists

Empty Signed → write “not logged.” Do not write “unsigned.”

**Speaker Notes:**  
Signed Temp DLL is still a path lead.

---

### Slide 7 – Initiating Process
**Title:** Who Loaded It

Event **7** / MDE: `Image` / `InitiatingProcess*` = the **loader**  
Event **6**: kernel driver — **do not invent** a user-mode parent

**Expected:** `WINWORD.EXE` → signed Office DLL  
**Lead:** Word / PowerShell → Temp `.dll`

**Speaker Notes:**  
Same field family, different job.

---

### Slide 8 – Visibility
**Title:** Event 7 May Be Missing

Event **7** is noisy. Many tenants sample it or omit it.

No 7 / no `DeviceImageLoadEvents` → write “image load not logged.”  
A Sysmon **11** file create is **not** a load.

**Speaker Notes:**  
Do not debate config. Describe what they have.

---

### Slide 9 – How It Is Logged
**Title:** Sysmon 6 / 7 ↔ DeviceImageLoadEvents

| Need | Look at |
|------|---------|
| User-mode load | **7** / `ImageLoaded` |
| Driver | **6** |
| Object | `ImageLoaded` or `FolderPath` + `FileName` |
| Loader (7) | `Image` / `InitiatingProcess*` |
| Trust | `Signed` / `Signature` when present |

**Speaker Notes:**  
Map ImageLoaded live.

---

### Slide 10 – Example 1: Expected Load
**Title:** Example 1 – Word → mso.dll

- MDE `ImageLoaded`
- `Program Files\...\Office16\mso.dll`
- Signed Microsoft (where logged)
- Hash matches catalog

**Interpretation:**  
User-mode image. Expected. Not an incident.

**Speaker Notes:**  
Students describe the row before you reveal.

---

### Slide 11 – Example 2: Temp DLL
**Title:** Example 2 – Word → Temp helper.dll

- Sysmon **7**
- `Signed=false`
- Matching Sysmon **11** is a **different** row

**Interpretation:**  
User-mode **lead** because of path + unsigned.

**Speaker Notes:**  
Force: create ≠ load.

---

### Slide 12 – Example 3: Driver
**Title:** Example 3 – Event 6 vs Event 7

**6:** unsigned `Temp\helpdesk.sys`  
**7:** `helpdesk.exe` loaded `helpdesk.dll` (user-mode — different row)

**Interpretation:**  
Driver lead. Not a DLL load. Not BYOVD class.

**Speaker Notes:**  
Park 2.6.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- Event 6 = DLL
- Event 11 = load
- Query with no filter
- Empty Signed = unsigned
- Asking how to enable Event 7
- Sideload / BYOVD lecture

**Speaker Notes:**  
Then the exercise.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide.
3. Two queries: DLL load from Temp/AppData; driver load outside `C:\Windows\`.
4. One analysis card (Example 2 or 3).

**Speaker Notes:**  
Park file, process, install. Review with the Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. User-mode vs driver? Which Sysmon IDs?
2. Why path + hash + signed together?
3. `InitiatingProcess*` on an image load? Event 6 parent?
4. Only Event 11, no Event 7 — was it loaded?
5. Empty `Signed` — what do you write?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Host load row: module into a process, or driver into the kernel.
- Path + hash + signed (if logged) + loader (user-mode).
- Sysmon 6 / 7 ↔ `DeviceImageLoadEvents`.
- 7 = user-mode. 6 = driver. 11 = file create.
- Unit **1.1** ends here. Next unit: Zeek (**1.2**).

**Speaker Notes:**  
Do not open a 1.2.1 lab unless that is the next scheduled hour.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Image / Driver Load — Quick Reference

| Need | Look at |
|------|---------|
| DLL / user-mode | Sysmon 7 / `DeviceImageLoadEvents` |
| Driver | Sysmon 6 |
| Object | `ImageLoaded` or `FolderPath` + `FileName` |
| Loader (7) | `Image` / `InitiatingProcess*` |
| Trust | `Signed` / `Signature` when present |

**Coming next:** Module 1.2.1 – Zeek concepts

**Footer:** SOC / Hunter / CTI Training Program
