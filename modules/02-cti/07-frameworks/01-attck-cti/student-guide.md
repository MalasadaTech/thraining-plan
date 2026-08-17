# Module 2.7.1 – MITRE ATT&CK for CTI Analysis and Reporting

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.1 B / C / C ; 2.7.1.1 3c / 4c / 4c  
- Hunter: 2.7.1 B / C / C ; 2.7.1.1 3c / 4c / 4c  
- SOC: 2.7.1 A / B / B ; 2.7.1.1 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use ATT&CK as a **CTI** label on a report or activity set — tactic, technique or sub-technique, evidence.
2. Reject the neighbor ID.

**Mapped Proficiency Items:**
- K: 2.7.1 – MITRE ATT&CK for CTI analysis and reporting
- T: 2.7.1.1 – Map activity or reports to MITRE ATT&CK

---

## 1. Key Concepts

CTI analysts put ATT&CK on a **product** so hunt and DE can reuse the same ID. The floor map is **0.6.1**. This hour is **report / activity-set** mapping. You do **not** redo hunt planning (**3.5**). You do **not** assign DTF P-IDs (**2.7.4**). You do **not** write T1059 as a SOC *category* (**1.4.4**).

Same rule as 0.6: tactic = why, technique = how, cite one field, reject the neighbor. An ID with no evidence is a slogan.

**What good looks like:**

- **Encoded PowerShell from `wscript` (A12):** Execution / **T1059.001** PowerShell. Cite `-enc` + parent. **Not** Command and Control — you have no beacon in this row.
- **GET `/update.exe` :8080:** Command and Control or Ingress Tool Transfer (**T1105**) only if the product is the *download*. **Not** T1059 — that ID is the process, not the GET.

---

## 2. Knowledge Check

1. This hour is hunt coverage planning. True or false?
2. What three things must a CTI ATT&CK line have?
3. `wscript` → `-enc` PowerShell. Tactic, ID, and why not C2?

---

## 3. Summary

Map the product. Cite the field. Reject the neighbor. Not hunt planning. Not a SOC category.

**Next:** **2.7.2** Diamond Model for CTI.

---

## 4. Related modules

- 2.6.1 – Advanced DNS (previous)
- 2.7.2 – Diamond
- 0.6.1 – ATT&CK floor
- 3.5 – Hunt planning
- 1.4.4 – Alert categories
