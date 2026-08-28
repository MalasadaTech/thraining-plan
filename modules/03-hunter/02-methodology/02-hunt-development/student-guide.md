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

Hunters bound a search **before** they query. An unbounded look — “search everything for malware” — is not a hunt. That is the job in this lesson: write a short **hunt card** so someone else can tell what you are looking for, where, why now, and which pattern is specific enough to search internally. The card is the four-line write-up: **hypothesis**, **scope**, **priority**, and **unique pattern**.

**3.2.1** named the hunt types. This lesson is the **write-up**. It is **not** a SIEM session (**3.3.1**). It is **not** your site’s hunt ticket or form (**3.7**). It is **not** “hunt persistence” (**3.6.3**).

| Piece | Meaning | A12 example |
|-------|---------|-------------|
| **Hypothesis** | If X is true, we should see Y | If A12 persistors exist elsewhere, we see HKCU Run **`Updater`** → `%TEMP%\update.exe` |
| **Scope** | Where / how long / which telemetry | User workstations, last 14 days, registry and file events (not every log source) |
| **Priority** | Why this hunt now | Open A12 incident plus the missed `GET /update.exe` download (a false negative); not a blog read |
| **Unique pattern** | Something specific enough to search internally | Run value name **`Updater`**, not “any Run key” |

A **hypothesis** is a testable if/then, not a topic. “Hunt persistence” names a class of techniques. “If A12 persistors exist elsewhere, we see HKCU Run `Updater` pointing at `%TEMP%\update.exe`” is a hypothesis you can document and check.

**Scope** names hosts, a time window, and which telemetry you will use. It does not say the whole estate, all time, and every log source.

**Priority** is why this hunt now. An open incident and a known miss beat a vendor write-up you just read.

A **unique pattern** is a behavior or artifact you can actually search for inside the network. The Run value name `Updater` is unique enough. “Any Run key” is not.

**What good looks like:** four lines on the card. Not a SIEM query this lesson. Not “hunt persistence.”

- **Hypothesis:** If A12 persistors exist elsewhere, we see HKCU Run **`Updater`** → `%TEMP%\update.exe`.
- **Scope:** User workstations, last 14 days, registry and file events.
- **Priority:** Open A12 incident plus the missed download.
- **Unique pattern:** Value name **`Updater`**, not any Run key.

Do not invent a ticket name or a tracking board. That is local process (**3.7**).

---

## 2. Knowledge Check

1. A hunt card is “search everything for malware.” True or false?
2. What four pieces does the hunt card have?
3. Write a one-line **A12** hypothesis and one unique pattern (not “any Run key”).

---

## 3. Summary

Hypothesis, scope, priority, unique pattern. Bound the search. The classroom card is training, not a ticket name you invent.

**Next:** **3.3.1** Hunt tool capabilities.

---

## 4. Related modules

- 3.2.1 – Hunt types (previous)
- 3.3.1 – Hunt tools
- 3.6.3 – Hunt one named technique
- 3.7.2 – Local documentation
