# Module 0.5 – How this course is laid out

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.5 A / B / B ; 0.5.1 1a / 2b / 2b  
- Hunter: 0.5 A / B / B ; 0.5.1 1a / 2b / 2b  
- CTI: 0.5 A / B / B ; 0.5.1 1a / 2b / 2b  
- DE: 0.5 A / B / B ; 0.5.1 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the order of the rest of this course.
2. Say what **DYA** and **PRD** are, and that they come back as one incident after the lessons.
3. Given a step in the flow, name the next hand-off and whose **product** it is.

**Mapped Proficiency Items:**
- K: 0.5 – How this course is laid out
- T: 0.5.1 – Given a step in the flow, name the next hand-off and whose product it is

---

## 1. Key Concepts

**0.4** was overlap. This hour is the map of the rest of the course.

**Order after this intro:** SOC analyst, then CTI, then hunting, then detection engineers.

**Inside SOC:** you learn what detections *are* before you live in the alert queue.

**Site-specific** “how we do it here” comes later. It will differ by shop. Do not invent your shop’s ticket names here.

**DYA and PRD again.** **Dixon, Yamada, & Associates (DYA)** is the law firm in this course. **Pink River Dolphin (PRD)** is the adversary name. Both are **fiction for this course**, not your site’s policy. After the lessons, a **companion story** retells the same flow you already have (alert → triage → IR and leadership → RFI → block and/or hunt package) as **one PRD / DYA incident**. We do not write that story this hour.

**What good looks like (0.5.1):** someone names a step. You name the **next hand-off** and **whose product** it is. You do not name how a site files the ticket.

- Given: triage is done. Next: incident response and notify leadership; and/or an RFI to intel. Products: IR contains and recovers; leadership is notified; intel’s product is later the intel note, not the ask.
- Given: intel found extra infrastructure. Next: whoever **blocks** (firewall / IA). Product: the block. Not a hunt.

---

## 2. Knowledge Check

1. After this intro, in what order do the four tracks run?
2. What are DYA and PRD? When do they come back as one incident?
3. Intel found extra infrastructure. Name the next hand-off and whose product it is.

---

## 3. Summary

SOC, then CTI, then hunting, then detections. Detections before the alert queue. Site-specific later. DYA and PRD are course fiction; the companion story retells this flow as one incident. Name the next hand-off and the product — not the ticket.

**Next:** **1.1** Process activity (start of the SOC analyst block).

---

## 4. Related modules

- 0.4 – Where the jobs lightly overlap
- 1.1 – Process activity
- [docs/story-bible.md](../../../docs/story-bible.md) – DYA / PRD names
