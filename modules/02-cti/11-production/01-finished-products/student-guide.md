# Module 3.11.1 – Creating Finished Intelligence Products

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.11.1 A / A / B · 3.11.1.1 1a / 1a / 2b · 3.11.1.2 1a / 1a / 1a  
- Hunter: 3.11.1 A / B / B · 3.11.1.1 1a / 2b / 3c · 3.11.1.2 1a / 2b / 3c  
- CTI: 3.11.1 B / C / C · 3.11.1.1 3c / 4c / 4d · 3.11.1.2 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the **classroom finished-product types** and pick the right one.
2. Use the **required structure** and **quality standards**.
3. **Draft** a short product and **evaluate** a draft against those standards.
4. Produce a **threat actor profile** that stays inside the evidence (empty who is honest).

**Mapped Proficiency Items:**
- K: 3.11.1 – Creating finished intelligence products
- T: 3.11.1.1 – Draft a finished product and evaluate it against standards
- T: 3.11.1.2 – Produce a threat actor profile

---

## 1. Key Concepts

This hour is the **prose product**. Audience *rewrite* is **3.1.6**. Attribution *assessment* is **3.1.7**. A STIX bundle is **3.10**. Channels and markings are **3.11.2**. SOC incident/RFI *tickets* are **1.6.1**. Local approval is **3.12.2**.

**Types (outline a) — classroom set, not live org names:**

| Type | Use when | Not |
|------|----------|-----|
| **Activity note** | What we *saw* this window (Harbor excerpt) | A who-profile |
| **Assessment** | What we *judge* (estimative) plus gaps | A STIX bundle |
| **Actor profile** | A durable picture of an activity set / actor | Nation-state from a vendor PDF |
| **Defensive note** | What to block or hunt *now* | A 3.11.3 RFI answer sheet |

**Structure (outline b) — every finished draft this hour:**

`BLUF | facts | assessment (estimative) | evidence | gaps | recommended action`

**Quality (outline c) — fail the draft if any box is no:**

| Standard | Pass | Fail |
|----------|------|------|
| Fact vs assessment labeled | “We saw X. We assess Y.” | Vendor voice as fact |
| Supported IDs only | T1059.001 / T1547.001 / T1071.001 / T1105 | Uncited T1486 |
| Honest who | Unattributed / empty | “Nation-state Night Owl APT” |
| Estimative, not certainty | likely / even chance (**3.2.1**) | “will / is definitely” |
| Action or explicit none | Block domain / hunt SNI | “Be aware” with no owner |

**Actor profile (3.11.1.2) — classroom sections:**

| Section | Night Owl fill |
|---------|----------------|
| **Name / aliases** | Night Owl (vendor cluster). Not a nation-state. |
| **TTPs** | Only dual-pass IDs from **3.8.2** |
| **Infrastructure** | `nightowl-updates.net`, `login-nightowl.net`, `203.0.113.88` |
| **Victimology** | Harbor `jlee` / WS-JLEE observed; not “all finance” |
| **Confidence on who** | **Low / unattributed** (**3.1.7**) |
| **Gaps** | No who; no encrypt observed |

**Draft line:** `type | BLUF | one gap | one action`  
**Eval line:** `standard | pass/fail | why`  
**Profile line:** `section | fill or empty | why empty is honest`

| This lesson | Other |
|-------------|-------|
| Draft + eval + profile | Rewrite for one audience — **3.1.6** |
| Not markings/channel | **3.11.2** |
| Not STIX/TAXII | **3.10.2** |
| Not SOC ticket type | **1.6.1** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Activity note or assessment with empty who | Actor profile that names a nation-state |
| Eval fails T1486 / “will encrypt” | Shipping the vendor PDF as the product |

---

## 2. Detailed Walkthrough / Examples

**Shared facts:** WS-JLEE; `powershell -enc`; Run `Updater`; GET `update.exe` :8080 `nightowl-updates.net`; sibling `login-nightowl.net`; vendor T1486 and “APT” — not observed.

### Example 1: Activity Note (Expected)

**Type:** Activity note.  
**BLUF:** Harbor host WS-JLEE ran encoded PowerShell, persisted via HKCU Run, and retrieved `update.exe` from `nightowl-updates.net`. Who: unattributed.  
**Action:** Block the domain; hunt the sibling.  
**Not:** a profile, not T1486.

### Example 2: Failed Draft (Lead)

**Draft:** “Night Owl, a nation-state APT, will encrypt Harbor with T1486. High confidence.”

**Fail.** Unearned who, uncited T1486, banned certainty.  
**Lead:** Quality table — three boxes red.

### Example 3: Honest Profile (Expected for 3.11.1.2)

**Name:** Night Owl (cluster).  
**TTPs:** T1059.001, T1547.001, T1071.001, T1105.  
**Infra:** two names + `203.0.113.88`.  
**Who:** empty / low.  
**Gaps:** no encrypt; no actor identity.

---

## 3. Hands-On Exercise

**Objective:** Draft, evaluate, and fill an honest profile.

**Use only the shared facts and classroom types.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Draft** (3.11.1.1): one **draft line** — activity note *or* assessment — for the Harbor excerpt.
3. **Evaluate** (3.11.1.1): **eval lines** for the Example 2 draft (who, T1486, certainty).
4. **Profile** (3.11.1.2): **profile lines** for TTPs, infra, who, gaps.
5. Do not pick a TLP or channel (**3.11.2**). Do not write STIX (**3.10**). Do not invent IDs. Do not fill nation-state.

**Expected Outcome:**
- Three example summaries
- One draft line
- Three eval fails on Ex 2
- Four profile lines (who empty)
- No markings, no TAXII

---

## 4. Knowledge Check

1. Name **two** classroom finished-product types and when you would *not* use one of them.
2. What must a **draft line** include besides the BLUF?
3. Give **one** quality fail from Example 2.
4. What belongs in the **who** section of this Night Owl profile?
5. Where do you choose the **channel and marking**?

---

## 5. Summary

- Right type. Required structure. Quality table. Honest profile.
- Next: **3.11.2** Dissemination (audience, markings, channels).

---

## 6. References & Further Reading

- Related modules:
  - 3.10.2 – STIX production (previous unit)
  - 3.1.6 – Audience rewrite floor
  - 3.1.7 – Attribution
  - 3.11.2 – Dissemination (next)
- Classroom type and quality cards in this guide (lesson-only)
