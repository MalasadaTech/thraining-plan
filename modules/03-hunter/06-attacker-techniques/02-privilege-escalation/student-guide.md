# Module 2.6.2 – Privilege Escalation Techniques

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.6.2 B / C / C · 2.6.2.1 3c / 4c / 4c  
- SOC: 2.6.2 A / B / B · 2.6.2.1 1a / 2b / 3c  
- CTI: 2.6.2 A / B / B · 2.6.2.1 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain common Windows privilege escalation methods and the indicators that go with them.
2. Recognize those methods in logs or telemetry (not persistence, not a process that was already privileged).
3. Say whether a row looks expected, a lead, or untestable because you cannot see the elevation.

**Mapped Proficiency Items:**
- K: 2.6.2 – Privilege escalation techniques
- T: 2.6.2.1 – Recognize privilege escalation techniques in logs or telemetry

---

## 1. Key Concepts

### 1.1 What privilege escalation is

**Privilege escalation** is a method that takes a process or user from a **lower** privilege to a **higher** one — typically Medium integrity / standard user → High (admin) or SYSTEM.

**2.6.1** taught persistence: something that will **run again**. This lesson is a different job: **recognize the elevation**. A SYSTEM scheduled task is persistence unless you also see *how* a non-privileged actor got SYSTEM. You are not writing a full hunt for a named technique (**2.6.3**).

| Privilege escalation | Not privilege escalation |
|----------------------|--------------------------|
| Privilege **changes** (token, UAC, hijacked SYSTEM service) | A process that was **already** SYSTEM / already admin |
| User parent → SYSTEM or High-IL child you cannot account for | Autorun that *starts* as SYSTEM (**2.6.1**) |
| Expected consented elevation *and* a silent UAC bypass | “They use privesc” with no method |

**Most critical distinction for daily work:**  
Name the **method** (token / UAC bypass / privileged-service abuse / other) and the **indicator that proves the elevation**. A slogan is not recognition.

If you have no telemetry for integrity, tokens, or service image changes, name a **visibility gap**. Do not invent an elevation so the card looks complete.

### 1.2 Common Windows methods and their indicators

Four method families. Same goal: more privilege. Different indicators.

| Method | What it is | Indicator that proves elevation | Common ATT&CK label (if you already mapped it) |
|--------|------------|---------------------------------|------------------------------------------------|
| **Token impersonation / theft** | Duplicate or steal a privileged token and run as that identity | User-context process opens a SYSTEM token, or child runs as SYSTEM with a user parent | T1134 |
| **UAC bypass** | Reach High integrity **without** a real consent prompt | Auto-elevate Windows binary (`fodhelper`, `eventvwr`, `computerdefaults`, …) launches an unexpected payload | T1548.002 |
| **Privileged service / image abuse** | Change or hijack something that already runs as SYSTEM | Service image path → user-writable file; new SYSTEM service created from a user session | T1543.003 / T1574 |
| **Other common methods** | SeImpersonate / potato-style, weak named pipe, driver/service exploit | Named tool or pipe + SYSTEM spawn you can point at — say which other | T1068 / T1134.001 |

You do not owe every Privilege Escalation technique in ATT&CK. These four families are the floor.

| Method | Expected (usually) | Lead (usually) |
|--------|--------------------|----------------|
| Token | Documented admin tool that impersonates by design | `helpdesk.exe` (user) → `cmd.exe` as SYSTEM |
| UAC bypass | Signed installer, user clicked **Yes**, High IL | `fodhelper.exe` → unknown exe, no consent event |
| Service abuse | IT changes a service path in a ticket | SYSTEM service binary under `C:\Users\Public` |
| Other | Known privileged installer | Potato-family parent + SYSTEM child, no change ticket |

**Indicators (outline b)** — ask these on every row:

| Indicator | Use it when | Not enough alone |
|-----------|-------------|------------------|
| Integrity / run-as **changes** (Medium → High or SYSTEM) | You can see both sides | A SYSTEM service doing its normal job |
| Parent vs child identity | User parent, privileged child | Child of an already-SYSTEM parent |
| Consent / 4673 / UAC event **missing** when High IL appears | UAC-bypass family | Admin logon that *did* consent |
| Service image path or new SYSTEM service from a user session | Service-abuse family | 4698 SYSTEM task with no elevation story (**2.6.1**) |
| Special privileges (4672) on a **non-admin** account | Privileged logon you cannot account for | Expected Domain Admin logon |

**Token:** look at who opened whose token, and the **resulting** identity of the child. “Process ran as SYSTEM” is not theft if the parent was already SYSTEM.

**UAC bypass:** look at the **auto-elevate parent** plus the payload, and whether a consent UI / 4673 exists. High IL after a clicked **Yes** on a signed installer is still UAC elevation — usually **expected**.

**Service abuse:** look at **image path**, **who changed it**, and **account the service runs as**. A user-writable SYSTEM binary is the indicator. Installing a service can also be persistence (**2.6.1** other). Call **both** classes if both are true; do not collapse them.

**Other:** say which other. Do not dump the rest of TA0004.

How you *hunt* a named technique end-to-end is **2.6.3**. Local hunt control is **2.7**. Stay here: method + indicator in the log.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Expected consented elevation)

**Telemetry (process + UAC):**

| Field | Value |
|-------|--------|
| Parent | `C:\Program Files\Vendor\VendorSetup.exe` (signed) |
| Child | same installer, **High** integrity |
| User | `BUILDINGC\jlee` (standard user) |
| UAC | Consent **Yes**, event present |
| Host | Laptop-14 |
| Note | Same installer in the software catalog |

**Recognition card**

| Field | What they wrote |
|-------|-----------------|
| Method | **UAC elevation** (consented) — still an elevation method |
| Indicator | Medium → High IL + consent event + signed catalogued installer |
| Expected vs lead | **Expected**. Still privilege escalation *as a method* |
| Not done | Did not call it an incident. Did not open a privesc hunt (**2.6.3**). Did not call it persistence |

**Interpretation:**  
You recognized the method. Expected elevations still count. Recognition ≠ escalate.

### Example 2: User Parent → SYSTEM Child (Lead)

A hunt channel paste:

> Building C-12, 14:03. `C:\Users\jlee\helpdesk.exe` (Medium IL, user `jlee`) opened a handle to `winlogon.exe` / SYSTEM token. Child `cmd.exe` **SYSTEM**. No consent event. No change ticket.

Compare a 4698 on the same host from **2.6.1**:

> 02:17. Event 4698. Task `\Microsoft\Windows\UpdateCheck`. Run as **SYSTEM**. Command `C:\Users\Public\update.bat`. No token event. No integrity change — the task *starts* as SYSTEM.

**Recognition card (the 14:03 row)**

| Field | What they wrote |
|-------|-----------------|
| Method | **Token impersonation / theft** |
| Indicator | User parent + SYSTEM token open + SYSTEM child; no consent |
| Expected vs lead | **Lead** — not an automatic incident |
| Not the 4698 | That row is **scheduled-task persistence** (**2.6.1**), not this elevation |

**Interpretation:**  
14:03 is privilege escalation because privilege **changed**. The 4698 is a persistence object. SYSTEM on a task is not automatically **2.6.2**.

### Example 3: Wrong Class + Silent UAC Bypass (Lead)

**Write-up A**

> New SYSTEM scheduled task in Public. Privilege escalation. Hunt TA0004.

**Write-up B**

> 14:11. `fodhelper.exe` launched `C:\Users\Public\sync.exe`. Child **High** IL. **No** UAC consent event. Class: **UAC bypass**. Lead — auto-elevate parent + unexpected payload. Not persistence (nothing will start at next logon unless they also dropped an autorun). Not “they use privesc.”

**Interpretation:**  
A names a **2.6.1** object and calls it privilege escalation. B names a UAC-bypass method and the indicators that prove High IL without consent. Recognition stops at the method and the indicator.

---

## 3. Hands-On Exercise

**Objective:** Practice naming privilege-escalation methods and recognizing their indicators in telemetry.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (method, expected vs lead, or not privesc).
2. For each item below, say **token**, **UAC bypass**, **service abuse**, **other**, or **not privilege escalation**. Give one reason.
   - `helpdesk.exe` (user, Medium) → `cmd.exe` SYSTEM after a token open
   - `fodhelper.exe` → `C:\Users\Public\sync.exe`, High IL, no consent
   - Service image path changed to `C:\Users\Public\svc.exe`, runs as SYSTEM
   - Signed `VendorSetup.exe`, user clicked Yes, High IL
   - Event 4698, SYSTEM, `C:\Users\Public\update.bat`, no token/UAC story
   - Single `whoami` as the same user, Medium IL
3. Write **two SIEM-style pseudo-queries** that would *surface candidates to recognize* (not a full hunt):
   - One for **user-context parent → SYSTEM (or High IL) child**, excluding known installer paths.
   - One for **auto-elevate parents** (`fodhelper`, `eventvwr`, `computerdefaults`) launching a payload **not** under `System32` / `Program Files`.
4. Write **one recognition card** (small table or four sentences): method, indicator(s), expected vs lead. Use Example 2 or the `fodhelper` row. Do not write a hunt plan. Do not explain persistence how-to. Do not execute the search.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- Two recognition-oriented pseudo-queries
- One card that names the method and the indicator, not a slogan

---

## 4. Knowledge Check

1. What makes an action **privilege escalation** rather than a process that was already privileged?
2. Name one **common Windows** privilege-escalation method and the indicator you would use to recognize it.
3. How is a **UAC bypass** different from a consented UAC elevation in telemetry?
4. Why is a new **SYSTEM scheduled task** not automatically privilege escalation?
5. Give one activity that is **not** privilege escalation in this lesson, and what you do if you cannot see integrity or tokens.

---

## 5. Summary

- Privilege escalation = privilege **changes** (usually to High or SYSTEM).
- Four method families here: token, UAC bypass, privileged-service abuse, other.
- Recognize with a named method and an indicator. Expected elevations still count as that method.
- Already-SYSTEM parents and autoruns that *start* as SYSTEM are not this class (**2.6.1** if they persist).
- No telemetry for the elevation → visibility gap, not a guessed method.
- Next: hunt for a specific persistence or privilege-escalation technique (**2.6.3**).

---

## 6. References & Further Reading

- Related modules:
  - 2.6.1 – Persistence techniques
  - 2.6.3 – Hunt for a specific persistence or privilege-escalation technique (next)
  - 2.5.1 – Using MITRE ATT&CK for hunt planning
  - 2.2.2 – Hunt development (hypothesis / scope)
- Local Windows logging / EDR field guide used in class (optional)
- MITRE ATT&CK — only as labels for methods you actually recognized
