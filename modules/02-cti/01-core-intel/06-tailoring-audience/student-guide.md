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

1. Say why **audience analysis** matters before you write.
2. Adjust **content**, **format**, and **detail** for a named reader — same facts, different product.

**Mapped Proficiency Items:**
- K: 2.1.6 – Tailoring output to the audience
- T: 2.1.6.1 – Adjust an intelligence product for a specified audience

---

## 1. Key Concepts

CTI analysts change **how they say the same facts** so the person who will act can use them. Leadership needs a short so-what they can support. IR and SOC need host, file, and domain they can work. The assessment does not change to please the reader. That is the job in this lesson: name who is reading, then adjust **content**, **format**, and **detail**.

Type (**2.1.3**) is the kind of answer. Whether the product can be acted on is **2.1.5**. This lesson is **who is reading**. You do **not** change the judgment. You do **not** write the finished actor profile (**2.11.1.2**). You do **not** pick the SOC ticket type (**1.5**). Dissemination channels in depth are **2.11.2**.

This course uses one incident as fiction. **A12** is that case: user `jlee` on host **WS-JLEE** ran encoded PowerShell from a script. IR has the host. A file in Temp (`invoice.vbs`) and an update domain are in the case. You already have the facts. This lesson is two products from those facts, not a new plot.

**Audience analysis** is naming who will read the product and what they can do with it. Do that before you write. Leadership owns awareness and support; they cannot work a file hash. IR and SOC own the host and the next technical step; they need path and domain. If you skip that step, you send the wrong shape: a hash dump the lead cannot use, or a one-liner IR cannot work.

The people who will use the product are the **consumers**. In this lesson those two consumers are leadership and IR / SOC.

| You adjust | Meaning |
|------------|---------|
| **Content** | Which facts this person needs to act |
| **Format** | One sentence versus a short paragraph |
| **Detail** | Hash and path versus no hash |

The facts stay. The judgment stays. You cut or keep what that reader needs. Leadership gets a **one-liner**. They do **not** need the file hash. IR / SOC can have host, user, process, and Temp `invoice.vbs`.

**What good looks like:** someone names the reader. You write that product. You do not invent a second incident.

- **Leadership:** “**WS-JLEE** / `jlee` ran encoded PowerShell from a script; IR has the host.” No hash.
- **IR / SOC:** same case plus Temp `invoice.vbs` and the update domain. Same facts. More detail. Not a different plot.

Do not drop the assessment so the line sounds softer. Do not pick email versus ticket yet (**2.11.2**).

---

## 2. Knowledge Check

1. Tailoring means you change the judgment so leadership likes it. True or false?
2. What three things do you adjust for a named audience?
3. Same A12 facts: `jlee` on **WS-JLEE** ran encoded PowerShell from Temp `invoice.vbs`; IR has the host; the update domain is in the case. Write the leadership line (no hash) and what you add for IR.

---

## 3. Summary

Name who is reading before you write. Same facts. Different content, format, and detail. Leadership does not need the hash.

**Next:** **2.1.7** Attribution.

---

## 4. Related modules

- 2.1.5 – Actionable intelligence
- 2.1.7 – Attribution
- 2.11.2 – Dissemination channels
- 1.5 – SOC report types / routing
