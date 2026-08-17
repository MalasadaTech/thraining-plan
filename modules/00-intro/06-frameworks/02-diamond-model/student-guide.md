# Module 1.5.2 – Diamond Model

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 1.5.2.1 A / B / C ; 1.5.2.2 2b / 3c / 4c  
- Hunter: 1.5.2.1 B / C / C ; 1.5.2.2 3c / 4c / 4d  
- CTI: 1.5.2.1 B / C / C ; 1.5.2.2 3c / 4c / 4d  
- DE: 1.5.2.1 A / B / B ; 1.5.2.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the four Diamond vertices.
2. Fill the four vertices from a short activity set and say which vertex is weakest.

**Mapped Proficiency Items:**
- K: 1.5.2.1 – Diamond Model  
  SOC A / B / C · Hunter B / C / C · CTI B / C / C · DE A / B / B
- T: 1.5.2.2 – Apply the Diamond Model to an incident or set of indicators  
  SOC 2b / 3c / 4c · Hunter 3c / 4c / 4d · CTI 3c / 4c / 4d · DE 1a / 2b / 2b

---

## 1. Key Concepts

ATT&CK named the **behavior**. You still have four holes in the story: who, with what, through what, against whom. Diamond is how you see which hole is empty.

**Purpose.** Organize what you know about an activity into four corners so you can see what you do **not** know. It is not a verdict. It is not attribution.

**The four vertices**

| Vertex | What goes here |
|--------|----------------|
| **Adversary** | Who (a name only if you have evidence — not a vendor PDF title) |
| **Capability** | What they used (tool, malware, technique) |
| **Infrastructure** | What they used to talk or host (IP, domain, mailbox) |
| **Victim** | Who was hit (host, user, org) |

**How you use it.** Fill all four from what you actually have. Name the **weakest** vertex — the one with the least evidence. That is the next question, not a guess you write as fact.

**What good looks like (1.5.2.2):** encoded PowerShell on a workstation talking to a domain. Victim = that host. Capability = encoded PowerShell. Infrastructure = that domain. Adversary = weakest (you have no actor evidence). Do not put a course-fiction name in Adversary.

Kill Chain is next (**1.5.3**).

---

## 2. Knowledge Check

1. Name the four vertices.
2. What do you do with the weakest vertex?
3. Encoded PowerShell on a workstation to a domain. Which vertex is usually weakest, and why?

---

## 3. Summary

Four corners. Fill what you have. Name the empty one. Do not invent the adversary.

**Next:** **1.5.3** Cyber Kill Chain.

---

## 4. Related modules

- 1.5.1 – MITRE ATT&CK
- 1.5.3 – Cyber Kill Chain
- 3.11 – Actor products (later)
