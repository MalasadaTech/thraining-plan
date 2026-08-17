# Module 2.1.1 – Difference between Data, Information, and Intelligence

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.1 B / C / C ; 2.1.1.1 3c / 4c / 4c  
- Hunter: 2.1.1 A / B / B ; 2.1.1.1 1a / 2b / 3c  
- SOC: 2.1.1 A / A / A ; 2.1.1.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Define **data**, **information**, and **intelligence**, and say how they differ.
2. Categorize a given item as data, information, or intelligence.

**Mapped Proficiency Items:**
- K: 2.1.1 – Difference between data, information, and intelligence
- T: 2.1.1.1 – Correctly categorize examples as data, information, or intelligence

---

## 1. Key Concepts

CTI analysts **sort what landed on the desk** so they do not brief a raw hash as intel. SOC sent an RFI on the update domain / file (**1.5**). This hour you label the layer. You do **not** walk the lifecycle (**2.1.2**). You do **not** write a PIR (**2.1.4**). You do **not** write a finished product (**2.11**).

| Term | What it is | What it answers |
|------|------------|-----------------|
| **Data** | A raw fact as recorded | What was recorded? |
| **Information** | That fact with context (who / what / when / where) | What happened, in a story? |
| **Intelligence** | That story judged against a **question**, with a so-what | So what? What should someone do? |

Information describes. Intelligence **judges**. Renaming a feed “intel” does not make it so.

The path is a process, not a rename: **data → information → intelligence**. You add context, then you add a judgment against a question. The question can be informal (“is this domain the payload host for **A12**?”). How to write PIRs is **2.1.4**.

**What good looks like:**

- **Data:** `203.0.113.88`. Or the hash of Temp `invoice.vbs`. A field. No story.
- **Information:** That IP is the A record for the update domain. Temp `invoice.vbs` sat on **WS-JLEE** / `jlee`. Context. No judgment.
- **Intelligence:** We assess the update domain is the payload host for **A12**; treat it as such (block / keep working it). That answers the RFI question. It is not a **2.11** paper.

If you are unsure, it is not intelligence yet.

---

## 2. Knowledge Check

1. A hash with no other text is intelligence. True or false?
2. What must you add before information becomes intelligence?
3. “We assess the update domain is the payload host for **A12**; treat it as such.” Data, information, or intelligence?

---

## 3. Summary

Data = raw fact. Information = story. Intelligence = judged answer to a question. Sort the layer. Do not rename a feed.

**Next:** **2.1.2** Intelligence lifecycle.

---

## 4. Related modules

- 1.5.3 – Notification and distribution (previous — the RFI is the door)
- 2.1.2 – Intelligence lifecycle
- 2.1.4 – Intelligence requirements (not this hour)
- 2.11 – Finished intelligence products (not this hour)
