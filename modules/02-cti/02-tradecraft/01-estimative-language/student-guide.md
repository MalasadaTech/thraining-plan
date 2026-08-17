# Module 2.2.1 – Estimative Language

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

CTI analysts pick a **likelihood word** so the reader does not guess whether “could be” means *likely* or *remote*. **Confidence** (low / medium / high) is how good the evidence is (**2.1.7**). This hour is **how probable**. You do **not** assign Admiralty letters (**2.2.3**). You do **not** write the actor profile (**2.11**).

**Purpose:** Make uncertainty comparable. Do not hide behind “we believe.”

**Classroom terms (this lesson only — not a live ODNI card):** almost certainly · highly likely · likely · even chance · unlikely · highly unlikely · remote.

If your shop publishes a term card, use it. Do not invent percents as policy.

**What good looks like:**

- **Write:** “The update domain is **likely** the payload host for **A12**.” Likelihood. Add confidence separately if you have it: “medium confidence.”
- **Interpret:** “It is **remote** that this is ordinary browsing.” That is very low likelihood — not “we have no idea.”
- **Fail:** “Could be PRD.” No term. Reader cannot compare it to the next product.

---

## 2. Knowledge Check

1. “Likely” and “high confidence” mean the same thing. True or false?
2. Why does estimative language exist?
3. Write one **A12** sentence that uses a classroom term (not “could be”).

---

## 3. Summary

Pick a term. Likelihood ≠ confidence. “Could be” is not a term.

**Next:** **2.2.2** Structured analytic techniques.

---

## 4. Related modules

- 2.1.8 – Collection sources (previous)
- 2.2.2 – Structured analytic techniques
- 2.1.7 – Attribution confidence (not this hour)
- 2.2.3 – Admiralty Code
