# Module 3.1 – Purpose of Threat Hunting

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.1.1 B / C / C ; 3.1.1.1 3c / 4c / 4c ; 3.1.1.2 3c / 4c / 4d  
- SOC: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
- CTI: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain why hunting exists in the program: find **missed** activity and **gaps**.
2. Name examples of activity existing controls can miss.

**Mapped Proficiency Items:**
- K: 3.1.1 – Purpose of Threat Hunting
- T: 3.1.1.1 – Explain the purpose of threat hunting in the context of the security program
- T: 3.1.1.2 – Identify examples of activity that existing controls might miss

---

## 1. Key Concepts

Hunters look for **activity the alerts missed**, and for **places the detections cannot see**. SOC already labeled the **A12** process alert (**1.4**). CTI answered the domain RFI (**2.11.3**). This hour is **why hunt exists**. You do **not** write a hunt card (**3.2.2**). You do **not** pick a hunt type (**3.2.1**). You do **not** invent a hunt ticket (**3.7**).

| Job | Meaning |
|-----|---------|
| **Missed activity** | Bad things that happened with **no** queue row (false negatives) |
| **Gaps** | Telemetry or detections that would not have caught it even if you looked |

The hunt **product** is a package: more hosts, a gap, something DE can take (**4.x**). It is **not** a rewrite of the SOC ticket.

**What good looks like:**

- **Purpose:** After A12, hunt asks: who else has HKCU Run **`Updater`**, `%TEMP%\update.exe`, or another `invoice.vbs`? The first alert did **not** require the Run key (**story bible**).
- **Missed:** `GET /update.exe` to `203.0.113.88:8080` with **no** alert (**1.4.2** FN). That is missed activity, not a disliked queue row.

---

## 2. Knowledge Check

1. Hunt rewrites the SOC ticket with a better story. True or false?
2. What two jobs does hunting exist to do?
3. Name one **A12** thing existing controls missed, and one thing hunt should look for that was **not** on the first alert.

---

## 3. Summary

Hunt finds what alerts missed, and names the gap. The product is a package, not a rewritten ticket.

**Next:** **3.2.1** Hunt types.

---

## 4. Related modules

- 2.12.3 – Local CTI channels (previous track)
- 3.2.1 – Hunt types
- 1.4.2 – FN is a miss
- 4.x – DE takes the gap
