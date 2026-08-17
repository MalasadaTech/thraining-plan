# Module 2.7.3 – Cyber Kill Chain in Intelligence Analysis

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.3 B / C / C ; 2.7.3.1 3c / 4c / 4c  
- Hunter: 2.7.3 B / C / C ; 2.7.3.1 3c / 4c / 4c  
- SOC: 2.7.3 A / B / B ; 2.7.3.1 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the seven Kill Chain stages.
2. Identify the stage of observed activity, reject the neighbor, and list **only supported** stages in the product.

**Mapped Proficiency Items:**
- K: 2.7.3 – Cyber Kill Chain in intelligence analysis
- T: 2.7.3.1 – Identify the Kill Chain stage of observed or reported activity

---

## 1. Key Concepts

CTI analysts put **progression** on a product so the reader sees what was observed — and what was not. The floor is **0.6.3**. This hour is a **report**. You do **not** map ATT&CK (**2.7.1**). You do **not** invent Reconnaissance you did not see.

Seven stages: Reconnaissance · Weaponization · Delivery · Exploitation · Installation · Command and Control · Actions on Objectives.

**What good looks like:**

- **`invoice.vbs` / `wscript` → encoded PowerShell:** **Installation** (or Delivery of the vbs). Cite the process. **Not** C2 — no beacon in that row.
- **GET `/update.exe` :8080:** Installation of the payload (or C2 if that is how you frame the channel). **Not** Reconnaissance.
- Product line: list **only** stages you can cite. Do **not** write Recon because “they must have scanned.”

---

## 2. Knowledge Check

1. You should list all seven stages on every product. True or false?
2. Name the seven stages in order.
3. `wscript` → `-enc`. Stage, and why not the neighbor?

---

## 3. Summary

Seven stages. Only what you saw. Reject the neighbor. Do not invent Recon.

**Next:** **2.7.4** DTF.

---

## 4. Related modules

- 2.7.2 – Diamond (previous)
- 2.7.4 – DTF
- 0.6.3 – Kill Chain floor
