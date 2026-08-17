# Module 2.1.5 – Ensuring Intelligence Is Actionable

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.5 B / C / C ; 2.1.5.1 3c / 4c / 4d  
- Hunter: 2.1.5 A / B / B ; 2.1.5.1 1a / 2b / 3c  
- SOC: 2.1.5 A / A / B ; 2.1.5.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name what makes intelligence **actionable**, and common reasons it fails.
2. Evaluate a piece and say **why** it is or is not actionable.

**Mapped Proficiency Items:**
- K: 2.1.5 – Ensuring intelligence is actionable
- T: 2.1.5.1 – Evaluate whether a piece of intelligence is actionable and explain why

---

## 1. Key Concepts

CTI analysts check whether the product lets someone **act** on the requirement (**2.1.4**). This hour is the **product**, not the question. You do **not** rewrite for audience (**2.1.6**). You do **not** write the actor profile (**2.11**). Hunt “can I hunt this?” is **3.4.1** — a different test.

| Actionable when | Fails when |
|-----------------|------------|
| It **answers the named requirement** | It is interesting, but not the question |
| A **who** can act | No role is named |
| A **what** they do is specific | “Be aware” / “monitor” with no next step |
| It is still **in time** for that decision | The window already closed |
| You state **how sure** you are | A slogan with no caveat |

“Interesting” is not a pass. A hash dump is usually still **data** (**2.1.1**), so it is not actionable intelligence.

**What good looks like:**

- **Actionable:** “We assess the update domain is the payload host for **A12**. IR has **WS-JLEE**. Treat the domain as such.” Answers the RFI. Who + what.
- **Not actionable:** “New activity in the news. Be aware.” No requirement answered. No who. No next step.

---

## 2. Knowledge Check

1. “Be aware” with no next step is actionable. True or false?
2. Name two reasons a product fails the actionable test.
3. “We assess the update domain is the **A12** payload host; IR has the host.” Actionable? Why?

---

## 3. Summary

Actionable = answers the question + who + what. Slogans fail. This is not the hunt-useful test.

**Next:** **2.1.6** Tailoring output to the audience.

---

## 4. Related modules

- 2.1.4 – Intelligence requirements (previous)
- 2.1.6 – Tailoring to audience
- 2.1.1 – Data / information / intelligence
- 3.4.1 – Assessing CTI for hunt value (different test)
