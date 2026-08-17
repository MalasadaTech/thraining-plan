# Instructor Guide – Module 2.3.1 – Tool Capabilities for Hunting

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.3.1 B / C / C · 2.3.1.1 3c / 4c / 4d · 2.3.1.2 3c / 4c / 4d · 2.3.1.3 3c / 4c / 4d  
- SOC: 2.3.1 A / B / B · 2.3.1.1 1a / 2b / 3c · 2.3.1.2 1a / 2b / 3c · 2.3.1.3 1a / 2b / 3c  
- CTI: 2.3.1 A / B / B · 2.3.1.1 2b / 3c / 4c · 2.3.1.2 2b / 3c / 4c · 2.3.1.3 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on identification

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach what the four enrichment tools can and cannot do for a hunt, how to pivot on named objects, how to pull a lead, and how to write a precise internal query. Public scores are not incidents.

**Key Teaching Points:**
- VT / AnyRun / URLScan / Silent Push each have one hunting job and one hard limit.
- Pivot = follow named objects. A detection count is not a pivot.
- Lead = internally searchable and not daily traffic.
- Convert = data, field, object, window, population.
- Stay out of CTI report extract (2.4), ATT&CK rank (2.5), persistence how-to (2.6), and full execute-by-type drills (2.2.1).

**Common Student Challenges:**
- Treating 12/72 or a red banner as “we are hit.”
- Uploading a private sample to a public tool.
- Writing “any 443” or “the whole ASN” as the internal query.
- Stealing C2 from an AnyRun task that is not their hash.
- Re-teaching the 2.2.2 card instead of the enrichment chain.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard for a four-field enrichment card (start → pivot → lead → query)
- Sanitized *already-public* screenshots if available (optional). No live private upload.
- Answer key (this guide)

---

## Learning Objectives

1. State what VirusTotal, AnyRun, URLScan, and Silent Push are good for in a hunt — and what they cannot prove.
2. Query and pivot across those four tools without treating a public score as an internal hit.
3. Extract an actionable hunting lead from an external result.
4. Convert that lead into a precise internal SIEM or Zeek query.

**Mapped Items:**
- K: 2.3.1 – Tool capabilities for hunting
- T: 2.3.1.1 – Perform advanced querying and pivoting in VirusTotal, AnyRun, URLScan, and Silent Push
- T: 2.3.1.2 – Extract actionable hunting leads from external tool results
- T: 2.3.1.3 – Convert external findings into precise internal SIEM or Zeek queries

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Blank four-field enrichment card |
| Four tools: strengths / limits | 14 min   | One limit per tool on the board |
| Pivot, lead, internal query    | 10 min   | Kill scores and banners live |
| Walkthrough Examples           | 14 min   | Students score each card first |
| Hands-On Exercise              | 15 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 3 min    | |
| **Total**                      | **~68 min** | Stretch Example 3 if the room still queries the ASN |

---

## Detailed Teaching Notes

### 1. Four tools

**Talking Points:**
- Ask “what does a VT score prove about *our* network?” before the table.
- Hunter 3 is already at principles (B / 3c). Push a chain they could hand a teammate.
- SOC: recognize a usable chain vs a score (1a → 2b). CTI: they often seed the object; they still owe hunt-shaped output (2b → 3c). 2.3.1.3 stays lighter for CTI (1a / 2b / 3c).

**What to emphasize:**
- Do not upload private samples. Use already-public objects or instructor screenshots.
- URLScan scanner path ≠ victim path. Silent Push coverage ≠ your DNS.

**Questions to ask the class:**
- “What object did you actually copy out of the tool?”
- “Would this internal query return half the company on a Tuesday?”

### 2. Pivot, lead, query

**Talking Points:**
- Three boxes: pivot / lead / query. If the middle box is a banner, the hunt is not ready.
- Reuse unique-pattern language from 2.2.2. Do not re-teach the full card.
- Do not open ATT&CK matrices (2.5) or STIX (2.4).

**What to emphasize:**
- Visibility gaps shrink the query; they do not get a “clean” stamp.
- Wrong-object pivots (someone else’s AnyRun task) are discarded.

**Question to ask:**  
“If we only have time to run one internal query this afternoon, which object and why?”

### 3. Examples

Work through all three interactively. Students mark converted vs not before you read the interpretation.

**Extra point for Example 1:**  
Complete chain. Point at Relations host, lab exclusion, and “score is not a hit.”

**Extra point for Example 2:**  
Same slogan family as 2.2.2 Example 3 write-up A (“any 443”). Here the fix is the *extract*, not the hunt type.

**Extra point for Example 3:**  
ASN queries will be popular. Force: shared infra is not unique.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 12–15 minutes.
- Allow use of the Student Guide.
- No live private upload. Screenshots of public objects are enough.
- Review answers as a group afterward. Do not collect a grade.
- If someone writes a full 2.2.1 execute block or a 2.4 TTP list, thank them and park it. Grade the enrichment card.

**What good answers look like:**

**Summaries:**
- Example 1: Converted — public VT relations host, URLScan/Silent Push agree, DNS/TLS query bounded, lab excluded.
- Example 2: First paste not ready (banner + any 443); second is a named-object extract.
- Example 3: A is an ASN / any-443 miss; B keeps the hostname list.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| “VirusTotal 12/72 — hunt it” | **Not ready** | Score, no object / no query |
| VT Relations contacted host = bulletin CDN name | **Usable pivot** (and can be the lead) | Named object |
| “AnyRun said malicious, so we are breached” | **Not ready** | Banner ≠ presence |
| `dns.query` = bulletin CDN name; finance VLAN; last 7 days | **Precise internal query** | Field, object, population, window |
| “Outbound 443 to the Silent Push ASN” | **Not ready** | Daily / shared infra |
| URLScan requested-host list as next VT/Silent Push objects | **Usable pivot** | Named hosts to follow |

**Enrichment card (example answer — bulletin host):**  
Start: public bulletin hash. Pivot: VT Relations → lookalike CDN name; URLScan requested hosts agree; Silent Push first-seen, not a CDN apex cluster. Lead: that hostname (hash is a second EDR lead). Query: `dns.query` or TLS `server_name` = that name; finance VLAN; 7 days; not lab.

Fail the card if the only input is a score, the query is unbounded or “any 443,” they uploaded a private sample, or they claimed an incident.

---

## Knowledge Check – Answer Key

1. **One VT strength and one limit for hunting?**  
   **Answer (strength, any one):** Relations / multi-engine file view / contacted hosts / similar samples. **Limit (any one):** upload leak; private samples missing; detection count ≠ it ran here; comments are not CTI.  
   **Explanation:** VT is a pivot surface, not a sensor.

2. **Why is an AnyRun “malicious” banner not an internal hit?**  
   **Answer:** It is one sandbox opinion on one run. It does not say the sample executed on *your* hosts.  
   **Explanation:** Extract hosts / files / command lines from *your* object, then query internally.

3. **What makes an external finding an actionable hunting lead?**  
   **Answer:** A named object or rare behavior you can search internally that is not daily traffic.  
   **Explanation:** Same bar as unique patterns (2.2.2). Scores and ASN-wide 443 fail.

4. **Convert a contacted hostname. Which fields / bounds?**  
   **Answer:** Data source (DNS and/or TLS), field (`query` / `server_name`), the hostname, time window, population (and exclusions).  
   **Explanation:** “Hunt the domain” is not converted.

5. **Silent Push shows the name on a huge CDN ASN. What do you not query, and what instead?**  
   **Answer:** Do **not** query the ASN / any 443 to that ASN. Pivot for the hostname (and listed lookalikes) on VT/URLScan; query those names in your DNS/TLS. Park if you only have the ASN.  
   **Explanation:** Shared infra is not a unique pattern.

---

## Additional Instructor Resources

- Local acceptable-use for public sandboxes and sample handling
- Escalation: hunt card → 2.2.2; execute → 2.2.1; CTI extract → 2.4; ATT&CK → 2.5
- Next recommended module: CTI for hunters (2.4)
