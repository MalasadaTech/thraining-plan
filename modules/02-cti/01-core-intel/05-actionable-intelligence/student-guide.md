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

CTI analysts check whether a write-up lets someone **act**. An interesting finding is not enough. Someone has to be able to do a specific next step, in time, on the question the work was supposed to answer. That is the job in this lesson: say whether a piece is **actionable**, and why.

**Actionable** intelligence is a judged answer someone can use. It is not a slogan, and it is not a pile of raw facts. The **requirement** is the question the work exists to answer. This lesson scores the **product** — the write-up — against that question. **2.1.4** wrote the question. This lesson does not rewrite the product for a different audience (**2.1.6**). It does not write an actor profile (**2.11**). Whether a hunter can hunt from the report is a different test (**3.4.1**).

| Actionable when | Fails when |
|-----------------|------------|
| It **answers the named requirement** | It is interesting, but not the question |
| A **who** can act | No role is named |
| A **what** they do is specific | “Be aware” / “monitor” with no next step |
| It is still **in time** for that decision | The window already closed |
| You state **how sure** you are | A slogan with no caveat |

“Interesting” is not a pass. A hash dump with no judgment and no next step is still **data**, so it is not actionable intelligence.

**What good looks like:** someone gives you a product. You say whether it is actionable, and why. You do not rewrite it for a new reader.

- **Actionable:** “We assess the update domain is the payload host for **A12**. IR has **WS-JLEE**. Treat the domain as the payload host.” It answers the named question. It names who acts and what they do.
- **Not actionable:** “New activity in the news. Be aware.” It answers no requirement. It names no who. It gives no next step.

---

## 2. Knowledge Check

1. “Be aware” with no next step is actionable. True or false?
2. Name two reasons a product fails the actionable test.
3. “We assess the update domain is the **A12** payload host; IR has the host.” Actionable? Why?

---

## 3. Summary

Actionable intelligence answers the named question, names a who, and names a specific what. Slogans and “be aware” fail. This is not the hunt-useful test.

**Next:** **2.1.6** Tailoring output to the audience.

---

## 4. Related modules

- 2.1.4 – Intelligence requirements (previous)
- 2.1.6 – Tailoring to audience
- 2.1.1 – Data / information / intelligence
- 3.4.1 – Assessing CTI for hunt value (different test)
