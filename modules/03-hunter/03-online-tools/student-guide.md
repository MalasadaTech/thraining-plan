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

1. Say each tool’s **hunt** strength and limit (VT, AnyRun, URLScan, Silent Push).
2. Pull a **hunt lead** from a classroom card and turn it into a **precise internal** SIEM or Zeek query.

**Mapped Proficiency Items:**
- K: 3.3.1 – Tool capabilities for hunting
- T: 3.3.1.1 – Advanced querying and pivoting in those four tools
- T: 3.3.1.2 – Extract actionable hunting leads from external results
- T: 3.3.1.3 – Convert external findings into precise internal SIEM or Zeek queries

---

## 1. Key Concepts

Hunters use external tools to **seed an internal search**. When to pick a tool is **0.7**. CTI tab depth is **2.9**. This hour is **hunt convert**. Card only. No live account.

| Tool | Hunt strength | Hunt limit |
|------|---------------|------------|
| **VirusTotal** | Relations / Behavior can name a host or dropped file | Reputation count is not a hunt question |
| **AnyRun** | Process / network from a detonation | A “malicious” tag is not a query |
| **URLScan** | Requested hosts on a URL | A screenshot is not a query |
| **Silent Push** | Other names on an A / NS | Whole `/24` is noise |

**What good looks like:**

- **Lead:** card shows `GET /update.exe` to `203.0.113.88:8080`.
- **Convert:** Zeek/HTTP `id.resp_h == 203.0.113.88 && id.resp_p == 8080 && uri == "/update.exe"` (or SIEM equivalent). **Not** `dest=*` and **not** a /24.

---

## 2. Knowledge Check

1. A VirusTotal detection count is a hunt query. True or false?
2. Name one hunt limit for Silent Push.
3. Turn the `:8080` `/update.exe` lead into one precise Zeek or SIEM query (not a /24).

---

## 3. Summary

Hunt strength vs limit. Lead → precise internal query. Card only.

**Next:** **3.4.1** Assessing CTI for hunting value.

---

## 4. Related modules

- 3.2.2 – Hunt card (previous)
- 3.4.1 – CTI triage
- 0.7 / 2.9 – Survey / CTI tab depth
- 1.2.5 – HTTP engine
