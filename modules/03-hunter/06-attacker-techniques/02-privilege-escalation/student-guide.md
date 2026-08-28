# Module 3.6.2 – Privilege Escalation Techniques

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.2 B / C / C ; 3.6.2.1 3c / 4c / 4c  
- SOC: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
- CTI: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name common Windows privilege-escalation methods and the indicators that prove elevation.
2. Recognize those methods in logs or telemetry — not persistence, and not a process that was already privileged.

**Mapped Proficiency Items:**
- K: 3.6.2 – Privilege escalation techniques
- T: 3.6.2.1 – Recognize privilege escalation techniques in logs or telemetry

---

## 1. Key Concepts

Threat hunters read host telemetry to see whether an actor **gained a higher privilege** than they started with. That change is **privilege escalation** (elevation): typically a standard user to administrator or **SYSTEM**. Persistence is a method that will **run again**. That was **3.6.1**. If you call a Run key elevation, you hunt the wrong class. The job in this lesson is to name the method and the indicator that proves the privilege changed. You do not hunt a named technique (**3.6.3**).

The A12 Run key **`Updater`** is **not** privilege escalation. It starts as the logged-on user. A scheduled task that runs as SYSTEM is persistence unless you also see **how** a non-privileged actor got SYSTEM.

| Method | Indicator that proves elevation |
|--------|---------------------------------|
| **Token theft / impersonation** | A user-context parent starts a child as SYSTEM (or High integrity). The parent was not already that privileged, and it is not an auto-elevate Windows binary. |
| **UAC bypass** | An **auto-elevate** Windows binary — a built-in program Windows will raise without a real consent prompt — launches an unexpected payload, and there is no real consent. |
| **Privileged service / image abuse** | The service image path points at a user-writable file, or a user who was not already privileged creates a service that then runs as SYSTEM. |
| **Other** | A named tool, named pipe, or other method you can point at, plus a SYSTEM spawn. Say which. |

A process that was **already** SYSTEM is not elevation. A user who clicked **Yes** on a signed installer is usual User Account Control (UAC) consent, not a bypass.

If you cannot see integrity level, tokens, or service-image changes, name a **visibility gap**. Do not invent a method.

**What good looks like** (classroom examples — not A12 facts):

- Given: user `helpdesk.exe` → `cmd.exe` as SYSTEM, no consent event. **Token theft.** Proof: parent identity versus child identity, and no consent.
- Given: `fodhelper.exe` → unknown executable, no consent. **UAC bypass.**
- Given: HKCU Run **`Updater`**. **Not** this class. That is persistence (**3.6.1**).

Do not hunt “privilege escalation” as a tactic. That is **3.6.3**.

---

## 2. Knowledge Check

1. HKCU Run **`Updater`** is privilege escalation. True or false?
2. Name two privilege-escalation methods.
3. A user `helpdesk.exe` launches `cmd.exe` as SYSTEM with no consent event. What method, and what indicator proves it?

---

## 3. Summary

Privilege escalation is a privilege change, not an autorun. Name the method and the indicator, or name a visibility gap.

**Next:** **3.6.3** Hunt one named technique.

---

## 4. Related modules

- 3.6.1 – Persistence techniques
- 3.6.3 – Hunt one named technique
- 3.5.1 – ATT&CK map
