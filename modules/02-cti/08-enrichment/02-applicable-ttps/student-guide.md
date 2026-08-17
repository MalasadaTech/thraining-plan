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

1. Find TTPs in a report.
2. Keep only those that **apply to this environment** — and reject the rest.

**Mapped Proficiency Items:**
- K: 2.8.2 – Extracting applicable TTPs from intelligence reports
- T: 2.8.2.1 – Extract applicable TTPs from an intelligence report

---

## 1. Key Concepts

CTI analysts pull TTPs a defender **here** can use. Mapping IDs is **2.7.1**. “So what / impact” is **2.8.4**. This hour is **applicable to DYA as a law firm / Windows workstation shop** — not every T-ID in the PDF.

**Applicable when:** we have that platform, that path is possible here, and a defender could detect or hunt it.  
**Not applicable:** OT / ICS, macOS-only, a TTP we have no visibility for and no way to get — unless you *name* that gap.

Use **real** ATT&CK IDs only.

**What good looks like:**

- **Keep:** T1059.001 encoded PowerShell — **WS-JLEE** already showed it. Applies.
- **Reject:** a report’s “wipe OT historians” line — not this shop (story bible: OT does not fit). Not an impact paragraph (**2.8.4**). Just: **not applicable here**.

---

## 2. Knowledge Check

1. Every T-ID in a vendor PDF is applicable here. True or false?
2. What makes a TTP applicable?
3. Encoded PowerShell vs an OT-wipe TTP from a report — keep or reject each, and why?

---

## 3. Summary

Extract. Keep what this shop can see or hunt. Reject the rest. Not an impact write-up.

**Next:** **2.8.3** IOC handling.

---

## 4. Related modules

- 2.8.1 – Infra hop (previous)
- 2.8.3 – IOC handling
- 2.7.1 – ATT&CK mapping
- 2.8.4 – Relevance / impact
