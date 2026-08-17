# Module 2.2.2 – Hunt Development Concepts

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.2.2 B / C / C · 2.2.2.1 3c / 4c / 4d · 2.2.2.2 3c / 4c / 4d · 2.2.2.3 3c / 4c / 4d  
- SOC: 2.2.2 A / B / B · 2.2.2.1 1a / 1a / 2b · 2.2.2.2 1a / 1a / 2b · 2.2.2.3 1a / 1a / 2b  
- CTI: 2.2.2 A / B / B · 2.2.2.1 1a / 2b / 3c · 2.2.2.2 1a / 2b / 3c · 2.2.2.3 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Develop and document a hunt hypothesis that can fail.
2. Scope a hunt (who, where, how long, what you can see).
3. Prioritize one hunt against another with a stated reason.
4. Identify unique patterns or behaviors that are worth an internal search.

**Mapped Proficiency Items:**
- K: 2.2.2 – Hunt development concepts
- T: 2.2.2.1 – Develop and document a hunt hypothesis
- T: 2.2.2.2 – Scope and prioritize a hunt
- T: 2.2.2.3 – Identify unique patterns or behaviors suitable for hunting

---

## 1. Key Concepts

### 1.1 Hypothesis and Unique Patterns

A hunt hypothesis is a **testable if/then**, not a slogan.

| Must include | Why |
|--------------|-----|
| **If** (the story) | What you think is happening |
| **Then we should see Y** | A searchable result. If Y cannot appear in your data, you do not have a hypothesis yet |
| **Scope hook** | Who / where / how long — even a draft |
| **What would kill it** | A result that means the story is wrong or untestable here |

**Most critical distinction for daily work:**  
“Attackers use scheduled tasks” is not a hypothesis. Nothing can fail.

| Weak | Documented |
|------|------------|
| Attackers persist with scheduled tasks | If a staging host on Building C servers uses new SYSTEM scheduled tasks after hours, we should see task-create events on servers that had none in 30 days |
| Finance is beaconing | If finance laptops talk to lookalike update CDNs after 21:00, we should see repeated DNS + TLS to those names from the finance VLAN |
| Hunt ransomware | If the bulletin installer hash ran here, we should see that hash or the parent process on endpoints with EDR |

**Unique pattern or behavior** means something you can search *internally* that is not already a high-volume SOC signature — rare, scoped, or off a named baseline.

| Suitable for hunting | Not suitable (yet) |
|----------------------|--------------------|
| New SYSTEM task on a server class with a 30-day none baseline | “Any scheduled task” |
| Repeated DNS+TLS to a lookalike CDN from one VLAN after hours | “Any outbound 443” |
| Same rare parent process on unalerted peers of an IR host | Re-pulling last night’s High queue |
| JA3 + odd SNI pairing that no analytic uses | A field with no place to query it |

If the pattern only exists in a segment you cannot see, name the **visibility gap**. Do not write a hypothesis you cannot test. Purpose from **2.1** still applies: you are aiming at missed activity or a gap. Hunt *type* (**2.2.1**) is how the work started. This lesson is how you write, bound, and rank it.

How to extract TTPs from a report is **2.4**. ATT&CK coverage ranking is **2.5**. Persistence how-to is **2.6**. Online enrichment is **2.3**. Do not pull those in here.

### 1.2 Scope and Priority

**Scope** answers four questions before the first search:

| Question | Write it as |
|----------|-------------|
| Who / what | Host class, user group, VLAN, app |
| Where (data) | Logs or sensors you actually have |
| How long | Time window and retention you can query |
| Out of scope | What you will *not* claim |

**Priority** is a stated reason to run *this* hunt before *that* one. Use what you already know: missed-activity likelihood, detection vs visibility gap, blast radius, freshness of the lead, and whether the search can even run.

| Higher priority (example reasons) | Lower / later |
|-----------------------------------|---------------|
| Named objects, data exists, no analytic (detection gap) | Slogan with no Y |
| Finance VLAN, current bulletin, 7-day window you can query | “Whole enterprise, all time” |
| IR spark + unalerted peers | Queue already owned by SOC |
| Pattern is rare and searchable | Pattern is every admin’s daily work |

A hunt that cannot be scoped (no telemetry, infinite window, entire company) is not ready. Park it or shrink it. Changing scope mid-hunt is allowed if you write the new bound.

Execute-by-type (first search, honest quiet, hand-back) was **2.2.1**. Here you owe the card *before* that search: hypothesis, pattern, scope, priority.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Hypothesis, Pattern, Scope, Priority)

**Input:** This week’s bulletin lists lookalike update CDN names. Finance is in scope for the program. DNS and TLS are in the SIEM. Lab has no DNS.

**Documented card**

| Field | What they wrote |
|-------|-----------------|
| Hypothesis | If finance laptops follow the bulletin CDN pattern after hours, we should see repeated DNS + TLS to those names from the finance VLAN |
| Pattern | Repeated after-hours DNS + TLS to the bulletin names (not “any HTTPS”) |
| Scope | Finance VLAN workstations; DNS + TLS; last 7 days; **not** lab (no DNS) |
| Priority | Run now: current bulletin, detection gap likely (data exists, no analytic), bounded window |
| Kill / quiet | No matching names in finance DNS/TLS for 7 days = hypothesis fails *for that VLAN*. Lab stays a visibility gap, not quiet |

**Interpretation:**  
This is hunt development. Y can fail. Scope names data and an exclusion. Priority has a reason. The pattern is specific enough to search. Type would be **hypothesis-driven** (or intel-seeded then switched — say so). You have not executed the 14-day beacon hunt yet; that first search is **2.2.1**.

### Example 2: Unbounded Slogan (Lead)

A hunt channel card:

> Hypothesis: attackers use scheduled tasks. Scope: everywhere. Priority: high. Pattern: persistence.

Compare a documented card from the same morning:

> If Building C Windows servers use new SYSTEM scheduled tasks after 02:00, we should see task-create events on hosts with a 30-day none baseline. Scope: Building C servers with process logging; 24 hours vs 30-day baseline; not lab (no process logs). Priority: after the finance CDN hunt — smaller blast radius, but the pattern is rare. Kill: no new SYSTEM tasks in that class.

**Interpretation:**  
The first card is not developed. No Y, no real scope, “persistence” is not a unique pattern, “high” is not a reason. The second is **2.2.2** done: hypothesis, unique pattern, scope, priority. Lab is excluded, not declared clean.

### Example 3: Two Patterns (Lead)

**Write-up A**

> Unique behavior: outbound 443. Hunt the enterprise. High priority because C2 uses HTTPS.

**Write-up B**

> Unique pattern: new outbound **8443** from VLAN 40, which had **none** in 30 days. Scope: VLAN 40 conn/TLS; 24 hours vs 30-day baseline. Priority: now if capacity — rare, no analytic. Not a pattern: “any 443.”

**Interpretation:**  
A is daily traffic. It will not find missed activity; it will drown the hunt. B is a unique, searchable deviation. If you have no 30-day baseline, you do not have this pattern yet — write a different Y or collect the baseline first.

---

## 3. Hands-On Exercise

**Objective:** Practice writing a hypothesis, bounding scope, ranking hunts, and picking a pattern.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (developed, or not, and why).
2. For each item below, say whether it is a **usable hypothesis**, a **usable scope**, a **stated priority**, a **hunt-worthy pattern**, or **not ready**. Give one reason.
   - “Attackers use scheduled tasks”
   - “If finance laptops beacon to bulletin CDN names after 21:00, we should see repeated DNS+TLS from the finance VLAN”
   - “Scope: the whole company, all logs, all time”
   - “Finance VLAN; DNS+TLS; 7 days; not lab”
   - “Run the finance CDN hunt before the Building C task hunt because the bulletin is current and data already exists”
   - “Unique pattern: any outbound 443”
3. Write **one hunt card** (four sentences or a small table): hypothesis, unique pattern, scope, priority. Use either the finance CDN bulletin or the Building C SYSTEM-task baseline. Do not execute the SIEM search (that was 2.2.1).

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- One card that can fail, is bounded, ranked, and names a searchable pattern

---

## 4. Knowledge Check

1. What must a documented hunt hypothesis include that a slogan does not?
2. What four questions does hunt scope answer?
3. Give one valid reason to prioritize hunt A over hunt B.
4. Which is a unique pattern suitable for hunting: “any outbound 443,” or “new outbound 8443 on a VLAN with a 30-day none baseline”? Why?
5. You write a hypothesis that can only be tested on a VLAN with no DNS logging. What do you do?

---

## 5. Summary

- Develop the hunt *before* the first search: hypothesis, pattern, scope, priority.
- A hypothesis is if/then with a Y that can fail.
- Scope names who, data, window, and what you will not claim.
- Priority is a reason, not the word “high.”
- Unique patterns are rare or off-baseline and searchable internally — not daily traffic.
- Types and first execute move remain **2.2.1**. Next unit is online enrichment (**2.3**).

---

## 6. References & Further Reading

- Related modules:
  - 2.1 – Purpose of Threat Hunting
  - 2.2.1 – Hunt types
  - 2.3 – Online tools and enrichment (next)
  - 2.4 – CTI for hunters
- Local hunt charter / intake card (when published)
