# Instructor Guide – Module 2.4.3 – STIX as Hunt Input

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.4.3 B / C / C · 2.4.3.1 3c / 4c / 4c · 2.4.3.2 3c / 4c / 4d  
- SOC: 2.4.3 A / A / B · 2.4.3.1 1a / 1a / 2b · 2.4.3.2 1a / 1a / 2b  
- CTI: 2.4.3 A / B / B · 2.4.3.1 1a / 2b / 3c · 2.4.3.2 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on identification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach hunters to read a STIX report or bundle as hunt input: name the objects they actually use, mark which are hunt-relevant, and turn leftovers into leads. They do not author STIX.

**Key Teaching Points:**
- Six hunter objects: indicator, attack-pattern, observed-data, malware, threat-actor / intrusion-set, relationship.
- Hunt-relevant ≠ every object in the JSON.
- A bundle seeds a hunt only after the 2.4.2 drop list.
- Identify (2.4.3.1), then convert (2.4.3.2).
- Stay out of triage-from-scratch (2.4.1), prose-only extract as the whole lesson (2.4.2), Navigator (2.5), STIX authoring (3.10), execute (2.2.1).

**Common Student Challenges:**
- Treating the whole indicator list as a hunt.
- Labeling types for 3.10 instead of asking “can I hunt this?”
- Using threat-actor / intrusion-set as a search.
- Inventing ATT&CK IDs or missing objects to “complete” the bundle.
- Extracting a visibility gap because it is valid STIX.
- Re-doing the 2.4.1 gate.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for a six-row object table and a seed card
- Same sanitized bulletin as 2.4.1 / 2.4.2, plus a one-page object table (not a full TAXII pull)
- Answer key (this guide)

---

## Learning Objectives

1. Name the STIX objects a hunter actually uses in a report or bundle.
2. Tell which of those objects are hunt-relevant and which only give context.
3. Explain how a STIX bundle seeds a hunt (you do not author STIX here).
4. Identify hunt-relevant objects, then turn them into hunt leads.

**Mapped Items:**
- K: 2.4.3 – STIX as hunt input
- T: 2.4.3.1 – Identify hunt-relevant objects in a report or bundle
- T: 2.4.3.2 – Turn those objects into hunt leads

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Assume 2.4.1 already said hunt-worthy |
| Six hunter objects             | 12 min   | Table on the board; skip CoA / Identity |
| How a bundle seeds a hunt      | 10 min   | Objects → drop → question |
| Walkthrough Examples           | 14 min   | Students score each card first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~68 min** | Stretch Example 2 if they still keep all 400 indicators |

---

## Detailed Teaching Notes

### 1. Objects a hunter actually uses

**Talking Points:**
- Show a six-row table, not raw JSON. JSON is optional decoration; the types are the lesson.
- Hunter 3 is already at principles (B / 3c). Push “which two objects would you hunt Monday?”
- SOC is A / A / B and 1a / 1a / 2b — recognize the six types and that a dump is not a seed.
- CTI: they may author this later (3.10). Here they still owe *hunt-shaped* leftovers (1a → 2b on identify; 1a / 1a / 2b on convert).
- Hunter 2.4.3.1 tops at **4c**, not 4d. Do not invent a 4d on identify.

**What to emphasize:**
- Relationship is the glue. Actor / intrusion-set is almost never the search.
- Observed-data is a sample, not a detection.

**Questions to ask the class:**
- “If we delete the relationships, what is left that we can still hunt?”
- “Did the attack-pattern actually print an ATT&CK ID?”

### 2. How a bundle seeds a hunt

**Talking Points:**
- Seed = identify + 2.4.2 drop + one question.
- Structured does not mean hunt-suitable.
- “None given” is a legal ATT&CK answer.

**What to emphasize:**
- Do not open a STIX editor.
- If leftovers cannot form a question, re-drop — same as 2.4.2.

**Question to ask:**  
“If we can keep only two objects from this bundle, which two — and what question do they support?”

### 3. Examples

Work through all three interactively. Students mark seeded vs not before you read the interpretation.

**Extra point for Example 1:**  
Complete seed. Point at recorded T1071.001, dropped task aside, actor as context only.

**Extra point for Example 2:**  
Same firehose family as 2.4.2 Example 2. Structure did not save the 400 IPs.

**Extra point for Example 3:**  
Invented T1547.001 and “I’ll add an indicator” will be popular. Force: if the bundle did not print it, you do not record or author it.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 14–16 minutes.
- Allow use of the Student Guide.
- Tell them 2.4.1 already passed. Do not grade a re-triage.
- Review as a group. Do not collect a grade.
- Park TAXII, STIX authoring, Navigator, and SIEM execute.

**What good answers look like:**

**Summaries:**
- Example 1: Seeded — CDN + hash indicators, HTTPS C2 pattern, uses-link; task aside and actor-as-search dropped; T1071.001 copied; question can fail.
- Example 2: First paste not a seed (annex + who-object); second keeps current domains/script and drops expired/noise.
- Example 3: A hunts a gap and invents an ID; B drops Run keys and keeps the hostname indicator.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| `indicator`: lookalike CDN this week | **Hunt-relevant** | Current named object |
| 400 generic VPS `indicator`s already blocked | **Drop** | Noise |
| `attack-pattern`: “They use persistence” | **Drop** | Slogan, not a TTP |
| `observed-data`: after-hours DNS+TLS to bundle names | **Hunt-relevant** | Searchable pattern |
| `attack-pattern` prints **T1071.001** | **Record ATT&CK** | Printed, not invented |
| `threat-actor` name, no linked indicator or pattern | **Context only** / **not a hunt lead** | Who is not a search |

**Seed card (example answer — finance CDN):**  
Identified: CDN + hash `indicator`s, HTTPS C2 `attack-pattern` (T1071.001 as printed), `uses` relationship. Dropped: task aside; actor as search; lab (no DNS). Leads: C2 method + hash + CDN names + after-hours DNS+TLS. Question: if finance follows those names after hours, we should see repeated DNS+TLS from the finance VLAN.

Fail the card if they keep the annex, invent an ATT&CK ID, author a missing object, extract a no-telemetry pattern, or the question is a slogan.

---

## Knowledge Check – Answer Key

1. **Three STIX objects a hunter uses, and what each is for?**  
   **Answer (any three, with the right job):** indicator — pattern/object to query; attack-pattern — method; observed-data — recorded sample; malware — family/sample (hash or named installer); threat-actor / intrusion-set — who / named activity (scope, not a search); relationship — which leftovers belong together.  
   **Explanation:** Kind alone does not make it hunt-relevant.

2. **When is an indicator hunt-relevant vs context or drop?**  
   **Answer:** Hunt-relevant when it is current, rare enough, and queryable. Drop when expired, already blocked, or daily noise. Context when it only names something you will not search.  
   **Explanation:** Being valid STIX is not enough.

3. **Attack-pattern already lists T1071.001. What do you do with the ID here?**  
   **Answer:** Copy it next to that lead. Do not map coverage or invent siblings.  
   **Explanation:** Mapping hunts is 2.5.

4. **Run-key attack-pattern, no registry logging. Identify, then what?**  
   **Answer:** Identify it, then **drop** it as a hunt lead. Name the visibility gap. Do not author a replacement object.  
   **Explanation:** Untestable is not a lead.

5. **One hunt question two leftover domain indicators could support?**  
   **Answer (equivalent):** If [population] talks to those names [window], we should see DNS `query` or TLS `server_name` matching them.  
   **Explanation:** The question must be able to fail.

---

## Additional Instructor Resources

- Same sanitized bulletin as 2.4.1 / 2.4.2, flattened to an object table
- Escalation: gate → 2.4.1; prose extract → 2.4.2; ATT&CK map → 2.5; author STIX → 3.10; card → 2.2.2
- Next recommended module: Using MITRE ATT&CK for hunt planning (2.5)
