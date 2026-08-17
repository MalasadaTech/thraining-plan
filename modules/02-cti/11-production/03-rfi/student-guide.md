# Module 3.11.3 – Handling RFIs

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.11.3 A / A / A · 3.11.3.1 1a / 1a / 1a  
- Hunter: 3.11.3 A / A / B · 3.11.3.1 1a / 1a / 2b  
- CTI: 3.11.3 B / C / C · 3.11.3.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. State the **purpose** of an intelligence RFI and its **lifecycle**.
2. **Evaluate** whether you can answer it and **prioritize** it.
3. **Produce** a short response — or decline/redirect.
4. **Reject** out-of-scope, duplicate, or “write me a profile” requests that belong elsewhere.

**Mapped Proficiency Items:**
- K: 3.11.3 – Handling RFIs
- T: 3.11.3.1 – Evaluate, prioritize, and produce a response to an RFI

---

## 1. Key Concepts

An intelligence **RFI** is a **customer question** that needs an intel answer. SOC **1.6.1** RFI is a *ticket type* (“I need info from another team”). This hour you **receive, prioritize, and answer** as CTI. Finished products are **3.11.1**. Dissemination is **3.11.2**. Local PIRs are **3.12.1**. A collection *request* is **3.12.2**.

**Purpose and lifecycle (outline a):**

| Stage | You do |
|-------|--------|
| **Receive** | Log the question, asker, deadline |
| **Evaluate** | In scope? Answerable from holdings? Need collection? |
| **Prioritize** | Decision + time vs other RFIs |
| **Respond** | Short answer, or decline / redirect |

**Evaluate and prioritize (outline b):**

| Ask | High | Low / decline |
|-----|------|----------------|
| Can Harbor **act** this window? | SOC “what do we block tonight?” | “Nice to know” with no owner |
| Do we **already** have the answer? | Holdings from 3.8 / 3.11.1 | Needs new collection (**3.12.2**) — say so |
| In **scope** for CTI? | Attribution confidence, infra, TTPs | Write an exploit; HR question |
| Already **answered**? | Point at the last note | Rewrite the same bulletin |

**Classroom RFI queue (this lesson only):**

| ID | Asker | Question | Evaluate |
|----|-------|----------|----------|
| **R1** | SOC | What do we block *tonight* for Night Owl? | In scope, holdings exist, **high** |
| **R2** | Leadership | Is Night Owl a nation-state? | In scope, holdings say **unattributed** — answer that; do not invent a who |
| **R3** | Analyst | “Write a working exploit for update.exe.” | **Out of scope** — decline |
| **R4** | Hunt | “Same as last activity note — anything new?” | **Duplicate** — point at 3.11.1 note |

**RFI line:** `id | in scope? | priority | respond or decline | one-sentence answer or redirect`

**Response (R1 classroom):** “Block `nightowl-updates.net` and `login-nightowl.net` at `fw-edge-01`. Hunt WS-JLEE-like hosts. Who remains unattributed.”  
**Response (R2 classroom):** “We assess **who** as unattributed / low confidence. Do not treat the vendor APT label as a nation-state. See the 3.11.1 profile gaps.”

| This lesson | Other |
|-------------|-------|
| Answer or decline the question | SOC ticket *type* RFI — **1.6.1** |
| Not a new finished product unless needed | **3.11.1** |
| Not the send/marking hour | **3.11.2** |
| Not local PIR list | **3.12.1** |
| Need new collection | **3.12.2** — say so, do not fake holdings |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| R1 high + concrete CoA | R2 answered as “yes, nation-state” |
| R3 decline | Writing the exploit |
| R4 point at last note | New 6-page product for a duplicate |

---

## 2. Detailed Walkthrough / Examples

### Example 1: SOC Block-Tonight (Expected)

**R1.** In scope. Holdings exist. **High.**  
**Response:** the classroom CoA sentence.  
**Not:** a new actor profile.

### Example 2: Nation-State RFI (Lead if over-answered)

**R2.** In scope. Answer **unattributed**.  
**Fail draft:** “Yes — nation-state APT.”  
**Lead:** The RFI does not create evidence. Same honest who as **3.11.1.2**.

### Example 3: Out of Scope / Duplicate (Expected decline)

**R3:** decline — not a CTI product.  
**R4:** redirect to the existing activity note — do not rewrite it as a new product.

---

## 3. Hands-On Exercise

**Objective:** Evaluate, prioritize, respond or decline.

**Use only the classroom queue.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Evaluate / prioritize** (task 1): **RFI lines** for R1–R4.
3. **Respond** (task 2): one-sentence answers for R1 and R2; decline/redirect text for R3 and R4.
4. Do not write a full **3.11.1** product unless you *must* — R1 and R2 are short answers. Do not invent collection. Do not mark/send (**3.11.2**).
5. If holdings are missing, say **3.12.2** — do not fabricate.

**Expected Outcome:**
- Three example summaries
- Four RFI lines
- Two short answers + two declines/redirects
- No exploit, no fake nation-state, no duplicate product

---

## 4. Knowledge Check

1. What is an intelligence **RFI** *for*?
2. Name the **lifecycle** stages.
3. Why is R1 **higher** priority than R4?
4. How do you answer R2 without filling **who**?
5. Where do you go if you **need collection** you do not have?

---

## 5. Summary

- Evaluate. Prioritize. Answer or decline. Do not invent holdings or a who.
- This closes unit **3.11**. Next: **3.12** Site-Specific CTI.

---

## 6. References & Further Reading

- Related modules:
  - 3.11.2 – Dissemination (previous)
  - 1.6.1 – SOC RFI as a ticket type
  - 3.11.1 – Finished products
  - 3.12.1 – Local PIRs (next unit)
  - 3.12.2 – Collection / approval request
- Classroom RFI queue in this guide (lesson-only)
