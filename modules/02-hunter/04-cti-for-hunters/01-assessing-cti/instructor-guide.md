# Instructor Guide – Module 2.4.1 – Assessing CTI for Hunting Value

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.4.1 B / C / C · 2.4.1.1 3c / 4c / 4d  
- SOC: 2.4.1 A / B / B · 2.4.1.1 1a / 2b / 3c  
- CTI: 2.4.1 A / B / B · 2.4.1.1 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on identification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach hunters (and secondary SOC/CTI) to assess a CTI report *before* extracting leads: hunt-worthy, awareness-only, or hand off to detections / IR — with a reason. Actionable means question + telemetry + scope.

**Key Teaching Points:**
- Three buckets only. “Interesting” is not a bucket.
- Actionable for a hunt = hunt question + telemetry that could answer it + bounded scope.
- Rapid triage is five passes and a one-sentence why. Not a TTP table.
- Mixed reports can split: hunt this, hand off that, awareness for the rest.
- Stay out of TTP/IOC extract (2.4.2), STIX (2.4.3), ATT&CK mapping (2.5), VT labs (2.3), execute-by-type (2.2.1).

**Common Student Challenges:**
- Hunting every PDF that says APT.
- Calling “high priority” a triage.
- Opening a hunt on an IR-owned hash.
- Dumping the IOC appendix into a hunt.
- Jumping into 2.4.2 extract before the label.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for a four-field triage card (question, telemetry, scope, disposition)
- One sanitized short bulletin and one actor-profile PDF if available (optional)
- Answer key (this guide)

---

## Learning Objectives

1. Sort a CTI report as hunt-worthy, awareness-only, or a hand-off to detections / IR.
2. Rapid-triage a report without extracting every TTP.
3. Say whether the report is actionable for a hunt (question, telemetry, scope).
4. Triage a report: hunt / don’t hunt / hand off, and say why.

**Mapped Items:**
- K: 2.4.1 – Assessing CTI for hunting value
- T: 2.4.1.1 – Triage a CTI report: hunt / don’t hunt / hand off, and say why

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Blank four-field triage card |
| Three dispositions + actionable | 14 min   | Kill “interesting / high” live |
| Rapid triage passes            | 10 min   | Five questions on the board |
| Walkthrough Examples           | 14 min   | Students score each card first |
| Hands-On Exercise              | 15 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 3 min    | |
| **Total**                      | **~68 min** | Stretch Example 3 if the room hunts open IR |

---

## Detailed Teaching Notes

### 1. Three dispositions and “actionable”

**Talking Points:**
- Ask “what would we actually search?” before definitions.
- Hunter 3 is already at principles (B / 3c). Push a label a teammate can use.
- SOC: recognize hunt vs their queue (1a → 2b). CTI: they wrote the report; they still need to see the *hunt* gate (1a → 2b). This is hunter-as-consumer, not CTI production.

**What to emphasize:**
- Question / telemetry / scope. Missing one → not hunt-worthy as written.
- Visibility gap is not “clean.” It is don’t hunt *as written*.

**Questions to ask the class:**
- “What result would kill this story in *our* data?”
- “Who already owns this object?”

### 2. Rapid triage

**Talking Points:**
- Five passes. If they start a TTP table, stop them — that is 2.4.2.
- Mixed reports are the adult case. Force a split in Example 3.
- Do not open ATT&CK Navigator (2.5) or STIX (2.4.3).

**What to emphasize:**
- One sentence why. “High” is not a why.
- Re-triage is allowed when objects appear later.

**Question to ask:**  
“If we only open one hunt this afternoon, which report and why — and what do we refuse?”

### 3. Examples

Work through all three interactively. Students mark disposition before you read the interpretation.

**Extra point for Example 1:**  
Complete hunt-worthy card. Point at question, DNS+TLS, lab exclusion.

**Extra point for Example 2:**  
Same slogan family as 2.2.2 “hunt ransomware.” Here the fail is *no testable question*, not missing Y format.

**Extra point for Example 3:**  
Force the split. Hunting the open IR case is the popular wrong answer.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 12–15 minutes.
- Allow use of the Student Guide.
- Review answers as a group afterward. Do not collect a grade.
- If someone writes a TTP extract or SIEM execute block, thank them and park it for 2.4.2 / 2.2.1. Grade the triage.

**What good answers look like:**

**Summaries:**
- Example 1: Hunt-worthy — question, finance/DNS+TLS/7 days, lab excluded, not owned.
- Example 2: Awareness-only — no object, no question that can fail.
- Example 3: Split — IR/detections hand-off; leftover finance CDN can still be hunt-worthy.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| “APT is active worldwide. Hunt it.” | **Awareness-only** (or **not ready**) | No question / object / scope |
| Bulletin CDN names; finance; DNS+TLS; no analytic | **Hunt-worthy** | Question + telemetry + scope |
| Same hash; IR already contains Building C | **Hand off** | Open incident |
| 400 generic IPs on yesterday’s block list | **Hand off** | Detections / blocking, not a hunt |
| Rare parent/script; process logging; no SOC rule | **Hunt-worthy** | Named behavior, data exists, not owned |
| “High priority CTI” | **Not ready** | Not a reason |

**Triage card (example answer — finance CDN):**  
Question: if finance follows the bulletin CDN names after hours, we should see repeated DNS+TLS from the finance VLAN. Telemetry: DNS/TLS. Scope: finance, 7 days, not lab. Disposition: hunt-worthy — named hosts, data exists, no analytic, no open IR.

Fail the card if disposition has no why, question is a slogan, telemetry is unnamed, scope is unbounded, or they extract a TTP table.

---

## Knowledge Check – Answer Key

1. **What three things must you name before a report is actionable for a hunt?**  
   **Answer:** Hunt question; telemetry that could answer it; bounded scope.  
   **Explanation:** Missing one means it is not hunt-worthy as written.

2. **One reason to mark a report awareness-only?**  
   **Answer (any one):** No named object or rare behavior; no question that can fail; expired / not in theater; context-only actor profile.  
   **Explanation:** Interesting is not a hunt.

3. **One reason to hand off instead of hunt?**  
   **Answer (any one):** Open IR; SOC already owns the queue; high-volume IOC pack for blocking / detections.  
   **Explanation:** Hunters do not re-own incidents or firehose blocklists.

4. **Named host, no DNS or TLS on that VLAN. What then?**  
   **Answer:** Do not hunt it as written. Name the **visibility gap**. Shrink to a population you can see, or park / awareness.  
   **Explanation:** Untestable is not hunt-worthy.

5. **IR owns the hash in Building C; bulletin also lists CDN names with no analytic on finance. What do you do?**  
   **Answer:** Hand off Building C to IR. Hunt-worthy (separately) the finance CDN names if question + DNS/TLS + scope exist.  
   **Explanation:** Mixed reports split. Do not hunt the open incident.

---

## Additional Instructor Resources

- Local CTI intake / hunt charter (sanitize an accepted vs rejected report)
- Escalation: extract leads → 2.4.2; STIX → 2.4.3; ATT&CK → 2.5; tools → 2.3; card → 2.2.2
- Next recommended module: Extracting hunt leads from CTI (2.4.2)
