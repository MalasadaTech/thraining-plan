# Module 3.3.1 – Internal Threat Intelligence Platform

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.3.1 A / A / B · 3.3.1.1 1a / 1a / 2b  
- Hunter: 3.3.1 A / B / B · 3.3.1.1 1a / 2b / 3c  
- CTI: 3.3.1 B / C / C · 3.3.1.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the **purpose** and **core functions** of the internal TIP.
2. **Navigate and search** (classroom Harbor TIP).
3. **Search and retrieve** a relevant object.
4. **Use** the TIP to enrich or analyze an indicator or report (link a sighting / related object).

**Mapped Proficiency Items:**
- K: 3.3.1 – Internal threat intelligence platform
- T: 3.3.1.1 – Search, retrieve, and use the internal TIP for enrichment or analysis

---

## 1. Key Concepts

The internal TIP is the **intel store** — indicators, reports, sightings, and cluster labels *we* already hold. It is not VirusTotal (**3.3.2** / **3.9**). It is not the SOC ticket worklog (**1.8.4**). It is not SIEM.

**Classroom TIP (this lesson only):** `https://tip.harbor.internal`  
If your site has a real TIP, use those screens. The obligation is **search / retrieve / attach**, not these menu names.

**Purpose and functions (outline a):**

| Function | What it is for |
|----------|----------------|
| **Store** | Indicators, reports, sightings, cluster/campaign objects |
| **Search** | Find what Harbor already knows about an IOC or cluster |
| **Link** | Connect a new sighting or related hash to an existing object |
| **Support production** | Pull prior hits into the draft; attach the TIP object to the product |

It does **not** replace collection in Zeek/SIEM (**3.1.8** internal class). It **records** and **links** what those tools already saw.

**Navigate and search (outline b):**

| Control | Classroom use |
|---------|----------------|
| Search box | Exact IOC, tag (`night-owl`), or cluster name |
| Type filter | Indicator / report / sighting / cluster |
| Date / TLP / source | Narrow; do not dump the whole tenant |
| Open object | Retrieve = fields + linked sightings + last updated |

No login → **1.8.3** `ACCESS-REQ`. Do not use a teammate’s session.

**Supports enrichment, analysis, production (outline c):**

| Use | You do this in the TIP | You do **not** do this here |
|-----|------------------------|----------------------------|
| **Enrich** | Add a **sighting** (host, time, sensor) or **link** a related indicator | VT Relations pivot (**3.9**) |
| **Analyze** | Read prior Harbor hits before you write *likely* | Full ACH grid (**3.2.2**) |
| **Produce** | Attach the object ID to the draft / ticket | Write the finished 3.11 product |

| This lesson | Other |
|-------------|-------|
| Harbor TIP search + link | VT / AnyRun / Silent Push / URLScan — **3.3.2** |
| Not STIX graph authoring | **3.10** |
| Not case-note location | **1.8.4** (you may *link* the TIP ID in the ticket) |

The tasks: a **retrieve line** and an **enrich line** — not “the TIP exists.”

`query | object opened | fields retrieved`  
`object | what you add or link | why it helps analysis`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Search SNI → open indicator → two prior sightings | Searching VT and calling it the TIP |
| Link WS-JLEE sighting to the existing Night Owl indicator | Finding the object and not attaching the new hit |
| Tag `night-owl` search for the cluster | Dumping every IOC in the tenant |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Search and Retrieve (Expected)

**Need:** Do we already know `nightowl-updates.net`?

**Query:** Search box = `nightowl-updates.net`, type = Indicator.  
**Retrieve:** Indicator object `IND-1882`. Fields: SNI, tag `night-owl`, TLP:AMBER, two sightings (lab host last week; none on WS-JLEE yet).  
**Not:** A VirusTotal tab.

### Example 2: VT Is Not the TIP (Lead)

**Draft:** “I enriched it in VT. TIP done.”

**Fail.** External enrichment is **3.3.2**. The internal question — *have we seen this?* — is unanswered.  
**Correct:** Example 1 first. VT can come *after* if the PIR needs commercial/OSINT (**3.1.8**).  
**Lead:** Right instinct (enrich). Wrong **store**.

### Example 3: Retrieve Without Enrich (Lead)

**Analyst** opens `IND-1882`, reads it, writes “likely Night Owl,” never adds WS-JLEE.

**Fail task 2.** The TIP did not *support* analysis/production — the new internal sighting is missing for the next shift.  
**Correct enrich:** Add sighting: host `WS-JLEE`, time 14:05, sensor `span-1` / EDR. Link hash `6734f374…` if it is a new related indicator.  
**Lead:** Opening the page is retrieve only.

---

## 3. Hands-On Exercise

**Objective:** Retrieve an object and use it (link or sight).

**Use the Harbor TIP card.** Overlay site names if posted.

**Instructions:**

1. One sentence each for Examples 1–3: retrieve vs enrich vs wrong store.
2. **Retrieve** (task 1): write the **retrieve line** for each.

   - A. JA3 `a0e9f5…` — do we have it?  
   - B. Cluster tag `night-owl` — what objects come back?

3. **Use** (task 2): write the **enrich line**.

   - C. New EDR hit: WS-JLEE loaded hash `6734f374…`. `IND-1882` already exists for the SNI.  
   - D. You need prior Harbor hits in a tactical note for SOC. What do you **pull from the TIP** into the draft (not VT)?

4. Do not open VT/AnyRun/Silent Push/URLScan. Do not author STIX. Do not file `ACCESS-REQ` unless you *label* a 403 (**1.8.3**).
5. If B returns both indicators and a cluster object, say so — that is a good retrieve.

**Expected Outcome:**
- Three example summaries
- Two retrieve lines
- Two enrich / pull lines
- No external-tool walkthrough

---

## 4. Knowledge Check

1. What problem does the **internal TIP** solve that SIEM and VT do not?
2. Name three **functions** on the classroom card.
3. What is the difference between **retrieve** and **enrich**?
4. Why is a VT tab not task 1?
5. Where do **case working notes** live, versus the TIP?

---

## 5. Summary

- Internal store: search, retrieve, link a sighting.
- Not VT. Not the ticket worklog.
- Next: external tools (**3.3.2**).

---

## 6. References & Further Reading

- Related modules:
  - 3.2.4 – Cognitive biases (previous cluster)
  - 3.3.2 – External tools (next)
  - 3.1.8 – Collection source classes
  - 1.8.3 – Tool access
  - 1.8.4 – Investigation notes
- Local TIP SOP / screenshots (optional — substitutes Harbor menus)
