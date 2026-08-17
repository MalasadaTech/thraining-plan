# Module 3.2.2 – Hunt Development Concepts

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.2 B / C / C ; 3.2.2.1–3.2.2.3 3c / 4c / 4d  
- SOC: 3.2.2 A / B / B ; 3.2.2.1–3.2.2.3 1a / 1a / 2b  
- CTI: 3.2.2 A / B / B ; 3.2.2.1 1a / 2b / 3c ; 3.2.2.2 1a / 2b / 3c ; 3.2.2.3 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Write a **hypothesis**, **scope**, and **priority** for a hunt.
2. Name a **unique pattern** worth searching internally.

**Mapped Proficiency Items:**
- K: 3.2.2 – Hunt development concepts
- T: 3.2.2.1 – Develop and document a hunt hypothesis
- T: 3.2.2.2 – Scope and prioritize a hunt
- T: 3.2.2.3 – Identify unique patterns or behaviors suitable for hunting

---

## 1. Key Concepts

Hunters write a **card** so the search is bounded. Type was **3.2.1**. Local ticket format is **3.7.2**. This hour is **hypothesis / scope / priority / pattern**. No invented board.

| Piece | Meaning | A12 classroom |
|-------|---------|----------------|
| **Hypothesis** | If X is true, we should see Y | If A12 persistors exist elsewhere, we see Run **`Updater`** → `%TEMP%\update.exe` |
| **Scope** | Where / how long / which telemetry | User workstations, last 14 days, registry + file (not every table) |
| **Priority** | Why this hunt now | Open incident + FN download; not a blog read |
| **Unique pattern** | Something specific enough to search | Run value name **`Updater`**, not “any Run key” |

**What good looks like:** four lines. Not a SIEM query this hour. Not “hunt persistence.”

---

## 2. Knowledge Check

1. A hunt card is “search everything for malware.” True or false?
2. What four pieces does the card have?
3. Write a one-line **A12** hypothesis and one unique pattern (not “any Run key”).

---

## 3. Summary

Hypothesis, scope, priority, unique pattern. Bounded. Not a ticket name you invent.

**Next:** **3.3.1** Hunt tool capabilities.

---

## 4. Related modules

- 3.2.1 – Hunt types (previous)
- 3.3.1 – Hunt tools
- 3.6.3 – Hunt one named technique
- 3.7.2 – Local documentation
