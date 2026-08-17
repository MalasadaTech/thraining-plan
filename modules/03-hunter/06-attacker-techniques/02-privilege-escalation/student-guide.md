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
2. Recognize those methods in logs — not persistence, not a process that was already privileged.

**Mapped Proficiency Items:**
- K: 3.6.2 – Privilege escalation techniques
- T: 3.6.2.1 – Recognize privilege escalation techniques in logs or telemetry

---

## 1. Key Concepts

**Privilege escalation** takes a process or user from a **lower** privilege to a **higher** one — typically standard user → admin or SYSTEM. **3.6.1** was something that will **run again**. This hour is **recognize the elevation**. You do not hunt a named technique (**3.6.3**).

The A12 Run key is **not** privilege escalation. It starts as the user. A SYSTEM scheduled task is persistence unless you also see *how* a non-privileged actor got SYSTEM.

| Method | Indicator that proves elevation |
|--------|---------------------------------|
| **Token theft / impersonation** | User-context parent → SYSTEM (or High IL) child |
| **UAC bypass** | Auto-elevate Windows binary launches an unexpected payload; no real consent |
| **Privileged service / image abuse** | Service image path → user-writable file; new SYSTEM service from a user session |
| **Other** | Named tool or pipe + SYSTEM spawn you can point at — say which |

A process that was **already** SYSTEM is not elevation. Consent **Yes** on a signed installer is usually expected UAC.

If you cannot see integrity, tokens, or service-image changes, name a **visibility gap**.

**What good looks like (classroom row — not an A12 fact):**

- User `helpdesk.exe` → `cmd.exe` as SYSTEM, no consent event: **token theft**.
- `fodhelper.exe` → unknown exe, no consent: **UAC bypass**.
- HKCU Run **`Updater`**: **not** this class.

---

## 2. Knowledge Check

1. HKCU Run **`Updater`** is privilege escalation. True or false?
2. Name two privilege-escalation methods.
3. A user parent launches `cmd.exe` as SYSTEM with no consent event. What method, and what indicator proves it?

---

## 3. Summary

Elevation, not autorun. Method + indicator, or a visibility gap.

**Next:** **3.6.3** Hunt one named technique.

---

## 4. Related modules

- 3.6.1 – Persistence (previous)
- 3.6.3 – Hunt one named technique
- 3.5.1 – ATT&CK map
