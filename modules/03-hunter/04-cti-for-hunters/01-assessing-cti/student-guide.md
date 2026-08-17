# Module 3.4.1 – Assessing CTI for Hunting Value

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.1 B / C / C ; 3.4.1.1 3c / 4c / 4d  
- SOC: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
- CTI: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Sort a CTI report as **hunt-worthy**, **awareness-only**, or a **hand-off**.
2. Triage a report: hunt / don’t hunt / hand off, and say why.

**Mapped Proficiency Items:**
- K: 3.4.1 – Assessing CTI for hunting value
- T: 3.4.1.1 – Triage a CTI report: hunt / don’t hunt / hand off, and say why

---

## 1. Key Concepts

Hunters do **not** hunt every report. They label it first. Extracting leads is **3.4.2**. STIX objects are **3.4.3**. ATT&CK coverage is **3.5**. This hour is the **gate**.

| Disposition | Meaning |
|-------------|---------|
| **Hunt-worthy** | You can name a question, telemetry that could answer it, and a bound scope |
| **Awareness-only** | Useful context. No hunt this week |
| **Hand-off** | Not a hunt. Detections or IR already own it |

**Actionable for a hunt** means you can name three things: **question**, **telemetry**, **scope**. “Interesting” is not a hunt.

**What good looks like:**

- **Hunt-worthy:** bulletin names `GET /update.exe` to `203.0.113.88:8080` and HKCU Run **`Updater`**. User workstations. Registry + HTTP exist. No analytic on that path.
- **Awareness:** “APT exists.” No object, no telemetry hook, no scope.
- **Hand-off:** IR is already open on the same installer hash.

Rapid triage is a **label and one sentence why**. If you start copying every MITRE ID, you have left this lesson.

---

## 2. Knowledge Check

1. An interesting actor profile is a hunt. True or false?
2. What three things must you name before a report is actionable for a hunt?
3. Label this classroom card and say why: installer hash + `:8080` `/update.exe`, no analytic, no open IR, registry + HTTP exist.

---

## 3. Summary

Hunt / don’t hunt / hand off, plus why. Question, telemetry, scope. Not a TTP table.

**Next:** **3.4.2** Extracting hunt leads.

---

## 4. Related modules

- 3.3.1 – Hunt tools (previous)
- 3.4.2 – Extract leads
- 3.4.3 – STIX input
- 3.5.1 – ATT&CK map
