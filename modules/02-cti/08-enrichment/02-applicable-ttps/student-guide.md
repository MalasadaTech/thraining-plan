# Module 2.8.2 – Extracting Applicable TTPs from Intelligence Reports

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.2 B / C / C ; 2.8.2.1 3c / 4c / 4d  
- Hunter: 2.8.2 B / C / C ; 2.8.2.1 3c / 4c / 4d  
- SOC: 2.8.2 A / B / B ; 2.8.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Find **TTPs** in a report — behaviors with a how, not slogans or indicator lists.
2. Keep only those that **apply to this environment**, and reject the rest.

**Mapped Proficiency Items:**
- K: 2.8.2 – Extracting applicable TTPs from intelligence reports
- T: 2.8.2.1 – Extract applicable TTPs from an intelligence report

---

## 1. Key Concepts

A vendor report often arrives with a long ATT&CK table. CTI analysts do not copy that table into the shop’s notes. They pull the behaviors a defender **here** can actually detect or hunt, because a list of techniques that cannot happen on this network wastes hunt and detection time. That is the job in this lesson: find the TTPs in the report, then keep only the ones that apply to this environment.

A **TTP** (tactic, technique, or procedure) is a **behavior** — how the adversary works. It is not an IOC (a hash, IP, or domain). Putting a new ATT&CK ID on activity is **2.7.1**. Writing the “so what here” line is **2.8.4**. This lesson is extract and apply.

**This environment** in class is **DYA**: a law firm with Windows workstations. **WS-JLEE** is a user workstation already in the course. At a real shop you take platform and visibility facts from that shop (**0.8**). Do not invent OT, macOS, or a plant network for DYA.

Use **real** ATT&CK IDs only. Do not invent an ID.

| In the report | Keep as a TTP candidate? |
|---------------|--------------------------|
| A **how**: tool, command, procedure, or ATT&CK ID tied to that how | Yes — it is a relevant TTP |
| IOC appendix (hashes, IPs, domains) | No — that is an indicator, not a TTP |
| Slogan (“they use persistence”) or a vendor group name | No — no how |
| ATT&CK ID with no how | No — not a finished extract |

**Applicable** when all three are true:

| Criterion | Meaning here |
|-----------|----------------|
| **Platform** | We have that OS / stack. DYA is Windows workstations, not OT / ICS and not macOS-only. |
| **Path** | The behavior can actually happen here (on our hosts, mail, or network). |
| **Use** | A defender here could detect or hunt it. If you have no visibility and no way to get it, it is not applicable unless you **name that gap** — and you still do not list it as something a defender here can use. |

**What good looks like:** someone gives you a report. You write keep / reject lines. You do not map a neighbor ID (**2.7.1**). You do not write an impact paragraph (**2.8.4**).

- Given: encoded PowerShell in the report, printed as **T1059.001** (PowerShell). **Keep.** DYA runs Windows workstations, and **WS-JLEE** already showed encoded PowerShell. A defender here can hunt or detect it.
- Given: a report line “wipe OT historians.” **Reject.** DYA is a law firm. It does not run OT (operational technology) plant historians. Write **not applicable here** — not a crisis sentence.

Do not copy every ATT&CK ID in the PDF. Do not keep a Unix-only or ESXi ransomware ID for this Windows shop.

---

## 2. Knowledge Check

1. Every ATT&CK ID in a vendor report is applicable here. True or false?
2. What three things make a TTP applicable to this environment?
3. Encoded PowerShell (**T1059.001**) vs an OT-wipe TTP from a report — keep or reject each, and why?

---

## 3. Summary

Find TTPs that have a how. Keep what this shop can see or hunt. Reject the rest. That is not an ATT&CK mapping class and not an impact write-up.

**Next:** **2.8.3** IOC handling.

---

## 4. Related modules

- 2.8.1 – Identifying additional adversary infrastructure (previous)
- 2.8.3 – IOC handling
- 2.7.1 – ATT&CK mapping
- 2.8.4 – Relevance / impact
- 0.8 – Environment / signal flow
- 3.4.2 – Extracting hunt leads from CTI
