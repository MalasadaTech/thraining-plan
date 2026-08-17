# Module 4.1 – What DE owns

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.1 B / C / C ; 4.1.1 3c / 4c / 4c  
- SOC: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
- Hunter: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
- CTI: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what Detection Engineering **owns**.
2. Given a piece of work, say whether it is **DE**, a **nominator**, **1.3**, or a **block**.

**Mapped Proficiency Items:**
- K: 4.1 – What DE owns
- T: 4.1.1 – Sort work to DE, nominator, 1.3, or block

---

## 1. Key Concepts

**0.2** said the detection engineer turns what we learned into lasting rules. This hour is what that desk **owns**.

DE owns the **set of detections**: **new**, **change**, **retire**, **deploy**.

**SOC**, **hunt**, and **CTI** **nominate**. The draft need not be perfect. A sketch is still DE’s to review. “Rough” is not “not DE’s problem.”

**1.3** is how a rule *works* (syntax, a first read/write). This section is how we **run** detections as a service. Do not write SIGMA, Suricata, YARA, or SIEM here.

**Firewall / IA** **blocks**. DE does not. A block request is not a DE deploy.

**What good looks like (4.1.1):** someone hands you a piece of work. You say DE, nominator, 1.3, or a block. You reject two mixes: treating a rough nomination as not DE, and treating a block request as a deploy.

- Given: “Write me a SIGMA rule for this log.” That is **1.3**, not this section.
- Given: “We keep missing this. Can you look?” That is a **nomination**. Rough is still DE’s to review.
- Given: “Block this IP at the firewall.” That is a **block**, not a DE deploy.

Do not invent a ticket name. Do not invent a field list. Those wait for **4.8**, and you obtain them.

---

## 2. Knowledge Check

1. What four things does DE own on the set of detections?
2. A rough nomination is not DE’s problem. True or false?
3. Someone asks you to block an IP at the firewall. Is that DE, a nominator, 1.3, or a block?

---

## 3. Summary

DE owns new, change, retire, and deploy. Nominations can be rough. 1.3 is how a rule works. A block is not a DE deploy.

**Next:** **4.2** Making a detection sound and meeting shop requirements.

---

## 4. Related modules

- 0.2 – Jobs in one sentence
- 0.3 – How work can move
- 1.3 – Detection authoring (how a rule works)
- 4.2 – Making a detection sound and meeting shop requirements
