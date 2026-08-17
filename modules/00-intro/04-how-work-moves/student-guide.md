# Module 0.4 – How work can move

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- Hunter: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- CTI: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- DE: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name one possible path of work after an alert.
2. Say where extra infrastructure goes, and where a hunt package can go.
3. Given a step in the flow, name the next hand-off and whose **product** it is.

**Mapped Proficiency Items:**
- K: 0.4 – How work can move
- T: 0.4.1 – Given a step in the flow, name the next hand-off and whose product it is

---

## 1. Key Concepts

**0.3** named the jobs. This hour is how **work** can move between them. One possible path. Not the only way a shop runs. Not DYA policy.

**RFI** still means Request for Information: asking intel for more work on that alert.

**The path:**

1. An analyst gets an alert and **triages** it (sorts what it is and what to do next).
2. They send it to **incident response** and **notify leadership**.
3. They send an **RFI** to intel.
4. Intel works the RFI, **enriches** it (adds context), and may find more adversary infrastructure.
5. Extra infrastructure can go to whoever **blocks** (firewall / IA).
6. Intel can also hand hunters a **hunt package**.
7. That same package can go to **detection engineers** to write or tune rules (MDE, YARA, Suricata, SIGMA, and so on).

One person may wear two hats — that is **0.5**.

An alert on **WS-JLEE** can start this path. Do not write the ticket. Do not write the RFI. This hour only names the steps.

**What good looks like (0.4.1):** someone names a step. You name the **next hand-off** and **whose product** it is. You do not name how a site files the ticket.

- Given: triage is done. Next: incident response and notify leadership; and/or an RFI to intel. Products: IR contains and recovers; leadership is notified; intel’s product is later the intel note, not the ask.
- Given: intel found extra infrastructure. Next: whoever **blocks** (firewall / IA). Product: the block. Not a hunt.

---

## 2. Knowledge Check

1. After triage, what two things can the analyst do with the alert besides asking intel?
2. Extra infrastructure goes to the hunt team. True or false?
3. Intel found extra infrastructure. Name the next hand-off and whose product it is.

---

## 3. Summary

Alert → triage → IR and leadership → RFI to intel → enrich. Extra infrastructure can be blocked. A hunt package can go to hunters and to detection engineers.

**Next:** **0.5** Where the jobs overlap.

---

## 4. Related modules

- 0.3 – Jobs in one sentence
- 0.5 – Where the jobs overlap
