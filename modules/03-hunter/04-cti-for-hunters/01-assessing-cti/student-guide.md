# Module 2.4.1 – Assessing CTI for Hunting Value

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.4.1 B / C / C · 2.4.1.1 3c / 4c / 4d  
- SOC: 2.4.1 A / B / B · 2.4.1.1 1a / 2b / 3c  
- CTI: 2.4.1 A / B / B · 2.4.1.1 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Sort a CTI report as hunt-worthy, awareness-only, or a hand-off to detections / IR.
2. Rapid-triage a report without extracting every TTP.
3. Say whether the report is actionable for a hunt (question, telemetry, scope).
4. Triage a report: hunt / don’t hunt / hand off, and say why.

**Mapped Proficiency Items:**
- K: 2.4.1 – Assessing CTI for hunting value
- T: 2.4.1.1 – Triage a CTI report: hunt / don’t hunt / hand off, and say why

---

## 1. Key Concepts

### 1.1 Hunt-worthy vs awareness-only vs hand-off

You are a **consumer** of CTI. This lesson is the gate: do we hunt, do we only read, or does someone else own it? Extracting the lead list is **2.4.2**. STIX objects are **2.4.3**. ATT&CK coverage is **2.5**.

| Disposition | What it means | Typical reason |
|-------------|----------------|----------------|
| **Hunt-worthy** | You can write a hunt question, you have (or can name) telemetry that could answer it, and you can bound scope | Named objects or a rare behavior; not already owned by SOC/IR; data exists for the population |
| **Awareness-only** | Useful context. No hunt this week | No question you can test; no objects; expired or unscoped story; “APT exists” |
| **Hand off** | Not a hunt. Give it to detections or IR | Already an incident; high-volume IOC pack for blocking; queue SOC already owns |

**Most critical distinction for daily work:**  
“Interesting report” is not a hunt. A report is **actionable for a hunt** only when you can name three things:

| Must name | Why |
|-----------|-----|
| **Hunt question** | What you would test (even a one-line if/then). Full card writing is **2.2.2** |
| **Telemetry** | Which logs or sensors could answer it. If none, that is a **visibility gap**, not a hunt |
| **Scope** | Who / where / how long you would claim. “Whole enterprise, all time” fails |

A public VirusTotal score is still not presence (**2.3**). A glossy actor profile with no objects is awareness. An IR ticket already in progress is a hand-off, even if the PDF is excellent.

### 1.2 Rapid triage of a report

Do this **before** you extract TTPs.

| Pass | Ask | If no |
|------|-----|-------|
| 1. Fresh and in theater? | Date, victim class, sector, geo — does it touch *us*? | Awareness, or park |
| 2. Named thing or rare behavior? | Hash, host, parent/script, off-baseline behavior you could search | Awareness |
| 3. Can we see it? | DNS, TLS, EDR, process logs for that population | Visibility gap — don’t hunt it as written |
| 4. Already owned? | SOC analytic, block list, open IR | Hand off |
| 5. Disposition | Hunt / don’t hunt (awareness) / hand off + **one sentence why** | You are not done |

Rapid triage is a **label and a reason**, not a TTP table. If you start copying every MITRE ID, you have left this lesson.

| Weak triage | Documented triage |
|-------------|-------------------|
| Hunt it, looks bad | **Awareness-only** — no named object, no telemetry hook, no scope |
| High priority | **Hand off to IR** — Building C incident already open on the same hash |
| Hunt ransomware | **Hunt-worthy** — bulletin installer hash + lookalike CDN; finance VLAN; DNS+TLS exist; no analytic |

You may later extract leads (**2.4.2**) only from reports you marked hunt-worthy. Mixed reports are allowed: hunt *this* section, hand off *that* IOC pack, awareness for the actor history.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Hunt-worthy)

**Input:** This week’s bulletin. Finance is in program scope. DNS and TLS are in the SIEM. Lab has no DNS. No SOC analytic on the lookalike CDN names. No open IR.

**Triage card**

| Field | What they wrote |
|-------|-----------------|
| Question | If finance laptops follow the bulletin CDN names after hours, we should see repeated DNS + TLS from the finance VLAN |
| Telemetry | DNS `query` and TLS `server_name`; finance VLAN. Lab has no DNS |
| Scope | Finance workstations; 7 days; **not lab** |
| Disposition | **Hunt-worthy** |
| Why | Named hosts, data exists, not owned by SOC/IR. Lab is a visibility gap, not a hunt |

**Interpretation:**  
This is assessing CTI. The report can become a hunt because question + telemetry + scope are present. You have not extracted the full TTP list (**2.4.2**) and you have not executed the search (**2.2.1**).

### Example 2: Awareness-only (Lead)

A hunt channel paste:

> New vendor report: “APT group still active worldwide.” Hunt it. High.

Compare a documented triage:

> **Awareness-only.** No named hash, host, or rare behavior we can search. No hunt question that can fail. No telemetry hook. Share the actor name with the team; do not open a hunt. If CTI later adds objects, re-triage.

**Interpretation:**  
The first paste is not a triage. “Worldwide” is not scope. A threat-actor slogan is not actionable for a hunt. Re-triage if the same PDF later includes objects — that is still this skill, not extract-everything.

### Example 3: Hand-off vs Hunt (Lead)

**Write-up A**

> Same bulletin hash. IR already contains Building C. Hunt the enterprise for ransomware. Also dump all 400 IOCs into a hunt.

**Write-up B**

> **Hand off to IR** for Building C — incident already open; hunters do not re-own it. **Hand off to detections** the high-volume blocklist IOCs (already yesterday’s SOC feed). **Hunt-worthy** only if unalerted *peers* or a *different* VLAN (finance) still have no analytic on the CDN names — then bound that hunt. Do not hunt the open incident.

**Interpretation:**  
A mixes IR, blocking, and hunting. B splits the report. Open IR is a hand-off. A firehose IOC pack is detections work. A leftover named object with telemetry and no owner can still be hunt-worthy. Extracting the leftover objects is **2.4.2**.

---

## 3. Hands-On Exercise

**Objective:** Practice labeling reports hunt-worthy, awareness-only, or hand-off — with a reason.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (disposition, and why).
2. For each item below, say **hunt-worthy**, **awareness-only**, **hand off**, or **not ready**. Give one reason.
   - “APT is active worldwide. Hunt it.”
   - Bulletin CDN names; finance in scope; DNS+TLS exist; no analytic
   - Same hash; IR already contains Building C
   - 400 generic IPs already on yesterday’s block list
   - Report names a rare parent/script pair; you have process logging on that class; no SOC rule
   - “High priority CTI”
3. Write **one triage card** (four sentences or a small table): question, telemetry, scope, disposition + why. Use either the finance CDN bulletin or the “APT worldwide” paste. Do not extract a TTP table. Do not write a SIEM execute block.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- One card that names question, telemetry, and scope — or honestly says the report cannot

---

## 4. Knowledge Check

1. What three things must you name before a CTI report is actionable for a hunt?
2. Give one reason to mark a report **awareness-only**.
3. Give one reason to **hand off** instead of hunt.
4. You have a named host but no DNS or TLS for that VLAN. Hunt-worthy, awareness, or something else? Why?
5. IR already owns the hash in Building C. The same bulletin lists CDN names with no analytic on finance. What do you do?

---

## 5. Summary

- Assess first: hunt-worthy, awareness-only, or hand off — plus one reason.
- Actionable for a hunt = question + telemetry + scope.
- Rapid triage is a label, not a TTP extract.
- Open incidents and blocklist firehoses are not hunts.
- Visibility gaps shrink or kill the hunt; they do not get a “clean” stamp.
- Extract leads next (**2.4.2**). STIX is **2.4.3**. ATT&CK mapping is **2.5**.

---

## 6. References & Further Reading

- Related modules:
  - 2.2.2 – Hunt development concepts
  - 2.3.1 – Tool capabilities for hunting
  - 2.4.2 – Extracting hunt leads from CTI (next)
  - 2.1 – Purpose of threat hunting
- Local CTI intake / hunt charter (when published)
