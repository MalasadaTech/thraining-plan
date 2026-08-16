# Instructor Guide – Module 2.4.2 – Extracting Hunt Leads from CTI

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.4.2 B / C / C · 2.4.2.1 3c / 4c / 4d · 2.4.2.2 3c / 4c / 4d · 2.4.2.3 3c / 4c / 4d  
- SOC: 2.4.2 A / B / B · 2.4.2.1 1a / 2b / 3c · 2.4.2.2 1a / 2b / 3c · 2.4.2.3 1a / 1a / 2b  
- CTI: 2.4.2 A / B / B · 2.4.2.1 1a / 2b / 3c · 2.4.2.2 1a / 2b / 3c · 2.4.2.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on identification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach hunters to pull hunt-suitable TTPs and artifacts from a report that already passed the 2.4.1 gate, drop what cannot be hunted, copy ATT&CK IDs only when printed, and state the hunt question the leftovers support.

**Key Teaching Points:**
- TTP vs IOC vs behavior — each can drive a hunt when searchable.
- Drop: no telemetry, expired IOCs, noise. Dropping is the skill.
- Record printed ATT&CK IDs. Do not invent or map (2.5).
- Kept leads must support one question that can fail (2.4.2.3).
- Stay out of triage-from-scratch (2.4.1), STIX (2.4.3), Navigator (2.5), tool labs (2.3), execute (2.2.1).

**Common Student Challenges:**
- Copying the entire annex.
- Keeping slogan TTPs (“persistence”).
- Inventing technique IDs so the card looks complete.
- Extracting a gap (no registry logs) as a lead.
- Writing “hunt ransomware” as the question.
- Re-doing 2.4.1 labels instead of extracting.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for an extract card (kept TTPs / kept artifacts / dropped / question)
- Same sanitized bulletin used in 2.4.1 if available
- Answer key (this guide)

---

## Learning Objectives

1. Tell which TTPs, IOCs, and behaviors in a report can drive a hunt.
2. Drop objects that have no telemetry, are expired, or are noise.
3. Record ATT&CK IDs when the report already has them (do not map the hunt here).
4. Extract hunt-suitable TTPs and artifacts, then state the hunt question those leads support.

**Mapped Items:**
- K: 2.4.2 – Extracting hunt leads from CTI
- T: 2.4.2.1 – Extract hunt-suitable TTPs from a CTI report
- T: 2.4.2.2 – Extract hunt-suitable artifacts (IOCs, patterns, behaviors)
- T: 2.4.2.3 – State the hunt question those leads support

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Assume 2.4.1 already said hunt-worthy |
| TTP vs IOC vs behavior         | 12 min   | Three columns on the board |
| Drop list + ATT&CK copy        | 10 min   | Kill annex firehose and invented IDs |
| Walkthrough Examples           | 14 min   | Students score each card first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~68 min** | Stretch Example 2 if they still keep all 400 IPs |

---

## Detailed Teaching Notes

### 1. TTP vs IOC vs behavior

**Talking Points:**
- Ask for one object from last week’s bulletin before definitions. Sort it live.
- Hunter 3 is already at principles (B / 3c). Push a short extract a teammate can hunt.
- SOC: recognize keep vs dump (1a → 2b). CTI: they authored the report; they still owe *hunt-shaped* leftovers (1a → 2b). 2.4.2.3 is lighter for SOC/CTI (1a / 1a / 2b).

**What to emphasize:**
- Method / object / pattern. Slogan names are not TTPs.
- Same unique-pattern bar as 2.2.2. Do not rewrite the full card.

**Questions to ask the class:**
- “Would this query return half the company?”
- “Did the report actually print that ATT&CK ID?”

### 2. Drop list and the question

**Talking Points:**
- Three drop reasons only: no telemetry, expired, noise.
- Visibility gap = drop as a hunt lead, not “hunt harder.”
- Question is one if/then. Full card is 2.2.2.

**What to emphasize:**
- “None given” is a legal ATT&CK answer.
- If leftovers cannot form a question, re-drop.

**Question to ask:**  
“If we can keep only two lines from this PDF, which two — and what question do they support?”

### 3. Examples

Work through all three interactively. Students mark extracted vs not before you read the interpretation.

**Extra point for Example 1:**  
Complete extract. Point at recorded T1071.001 and the dropped “scheduled tasks” aside.

**Extra point for Example 2:**  
Same firehose family as 2.4.1 Example 3 write-up A. Here the fix is *drop*, not the disposition label.

**Extra point for Example 3:**  
Invented T1547.001 will be popular. Force: if the report did not print it, you do not record it.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 14–16 minutes.
- Allow use of the Student Guide.
- Tell them 2.4.1 already passed. Do not grade a re-triage.
- Review as a group. Do not collect a grade.
- Park STIX bundles, Navigator screenshots, and SIEM execute blocks.

**What good answers look like:**

**Summaries:**
- Example 1: Extracted — CDN procedure + hash + after-hours behavior; tasks aside dropped; T1071.001 copied; question can fail.
- Example 2: First paste not extract (annex + slogan); second keeps current names/script and drops expired/noise.
- Example 3: A hunts a gap and invents an ID; B drops Run keys and keeps the hostname.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Lookalike CDN hostname from this week’s bulletin | **Keep (artifact)** | Current named object |
| 400 generic VPS IPs already blocked | **Drop** | Noise |
| “They use persistence” | **Drop** | Slogan, not a TTP |
| After-hours repeated DNS+TLS to bulletin names | **Keep (artifact / behavior)** | Searchable pattern |
| Report prints **T1071.001** next to the CDN paragraph | **Record ATT&CK** | Printed, not invented |
| “Hunt ransomware” | **Not a hunt question** | Cannot fail |

**Extract card (example answer — finance CDN):**  
TTPs kept: C2 over HTTPS to named lookalike CDNs (T1071.001 as printed). Artifacts: hash + CDN names + after-hours DNS+TLS. Dropped: task aside; lab (no DNS). Question: if finance follows those names after hours, we should see repeated DNS+TLS from the finance VLAN.

Fail the card if they keep the annex, invent an ATT&CK ID, extract a no-telemetry TTP, or the question is a slogan.

---

## Knowledge Check – Answer Key

1. **When can a TTP / IOC / behavior drive a hunt?**  
   **Answer:** TTP — specific method plus telemetry for that method. IOC — current named object you can query. Behavior — scoped or off-baseline pattern, not daily work.  
   **Explanation:** Kind alone does not make it hunt-suitable.

2. **One reason to drop an object?**  
   **Answer (any one):** No telemetry; expired IOC; noise (blocked firehose, slogan, shared CDN/ASN).  
   **Explanation:** Dropping is required before the question.

3. **Report lists T1053.005 next to a scheduled-task procedure. What do you do with the ID here?**  
   **Answer:** Copy it next to that lead. Do not map coverage or invent siblings.  
   **Explanation:** Mapping hunts is 2.5.

4. **Run-key TTP, no registry logging. Keep or drop?**  
   **Answer:** Drop as a hunt lead. Name the visibility gap.  
   **Explanation:** Untestable is not extracted.

5. **One hunt question two leftover CDN names could support?**  
   **Answer (equivalent):** If [population] talks to those names [window], we should see DNS `query` or TLS `server_name` matching them.  
   **Explanation:** The question must be able to fail.

---

## Additional Instructor Resources

- Same sanitized bulletin as 2.4.1
- Escalation: gate → 2.4.1; STIX → 2.4.3; ATT&CK map → 2.5; card → 2.2.2
- Next recommended module: STIX as hunt input (2.4.3)
