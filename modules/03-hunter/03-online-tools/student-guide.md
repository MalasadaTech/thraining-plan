# Module 3.3.1 – Tool Capabilities for Hunting

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.3.1 B / C / C ; 3.3.1.1–3.3.1.3 3c / 4c / 4d  
- SOC: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 1a / 2b / 3c ; 3.3.1.3 1a / 2b / 3c  
- CTI: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 2b / 3c / 4c ; 3.3.1.3 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name each tool’s **hunt** strength and **hunt** limit (VirusTotal, AnyRun, URLScan, Silent Push).
2. From a classroom result card, pull a **hunt lead** and turn it into a **precise** internal SIEM or Zeek query.

**Mapped Proficiency Items:**
- K: 3.3.1 – Tool capabilities for hunting
- T: 3.3.1.1 – Perform advanced querying and pivoting in VirusTotal, AnyRun, URLScan, and Silent Push
- T: 3.3.1.2 – Extract actionable hunting leads from external tool results
- T: 3.3.1.3 – Convert external findings into precise internal SIEM or Zeek queries

---

## 1. Key Concepts

Hunters take a finding from an external tool and turn it into a search they can run **here**, in the SIEM or in Zeek. They do that because a public detection count, a “malicious” tag, or a screenshot does not tell you whether that activity happened on your network. That is the job in this lesson: name each tool’s hunt strength and hunt limit, pull a lead you can actually search, and write a **precise** internal query.

You work from a **classroom result card** — a copy of an external-tool result this lesson provides. You write what the card shows. You do not log in. You do not need a live vendor account.

When to pick a tool is **0.7**. How CTI reads each platform’s tabs is **2.9**. This lesson is that conversion. It is not those lessons.

| Tool | Hunt strength | Hunt limit |
|------|---------------|------------|
| **VirusTotal** | Linked objects and sandbox events (Relations / Behavior) can name a host or dropped file | A detection count is not a hunt query |
| **AnyRun** | Process and network facts from a detonation | A “malicious” tag is not a query |
| **URLScan** | Requested hosts on a URL | A screenshot is not a query |
| **Silent Push** | Other names on an **A** record (an IPv4 mapping) or an **NS** (nameserver) | The whole **/24** (a 256-address block) is noise |

**Query** means you look up a seed the card already has — a hash, an IP, a URL — and you write the related object the card shows. **Pivot** means you take that object and name the next related object on the **same** card: a contacted host, a dropped file, another name on the same A record. You do not invent a sibling. You do not open a live account.

A **hunt lead** is a named artifact you can search internally: an IP, a port, a URI, a file name, a hostname. A detection count, a “malicious” tag, or a screenshot is not a lead.

A **precise** query names that lead in SIEM or Zeek — the IP **and** the port **and** the URI. It is not a filter that matches every destination (`dest=*`). It is not the whole `/24`.

**What good looks like:**

- **Query / pivot:** the card shows the hash of `update.exe` contacted `203.0.113.88` on port `8080`. You name that host and port. You do not write a sibling domain you did not see. You do not query `203.0.113.0/24`.
- **Lead:** `GET /update.exe` to `203.0.113.88:8080`. Not “VirusTotal said malicious.”
- **Convert:** Zeek `http` `id.resp_h == 203.0.113.88 && id.resp_p == 8080 && uri == "/update.exe"` (or the SIEM equivalent). **Not** `dest=*`. **Not** a `/24`.

---

## 2. Knowledge Check

1. A VirusTotal detection count is a hunt query. True or false?
2. Name one hunt limit for Silent Push.
3. The classroom result card shows `GET /update.exe` to `203.0.113.88:8080`. Write one precise Zeek or SIEM query. Do not use a `/24`.

---

## 3. Summary

Each tool has a hunt strength and a hunt limit. A lead is a named artifact you can search here. The query names that lead — not a count, not a tag, not a screenshot, and not a whole `/24`.

**Next:** **3.4.1** Assessing CTI for hunting value.

---

## 4. Related modules

- 3.2.2 – Hunt development concepts
- 3.4.1 – Assessing CTI for hunting value
- 0.7 – External tools (when to pick)
- 2.9 – Platform-specific skills
- 1.2.5 – HTTP engine
