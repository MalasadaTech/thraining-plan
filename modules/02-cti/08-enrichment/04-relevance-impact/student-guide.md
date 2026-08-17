# Module 3.8.4 – Threat Relevance and Organizational Impact

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.8.4 A / B / B · 3.8.4.1 1a / 2b / 3c  
- Hunter: 3.8.4 B / C / C · 3.8.4.1 2b / 3c / 4c  
- CTI: 3.8.4 B / C / C · 3.8.4.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Judge **relevance**: does this finding apply to *this* environment (mission / assets / platform)?
2. State **potential impact** if the finding is true — what would change here.
3. **Reject** impact that skips the path, a PIR you invented, and an attribution letter.

**Mapped Proficiency Items:**
- K: 3.8.4 – Threat relevance and organizational impact
- T: 3.8.4.1 – Assess threat relevance and potential impact to the organization

---

## 1. Key Concepts

**3.8.2** asked whether a TTP *can run here* (platform + path). This hour asks the next question: **so what, here?** Interesting ≠ relevant. Relevant ≠ “pay-db-01 is down.”

Do not rewrite the TTP apply list. Do not handle IOCs (**3.8.3**). Do not write a PIR (**3.1.4** / **3.12.1**). Do not assign a 3.1.7 confidence letter. Do not write a **3.11** profile.

**Relevance (outline a):** use Harbor facts you already have (**1.8.1**, lesson-only). If the instructor overlays a real site card, use *that*.

| Harbor stand-in | What it means for “here” |
|-----------------|--------------------------|
| User endpoints are **Windows** (`WS-JLEE`) | A Windows Run-key + encoded PowerShell finding can be relevant |
| Crown jewel **`pay-db-01`** | Impact on payroll is a *separate* claim — you need a path |
| Users do **not** initiate to OT | An OT-only finding is not relevant on this card |
| No ESXi / no Unix user fleet | ESXi encrypt / Unix shell stays **not relevant** (3.8.2 already dropped the TTP) |

**Impact (outline b):** if the relevant finding is **true**, what changes? Stay on the evidence. User-endpoint persistence + HTTP C2 is impact on **that user estate**. It is not automatically “payroll is encrypted.”

**Not this hour (outline c):**

| Tempting fill | Why it fails |
|---------------|--------------|
| A PIR you wrote | **3.1.4** / **3.12.1** |
| “Nation-state, high confidence” | **3.1.7** |
| Re-listing T1059.001 as the product | **3.8.2** |

**Impact line:**  
`finding | relevant here? (Harbor fact) | impact if true | not because`

**In the product:** “Night Owl on WS-JLEE is relevant to Harbor Windows users. If true: persistent user-endpoint access and HTTP egress C2. Not shown: a path to `pay-db-01`.”

| This lesson | Other |
|-------------|-------|
| So what *here* | TTP apply — **3.8.2** |
| Not IOC file | **3.8.3** |
| Not write / obtain PIRs | **3.1.4** / **3.12.1** |
| Not attribution | **3.1.7** |
| Harbor facts | **1.8.1** (stand-in) |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Relevant to Windows users; impact = that estate | “pay-db-01 is compromised” with no path |
| ESXi finding = not relevant | “Nation-state PIR-1” as the impact line |
| Name what is *not* shown | Whole-org outage from one workstation |

---

## 2. Detailed Walkthrough / Examples

**Finding on the desk (already handled):** WS-JLEE — `powershell -enc`, HKCU Run `Updater`, GET `update.exe` to `nightowl-updates.net`. Vendor PDF also waves at ESXi T1486.

### Example 1: User-Estate Impact (Expected)

**Impact line:** `Night Owl on WS-JLEE | relevant — Harbor Windows users (1.8.1) | if true: persistent user access + HTTP C2 from that estate | not shown: path to pay-db-01 or OT`

**Not:** a TTP list. **Not:** a PIR.

### Example 2: Skipped Path (Lead)

**Draft:** “Relevant to payroll. Impact: `pay-db-01` is down / data stolen.”

**Fail.** Crown jewel is on the Harbor card. A path from WS-JLEE to `pay-db-01` is **not**.  
**Lead:** Name the jewel only if the finding reaches it. Otherwise say **not shown**.

### Example 3: PIR / Attribution Swap (Lead)

**Draft A:** “Harbor PIR-1 nation-state finance — this is it.”  
**Draft B:** “Nation-state, high confidence.”

**Fail.** You wrote a requirement (**3.12.1**) or an attribution letter (**3.1.7**).  
**Lead:** Relevance and impact are not those products.

---

## 3. Hands-On Exercise

**Objective:** Write impact lines. Reject skipped-path and PIR/attribution swaps.

**Use the Harbor stand-in and the Night Owl finding above.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Assess** (task): write an **impact line** for each.

   - A. Night Owl on WS-JLEE (Windows user).  
   - B. Vendor ESXi T1486 (no ESXi on the card).  
   - C. Same Night Owl finding, impact = `pay-db-01` outage.  
   - D. “Write PIR-1 so we can say it is in focus.”  
   - E. “Nation-state, high confidence.”

3. Ship **A** as the product. B = not relevant. C–E fail.
4. Do not re-list TTPs (**3.8.2**). Do not handle IOCs (**3.8.3**). Do not invent a PIR.
5. If the instructor overlays a real site card, relevance uses *that* card — still no invented PIR.

**Expected Outcome:**
- Three example summaries
- Five impact lines (B not relevant; C–E fail)
- One product sentence (A)
- No PIR, no attribution letter

---

## 4. Knowledge Check

1. What is **relevance** this hour, versus **3.8.2** applicability?
2. What belongs on an **impact line**?
3. Why is “`pay-db-01` is down” not the impact of WS-JLEE alone?
4. Why is a **PIR** not the product?
5. Where do you **obtain** the real local priority list?

---

## 5. Summary

- Relevant to *this* estate. Impact stays on the evidence. Path not shown stays “not shown.”
- 3.8 enrichment block ends here.

---

## 6. References & Further Reading

- Related modules:
  - 3.8.2 – Applicable TTPs
  - 3.8.3 – IOC handling (previous)
  - 1.8.1 – Harbor orientation stand-in
  - 3.12.1 – Obtain local PIRs
  - 3.1.7 – Attribution
- Classroom Harbor card / Night Owl finding (lesson-only)
