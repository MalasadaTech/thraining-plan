# Module 2.9.3 – Silent Push

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.3 B / C / C ; 2.9.3.1 3c / 4c / 4d  
- Hunter: 2.9.3 A / B / B ; 2.9.3.1 2b / 3c / 4c  
- SOC: 2.9.3 A / A / B ; 2.9.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what Silent Push is for (passive DNS / infra context).
2. Enrich a seed and pivot to additional names or IPs **on a classroom card**.

**Mapped Proficiency Items:**
- K: 2.9.3 – Silent Push
- T: 2.9.3.1 – Enrich an indicator and pivot in Silent Push

---

## 1. Key Concepts

CTI analysts use Silent Push for **passive DNS and infra context**. When to pick it is **0.7**. SOA/RDAP classes are **2.5** / **2.6**. The hop sentence is **2.8.1**. This hour is **this UI**. Card only.

| Move | Job |
|------|-----|
| **Enrich** | What names have pointed at `203.0.113.88`? What A records has the update domain had? |
| **Pivot** | Other names with the same NS pair — if the card shows them |

**What good looks like:** enrich `203.0.113.88` → names on that A **on the card** (update domain, maybe `login-prd.net`). **Reject** treating the whole `/24` as theirs. Not on card is legal.

---

## 2. Knowledge Check

1. This hour is “when to pick Silent Push.” True or false?
2. What two jobs do you do in this UI?
3. Enrich `203.0.113.88`. One legal pivot, and one thing you must reject.

---

## 3. Summary

PDNS / infra context. Enrich the seed. Pivot only what the card shows. Shared /24 is not theirs.

**Next:** **2.9.4** URLScan.

---

## 4. Related modules

- 2.9.2 – AnyRun (previous)
- 2.9.4 – URLScan
- 0.7 – When to pick Silent Push
- 2.6 / 2.8.1 – SOA / hop sentence
