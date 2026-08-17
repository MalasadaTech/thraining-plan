# Module 2.8.4 – Threat Relevance and Organizational Impact

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.4 B / C / C ; 2.8.4.1 3c / 4c / 4d  
- Hunter: 2.8.4 B / C / C ; 2.8.4.1 2b / 3c / 4c  
- SOC: 2.8.4 A / B / B ; 2.8.4.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say whether a finding **applies here**, and **what would change** if it is true.
2. Keep that line off PIR writing, TTP extract, and attribution.

**Mapped Proficiency Items:**
- K: 2.8.4 – Threat relevance and organizational impact
- T: 2.8.4.1 – Assess threat relevance and potential impact to the organization

---

## 1. Key Concepts

CTI analysts write the **so what here**. Applicable TTPs are **2.8.2**. PIRs are **2.1.4** / **2.12.1**. Attribution is **2.1.7**. This hour is two sentences: **relevance** and **impact**.

| Sentence | Meaning |
|----------|---------|
| **Relevance** | Does this finding apply to this mission / assets / platform? |
| **Impact** | If it is true, what would change here (host, mail, clients)? |

Do not invent OT impact. DYA is a law firm. Do not invent a PIR list.

**What good looks like:**

- **Relevant:** encoded PowerShell + update domain on **WS-JLEE** — we have that platform; we already saw it.
- **Impact:** IR has the host; the payload path is live on a user workstation. Not “nation-state crisis.” Not a new PIR.
- **Not relevant:** an OT-wipe finding. Impact: none here — we do not run that process.

---

## 2. Knowledge Check

1. Relevance is the same as writing a PIR. True or false?
2. What two sentences do you write?
3. **A12** on WS-JLEE — one relevance line and one impact line (no country, no PIR).

---

## 3. Summary

Applies here? What would change? Not a PIR. Not a country. Not a TTP list.

**Next:** **2.9.1** VirusTotal Relations and Behavior.

---

## 4. Related modules

- 2.8.3 – IOC handling (previous)
- 2.9.1 – VirusTotal
- 2.8.2 – Applicable TTPs
- 2.1.4 / 2.12.1 – Requirements
- 2.1.7 – Attribution
