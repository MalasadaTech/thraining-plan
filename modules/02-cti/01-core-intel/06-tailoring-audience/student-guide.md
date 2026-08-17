# Module 2.1.6 – Tailoring Output to the Audience

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.6 B / C / C ; 2.1.6.1 3c / 4c / 4d  
- Hunter: 2.1.6 A / B / B ; 2.1.6.1 1a / 2b / 3c  
- SOC: 2.1.6 A / A / B ; 2.1.6.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why audience analysis matters.
2. Adjust **content, format, and detail** for a named consumer — same facts, different product.

**Mapped Proficiency Items:**
- K: 2.1.6 – Tailoring output to the audience
- T: 2.1.6.1 – Adjust an intelligence product for a specified audience

---

## 1. Key Concepts

CTI analysts change **how they say it** so the consumer can use it. The facts do not change. Type (**2.1.3**) is the kind of answer. This hour is **who is reading**. You do **not** change the judgment to please them. You do **not** write the finished actor profile (**2.11.1.2**). You do **not** pick the SOC ticket type (**1.5**). Dissemination channels in depth are **2.11.2**.

| You adjust | Meaning |
|------------|---------|
| **Content** | Which facts this person needs to act |
| **Format** | One sentence vs a short para vs a ticket field |
| **Detail** | Hash and path vs no hash |

Leadership gets a **one-liner**. They do **not** need the file hash (**story bible**). IR / SOC can have host, user, process, Temp `invoice.vbs`.

**What good looks like:**

- **Leadership:** “**WS-JLEE** / `jlee` ran encoded PowerShell from a script; IR has the host.” No hash.
- **IR / SOC:** same case plus Temp `invoice.vbs` and the update domain. Same facts. More detail. Not a different plot.

---

## 2. Knowledge Check

1. Tailoring means you change the judgment so leadership likes it. True or false?
2. What three things do you adjust?
3. Write the **A12** fact for leadership (no hash) versus for IR (what you add).

---

## 3. Summary

Same facts. Different content, format, and detail. Leadership does not need the hash.

**Next:** **2.1.7** Attribution.

---

## 4. Related modules

- 2.1.5 – Actionable intelligence (previous)
- 2.1.7 – Attribution
- 2.11.2 – Dissemination channels (not this hour)
- 1.5 – SOC report types / routing
