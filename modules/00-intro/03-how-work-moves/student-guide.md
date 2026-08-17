# Module 0.3 – How work can move

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.3 A / B / B  
- Hunter: 0.3 A / B / B  
- CTI: 0.3 A / B / B  
- DE: 0.3 A / B / B  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name one possible path of work after an alert.
2. Say where extra infrastructure goes, and where a hunt package can go.

**Mapped Proficiency Items:**
- K: 0.3 – How work can move

---

## 1. Key Concepts

**0.2** named the jobs. This hour is how **work** can move between them. One possible path. Not the only way a shop runs. Not DYA policy.

**RFI** still means Request for Information: asking intel for more work on that alert.

**The path:**

1. An analyst gets an alert and **triages** it (sorts what it is and what to do next).
2. They send it to **incident response** and **notify leadership**.
3. They send an **RFI** to intel.
4. Intel works the RFI, **enriches** it (adds context), and may find more adversary infrastructure.
5. Extra infrastructure can go to whoever **blocks** (firewall / IA).
6. Intel can also hand hunters a **hunt package**.
7. That same package can go to **detection engineers** to write or tune rules (MDE, YARA, Suricata, SIGMA, and so on).

One person may wear two hats — that is **0.4**.

An alert on **WS-JLEE** can start this path. Do not write the ticket. Do not write the RFI. This hour only names the steps.

---

## 2. Knowledge Check

1. After triage, what two things can the analyst do with the alert besides asking intel?
2. Extra infrastructure goes to the hunt team. True or false?
3. Where can a hunt package go besides the hunt team?

---

## 3. Summary

Alert → triage → IR and leadership → RFI to intel → enrich. Extra infrastructure can be blocked. A hunt package can go to hunters and to detection engineers.

**Next:** **0.4** Where the jobs overlap.

---

## 4. Related modules

- 0.2 – Jobs in one sentence
- 0.4 – Where the jobs overlap
