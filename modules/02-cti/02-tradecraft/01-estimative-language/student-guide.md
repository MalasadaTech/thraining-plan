# Module 3.2.1 – Estimative Language

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.2.1 A / A / A · 3.2.1.1 1a / 1a / 1a  
- Hunter: 3.2.1 A / B / B · 3.2.1.1 1a / 2b / 3c  
- CTI: 3.2.1 B / C / C · 3.2.1.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain **why** estimative language exists.
2. Use the classroom **terms** and say what each one means.
3. Separate **likelihood** (how probable) from **confidence** (how good the evidence is — **3.1.7**).
4. **Write** a judgment with a legal term, and **interpret** a term in someone else’s sentence.

**Mapped Proficiency Items:**
- K: 3.2.1 – Estimative language
- T: 3.2.1.1 – Use and interpret estimative language in analytic judgments

---

## 1. Key Concepts

Estimative language tells the consumer **how likely** you assess something to be, and (with a confidence word) **how well supported** that call is. It is not Admiralty source letters (**3.2.3**). It is not “we believe” filler.

**Purpose (outline a):** Make uncertainty **comparable** across products. A reader should not have to guess whether “could be Night Owl” means *likely* or *remote*.

**Classroom terms (outline b — this lesson only, not a live ODNI card):**

| Term | Classroom meaning |
|------|-------------------|
| **Almost certainly** | Very high likelihood |
| **Highly likely** | High |
| **Likely** | Greater than even |
| **Even chance** | About as likely as not |
| **Unlikely** | Less than even |
| **Highly unlikely** | Low |
| **Remote** | Very low / almost certainly not |

If your site publishes a term card, use it. The obligation is **pick a term from the card and mean it**, not these labels. Do **not** invent percents as policy. If a number helps you *learn* the order, leave it in the classroom — do not put it in a product unless the site card says so.

**Not on the card (reject as the likelihood word):** will, is (for a judgment), might, could, may, possibly, we believe, suggests, appears.

**Two axes (outline c):**

| Axis | Question | Classroom words |
|------|----------|-----------------|
| **Likelihood** | How probable is the assessed thing? | The table above |
| **Confidence** | How good is the evidence? | **Low / medium / high** from **3.1.7** |

You can write: *We assess it is **likely** that WS-JLEE is Night Owl (**medium** confidence).*  
Those are **different** knobs. Thin evidence → lower **confidence**, not a fake “remote” if the pattern actually fits.

| This lesson | Other |
|-------------|-------|
| Likelihood terms | Attribution type / evidence — **3.1.7** |
| Not source A–F / 1–6 | **3.2.3** |
| Not ACH / key assumptions | **3.2.2** |

The tasks: **write** a judgment with a card term, and **interpret** someone else’s term (what it means; is confidence stated?).

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| “Likely … medium confidence” | “WS-JLEE **is** Night Owl” |
| Interpreting “highly unlikely” as low likelihood | Treating “could” as a card term |
| Likelihood and confidence both named | Using “high confidence” as if it were “highly likely” |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Legal Judgment (Expected)

**Facts:** WS-JLEE has the Night Owl SNI + JA3 + encoded-PS/Run path. One other lab host matches. Domain is not unique to them.

**Write:** We assess it is **likely** that WS-JLEE is Night Owl activity (**medium** confidence).  
**Interpret:** *Likely* = greater than even. *Medium* = evidence quality (**3.1.7**), not a second likelihood word.

### Example 2: “Is” / “Will” (Lead)

**Shipped:** “WS-JLEE **is** Night Owl. It **will** beacon again tonight.”

**Interpret:** No card term. *Is* / *will* claim certainty.  
**Rewrite:** We assess it is **highly likely** that WS-JLEE is Night Owl (**medium** confidence). We assess it is **even chance** it beacons again tonight (**low** confidence — we have one night of data).  
**Lead:** Two judgments, two terms. Do not smuggle certainty.

### Example 3: “Could” and Mixed Axes (Lead)

**Shipped:** “This **could** be China. High confidence.”

**Interpret:** *Could* is **not** on the card. *High confidence* is the **3.1.7** axis — and **3.1.7** already failed this as an over-claim.  
**Rewrite (activity group only):** We assess it is **unlikely** this is a nation-state operation on present evidence (**low** confidence). We assess it is **likely** a Night Owl **cluster** (**medium** confidence).  
**Lead:** Wrong type plus a banned word plus a swapped axis.

---

## 3. Hands-On Exercise

**Objective:** Write with a card term and interpret someone else’s sentence.

**Use the classroom table.** Night Owl facts as in Example 1 unless stated.

**Instructions:**

1. One sentence each for Examples 1–3: legal term vs banned word.
2. **Write** (task 1): one judgment for each.

   - A. WS-JLEE is / is not Night Owl (cluster).
   - B. Whether Night Owl will keep using weak TLS against finance-adjacent hosts **this quarter**.

3. **Interpret** (task 2): for each sentence, name the **term**, its **meaning**, and whether **confidence** is stated.

   - C. “We assess it is **highly unlikely** the guest-laptop SNI hit is Night Owl (low confidence).”
   - D. “SOC should isolate WS-JLEE; it **might** be Night Owl.”
   - E. “**Almost certainly** Night Owl — **high** confidence.” (SNI only, shared CDN.)
   - F. “Even chance the extra TLS sensor would have seen the next beacon.”

4. Do not assign Admiralty letters. Do not run ACH (**3.2.2**). Do not change the **3.1.7** type (cluster vs country) except to refuse a country claim the way Example 3 does.
5. If E over-claims, say the *language* is legal but the **confidence** and maybe the **term** are too strong for the evidence.

**Expected Outcome:**
- Three example summaries
- Two written judgments (A–B)
- Four interpret lines (C–F)
- No Admiralty, no SAT

---

## 4. Knowledge Check

1. What problem does estimative language **prevent**?
2. Name three **card** terms and one **banned** word.
3. How is **likely** different from **medium confidence**?
4. Why is “WS-JLEE **is** Night Owl” not estimative language?
5. Where are **source reliability letters** taught?

---

## 5. Summary

- Card term = likelihood. Low/medium/high = confidence (**3.1.7**).
- Write it. Interpret it. Reject *is* / *will* / *could*.
- Next: structured analytic techniques (**3.2.2**).

---

## 6. References & Further Reading

- Related modules:
  - 3.1.7 – Attribution (previous cluster; confidence axis)
  - 3.2.2 – Structured analytic techniques (next)
  - 3.2.3 – Admiralty Code
- Local estimative-language card (optional — substitutes classroom terms)
