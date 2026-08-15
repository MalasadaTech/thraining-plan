# Instructor Guide – Module 2.2.2 – Hunt Development Concepts

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.2.2 B / C / C · 2.2.2.1 3c / 4c / 4d · 2.2.2.2 3c / 4c / 4d · 2.2.2.3 3c / 4c / 4d  
- SOC: 2.2.2 A / B / B · 2.2.2.1 1a / 1a / 2b · 2.2.2.2 1a / 1a / 2b · 2.2.2.3 1a / 1a / 2b  
- CTI: 2.2.2 A / B / B · 2.2.2.1 1a / 2b / 3c · 2.2.2.2 1a / 2b / 3c · 2.2.2.3 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on identification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach how to develop a hunt: write a hypothesis that can fail, scope it, prioritize it, and name a unique searchable pattern. This is the card *before* execute-by-type (2.2.1).

**Key Teaching Points:**
- Hypothesis = if/then + Y that can fail. Slogans are not hypotheses.
- Scope = who, data, window, out-of-scope. “Everywhere / all time” is not scope.
- Priority = a reason. “High” is not a reason.
- Unique pattern = rare or off-baseline and internally searchable. Daily 443 is not unique.
- Stay out of execute-by-type drills (2.2.1), VT/AnyRun (2.3), TTP extract (2.4), ATT&CK rank (2.5), persistence how-to (2.6).

**Common Student Challenges:**
- Writing mission statements instead of Y.
- Scoping the entire enterprise to look thorough.
- Ranking by excitement or chat volume.
- Calling any TTP name a unique pattern.
- Re-running 2.2.1 type-sort instead of writing the card.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for a four-field hunt card
- Answer key (this guide)

---

## Learning Objectives

1. Develop and document a hunt hypothesis that can fail.
2. Scope a hunt (who, where, how long, what you can see).
3. Prioritize one hunt against another with a stated reason.
4. Identify unique patterns or behaviors that are worth an internal search.

**Mapped Items:**
- K: 2.2.2 – Hunt development concepts
- T: 2.2.2.1 – Develop and document a hunt hypothesis
- T: 2.2.2.2 – Scope and prioritize a hunt
- T: 2.2.2.3 – Identify unique patterns or behaviors suitable for hunting

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Blank four-field card on the board |
| Hypothesis and unique patterns | 14 min   | Kill slogans live |
| Scope and priority             | 10 min   | Four scope questions; one priority reason |
| Walkthrough Examples           | 14 min   | Students score each card first |
| Hands-On Exercise              | 15 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 3 min    | |
| **Total**                      | **~68 min** | Stretch Example 2 if the room still accepts “everywhere” |

---

## Detailed Teaching Notes

### 1. Hypothesis and Unique Patterns

**Talking Points:**
- Ask for a hypothesis before you show the table. Write the slogans and leave them up until Example 2 kills them.
- Hunter 3 is already at principles (B / 3c). Push a card they could hand a teammate, not a vibe.
- SOC: recognize a usable card vs a slogan (1a). CTI: they will often seed Y; they should still see what hunt needs (2b → 3c).

**What to emphasize:**
- Y must be able to fail in *their* data.
- Unique ≠ “MITRE technique name.” Unique = searchable and not daily noise.

**Questions to ask the class:**
- “What result would kill this story?”
- “Would this query return half the company on a Tuesday?”

### 2. Scope and Priority

**Talking Points:**
- Four scope questions. If one is blank, the hunt is not ready.
- Priority is comparative: why this before that.
- Do not open ATT&CK coverage matrices (2.5). Simple reasons are enough.

**What to emphasize:**
- Visibility gaps shrink scope; they do not get a “clean” stamp.
- Changing scope mid-hunt is fine if written.

**Question to ask:**  
“If we only have time for one hunt this afternoon, which card and why?”

### 3. Examples

Work through all three interactively. Students mark developed vs not before you read the interpretation.

**Extra point for Example 1:**  
Complete card. Point at Y, exclusion of lab, and a priority reason.

**Extra point for Example 2:**  
Same slogan family as 2.2.1 Example 3 write-up A. Here the fix is the *card*, not the type name.

**Extra point for Example 3:**  
A will be popular with people who fear missing C2. Force: 443 is not unique.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 12–15 minutes.
- Allow use of the Student Guide.
- Review answers as a group afterward. Do not collect a grade.
- If someone writes a SIEM execute block, thank them and park it for 2.2.1. Grade the card.

**What good answers look like:**

**Summaries:**
- Example 1: Developed — testable Y, finance/7-day/DNS+TLS, lab excluded, priority reason.
- Example 2: First card not ready; second is a complete development card.
- Example 3: A is daily 443 (not a pattern); B is a unique 8443 deviation with a baseline.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| “Attackers use scheduled tasks” | **Not ready** | No Y |
| Finance CDN if/then | **Usable hypothesis** | Y can fail |
| Whole company, all logs, all time | **Not ready** | Not a scope |
| Finance VLAN; DNS+TLS; 7 days; not lab | **Usable scope** | Who, data, window, exclusion |
| Finance CDN before Building C tasks because bulletin is current and data exists | **Stated priority** | Comparative reason |
| Any outbound 443 | **Not ready** | Not unique |

**Hunt card (example answer — finance CDN):**  
Hypothesis: if finance laptops follow the bulletin CDN names after 21:00, we should see repeated DNS+TLS from the finance VLAN. Pattern: repeated after-hours resolutions/sessions to those names. Scope: finance VLAN, DNS+TLS, 7 days, not lab. Priority: now — current bulletin, data exists, no analytic.

Fail the card if Y is missing, scope is unbounded, priority is only “high,” or the pattern is daily traffic.

---

## Knowledge Check – Answer Key

1. **What must a documented hunt hypothesis include that a slogan does not?**  
   **Answer:** A searchable Y (then we should see …) that can fail, plus at least a draft scope hook and what would kill the story.  
   **Explanation:** “Attackers use X” cannot fail.

2. **What four questions does hunt scope answer?**  
   **Answer:** Who/what; where (which data); how long; what is out of scope / will not be claimed.  
   **Explanation:** Missing one of these means the hunt is not ready.

3. **Give one valid reason to prioritize hunt A over hunt B.**  
   **Answer (any one):** Current lead; data already exists (detection gap likely); larger blast radius; the search can actually run; the other card has no Y.  
   **Explanation:** “High” is not a reason.

4. **Which is a unique pattern: any outbound 443, or new outbound 8443 on a VLAN with a 30-day none baseline? Why?**  
   **Answer:** The 8443 / 30-day none pattern. It is rare, measurable, and searchable. 443 is daily traffic.  
   **Explanation:** Unique means the internal search is selective.

5. **Hypothesis that can only be tested on a VLAN with no DNS logging. What do you do?**  
   **Answer:** Do not run it as written. Name the **visibility gap**, shrink or move scope to where data exists, or park the hunt.  
   **Explanation:** An untestable hypothesis is not developed.

---

## Additional Instructor Resources

- Local hunt intake card (sanitize an accepted card vs a rejected slogan)
- Escalation: type/execute → 2.2.1; tools → 2.3; CTI extract → 2.4; ATT&CK → 2.5
- Next recommended module: Online tools and enrichment (2.3)
