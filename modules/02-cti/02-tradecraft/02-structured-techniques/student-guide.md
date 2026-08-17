# Module 2.2.2 – Structured Analytic Techniques

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.2 B / C / C ; 2.2.2.1 3c / 4c / 4d  
- Hunter: 2.2.2 A / B / B ; 2.2.2.1 1a / 2b / 3c  
- SOC: 2.2.2 A / A / A ; 2.2.2.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say why structured techniques exist, and when to use **ACH** versus a **Key Assumptions Check**.
2. Apply one of those two to a given problem.

**Mapped Proficiency Items:**
- K: 2.2.2 – Structured analytic techniques
- T: 2.2.2.1 – Apply a structured analytic technique and select the right one for a scenario

---

## 1. Key Concepts

CTI analysts use a **named method** so a favorite story does not win by habit. Estimative words are **2.2.1**. This hour is the **method**. You do **not** run Admiralty (**2.2.3**). You do **not** name a bias yet (**2.2.4**). You do **not** invent a third official technique as syllabus.

| Technique | Use when | What you do |
|-----------|----------|-------------|
| **Key Assumptions Check** | One claim is carrying the call | List the assumption; say what would break it |
| **Analysis of Competing Hypotheses (ACH)** | Two or more explanations are live | List hypotheses; see which evidence **hurts** each one |

**Purpose:** Slow the jump to one story. Pick the technique that matches the problem — do not run both to fill time.

**What good looks like:**

- **Key Assumptions Check:** Assumption: “a vendor APT name is who they are.” Break: the label is a PDF, not internals. That is why **2.1.7** rejected high nation-state on **A12**.
- **ACH:** H1 = update domain is the **A12** payload host. H2 = ordinary browse. The `:8080` `GET /update.exe` **hurts** H2. You do not need a full matrix to name that.

---

## 2. Knowledge Check

1. You should always run ACH and a Key Assumptions Check on every product. True or false?
2. When do you pick a Key Assumptions Check instead of ACH?
3. For **A12**, name one assumption a Key Assumptions Check would test.

---

## 3. Summary

Named method. ACH when two stories compete. Key Assumptions Check when one claim is carrying the call.

**Next:** **2.2.3** Admiralty Code.

---

## 4. Related modules

- 2.2.1 – Estimative language (previous)
- 2.2.3 – Admiralty Code
- 2.2.4 – Cognitive biases
- 2.1.7 – Attribution
