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

1. Name four persistence classes: registry-based, start menu / startup folder, scheduled tasks, and other common methods.
2. Recognize those methods in logs or telemetry — not a one-off run, not a registry-event write-up, not privilege escalation.

**Mapped Proficiency Items:**
- K: 3.6.1 – Persistence techniques
- T: 3.6.1.1 – Recognize persistence techniques in logs or telemetry

---

## 1. Key Concepts

Hunters look at host telemetry to see whether something will **run again** after reboot, logon, or a time trigger. SOC already described the registry **set** on that host (**1.1.5**): which hive and key changed, and who changed it. That write-up is the event. This lesson names the **method**: if Windows will launch that payload later, the set is **persistence**. Hunters do this so they can tell autorun from a one-off run, and so a later hunt can pick one named method instead of “hunt persistence.”

**Persistence** is a method that makes code **run again** after reboot, logon, or a time trigger.

This lesson is **not** how to read a registry event (**1.1.5**). It is **not** privilege escalation (**3.6.2**). It is **not** a hunt for a named technique (**3.6.3**). **3.5.1** mapped a hunt to a Persistence technique. This lesson is recognizing the mechanism.

| Class | What recognition looks like |
|-------|-----------------------------|
| **Registry-based** | A value **set** under Run, RunOnce, or Winlogon (Shell, Userinit). The **data** is the payload path Windows will launch. |
| **Start menu / startup folder** | A file or `.lnk` **created** in the user Startup folder or All Users Startup. That path runs at logon. |
| **Scheduled tasks** | A task **created** or **updated**. Name the trigger, the command, and the account it runs as. |
| **Other common methods** | A new or changed **service**, a **WMI** event subscription, or a **logon script**. Say which. |

A one-off process is not persistence. `wscript` running Temp `invoice.vbs` once is execution. The Run key that PowerShell set afterward is persistence.

A privilege change by itself is **3.6.2**.

A catalogued vendor updater under `Program Files` that writes a Run key is still persistence *as a method*. Expected autorun is still the class.

Name the **class** and the **field that proves it**. If you cannot see that class in the telemetry you have, name a **visibility gap**. Do not invent a method.

**What good looks like:**

- Given: on host **WS-JLEE**, HKCU Run value **`Updater`** = `%TEMP%\update.exe`. **Class:** registry-based persistence. **Proof:** value name + payload path. That is the method that will run again at logon.
- Given: `wscript.exe` runs Temp `invoice.vbs` once. **Not persistence.** One-off execution.
- Not this lesson: search every Run key, or write a hunt named “persistence.” That is **3.6.3**.

---

## 2. Knowledge Check

1. A one-off `wscript invoice.vbs` is persistence. True or false?
2. Name the four persistence classes.
3. Class + proof for HKCU Run **`Updater`** → `%TEMP%\update.exe`.

---

## 3. Summary

Persistence is a method that will run again. Four classes. Name the class and the proof in the log. A one-off run is not persistence. Do not hunt the tactic.

**Next:** **3.6.2** Privilege escalation techniques.

---

## 4. Related modules

- 3.5.1 – ATT&CK map (previous)
- 1.1.5 – Registry activity
- 3.6.2 – Privilege escalation techniques
- 3.6.3 – Hunt one named technique
