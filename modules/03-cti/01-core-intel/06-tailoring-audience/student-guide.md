# Module 3.1.6 – Tailoring Output to the Audience

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.1.6 A / A / B · 3.1.6.1 1a / 1a / 2b  
- Hunter: 3.1.6 A / B / B · 3.1.6.1 1a / 2b / 3c  
- CTI: 3.1.6 B / C / C · 3.1.6.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Analyze **who** the consumer is and what decision they own.
2. Adjust **content, format, and detail** for that consumer.
3. **Rewrite** a product for a specified audience (not just say “it depends”).

**Mapped Proficiency Items:**
- K: 3.1.6 – Tailoring output to the audience
- T: 3.1.6.1 – Adjust an intelligence product for a specified audience

---

## 1. Key Concepts

The facts can stay the same. The **product** changes. Actionable (**3.1.5**) asked whether someone can act. This hour is **making** the product fit a named audience. Finished dissemination (channels, markings) is **3.11.2**.

**Audience analysis (outline a):**

| Ask | Why it matters |
|-----|----------------|
| What **decision** do they own? | Type (**3.1.3**) and depth |
| How much **time** do they have? | Format (ticket line vs one-pager vs brief) |
| What **vocabulary** can they use? | JA3 vs “weak TLS fingerprint” vs “sensor gap” |
| What must they **not** have to ask you next? | Detail you keep vs cut |

**Adjust (outline b):** content (what stays), format (ticket / para / slides), detail (fields vs implication).

**Classroom rewrite line:**

`audience | keep | cut | format | one usable sentence`

| Audience | Keep | Cut | Format |
|----------|------|-----|--------|
| **SOC / IR** | Host, action, hunt pivot, confidence | Quarter budget, actor history essay | Ticket / worklog line |
| **Hunt lead** | Cluster, scope, 10-day plan | CEO risk paragraph | Short operational note |
| **Leadership** | Implication, decision, residual risk | JA3, mutex, raw hashes | Short paragraph / 3 bullets |

| This lesson | Other |
|-------------|-------|
| Rewrite for a named audience | Score actionable — **3.1.5** |
| Not the approved *channel* | **3.11.2** / **1.6.3** |
| Not a finished actor profile | **3.11.1.2** |

The task is the **rewrite**, not “audiences differ.”

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Same Night Owl facts → SOC isolate line *and* leadership fund/defer line | JA3 dump to the CEO |
| Cut hashes from the exec para | One product shipped to everyone |

---

## 2. Detailed Walkthrough / Examples

**Shared facts:** WS-JLEE; `nightowl-updates.net`; JA3 `a0e9f5…`; medium confidence; extra TLS sensor would see the next one.

### Example 1: Two Audiences, Two Products (Expected)

**SOC:** Isolate WS-JLEE with IR concurrence tonight; hunt that SNI/JA3 this shift. (Medium.)  
**Leadership:** We assess Night Owl will keep using weak TLS against finance-adjacent hosts this quarter; **fund the extra TLS sensor now** rather than wait. Residual risk if deferred: more missed beacons like WS-JLEE.

Same facts. Different keep/cut/format.

### Example 2: JA3 to the CEO (Lead)

**Shipped:** “JA3 `a0e9f5…`, SNI `nightowl-updates.net`, hash `6734f374…`.”

**Fail:** Leadership cannot act on those fields.  
**Adjust:** Use the leadership paragraph from Example 1. Put the JA3 in a **technical annex** or the SOC ticket — not the exec body.  
**Lead:** The facts are not wrong. The **audience fit** is.

### Example 3: One Memo for Everyone (Lead)

**Shipped:** Three pages mixing isolate steps, JA3, and a budget ask.

**Adjust:** Split. SOC gets Example 1 line. Leadership gets the fund/defer paragraph. Hunt lead gets the 10-day operational sentence.  
**Lead:** One blob is not tailoring.

---

## 3. Hands-On Exercise

**Objective:** Produce a rewrite line and the usable sentence.

**Use the shared Night Owl facts.**

**Instructions:**

1. One sentence each for Examples 1–3: what was kept vs cut.
2. For each audience, write the **rewrite line** plus the usable sentence.

   - A. **SOC** on WS-JLEE tonight.
   - B. **Hunt lead** deciding the next ten days.
   - C. **Leadership** on TLS sensor spend this quarter.
   - D. Same facts, audience = **detections** (technical).

3. Do not invent a new PIR. Do not pick the 3.11 channel. Do not re-score 3.1.5 unless you say you are checking the rewrite still passes.
4. If D is only fields and no action, that can still be correct **technical** tailoring.

**Expected Outcome:**
- Three example summaries
- Four rewrite lines + sentences
- No dissemination path, no actor profile

---

## 4. Knowledge Check

1. What four questions does **audience analysis** ask?
2. What three things do you **adjust** (outline b)?
3. Why is a correct JA3 still wrong for leadership?
4. Why is one memo to everyone not tailoring?
5. Where is **approved channel / marking** taught?

---

## 5. Summary

- Analyze the audience. Rewrite keep / cut / format.
- Next: attribution purpose, confidence, types (**3.1.7**).

---

## 6. References & Further Reading

- Related modules:
  - 3.1.5 – Actionable intelligence (previous)
  - 3.1.7 – Attribution (next)
  - 3.11.2 – Disseminating intelligence (builds on this)
  - 3.1.3 – Intelligence types
- Local audience / product catalog (optional)
