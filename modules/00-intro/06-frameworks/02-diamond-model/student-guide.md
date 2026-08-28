# Module 0.6.2 – Diamond Model

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.2.1 A / B / C ; 0.6.2.2 2b / 3c / 4c  
- Hunter: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- CTI: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- DE: 0.6.2.1 A / B / B ; 0.6.2.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the four Diamond vertices and say what the model is for.
2. Fill the four vertices from an incident or a short set of indicators and say which vertex is weakest.

**Mapped Proficiency Items:**
- K: 0.6.2.1 – Diamond Model
- T: 0.6.2.2 – Apply the Diamond Model to an incident or set of indicators

---

## 1. Key Concepts

You get an incident or a short set of indicators: a host, a tool, a domain. Someone still wants a group name on the write-up. Before you claim who did it, put what you actually have on four corners and see which corner is empty. That is the job in this lesson: fill the Diamond from evidence, and name the weakest vertex so you do not invent the adversary.

The **Diamond Model** organizes what you know about an activity so you can see what you do **not** know. It is not a verdict. It is not attribution.

The Diamond has four **vertices** (corners):

| Vertex | What goes here |
|--------|----------------|
| **Adversary** | Who (a name only if you have evidence — not a vendor PDF title) |
| **Capability** | What they used (tool, malware, technique) |
| **Infrastructure** | What they used to talk or host (IP, domain, mailbox) |
| **Victim** | Who was hit (host, user, org) |

Fill all four from the evidence you have. Name the **weakest** vertex — the one with the least evidence. That is the next question, not a guess you write as fact. A vendor name on a PDF is not Adversary evidence. A course-fiction name is not Adversary evidence either.

**What good looks like:** encoded PowerShell on a workstation talking to a domain. Victim is that host. Capability is encoded PowerShell. Infrastructure is that domain. Adversary is weakest, because you have no actor evidence. Do not put a course-fiction name in Adversary.

This lesson does not assign ATT&CK IDs (**0.6.1**). Putting Diamond on a CTI product is later (**2.7.2**). Kill Chain is next (**0.6.3**).

---

## 2. Knowledge Check

1. Name the four Diamond vertices.
2. What do you do with the weakest vertex?
3. Encoded PowerShell on a workstation talking to a domain. Which vertex is usually weakest, and why?

---

## 3. Summary

The Diamond Model has four vertices. Fill them from the evidence you have. Name the weakest. Do not invent the adversary.

**Next:** **0.6.3** Cyber Kill Chain.

---

## 4. Related modules

- 0.6.1 – MITRE ATT&CK
- 0.6.3 – Cyber Kill Chain
- 2.7.2 – Diamond Model application in CTI (later)
