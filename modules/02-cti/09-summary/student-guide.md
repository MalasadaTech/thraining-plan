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

> Available evidence supports the assessment that the update domain was used for attempted payload delivery in A12. `WS-JLEE` requested `/update.exe` from that destination during the suspicious activity, but current evidence does not establish successful transfer or execution of the file.

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

## 4. Concepts to Keep Separate During CTI Analysis

The CTI workflow contains several closely related concepts. The distinctions below matter because each one changes what the analyst is justified in claiming or doing next.

### Data, information, and intelligence build on one another

**Data** are recorded observations or values. **Information** adds context that explains how those observations relate. **Intelligence** adds an assessed answer to a relevant question or requirement.

The transition is not created by renaming the artifact. It comes from adding context, analysis, and decision relevance.

### The requirement directs collection

The requirement defines the question and the decision the work is meant to support. Collection obtains the evidence needed to answer it.

Starting with the requirement helps the analyst choose sources deliberately instead of allowing an interesting tool result to redefine the task.

### Source reliability and information credibility are separate judgments

A source with a strong historical record can still provide a weak or poorly supported claim. An unfamiliar source can still provide information that is technically verifiable.

Evaluate the source and the specific information independently, then explain how those judgments affect the assessment.

### Platform output becomes intelligence through analysis

A sandbox event, passive-DNS record, detection count, TIP relationship, or web scan is evidence with provenance. Its significance depends on the question, surrounding evidence, and interpretation.

The analyst's job is to explain what the platform result supports and where its limitations begin.

### An observable becomes an operational IOC through context and purpose

A hash, IP, domain, URL, or filename is first a technical observable. Promoting it into an IOC requires enough suspicious or malicious context, provenance, specificity, validity, and operational purpose to justify using it defensively.

This is also why lifecycle decisions such as retain, enrich, review/expire, and reject are evidence-dependent.

### A pivot candidate needs corroboration before it becomes a supported relationship

A shared nameserver, address, certificate field, or page characteristic can justify another lookup. The initial overlap is a reason to investigate, not proof of common control or malicious purpose.

Use distinctiveness, time relevance, hosting context, and independent evidence to decide whether the relationship strengthens.

### Candidate relationships, campaign assessments, and attribution require progressively stronger evidence

A candidate link can be recorded early. A campaign or activity-set assessment requires a coherent pattern of related activity. Attribution adds the still stronger judgment about who is responsible.

Keeping those levels separate allows the analysis to mature without promoting a tentative relationship beyond the evidence.

### DTF is used for infrastructure relationships

The Defender's ThreatMesh Framework organizes justified infrastructure pivots. File similarity and behavioral relationships remain useful evidence, but they should be recorded alongside the infrastructure analysis rather than forced into an infrastructure-only model.

### Applicability, visibility, relevance, and impact answer different organizational questions

**Applicability** asks whether the behavior can occur in the environment.

**Visibility** asks whether current telemetry can observe it.

**Relevance** asks whether the finding materially intersects the organization's mission, assets, technology, or exposure.

**Impact** asks what plausible organizational consequence follows if the finding is true here.

Because these questions are different, they can legitimately produce different answers.

### STIX represents intelligence; the representation does not establish the claim

STIX provides a structured way to describe objects and relationships. The represented assertion still needs evidence, provenance, and appropriate confidence.

A well-formed STIX relationship is useful for exchange and reuse, but formatting cannot substitute for analysis.

### Enrichment supports the finished answer

A large set of lookups, pivots, and graphs may be valuable working material. The finished intelligence product selects the evidence that answers the requirement and explains its significance.

The goal is not to show every action the analyst performed; it is to deliver a supported answer.

### RFI intake and RFI response are different stages of the same requirement

Module 2.1.5 captures, clarifies, prioritizes, and assigns the question. Module 2.7.4 returns to that requirement with the supported answer, uncertainty, and closure or agreed follow-up.

Keeping both stages visible makes it possible to judge whether the analysis actually answered what the requester needed.

## 5. Integrated Review Exercise

Use this **hypothetical CTI practice card built from the A12 case**. The supplied enrichment and visibility details are exercise conditions rather than additional canonical A12 facts:

> **Requirement:** Determine what role the update domain played and whether available evidence establishes successful payload delivery.  
> **Case evidence:** encoded PowerShell on `WS-JLEE`; HTTP request for `/update.exe` to the update domain  
> **Enrichment:** `login-prd.net` shares an uncommon nameserver pair and an overlapping observed IP with the update domain  
> **Environment:** Windows workstations are present; process visibility is partial on one endpoint population  
> **Evidence gap:** successful transfer or execution of `update.exe` is not established

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

**Next:** [3.0 – Threat Hunting Orientation](../../03-hunter/00-intro/student-guide.md).
