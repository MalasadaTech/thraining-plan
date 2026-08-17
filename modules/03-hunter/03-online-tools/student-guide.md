# Module 2.3.1 – Tool Capabilities for Hunting

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.3.1 B / C / C · 2.3.1.1 3c / 4c / 4d · 2.3.1.2 3c / 4c / 4d · 2.3.1.3 3c / 4c / 4d  
- SOC: 2.3.1 A / B / B · 2.3.1.1 1a / 2b / 3c · 2.3.1.2 1a / 2b / 3c · 2.3.1.3 1a / 2b / 3c  
- CTI: 2.3.1 A / B / B · 2.3.1.1 2b / 3c / 4c · 2.3.1.2 2b / 3c / 4c · 2.3.1.3 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. State what VirusTotal, AnyRun, URLScan, and Silent Push are good for in a hunt — and what they cannot prove.
2. Query and pivot across those four tools without treating a public score as an internal hit.
3. Extract an actionable hunting lead from an external result.
4. Convert that lead into a precise internal SIEM or Zeek query.

**Mapped Proficiency Items:**
- K: 2.3.1 – Tool capabilities for hunting
- T: 2.3.1.1 – Perform advanced querying and pivoting in VirusTotal, AnyRun, URLScan, and Silent Push
- T: 2.3.1.2 – Extract actionable hunting leads from external tool results
- T: 2.3.1.3 – Convert external findings into precise internal SIEM or Zeek queries

---

## 1. Key Concepts

### 1.1 Four tools: strengths and limits

These tools **enrich** a hunt. They do not replace your logs. A public “malicious” label is not an incident. A score is not presence on your network.

| Tool | Strength for hunting | Limit for hunting |
|------|----------------------|-------------------|
| **VirusTotal** | File / URL / domain / IP views; multi-engine detections; **Relations** (contacted hosts, dropped files, similar samples); submission history | Public upload can leak an operation. Private malware may be missing or late. Detection count ≠ it ran here. Comments are not a CTI product (**2.4**) |
| **AnyRun** | Interactive sandbox: process tree, command line, files written, hosts contacted on *that* run | One VM, one run. Sandbox-aware malware stays quiet. A public task can leak the sample. “Malicious” is the sandbox opinion, not your estate |
| **URLScan** | Page snapshot: redirects, requested hosts, DOM clues, similar scans, screenshot | Scanner geo / IP ≠ the victim. Kits rotate. Do not treat the scanner’s resolver path as attacker infra. One scan is one moment |
| **Silent Push** | Passive DNS and infra clustering; newly observed names; “who else resolved this” style pivots | Coverage is not your DNS. Shared hosting and CDNs create false friends. A shared ASN is not a unique pattern |

**Most critical distinction for daily work:**  
External tools answer “what else is known about this object?” Internal queries answer “did *we* see it?” You owe both, in that order, before you claim a hit.

How to extract TTPs from a full CTI report is **2.4**. ATT&CK coverage ranking is **2.5**. Hunt *type* and first execute move are **2.2.1**. Writing the if/then card is **2.2.2**. Do not pull those lessons in here.

### 1.2 Pivot, lead, internal query

**Advanced query / pivot** means you do not stop at the first hash or URL. You follow *named objects* the tool already linked.

| Start | Typical next hop | Stop if |
|-------|------------------|---------|
| Hash on VT | Contacted hosts, dropped files, similar samples | You only have a score and no object |
| Public AnyRun task | Hosts / files / command lines *from that run* | The only takeaway is the red banner |
| URL on URLScan | Redirect chain, requested hostnames, similar scans | You copy the scanner IP as C2 |
| Name or IP on Silent Push | First-seen, related names, infra cluster | The cluster is “the whole CDN” |

**Actionable hunting lead** = a named object or rare behavior you can search *internally*, with a reason it is not daily traffic. Same bar as unique patterns in **2.2.2**.

| Actionable lead | Not a lead (yet) |
|-----------------|------------------|
| Bulletin installer hash | “VirusTotal says 12/72” |
| Lookalike CDN hostname from VT Relations | “Any outbound 443” |
| Parent process + command line from an AnyRun run of *that* hash | “Sandbox said malicious, we are breached” |
| First-seen lookalike name in Silent Push that you can query in DNS | “Same ASN as a major CDN” |

**Convert to an internal query** means you name the data source, the field, the object, the window, and the population. If you have no DNS for that VLAN, say so — that is a **visibility gap**, not a quiet hunt.

| External finding | Precise internal shape (pseudo) |
|------------------|----------------------------------|
| VT contacted host `upd-fin-cdn.net` | DNS `query` = that name; finance VLAN; last 7 days |
| Same host on TLS | TLS `server_name` = that name; same VLAN / window |
| Hash from the bulletin | EDR / file log hash = that value; workstations; 7 days |
| AnyRun parent `wscript.exe` + rare script name | Process create where parent and script match; Building C; 24 hours vs 30-day baseline |

A query that says “hunt VirusTotal” or “any 443” is not converted. Changing the object mid-pivot is allowed if you write the new object.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Hash → host → internal DNS/TLS)

**Input:** This week’s bulletin lists an installer hash. Finance is in program scope. You have DNS and TLS in the SIEM. Lab has no DNS. You will not upload the hash if it is not already public.

**Enrichment card**

| Field | What they wrote |
|-------|-----------------|
| Query / pivot | VT file view (already public) → Relations → contacted host = bulletin lookalike CDN name. URLScan of that host shows a redirect to the same name. Silent Push: name is newly observed; not a giant CDN cluster |
| Lead | That hostname (not the VT score). Rare enough to search. Hash remains a second lead for EDR |
| Internal query | `dns.query` = that name OR TLS `server_name` = that name; finance VLAN; 7 days; **not lab** |
| Kill / not a hit | No matching DNS/TLS in finance for 7 days. Lab is a visibility gap, not quiet. VT detections alone are not a hit |

**Interpretation:**  
This is enrichment done. Pivot used named objects. The lead can fail internally. The query names fields, population, and window. You have not executed the 14-day hunt yet (**2.2.1**) and you have not written the full if/then card as the lesson (**2.2.2**) — but the query is precise enough to drop onto that card.

### Example 2: Sandbox Banner (Lead)

A hunt channel paste:

> AnyRun public task: malicious. Hunt all 443. Priority: incident.

Compare a documented enrichment from the same paste:

> Pivot: AnyRun network tab for *this* bulletin hash lists `upd-fin-cdn.net` and a rare script name under `wscript.exe`. Lead: that host + parent/script pair. Not a lead: the red banner, or “any 443.” Internal: DNS/TLS for the host (finance, 7 days); process-create for parent+script on endpoints with process logging (24 hours). Public task already existed — we did not re-upload.

**Interpretation:**  
The first paste is not enrichment. A sandbox verdict is not presence. “Any 443” is daily traffic. The second extract is **2.3.1.2** and **2.3.1.3**. If the public task is *not* your hash, do not steal its C2 list — wrong object.

### Example 3: Shared Infra (Lead)

**Write-up A**

> Silent Push: lookalike name shares an ASN with a major CDN. Unique behavior: outbound 443 to that ASN. Hunt the enterprise.

**Write-up B**

> Silent Push: name first seen recently; cluster mates are other lookalikes, not the CDN apex. Lead: the hostname (and close lookalikes you can list). Internal: DNS `query` in (those names); 7 days; finance first. Not a query: the ASN. VT/URLScan agree the name is the object, not the CDN.

**Interpretation:**  
A converts a coverage-biased cluster into daily traffic. B keeps the object small enough to search. If Silent Push only gives you the ASN and no hostname, you do not have a converted query yet — pivot on VT/URLScan or park it.

---

## 3. Hands-On Exercise

**Objective:** Practice pivoting, naming a lead, and writing an internal query — without treating a public score as a hit.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (converted, or not, and why).
2. For each item below, say whether it is a **usable pivot**, an **actionable lead**, a **precise internal query**, or **not ready**. Give one reason.
   - “VirusTotal 12/72 — hunt it”
   - VT Relations contacted host = the bulletin CDN name
   - “AnyRun said malicious, so we are breached”
   - `dns.query` = bulletin CDN name; finance VLAN; last 7 days
   - “Outbound 443 to the Silent Push ASN”
   - URLScan requested-host list used as the next VT/Silent Push objects
3. Write **one enrichment card** (four sentences or a small table): start object, pivot, lead, internal SIEM/Zeek-style query. Use the bulletin hash or the lookalike CDN name. Do not claim an incident. Do not upload a private sample in class.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- One card that pivots on a named object, names a lead that can fail internally, and specifies data / field / window / population

---

## 4. Knowledge Check

1. Give one hunting strength and one hunting limit for VirusTotal.
2. Why is an AnyRun “malicious” banner not an internal hit?
3. What makes an external finding an actionable hunting lead?
4. Convert a contacted hostname into a precise internal query. Which fields / bounds must you name?
5. Silent Push shows your name on a huge CDN ASN. What do you *not* query, and what do you try instead?

---

## 5. Summary

- Four tools, four jobs: VT relations, AnyRun run artifacts, URLScan page graph, Silent Push infra — each with a hard limit.
- Pivot on named objects. Stop when you only have a score or a banner.
- A lead is searchable internally and not daily traffic.
- Convert means data + field + object + window + population. Visibility gaps shrink the query; they do not get a “clean” stamp.
- Cards and execute-by-type remain **2.2**. Next unit is CTI for hunters (**2.4**).

---

## 6. References & Further Reading

- Related modules:
  - 2.2.2 – Hunt development concepts
  - 2.2.1 – Hunt types
  - 2.4 – CTI for hunters (next)
  - 1.2.2 / 1.2.3 / 1.2.4 – Zeek conn / DNS / TLS fields
- Local acceptable-use rules for public sandboxes and sample upload (when published)
