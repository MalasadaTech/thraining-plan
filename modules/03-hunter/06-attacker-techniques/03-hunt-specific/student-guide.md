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
2. Reject “hunt persistence / hunt privesc” and a hunt that uses the **wrong class**.

**Mapped Proficiency Items:**
- T: 3.6.3 – Hunt for specific persistence or privilege escalation techniques

---

## 1. Key Concepts

**3.6.1** and **3.6.2** taught you to *recognize* the method. This hour you **hunt one named technique**. You do not rewrite the hunt-development card (**3.2.2**). You do not open the local ticket path (**3.7**).

**Named** means a method you can point at: HKCU Run **`Updater`**, user parent → SYSTEM child. “Persistence” and “privilege escalation” are classes, not hunts.

**Hunt line:**  
`named technique | persist or privesc | unique pattern | scope | why not the whole tactic`

**What good looks like:**

- **Hunt:** HKCU Run **`Updater`** → `%TEMP%\update.exe` on user workstations, last 14 days, registry + file. Unique pattern is the **value name**, not “any Run key.”
- **Fail:** “Hunt persistence.” No unique pattern.
- **Fail:** Call a SYSTEM scheduled task privilege escalation when no elevation was shown. Wrong class.

The product is a **bounded hunt**, not a rewrite of the SOC ticket, and not a ticket name you invent.

---

## 2. Knowledge Check

1. “Hunt persistence” is a valid 3.6.3 hunt. True or false?
2. What does **named** mean in this hour?
3. Write one hunt line for A12 Run **`Updater`** (technique, class, unique pattern, scope).

---

## 3. Summary

One named method. Unique pattern. Wrong class fails.

**Next:** **3.7.1** Hunt control and lead management.

---

## 4. Related modules

- 3.6.2 – Privilege escalation (previous)
- 3.6.1 – Persistence recognition
- 3.2.2 – Hunt card
- 3.7.1 – Local control
