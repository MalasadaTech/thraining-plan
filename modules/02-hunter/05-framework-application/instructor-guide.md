# Instructor Guide – Module 2.5.1 – Using MITRE ATT&CK for Hunt Planning and Coverage Analysis

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.5.1 B / C / C · 2.5.1.1 3c / 4c / 4c · 2.5.1.2 3c / 4c / 4d · 2.5.1.3 3c / 4c / 4d  
- SOC: 2.5.1 A / B / B · 2.5.1.1 1a / 2b / 3c · 2.5.1.2 1a / 2b / 3c · 2.5.1.3 1a / 1a / 2b  
- CTI: 2.5.1 B / C / C · 2.5.1.1 3c / 4c / 4c · 2.5.1.2 2b / 3c / 4c · 2.5.1.3 2b / 3c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on identification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach hunters to map a hunt plan or findings to ATT&CK tactics and techniques, use that map to name detection vs visibility gaps, and let ATT&CK support (not replace) hunt priority.

**Key Teaching Points:**
- Copy ID (2.4.2) ≠ map this hunt (2.5.1.1).
- Map only techniques the hunt actually uses.
- Detection gap vs visibility gap, per mapped technique (2.5.1.2).
- ATT&CK supports priority with 2.2.2 reasons (2.5.1.3).
- Stay out of extract-from-scratch (2.4), STIX authoring (3.10), persistence how-to (2.6), execute (2.2.1), published Navigator layers as the deliverable.

**Common Student Challenges:**
- Shading a whole intrusion-set layer.
- Inventing T1547.001 to fill Persistence.
- Calling a heat-map color a priority reason.
- Hunting a visibility gap because the cell is “in ATT&CK.”
- Stopping after copying the report’s ID.
- Teaching how the technique works on disk (2.6).

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for an ATT&CK card (map / gap / priority)
- Optional: one Navigator screenshot as a *bad* heat map, not as a lab
- Same finance CDN / Building C leftovers from 2.4 if available
- Answer key (this guide)

---

## Learning Objectives

1. Map a hunt plan or hunt findings to ATT&CK tactics and techniques.
2. Use that map to name detection gaps and visibility gaps.
3. Use ATT&CK to support which hunt runs first — not as the only reason.
4. Tell mapping and coverage work apart from copying an ID off a report.

**Mapped Items:**
- K: 2.5.1 – Using MITRE ATT&CK for hunt planning and coverage analysis
- T: 2.5.1.1 – Map a hunt plan or hunt findings to MITRE ATT&CK
- T: 2.5.1.2 – Use ATT&CK to identify detection or visibility gaps
- T: 2.5.1.3 – Use ATT&CK to support hunt prioritization

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Copy vs map; 2.4.2 already done |
| Mapping tactics / techniques   | 12 min   | One hunt, two rows on the board |
| Gaps + ATT&CK-supported priority | 10 min | Kill heat-map priority |
| Walkthrough Examples           | 14 min   | Students score each card first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~68 min** | Stretch Example 2 if they still hunt “all of Persistence” |

---

## Detailed Teaching Notes

### 1. Mapping

**Talking Points:**
- Ask for last week’s leftover hunt before definitions. Map it live in two rows: tactic, technique, method.
- Hunter 3 is already at principles (B / 3c). Push a map a teammate can hunt from.
- Hunter 2.5.1.1 tops at **4c**, not 4d. Do not invent a 4d on mapping.
- SOC: recognize a real map vs a dump (1a → 2b). CTI maps at the same 3c / 4c / 4c bar as hunters on 2.5.1.1.
- SOC/CTI priority is lighter (SOC 1a / 1a / 2b; CTI 2b / 3c / 4c).

**What to emphasize:**
- Plan and findings both count. Findings map what you *saw*, not what the group “also does.”
- Navigator is optional. A table is the standard.

**Questions to ask the class:**
- “Which technique did *this* hunt actually use?”
- “Did we extract that method in 2.4.2, or are we filling a tactic?”

### 2. Gaps and priority

**Talking Points:**
- Two gap types only, per mapped technique.
- Visibility gap = name it, do not hunt it.
- Priority = ATT&CK + can we run it + why this population.

**What to emphasize:**
- Same technique on two hunts → ATT&CK cannot break the tie.
- “Red cell” is not a reason.

**Question to ask:**  
“If we can run only one hunt Monday, which mapped technique and why — in one sentence that names the gap type?”

### 3. Examples

Work through all three interactively. Students mark mapped vs not before you read the interpretation.

**Extra point for Example 1:**  
Complete card. Point at reused T1071.001 *and* the dropped task aside.

**Extra point for Example 2:**  
Heat map of a group ≠ map of a hunt. Same firehose family as 2.4.2 / 2.4.3 Example 2.

**Extra point for Example 3:**  
Invented T1547.001 will be popular. Force: if the hunt is not Run keys, do not map T1547.001.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 14–16 minutes.
- Allow use of the Student Guide.
- Tell them extract already happened. Do not grade a re-triage or a STIX label set.
- Review as a group. Do not collect a grade.
- Park persistence labs, TAXII, and SIEM execute.

**What good answers look like:**

**Summaries:**
- Example 1: Mapped — T1071.001 + finance method; detection gap in prod; lab is visibility; priority uses that gap.
- Example 2: First paste not a map (whole layer); second maps one technique and a detection gap.
- Example 3: A invents Persistence and hunts a gap; B maps only the hostname/C2 hunt.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Finance CDN hunt → TA0011 / T1071.001 | **Map** | This hunt’s method |
| Navigator layer, every tactic shaded | **Not a map** | Group heat map |
| DNS+TLS exist; no analytic for those names | **Detection gap** | See it, nothing alerts |
| Run-key technique, no registry logging | **Visibility gap** | Cannot test |
| “TA0003 is the reddest, hunt it first” | **Not a reason** | Color is not priority |
| Building C script hunt first: mapped, logged, no analytic | **ATT&CK-supported priority** | Technique + data + detection gap + scope |

**ATT&CK card (example answer — finance CDN):**  
Map: TA0011 / T1071.001 (CDN HTTPS C2). Detection gap: finance DNS+TLS, no name analytic. Visibility: lab DNS (do not hunt). Priority: finance after-hours DNS+TLS first — mapped, current, scoped, detection gap. Hash-only later if EDR already covers the hash.

Fail the card if they shade a whole tactic, invent an ID, hunt a visibility gap, or the priority is “because ATT&CK.”

---

## Knowledge Check – Answer Key

1. **Copy ID vs map a hunt?**  
   **Answer:** Copying records an ID the report already printed (2.4.2). Mapping assigns tactic + technique to *this* plan or these findings so you can do coverage and priority.  
   **Explanation:** A label is not coverage analysis.

2. **One mapped hunt?**  
   **Answer (equivalent):** [method] → [TAxxxx] / [Txxxx(.xxx)]. Example: after-hours DNS+TLS to named CDNs → TA0011 / T1071.001.  
   **Explanation:** Method must be present, not only the ID.

3. **Detection gap vs visibility gap after a map?**  
   **Answer:** Detection gap — telemetry for that technique exists, no (or weak) analytic. Visibility gap — you cannot see that technique here.  
   **Explanation:** Only hunt what you can test.

4. **Why is a red heat-map tactic not enough to prioritize?**  
   **Answer:** It is not tied to this hunt’s method, scope, or whether the search can run. Color is not a reason.  
   **Explanation:** ATT&CK supports 2.2.2 priority; it does not replace it.

5. **Same technique on two hunts — tie break?**  
   **Answer:** Scope, impact / blast radius, freshness, and whether the search can run. ATT&CK cannot break a same-technique tie.  
   **Explanation:** Framework supports judgment; it is not the judgment.

---

## Additional Instructor Resources

- Same leftovers as 2.4.2 / 2.4.3
- Escalation: copy ID → 2.4.2; STIX → 2.4.3; card format → 2.2.2; technique how-to → 2.6
- Next recommended module: Persistence techniques (2.6)
