# Module 2.11.1 – Creating Finished Intelligence Products

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.11.1 B / C / C ; 2.11.1.1 3c / 4c / 4d ; 2.11.1.2 3c / 4c / 4d  
- Hunter: 2.11.1 A / B / B ; 2.11.1.1 1a / 2b / 3c ; 2.11.1.2 1a / 2b / 3c  
- SOC: 2.11.1 A / A / B ; 2.11.1.1 1a / 1a / 2b ; 2.11.1.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name what a **finished product** must contain, and evaluate a draft against those standards.
2. Produce a short **actor / activity profile** that does not invent a nation-state.

**Mapped Proficiency Items:**
- K: 2.11.1 – Creating finished intelligence products
- T: 2.11.1.1 – Draft a finished product and evaluate it against standards
- T: 2.11.1.2 – Produce a threat actor profile

---

## 1. Key Concepts

CTI analysts write a **finished product** so someone can use the judged answer. Collection and notes do not help until that answer is on the page to a standard. Pasting indicators out of a **TIP** (threat intelligence platform — the shop store of indicators and reports) is not that product. This lesson is how to draft the product, check it against those standards, and write a short profile of the cluster you can actually defend.

A finished product is intelligence written down: a judged answer to a named question. It is not a hash list. It is not a machine bundle. Audience rewrite is **2.1.6**. Attribution assessment (confidence versus evidence) is **2.1.7**. STIX is **2.10**. SOC ticket types are **1.5**. Who gets the product, and on which channel, is **2.11.2**. Local approval is **2.12**. How to run an **RFI** (request for information) queue is **2.11.3**.

| Type | What it is |
|------|------------|
| **Assessment** | A judged answer to a named question (for example: is this the payload host *here*?) |
| **Profile** | A short picture of an activity cluster or actor — what they do, not a country you invented |
| **RFI response** | A finished answer to a request for information. Pick the type that matches the question. The queue itself is **2.11.3**. |

Pick **one** type that matches the requirement. Do not staple all three into one dump.

| Required element | What to write |
|------------------|---------------|
| **Question** | The requirement the product answers |
| **What you know** | Sourced facts — what you used, not everything in the TIP |
| **Judgment** | An estimative term (**likely**, **unlikely**, and the rest of the classroom set). Not “could be.” |
| **So-what** | Who can act, and on what |
| **Confidence / caveat** | How good the evidence is, and what you do not know |

**Quality and analytic standards.** A draft **passes** when it answers the named requirement, names its sources, uses an estimative term, and does not invent a country. A **hash dump** fails. A TIP paste fails. A vendor “APT” name is a **label**, not proof of a government.

**A12** is the classroom incident on workstation **WS-JLEE**: encoded PowerShell, an update domain, and a distinctive nameserver pair. Use that cluster. Do not invent a nation-state.

**What good looks like:**

- **Draft.** Given: requirement = is the payload host *here*? **Pass:** the update domain is **likely** the **A12** payload host; IR has **WS-JLEE**; medium confidence; sources = Zeek A record (the name-to-IP the network sensor logged) and the host file (this host logged the talk). **Fail:** a hash dump with no question, no judgment, and no so-what.
- **Profile:** activity cluster (encoded PowerShell, update domain, distinctive nameserver pair). Victim host **WS-JLEE**. Vendor APT name stays a label. **Not** “nation-state PRD APT.”

---

## 2. Knowledge Check

1. A TIP paste is a finished product. True or false?
2. Name three required elements of a finished product.
3. Write a three-line **A12** profile that does **not** claim a country.

---

## 3. Summary

A finished product is the judged answer: question, what you know, judgment, so-what, and a caveat. Profile the cluster you can defend. Do not invent a government. Do not paste the TIP.

**Next:** **2.11.2** Dissemination.

---

## 4. Related modules

- 2.10.2 – STIX production (previous)
- 2.11.2 – Dissemination
- 2.1.6 / 2.1.7 – Audience / attribution
- 2.12 – Local approval
