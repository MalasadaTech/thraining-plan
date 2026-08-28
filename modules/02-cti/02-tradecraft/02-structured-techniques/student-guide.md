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

1. Say why structured analytic techniques exist, and when to use **ACH** versus a **Key Assumptions Check**.
2. Apply one of those two to a given problem.

**Mapped Proficiency Items:**
- K: 2.2.2 – Structured analytic techniques
- T: 2.2.2.1 – Apply a structured analytic technique and select the right one for a scenario

---

## 1. Key Concepts

CTI analysts use a **named method** so a favorite story does not win by habit. A draft judgment often already has a preferred explanation. Before you publish, you pick a structured analytic technique that matches the problem and you apply it. That is the job in this lesson: slow the jump to one story, then show the work.

**2.2.1** was the likelihood word (how probable). This lesson is the **method**. It is **not** source letters (**2.2.3**). It is **not** a bias list (**2.2.4**). This lesson teaches two techniques only. Do not invent a third official technique as syllabus.

A **structured analytic technique** is a named way to test a call. You write the method down so someone else can see what you tested.

| Technique | Use when | What you do |
|-----------|----------|-------------|
| **Key Assumptions Check** | One claim is carrying the call | List the assumption. Say what would break it. |
| **Analysis of Competing Hypotheses (ACH)** | Two or more explanations are live | List the hypotheses. See which evidence **hurts** each one. |

**Purpose:** Make the jump to one story slower and inspectable. Pick the technique that matches the problem. Do not run both to fill time.

When you apply a technique in this course, the given is incident **A12** on `WS-JLEE`. You do not need the whole plot. Two facts are enough: a vendor PDF labels the cluster with an APT name, and the host fetched `update.exe` on port **8080**.

**What good looks like:**

- **Key Assumptions Check.** Given: a vendor PDF labels **A12** with an APT name, and the draft says that is who they are. **Assumption:** a vendor APT name is who they are. **Break:** the label is a PDF, not internals. You do not need a new technique to say that.
- **ACH.** Given: `GET /update.exe` on port **8080** to an update domain. **H1** = the domain is the payload host for **A12**. **H2** = ordinary browse. The `:8080` `GET /update.exe` **hurts** H2. You do not need a full matrix to name that.

Do not assign Admiralty letters. Do not name a bias. Do not write a 12-row ACH spreadsheet for this lesson.

---

## 2. Knowledge Check

1. You should always run ACH and a Key Assumptions Check on every product. True or false?
2. When do you pick a Key Assumptions Check instead of ACH?
3. For **A12**, name one assumption a Key Assumptions Check would test.

---

## 3. Summary

Use a named method. Pick **ACH** when two stories compete. Pick a **Key Assumptions Check** when one claim is carrying the call. Apply the one the problem needs.

**Next:** **2.2.3** Admiralty Code.

---

## 4. Related modules

- 2.2.1 – Estimative language (previous)
- 2.2.3 – Admiralty Code
- 2.2.4 – Cognitive biases
- 2.1.7 – Attribution
