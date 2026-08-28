# Module 3.6.3 – Hunt for a Specific Persistence or Privilege-Escalation Technique

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.3 3c / 4c / 4d  
- SOC: 3.6.3 1a / 1a / 2b  
- CTI: 3.6.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Turn **one named** persistence or privilege-escalation technique into a **scoped hunt**.
2. Reject “hunt persistence / hunt privilege escalation” and a hunt that uses the **wrong class**.

**Mapped Proficiency Items:**
- T: 3.6.3 – Hunt for specific persistence or privilege escalation techniques

---

## 1. Key Concepts

Hunters search for activity the alerts missed. After you can recognize a persistence or privilege-escalation method, you still have to turn it into a hunt someone can run. That is the job in this lesson: name **one method**, a **unique pattern**, and a **bound**, so you do not sweep a whole tactic and call it a hunt.

**3.6.1** and **3.6.2** taught you to *recognize* the method. This lesson **hunts one named technique**. You do not rewrite the hunt-development card (**3.2.2**). You do not open the local ticket path (**3.7**).

**Named** means a method you can point at: a current-user (HKCU) Run value named **`Updater`**, or a user parent launching a SYSTEM child. “Persistence” and “privilege escalation” are **classes**, not hunts.

A **unique pattern** is the specific thing you search — a value name, a parent/child pair, a specific binary — not every method in the class. **Scope** is where you look, how long, and which telemetry. Together those pieces are the **hunt line** — the bounded hunt in one pass:

| Piece | What you name |
|-------|----------------|
| **Named technique** | The method you can point at |
| **Class** | Persistence or privilege escalation |
| **Unique pattern** | What you search (not the whole tactic) |
| **Scope** | Where / how long / which telemetry |
| **Why not the whole tactic** | Why this pattern, not “all persistence” or “all privilege escalation” |

**What good looks like:**

- **Hunt:** HKCU Run **`Updater`** → `%TEMP%\update.exe` on user workstations, last 14 days, registry + file. Unique pattern is the **value name `Updater`**, not “any Run key.” Class is persistence. Why not the whole tactic: you are looking for this value, not every autorun.
- **Fail:** “Hunt persistence.” No unique pattern and no bound.
- **Fail:** Call a SYSTEM scheduled task privilege escalation when no elevation was shown. Wrong class. A task that *runs as* SYSTEM is persistence unless the log also shows how a non-privileged actor *got* SYSTEM.

The product is a **bounded hunt**, not a rewrite of the SOC ticket, and not a ticket name you invent.

Hunt types (**3.2.1**), the full hunt card (**3.2.2**), and ATT&CK remapping (**3.5**) are other lessons. Local control of the hunt is **3.7**.

---

## 2. Knowledge Check

1. “Hunt persistence” is a valid 3.6.3 hunt. True or false?
2. What does **named** mean in this lesson?
3. Write one hunt line for HKCU Run **`Updater`** → `%TEMP%\update.exe` (named technique, class, unique pattern, scope).

---

## 3. Summary

One named method. A unique pattern. A bound. Wrong class fails. Persistence and privilege escalation are classes, not hunts.

**Next:** **3.7.1** Hunt control and lead management.

---

## 4. Related modules

- 3.6.2 – Privilege escalation (previous)
- 3.6.1 – Persistence recognition
- 3.2.2 – Hunt card
- 3.7.1 – Local control
