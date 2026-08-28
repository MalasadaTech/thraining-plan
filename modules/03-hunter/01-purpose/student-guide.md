# Module 3.1 – Purpose of Threat Hunting

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.1.1 B / C / C ; 3.1.1.1 3c / 4c / 4c ; 3.1.1.2 3c / 4c / 4d  
- SOC: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
- CTI: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain why threat hunting exists in the security program: find **missed** activity, and name **detection and visibility gaps**.
2. Name examples of activity that existing controls can miss.

**Mapped Proficiency Items:**
- K: 3.1.1 – Purpose of Threat Hunting
- T: 3.1.1.1 – Explain the purpose of threat hunting in the context of the security program
- T: 3.1.1.2 – Identify examples of activity that existing controls might miss

---

## 1. Key Concepts

SOC analysts work the **alert queue** — the list of detections that already fired. CTI answers requests for more context on those cases. Some malicious or suspicious activity never appears in that list. Hunters look for that missed activity, and they name the holes that let it hide: a detection that never fired, or telemetry that was never collected. That is the job in this lesson. Hunting exists because the queue and the intel note still leave coverage unexamined.

**0.3** named the hunter in one sentence: look for more activity the alerts missed. This lesson is *why* that job exists in the program — next to SOC tickets and detections, not instead of them.

| Job | Meaning |
|-----|---------|
| **Missed activity** | Malicious or suspicious activity that happened with **no** fired alert. That is a **false negative** (**1.4.2**). |
| **Detection gap** | The logs exist, but no detection (rule or analytic) would have caught it. |
| **Visibility gap** | You cannot see it even if you look — the telemetry is not there. |

A false negative is not a fired alert you dislike. It is activity that should have been detected and was not. You find it in related logs, in a hunt, or after an incident.

The hunt **product** is a **package**: more hosts, a named gap, something detection engineering can take (**0.4**). It is **not** a rewrite of the SOC ticket. SOC still owns the incident they already labeled.

This lesson does **not** pick a hunt type (**3.2.1**). It does **not** write a hunt card (**3.2.2**). It does **not** invent a hunt ticket (**3.7**). Mapping a hunt onto ATT&CK is later (**3.5.1**).

**What good looks like:** someone asks why hunting exists. You name missed activity and gaps. Someone asks for an example. You name something existing controls did not catch, and something a hunt would look for that the first alert did not require.

Incident **A12** is the process alert already taught: `wscript` launched encoded PowerShell on **WS-JLEE**. That alert fired. It did **not** require the registry Run key.

- **Missed activity:** HTTP shows `GET /update.exe` to `203.0.113.88:8080`, and **no** alert fired. That is a false negative (**1.4.2**), not a noisy item in the queue.
- **Look for (not on the first alert):** HKCU Run value **`Updater`** pointing at `%TEMP%\update.exe`; `update.exe` or another `invoice.vbs` on **other** hosts.
- **Detection gap:** registry logs show **`Updater`**, but no detection fired on that value. The telemetry is there; the rule is not.
- **Visibility gap:** if those hosts have no registry telemetry, a hunt for **`Updater`** cannot see it. Name the hole. Do not pretend the hunt ran.

---

## 2. Knowledge Check

1. Threat hunting rewrites the SOC ticket with a better story. True or false?
2. What two jobs does hunting exist to do in the security program?
3. HTTP shows `GET /update.exe` to `203.0.113.88:8080`, and no alert fired. The first process alert did not require the HKCU Run value `Updater`. Name the missed activity, and name one thing a hunt should look for that was not on that first alert.

---

## 3. Summary

Hunting finds activity the alerts missed, and it names detection and visibility gaps. The product is a package, not a rewritten SOC ticket.

**Next:** **3.2.1** Hunt types.

---

## 4. Related modules

- 0.3 – Jobs in one sentence
- 0.4 – How work can move
- 1.4.2 – Alert classification
- 2.12.3 – Local dissemination channels (previous track)
- 3.2.1 – Hunt types
