# Module 3.11.2 – Disseminating Intelligence to the Correct Audiences

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.11.2 A / A / B · 3.11.2.1 1a / 1a / 2b · 3.11.2.2 1a / 1a / 2b · 3.11.2.3 1a / 1a / 2b  
- Hunter: 3.11.2 A / B / B · 3.11.2.1 1a / 2b / 3c · 3.11.2.2 1a / 2b / 3c · 3.11.2.3 1a / 2b / 3c  
- CTI: 3.11.2 B / C / C · 3.11.2.1 3c / 4c / 4c · 3.11.2.2 3c / 4c / 4d · 3.11.2.3 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. **Identify** the audience for a finished product.
2. Pick an **approved method** and apply a **classroom handling marking**.
3. **Tailor** the same facts for technical vs leadership audiences.
4. **Disseminate** on an approved channel — and reject Slack / public post.

**Mapped Proficiency Items:**
- K: 3.11.2 – Disseminating intelligence to the correct audiences
- T: 3.11.2.1 – Select audience and method and apply correct handling markings
- T: 3.11.2.2 – Tailor products to different audiences
- T: 3.11.2.3 – Disseminate intelligence products through approved channels

---

## 1. Key Concepts

**3.11.1** wrote the product. **3.1.6** taught the rewrite. This hour **sends** it: audience + method + marking + channel. SOC ticket routing is **1.6.3**. Local customer lists are **3.12.3**. TAXII publish is **3.10.2**.

**Classroom cards (this lesson only, not live org policy).** If your site posts a real marking/channel card, use it. Keep: audience + method + marking + approved channel.

**Audience (outline a):**

| Audience | Decision they own |
|----------|-------------------|
| **SOC / IR** | Isolate, ticket, block now |
| **Hunt** | Scope the next look |
| **Leadership** | Fund, accept risk, notify |
| **Partner** | Only what the marking allows |

**Methods and channels (outline b) — classroom approved set:**

| Approved | Use | Reject |
|----------|-----|--------|
| **TIP** | Lasting record, tagged to the indicator | Personal notes app |
| **Intel DL** (internal mail) | Named consumers on the card | Personal Gmail |
| **SOC ticket** | Action on a host tonight | “I’ll Slack jlee’s boss” |
| **Leadership brief slot** | Decision in 5 minutes | Public blog / X |

**Markings (outline c) — classroom TLP 2.0 (real standard, lesson application):**

| Marking | Classroom meaning |
|---------|-------------------|
| **TLP:CLEAR** | May go widely inside Harbor |
| **TLP:GREEN** | Harbor community; not public |
| **TLP:AMBER** | Need-to-know; SOC/hunt/leadership on the card |
| **TLP:RED** | Named recipients only |

Harbor Night Owl *activity note* this hour: **TLP:AMBER** (host names, live infra). A public blog post is always wrong.

**Tailor (3.11.2.2):** same **3.1.6** rewrite line, then attach marking + channel.

`audience | keep | cut | format | marking | channel`

**Disseminate line (3.11.2.3):**  
`product | audience | channel | marking | not this channel`

| This lesson | Other |
|-------------|-------|
| Send the product | Draft the product — **3.11.1** |
| Rewrite + channel | Rewrite only — **3.1.6** |
| Not SOC routing matrix | **1.6.3** |
| Not local customer list | **3.12.3** |
| Not TAXII collection | **3.10.2** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| AMBER + TIP + SOC ticket | TLP:CLEAR to the whole company with host names |
| Leadership brief without hashes | Slack the CEO the JA3 |
| Two tailored versions, one send each | One blob to everyone |

---

## 2. Detailed Walkthrough / Examples

**Product:** Night Owl activity note from **3.11.1** (WS-JLEE, domain, unattributed).

### Example 1: SOC Send (Expected)

**Audience:** SOC/IR. **Keep:** host, domain, action. **Cut:** actor-history essay.  
**Marking:** TLP:AMBER. **Channel:** SOC ticket + TIP.  
**Not:** Slack.

### Example 2: CLEAR + Public (Lead)

**Draft:** Mark TLP:CLEAR and post the note (with WS-JLEE) on the intranet homepage.

**Fail.** Live host + live infra is not CLEAR. Homepage is not an approved channel on the card.  
**Lead:** Marking and channel both fail.

### Example 3: Two Audiences (Expected for 3.11.2.2)

**SOC ticket:** Isolate WS-JLEE; block `nightowl-updates.net`. TLP:AMBER.  
**Leadership brief:** We assess further invoice-lure activity against Harbor users is **likely** this week; accept residual risk or fund the extra TLS sensor. No hashes. TLP:AMBER. Leadership brief slot.

Same facts. Two products. Two sends.

---

## 3. Hands-On Exercise

**Objective:** Tailor, mark, and send. Reject CLEAR/public and personal Slack.

**Use the classroom TLP and channel cards.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Select + mark** (3.11.2.1): **disseminate lines** for A–C.

   - A. SOC must isolate WS-JLEE tonight.  
   - B. Leadership needs a 5-minute decision on the TLS sensor.  
   - C. “Post it publicly so partners see.”

3. **Tailor** (3.11.2.2): rewrite lines for A and B (`keep | cut | format`).
4. **Send** (3.11.2.3): name the approved channel for A and B; reject C.
5. Do not redraft the whole **3.11.1** profile. Do not invent a classification system. Do not use TAXII as the *only* answer for a leadership brief.

**Expected Outcome:**
- Three example summaries
- Three disseminate lines (C fail)
- Two tailor lines
- Two approved sends
- No Slack, no CLEAR host dump

---

## 4. Knowledge Check

1. What three things must you pick before you **send**?
2. Why is the Night Owl activity note **not** TLP:CLEAR?
3. Give one **approved** channel and one **rejected** channel from the classroom card.
4. How does this hour **add** to **3.1.6**?
5. Where is the **local** customer list?

---

## 5. Summary

- Audience. Marking. Approved channel. Tailor, then send.
- Next: **3.11.3** Handling RFIs.

---

## 6. References & Further Reading

- Related modules:
  - 3.11.1 – Finished products (previous)
  - 3.1.6 – Audience rewrite floor
  - 1.6.3 – SOC notification routing
  - 3.11.3 – RFIs (next)
  - 3.12.3 – Local customers
- Classroom TLP and channel cards (lesson-only)
- TLP 2.0 (lookup — application is classroom)
