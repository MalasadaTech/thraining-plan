# Instructor Guide – Module 2.6.2 – Privilege Escalation Techniques

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.6.2 B / C / C · 2.6.2.1 3c / 4c / 4c  
- SOC: 2.6.2 A / B / B · 2.6.2.1 1a / 2b / 3c  
- CTI: 2.6.2 A / B / B · 2.6.2.1 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on identification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach hunters to name common Windows privilege-escalation methods, name the indicators that prove an elevation, and recognize those methods in logs or telemetry. Recognition is the task. A full hunt for a named technique is 2.6.3.

**Key Teaching Points:**
- Privilege escalation = privilege **changes** (not already SYSTEM).
- Outline a–b: common Windows methods + indicators (2.6.2).
- Recognize with method + indicator (2.6.2.1).
- Expected consented elevations are still that method.
- Stay out of persistence how-to (2.6.1), hunt-for-specific (2.6.3), ATT&CK remapping (2.5.1), local hunt control (2.7), execute (2.2.1), exploit writing.

**Common Student Challenges:**
- Calling any SYSTEM activity privilege escalation.
- Calling a SYSTEM scheduled task “privesc” (usually **2.6.1**).
- Slogan: “they use privesc” with no method.
- Dumping the entire ATT&CK Privilege Escalation tactic.
- Writing a hunt plan instead of a recognition card.
- Inventing an elevation when integrity/token logs are missing (visibility gap).

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for a four-row method table
- Optional: one sanitized token / fodhelper / consent screenshot
- Same Building C 4698 leftover from 2.6.1 if available
- Answer key (this guide)

---

## Learning Objectives

1. Explain common Windows privilege escalation methods and the indicators that go with them.
2. Recognize those methods in logs or telemetry (not persistence, not a process that was already privileged).
3. Say whether a row looks expected, a lead, or untestable because you cannot see the elevation.

**Mapped Items:**
- K: 2.6.2 – Privilege escalation techniques
- T: 2.6.2.1 – Recognize privilege escalation techniques in logs or telemetry

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Persistence (2.6.1) vs elevation |
| What privesc is                | 8 min    | Privilege changes vs already SYSTEM |
| Methods + indicators           | 14 min   | a–b on the board; one indicator each |
| Walkthrough Examples           | 14 min   | Students score each card first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~68 min** | Stretch Example 3 if they still call 4698 privesc |

---

## Detailed Teaching Notes

### 1. What privilege escalation is

**Talking Points:**
- Hold up last week’s SYSTEM task leftover. Ask: did privilege *change*, or did something *start* as SYSTEM?
- Hunter 3 is already at principles (B / 3c). Push method + indicator a teammate can check.
- Hunter 2.6.2.1 tops at **4c**, not 4d. Do not invent a 4d on recognition.
- SOC/CTI: K is **A / B / B**; task is **1a / 2b / 3c**. Recognize a real method vs a slogan.

**What to emphasize:**
- Expected consented elevations are still UAC elevation.
- No integrity/token/service-path log = visibility gap. Do not guess.

**Questions to ask the class:**
- “Did privilege change, or was this already privileged?”
- “Which method, and which indicator proves it?”

### 2. Methods and indicators

**Talking Points:**
- Outline a is a *short* Windows list: token, UAC bypass, service/image abuse, other. Stop there.
- Outline b is the indicator column — teach it on the same table, not as a second lecture.
- Token: who opened whose token + resulting child identity.
- UAC: auto-elevate parent + payload + consent present or missing.
- Service: image path + who changed it + run-as.
- Other: they must say which other. No exploit-dev.

**What to emphasize:**
- Same goal, different telemetry. Do not treat all four as “UAC.”
- A row can be **both** service abuse (2.6.2) and persistence (2.6.1 other). Name both. Do not collapse.
- ATT&CK IDs are labels if already mapped. This lesson is not 2.5.1.

**Question to ask:**  
“If we only have process-create with no integrity field, which methods can we actually recognize?”

### 3. Examples

Work through all three interactively. Students mark method / expected / lead / not privesc before you read the interpretation.

**Extra point for Example 1:**  
Expected ≠ “not privilege escalation.” Recognition still names the method.

**Extra point for Example 2:**  
Token row is 2.6.2. 4698 leftover is 2.6.1. SYSTEM on the task is not this class.

**Extra point for Example 3:**  
Force: 4698 ≠ TA0004. `fodhelper` + no consent = UAC bypass. They must say the method, not only “privesc.”

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 14–16 minutes.
- Allow use of the Student Guide.
- Grade recognition, not a hunt card or a Navigator layer.
- Review as a group. Do not collect a grade.
- Park persistence labs, 2.6.3 execute, exploit writing, and SIEM run.

**What good answers look like:**

**Summaries:**
- Example 1: Consented UAC elevation; expected signed installer; still that method.
- Example 2: Token-theft lead (user → SYSTEM); 4698 is persistence, not this class.
- Example 3: A mislabels 2.6.1 as privesc; B is UAC bypass with indicators.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| `helpdesk.exe` (user) → `cmd.exe` SYSTEM after token open | **Token** | Privilege changed via token |
| `fodhelper.exe` → Public payload, High IL, no consent | **UAC bypass** | Auto-elevate parent, no Yes |
| Service path → `C:\Users\Public\svc.exe`, SYSTEM | **Service abuse** | Privileged image hijack |
| Signed `VendorSetup.exe`, clicked Yes, High IL | **UAC** (expected) | Elevation happened; consented |
| 4698 SYSTEM + Public bat, no token/UAC story | **Not privilege escalation** | **2.6.1** persistence |
| `whoami` same user, Medium IL | **Not privilege escalation** | No elevation |

Accept “UAC” or “expected UAC elevation” for the installer. Fail if they mark it “not privilege escalation” *and* deny it is an elevation method — the student guide calls it expected UAC. If they say “UAC, expected,” that is the key.

**Pseudo-queries (equivalent is fine):**

```
process
| where (integrity_level in ("System", "High") or user == "SYSTEM")
| where parent_integrity_level == "Medium" or parent_user !in ("SYSTEM", "LOCAL SERVICE", "NETWORK SERVICE")
| where parent_path !has @"C:\Program Files\"
```

```
process
| where parent_name in ("fodhelper.exe", "eventvwr.exe", "computerdefaults.exe")
| where path !has @"C:\Windows\System32\" and path !has @"C:\Program Files\"
```

Fail a query that hunts “all of TA0004,” alerts on every SYSTEM process, or looks for Run keys.

**Recognition card (example answer — Example 2):**  
Method: token impersonation / theft. Indicator: `helpdesk.exe` Medium/`jlee` opened a SYSTEM token; child `cmd.exe` SYSTEM; no consent; no ticket. Lead: not an incident by itself. Not persistence. Not a hunt plan.

Fail the card if they only write “privesc,” call the 4698 this class, or write a scoped hunt hypothesis as the deliverable.

---

## Knowledge Check – Answer Key

1. **Privesc vs already privileged?**  
   **Answer:** Privilege escalation is a method that **changes** privilege (typically to High or SYSTEM). A process that started already privileged is not this class unless you can show the elevation.  
   **Explanation:** Did privilege change?

2. **One Windows method + indicator?**  
   **Answer (equivalent):** Token theft — user parent + SYSTEM token / SYSTEM child. Or UAC bypass — auto-elevate parent + unexpected payload + no consent. Or service abuse — SYSTEM image path on a user-writable file.  
   **Explanation:** Method and indicator both required.

3. **UAC bypass vs consented elevation?**  
   **Answer:** Both can reach High IL. Bypass: auto-elevate Windows binary + payload, **no** real consent event. Consented: user clicked Yes (event present), usually a signed installer.  
   **Explanation:** High IL alone does not tell you which.

4. **Why is a SYSTEM scheduled task not automatically privesc?**  
   **Answer:** The task *starts* as SYSTEM. That is a persistence object (**2.6.1**) unless you also see how a non-privileged actor obtained SYSTEM.  
   **Explanation:** SYSTEM ≠ elevation.

5. **One non-privesc; no telemetry?**  
   **Answer (equivalent):** Not this lesson = one-off same-user process, or persistence that starts privileged (**2.6.1**). No integrity/token/service-path logs → name a **visibility gap**. Do not invent a method.  
   **Explanation:** Recognition needs an indicator.

---

## Additional Instructor Resources

- Same Building C 4698 leftover as 2.6.1
- Escalation: persistence class → 2.6.1; hunt-for-specific → 2.6.3; map/coverage → 2.5.1; card format → 2.2.2
- Next recommended module: Hunt for a specific persistence or privilege-escalation technique (2.6.3)
