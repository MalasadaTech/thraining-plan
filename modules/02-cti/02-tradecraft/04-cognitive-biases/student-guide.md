# Module 3.2.4 – Cognitive Biases and Mitigation

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.2.4 A / A / A · 3.2.4.1 1a / 1a / 1a  
- Hunter: 3.2.4 A / B / B · 3.2.4.1 1a / 2b / 3c  
- CTI: 3.2.4 B / C / C · 3.2.4.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the classroom **common biases** and how they warp a product.
2. **Identify** a likely bias in a written judgment (and what in the text shows it).
3. **Apply** a mitigation — a concrete next step, not “be more objective.”

**Mapped Proficiency Items:**
- K: 3.2.4 – Cognitive biases and mitigation
- T: 3.2.4.1 – Identify cognitive bias in a judgment and apply a mitigation technique

---

## 1. Key Concepts

A bias is a **predictable tilt** in how people handle evidence. It is not an Admiralty letter (**3.2.3**) and not a *likely* word (**3.2.1**). ACH and KAC (**3.2.2**) are **tools** you can use to mitigate — this hour is *spot the tilt, then do something*.

**Classroom set (outline a — this lesson only).** Other named biases exist. They are **not** sign-off here. Overlay a site list if you have one.

| Bias | What it looks like in a product |
|------|--------------------------------|
| **Confirmation** | Only the evidence that fits the favorite story is cited; disconfirming rows are missing |
| **Anchoring** | The first number, blog, or country name never gets revisited |
| **Availability** | Last week’s vivid case drives this week’s call (“last encoded-PS was ransomware, so this is too”) |
| **Premature closure** | The story is locked (*is*, isolate, A1) before a second line of evidence |

**Impact (outline b):** over-confident wording, skipped alternatives, vanity **A1**, Night Owl on every SNI, a country claim that is really an anchor from a vendor title.

**Mitigations (outline c) — each one is an action:**

| Bias | Classroom mitigation |
|------|----------------------|
| Confirmation | Run a small **ACH** and *require* at least one **I** hunt (what evidence would hurt H1?) |
| Anchoring | Write the judgment **without** the first source’s label; then see if the internals still support it |
| Availability | State the **base rate** / last similar cases (how often is encoded-PS actually Night Owl *here*?) |
| Premature closure | **KAC** three must-bes; do not ship *is* / isolate until one assumption is tested |

“Be aware of bias” is **not** a mitigation.

| This lesson | Other |
|-------------|-------|
| Name the tilt + do the mitigation | How to fill ACH/KAC tables — **3.2.2** |
| Not *likely* vs *medium* | **3.2.1** / **3.1.7** |
| Not A–F / 1–6 | **3.2.3** |

The tasks: **identify** (which bias + textual tell) and **apply** (named mitigation + what you will actually do).

`bias | tell in the text | mitigation | next action`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Confirmation — only SNI cited, scanner hour omitted → ACH / hunt I | “Humans are biased” with no name |
| Anchoring — every sentence still says China from blog #1 → rewrite without the flag | Reciting eight extra bias names |
| Premature closure — isolate before a second line → KAC | Re-teaching the full ACH matrix |

---

## 2. Detailed Walkthrough / Examples

**Shared facts:** E1 SNI on WS-JLEE. E2 JA3 match. E3 PS+Run. E4 scanner `10.10.8.90` same hour. E5 domain on a CDN test list.

### Example 1: Confirmation (Expected)

**Judgment shipped:** “WS-JLEE is Night Owl. Evidence: SNI `nightowl-updates.net`.” (E4 and E5 omitted.)

**Identify:** **Confirmation** — only the fitting row is shown.  
**Mitigate:** ACH H1 Night Owl vs H2 scanner/CDN; force E4 and E5 onto the matrix and mark **I** / **N**. Then rewrite with a **3.2.1** term if it still stands.  
**Apply:** Add the two omitted rows *today* before the isolate sentence.

### Example 2: Anchoring (Lead)

**Day 1 blog:** “HIGH CONFIDENCE CHINA.”  
**Day 3 product:** Still opens with China. Internals only support a **cluster**. No new nation-state evidence.

**Identify:** **Anchoring** (the first label never moved). Also a **3.1.7** type over-claim — here you name the *bias*.  
**Mitigate:** Rewrite the draft with the blog title **removed**. If internals only support Night Owl *cluster*, the country sentence dies.  
**Lead:** Do not spend the hour rating the blog **F6** (**3.2.3**) unless you also name the tilt.

### Example 3: Availability + Closure (Lead)

**Judgment:** “Last Thursday’s encoded-PS was ransomware. Isolate WS-JLEE as ransomware. High confidence.”

**Identify:** **Availability** (vivid last case) and **premature closure** (isolate + high, no second family line).  
**Mitigate:** Base rate: how many encoded-PS on Harbor last 90 days were ransomware vs Night Owl vs FP? KAC the “encoded-PS ⇒ ransomware” must-be.  
**Lead:** Two biases can sit in one sentence. Name the strongest tell; mitigate that first.

---

## 3. Hands-On Exercise

**Objective:** Identify the bias and apply a mitigation.

**Use the classroom four only.**

**Instructions:**

1. One sentence each for Examples 1–3: bias + mitigation.
2. **Identify** (task 1): `bias | tell`.

   - A. Product cites E1–E3 only and concludes Night Owl. E4–E5 are in the case file, unused.  
   - B. First slide last month said “APT-12.” Every update still leads with APT-12; no new attribution evidence.  
   - C. “Guest laptop SNI once — isolate, almost certainly Night Owl.”  
   - D. “We always assume Zeek sees OT, so no Night Owl in OT.” (**1.8.1** — there is no OT span.)

3. **Apply** (task 2): for **A** and **C**, write the **mitigation + next action** (one concrete step each).
4. Do not fill a twelve-column ACH. Do not assign Admiralty. Do not invent a fifth classroom bias unless the instructor overlays a site name — then map it onto these four.
5. If two biases fit, pick the one the *text* shows most clearly.

**Expected Outcome:**
- Three example summaries
- Four identify lines
- Two mitigation actions (A and C)
- No Admiralty table, no extra bias catalog

---

## 4. Knowledge Check

1. Name the four **classroom** biases and one **impact** on a product.
2. Why is “be aware of bias” not a mitigation?
3. Which mitigation fits **confirmation**, and what do you actually do?
4. How is this different from **3.2.2** (running ACH/KAC)?
5. What cluster does this lesson **close**?

---

## 5. Summary

- Four classroom biases. Impact is in the *product*.
- Identify the tell. Mitigate with a step.
- Cluster **3.2** ends. Next cluster: **3.3** Tools.

---

## 6. References & Further Reading

- Related modules:
  - 3.2.3 – Admiralty Code (previous)
  - 3.2.2 – Structured analytic techniques (tools you may use to mitigate)
  - 3.3.1 – Internal TIP (next cluster)
- Local bias / tradecraft card (optional — may add names; this lesson’s sign-off is still the four + a concrete mitigation)
