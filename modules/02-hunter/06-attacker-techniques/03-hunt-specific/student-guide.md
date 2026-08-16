# Module 2.6.3 – Hunt for a Specific Persistence or Privilege-Escalation Technique

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.6.3 3c / 4c / 4d  
- SOC: 2.6.3 1a / 1a / 2b  
- CTI: 2.6.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Turn a **named** persistence or privilege-escalation technique into a **scoped hunt**.
2. Cite a **unique pattern** (not the whole tactic).
3. **Reject** an unbounded “hunt persistence / hunt privesc” and a hunt that uses the **wrong class**.

**Mapped Proficiency Items:**
- T: 2.6.3 – Hunt for specific persistence or privilege escalation techniques

---

## 1. Key Concepts

**2.6.1** and **2.6.2** already taught you to *recognize* the method in a log. This hour you **hunt one named technique**. You do not re-score the recognition card. You do not execute all four hunt types (**2.2.1**). You do not open the local control path (**2.7**).

**Named** means a method you can point at: HKCU Run `Updater`, `fodhelper` → unexpected payload, user parent → SYSTEM child. “Persistence” and “privilege escalation” are classes, not hunts.

**Hunt line:**  
`named technique | persist or privesc | unique pattern | scope (hosts / time / telemetry) | internal query idea | why not the whole tactic`

**4d:** the unique pattern is what makes this hunt testable. “Any Run key” or “any SYSTEM process” is not 4d.

| This lesson | Other |
|-------------|-------|
| Hunt **one named** method | Recognize it in a row — **2.6.1** / **2.6.2** |
| Scope + unique pattern | Write the full hunt-development card — **2.2.2** |
| Not all four hunt types | **2.2.1** |
| Not remap the tactic | **2.5** |
| Not the local ticket | **2.7** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| HKCU Run `Updater` → `%TEMP%\update.exe` on Windows endpoints | Hunt TA0003 / “all persistence” |
| Token theft: user parent → SYSTEM child | Hunt privesc because a SYSTEM *task* exists (**2.6.1**) |
| Time + host class + one field pattern | “Hunt everything on WS-JLEE” |

**Classroom facts (already recognized — do not re-litigate):**

| Fact | Class | Named technique |
|------|-------|-----------------|
| HKCU Run `Updater` → `%TEMP%\update.exe` on **WS-JLEE** | Persist | Registry Run (**T1547.001**) |
| 4698 SYSTEM task `NightOwl` with no elevation story | Persist | Scheduled task (**T1053.005**) — **not** privesc |
| `helpdesk.exe` (user) → `cmd.exe` SYSTEM, no consent | Privesc | Token theft (**T1134**) |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Named Run-Key Hunt (Expected)

**Hunt line:** `HKCU Run Updater → %TEMP%\update.exe | persist | value name Updater + path in %TEMP% | Harbor Windows endpoints / last 14 days / Sysmon 13 + MDE DeviceRegistryEvents | query Run key value Updater OR image %TEMP%\update.exe | not every Run key`

**Why it is a hunt:** one method, one pattern, a place to look, a stop.

### Example 2: Whole-Tactic Hunt (Lead)

**Draft:** “Hunt Persistence. Any Run key, any 4698, any startup folder.”

**Fail.** That is a tactic sweep. No unique pattern.  
**Lead:** Name **one** method. Then scope it.

### Example 3: Wrong Class (Lead)

**Draft:** “Hunt privilege escalation for the Night Owl SYSTEM scheduled task.”

**Fail.** That row is persistence (**2.6.1**). No elevation was shown.  
**Lead:** Hunt the **task**. Or hunt token theft if *that* row is the seed. Do not swap the class.

---

## 3. Hands-On Exercise

**Objective:** Write hunt lines for a named technique. Reject unbounded and wrong-class hunts.

**Use only the classroom facts above.**

**Instructions:**

1. One sentence each for Examples 1–3: hunt vs fail.
2. **Hunt** (task): write a **hunt line** for each.

   - A. HKCU Run `Updater` → `%TEMP%\update.exe`.  
   - B. “Hunt all persistence on Harbor.”  
   - C. `helpdesk.exe` (user) → `cmd.exe` SYSTEM.  
   - D. 4698 SYSTEM task `NightOwl` as a *privesc* hunt.  
   - E. “Write the 2.7 ticket and start the hunt today.”

3. Pick **one** of A or C as the product hunt. Do not ship B, D, or E.
4. Do not re-teach recognition. Do not remap ATT&CK (**2.5**). Do not invent a local approval path (**2.7**).
5. Unbounded tactic = fail. Wrong class = fail.

**Expected Outcome:**
- Three example summaries
- Five hunt lines (B, D, E fail or refuse)
- One product hunt (A or C)
- No local ticket, no tactic sweep

---

## 4. Knowledge Check

1. What must be **named** before this hour is a hunt?
2. What belongs on a **hunt line** besides the technique name?
3. Why is “hunt persistence” not a **2.6.3** product?
4. Why is the SYSTEM scheduled task **not** a privilege-escalation hunt?
5. Where do you learn the **local** process to open the hunt?

---

## 5. Summary

- One named method. Unique pattern. Scoped query idea. Wrong class stays out.
- Next: **2.7.1** Hunt control and lead management (local — they vary).

---

## 6. References & Further Reading

- Related modules:
  - 2.6.1 – Persistence recognition
  - 2.6.2 – Privilege-escalation recognition
  - 2.2.2 – Hunt development
  - 2.7.1 – Local hunt control (next)
- Classroom facts in this guide (lesson-only)
