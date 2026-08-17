# Module 3.2.3 – Admiralty Code

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.2.3 A / A / B · 3.2.3.1 1a / 1a / 2b  
- Hunter: 3.2.3 A / B / B · 3.2.3.1 1a / 2b / 3c  
- CTI: 3.2.3 B / C / C · 3.2.3.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Use the classroom **source reliability** scale (A–F).
2. Use the classroom **information credibility** scale (1–6).
3. **Combine** them into one code (letter + number).
4. **Assign** a code to a source and a report, and **explain** a given code.

**Mapped Proficiency Items:**
- K: 3.2.3 – Admiralty Code / source reliability and information credibility
- T: 3.2.3.1 – Assign Admiralty Code ratings and evaluate source reliability and credibility

---

## 1. Key Concepts

Admiralty Code rates the **source** and the **report** separately, then writes them together. It is not an estimative *likely* (**3.2.1**). It is not attribution *medium confidence* (**3.1.7**). It is not ACH (**3.2.2**).

**Classroom scales (this lesson only — not a live NATO card).** If your site prints different wording, use that card. The obligation is **letter + number, two axes**, not these glosses.

**Source reliability (outline a) — how much history do we have with *this reporter*?**

| Letter | Classroom meaning |
|--------|-------------------|
| **A** | Completely reliable — long, checked record; errors are rare |
| **B** | Usually reliable — known source, mostly right |
| **C** | Fairly reliable — mixed record |
| **D** | Not usually reliable — often wrong |
| **E** | Unreliable — a record of false reporting |
| **F** | Cannot be judged — new, anonymous, or no track record |

**Information credibility (outline b) — how well does *this claim* stand up?**

| Number | Classroom meaning |
|--------|-------------------|
| **1** | Confirmed by other **independent** sources |
| **2** | Probably true — consistent with other reporting, not independently confirmed |
| **3** | Possibly true — plausible, thin corroboration |
| **4** | Doubtful |
| **5** | Improbable |
| **6** | Cannot be judged — no way to test the claim yet |

**Combine (outline c):** `letter` + `number` → **B2**, **F6**, **A1**.  
Read it as two sentences: *This source is B. This report is 2.*

| Legal pair | Why it happens |
|------------|----------------|
| **F1** | Brand-new blog, but *this* IOC already sits in our Zeek **and** EDR independently |
| **B3** | Trusted sensor team; *this* claim is a single uncorroborated inference |
| **A1** | Rare. Do not award it because the slide looks official |

**F** and **6** are valid. “Cannot judge” is better than guessing **A** or **1**.

| This lesson | Other |
|-------------|-------|
| Source + report code | *Likely* / *even chance* — **3.2.1** |
| Not “medium confidence” on the cluster | **3.1.7** |
| Not which SAT to run | **3.2.2** |
| Not a bias name | **3.2.4** |

The tasks: **assign** a pair, and **explain** a pair you are given — not “recite A through 6.”

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Internal Zeek (known) + one uncorroborated SNI → **B3** | Vendor “APT” blog → **A1** |
| New paste + same hash already in two internal tools → **F1** | Treating **F6** as trash instead of “do not weight it” |
| Explaining **C3** as two axes | Using **B** as if it meant *likely* |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Known Sensor, Thin Claim (Expected)

**Source:** Harbor Zeek `span-1` (known, usually right).  
**Claim:** One `nightowl-updates.net` hit on WS-JLEE. No second sensor, no EDR yet.

**Assign:** Source **B**. Information **3** (possible; not independently confirmed). Code **B3**.  
**Explain:** Usually reliable sensor; *this* report is only possibly true until a second line exists.

### Example 2: Blog Flagged A1 (Lead)

**Source:** First-time vendor blog, “HIGH CONFIDENCE CHINA,” three IOCs.  
**Shipped rating:** **A1**.

**Reject.** Source has **no** local track record → **F** (or **C** only if the site already vets that vendor). The country claim is **not** independently confirmed → **5** or **6**, not **1**.  
**Better:** **F6** on the nation-state sentence. If an IOC later matches Zeek **and** EDR, *that IOC line* can become **F1**.  
**Lead:** Fancy PDF ≠ **A**. “Confirmed” ≠ “we liked the blog.”

### Example 3: F1 Is Legal (Lead)

**Source:** Anonymous paste, never seen before.  
**Claim:** Hash `6734f374…` is Night Owl.  
**Also true:** That hash already landed from WS-JLEE **EDR** and from a second host’s disk scan — two independent internals.

**Assign:** Source **F**. Information **1** (the *hash-on-those-hosts* fact is confirmed; the *Night Owl label* is a different claim — rate it separately, likely **F3**).  
**Lead:** Do not throw away **F** sources. Do not give the *label* a **1** just because the *hash* is confirmed.

---

## 3. Hands-On Exercise

**Objective:** Assign a code and explain a code.

**Use the classroom scales.**

**Instructions:**

1. One sentence each for Examples 1–3: letter, number, why.
2. **Assign** (task 1): source letter, info number, combined code, one reason each.

   - A. Duty SOC lead (accurate all quarter) reports WS-JLEE isolated; ticket + EDR both show the isolate.  
   - B. Brand-new Telegram channel posts “Night Owl = China.” Nothing internal matches.  
   - C. Commercial TIP (paid, mixed history on this vendor) says the JA3 is theirs; we have not looked internally yet.  
   - D. Same TIP **after** Zeek and EDR both show that JA3 on WS-JLEE.

3. **Explain** (task 2): in one sentence each, what the letter means and what the number means.

   - E. **C4**  
   - F. **F1**

4. Do not write *likely* as a substitute for the number. Do not run ACH. Do not name a 3.2.4 bias.
5. If two claims sit in one paragraph (hash vs country), **split** and rate each.

**Expected Outcome:**
- Three example summaries
- Four assign lines (A–D)
- Two explain lines (E–F)
- No estimative rewrite, no SAT

---

## 4. Knowledge Check

1. What does the **letter** rate, and what does the **number** rate?
2. When do you use **F** or **6** instead of guessing **A** or **1**?
3. Why can **F1** be a correct code?
4. Why is a vendor “APT” PDF not automatically **A1**?
5. How is **B2** different from *likely, medium confidence*?

---

## 5. Summary

- Letter = source. Number = this report. Write both.
- **F** and **6** are honest. **A1** is rare.
- Next: cognitive biases (**3.2.4**).

---

## 6. References & Further Reading

- Related modules:
  - 3.2.2 – Structured analytic techniques (previous)
  - 3.2.4 – Cognitive biases (next)
  - 3.2.1 – Estimative language
  - 3.1.7 – Attribution confidence
- Local source-evaluation / Admiralty card (optional — substitutes classroom A–F / 1–6 wording)
