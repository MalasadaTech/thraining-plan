# Module 2.5.1 – Using MITRE ATT&CK for Hunt Planning and Coverage Analysis

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.5.1 B / C / C · 2.5.1.1 3c / 4c / 4c · 2.5.1.2 3c / 4c / 4d · 2.5.1.3 3c / 4c / 4d  
- SOC: 2.5.1 A / B / B · 2.5.1.1 1a / 2b / 3c · 2.5.1.2 1a / 2b / 3c · 2.5.1.3 1a / 1a / 2b  
- CTI: 2.5.1 B / C / C · 2.5.1.1 3c / 4c / 4c · 2.5.1.2 2b / 3c / 4c · 2.5.1.3 2b / 3c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Map a hunt plan or hunt findings to ATT&CK tactics and techniques.
2. Use that map to name detection gaps and visibility gaps.
3. Use ATT&CK to support which hunt runs first — not as the only reason.
4. Tell mapping and coverage work apart from copying an ID off a report.

**Mapped Proficiency Items:**
- K: 2.5.1 – Using MITRE ATT&CK for hunt planning and coverage analysis
- T: 2.5.1.1 – Map a hunt plan or hunt findings to MITRE ATT&CK
- T: 2.5.1.2 – Use ATT&CK to identify detection or visibility gaps
- T: 2.5.1.3 – Use ATT&CK to support hunt prioritization

---

## 1. Key Concepts

### 1.1 Mapping hunts to tactics and techniques

**2.4.2** taught you to *copy* an ATT&CK ID when a report already printed it. This lesson is the next job: **map the hunt you will run** (or what you already found) onto tactics and techniques so you can see coverage and rank work.

You map **this hunt**, not the whole enterprise and not the vendor’s entire matrix.

| You map | You write | You do not |
|---------|-----------|------------|
| Hunt **plan** | The method you will search → tactic + technique (and sub-technique if you actually use it) | Color every cell in Navigator “because CTI mentioned the group” |
| Hunt **findings** | What you observed → the technique that describes *that* method | Invent an ID so the card looks complete |
| Printed ID from CTI | Keep it if the hunt is still about that method | Treat the printed ID as a coverage analysis |

**Most critical distinction for daily work:**  
A copied ID is a label. A **map** is tactic + technique + *this* hunt’s method, plus whether you can see it and whether anything already alerts on it.

| Mapped (good) | Not a map |
|---------------|-----------|
| Finance after-hours CDN hunt → **TA0011** Command and Control / **T1071.001** Web Protocols | “They use persistence” with no technique |
| New SYSTEM task on Building C servers → **TA0003** Persistence / **T1053.005** Scheduled Task | Navigator layer with every tactic shaded |
| Finding: `wscript.exe` + rare script → **T1059.005** Visual Basic (if that is what you saw) | Guessing **T1547.001** because Run keys are popular |
| Report printed **T1071.001** and the hunt is still those CDN names | Copying **T1071.001** and stopping (**2.4.2** only) |

Navigator is a *view*. A four-row table is enough. You do not owe a published layer, a scoring model, or a full ATT&CK catalog.

How techniques *work* on disk (Run keys, startup folder, task XML) is **2.6**. Full hunt-card format is **2.2.2**. STIX objects are **2.4.3**. Stay here: map, name gaps, rank.

### 1.2 Coverage gaps and ATT&CK-supported priority

After the map, ask two gap questions **per technique you actually mapped**.

| Gap | Meaning | ATT&CK helps when |
|-----|---------|-------------------|
| **Detection gap** | Telemetry exists; no analytic (or a weak one) covers that technique in this scope | You can point at T1071.001 + “we log DNS+TLS, no lookalike-CDN rule” |
| **Visibility gap** | You cannot see the technique here | You can point at T1547.001 + “no registry logging on that class” |

Do not hunt a visibility gap. Name it. A detection gap on a mapped, scoped technique is often hunt-shaped.

**Priority** still needs a stated reason (**2.2.2**). ATT&CK **supports** the reason. It does not replace scope, blast radius, or freshness.

| ATT&CK-supported (higher) | Later / not a reason |
|---------------------------|----------------------|
| Mapped technique, data exists, no analytic (detection gap), scoped population | “TA0002 is red on the heat map” |
| Two leftover techniques; hunt the one you can see this week | “Persistence is always first” |
| Findings already map to T1053.005 on a server class with no task analytic | Whole-matrix coverage score with no hunt attached |

If two hunts map to the same technique, ATT&CK cannot break the tie. Use scope, impact, and whether the search can run.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Map → gap → rank)

**Input:** Hunt-worthy finance CDN bulletin already extracted (**2.4.1** / **2.4.2**). Plan: after-hours DNS+TLS to named lookalike CDNs; installer hash on EDR. DNS+TLS exist. No analytic for those names. Lab has no DNS (visibility gap for the *lab*, not for production finance). Report already listed **T1071.001**.

**ATT&CK card**

| Field | What they wrote |
|-------|-----------------|
| Map (plan) | C2 over HTTPS to named CDNs → **TA0011** / **T1071.001**. Hash check is the same campaign, not a second tactic unless you are hunting the installer behavior |
| Coverage | **Detection gap** on T1071.001 in finance (logs yes, analytic no). Lab DNS = **visibility gap** (do not hunt the lab) |
| Priority | Run the finance DNS+TLS hunt first: mapped, scoped, current, detection gap. Park the hash-only question if EDR already alerts on that hash |
| Not done | Did not shade TA0003 because the report had a “scheduled tasks” aside. That aside was dropped in **2.4.2** |

**Interpretation:**  
This is mapping and coverage. The printed ID was reused because the hunt is still that method. Priority uses ATT&CK *and* the **2.2.2** reasons. Nobody executed the search (**2.2.1**). Nobody taught scheduled-task mechanics (**2.6**).

### Example 2: Heat-Map Dump (Lead)

A hunt channel paste:

> Mapped to ATT&CK: whole Navigator layer for the intrusion-set. Everything in Persistence and C2 is red. Hunt the enterprise. Priority: TA0003 because it is the reddest.

Compare a documented map from the same extract:

> Map: parent `wscript.exe` + rare script → **T1059.005** (this hunt only). Coverage: process logging on Building C = yes; no analytic for that parent+script = **detection gap**. Visibility: no coverage claim on T1547 — we never extracted Run keys. Priority: Building C process-create in 24 hours before any “whole Persistence tactic” hunt. Reason: mapped technique + data + no analytic + finite scope.

**Interpretation:**  
A heat map of a group is not a hunt map. Red cells are not a priority reason. The second write-up is **2.5.1.1**–**2.5.1.3**.

### Example 3: Invented Technique + Gap as Hunt (Lead)

**Write-up A**

> Mapped to T1547.001 so we have Persistence coverage. We don’t have registry logging. Priority: hunt persistence first because ATT&CK says so.

**Write-up B**

> No map to **T1547.001** — the plan is the hostname, not Run keys, and we have **no telemetry** (visibility gap). Map: hostname follow-through → **TA0011** / **T1071.001** only if the hunt is still DNS/TLS to that name (or leave tactic blank and write “none — infra IOC only”). Priority: the DNS/TLS hunt if finance + 7 days is queryable; do not prioritize a Persistence cell we cannot see.

**Interpretation:**  
A invents a technique to fill a tactic and then hunts a visibility gap. B only maps what the hunt actually is, names the gap, and lets ATT&CK support a reason that can fail.

---

## 3. Hands-On Exercise

**Objective:** Practice mapping a hunt, naming gaps from that map, and using ATT&CK to support priority.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (mapped, or not, and why).
2. For each item below, say **map**, **detection gap**, **visibility gap**, **ATT&CK-supported priority**, or **not a map / not a reason**. Give one reason.
   - Finance CDN hunt → TA0011 / T1071.001
   - Navigator layer with every tactic shaded for the intrusion-set
   - DNS+TLS exist; no analytic for those CDN names
   - Run-key technique, no registry logging
   - “TA0003 is the reddest, hunt it first”
   - Building C script hunt first because T1059.005 is mapped, logged, and has no analytic
3. Write **one ATT&CK card** (small table or four sentences): map, detection vs visibility gap, priority reason. Use the finance CDN hunt *or* the Building C parent+script leftover. Do not extract CTI from scratch. Do not author STIX. Do not explain how persistence works. Do not execute a SIEM search.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- One card that maps *this* hunt, names the right gap type, and uses ATT&CK to support a priority that can be argued

---

## 4. Knowledge Check

1. What is the difference between recording an ATT&CK ID from a report and mapping a hunt?
2. Give one mapped hunt (tactic + technique + the method you would search).
3. After you map a technique, how do you tell a **detection gap** from a **visibility gap**?
4. Why is “this tactic is red on the heat map” not enough to prioritize a hunt?
5. Two hunts map to the same technique. What do you use to break the tie?

---

## 5. Summary

- Map **this** hunt plan or these findings — not the vendor matrix and not a group heat map.
- A map is tactic + technique + method. Copied IDs from **2.4.2** are inputs, not coverage analysis.
- Per mapped technique: detection gap (see it, nothing alerts) vs visibility gap (cannot see it).
- ATT&CK supports priority. It does not replace scope, impact, or “can this search run.”
- Do not invent techniques to fill a tactic. Do not hunt a visibility gap.
- Next: persistence techniques (**2.6**).

---

## 6. References & Further Reading

- Related modules:
  - 2.4.2 – Extracting hunt leads from CTI (copy IDs)
  - 2.4.3 – STIX as hunt input
  - 2.2.2 – Hunt development (scope and non-ATT&CK priority)
  - 2.6 – Persistence techniques (next)
- Local ATT&CK version / Navigator view used in class (optional)
- MITRE ATT&CK (enterprise) — tactics and techniques named in class
