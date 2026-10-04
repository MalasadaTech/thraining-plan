# Module 2.9 – Cyber Threat Intelligence Section Summary

**Target Audience:** CTI Analyst (primary); SOC Analyst, Threat Hunter (secondary)  
**Estimated Time:** 15–20 minutes  
**Module Type:** Section summary — no proficiency mapping

## Purpose

Module 2.0 introduced the CTI workflow:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

Module 2.9 closes that loop.

By this point, you have learned how to define intelligence requirements, evaluate evidence, use structured tradecraft, select platforms, enrich technical objects, test relationships, assess local significance, produce intelligence, answer RFIs, and disseminate the result.

This summary reconnects those skills into one requirement-to-answer workflow.

## 1. What You Can Now Do

You should now be able to:

- distinguish data, information, and intelligence;
- identify the customer, requirement, and decision context;
- intake and prioritize an RFI;
- choose collection sources based on the question;
- preserve provenance and distinguish independent reporting from repeated upstream claims;
- use estimative language and structured techniques without hiding uncertainty;
- evaluate source reliability and information credibility;
- recognize and mitigate common analytic biases;
- use ATT&CK, Diamond, and Kill Chain to organize evidence appropriately;
- select CTI platforms based on the lookup required;
- manage observables/IOCs through retain, enrich, review/expire, or reject decisions;
- perform file, RDAP/WHOIS, DNS, and infrastructure enrichment;
- keep DTF infrastructure pivots separate from file and behavioral relationships;
- correlate evidence while testing alternative explanations;
- distinguish a candidate relationship, campaign/activity-set assessment, and actor attribution;
- assess applicability, visibility, relevance, and impact separately;
- represent intelligence in STIX when useful;
- produce a finished intelligence answer;
- close an RFI or document follow-up;
- disseminate through the correct audience and local process.

The important skill is not producing more enrichment.

It is producing a supported answer.

## 2. The 2.x Block at a Glance

| Unit | Core skill retained |
|---|---|
| **2.1 – Foundations and Requirements** | Define the question, customer, collection need, and desired intelligence outcome. |
| **2.2 – Analytical Tradecraft** | Make disciplined judgments from incomplete or conflicting evidence. |
| **2.3 – Frameworks** | Organize adversary behavior, relationships, and intrusion progression without manufacturing missing facts. |
| **2.4 – Tools and Platforms** | Select the right source for the question and preserve the result as an evidence record. |
| **2.5 – Enrichment and Discovery** | Test technical relationships and combine evidence into stronger or weaker links. |
| **2.6 – Assessment** | Determine what applies, what is visible, why the finding matters locally, and plausible impact. |
| **2.7 – Production and Dissemination** | Turn analysis into structured and finished products that answer the requirement. |
| **2.8 – Local Application** | Follow the organization's real requirements, approval process, customers, and dissemination channels. |

## 3. A12 End to End

A12 can demonstrate the entire CTI workflow.

### Step 1 – Intake the requirement

SOC asks:

> **What is known about the update domain, and does available evidence support that it delivered `update.exe` during A12?**

Capture:
- customer;
- question;
- priority;
- existing evidence;
- desired answer;
- deadline/follow-up expectations.

### Step 2 – Separate data, information, and intelligence

Examples:

**Data**  
> DNS response, hash, IP, sandbox process event.

**Information**  
> The domain resolved to an IP during the incident window.

**Intelligence**  
> An assessed answer explaining what the relationship means for A12 and how strongly the evidence supports it.

### Step 3 – Apply tradecraft

Evaluate:
- source provenance;
- reliability;
- credibility;
- uncertainty;
- alternative explanations;
- possible bias.

Do not treat two reports repeating the same upstream source as independent corroboration.

### Step 4 – Organize with frameworks

Use:
- ATT&CK to organize behavior;
- Diamond Model to organize adversary/capability/infrastructure/victim relationships;
- Kill Chain to reason about intrusion progression.

Frameworks help structure analysis.

They do not fill evidence gaps.

### Step 5 – Select the source

Choose platforms based on the unresolved question.

For example:
- internal TIP for prior local/contextual knowledge;
- VirusTotal for file relations/behavior/context;
- ANY.RUN for sandbox execution evidence;
- Silent Push for passive-DNS/infrastructure context;
- urlscan.io for observed web behavior.

Record:
- object;
- source;
- time;
- result;
- limitation.

### Step 6 – Enrich and pivot

Use the appropriate method:

- IOC lifecycle;
- file similarity;
- registration/RDAP;
- advanced DNS;
- infrastructure pivoting;
- DTF identifiers for infrastructure relationships;
- correlation/link analysis.

Preserve file and behavioral pivots as their own evidence rather than forcing them into an infrastructure-only framework.

### Step 7 – Correlate

Suppose the update domain and another domain share:

- an uncommon nameserver;
- a time-overlapping IP;
- additional supporting context.

Record a candidate relationship first.

A stronger campaign/activity-set claim requires stronger, time-relevant activity evidence.

Actor attribution requires still more.

### Step 8 – Assess organizational significance

For each relevant behavior/finding, separate:

**Applicability**  
> Can it occur here?

**Visibility**  
> Can we observe it?

**Relevance**  
> Does it intersect our mission/assets/technology/exposure?

**Impact**  
> What plausible consequence follows if true here?

This converts technical findings into organizational intelligence.

### Step 9 – Produce the answer

A strong RFI response might say:

> Available evidence supports the update domain's association with the A12 activity set and is consistent with attempted payload delivery. Current evidence does not establish successful execution of `update.exe`.

The answer:
- addresses the question;
- identifies what is supported;
- preserves the unresolved gap.

### Step 10 – Disseminate and close

Deliver through the approved audience/channel.

Then record:
- requirement answered;
- confidence/limitations;
- follow-up agreed;
- new requirement if needed.

## 4. Distinctions Worth Keeping

### Data ≠ information ≠ intelligence

Raw observations become information when context is added.

Intelligence requires analysis against a question or requirement.

### Requirement ≠ collection activity

The requirement is the question.

Collection is how you gather evidence to answer it.

### Source reliability ≠ information credibility

A generally reliable source can still report a weak claim.

An unfamiliar source can still provide technically verifiable information.

Evaluate both.

### Platform result ≠ intelligence judgment

A sandbox event, passive-DNS record, detection count, or web scan is evidence.

The analyst decides what that evidence supports.

### Observable ≠ IOC

A technical value is an observable.

Its promotion into an operational IOC depends on context, provenance, specificity, validity, and purpose.

### Candidate pivot ≠ supported relationship

A shared field can justify another check.

It does not automatically establish common control or common malicious purpose.

### Candidate relationship ≠ campaign ≠ attribution

These are progressively stronger claims.

Promote only as far as the evidence supports.

### File/behavioral relationship ≠ DTF infrastructure relationship

DTF remains infrastructure-focused.

File similarity and behavioral pivots should be retained alongside infrastructure analysis without being forced into DTF.

### Applicability ≠ visibility ≠ relevance ≠ impact

These answer different questions and can produce different outcomes.

### STIX representation ≠ proof

STIX structures information.

The object or relationship still needs evidence and appropriate confidence.

### Enrichment ≠ finished intelligence

A large collection of lookups is not the product.

The supported answer is the product.

### RFI intake ≠ RFI response

2.1.5 captures and prioritizes the question.

2.7.4 returns to that question and records closure or follow-up.

## 5. Integrated Review Exercise

Use this A12 CTI card:

> **Requirement:** Determine what is known about the update domain and whether evidence supports payload delivery.  
> **Internal TIP:** no prior hash match  
> **Sandbox:** encoded PowerShell and attempted retrieval behavior observed  
> **DNS/RDAP:** update domain and `login-prd.net` share an uncommon nameserver; IP overlap exists during part of the relevant window  
> **Environment:** Windows workstations are present; process visibility is partial on one endpoint population  
> **Evidence gap:** successful execution of `update.exe` is not established

Write a short intelligence answer using:

### Requirement
What question are you answering?

### Evidence
Which observations materially support the answer?

### Relationship assessment
What can you say about the infrastructure relationship?

### Applicability / visibility
Which behavior applies, and what can or cannot be seen?

### Relevance / impact
Why does the finding matter locally?

### Judgment
What does the evidence support?

### Gap
What remains unresolved?

### Closure / follow-up
Is the RFI answered, or is a new requirement needed?

A strong answer should not let the amount of enrichment exceed the strength of the evidence.

## 6. CTI Readiness Checklist

Before moving into 3.x, you should be comfortable saying:

- [ ] I can distinguish data, information, and intelligence.
- [ ] I can define the customer and intelligence requirement before collecting.
- [ ] I can intake and prioritize an RFI.
- [ ] I can preserve provenance and evaluate source/reporting quality.
- [ ] I can use estimative language without hiding uncertainty.
- [ ] I can test alternative explanations and recognize bias.
- [ ] I can use ATT&CK, Diamond, and Kill Chain for their appropriate purposes.
- [ ] I can choose a CTI platform based on the question.
- [ ] I can record platform results with time/source/limitations.
- [ ] I can manage observable/IOC lifecycle decisions.
- [ ] I can perform file, registration, DNS, and infrastructure enrichment.
- [ ] I can keep file/behavioral and infrastructure pivots conceptually separate.
- [ ] I can distinguish a candidate link, stronger activity-set/campaign assessment, and attribution.
- [ ] I can separate applicability, visibility, relevance, and impact.
- [ ] I can produce an evidence-based answer rather than an enrichment dump.
- [ ] I can close an RFI or identify a follow-up requirement.
- [ ] I can follow the local production, approval, and dissemination process.

If one area is weak, return to the corresponding 2.x unit.

## 7. Bridge Into 3.x Threat Hunting

CTI can answer:

> **What does the available intelligence tell us about the threat?**

That answer may create a new internal question:

> **Does this behavior or related activity exist elsewhere in our environment?**

That is where threat hunting begins.

CTI should hand hunting:
- the behavior/procedure;
- relevant indicators and observables;
- infrastructure context;
- provenance;
- uncertainty;
- applicability/visibility notes;
- the reason the lead matters.

Hunting then converts that intelligence into a bounded internal search.

## Summary

The 2.x block taught one complete intelligence workflow:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

A strong intelligence product does not show everything the analyst found.

It shows what the evidence supports, why it matters, and what remains uncertain.

Keep one principle with you into 3.x:

> **The value of CTI is the supported answer—not the number of tools, indicators, or pivots used to reach it.**

**Next:** **3.x – Threat Hunting**.
