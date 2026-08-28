# Module 3.7.1 – Hunt control and lead management

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.1 B / C / C ; 3.7.1.1 3c / 4c / 4c  
- SOC: 3.7.1 A / A / B ; 3.7.1.1 1a / 1a / 2b  
- CTI: 3.7.1 A / A / B ; 3.7.1.1 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that **how hunts are initiated and controlled**, and **how leftover leads are managed**, **varies by site**.
2. **Follow** the local process you were shown — or record that you **do not have the local process yet**. Do not invent a ticket or a board.

**Mapped Proficiency Items:**
- K: 3.7.1 – Hunt control and lead management
- T: 3.7.1.1 – Follow the local process for initiating and controlling a hunt

---

## 1. Key Concepts

A hunter who already has a named technique still does not start searching the live environment on their own. The shop decides **how a hunt is opened**, **who can change its scope or stop it**, and **where leftover findings go**. That path is local. Every shop builds its own. That is the job in this lesson: obtain that path and follow it, so a hunt is official — not only interesting.

You do **not** invent a hunt ticket, a lead board, or policy for the classroom firm (**DYA**). This course does **not** publish those. **3.2.2** taught the classroom hunt card. **3.6.3** scoped one named technique. This lesson is the site path that makes a hunt official. How the hunt is written down is **3.7.2**. Finished outputs and hand-off are **3.7.3**. The SOC queue is **1.5**.

| Piece | What it is | You do not invent |
|------|------------|-------------------|
| **Initiate** | How a hunt is opened here — who may start it, and on what path | A ticket name so the hunt looks official |
| **Control** | Who may widen scope, pause, or stop | Running a hunt because the technique is interesting |
| **Leads** | Where leftovers that are not this hunt’s scope are parked, and who triages them | A personal spreadsheet or classroom board as shop policy |

A hunt **lead** in this lesson is leftover work from a hunt that is not this hunt’s scope. It is not the TTP you extracted from a CTI report (**3.4.2**). You obtain where those leftovers go. You do not stand up a board.

**Obtain-and-follow.** Ask where the initiate / control / lead path lives (the role or place your lead names). Use that path. If no one has shown you the process, write **I do not have the local process yet.** If an instructor overlays a real shop path, that overlay is the path for the room. It is still not DYA policy.

A made-up ticket number, a DYA hunt board, and a spreadsheet treated as the shop’s lead process are invented. Do not use them.

**What good looks like:** someone asks you to open a hunt, change its scope, or park a leftover.

- **Obtain:** “I obtain the initiate, control, and lead path from [the role or place the instructor names, or my lead].” If none was shown: **“I do not have the local process yet.”**
- **Follow:** Use only the path you were shown. Do not open a hunt on a made-up ticket. “Not yet” is a pass.

Do not rewrite the classroom card (**3.2.2**). Do not invent a documentation form (**3.7.2**).

---

## 2. Knowledge Check

1. You should invent a DYA hunt ticket so the exercise has a number. True or false?
2. What three path pieces does this lesson obtain?
3. What do you write if no one has shown you the process?

---

## 3. Summary

Every shop has a path to initiate a hunt, control it, and manage leftover leads. Obtain that path. Follow what you were shown. If you do not have the process, write that. Do not invent a ticket or a board.

**Next:** **3.7.2** Hunt documentation standards.

---

## 4. Related modules

- 3.6.3 – Hunt for a specific persistence or privilege-escalation technique (previous)
- 3.7.2 – Hunt documentation standards
- 3.2.2 – Hunt development concepts (classroom card)
- 2.12.1 – Local intelligence requirements and priorities (same obtain-and-follow rule)
