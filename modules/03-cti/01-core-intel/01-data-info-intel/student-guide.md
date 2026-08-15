# Module 3.1.1 – Data, Information, and Intelligence

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- CTI: 3-level (B/3c) → 5-level (C/4c) → 7-level (C/4c)  
- Hunter: A/1a → B/2b → B/3c  
- SOC: awareness only (A / 1a)  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Define data, information, and intelligence and state how they differ.
2. Explain how raw data becomes information and then intelligence.
3. Correctly categorize examples as data, information, or intelligence.
4. Spot products that are labeled “intel” but are still only data or information.

**Mapped Proficiency Items:**
- K: 3.1.1 – Difference between data, information, and intelligence
- T: 3.1.2 – Correctly categorize examples as data, information, or intelligence

---

## 1. Key Concepts

### 1.1 Definitions and Distinctions

These three words get used as if they mean the same thing. They do not. Your job starts when something becomes **intelligence**.

| Term | What it is | What it answers | Typical form |
|------|------------|-----------------|--------------|
| **Data** | Raw, unprocessed observations or facts | “What was recorded?” | A log field, a hash, an IP, a timestamp, a packet count |
| **Information** | Data that has been organized, correlated, or given context | “Who / what / when / where?” | A timeline, a parsed alert, a list of related indicators, a rewritten log story |
| **Intelligence** | Information analyzed against a requirement to support a decision | “So what? What should we do?” | An assessment, a judgment, a recommended action, a confidence statement |

**Most critical distinction for daily work:**  
Information describes. Intelligence judges and enables a decision.

A single Zeek `ssl` row is **data**.  
“Host 10.10.50.88 opened TLS to a lookalike Microsoft name with a self-signed certificate at 19:41” is **information**.  
“We assess this host is likely in a credential-harvesting session; isolate it and hunt the same SNI/cert pair” is **intelligence**.

That last sentence does three things data and information do not:

- It answers a question someone actually has (is this host compromised?).
- It adds analytic judgment, not just restated facts.
- It points to a decision or next action.

### 1.2 How Raw Data Becomes Intelligence

The path is a process, not a rename.

```
Raw observation (data)
        ↓  parse, enrich, correlate, put in time and asset context
Organized picture (information)
        ↓  analyze against a requirement; add judgment, alternatives, and “so what”
Decision support (intelligence)
```

| Step | What you add | What you still do not have |
|------|----------------|----------------------------|
| Data → information | Context: asset owner, time window, related events, who talked to whom | Meaning for the mission |
| Information → intelligence | Analysis: what it implies, how sure you are, what to do next | Nothing useful if you skip the requirement |

**Requirement** here is only the reason the work exists (“Are we seeing this campaign?”). How to write PIRs is a later module.

Common failure: people stop at information and ship it as intelligence.

| Labeled “intel” | What it usually is | Why it fails |
|-----------------|--------------------|--------------|
| A pasted IOC list from a blog | Data or information | No analysis of *your* environment or a decision |
| “VirusTotal says 12 vendors detect this hash” | Information | A count is context, not a judgment |
| “New ransomware family reported this morning” | Information (sometimes data) | Headline, not an assessment of exposure or action |
| “This JA3 is associated with malware on Twitter” | Data plus a claim | No evaluation, no confidence, no “so what for us” |

A lead is not an incident. A feed is not a finished product. Calling either “intelligence” does not make it so.

### 1.3 How to Categorize

Ask three questions, in order:

1. **Is it still a raw fact?** If yes → **data**.
2. **Has it been organized or given context, but not judged?** If yes → **information**.
3. **Does it answer a requirement with analysis and a usable implication?** If yes → **intelligence**.

If you are unsure, it is not intelligence yet.

| Signal | Points toward |
|--------|----------------|
| Field names, hashes, IPs, raw JSON | Data |
| “Host X did Y at time Z” with no recommendation | Information |
| “We assess / we judge / therefore do Z” tied to a question | Intelligence |
| Vendor or OSINT copied forward unchanged | Data or information, until *you* analyze it |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Path (Same Activity, Three Layers)

**Data**

```
ts: 2026-08-14T19:40:11.210Z
id.orig_h: 10.10.50.23
id.resp_h: 93.184.216.34
id.resp_p: 443
server_name: www.example.com
```

**Information**  
Workstation `10.10.50.23` (finance VLAN, user jsmith) started a TLS 1.3 session to `www.example.com` on 443 at 19:40. SNI and certificate subject match. Duration 8 seconds. No other unusual connections from this host in the last hour.

**Intelligence**  
We assess this session is ordinary SaaS browsing, not a follow-up from this morning’s phishing requirement. No containment. Keep the host in the existing 24-hour review set only because the user was on the original target list.

**Interpretation:**  
Same activity, three products. The log row is data. The rewritten story is information. The assessment against a requirement — with a decision — is intelligence. Do not brief the raw row and call it intel.

### Example 2: IOC Dump Labeled as Intelligence (Lead)

A chat message to hunt and SOC:

> CTI INTEL: New APT activity. Block these now.  
> `45.76.12.88`  
> `update.not-a-real-cdn.example`  
> `6734f37431670b3ab4292b8f60f29984`  
> Source: public blog, posted today.

**Interpretation:**  
This is **data** (three indicators) plus a thin claim. It is not intelligence. There is no analysis of relevance, no statement of confidence, no “what this means here,” and “block these now” is an instruction without a supported judgment. Treat it as a **lead**: enrich, see if the indicators appear internally, then decide. Shipping the paste as a finished product trains consumers to confuse volume with insight.

### Example 3: Two Write-ups of the Same Alert (Lead)

**Write-up A**

> Alert T-4418 fired. Source 10.10.22.17, destination 203.0.113.90:8443, TLS 1.0, RC4, SNI `update.not-a-real-cdn.example`. Hash of the JA3 is on two public malware lists. Ticket closed as “suspicious TLS.”

**Write-up B**

> Requirement: are endpoints talking to the “fake update CDN” cluster from this week’s report?  
> We assess **10.10.22.17** is likely C2 or malware update traffic, not a browser. The stack of TLS 1.0 + RC4 + port 8443 + generic update SNI is inconsistent with the standard image, and the same JA3 appears on two other lab VLANs.  
> Recommend: isolate the host, hunt that JA3 and SNI fleet-wide, and report confirmed victims to IR. Confidence is moderate: we have protocol and fleet pattern, not a malware detonation yet.

**Interpretation:**  
A is **information** (and some data) with a label. Closing the ticket does not create intelligence. B is **intelligence**: it answers a requirement, states a judgment, gives the “so what,” and names a decision. The extra fields in A did not promote it. The analysis did.

---

## 3. Hands-On Exercise

**Objective:** Practice the distinction and the data → information → intelligence path.

**Instructions:**

1. Review the three examples above and write a one-sentence summary for each (what layer it is, and why).
2. Categorize each item below as **data**, **information**, or **intelligence**. Give one reason.
   - A SHA-256 value in a ticket with no other text
   - “Three hosts in Building C resolved `login.micros0ft-sso.net` between 02:00 and 02:12”
   - “We assess those three hosts are in an active credential-phishing session; disable the accounts and hunt the domain”
   - A STIX bundle imported from a vendor and not yet reviewed
   - A SOC timeline of process, DNS, and TLS events for one host
   - “Priority is low; this family does not match our technology stack, so no detection work this week”
3. Take the raw TLS row in Example 1 and write:
   - one sentence of **information** (context only), and
   - one sentence of **intelligence** that answers: *Is this host part of the lookalike-Microsoft activity?*

**Expected Outcome:**
- Accurate short summaries of the three examples
- Six categorizations with a reason each
- A clear information sentence and a clear intelligence sentence from the same data

---

## 4. Knowledge Check

1. What is the difference between data and information?
2. What must be present before information becomes intelligence?
3. Why is a public IOC list not intelligence by itself?
4. Categorize: “Host 10.10.50.88 presented a self-signed certificate for a Microsoft lookalike SNI at 19:41.”
5. Categorize: “We assess that host is in a phishing session; isolate it and hunt the same certificate pair.”

---

## 5. Summary

- Data is the raw record. Information is the organized story. Intelligence is the judged answer to a requirement.
- You do not get intelligence by renaming a feed or pasting indicators into a brief.
- The path is: add context, then add analysis and a decision. Skip either step and you still have information (or data).
- A lead is something to work. It is not an incident and it is not finished intelligence.
- If you cannot say what question you answered and what someone should do, you are not done.

---

## 6. References & Further Reading

- Related modules:
  - 3.1.3 – Intelligence lifecycle (next)
  - 3.1.5 – Intelligence types
  - 3.1.7 – Intelligence requirements
- Internal style for assessments (when published)
- Joint / ODNI primers on the distinction between data, information, and intelligence (use the local copies)
