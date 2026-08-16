# Module 3.2.2 – Structured Analytic Techniques

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.2.2 A / A / A · 3.2.2.1 1a / 1a / 2b  
- Hunter: 3.2.2 A / B / B · 3.2.2.1 1a / 2b / 3c  
- CTI: 3.2.2 B / C / C · 3.2.2.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain **why** structured analytic techniques exist.
2. Describe classroom **ACH** and **Key Assumptions Check**.
3. **Choose** which of those two fits a scenario.
4. **Apply** one of them to a small problem set.

**Mapped Proficiency Items:**
- K: 3.2.2 – Structured analytic techniques
- T: 3.2.2.1 – Apply a structured analytic technique and select the right one for a scenario

---

## 1. Key Concepts

A structured analytic technique (SAT) makes the thinking **visible** so you do not lock onto the first story. Estimative *words* (**3.2.1**) go on the *output*. This hour is the **method** before that sentence. Admiralty letters are **3.2.3**. The bias catalog is **3.2.4**.

**Purpose (outline a):** Slow the jump to one explanation. Show which evidence would **hurt** a favorite story. Surface “must be true” claims before you ship.

**Classroom pair (outline b — this lesson only).** Other techniques exist (devil’s advocate, quality of information). They are **not** sign-off here. Overlay a site SAT list if you have one.

| Technique | What you do | Output |
|-----------|-------------|--------|
| **Key Assumptions Check (KAC)** | List the claims the judgment *needs* to be true. For each: what if it is false? | Assumption table |
| **Analysis of Competing Hypotheses (ACH)** | Name 2+ explanations. Score each evidence item **C** (consistent), **I** (inconsistent), or **N** (neutral). Prefer the story with the **fewest I**. | Mini matrix |

**When (outline c):**

| Situation | First SAT |
|-----------|-----------|
| One story already written; the “must be trues” are hidden | **KAC** |
| Two or more live explanations and evidence that can discriminate | **ACH** |
| Only one possible story and no evidence yet | **Neither** — collect (**3.1.8**). Do not fake a matrix |

ACH does **not** start with “which hyp do I like?” It starts with **which evidence kills a hyp**.

**Classroom ACH marks:** C = this item can live with that hyp. I = this item is hard to square with that hyp. N = it does not help either way. You do **not** add a popularity score.

| This lesson | Other |
|-------------|-------|
| Choose + apply KAC or ACH | Likelihood wording — **3.2.1** |
| Not source A–F / 1–6 | **3.2.3** |
| Not the bias *names* | **3.2.4** (KAC can *expose* an assumption; the catalog is later) |
| Not cluster vs country | **3.1.7** |

The tasks: **pick** the SAT, then **fill** a small KAC table or ACH matrix — not “SAT is good.”

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Two host stories + mixed evidence → **ACH** | Running ACH on a single locked story |
| “It’s Night Owl” with unstated must-bes → **KAC** | Picking ACH because it looks more serious |
| No second hyp, no evidence → collect first | A 12-column matrix in this hour |

---

## 2. Detailed Walkthrough / Examples

**Shared Night Owl facts (use these unless stated):**  
E1 SNI `nightowl-updates.net` on WS-JLEE.  
E2 Same JA3 as last week’s lab host.  
E3 Encoded PS + HKCU Run on WS-JLEE.  
E4 Helpdesk scanner `10.10.8.90` ran the same hour (known FP class — **1.4.3**).  
E5 Domain also appears on a public CDN test list.

### Example 1: ACH Fits (Expected)

**Question:** What is WS-JLEE?  
**Hyps:** H1 Night Owl cluster. H2 scanner/tool FP. H3 unrelated commodity malware.

| Evidence | H1 Night Owl | H2 scanner FP | H3 commodity |
|----------|--------------|---------------|--------------|
| E1 SNI | C | I (scanner does not need that SNI) | N |
| E2 JA3 match | C | I | N |
| E3 PS + Run | C | I | C |
| E4 scanner same hour | N | C | N |
| E5 shared CDN | N | N | N |

**Read:** H2 has the most **I**. H1 has none. H3 is possible but weaker on E1/E2.  
**Then** you may write a **3.2.1** sentence (*likely* H1, *medium* confidence). That sentence is not this lesson’s SAT.

### Example 2: KAC First (Lead)

**Shipped judgment:** “WS-JLEE **is** Night Owl. Isolate.”

**Hidden assumptions (KAC):**  
A1 The SNI is unique to Night Owl.  
A2 The lab JA3 is the same *actor*, not a shared library.  
A3 The scanner hour is coincidence.

If A1 is false (E5), the isolate call is too strong. **KAC** is the right SAT — there are not two *worked* competing hyps yet, just a locked story.  
**Lead:** Do not open a full ACH to look busy. Name the must-bes.

### Example 3: Wrong Tool (Lead)

**Situation:** Leadership asks whether to *fund* extra TLS this quarter. One draft: “Night Owl exists; fund it.” No alternate budget story, no evidence list.

**Correct pick:** **Neither** until there is a requirement-shaped question (**3.1.4**) and at least two explanations *or* a judgment with hidden must-bes. If they already wrote “fund it because Night Owl always uses weak TLS,” that is a **KAC** (A: Night Owl will keep using weak TLS).  
**Reject:** A fake three-hyp ACH with no evidence rows.  
**Lead:** SAT follows the *problem*, not the prestige of the acronym.

---

## 3. Hands-On Exercise

**Objective:** Pick the SAT, then apply one.

**Use the shared facts and the classroom pair only.**

**Instructions:**

1. One sentence each for Examples 1–3: which SAT and why.
2. **Select** (task 2): which SAT (KAC / ACH / neither)? One reason.

   - A. Two live hyps: Night Owl cluster vs scanner FP. Evidence E1–E5 in hand.
   - B. Draft already says “highly likely nation-state.” No competing hyp written.
   - C. Brand-new SNI, no other evidence, no second story.
   - D. Hunt lead: “We always assume east-west Zeek sees OT.” (Coverage assumption.)

3. **Apply** (task 1):  
   - If you picked **ACH** for A, fill a 2-hyp × E1–E5 mini matrix (C / I / N) and say which hyp has fewer **I**.  
   - If you picked **KAC** for B or D, list **three** assumptions and one “if false, then…” each.

4. Do not write Admiralty letters. Do not name a 3.2.4 bias. Do not spend the hour on the *likely* wording (you may add one legal term after the SAT — optional).
5. Two hyps is enough. Do not build a twelve-column ACH.

**Expected Outcome:**
- Three example summaries
- Four select lines
- One filled ACH **or** one three-row KAC
- No Admiralty, no bias catalog

---

## 4. Knowledge Check

1. What problem does a SAT **prevent**?
2. What does an **I** mean on the classroom ACH, and how do you read the matrix?
3. When is **KAC** the first technique, not ACH?
4. When is the answer **neither**?
5. Where is the **bias catalog** taught?

---

## 5. Summary

- Purpose: make thinking visible. Classroom pair: KAC and ACH.
- Pick for the problem. Apply a small table. Fewest **I** wins ACH.
- Next: Admiralty Code (**3.2.3**).

---

## 6. References & Further Reading

- Related modules:
  - 3.2.1 – Estimative language (previous)
  - 3.2.3 – Admiralty Code (next)
  - 3.2.4 – Cognitive biases
  - 3.1.7 – Attribution
- Local SAT / tradecraft card (optional — may add named techniques; this lesson’s sign-off is still KAC + ACH)
