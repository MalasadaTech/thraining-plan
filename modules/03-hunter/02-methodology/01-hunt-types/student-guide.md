# Module 3.2.1 – Hunt Types

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.1 B / C / C ; 3.2.1.1–3.2.1.4 3c / 4c / 4c  
- SOC: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
- CTI: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the four hunt types.
2. Say what **execute** looks like for each type on **A12** — pick the type and the look-for.

**Mapped Proficiency Items:**
- K: 3.2.1 – Hunt types
- T: 3.2.1.1 – Execute an intel-driven hunt
- T: 3.2.1.2 – Execute a hypothesis-driven hunt
- T: 3.2.1.3 – Execute a reactive hunt
- T: 3.2.1.4 – Execute an anomaly-based hunt

---

## 1. Key Concepts

Hunters pick a **type** so the search has a reason. Purpose was **3.1**. The hunt *card* (hypothesis write-up) is **3.2.2**. This hour is **type + what execute means**. No lab. No invented ticket.

| Type | Starts from | Execute looks like (A12) |
|------|-------------|--------------------------|
| **Intel-driven** | A CTI fact (domain, hash, TTP) | Search hosts for the update domain / file CTI already worked |
| **Hypothesis-driven** | “If they persist, we should see X” | Search HKCU Run **`Updater`** because persistors leave that key |
| **Reactive** | A known incident | After A12, look for more `invoice.vbs` / `update.exe` on other hosts |
| **Anomaly-based** | Odd pattern, no intel yet | Hosts with GET `:8080` `/update.exe` that **never** alerted |

**What good looks like:** name the type, the seed, and the look-for. “Execute” is that product line — not a SIEM session this hour.

---

## 2. Knowledge Check

1. All four types start from a CTI report. True or false?
2. Name the four types.
3. “If they persist, we should see Run `Updater` on more hosts.” Which type, and what do you search?

---

## 3. Summary

Four types. Each has a different start. Execute = type + look-for, not a rewritten ticket.

**Next:** **3.2.2** Hunt development.

---

## 4. Related modules

- 3.1 – Purpose (previous)
- 3.2.2 – Hunt card / hypothesis write-up
- 2.11.3 – CTI RFI (intel seed)
- 3.6.3 – Hunt one named technique
