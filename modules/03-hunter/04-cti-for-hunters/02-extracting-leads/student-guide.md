# Module 2.4.2 – Extracting Hunt Leads from CTI

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.4.2 B / C / C · 2.4.2.1 3c / 4c / 4d · 2.4.2.2 3c / 4c / 4d · 2.4.2.3 3c / 4c / 4d  
- SOC: 2.4.2 A / B / B · 2.4.2.1 1a / 2b / 3c · 2.4.2.2 1a / 2b / 3c · 2.4.2.3 1a / 1a / 2b  
- CTI: 2.4.2 A / B / B · 2.4.2.1 1a / 2b / 3c · 2.4.2.2 1a / 2b / 3c · 2.4.2.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Tell which TTPs, IOCs, and behaviors in a report can drive a hunt.
2. Drop objects that have no telemetry, are expired, or are noise.
3. Record ATT&CK IDs when the report already has them (do not map the hunt here).
4. Extract hunt-suitable TTPs and artifacts, then state the hunt question those leads support.

**Mapped Proficiency Items:**
- K: 2.4.2 – Extracting hunt leads from CTI
- T: 2.4.2.1 – Extract hunt-suitable TTPs from a CTI report
- T: 2.4.2.2 – Extract hunt-suitable artifacts (IOCs, patterns, behaviors)
- T: 2.4.2.3 – State the hunt question those leads support

---

## 1. Key Concepts

### 1.1 TTPs vs IOCs vs behaviors

You extract **after** the **2.4.1** gate. If the report is awareness-only or a full hand-off, stop. Mixed reports: extract only the hunt-worthy slice.

| Kind | What it is | Can drive a hunt when |
|------|------------|------------------------|
| **TTP** | How they work — a technique or procedure you can look for as a *method* | It is specific enough to search (parent/script, scheduled-task class) and you have telemetry for that method |
| **IOC** | A named object — hash, host, IP, URL, email | It is current, rare enough, and you can query that field internally |
| **Behavior** | A pattern over time — repeated after-hours DNS+TLS, new 8443 on a none baseline | It is off-baseline or scoped, not daily admin work |

**Most critical distinction for daily work:**  
Copying the appendix is not extract. A hunt lead is something you can search *internally* that is not already SOC/IR work.

| Keep (hunt-suitable) | Drop |
|----------------------|------|
| Bulletin installer hash (public, current) | Hash from a 2019 annex with no reuse note |
| Lookalike CDN hostname | “Any outbound 443” / the vendor’s whole CDN ASN |
| Rare `wscript.exe` + named script | Technique nickname only: “they use persistence” |
| After-hours repeated DNS+TLS to those names | 400 generic VPS IPs already on yesterday’s block list |
| Report lists **T1053.005** next to the task procedure | Inventing ATT&CK IDs the report never used (**2.5**) |

**Record ATT&CK IDs if the report has them.** Copy the ID next to the lead. Do **not** open Navigator, score coverage, or prioritize by tactic — that is **2.5**. If the report has no IDs, write “none given.” Do not guess.

How a STIX bundle encodes the same objects is **2.4.3**. Full hunt-card format is **2.2.2**. Tool pivots are **2.3**. Persistence how-to is **2.6**. Stay here: extract and name the question.

### 1.2 What to drop, and the hunt question

Drop before you write the question.

| Drop if | Why |
|---------|-----|
| **No telemetry** | You cannot test it. Name the **visibility gap**. Do not extract it as a hunt lead |
| **Expired IOC** | Old hash/host with no “still in use” note. Awareness or detections history, not a hunt |
| **Noise** | Daily traffic, shared CDN/ASN, already-blocked firehose, slogan TTP |

A leftover after the drop list must support **one hunt question** — a testable if/then, even one line. That is **2.4.2.3**. You are not writing the full four-field card unless the question needs a scope hook.

| Extract (good) | Question it supports |
|----------------|----------------------|
| CDN names + after-hours repeated DNS+TLS | If finance follows those names after hours, we should see repeated DNS+TLS from the finance VLAN |
| New SYSTEM task procedure + 30-day none baseline | If Building C servers add new SYSTEM tasks after 02:00, we should see task-create on that class |
| Hash only, no behavior | If the bulletin installer ran here, we should see that hash on endpoints with EDR |

If the leftovers cannot form a question that can fail, you extracted noise. Re-drop.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Keep TTP + IOC + behavior)

**Input:** Hunt-worthy bulletin (**2.4.1** already passed). Finance in scope. DNS+TLS exist. Lab has no DNS. Report lists lookalike CDN names, installer hash, “scheduled tasks” as a one-line aside, and **T1071.001** next to the CDN C2 paragraph. No open IR.

**Extract card**

| Field | What they wrote |
|-------|-----------------|
| TTPs kept | C2 over HTTPS to named lookalike update CDNs (report’s procedure). **T1071.001** recorded as given |
| Artifacts kept | Installer hash; the CDN hostnames; after-hours repeated DNS+TLS from finance |
| Dropped | “Scheduled tasks” aside — no procedure, no host class; lab (no DNS) is a visibility gap, not a lead |
| Hunt question | If finance laptops follow the bulletin CDN names after hours, we should see repeated DNS+TLS from the finance VLAN (hash is a second EDR question) |

**Interpretation:**  
This is extract. TTPs vs IOCs vs behavior are named. ATT&CK ID is copied, not mapped. The question can fail. You have not authored STIX (**2.4.3**) or ranked coverage (**2.5**).

### Example 2: Appendix Firehose (Lead)

A hunt channel paste:

> Extracted leads: all 400 IPs, every hash in Annex B (2019), “persistence,” hunt the enterprise.

Compare a documented extract from the same PDF:

> Kept: two CDN names still listed as current; parent `wscript.exe` + rare script from the *current* procedure. Dropped: 2019 annex hashes (expired); 400 VPS IPs (noise / already blocked); “persistence” (slogan, no method). ATT&CK: none given. Question: if Building C workstations run that parent+script, we should see process-create on hosts with process logging in 24 hours.

**Interpretation:**  
The first paste is not extract. Expired + noise + slogan cannot support a hunt question. The second is **2.4.2.1**–**2.4.2.3**.

### Example 3: No Telemetry vs Invented ATT&CK (Lead)

**Write-up A**

> TTP: registry Run keys. We don’t have registry logging. Mapped to T1547.001 anyway so we can hunt it. Question: hunt persistence.

**Write-up B**

> Drop the Run-key TTP — **no telemetry** (visibility gap). Do not invent **T1547.001**; the report never listed it. Kept: the report’s current hostname. Question: if that host was used here, we should see DNS `query` or TLS `server_name` = that name; finance; 7 days.

**Interpretation:**  
A hunts a gap and fabricates an ID. B drops what cannot be tested and only records IDs the report printed. Mapping and coverage ranking stay in **2.5**.

---

## 3. Hands-On Exercise

**Objective:** Practice keeping hunt-suitable TTPs and artifacts, dropping the rest, and stating the question.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (extracted, or not, and why).
2. For each item below, say **keep (TTP)**, **keep (artifact / behavior)**, **drop**, **record ATT&CK**, or **not a hunt question**. Give one reason.
   - Lookalike CDN hostname from this week’s bulletin
   - 400 generic VPS IPs already on yesterday’s block list
   - “They use persistence”
   - After-hours repeated DNS+TLS to the bulletin names
   - Report prints **T1071.001** next to the CDN paragraph
   - “Hunt ransomware”
3. Write **one extract card** (small table or four sentences): TTPs kept, artifacts/behaviors kept, what you dropped, hunt question. Use the finance CDN bulletin *or* the parent+script leftover. Do not triage from scratch (assume **2.4.1** already said hunt-worthy). Do not map ATT&CK. Do not execute a SIEM search.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- One card that keeps searchable leads, drops noise/expired/no-telemetry, records IDs only if given, and states a question that can fail

---

## 4. Knowledge Check

1. When can a TTP drive a hunt, versus an IOC, versus a behavior?
2. Give one reason to **drop** an object from a report.
3. The report lists **T1053.005** next to a scheduled-task procedure. What do you do with that ID in this lesson?
4. You extract a Run-key TTP but have no registry logging. Keep or drop? Why?
5. Write one hunt question that two leftover CDN names could support.

---

## 5. Summary

- Extract only after the **2.4.1** gate, and only the hunt-worthy slice.
- TTPs, IOCs, and behaviors can all drive a hunt when they are searchable and not daily noise.
- Drop no-telemetry, expired IOCs, and noise before you write the question.
- Record ATT&CK IDs the report already printed. Do not invent or map them here (**2.5**).
- Every kept set must support a hunt question that can fail.
- Next: STIX as hunt input (**2.4.3**).

---

## 6. References & Further Reading

- Related modules:
  - 2.4.1 – Assessing CTI for hunting value
  - 2.4.3 – STIX as hunt input (next)
  - 2.2.2 – Hunt development concepts
  - 2.5 – ATT&CK for hunt planning (later)
- Local CTI report / bulletin used in class (sanitize)
