# Module 1.4.1 – Alert Context and Investigation

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.1.1 A / B / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- Hunter: 1.4.1.1 B / C / C ; 1.4.1.2–1.4.1.6 2b / 3c / 4c  
- CTI: 1.4.1.1 A / A / B ; 1.4.1.2–1.4.1.4 1a / 1a / 2b ; 1.4.1.5–1.4.1.6 1a / 1a / 1a  
**Estimated Time:** 30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what context the alert already has (including a VirusTotal lookup of a hash, IP, or domain you have), what the config would fire, and name each hop upstream.
2. Say what related endpoint logs and PCAP **add** — or fail to add — versus the alert fields.

**Mapped Proficiency Items:**
- K: 1.4.1.1 – Alert context and investigation
- T: 1.4.1.2 – Review an alert and identify which context is present and which is missing
- T: 1.4.1.3 – Review the alert configuration and explain what would fire
- T: 1.4.1.4 – Trace an alert to its upstream detection logic and name each hop
- T: 1.4.1.5 – Collect related endpoint logs and state what they add (or fail to add)
- T: 1.4.1.6 – Collect related PCAP and state what it adds versus the alert fields

---

## 1. Key Concepts

SOC analysts **investigate the fired object**. **1.3** wrote the rule. This hour you do **not** write a new one. You do **not** classify TP/FP (**1.4.2**).

The alert that fires first in this course is the **process create**: `wscript` → encoded PowerShell (`jlee`). That is what the **1.3.1** / **1.3.4** detection keys on.

| Idea | What to do |
|------|------------|
| **Context** | Two columns: **present** / **missing**. Host, user, time, rule name, the field the rule keys on. If you have a **hash**, **IP**, or **domain**, look it up on **VirusTotal** (**0.7**). Write what VT adds or fails to add (reputation, “not in VT”). That is gathering context, not Relations / a 12-node graph (**3.9**). Missing is a gap, not “benign.” Do not invent a command line or a VT hit |
| **Configuration** | Read the detection behind the alert. One sentence: **what would fire**. Same field language as **1.3** |
| **Upstream hops** | Name each hop. Classroom pattern: Suricata sid → SIEM rule → SIEM alert. Some alerts are SIEM-only. Do not invent a Suricata hop |
| **Endpoint logs** | Pull **1.1** rows for that host and window. State what they **add** or **fail to add**. Opening the table is not the task. The Temp `invoice.vbs` file row can add the dropper path. The Run key is **not** required on this first pass (**2.x**) |
| **PCAP** | For a **network** alert: what the capture adds versus the alert fields (URI, SNI, payload). Why you pull PCAP is **1.2.1**. Sensors are **0.8**. If the alert is process-only and no capture exists, write **PCAP not applicable**. Do not invent a download path |

**What good looks like:**

- Context: present = host, user, rule, `powershell -enc`, parent `wscript`. Missing = dest IP, URI, file hash — unless you pull more. After the file row adds Temp `invoice.vbs` (or you have `203.0.113.88`), **VT** that hash or IP. Write the one-line result. Do not open Relations.
- Config: “PowerShell with `-enc` and parent `wscript` fires.”
- Hops: SIEM rule → SIEM alert (no Suricata unless the given has a sid).
- Endpoint logs: Sysmon 11 / `DeviceFileEvents` **adds** Temp `invoice.vbs`. If no process parent in the tenant, they **fail to add** it — say so.
- PCAP: on the `:8080` GET, PCAP can **add** the URI `/update.exe` if the alert only had IP:port. On this process alert, PCAP is **not applicable** until you have a flow.

---

## 2. Knowledge Check

1. The alert context is missing a parent process. That means the activity was benign. True or false?
2. Name the hops for a SIEM-only process alert.
3. You have the hash of Temp `invoice.vbs` and IP `203.0.113.88`. What do you look up on VirusTotal, and what is **not** this hour?

---

## 3. Summary

Present vs missing. Hash, IP, or domain you have goes to **VirusTotal**. What the config would fire. Name each hop. Endpoint logs and PCAP must **add** something — or you say they failed to. You do not classify and you do not write the rule.

**Next:** **1.4.2** Alert classification.

---

## 4. Related modules

- 1.3.4 – SIEM rules (previous)
- 1.4.2 – Alert classification
- 1.1.2 – Process activity
- 1.2.1 – Why pull PCAP
- 0.7 – External tools (VirusTotal)
- 0.8 – Where sensors sit
