# Module 3.1.7 – Attribution

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.1.7 A / A / A · 3.1.7.1 1a / 1a / 1a  
- Hunter: 3.1.7 A / B / B · 3.1.7.1 1a / 2b / 3c  
- CTI: 3.1.7 B / C / C · 3.1.7.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain **why** we attribute and **why it is hard**.
2. Use **confidence levels** and **types** (activity group vs nation-state).
3. **Assess** an attribution statement: confidence claimed vs evidence present.

**Mapped Proficiency Items:**
- K: 3.1.7 – Attribution (purpose, confidence, types)
- T: 3.1.7.1 – Assess attribution statements for confidence and supporting evidence

---

## 1. Key Concepts

Attribution names **who or what cluster** is responsible — at a stated type and confidence. It is not a finished actor profile (**3.11.1.2**). Estimative wording depth is **3.2.1**.

**Purpose (outline a):** Focus collection, hunting, and defense on the right cluster.  
**Challenges (outline a):** Shared infrastructure, false flags, vendor marketing names, missing internals, one-blog claims.

**Classroom confidence (outline b — this lesson only, not a live ODNI card):**

| Level | Use when |
|-------|----------|
| **Low** | Thin or single-source; alternatives are easy |
| **Medium** | Multiple independent internals *or* internals + one solid external, still other explanations |
| **High** | Several independent lines (malware, infra, victimology, ops tempo) and alternatives are weak |

If your site uses a different scale, substitute it. The obligation is **stated confidence + evidence**, not these labels.

**Types (outline c):**

| Type | Means | Do not treat as |
|------|-------|-----------------|
| **Activity group / cluster** | Same tooling, infra, or ops pattern (e.g., Night Owl) | A country |
| **Named intrusion set** | A tracked set with a stable label | Automatically a government |
| **Nation-state** | A government or its tasked organ | A blog nickname |

**Most critical distinction:** Activity-group clustering is usually what you can support. Nation-state is a **higher** claim and needs more.

| This lesson | Other |
|-------------|-------|
| Assess the *statement* | Write the finished profile — **3.11.1.2** |
| Classroom low/med/high | Estimative lexicon — **3.2.1** |
| Not Admiralty source letter | **3.2.3** |

The task is an **assess line**:

`claim | type claimed | confidence claimed | evidence present | supported / over-claim / wrong type`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Night Owl cluster, medium, infra+host overlap | “It’s China” from one blog name |
| Low confidence on nation-state, correctly caveated | Calling a cluster a country |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Supported Cluster (Expected)

**Claim:** “WS-JLEE is **Night Owl activity group**, **medium** — same SNI/JA3 as last week’s two lab hosts plus the encoded-PS + Run pattern.”

**Assess:** Type = activity group. Confidence = medium. Evidence = internal overlap on two independent lines (infra + tradecraft).  
**Supported.** Not a nation-state claim.

### Example 2: Blog Name = Country (Lead)

**Claim:** “High confidence nation-state (VendorName APT-12). Source: one public blog that used a country flag.”

**Assess:** Type claimed = nation-state. Confidence claimed = high. Evidence = single external nickname.  
**Over-claim.** At most **low** on an **activity group** (if the infra matches).  
**Lead:** Vendor name ≠ country. High is not earned.

### Example 3: Right Type, Inflated Confidence (Lead)

**Claim:** “High confidence Night Owl” based only on `nightowl-updates.net` resolving once on a guest laptop. No malware, no second host, no uniqueness note.

**Assess:** Type (activity group) is the right *kind*. Confidence **high** is not supported — one weak infra hit. Score **low** (or medium only if the domain is uniquely theirs *and* you say why).  
**Lead:** Type OK. Confidence fails.

---

## 3. Hands-On Exercise

**Objective:** Write the assess line.

**Use classroom low / medium / high.**

**Instructions:**

1. One sentence each for Examples 1–3: supported vs over-claim.
2. For each item, write the **assess line**.

   - A. “Medium: Night Owl cluster. Evidence: SNI + JA3 + same Run-key path on WS-JLEE and one lab host.”
   - B. “High: nation-state. Evidence: the blog headline.”
   - C. “Night Owl *is* China because the vendor map is red.”
   - D. “Low: possible Night Owl cluster. Evidence: one SNI hit; domain is also used by a CDN test.”

3. Do not write a 3.11 profile. Do not assign Admiralty letters (**3.2.3**).
4. If D is appropriately caveated, say **supported** at low.

**Expected Outcome:**
- Three example summaries
- Four assess lines
- No actor profile, no estimative-lexicon lesson

---

## 4. Knowledge Check

1. What is attribution **for**, and name one **challenge**?
2. When do you use **medium** vs **high** on the classroom scale?
3. Why is an **activity group** not automatically a **nation-state**?
4. What is wrong with “high confidence” on a single blog flag?
5. Where is the finished **actor profile** taught?

---

## 5. Summary

- Purpose, challenges, confidence, type.
- Assess claim vs evidence. Over-claim fails.
- Next: collection source classes (**3.1.8**).

---

## 6. References & Further Reading

- Related modules:
  - 3.1.6 – Tailoring to the audience (previous)
  - 3.1.8 – Collection sources (next)
  - 3.2.1 – Estimative language
  - 3.11.1.2 – Threat actor profile
- Local attribution / confidence card (optional — substitutes classroom low/med/high)
