# Module 2.2.1 – Estimative language

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.1 B / C / C ; 2.2.1.1 3c / 4c / 4c  
- Hunter: 2.2.1 A / B / B ; 2.2.1.1 1a / 2b / 3c  
- SOC: 2.2.1 A / A / A ; 2.2.1.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why estimative language exists, and use a classroom term for **likelihood**.
2. Write or interpret a judgment: the term is the likelihood, not the **confidence** from **2.1.7**.

**Mapped Proficiency Items:**
- K: 2.2.1 – Estimative language
- T: 2.2.1.1 – Use and interpret estimative language in analytic judgments

---

## 1. Key Concepts

CTI analysts write judgments that other people act on. Those people should not have to guess whether “could be” means *likely* or *remote*. That is the job in this lesson: pick a **likelihood** word so the next reader can compare products. **Confidence** (low / medium / high) is how good the evidence is (**2.1.7**). This lesson is how probable.

Estimative language exists to make uncertainty comparable. Do not hide behind “we believe.”

| Term | Meaning |
|------|---------|
| **almost certainly** | Near certain. You would be surprised if it were not so. |
| **highly likely** | Very probable. Strongly on the “is so” side. |
| **likely** | More probable than not. Clearly above even. |
| **even chance** | About as likely as not. |
| **unlikely** | More probable that it is not so. |
| **highly unlikely** | Very improbable. Strongly on the “is not” side. |
| **remote** | Almost no chance. |

These are **classroom terms for this lesson**. They are not a live ODNI (US Intelligence Community) card. If your shop publishes a term card, use that card. Do not invent percents as policy.

The estimative term is how probable the claim is. That is the uncertainty the term communicates. People sometimes call that term a **confidence level**. In this lesson that still means how probable — not the 2.1.7 evidence scale. You can write both in one line: “**likely**, medium confidence.” The first word is probability. The second is how good the sourcing is.

You do **not** assign Admiralty letters (**2.2.3**). You do **not** write the actor profile (**2.11**).

**What good looks like:** someone gives you a claim. You pick a classroom term, or you read the term that is already there. You do not leave the reader to guess.

- **Write:** “The update domain is **likely** the payload host for incident **A12**.” That is likelihood. Add confidence separately if you have it: “medium confidence.”
- **Interpret:** “It is **remote** that this is ordinary browsing.” That is very low likelihood — not “we have no idea.”
- **Fail:** “Could be PRD.” **PRD** is the course-fiction adversary, and “could be” is still not a term. The next reader cannot compare it to the next product.

---

## 2. Knowledge Check

1. “Likely” and “high confidence” mean the same thing. True or false?
2. Why does estimative language exist?
3. Write one **A12** sentence that uses a classroom term (not “could be”).

---

## 3. Summary

Pick a term. Likelihood is not confidence. “Could be” is not a term.

**Next:** **2.2.2** Structured analytic techniques.

---

## 4. Related modules

- 2.1.8 – Collection sources (previous)
- 2.2.2 – Structured analytic techniques
- 2.1.7 – Attribution confidence (not this lesson)
- 2.2.3 – Admiralty Code
