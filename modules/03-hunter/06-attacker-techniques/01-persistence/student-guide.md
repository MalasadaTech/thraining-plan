# Module 3.6.1 – Persistence Techniques

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.1 B / C / C ; 3.6.1.1 3c / 4c / 4c  
- SOC: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
- CTI: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name four persistence classes: registry, startup folder, scheduled tasks, other.
2. Recognize those methods in logs or telemetry — not a one-off run, not privilege escalation.

**Mapped Proficiency Items:**
- K: 3.6.1 – Persistence techniques
- T: 3.6.1.1 – Recognize persistence techniques in logs or telemetry

---

## 1. Key Concepts

**Persistence** is a method that makes code **run again** after reboot, logon, or a time trigger. **3.5.1** mapped a hunt to a Persistence technique. This hour is **recognize the mechanism**. You do not hunt a named technique (**3.6.3**). You do not teach privilege escalation (**3.6.2**).

| Class | What recognition looks like |
|-------|-----------------------------|
| **Registry** | Value **set** under Run / RunOnce / Winlogon; data is the payload |
| **Startup folder** | File or `.lnk` created in user or All Users Startup |
| **Scheduled task** | Task **created** or **updated**; trigger + command + run-as |
| **Other** | New/changed **service**, **WMI** subscription, or **logon script** — say which |

A one-off process is not persistence. A privilege change by itself is **3.6.2**.

Name the **class** and the **field that proves it**. If you cannot see that class, name a **visibility gap**. Do not invent a method.

**What good looks like:**

- **A12:** HKCU Run **`Updater`** → `%TEMP%\update.exe` on **WS-JLEE** is **registry** persistence. Proof: value name + path.
- **Expected:** catalogued vendor updater under `Program Files`. Still persistence *as a method*.
- **Not this hour:** “hunt persistence.” That is **3.6.3**.

---

## 2. Knowledge Check

1. A one-off `wscript invoice.vbs` is persistence. True or false?
2. Name the four persistence classes.
3. Class + proof for HKCU Run **`Updater`** → `%TEMP%\update.exe`.

---

## 3. Summary

Four classes. Recognize the mechanism in the log. Do not hunt the tactic.

**Next:** **3.6.2** Privilege escalation techniques.

---

## 4. Related modules

- 3.5.1 – ATT&CK map (previous)
- 3.6.2 – Privilege escalation
- 3.6.3 – Hunt one named technique
- 1.1.5 – Registry (endpoint)
