# Module 2.4.3 – STIX as Hunt Input

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 2.4.3 B / C / C · 2.4.3.1 3c / 4c / 4c · 2.4.3.2 3c / 4c / 4d  
- SOC: 2.4.3 A / A / B · 2.4.3.1 1a / 1a / 2b · 2.4.3.2 1a / 1a / 2b  
- CTI: 2.4.3 A / B / B · 2.4.3.1 1a / 2b / 3c · 2.4.3.2 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the STIX objects a hunter actually uses in a report or bundle.
2. Tell which of those objects are hunt-relevant and which only give context.
3. Explain how a STIX bundle seeds a hunt (you do not author STIX here).
4. Identify hunt-relevant objects, then turn them into hunt leads.

**Mapped Proficiency Items:**
- K: 2.4.3 – STIX as hunt input
- T: 2.4.3.1 – Identify hunt-relevant objects in a report or bundle
- T: 2.4.3.2 – Turn those objects into hunt leads

---

## 1. Key Concepts

### 1.1 Objects a hunter actually uses

You read STIX **after** the **2.4.1** gate. If the bundle is awareness-only or a full hand-off, stop. Mixed bundles: identify only the hunt-worthy slice.

A **bundle** is a package of STIX objects plus the links between them. You do **not** write, validate, or share STIX here. That is **3.10**.

| Object | What it is | Hunt-relevant when |
|--------|------------|--------------------|
| **indicator** | A pattern to look for (hash, host, IP, URL) | Current, rare enough, and you can query that field |
| **attack-pattern** | How they work (a technique or procedure; often already tagged with ATT&CK) | Specific enough to search as a *method*, and you have telemetry |
| **observed-data** | A recorded sample of observables (what was *seen*, not a detection rule) | It names artifacts or a pattern you can still search internally |
| **malware** | Family or sample | A current hash or named installer you can query — not the family slogan alone |
| **threat-actor** / **intrusion-set** | Who, or a named set of activity | Scope or priority hook. Not a search by itself |
| **relationship** | Links objects (`indicates`, `uses`, `attributed-to`) | Tells you which leftovers belong together |

**Most critical distinction for daily work:**  
Labeling every object in the JSON is **3.10**. **Hunt-relevant** means the object can become a keep under **2.4.2** (searchable TTP, artifact, or behavior) or it ties those leftovers together.

| Hunt-relevant (keep looking) | Context only, or drop |
|------------------------------|------------------------|
| `indicator` for this week’s lookalike CDN | 400 generic VPS `indicator`s already on yesterday’s block list |
| `attack-pattern` for HTTPS C2 to named CDNs; report already lists **T1071.001** | `attack-pattern` that only says “persistence” |
| `observed-data`: after-hours repeated DNS+TLS to those names | `observed-data` of registry Run keys when you have **no telemetry** |
| `malware` object with a current installer hash | `malware` name only (“Family X”) with no artifact |
| `relationship`: malware `uses` that C2 `attack-pattern` | `threat-actor` name with no linked indicator or pattern |
| Copy **T1071.001** if the `attack-pattern` already has it | Inventing ATT&CK IDs or opening Navigator (**2.5**) |

Campaign, course-of-action, identity, and sighting exist in STIX. Hunters may see them. They are **not** the objects this lesson signs off. Do not author the missing ones.

### 1.2 How a STIX bundle seeds a hunt

A bundle **seeds** a hunt when you can walk objects → leftovers → a question that can fail. It does not execute the hunt (**2.2.1**). It does not replace the **2.4.2** drop list.

| Step | You do | You do not |
|------|--------|------------|
| 1 | Confirm the bundle (or slice) already passed **2.4.1** | Re-triage the whole PDF from scratch |
| 2 | Identify hunt-relevant objects (**2.4.3.1**) | Label every STIX type for production (**3.10**) |
| 3 | Apply **2.4.2** keep/drop: no telemetry, expired, noise | Keep the whole indicator list because it is “structured” |
| 4 | Turn leftovers into leads (**2.4.3.2**): TTP / artifact / question | Write a full four-field card unless the question needs a scope hook (**2.2.2**) |
| 5 | Record ATT&CK IDs the objects already print | Map coverage or prioritize by tactic (**2.5**) |

**Seed (good):** two current domain `indicator`s + HTTPS C2 `attack-pattern` + `uses` relationship → if finance follows those names after hours, we should see repeated DNS+TLS.

**Not a seed:** dump all IPv4 `indicator`s into a block list and call it a hunt. That is detections / IR, or noise.

How to write STIX, `external_references` graphs, or TAXII sharing is **3.10**. Stay here: identify, then turn into leads.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Bundle → seed)

**Input:** Hunt-worthy bundle (**2.4.1** already passed). Finance in scope. DNS+TLS exist. Lab has no DNS. Objects:

| Type | Content |
|------|---------|
| `indicator` | Lookalike CDN hostnames (valid_until this quarter) |
| `indicator` | Installer hash (current bulletin) |
| `attack-pattern` | C2 over HTTPS to those CDNs; **T1071.001** already on the object |
| `malware` | Installer sample; `relationship` malware `uses` the C2 pattern |
| `attack-pattern` | One-line “scheduled tasks” aside; no host class |
| `threat-actor` | Named group; `attributed-to` only |

**Identify (2.4.3.1)**  
Hunt-relevant: CDN `indicator`s, hash `indicator`, HTTPS C2 `attack-pattern`, `uses` relationship, `malware` (for the hash).  
Context only: `threat-actor` name.  
Drop: task `attack-pattern` (slogan / no procedure); lab (no DNS) is a **visibility gap**, not a lead.

**Turn into leads (2.4.3.2)**

| Field | What they wrote |
|-------|-----------------|
| TTPs kept | C2 over HTTPS to named lookalike CDNs. **T1071.001** recorded as given |
| Artifacts kept | Installer hash; CDN hostnames; after-hours repeated DNS+TLS from finance |
| Dropped | Task aside; actor name as a search; lab (no DNS) |
| Hunt question | If finance laptops follow the bundle CDN names after hours, we should see repeated DNS+TLS from the finance VLAN |

**Interpretation:**  
The bundle seeded a hunt. Objects were identified, then converted with the same keep/drop/question bar as **2.4.2**. Nobody authored STIX. Nobody mapped coverage.

### Example 2: Indicator Firehose (Lead)

A hunt channel paste:

> Seeded from STIX: all 400 IPv4 indicators, every 2019 hash in the bundle, hunt the enterprise for the intrusion-set.

Compare a documented seed from the same bundle:

> Identified: two domain `indicator`s still `valid`; `attack-pattern` parent `wscript.exe` + rare script; `uses` relationship. Dropped: 2019 hash `indicator`s (expired); 400 VPS `indicator`s (noise / already blocked); intrusion-set name (not a search). ATT&CK: none given. Question: if Building C workstations run that parent+script, we should see process-create on hosts with process logging in 24 hours.

**Interpretation:**  
Structured JSON is not a seed. Expired + noise + a who-object cannot become leads. The second write-up is **2.4.3.1** then **2.4.3.2**.

### Example 3: Gap + Invented Object (Lead)

**Write-up A**

> `attack-pattern`: registry Run keys. No registry logging. Added T1547.001 so the bundle is complete. Question: hunt persistence.

**Write-up B**

> Identified then **dropped** the Run-key `attack-pattern` and the Run-key `observed-data` — **no telemetry** (visibility gap). Do not invent **T1547.001**; the objects never listed it. Do not author a replacement `indicator`. Kept: the bundle’s current hostname `indicator`. Question: if that host was used here, we should see DNS `query` or TLS `server_name` = that name; finance; 7 days.

**Interpretation:**  
A hunts a gap and fabricates an ID (and pretends to author STIX). B identifies, drops what cannot be tested, and turns one leftover object into a lead. Mapping stays in **2.5**. Authoring stays in **3.10**.

---

## 3. Hands-On Exercise

**Objective:** Practice identifying hunt-relevant STIX objects and turning them into hunt leads.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (seeded, or not, and why).
2. For each item below, say **hunt-relevant**, **drop**, **context only**, **record ATT&CK**, or **not a hunt lead**. Give one reason.
   - `indicator`: lookalike CDN hostname from this week’s bundle
   - 400 generic VPS `indicator`s already on yesterday’s block list
   - `attack-pattern`: “They use persistence”
   - `observed-data`: after-hours repeated DNS+TLS to the bundle names
   - `attack-pattern` already prints **T1071.001** next to the CDN C2 procedure
   - `threat-actor` name with no linked indicator or pattern
3. Write **one seed card** (small table or four sentences): objects identified, objects dropped, hunt leads (TTP / artifact), hunt question. Use the finance CDN bundle *or* the parent+script leftover. Do not triage from scratch (assume **2.4.1** already said hunt-worthy). Do not author STIX. Do not map ATT&CK. Do not execute a SIEM search.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six identifications with a reason each
- One card that names hunt-relevant objects, drops noise/expired/no-telemetry, records IDs only if given, and states a question that can fail

---

## 4. Knowledge Check

1. Name three STIX objects a hunter actually uses, and what each is for.
2. When is an `indicator` hunt-relevant, versus context or drop?
3. The `attack-pattern` already lists **T1071.001**. What do you do with that ID in this lesson?
4. A bundle has a Run-key `attack-pattern` and you have no registry logging. Identify, then what?
5. Write one hunt question two leftover domain `indicator`s could support.

---

## 5. Summary

- Read STIX only after the **2.4.1** gate, and only the hunt-worthy slice.
- Hunters use **indicator**, **attack-pattern**, **observed-data**, **malware**, **threat-actor / intrusion-set**, and **relationship**.
- A bundle seeds a hunt when objects survive the **2.4.2** drop list and support a question that can fail.
- Identify first (**2.4.3.1**), then turn leftovers into leads (**2.4.3.2**).
- Do not author STIX (**3.10**). Do not map ATT&CK (**2.5**).
- Next: using ATT&CK for hunt planning (**2.5**).

---

## 6. References & Further Reading

- Related modules:
  - 2.4.1 – Assessing CTI for hunting value
  - 2.4.2 – Extracting hunt leads from CTI
  - 2.5 – ATT&CK for hunt planning (next)
  - 2.2.2 – Hunt development concepts
  - 3.10 – Common STIX objects (author / produce — later, CTI)
- Local sanitized bundle or object table used in class
