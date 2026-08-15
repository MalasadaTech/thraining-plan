# Module 2.2.2 – Hunt Development Concepts  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 2.2.2 – Hunt Development Concepts  
**Subtitle:** Threat Hunter Training (SOC / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Ask for a hunt hypothesis before definitions. This lesson is the card before execute. Not type-sort. Not tool labs.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Develop and document a hypothesis that can fail
2. Scope a hunt (who, data, window, exclusions)
3. Prioritize with a stated reason
4. Identify unique patterns worth an internal search

**Mapped Items:**  
K: 2.2.2 | T: 2.2.2.1–2.2.2.3

**Speaker Notes:**  
Hunter 3 is already at principles (B / 3c). Push a teammate-ready card.

---

### Slide 3 – Agenda
**Title:** Agenda

- Hypothesis and unique patterns
- Scope and priority
- Three worked examples
- Identification practice
- Hands-on hunt card
- Knowledge check

**Speaker Notes:**  
2.2.1 was types + first search. 2.3 is tools. Stay here.

---

### Slide 4 – Not a Hypothesis
**Title:** Slogans Are Not Hypotheses

“Attackers use scheduled tasks.”  
“Hunt ransomware.”  
“Finance is beaconing.”

**Key Point:** If Y cannot fail in your data, you do not have a hypothesis yet.

**Speaker Notes:**  
Leave the slogans up. Kill them in Example 2.

---

### Slide 5 – Documented Hypothesis
**Title:** If / Then / Kill

| Field | Job |
|-------|-----|
| **If** | The story |
| **Then we should see Y** | Searchable result |
| **Scope hook** | Who / where / how long |
| **Kill** | What means the story is wrong or untestable |

**Analyst Tip:** Type (intel / hypothesis / reactive / anomaly) is **2.2.1**. This is the write-up.

**Speaker Notes:**  
Have a student rewrite one slogan live.

---

### Slide 6 – Unique Patterns
**Title:** Suitable for an Internal Search

**Hunt-worthy:** rare, scoped, or off a named baseline  
**Not yet:** daily admin work, “any 443,” a field you cannot query

**Key Point:** Unique ≠ a MITRE name. Unique = the query will not return half the company.

**Speaker Notes:**  
Park ATT&CK depth (2.5) and persistence catalogs (2.6).

---

### Slide 7 – Scope
**Title:** Four Scope Questions

1. Who / what?
2. Which data / sensors?
3. How long?
4. What will we **not** claim?

**Analyst Tip:** No DNS on lab → lab is out of scope, not “clean.”

**Speaker Notes:**  
“Everywhere, all time” fails all four.

---

### Slide 8 – Priority
**Title:** Priority Is a Reason

Run A before B because:

- The lead is current
- Data already exists (likely detection gap)
- Blast radius is larger
- The other card has no Y or no telemetry

**Key Point:** The word “high” is not a priority.

**Speaker Notes:**  
Do not open ATT&CK coverage scoring.

---

### Slide 9 – Example 1: Complete Card
**Title:** Example 1 – Finance CDN

- If finance follows bulletin CDN names after hours → repeated DNS+TLS
- Pattern: those names, after hours, finance VLAN
- Scope: finance; DNS+TLS; 7 days; **not lab**
- Priority: now — current bulletin, data exists

**Interpretation:**  
Developed. Y can fail. Lab is a visibility gap, not quiet.

**Speaker Notes:**  
Students score the card before you reveal the interpretation.

---

### Slide 10 – Example 2: Slogan vs Card
**Title:** Example 2 – Scheduled Tasks

**A:** Attackers use scheduled tasks. Scope: everywhere. Priority: high.  
**B:** If Building C servers create new SYSTEM tasks after 02:00, we should see task-create on a 30-day none baseline. Lab excluded.

**Interpretation:**  
A is not developed. B is the card.

**Speaker Notes:**  
Same slogan family as 2.2.1 Example 3 write-up A.

---

### Slide 11 – Example 3: Two Patterns
**Title:** Example 3 – 443 vs 8443

**A:** Unique behavior: outbound 443. Hunt the enterprise.  
**B:** New outbound **8443** on VLAN 40; **none** in 30 days.

**Interpretation:**  
A is daily traffic. B is a unique, searchable deviation.

**Speaker Notes:**  
Force: no baseline, you do not have B yet.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Mission statement instead of Y
- Scope = entire company
- Priority = “high”
- Pattern = technique nickname
- Re-doing type-sort instead of writing the card

**Speaker Notes:**  
Ask for a local rejected intake card. Then the exercise.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 12–15 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide (reason each).
3. Write one hunt card: hypothesis, pattern, scope, priority.

**Speaker Notes:**  
Park SIEM execute blocks. Review with the Instructor Guide key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. What must a hypothesis include that a slogan does not?
2. Four scope questions?
3. One valid reason to run A before B?
4. Any 443 vs new 8443 on a 30-day none VLAN — which pattern, and why?
5. Hypothesis only testable on a VLAN with no DNS — what do you do?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Card first: hypothesis, pattern, scope, priority.
- Y must be able to fail.
- Scope names data and exclusions.
- Priority is a reason.
- Unique patterns are selective internal searches.
- Types / first search → **2.2.1**. Tools → **2.3**.

**Speaker Notes:**  
Do not open 2.3 tool labs.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 2.3 – Online tools and enrichment

**Resources:**
- Student Guide for this module
- Module 2.2.1 – Hunt types
- Module 2.1 – Purpose of Threat Hunting

**Speaker Notes:**  
Park VT, STIX, ATT&CK, persistence.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** Hunt Development Quick Reference

**Hypothesis:** If X, then we should see Y (Y can fail)

**Scope:** who · data · window · will not claim

**Priority:** why this before that

**Pattern:** rare / off-baseline / searchable — not daily traffic

**Test:**  
- no Y → not ready  
- everywhere / all time → not ready  
- “high” only → not ready  

**Speaker Notes:**  
Leave this up as a reference or print it.

---

## Design Notes for Slide Builder

- Keep the four-field card large enough to read
- Visually reject slogan / everywhere / any-443
- Consistent footer with module number
- Minimal text — let the three examples teach
