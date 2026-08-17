# Concept index

Use this file to answer: *if a signed-off analyst says they never learned X, where was X taught?*

It is a book-style index of **taught** concepts, not a full-text search of the repo. A word can appear in a sample log without creating an obligation.

| Coverage | Meaning |
|----------|---------|
| **Taught** | This module created the obligation. A signed-off analyst for these roles should know it. |
| **Used** | They saw it again here. This is not the lesson that first owed the knowledge. |

Roles are who the module trains. Depth still comes from the [proficiency matrices](matrices/combined.md) (a signed-off CTI analyst is not held to the same TLS bar as a hunter).

**How to maintain:** add the term to the module `README.md` Concepts list, then add or update the entry here in the same change. Do not scrape student guides.

Module IDs below are teaching-unit IDs (same as the tracker), not outline K/T headings.

---

## 5

### 5-tuple

Also: source/destination IP and port, `id.orig_h`, `id.orig_p`, `id.resp_h`, `id.resp_p`, `proto`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |
| Used | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |
| Used | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |
| Used | [1.2.5 HTTP Engine](../modules/01-soc/02-zeek/05-http-engine/) | SOC, Hunter, CTI |
| Used | [1.2.6 SMTP Engine](../modules/01-soc/02-zeek/06-smtp-engine/) | SOC, Hunter, CTI |
| Used | [1.2.8 Weird Engine](../modules/01-soc/02-zeek/08-weird-engine/) | SOC, Hunter, CTI |

See also: [conn log](#conn-log)

---

## A

### A / AAAA

See [qtype_name](#qtype_name).

### accessing required tools and their URLs

Also: tool URL, open the SIEM URL

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.3 Tool Access and Requests](../modules/01-soc/08-site-specific/03-tool-access/) | SOC, Hunter, CTI |

See also: [requesting access (e.g., SIEM)](#requesting-access-eg-siem), [requesting a tool to be installed](#requesting-a-tool-to-be-installed)

### adjust an intelligence product for a specified audience

Also: rewrite for audience, keep cut format

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.6 Tailoring Output to the Audience](../modules/03-cti/01-core-intel/06-tailoring-audience/) | CTI, Hunter |

See also: [audience analysis](#audience-analysis), [adjusting content, format, and detail for consumers](#adjusting-content-format-and-detail-for-consumers)

### adjusting content, format, and detail for consumers

Also: content format detail, tailor product shape

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.6 Tailoring Output to the Audience](../modules/03-cti/01-core-intel/06-tailoring-audience/) | CTI, Hunter |

See also: [audience analysis](#audience-analysis), [adjust an intelligence product for a specified audience](#adjust-an-intelligence-product-for-a-specified-audience)

### assess attribution statements for confidence and evidence

Also: over-claim, supported attribution, assess the claim

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.7 Attribution](../modules/03-cti/01-core-intel/07-attribution/) | CTI, Hunter |

See also: [levels of confidence in attribution](#levels-of-confidence-in-attribution), [types of attribution (activity group vs nation-state)](#types-of-attribution-activity-group-vs-nation-state)

### audience analysis

Also: who owns the decision, audience questions

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.6 Tailoring Output to the Audience](../modules/03-cti/01-core-intel/06-tailoring-audience/) | CTI, Hunter |
| Used | [3.11.2 Disseminating Intelligence to the Correct Audiences](../modules/03-cti/11-production/02-dissemination/) | CTI, Hunter |

See also: [adjust an intelligence product for a specified audience](#adjust-an-intelligence-product-for-a-specified-audience), [tailor products to different audiences](#tailor-products-to-different-audiences)

### audience identification for dissemination

Also: who owns the next decision, SOC vs leadership audience

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.11.2 Disseminating Intelligence to the Correct Audiences](../modules/03-cti/11-production/02-dissemination/) | CTI, Hunter |

See also: [audience analysis](#audience-analysis), [disseminate through approved channels](#disseminate-through-approved-channels)

### approved dissemination methods and handling markings

Also: classroom TLP, TLP:AMBER, approved intel channel

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.11.2 Disseminating Intelligence to the Correct Audiences](../modules/03-cti/11-production/02-dissemination/) | CTI, Hunter |

Classroom TLP/channel cards are lesson-only, not live org policy.

See also: [disseminate through approved channels](#disseminate-through-approved-channels), [audience identification for dissemination](#audience-identification-for-dissemination)

### tailor products to different audiences

Also: technical vs leadership product, two sends same facts

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.11.2 Disseminating Intelligence to the Correct Audiences](../modules/03-cti/11-production/02-dissemination/) | CTI, Hunter |

See also: [adjust an intelligence product for a specified audience](#adjust-an-intelligence-product-for-a-specified-audience), [audience identification for dissemination](#audience-identification-for-dissemination)

### disseminate through approved channels

Also: send on TIP or ticket or brief, reject Slack and public post

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.11.2 Disseminating Intelligence to the Correct Audiences](../modules/03-cti/11-production/02-dissemination/) | CTI, Hunter |
| Used | [3.12.3 Local Dissemination Channels and Customers](../modules/03-cti/12-site-specific/03-local-dissemination/) | CTI, Hunter |

See also: [approved dissemination methods and handling markings](#approved-dissemination-methods-and-handling-markings), [local customers and channels are site-specific](#local-customers-and-channels-are-site-specific)

### local customers and channels are site-specific

Also: classroom 3.11.2 channels are not the local list, do not invent a customer roster

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.12.3 Local Dissemination Channels and Customers](../modules/03-cti/12-site-specific/03-local-dissemination/) | CTI, Hunter |

See also: [disseminate using the correct local list](#disseminate-using-the-correct-local-list), [disseminate through approved channels](#disseminate-through-approved-channels)

### disseminate using the correct local list

Also: reject sending without checking local customers, send only from a shown list

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.12.3 Local Dissemination Channels and Customers](../modules/03-cti/12-site-specific/03-local-dissemination/) | CTI, Hunter |

See also: [local customers and channels are site-specific](#local-customers-and-channels-are-site-specific), [disseminate through approved channels](#disseminate-through-approved-channels)

### actionable for a hunt

Also: actionable CTI for hunting, hunt question telemetry scope

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.1 Assessing CTI for Hunting Value](../modules/02-hunter/04-cti-for-hunters/01-assessing-cti/) | Hunter, SOC, CTI |
| Used | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

See also: [assessing CTI for hunting value](#assessing-cti-for-hunting-value), [hunt-worthy CTI](#hunt-worthy-cti)

### activity missed by existing security mechanisms

Also: missed activity, activity existing controls might miss, activity the stack did not surface

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.1 Purpose of Threat Hunting](../modules/02-hunter/01-purpose/) | Hunter, SOC, CTI |

See also: [detection gaps](#detection-gaps), [visibility gaps](#visibility-gaps), [purpose of threat hunting](#purpose-of-threat-hunting)

### alert configuration (what would fire)

Also: alert config, what the detection would fire

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.1 Alert Context and Investigation](../modules/01-soc/04-alerts/01-context-investigation/) | SOC, Hunter, CTI |

See also: [alert context (present vs missing)](#alert-context-present-vs-missing), [SIEM detection rules / correlation searches](#siem-detection-rules--correlation-searches)

### alert context (present vs missing)

Also: alert pane, missing context, present context

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.1 Alert Context and Investigation](../modules/01-soc/04-alerts/01-context-investigation/) | SOC, Hunter, CTI |

See also: [alert configuration (what would fire)](#alert-configuration-what-would-fire), [upstream alerting hops](#upstream-alerting-hops)

### assign Admiralty Code ratings

Also: rate source and report, write B3 F1

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.3 Admiralty Code](../modules/03-cti/02-tradecraft/03-admiralty-code/) | CTI, Hunter |

See also: [source reliability scale](#source-reliability-scale), [information credibility scale](#information-credibility-scale)

### assigning a category and ruling out the adjacent one

Also: reject the adjacent category, category neighbor

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.4 Common Alert Categorizations](../modules/01-soc/04-alerts/04-categorizations/) | SOC, Hunter, CTI |

See also: [category: scanning / reconnaissance](#category-scanning--reconnaissance), [category: unsuccessful activity](#category-unsuccessful-activity)

### analysis and production

Also: analysis, production, analytic production, finished intelligence production

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

See also: [intelligence lifecycle](#intelligence-lifecycle), [intelligence](#intelligence)

### Analysis of Competing Hypotheses (ACH)

Also: ACH matrix, fewest inconsistent, competing hypotheses

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.2 Structured Analytic Techniques](../modules/03-cti/02-tradecraft/02-structured-techniques/) | CTI, Hunter |

See also: [Key Assumptions Check](#key-assumptions-check), [when to apply ACH vs Key Assumptions Check](#when-to-apply-ach-vs-key-assumptions-check)

### apply a mitigation technique

Also: concrete bias mitigation, not be aware

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.4 Cognitive Biases and Mitigation](../modules/03-cti/02-tradecraft/04-cognitive-biases/) | CTI, Hunter |

See also: [identify potential cognitive bias in a judgment](#identify-potential-cognitive-bias-in-a-judgment), [techniques to mitigate cognitive biases](#techniques-to-mitigate-cognitive-biases)

### apply a structured analytic technique

Also: fill a mini ACH, fill a KAC table

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.2 Structured Analytic Techniques](../modules/03-cti/02-tradecraft/02-structured-techniques/) | CTI, Hunter |

See also: [select the right structured analytic technique for a scenario](#select-the-right-structured-analytic-technique-for-a-scenario), [Analysis of Competing Hypotheses (ACH)](#analysis-of-competing-hypotheses-ach)

### apply the Diamond Model to an intelligence problem

Also: Diamond on a report, Diamond activity-set card, CTI Diamond line

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.2 Diamond Model Application in CTI](../modules/03-cti/07-frameworks/02-diamond-cti/) | CTI, Hunter |

Incident / indicator cards are [1.5.2 Diamond Model](../modules/01-soc/05-frameworks/02-diamond-model/).

See also: [Diamond Model application in CTI](#diamond-model-application-in-cti), [weakest vertex constrains the intel product](#weakest-vertex-constrains-the-intel-product)

### approved reporting channels

Also: ticket channel, RFI form, approved distro

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.6.3 Notification and Distribution](../modules/01-soc/06-reporting/03-notification-distribution/) | SOC, Hunter, CTI |

See also: [notification chart / matrix](#notification-chart--matrix), [routing a report (recipients, leadership, channel)](#routing-a-report-recipients-leadership-channel)

### answers

Also: DNS answers, response records

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

### anomaly-based hunt

Also: anomaly hunt, baseline hunt, deviation hunt

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.1 Hunt Types](../modules/02-hunter/02-methodology/01-hunt-types/) | Hunter, SOC, CTI |

See also: [hunt types](#hunt-types), [hypothesis-driven hunt](#hypothesis-driven-hunt)

### AnyRun for hunting

Also: Any.Run, AnyRun sandbox, interactive sandbox for hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |
| Used | [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/) | CTI, Hunter |

See also: [tool capabilities for hunting](#tool-capabilities-for-hunting), [purpose, strengths, and weaknesses of AnyRun](#purpose-strengths-and-weaknesses-of-anyrun)

### purpose, strengths, and weaknesses of AnyRun

Also: AnyRun for intelligence, detonate a sample

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/) | CTI, Hunter |
| Used | [3.9.2 AnyRun](../modules/03-cti/09-platforms/02-anyrun/) | CTI, Hunter |

See also: [AnyRun for hunting](#anyrun-for-hunting), [when to use each external tool in the intelligence process](#when-to-use-each-external-tool-in-the-intelligence-process)

### searching AnyRun by tag, IP, domain, or hash

Also: AnyRun search types, search AnyRun submissions

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.9.2 AnyRun](../modules/03-cti/09-platforms/02-anyrun/) | CTI, Hunter |

See also: [reviewing an AnyRun submission for actionable intelligence](#reviewing-an-anyrun-submission-for-actionable-intelligence), [purpose, strengths, and weaknesses of AnyRun](#purpose-strengths-and-weaknesses-of-anyrun)

### reviewing an AnyRun submission for actionable intelligence

Also: extract actionable intelligence from an AnyRun submission, AnyRun R1 vs R2

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.9.2 AnyRun](../modules/03-cti/09-platforms/02-anyrun/) | CTI, Hunter |

See also: [searching AnyRun by tag, IP, domain, or hash](#searching-anyrun-by-tag-ip-domain-or-hash), [purpose, strengths, and weaknesses of AnyRun](#purpose-strengths-and-weaknesses-of-anyrun)

### assessing CTI for hunting value

Also: CTI hunting value, assess a report for hunting, hunter as CTI consumer

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.1 Assessing CTI for Hunting Value](../modules/02-hunter/04-cti-for-hunters/01-assessing-cti/) | Hunter, SOC, CTI |

See also: [hunt-worthy CTI](#hunt-worthy-cti), [awareness-only CTI](#awareness-only-cti), [hand off to detections / IR](#hand-off-to-detections--ir)

### ATT&CK tactics

Also: ATT&CK tactic, why column, TA0002 Execution

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.1 MITRE ATT&CK](../modules/01-soc/05-frameworks/01-attck/) | SOC, Hunter, CTI |
| Used | [3.7.1 MITRE ATT&CK for CTI Analysis and Reporting](../modules/03-cti/07-frameworks/01-attck-cti/) | CTI, Hunter |

See also: [ATT&CK techniques and sub-techniques](#attck-techniques-and-sub-techniques), [mapping observed activity to ATT&CK](#mapping-observed-activity-to-attck)

### ATT&CK techniques and sub-techniques

Also: ATT&CK technique, sub-technique, T1059.001

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.1 MITRE ATT&CK](../modules/01-soc/05-frameworks/01-attck/) | SOC, Hunter, CTI |
| Used | [3.7.1 MITRE ATT&CK for CTI Analysis and Reporting](../modules/03-cti/07-frameworks/01-attck-cti/) | CTI, Hunter |

See also: [ATT&CK tactics](#attck-tactics), [MITRE ATT&CK purpose and structure](#mitre-attck-purpose-and-structure)

### ATT&CK coverage analysis

Also: ATT&CK coverage, coverage analysis for hunting, Navigator as a view

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |

See also: [mapping hunts to ATT&CK](#mapping-hunts-to-attck), [using ATT&CK to identify detection or visibility gaps](#using-attck-to-identify-detection-or-visibility-gaps)

### ATT&CK for CTI analysis and reporting

Also: ATT&CK in intel products, advanced ATT&CK for CTI, supported ATT&CK IDs in a product

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.1 MITRE ATT&CK for CTI Analysis and Reporting](../modules/03-cti/07-frameworks/01-attck-cti/) | CTI, Hunter |
| Used | [3.7.4 Defender’s ThreatMesh Framework (DTF) for Infrastructure Discovery](../modules/03-cti/07-frameworks/04-dtf/) | CTI, Hunter |

SOC alert mapping is [1.5.1 MITRE ATT&CK](../modules/01-soc/05-frameworks/01-attck/). Hunt coverage is [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/).

See also: [extracting TTPs onto ATT&CK IDs](#extracting-ttps-onto-attck-ids), [map a report or activity set to ATT&CK](#map-a-report-or-activity-set-to-attck), [how DTF complements ATT&CK, Diamond, and Kill Chain](#how-dtf-complements-attck-diamond-and-kill-chain)

### awareness-only CTI

Also: awareness only, context-only CTI, do not hunt this report

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.1 Assessing CTI for Hunting Value](../modules/02-hunter/04-cti-for-hunters/01-assessing-cti/) | Hunter, SOC, CTI |

See also: [assessing CTI for hunting value](#assessing-cti-for-hunting-value), [hunt-worthy CTI](#hunt-worthy-cti)

---

## B

### beaconing

Also: long-duration connection, C2 beacon

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

See also: [duration](#duration), [conn_state](#conn_state)

### Bro

See [Zeek](#zeek).

---

## C

### category: root-level access

Also: root-level alert category, SYSTEM / admin category

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.4 Common Alert Categorizations](../modules/01-soc/04-alerts/04-categorizations/) | SOC, Hunter, CTI |

See also: [category: user-level access](#category-user-level-access), [assigning a category and ruling out the adjacent one](#assigning-a-category-and-ruling-out-the-adjacent-one)

### category: scanning / reconnaissance

Also: scan category, recon category

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.4 Common Alert Categorizations](../modules/01-soc/04-alerts/04-categorizations/) | SOC, Hunter, CTI |

See also: [category: unsuccessful activity](#category-unsuccessful-activity), [assigning a category and ruling out the adjacent one](#assigning-a-category-and-ruling-out-the-adjacent-one)

### category: unsuccessful activity

Also: unsuccessful attempt category, failed access category

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.4 Common Alert Categorizations](../modules/01-soc/04-alerts/04-categorizations/) | SOC, Hunter, CTI |

See also: [category: scanning / reconnaissance](#category-scanning--reconnaissance)

### category: user-level access

Also: user-level alert category, Medium user token category

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.4 Common Alert Categorizations](../modules/01-soc/04-alerts/04-categorizations/) | SOC, Hunter, CTI |

See also: [category: root-level access](#category-root-level-access)

### changeover report record location

Also: SOC-CHANGEOVER, shift change log, system of record for changeover

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.7.1 Shift Changeover Process](../modules/01-soc/07-shift-change/01-changeover-process/) | SOC, Hunter, CTI |

See also: [conducting or participating in a shift changeover](#conducting-or-participating-in-a-shift-changeover), [producing a complete changeover report](#producing-a-complete-changeover-report)

### characteristics of actionable intelligence

Also: five actionable checks, who what timely confidence

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.5 Ensuring Intelligence Is Actionable](../modules/03-cti/01-core-intel/05-actionable-intelligence/) | CTI, Hunter |

See also: [evaluate whether intelligence is actionable](#evaluate-whether-intelligence-is-actionable), [common reasons intelligence fails to be actionable](#common-reasons-intelligence-fails-to-be-actionable)

### certificate subject / issuer

Also: `subject`, `issuer`, CN, certificate name

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |
| Used | [3.4.1 Hashing and Similarity Concepts](../modules/03-cti/04-file-similarity/) | CTI, Hunter |

See also: [self-signed certificate](#self-signed-certificate), [certificate / code-signing information](#certificate--code-signing-information)

### certificate / code-signing information

Also: signed vs unsigned, issuer not subject, stolen cert serial

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.4.1 Hashing and Similarity Concepts](../modules/03-cti/04-file-similarity/) | CTI, Hunter |

See also: [extract and interpret certificate information from a file](#extract-and-interpret-certificate-information-from-a-file), [certificate subject / issuer](#certificate-subject--issuer)

### cipher suite

Also: `cipher`, weak cipher, RC4

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

### CNAME

See [qtype_name](#qtype_name).

### collection

Also: collect, intelligence collection, raw intake

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

Collection *sources* (OSINT, commercial, internal) are [3.1.8 Collection Sources](../modules/03-cti/01-core-intel/08-collection-sources/), not this module.

See also: [intelligence lifecycle](#intelligence-lifecycle), [collection source classes (OSINT, commercial, internal)](#collection-source-classes-osint-commercial-internal)

### collection source classes (OSINT, commercial, internal)

Also: OSINT, commercial TIP, internal telemetry as collection class

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.8 Collection Sources and Methods](../modules/03-cti/01-core-intel/08-collection-sources/) | CTI, Hunter |

See also: [identify collection source classes for a requirement](#identify-collection-source-classes-for-a-requirement), [plan collection against an intelligence requirement](#plan-collection-against-an-intelligence-requirement)

### combining Admiralty ratings

Also: letter plus number, B2 F6 A1 rare

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.3 Admiralty Code](../modules/03-cti/02-tradecraft/03-admiralty-code/) | CTI, Hunter |

See also: [assign Admiralty Code ratings](#assign-admiralty-code-ratings), [explain an Admiralty Code rating](#explain-an-admiralty-code-rating)

### classify an intelligence product or requirement by type

Also: classify by type, intelligence type classification

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [intelligence types](#intelligence-types)

### classifying cases and citing evidence

Also: classify TP FP TN FN, cite evidence for classification

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.2 Alert Classification](../modules/01-soc/04-alerts/02-classification/) | SOC, Hunter, CTI |

See also: [True Positive](#true-positive), [False Negative](#false-negative)

### close/escalate clock (time to process)

Also: close clock, escalate clock, time to process an alert

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.5 SLA / Response Time Goals](../modules/01-soc/04-alerts/05-sla-response-times/) | SOC, Hunter, CTI |

See also: [start clock (time to begin investigation)](#start-clock-time-to-begin-investigation), [recording a close or escalate against the correct clock](#recording-a-close-or-escalate-against-the-correct-clock)

### common Windows privilege escalation methods

Also: Windows privilege escalation, token theft, UAC bypass, service image abuse

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.2 Privilege Escalation Techniques](../modules/02-hunter/06-attacker-techniques/02-privilege-escalation/) | Hunter, SOC, CTI |

See also: [privilege escalation techniques](#privilege-escalation-techniques), [indicators associated with privilege escalation](#indicators-associated-with-privilege-escalation)

### common cognitive biases that affect analysis

Also: confirmation anchoring availability premature closure

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.4 Cognitive Biases and Mitigation](../modules/03-cti/02-tradecraft/04-cognitive-biases/) | CTI, Hunter |

See also: [impact of biases on intelligence products](#impact-of-biases-on-intelligence-products), [techniques to mitigate cognitive biases](#techniques-to-mitigate-cognitive-biases)

### common data sources for infrastructure enrichment

Also: RDAP SOA PDNS TIP as infra sources, classroom infra source set

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/) | CTI, Hunter |

How to *read* those sources was taught in [3.5.1 RDAP and WHOIS Concepts](../modules/03-cti/05-rdap-whois/), [3.6.1 Advanced DNS Concepts](../modules/03-cti/06-advanced-dns/), and [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/).

See also: [pivoting concepts and techniques](#pivoting-concepts-and-techniques), [pivot from a seed indicator to additional adversary infrastructure](#pivot-from-a-seed-indicator-to-additional-adversary-infrastructure)

### common estimative terms and their meaning

Also: likely, even chance, remote, estimative term card

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.1 Estimative Language](../modules/03-cti/02-tradecraft/01-estimative-language/) | CTI, Hunter |

See also: [purpose of estimative language](#purpose-of-estimative-language), [use estimative language in an analytic judgment](#use-estimative-language-in-an-analytic-judgment)

### common reasons intelligence fails to be actionable

Also: IOC list only, too late, no so-what, not actionable

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.5 Ensuring Intelligence Is Actionable](../modules/03-cti/01-core-intel/05-actionable-intelligence/) | CTI, Hunter |

See also: [characteristics of actionable intelligence](#characteristics-of-actionable-intelligence), [evaluate whether intelligence is actionable](#evaluate-whether-intelligence-is-actionable)

### common persistence locations (Run, Services)

Also: Run key, RunOnce, Services key, registry persistence locations as examples

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.4 Registry Activity](../modules/01-soc/01-endpoint/04-registry-activity/) | SOC, Hunter, CTI |

Persistence *techniques* are [2.6.1 Persistence Techniques](../modules/02-hunter/06-attacker-techniques/01-persistence/).

See also: [registry activity](#registry-activity), [registry-based persistence](#registry-based-persistence)

### conducting or participating in a shift changeover

Also: handoff line, who runs the changeover, reject informal shift change

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.7.1 Shift Changeover Process](../modules/01-soc/07-shift-change/01-changeover-process/) | SOC, Hunter, CTI |

See also: [shift change participants](#shift-change-participants), [changeover report record location](#changeover-report-record-location)

### conn log

Also: `conn`, connection log, Zeek conn

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |
| Used | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |
| Used | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

1.2.1 teaches that the log exists and what it is for. 1.2.2 teaches fields, states, and analysis.

### conn_state

Also: connection state, how the connection ended

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

Common values taught here: `SF`, `S0`, `S1`, `REJ`, `RSTO`, `RSTR`, `RSTOS0`, `RSTRH`, `SH`, `SHR`, `OTH`.

See also: [SF](#sf), [S0](#s0), [REJ](#rej), [scanning](#scanning)

### conn_uids (link to other Zeek logs)

Also: files.conn_uids, connection UIDs on the files log

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.7 Files Engine](../modules/01-soc/02-zeek/07-files-engine/) | SOC, Hunter, CTI |

See also: [files log](#files-log), [uid](#uid)

### creating a SIEM rule from log fields or from SIGMA

Also: SIEM from SIGMA, SIEM from log fields, propose a SIEM detection

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.4 SIEM Rules](../modules/01-soc/03-detection/04-siem-rules/) | SOC, Hunter, CTI |

See also: [SIEM detection rules / correlation searches](#siem-detection-rules--correlation-searches), [how SIGMA translates to SIEM queries](#how-sigma-translates-to-siem-queries)

### convert external findings to internal queries

Also: convert to SIEM query, convert to Zeek query, internal query from enrichment

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |

See also: [hunting leads from external tools](#hunting-leads-from-external-tools), [tool capabilities for hunting](#tool-capabilities-for-hunting)

### criteria for TTP applicability to the environment

Also: Harbor platform and path, applicable vs relevant TTP, classroom apply criteria

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.2 Extracting Applicable TTPs from Intelligence Reports](../modules/03-cti/08-enrichment/02-applicable-ttps/) | CTI, Hunter |

Organizational impact is later (`3.8.4`). Harbor facts are [1.8.1 Environment Orientation](../modules/01-soc/08-site-specific/01-environment-orientation/).

See also: [extract applicable TTPs from an intelligence report](#extract-applicable-ttps-from-an-intelligence-report), [identifying relevant TTPs in a report](#identifying-relevant-ttps-in-a-report)

### crown jewel / critical assets

Also: pay-db-01, crown jewel host, critical asset

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.1 Environment Orientation](../modules/01-soc/08-site-specific/01-environment-orientation/) | SOC, Hunter, CTI |

See also: [key network segments and data flow](#key-network-segments-and-data-flow), [site-specific incident response processes](#site-specific-incident-response-processes)

### Cyber Kill Chain in intelligence analysis

Also: advanced Kill Chain for CTI, Kill Chain in intel products, supported Kill Chain stages in a product

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.3 Cyber Kill Chain in Intelligence Analysis](../modules/03-cti/07-frameworks/03-kill-chain-cti/) | CTI, Hunter |
| Used | [3.7.4 Defender’s ThreatMesh Framework (DTF) for Infrastructure Discovery](../modules/03-cti/07-frameworks/04-dtf/) | CTI, Hunter |

SOC single-row staging is [1.5.3 Cyber Kill Chain](../modules/01-soc/05-frameworks/03-cyber-kill-chain/).

See also: [place a report or activity set on the Kill Chain](#place-a-report-or-activity-set-on-the-kill-chain), [identify the Kill Chain stage of observed or reported activity](#identify-the-kill-chain-stage-of-observed-or-reported-activity), [how DTF complements ATT&CK, Diamond, and Kill Chain](#how-dtf-complements-attck-diamond-and-kill-chain)

### Cyber Kill Chain purpose

Also: Kill Chain, Lockheed Martin Kill Chain

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.3 Cyber Kill Chain](../modules/01-soc/05-frameworks/03-cyber-kill-chain/) | SOC, Hunter, CTI |
| Used | [3.7.3 Cyber Kill Chain in Intelligence Analysis](../modules/03-cti/07-frameworks/03-kill-chain-cti/) | CTI, Hunter |

See also: [Kill Chain stages](#kill-chain-stages), [identifying the stage and rejecting the previous or next](#identifying-the-stage-and-rejecting-the-previous-or-next), [Cyber Kill Chain in intelligence analysis](#cyber-kill-chain-in-intelligence-analysis)

---

## D

### develop or refine intelligence requirements

Also: draft a PIR, refine a requirement

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.4 Intelligence Requirements](../modules/03-cti/01-core-intel/04-intelligence-requirements/) | CTI, Hunter |

See also: [purpose of intelligence requirements](#purpose-of-intelligence-requirements), [translate stakeholder questions into clear intelligence requirements](#translate-stakeholder-questions-into-clear-intelligence-requirements)

### Diamond Model application in CTI

Also: advanced Diamond for CTI, Diamond in intel products

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.2 Diamond Model Application in CTI](../modules/03-cti/07-frameworks/02-diamond-cti/) | CTI, Hunter |
| Used | [3.7.4 Defender’s ThreatMesh Framework (DTF) for Infrastructure Discovery](../modules/03-cti/07-frameworks/04-dtf/) | CTI, Hunter |

SOC incident cards are [1.5.2 Diamond Model](../modules/01-soc/05-frameworks/02-diamond-model/). Actor profile is later (`3.11`).

See also: [apply the Diamond Model to an intelligence problem](#apply-the-diamond-model-to-an-intelligence-problem), [reject filling Adversary from a vendor name](#reject-filling-adversary-from-a-vendor-name), [how DTF complements ATT&CK, Diamond, and Kill Chain](#how-dtf-complements-attck-diamond-and-kill-chain)

### Diamond Model purpose

Also: Diamond Model, intrusion diamond

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.2 Diamond Model](../modules/01-soc/05-frameworks/02-diamond-model/) | SOC, Hunter, CTI |
| Used | [3.7.2 Diamond Model Application in CTI](../modules/03-cti/07-frameworks/02-diamond-cti/) | CTI, Hunter |

See also: [Diamond vertices: Adversary, Capability, Infrastructure, Victim](#diamond-vertices-adversary-capability-infrastructure-victim), [Diamond Model application in CTI](#diamond-model-application-in-cti)

### Diamond vertices: Adversary, Capability, Infrastructure, Victim

Also: Adversary vertex, Capability vertex, Infrastructure vertex, Victim vertex

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.2 Diamond Model](../modules/01-soc/05-frameworks/02-diamond-model/) | SOC, Hunter, CTI |
| Used | [3.7.2 Diamond Model Application in CTI](../modules/03-cti/07-frameworks/02-diamond-cti/) | CTI, Hunter |

See also: [filling four vertices and naming the weakest](#filling-four-vertices-and-naming-the-weakest), [using Diamond for analysis and attribution](#using-diamond-for-analysis-and-attribution)

### DTF pivot tactics and pivots

Also: PTA0001 Domain, PTA0002 IP, P0101.010, real DTF IDs

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.4 Defender’s ThreatMesh Framework (DTF) for Infrastructure Discovery](../modules/03-cti/07-frameworks/04-dtf/) | CTI, Hunter |

Source of truth: [defenders-threatmesh-framework](https://github.com/MalasadaTech/defenders-threatmesh-framework). No scoring methodology.

See also: [purpose of DTF (discover additional adversary infrastructure)](#purpose-of-dtf-discover-additional-adversary-infrastructure), [apply DTF from a known-bad seed](#apply-dtf-from-a-known-bad-seed), [reject a weak DTF pivot](#reject-a-weak-dtf-pivot)

### data

Also: raw data, raw observation, unprocessed fact

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.1 Data, Information, and Intelligence](../modules/03-cti/01-core-intel/01-data-info-intel/) | CTI, Hunter |
| Used | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |
| Used | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [information](#information), [intelligence](#intelligence)

### detection gaps

Also: detection gap, data exists no alert, missed detection

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.1 Purpose of Threat Hunting](../modules/02-hunter/01-purpose/) | Hunter, SOC, CTI |
| Used | [2.2.1 Hunt Types](../modules/02-hunter/02-methodology/01-hunt-types/) | Hunter, SOC, CTI |
| Used | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |
| Used | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |

See also: [visibility gaps](#visibility-gaps), [activity missed by existing security mechanisms](#activity-missed-by-existing-security-mechanisms)

### DGA

Also: domain generation algorithm

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

See also: [NXDOMAIN](#nxdomain)

### distinction between data, information, and intelligence

Also: data vs information vs intelligence, three terms

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.1 Data, Information, and Intelligence](../modules/03-cti/01-core-intel/01-data-info-intel/) | CTI, Hunter |
| Used | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

See also: [data](#data), [information](#information), [intelligence](#intelligence)

### dissemination

Also: disseminate, deliver intelligence, intelligence dissemination

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |
| Used | [3.11.2 Disseminating Intelligence to the Correct Audiences](../modules/03-cti/11-production/02-dissemination/) | CTI, Hunter |

Production and dissemination *process* depth is [3.11.1 Creating Finished Intelligence Products](../modules/03-cti/11-production/01-finished-products/) and [3.11.2 Disseminating Intelligence to the Correct Audiences](../modules/03-cti/11-production/02-dissemination/).

See also: [intelligence lifecycle](#intelligence-lifecycle), [disseminate through approved channels](#disseminate-through-approved-channels)

### dns log

Also: `dns`, Zeek dns

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |
| Used | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

1.2.1 teaches that the log exists. 1.2.3 teaches fields, query types, response codes, and analysis.

### DNS tunneling

Also: TXT tunneling, covert DNS channel

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

See also: [qtype_name](#qtype_name)

### domain / URL (endpoint-logged)

Also: DestinationHostname, RemoteUrl, QueryName, endpoint-logged domain

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.3 Network Activity (Endpoint)](../modules/01-soc/01-endpoint/03-network-activity/) | SOC, Hunter, CTI |

See also: [network activity (endpoint)](#network-activity-endpoint), [Sysmon 3 / 22 and DeviceNetworkEvents](#sysmon-3--22-and-devicenetworkevents)

### duration

Also: `duration`, connection length

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

See also: [beaconing](#beaconing)

---

## E

### edge firewall / choke points

Also: fw-edge, fw-ot, network choke point

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.1 Environment Orientation](../modules/01-soc/08-site-specific/01-environment-orientation/) | SOC, Hunter, CTI |

See also: [path to the internet / network egress](#path-to-the-internet--network-egress), [PCAP collection points / sensors](#pcap-collection-points--sensors)

### email flow and related systems

Also: mail-edge, MX path, email flow vs egress

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.1 Environment Orientation](../modules/01-soc/08-site-specific/01-environment-orientation/) | SOC, Hunter, CTI |

See also: [path to the internet / network egress](#path-to-the-internet--network-egress), [identifying which orientation fact applies and rejecting the adjacent fact](#identifying-which-orientation-fact-applies-and-rejecting-the-adjacent-fact)

### escalation timeline when more information is needed

Also: blocked escalate clock, escalate-for-more-info

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.6.2 Reporting Timelines](../modules/01-soc/06-reporting/02-reporting-timelines/) | SOC, Hunter, CTI |

See also: [submit timelines by report type](#submit-timelines-by-report-type), [identifying which report timeline applies and whether it is at risk](#identifying-which-report-timeline-applies-and-whether-it-is-at-risk)

### empty SNI

See [missing SNI](#missing-sni).

### enrich or pivot using an external tool

Also: one hop, classroom pivot, not Relations graph

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/) | CTI, Hunter |
| Used | [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/) | CTI, Hunter |

See also: [select the appropriate external tool](#select-the-appropriate-external-tool), [when to use each external tool in the intelligence process](#when-to-use-each-external-tool-in-the-intelligence-process)

### evaluation and feedback

Also: feedback, evaluation, intelligence feedback loop

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

See also: [intelligence lifecycle](#intelligence-lifecycle)

### evaluate whether intelligence is actionable

Also: score the five checks, actionable pass fail

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.5 Ensuring Intelligence Is Actionable](../modules/03-cti/01-core-intel/05-actionable-intelligence/) | CTI, Hunter |

See also: [characteristics of actionable intelligence](#characteristics-of-actionable-intelligence), [actionable for a hunt](#actionable-for-a-hunt)

### explain an Admiralty Code rating

Also: what C3 means, what F1 means

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.3 Admiralty Code](../modules/03-cti/02-tradecraft/03-admiralty-code/) | CTI, Hunter |

See also: [combining Admiralty ratings](#combining-admiralty-ratings), [source reliability scale](#source-reliability-scale)

### explain how a given requirement drives analytic work

Also: what the PIR stops you collecting, drive collection and analysis

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.4 Intelligence Requirements](../modules/03-cti/01-core-intel/04-intelligence-requirements/) | CTI, Hunter |

See also: [how requirements drive collection and analysis](#how-requirements-drive-collection-and-analysis), [develop or refine intelligence requirements](#develop-or-refine-intelligence-requirements)

### extract and interpret certificate information from a file

Also: interpret signer issuer validity, signed is not trusted

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.4.1 Hashing and Similarity Concepts](../modules/03-cti/04-file-similarity/) | CTI, Hunter |

See also: [certificate / code-signing information](#certificate--code-signing-information), [use file similarity hashes to identify related samples](#use-file-similarity-hashes-to-identify-related-samples)

### extract and interpret RDAP/WHOIS fields

Also: redacted is not empty, cloud org is not the actor

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.5.1 RDAP and WHOIS Concepts](../modules/03-cti/05-rdap-whois/) | CTI, Hunter |

See also: [key RDAP/WHOIS fields for enrichment and attribution](#key-rdapwhois-fields-for-enrichment-and-attribution), [query RDAP/WHOIS for a domain or IP](#query-rdapwhois-for-a-domain-or-ip)

### event engine

Also: Zeek events, `connection_established`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

### extract applicable TTPs from an intelligence report

Also: applicable TTP line, dual-gate TTP extract, Harbor-applicable IDs

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.2 Extracting Applicable TTPs from Intelligence Reports](../modules/03-cti/08-enrichment/02-applicable-ttps/) | CTI, Hunter |

Evidence-bound mapping is [3.7.1 MITRE ATT&CK for CTI Analysis and Reporting](../modules/03-cti/07-frameworks/01-attck-cti/).

See also: [criteria for TTP applicability to the environment](#criteria-for-ttp-applicability-to-the-environment), [reject a TTP that does not apply here](#reject-a-ttp-that-does-not-apply-here)

### jobs in one sentence

Also: SOC analyst, CTI, hunter, detection engineer, IR, firewall IA one-liners

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.2 Jobs in one sentence](../modules/00-intro/02-jobs-in-one-sentence/) | SOC, Hunter, CTI, DE |
| Used | [0.3 How work can move](../modules/00-intro/03-how-work-moves/) | SOC, Hunter, CTI, DE |
| Used | [0.4 Where the jobs lightly overlap](../modules/00-intro/04-where-jobs-overlap/) | SOC, Hunter, CTI, DE |

See also: [what a SOC is](#what-a-soc-is), [how work can move from an alert](#how-work-can-move-from-an-alert), [the product is different](#the-product-is-different)

### same host, log, or domain

Also: same evidence on more than one desk

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.4 Where the jobs lightly overlap](../modules/00-intro/04-where-jobs-overlap/) | SOC, Hunter, CTI, DE |

See also: [the product is different](#the-product-is-different)

### the product is different

Also: close or escalate an alert, intel note, hunt, rule

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.4 Where the jobs lightly overlap](../modules/00-intro/04-where-jobs-overlap/) | SOC, Hunter, CTI, DE |

See also: [same host, log, or domain](#same-host-log-or-domain), [two hats still two products](#two-hats-still-two-products)

### asking the next desk is not that desk’s whole job

Also: asking is not doing, RFI is not the intel note

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.4 Where the jobs lightly overlap](../modules/00-intro/04-where-jobs-overlap/) | SOC, Hunter, CTI, DE |

See also: [the product is different](#the-product-is-different), [RFI to intel](#rfi-to-intel)

### two hats still two products

Also: smaller shop, one person two jobs, products stay clear

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.4 Where the jobs lightly overlap](../modules/00-intro/04-where-jobs-overlap/) | SOC, Hunter, CTI, DE |

See also: [the product is different](#the-product-is-different), [jobs in one sentence](#jobs-in-one-sentence)

### how this course is laid out

Also: SOC then CTI then hunting then detection engineers

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.5 How this course is laid out](../modules/00-intro/05-course-layout/) | SOC, Hunter, CTI, DE |

See also: [detections before the alert queue](#detections-before-the-alert-queue), [site-specific comes later](#site-specific-comes-later)

### detections before the alert queue

Also: learn what detections are first, 1.3 before 1.4

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.5 How this course is laid out](../modules/00-intro/05-course-layout/) | SOC, Hunter, CTI, DE |

See also: [how this course is laid out](#how-this-course-is-laid-out)

### site-specific comes later

Also: how we do it here differs by shop

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.5 How this course is laid out](../modules/00-intro/05-course-layout/) | SOC, Hunter, CTI, DE |

See also: [how this course is laid out](#how-this-course-is-laid-out)

### PRD / DYA companion story

Also: one PRD DYA incident after the lessons, same flow

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.5 How this course is laid out](../modules/00-intro/05-course-layout/) | SOC, Hunter, CTI, DE |

See also: [DYA and PRD are course fiction](#dya-and-prd-are-course-fiction), [how work can move from an alert](#how-work-can-move-from-an-alert)

### name the next hand-off and whose product it is

Also: 0.5.1, not how the site files the ticket

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.5 How this course is laid out](../modules/00-intro/05-course-layout/) | SOC, Hunter, CTI, DE |

See also: [the product is different](#the-product-is-different), [how work can move from an alert](#how-work-can-move-from-an-alert)

### what a SOC is

Also: Security Operations Center, watch and start the response

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.1 What a SOC is](../modules/00-intro/01-what-a-soc-is/) | SOC, Hunter, CTI, DE |

See also: [a SOC is a team sport](#a-soc-is-a-team-sport), [DYA and PRD are course fiction](#dya-and-prd-are-course-fiction)

### a SOC is a team sport

Also: more than one job next to the SOC

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.1 What a SOC is](../modules/00-intro/01-what-a-soc-is/) | SOC, Hunter, CTI, DE |

See also: [what a SOC is](#what-a-soc-is)

### DYA and PRD are course fiction

Also: Dixon Yamada and Associates, Pink River Dolphin, not site policy

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.1 What a SOC is](../modules/00-intro/01-what-a-soc-is/) | SOC, Hunter, CTI, DE |
| Used | [0.5 How this course is laid out](../modules/00-intro/05-course-layout/) | SOC, Hunter, CTI, DE |

See also: [what a SOC is](#what-a-soc-is), [PRD / DYA companion story](#prd--dya-companion-story)

### what an IOC is versus a TTP

Also: IOC vs TTP, observable vs behavior

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.3 IOC Handling and Enrichment Concepts](../modules/03-cti/08-enrichment/03-ioc-handling/) | CTI, Hunter |

See also: [IOC handling rules (keep, expire, reject)](#ioc-handling-rules-keep-expire-reject), [extract applicable TTPs from an intelligence report](#extract-applicable-ttps-from-an-intelligence-report)

### IOC handling rules (keep, expire, reject)

Also: keep cited IOC, expire stale IOC, reject uncited IOC

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.3 IOC Handling and Enrichment Concepts](../modules/03-cti/08-enrichment/03-ioc-handling/) | CTI, Hunter |

See also: [what an IOC is versus a TTP](#what-an-ioc-is-versus-a-ttp), [record an enrichment without re-teaching the tool](#record-an-enrichment-without-re-teaching-the-tool)

### record an enrichment without re-teaching the tool

Also: enrich line, name the next lookup, 3.8.3.1

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.3 IOC Handling and Enrichment Concepts](../modules/03-cti/08-enrichment/03-ioc-handling/) | CTI, Hunter |

The generic hop sentence is [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/).

See also: [IOC handling rules (keep, expire, reject)](#ioc-handling-rules-keep-expire-reject), [link analysis and campaign tracking](#link-analysis-and-campaign-tracking)

### link analysis and campaign tracking

Also: same activity set, link line, not a group name

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.3 IOC Handling and Enrichment Concepts](../modules/03-cti/08-enrichment/03-ioc-handling/) | CTI, Hunter |

See also: [reject a vendor group name with no shared objects](#reject-a-vendor-group-name-with-no-shared-objects), [IOC handling rules (keep, expire, reject)](#ioc-handling-rules-keep-expire-reject)

### extracting hunt leads from CTI

Also: extract hunt leads, pull leads from a report, CTI extract for hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

See also: [hunt-suitable TTPs](#hunt-suitable-ttps), [hunt-suitable artifacts](#hunt-suitable-artifacts), [what to drop from CTI](#what-to-drop-from-cti)

### extracting TTPs onto ATT&CK IDs

Also: TTP extract to ATT&CK, extract behavior onto T-ID, evidence-bound ATT&CK map

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.1 MITRE ATT&CK for CTI Analysis and Reporting](../modules/03-cti/07-frameworks/01-attck-cti/) | CTI, Hunter |
| Used | [3.8.2 Extracting Applicable TTPs from Intelligence Reports](../modules/03-cti/08-enrichment/02-applicable-ttps/) | CTI, Hunter |

Copying printed IDs from a hunt-facing skim is [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/). Which extracted TTPs apply here is [3.8.2 Extracting Applicable TTPs from Intelligence Reports](../modules/03-cti/08-enrichment/02-applicable-ttps/).

See also: [map a report or activity set to ATT&CK](#map-a-report-or-activity-set-to-attck), [reject a neighbor ATT&CK ID](#reject-a-neighbor-attck-id), [extract applicable TTPs from an intelligence report](#extract-applicable-ttps-from-an-intelligence-report)

### examples of activity existing controls might miss

Also: examples existing controls might miss, identify missed-control examples

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.1 Purpose of Threat Hunting](../modules/02-hunter/01-purpose/) | Hunter, SOC, CTI |

See also: [activity missed by existing security mechanisms](#activity-missed-by-existing-security-mechanisms)

### execute a hunt by type

Also: execute by type, first hunt search, hunt execute

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.1 Hunt Types](../modules/02-hunter/02-methodology/01-hunt-types/) | Hunter, SOC, CTI |

See also: [hunt types](#hunt-types)


---

## F

### filling four vertices and naming the weakest

Also: weakest Diamond vertex, honest empty vertex

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.2 Diamond Model](../modules/01-soc/05-frameworks/02-diamond-model/) | SOC, Hunter, CTI |
| Used | [3.7.2 Diamond Model Application in CTI](../modules/03-cti/07-frameworks/02-diamond-cti/) | CTI, Hunter |

See also: [Diamond vertices: Adversary, Capability, Infrastructure, Victim](#diamond-vertices-adversary-capability-infrastructure-victim), [weakest vertex constrains the intel product](#weakest-vertex-constrains-the-intel-product)

### False Negative

Also: FN, missed detection, quiet and bad

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.2 Alert Classification](../modules/01-soc/04-alerts/02-classification/) | SOC, Hunter, CTI |

See also: [True Positive](#true-positive), [activity missed by existing security mechanisms](#activity-missed-by-existing-security-mechanisms)

### False Positive

Also: FP, fired and benign

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.2 Alert Classification](../modules/01-soc/04-alerts/02-classification/) | SOC, Hunter, CTI |

See also: [false positive cause: analyst or tool activity](#false-positive-cause-analyst-or-tool-activity), [classifying cases and citing evidence](#classifying-cases-and-citing-evidence)

### false positive cause: analyst or tool activity

Also: analyst testing a live rule, packet replay FP, scanner FP

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.3 Common False Positive Causes](../modules/01-soc/04-alerts/03-false-positive-causes/) | SOC, Hunter, CTI |

See also: [false positive cause: untuned or overly broad logic](#false-positive-cause-untuned-or-overly-broad-logic)

### false positive cause: untuned or overly broad logic

Also: over-broad detection, any-PowerShell rule, untuned logic

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.3 Common False Positive Causes](../modules/01-soc/04-alerts/03-false-positive-causes/) | SOC, Hunter, CTI |

See also: [identifying the cause class and what you would change](#identifying-the-cause-class-and-what-you-would-change)

### file create / rename-move / delete / modify / read

Also: FileCreated, FileRenamed, FileDeleted, FileModified, FileRead, Sysmon Event ID 11, Sysmon Event ID 23, Sysmon Event ID 26

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.2 File System Activity](../modules/01-soc/01-endpoint/02-file-system-activity/) | SOC, Hunter, CTI |

See also: [file system activity](#file-system-activity), [Sysmon 11 / 23 / 26 and DeviceFileEvents](#sysmon-11--23--26-and-devicefileevents)

### file hashes

Also: file SHA256, DeviceFileEvents SHA256, file hash

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.2 File System Activity](../modules/01-soc/01-endpoint/02-file-system-activity/) | SOC, Hunter, CTI |
| Used | [1.1.5 Image and Driver Load Activity](../modules/01-soc/01-endpoint/05-image-driver-load/) | SOC, Hunter, CTI |
| Used | [1.2.7 Files Engine](../modules/01-soc/02-zeek/07-files-engine/) | SOC, Hunter, CTI |

See also: [file system activity](#file-system-activity), [hashes and original filename](#hashes-and-original-filename), [files-log hashes (MD5, SHA1, SHA256)](#files-log-hashes-md5-sha1-sha256)

### file system activity

Also: file events, file telemetry, host file activity, DeviceFileEvents

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.2 File System Activity](../modules/01-soc/01-endpoint/02-file-system-activity/) | SOC, Hunter, CTI |

See also: [file create / rename-move / delete / modify / read](#file-create--rename-move--delete--modify--read), [path, name, and extension](#path-name-and-extension)

### files log

Also: `files`, Zeek files

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |
| Taught | [1.2.7 Files Engine](../modules/01-soc/02-zeek/07-files-engine/) | SOC, Hunter, CTI |

1.2.1 teaches that the log exists. 1.2.7 teaches filename, MIME, hashes, tx/rx hosts, and `conn_uids`.

### filename (files log)

Also: files.filename, Zeek filename

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.7 Files Engine](../modules/01-soc/02-zeek/07-files-engine/) | SOC, Hunter, CTI |

See also: [files log](#files-log), [MIME type](#mime-type)

### files-log hashes (MD5, SHA1, SHA256)

Also: files.md5, files.sha1, files.sha256, Zeek file hash

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.7 Files Engine](../modules/01-soc/02-zeek/07-files-engine/) | SOC, Hunter, CTI |

See also: [files log](#files-log), [file hashes](#file-hashes)

### flow of the intelligence lifecycle

Also: intelligence cycle flow, lifecycle loop, not a one-way pipeline

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

See also: [intelligence lifecycle](#intelligence-lifecycle)

---

## H

### hand off to detections / IR

Also: hand off CTI, detections hand off, IR hand off from a report

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.1 Assessing CTI for Hunting Value](../modules/02-hunter/04-cti-for-hunters/01-assessing-cti/) | Hunter, SOC, CTI |

See also: [assessing CTI for hunting value](#assessing-cti-for-hunting-value), [hunt-worthy CTI](#hunt-worthy-cti)

### hashes and original filename

Also: process SHA256, OriginalFileName, PE original filename

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.1 Process Activity](../modules/01-soc/01-endpoint/01-process-activity/) | SOC, Hunter, CTI |
| Used | [1.1.2 File System Activity](../modules/01-soc/01-endpoint/02-file-system-activity/) | SOC, Hunter, CTI |
| Used | [1.1.5 Image and Driver Load Activity](../modules/01-soc/01-endpoint/05-image-driver-load/) | SOC, Hunter, CTI |

See also: [process activity](#process-activity), [PID, name, and command line](#pid-name-and-command-line), [file hashes](#file-hashes)

### history

Also: `history`, Zeek history flags

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

3-level: awareness. 5- and 7-level: read the flag string.

### hives and key → value

Also: registry hive, HKLM, HKCU, TargetObject, RegistryKey, RegistryValueName

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.4 Registry Activity](../modules/01-soc/01-endpoint/04-registry-activity/) | SOC, Hunter, CTI |

See also: [registry activity](#registry-activity), [registry set / delete / rename](#registry-set--delete--rename)

### host-observed vs Zeek

Also: host-observed network, endpoint vs network sensor, 1.1.3 vs 1.2

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.3 Network Activity (Endpoint)](../modules/01-soc/01-endpoint/03-network-activity/) | SOC, Hunter, CTI |

See also: [network activity (endpoint)](#network-activity-endpoint), [initiating process (endpoint network)](#initiating-process-endpoint-network)

### HTTP host

Also: http.host, Host header

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.5 HTTP Engine](../modules/01-soc/02-zeek/05-http-engine/) | SOC, Hunter, CTI |

See also: [http log](#http-log), [URI / URL](#uri--url)

### how work can move from an alert

Also: path after an alert, one possible path, not every shop

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.3 How work can move](../modules/00-intro/03-how-work-moves/) | SOC, Hunter, CTI, DE |

See also: [jobs in one sentence](#jobs-in-one-sentence), [RFI to intel](#rfi-to-intel), [hunt package and block list as later hand-offs](#hunt-package-and-block-list-as-later-hand-offs)

### how a STIX bundle seeds a hunt

Also: STIX bundle seeds a hunt, bundle as hunt seed, not how to author STIX

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

Authoring STIX is [3.10.1 Core STIX Objects](../modules/03-cti/10-stix/01-core-objects/) and [3.10.2 How STIX Objects Are Used in Intelligence Production](../modules/03-cti/10-stix/02-stix-production/), not this module.

See also: [STIX as hunt input](#stix-as-hunt-input), [turning STIX objects into hunt leads](#turning-stix-objects-into-hunt-leads)

### how SIGMA translates to SIEM queries

Also: SIGMA to SIEM, SIGMA conversion, logsource to table

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.1 SIGMA Rules](../modules/01-soc/03-detection/01-sigma-rules/) | SOC, Hunter, CTI |
| Used | [1.3.4 SIEM Rules](../modules/01-soc/03-detection/04-siem-rules/) | SOC, Hunter, CTI |

See also: [SIGMA rules](#sigma-rules), [creating a SIEM rule from log fields or from SIGMA](#creating-a-siem-rule-from-log-fields-or-from-sigma)

### how Suricata rules relate to Zeek

Also: Suricata vs Zeek, signature vs parsed session

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.2 Suricata Rules](../modules/01-soc/03-detection/02-suricata-rules/) | SOC, Hunter, CTI |

See also: [Suricata rules](#suricata-rules), [http log](#http-log)

### how to download PCAP

Also: PCAP-REQ, pcap.harbor.internal, hot vs warm PCAP

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.2 PCAP Handling](../modules/01-soc/08-site-specific/02-pcap-handling/) | SOC, Hunter, CTI |

See also: [what tool to use to view PCAP](#what-tool-to-use-to-view-pcap), [PCAP collection points / sensors](#pcap-collection-points--sensors)

### how estimative language communicates confidence and uncertainty

Also: likelihood vs confidence, two axes estimative

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.1 Estimative Language](../modules/03-cti/02-tradecraft/01-estimative-language/) | CTI, Hunter |

See also: [common estimative terms and their meaning](#common-estimative-terms-and-their-meaning), [levels of confidence in attribution](#levels-of-confidence-in-attribution)

### how requirements drive collection and analysis

Also: requirement drives work, PIR drives collect and analyze

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.4 Intelligence Requirements](../modules/03-cti/01-core-intel/04-intelligence-requirements/) | CTI, Hunter |

See also: [explain how a given requirement drives analytic work](#explain-how-a-given-requirement-drives-analytic-work), [purpose of intelligence requirements](#purpose-of-intelligence-requirements)

### how advanced DNS supports enrichment and infrastructure analysis

Also: stack SOA NS TXT, cluster on MNAME

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.6.1 Advanced DNS Concepts](../modules/03-cti/06-advanced-dns/) | CTI, Hunter |

See also: [SOA records](#soa-records), [use advanced DNS records to enrich or pivot](#use-advanced-dns-records-to-enrich-or-pivot)

### how DTF complements ATT&CK, Diamond, and Kill Chain

Also: DTF vs ATT&CK, DTF discovery not behavior, DTF does not replace Diamond

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.4 Defender’s ThreatMesh Framework (DTF) for Infrastructure Discovery](../modules/03-cti/07-frameworks/04-dtf/) | CTI, Hunter |

See also: [purpose of DTF (discover additional adversary infrastructure)](#purpose-of-dtf-discover-additional-adversary-infrastructure), [ATT&CK for CTI analysis and reporting](#attck-for-cti-analysis-and-reporting)

### how the TIP supports enrichment, analysis, and production

Also: TIP sighting, attach TIP object to draft

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.1 Internal Threat Intelligence Platform](../modules/03-cti/03-tools/01-internal-tip/) | CTI, Hunter |

See also: [search and retrieve from the internal TIP](#search-and-retrieve-from-the-internal-tip), [use the TIP for enrichment or analysis](#use-the-tip-for-enrichment-or-analysis)

### how YARA is used with files / memory

Also: YARA file scan, YARA memory scan

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.3 YARA Rules](../modules/01-soc/03-detection/03-yara-rules/) | SOC, Hunter, CTI |

See also: [YARA rules](#yara-rules), [files log](#files-log)

### http log

Also: `http`, Zeek http

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |
| Taught | [1.2.5 HTTP Engine](../modules/01-soc/02-zeek/05-http-engine/) | SOC, Hunter, CTI |

1.2.1 teaches that the log exists. 1.2.5 teaches method, host, URI, User-Agent, status, and analysis.

### HTTP method

Also: GET, POST, PUT, HEAD, http.method

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.5 HTTP Engine](../modules/01-soc/02-zeek/05-http-engine/) | SOC, Hunter, CTI |

See also: [http log](#http-log), [HTTP status code](#http-status-code)

### HTTP status code

Also: status_code, HTTP 200, HTTP 404, HTTP 401

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.5 HTTP Engine](../modules/01-soc/02-zeek/05-http-engine/) | SOC, Hunter, CTI |

See also: [http log](#http-log), [HTTP method](#http-method)

### hunt package and block list as later hand-offs

Also: extra infrastructure to firewall IA, hunt package to hunters and detection engineers

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.3 How work can move](../modules/00-intro/03-how-work-moves/) | SOC, Hunter, CTI, DE |

See also: [how work can move from an alert](#how-work-can-move-from-an-alert), [RFI to intel](#rfi-to-intel)

### hunt development concepts

Also: developing a hunt, hunt intake card, hunt planning card

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |

See also: [hunt hypothesis](#hunt-hypothesis), [scoping a hunt](#scoping-a-hunt), [prioritizing hunts](#prioritizing-hunts)

### hunt for a named persistence or privilege-escalation technique

Also: 2.6.3 hunt line, named technique hunt, unique pattern hunt

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.3 Hunt for Specific Persistence or Privilege Escalation Techniques](../modules/02-hunter/06-attacker-techniques/03-hunt-specific/) | Hunter, SOC, CTI |

Recognition is [2.6.1 Persistence Techniques](../modules/02-hunter/06-attacker-techniques/01-persistence/) and [2.6.2 Privilege Escalation Techniques](../modules/02-hunter/06-attacker-techniques/02-privilege-escalation/).

See also: [reject an unbounded tactic hunt](#reject-an-unbounded-tactic-hunt), [reject hunting the wrong class (persist vs privesc)](#reject-hunting-the-wrong-class-persist-vs-privesc)

### hunt hand-off to SOC, IR, or CTI is site-specific

Also: hunt recipient chart, do not invent a hunt hand-off

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.7.3 Hunt Outputs and Hand-off](../modules/02-hunter/07-site-specific/03-hunt-outputs/) | Hunter, SOC, CTI |

See also: [expected hunt outputs are site-specific](#expected-hunt-outputs-are-site-specific), [produce required hunt outputs and perform proper hand-off](#produce-required-hunt-outputs-and-perform-proper-hand-off)

### hunt initiation and control are site-specific

Also: hunt queue varies, do not invent a hunt ticket

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.7.1 Hunt Control and Lead Management](../modules/02-hunter/07-site-specific/01-hunt-control/) | Hunter, SOC, CTI |

See also: [lead management is site-specific](#lead-management-is-site-specific), [follow the local process for initiating and controlling a hunt](#follow-the-local-process-for-initiating-and-controlling-a-hunt)

### hunt hypothesis

Also: developing a hunt hypothesis, documented hunt hypothesis, testable if/then

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |

See also: [hypothesis-driven hunt](#hypothesis-driven-hunt), [unique patterns or behaviors suitable for hunting](#unique-patterns-or-behaviors-suitable-for-hunting)

### hunt question from CTI leads

Also: hunt question those leads support, if/then from extracted leads

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

See also: [extracting hunt leads from CTI](#extracting-hunt-leads-from-cti), [hunt hypothesis](#hunt-hypothesis)

### hunt-relevant STIX objects

Also: hunt relevant objects in a bundle, identify hunt-relevant STIX

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

See also: [STIX objects a hunter uses](#stix-objects-a-hunter-uses), [STIX as hunt input](#stix-as-hunt-input)

### hunt-suitable artifacts

Also: hunt-suitable IOCs, hunt-suitable patterns, hunt-suitable behaviors from CTI

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |

See also: [TTPs vs IOCs vs behaviors](#ttps-vs-iocs-vs-behaviors), [what to drop from CTI](#what-to-drop-from-cti)

### hunt-suitable TTPs

Also: hunt suitable TTPs, extract TTPs for hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |

See also: [TTPs vs IOCs vs behaviors](#ttps-vs-iocs-vs-behaviors), [extracting hunt leads from CTI](#extracting-hunt-leads-from-cti)

### hunting leads from external tools

Also: actionable hunting lead, extract hunt lead, enrichment lead

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |

See also: [convert external findings to internal queries](#convert-external-findings-to-internal-queries), [unique patterns or behaviors suitable for hunting](#unique-patterns-or-behaviors-suitable-for-hunting)

### hunt types

Also: types of hunts, four hunt types, hunt type taxonomy

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.1 Hunt Types](../modules/02-hunter/02-methodology/01-hunt-types/) | Hunter, SOC, CTI |

See also: [intel-driven hunt](#intel-driven-hunt), [hypothesis-driven hunt](#hypothesis-driven-hunt), [reactive hunt](#reactive-hunt), [anomaly-based hunt](#anomaly-based-hunt)

### lead management is site-specific

Also: hunt lead board, park leads locally

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.7.1 Hunt Control and Lead Management](../modules/02-hunter/07-site-specific/01-hunt-control/) | Hunter, SOC, CTI |

See also: [hunt initiation and control are site-specific](#hunt-initiation-and-control-are-site-specific)

### hunt-worthy CTI

Also: hunt worthy report, hunt this report, CTI worth hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.1 Assessing CTI for Hunting Value](../modules/02-hunter/04-cti-for-hunters/01-assessing-cti/) | Hunter, SOC, CTI |
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |
| Used | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |

See also: [awareness-only CTI](#awareness-only-cti), [actionable for a hunt](#actionable-for-a-hunt)

### hypothesis-driven hunt

Also: hypothesis hunt, if/then hunt, testable hunt hypothesis

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.1 Hunt Types](../modules/02-hunter/02-methodology/01-hunt-types/) | Hunter, SOC, CTI |
| Used | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |

How to write and document the hypothesis is [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/).

See also: [hunt types](#hunt-types), [hunt hypothesis](#hunt-hypothesis), [anomaly-based hunt](#anomaly-based-hunt)

---

## I

### image and driver load activity

Also: image load, driver load, DLL load, DeviceImageLoadEvents

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.5 Image and Driver Load Activity](../modules/01-soc/01-endpoint/05-image-driver-load/) | SOC, Hunter, CTI |

See also: [user-mode image load vs kernel driver load](#user-mode-image-load-vs-kernel-driver-load), [Sysmon 6 / 7 and DeviceImageLoadEvents](#sysmon-6--7-and-deviceimageloadevents)

### identifying the report type and rejecting the adjacent type

Also: incident vs RFI, reject neighbor report type

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.6.1 Report Types](../modules/01-soc/06-reporting/01-report-types/) | SOC, Hunter, CTI |

See also: [incident report](#incident-report), [Request for Information (RFI)](#request-for-information-rfi)

### identifying which report timeline applies and whether it is at risk

Also: report clock at risk, submit vs blocked clock

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.6.2 Reporting Timelines](../modules/01-soc/06-reporting/02-reporting-timelines/) | SOC, Hunter, CTI |

See also: [submit timelines by report type](#submit-timelines-by-report-type), [escalation timeline when more information is needed](#escalation-timeline-when-more-information-is-needed)

### apply DTF from a known-bad seed

Also: DTF line, PTA plus P-ID, cite the shared characteristic

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.4 Defender’s ThreatMesh Framework (DTF) for Infrastructure Discovery](../modules/03-cti/07-frameworks/04-dtf/) | CTI, Hunter |

See also: [DTF pivot tactics and pivots](#dtf-pivot-tactics-and-pivots), [reject a weak DTF pivot](#reject-a-weak-dtf-pivot)

### identify the Kill Chain stage of observed or reported activity

Also: stage a report span, Kill Chain stage from a report, CTI Kill Chain stage line

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.3 Cyber Kill Chain in Intelligence Analysis](../modules/03-cti/07-frameworks/03-kill-chain-cti/) | CTI, Hunter |

Single-row staging is [1.5.3 Cyber Kill Chain](../modules/01-soc/05-frameworks/03-cyber-kill-chain/).

See also: [identifying the stage and rejecting the previous or next](#identifying-the-stage-and-rejecting-the-previous-or-next), [place a report or activity set on the Kill Chain](#place-a-report-or-activity-set-on-the-kill-chain)

### identifying the stage and rejecting the previous or next

Also: Kill Chain neighbor stage, not previous not next

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.3 Cyber Kill Chain](../modules/01-soc/05-frameworks/03-cyber-kill-chain/) | SOC, Hunter, CTI |
| Used | [3.7.3 Cyber Kill Chain in Intelligence Analysis](../modules/03-cti/07-frameworks/03-kill-chain-cti/) | CTI, Hunter |

See also: [Kill Chain stages](#kill-chain-stages), [using the Kill Chain to understand attack progression](#using-the-kill-chain-to-understand-attack-progression), [identify the Kill Chain stage of observed or reported activity](#identify-the-kill-chain-stage-of-observed-or-reported-activity)

### identifying the cause class and what you would change

Also: FP cause class plus change, class a or b and a change

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.3 Common False Positive Causes](../modules/01-soc/04-alerts/03-false-positive-causes/) | SOC, Hunter, CTI |

See also: [false positive cause: analyst or tool activity](#false-positive-cause-analyst-or-tool-activity), [false positive cause: untuned or overly broad logic](#false-positive-cause-untuned-or-overly-broad-logic)

### identifying which clock is at risk

Also: start clock at risk, close/escalate clock at risk

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.5 SLA / Response Time Goals](../modules/01-soc/04-alerts/05-sla-response-times/) | SOC, Hunter, CTI |

See also: [start clock (time to begin investigation)](#start-clock-time-to-begin-investigation), [close/escalate clock (time to process)](#closeescalate-clock-time-to-process)

### identifying relevant TTPs in a report

Also: relevant TTP in a report, TTP with a how, gate 1 TTP extract

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.2 Extracting Applicable TTPs from Intelligence Reports](../modules/03-cti/08-enrichment/02-applicable-ttps/) | CTI, Hunter |

See also: [extracting TTPs onto ATT&CK IDs](#extracting-ttps-onto-attck-ids), [criteria for TTP applicability to the environment](#criteria-for-ttp-applicability-to-the-environment)

### identifying which orientation fact applies and rejecting the adjacent fact

Also: orientation neighbor, egress vs email vs sensor gap

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.1 Environment Orientation](../modules/01-soc/08-site-specific/01-environment-orientation/) | SOC, Hunter, CTI |
| Used | [3.8.2 Extracting Applicable TTPs from Intelligence Reports](../modules/03-cti/08-enrichment/02-applicable-ttps/) | CTI, Hunter |

See also: [path to the internet / network egress](#path-to-the-internet--network-egress), [PCAP collection points / sensors](#pcap-collection-points--sensors), [criteria for TTP applicability to the environment](#criteria-for-ttp-applicability-to-the-environment)

### identify collection source classes for a requirement

Also: which collection class, OSINT vs internal first

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.8 Collection Sources and Methods](../modules/03-cti/01-core-intel/08-collection-sources/) | CTI, Hunter |

See also: [collection source classes (OSINT, commercial, internal)](#collection-source-classes-osint-commercial-internal), [plan collection against an intelligence requirement](#plan-collection-against-an-intelligence-requirement)

### identify potential cognitive bias in a judgment

Also: name the tilt, textual tell of bias

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.4 Cognitive Biases and Mitigation](../modules/03-cti/02-tradecraft/04-cognitive-biases/) | CTI, Hunter |

See also: [common cognitive biases that affect analysis](#common-cognitive-biases-that-affect-analysis), [apply a mitigation technique](#apply-a-mitigation-technique)

### interpret an SOA record

Also: MNAME RNAME serial, serial is not a hash

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.6.1 Advanced DNS Concepts](../modules/03-cti/06-advanced-dns/) | CTI, Hunter |

See also: [SOA records](#soa-records), [how advanced DNS supports enrichment and infrastructure analysis](#how-advanced-dns-supports-enrichment-and-infrastructure-analysis)

### interpret the likelihood expressed in an estimative statement

Also: read an estimative term, interpret likely vs high confidence

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.1 Estimative Language](../modules/03-cti/02-tradecraft/01-estimative-language/) | CTI, Hunter |

See also: [common estimative terms and their meaning](#common-estimative-terms-and-their-meaning), [use estimative language in an analytic judgment](#use-estimative-language-in-an-analytic-judgment)

### impact of biases on intelligence products

Also: omitted evidence, stuck first label, isolate too early

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.4 Cognitive Biases and Mitigation](../modules/03-cti/02-tradecraft/04-cognitive-biases/) | CTI, Hunter |

See also: [common cognitive biases that affect analysis](#common-cognitive-biases-that-affect-analysis), [identify potential cognitive bias in a judgment](#identify-potential-cognitive-bias-in-a-judgment)

### imphash

Also: import hash, PE import table hash

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.4.1 Hashing and Similarity Concepts](../modules/03-cti/04-file-similarity/) | CTI, Hunter |

See also: [ssdeep](#ssdeep), [use file similarity hashes to identify related samples](#use-file-similarity-hashes-to-identify-related-samples)

### incident report

Also: incident case record, IR case report

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.6.1 Report Types](../modules/01-soc/06-reporting/01-report-types/) | SOC, Hunter, CTI |

See also: [Request for Information (RFI)](#request-for-information-rfi), [other common report types](#other-common-report-types)

### indicators associated with privilege escalation

Also: privilege escalation indicators, integrity change, parent vs child identity, missing UAC consent

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.2 Privilege Escalation Techniques](../modules/02-hunter/06-attacker-techniques/02-privilege-escalation/) | Hunter, SOC, CTI |

See also: [privilege escalation techniques](#privilege-escalation-techniques), [recognizing privilege escalation techniques in logs or telemetry](#recognizing-privilege-escalation-techniques-in-logs-or-telemetry)

### information

Also: organized data, context, parsed alert, rewritten log story

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.1 Data, Information, and Intelligence](../modules/03-cti/01-core-intel/01-data-info-intel/) | CTI, Hunter |
| Used | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |
| Used | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [data](#data), [intelligence](#intelligence)

### information credibility scale

Also: Admiralty 1–6, confirmed probably possibly

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.3 Admiralty Code](../modules/03-cti/02-tradecraft/03-admiralty-code/) | CTI, Hunter |

See also: [source reliability scale](#source-reliability-scale), [combining Admiralty ratings](#combining-admiralty-ratings)

### initiating process (endpoint network)

Also: who talked, DeviceNetworkEvents InitiatingProcess, Sysmon 3 Image

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.3 Network Activity (Endpoint)](../modules/01-soc/01-endpoint/03-network-activity/) | SOC, Hunter, CTI |

See also: [network activity (endpoint)](#network-activity-endpoint), [parent-child process](#parent-child-process)

### initiating process (file events)

Also: file initiating process, who touched the file, DeviceFileEvents InitiatingProcess

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.2 File System Activity](../modules/01-soc/01-endpoint/02-file-system-activity/) | SOC, Hunter, CTI |
| Used | [1.1.3 Network Activity (Endpoint)](../modules/01-soc/01-endpoint/03-network-activity/) | SOC, Hunter, CTI |
| Used | [1.1.4 Registry Activity](../modules/01-soc/01-endpoint/04-registry-activity/) | SOC, Hunter, CTI |
| Used | [1.1.5 Image and Driver Load Activity](../modules/01-soc/01-endpoint/05-image-driver-load/) | SOC, Hunter, CTI |

See also: [file system activity](#file-system-activity), [parent-child process](#parent-child-process)

### initiating process (image load)

Also: who loaded the module, image-load initiating process, Event 7 Image

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.5 Image and Driver Load Activity](../modules/01-soc/01-endpoint/05-image-driver-load/) | SOC, Hunter, CTI |

See also: [image and driver load activity](#image-and-driver-load-activity), [parent-child process](#parent-child-process)

### initiating process (registry events)

Also: who changed the registry, DeviceRegistryEvents InitiatingProcess

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.4 Registry Activity](../modules/01-soc/01-endpoint/04-registry-activity/) | SOC, Hunter, CTI |

See also: [registry activity](#registry-activity), [parent-child process](#parent-child-process)

### integrity / user context

Also: integrity level, process user, Medium vs High vs SYSTEM

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.1 Process Activity](../modules/01-soc/01-endpoint/01-process-activity/) | SOC, Hunter, CTI |

See also: [process activity](#process-activity), [parent-child process](#parent-child-process)

### intelligence

Also: analytic judgment, decision support, finished intelligence, so what

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.1 Data, Information, and Intelligence](../modules/03-cti/01-core-intel/01-data-info-intel/) | CTI, Hunter |
| Used | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |
| Used | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [data](#data), [information](#information), [transformation from raw data to information to intelligence](#transformation-from-raw-data-to-information-to-intelligence)

### intelligence lifecycle

Also: intelligence cycle, intel lifecycle, intelligence process

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |
| Used | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [stages of the intelligence lifecycle](#stages-of-the-intelligence-lifecycle), [flow of the intelligence lifecycle](#flow-of-the-intelligence-lifecycle)

### intelligence types

Also: types of intelligence, intel types, four intelligence types

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [strategic intelligence](#strategic-intelligence), [operational intelligence](#operational-intelligence), [tactical intelligence](#tactical-intelligence), [technical intelligence](#technical-intelligence)

### intel-driven hunt

Also: intelligence-driven hunt, IOC hunt, bulletin hunt

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.1 Hunt Types](../modules/02-hunter/02-methodology/01-hunt-types/) | Hunter, SOC, CTI |

Extracting TTPs from a CTI report is a later item (2.4), not this module.

See also: [hunt types](#hunt-types)

### id.orig_h / id.resp_h

See [5-tuple](#5-tuple).

### IDS / IPS

See [Zeek vs signature-based IDS](#zeek-vs-signature-based-ids).

### issuer

See [certificate subject / issuer](#certificate-subject--issuer).

---

## J

### JA3

Also: `ja3`, JA3S, `ja3s`, TLS fingerprint, client hello fingerprint, server hello fingerprint

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

Taught as a lead, not a malware verdict. Fields are used only where the deployment logs them.

---

## K

### Key Assumptions Check

Also: KAC, must-be-true claims, if assumption false

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.2 Structured Analytic Techniques](../modules/03-cti/02-tradecraft/02-structured-techniques/) | CTI, Hunter |

See also: [Analysis of Competing Hypotheses (ACH)](#analysis-of-competing-hypotheses-ach), [purpose of structured analytic techniques](#purpose-of-structured-analytic-techniques)

### Kill Chain stages

Also: Reconnaissance Delivery Exploitation Installation C2 Actions on Objectives, Weaponization

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.3 Cyber Kill Chain](../modules/01-soc/05-frameworks/03-cyber-kill-chain/) | SOC, Hunter, CTI |
| Used | [3.7.3 Cyber Kill Chain in Intelligence Analysis](../modules/03-cti/07-frameworks/03-kill-chain-cti/) | CTI, Hunter |

See also: [Cyber Kill Chain purpose](#cyber-kill-chain-purpose), [Cyber Kill Chain in intelligence analysis](#cyber-kill-chain-in-intelligence-analysis)

### key network segments and data flow

Also: user VLAN, OT segment, Harbor segments

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.1 Environment Orientation](../modules/01-soc/08-site-specific/01-environment-orientation/) | SOC, Hunter, CTI |

See also: [path to the internet / network egress](#path-to-the-internet--network-egress), [crown jewel / critical assets](#crown-jewel--critical-assets)

### key differences between WHOIS and RDAP

Also: RDAP first, structured vs free text, HTTPS vs port 43

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.5.1 RDAP and WHOIS Concepts](../modules/03-cti/05-rdap-whois/) | CTI, Hunter |

See also: [purpose of WHOIS and RDAP](#purpose-of-whois-and-rdap), [query RDAP/WHOIS for a domain or IP](#query-rdapwhois-for-a-domain-or-ip)

### key RDAP/WHOIS fields for enrichment and attribution

Also: created registrar nameservers, IP CIDR org

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.5.1 RDAP and WHOIS Concepts](../modules/03-cti/05-rdap-whois/) | CTI, Hunter |

See also: [extract and interpret RDAP/WHOIS fields](#extract-and-interpret-rdapwhois-fields), [purpose of WHOIS and RDAP](#purpose-of-whois-and-rdap)

---

## L

### leadership awareness

Also: duty SOC lead awareness, notify leadership

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.6.3 Notification and Distribution](../modules/01-soc/06-reporting/03-notification-distribution/) | SOC, Hunter, CTI |

See also: [notification chart / matrix](#notification-chart--matrix), [routing a report (recipients, leadership, channel)](#routing-a-report-recipients-leadership-channel)

### levels of confidence in attribution

Also: low medium high attribution, classroom confidence scale

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.7 Attribution](../modules/03-cti/01-core-intel/07-attribution/) | CTI, Hunter |

See also: [assess attribution statements for confidence and evidence](#assess-attribution-statements-for-confidence-and-evidence), [purpose and challenges of attribution](#purpose-and-challenges-of-attribution)

### logging framework

Also: Zeek logs, TSV, JSON logs

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

---

## M

### mail from

Also: mailfrom, SMTP MAIL FROM, envelope from

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.6 SMTP Engine](../modules/01-soc/02-zeek/06-smtp-engine/) | SOC, Hunter, CTI |

See also: [smtp log](#smtp-log), [rcpt to](#rcpt-to)

### map a report or activity set to ATT&CK

Also: map a report to ATT&CK, map an activity set to ATT&CK, CTI ATT&CK map line

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.1 MITRE ATT&CK for CTI Analysis and Reporting](../modules/03-cti/07-frameworks/01-attck-cti/) | CTI, Hunter |

Alert mapping is [1.5.1 MITRE ATT&CK](../modules/01-soc/05-frameworks/01-attck/). Hunt planning maps are [2.5.1](../modules/02-hunter/05-framework-application/).

See also: [extracting TTPs onto ATT&CK IDs](#extracting-ttps-onto-attck-ids), [mapping observed activity to ATT&CK](#mapping-observed-activity-to-attck)

### mapping observed activity to ATT&CK

Also: map an alert to ATT&CK, tactic plus technique plus cite

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.1 MITRE ATT&CK](../modules/01-soc/05-frameworks/01-attck/) | SOC, Hunter, CTI |
| Used | [3.7.1 MITRE ATT&CK for CTI Analysis and Reporting](../modules/03-cti/07-frameworks/01-attck-cti/) | CTI, Hunter |

Hunt planning maps are [2.5.1](../modules/02-hunter/05-framework-application/). Report / activity-set maps are [3.7.1 MITRE ATT&CK for CTI Analysis and Reporting](../modules/03-cti/07-frameworks/01-attck-cti/).

See also: [ATT&CK tactics](#attck-tactics), [mapping hunts to ATT&CK](#mapping-hunts-to-attck), [map a report or activity set to ATT&CK](#map-a-report-or-activity-set-to-attck)

### mapping hunts to ATT&CK

Also: map a hunt plan to ATT&CK, map hunt findings to ATT&CK, ATT&CK tactics and techniques

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |

See also: [using MITRE ATT&CK for hunt planning](#using-mitre-attck-for-hunt-planning), [recording ATT&CK IDs from a report](#recording-attck-ids-from-a-report)

### message ID

Also: msg_id, SMTP Message-ID

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.6 SMTP Engine](../modules/01-soc/02-zeek/06-smtp-engine/) | SOC, Hunter, CTI |

See also: [smtp log](#smtp-log), [uid](#uid)

### MIME type

Also: mime_type, files MIME, application/pdf, application/x-dosexec

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.7 Files Engine](../modules/01-soc/02-zeek/07-files-engine/) | SOC, Hunter, CTI |

See also: [files log](#files-log), [filename (files log)](#filename-files-log)

### matching techniques: ASCII, hex, and regex

Also: ASCII match, hex match, regex match, pcre, YARA hex string

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.2 Suricata Rules](../modules/01-soc/03-detection/02-suricata-rules/) | SOC, Hunter, CTI |
| Taught | [1.3.3 YARA Rules](../modules/01-soc/03-detection/03-yara-rules/) | SOC, Hunter, CTI |
| Used | [1.3.4 SIEM Rules](../modules/01-soc/03-detection/04-siem-rules/) | SOC, Hunter, CTI |

See also: [Suricata rule options](#suricata-rule-options), [YARA strings and conditions](#yara-strings-and-conditions)

### matching techniques: regex and wildcards (SIEM)

Also: SIEM wildcard, SIEM regex, has vs matches regex

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.4 SIEM Rules](../modules/01-soc/03-detection/04-siem-rules/) | SOC, Hunter, CTI |

See also: [SIEM detection rules / correlation searches](#siem-detection-rules--correlation-searches), [matching techniques: ASCII, hex, and regex](#matching-techniques-ascii-hex-and-regex)

### missing SNI

Also: empty SNI, no `server_name`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

See also: [SNI](#sni)

### MITRE ATT&CK purpose and structure

Also: ATT&CK matrix, ATT&CK Enterprise

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.1 MITRE ATT&CK](../modules/01-soc/05-frameworks/01-attck/) | SOC, Hunter, CTI |
| Used | [3.7.1 MITRE ATT&CK for CTI Analysis and Reporting](../modules/03-cti/07-frameworks/01-attck-cti/) | CTI, Hunter |

See also: [ATT&CK tactics](#attck-tactics), [mapping observed activity to ATT&CK](#mapping-observed-activity-to-attck), [ATT&CK for CTI analysis and reporting](#attck-for-cti-analysis-and-reporting)

### MX

See [qtype_name](#qtype_name).

---

## N

### navigating and searching the internal TIP

Also: Harbor TIP search, indicator type filter

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.1 Internal Threat Intelligence Platform](../modules/03-cti/03-tools/01-internal-tip/) | CTI, Hunter |

See also: [purpose and core functions of the internal TIP](#purpose-and-core-functions-of-the-internal-tip), [search and retrieve from the internal TIP](#search-and-retrieve-from-the-internal-tip)

### network activity (endpoint)

Also: host network activity, endpoint network, DeviceNetworkEvents, Sysmon Event ID 3

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.3 Network Activity (Endpoint)](../modules/01-soc/01-endpoint/03-network-activity/) | SOC, Hunter, CTI |

See also: [host-observed vs Zeek](#host-observed-vs-zeek), [source / dest IP and port, protocol, direction](#source--dest-ip-and-port-protocol-direction)

### newly opened, updated, or closed reports (changeover)

Also: what changed this shift, opened updated closed this shift

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.7.2 Required Content of the Changeover Report](../modules/01-soc/07-shift-change/02-changeover-report/) | SOC, Hunter, CTI |

See also: [open / in-progress investigations (changeover)](#open--in-progress-investigations-changeover), [producing a complete changeover report](#producing-a-complete-changeover-report)

### notice log

Also: `notice`, Zeek notices

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

### notification chart / matrix

Also: who gets which report, notification matrix

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.6.3 Notification and Distribution](../modules/01-soc/06-reporting/03-notification-distribution/) | SOC, Hunter, CTI |

See also: [leadership awareness](#leadership-awareness), [approved reporting channels](#approved-reporting-channels)

### NOERROR

See [rcode_name](#rcode_name).

### NULL (DNS)

See [qtype_name](#qtype_name) and [DNS tunneling](#dns-tunneling).

### NXDOMAIN

Also: non-existent domain, `rcode_name = NXDOMAIN`, NXDOMAIN spikes

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

See also: [DGA](#dga), [rcode_name](#rcode_name)

---

## O

### ongoing / occurred-during-shift outages

Also: sensor down this shift, occurred outage, lost visibility this shift

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.7.2 Required Content of the Changeover Report](../modules/01-soc/07-shift-change/02-changeover-report/) | SOC, Hunter, CTI |

See also: [planned service outages](#planned-service-outages), [producing a complete changeover report](#producing-a-complete-changeover-report)

### open / in-progress investigations (changeover)

Also: still-open cases at changeover, in-progress investigations

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.7.2 Required Content of the Changeover Report](../modules/01-soc/07-shift-change/02-changeover-report/) | SOC, Hunter, CTI |

See also: [newly opened, updated, or closed reports (changeover)](#newly-opened-updated-or-closed-reports-changeover), [producing a complete changeover report](#producing-a-complete-changeover-report)

### operational intelligence

Also: operational intel, campaign intelligence, operational type

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [intelligence types](#intelligence-types)

### orig_bytes / resp_bytes

Also: byte counts, `orig_bytes`, `resp_bytes`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

See also: [beaconing](#beaconing)

### other common persistence methods

Also: service persistence, WMI persistence, logon script persistence

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.1 Persistence Techniques](../modules/02-hunter/06-attacker-techniques/01-persistence/) | Hunter, SOC, CTI |

See also: [persistence techniques](#persistence-techniques), [recognizing persistence techniques in logs or telemetry](#recognizing-persistence-techniques-in-logs-or-telemetry)

### other advanced DNS record types of intelligence value

Also: NS MX TXT SRV intel value

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.6.1 Advanced DNS Concepts](../modules/03-cti/06-advanced-dns/) | CTI, Hunter |

See also: [SOA records](#soa-records), [use advanced DNS records to enrich or pivot](#use-advanced-dns-records-to-enrich-or-pivot)

### other common report types

Also: informational report, awareness note, local report types

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.6.1 Report Types](../modules/01-soc/06-reporting/01-report-types/) | SOC, Hunter, CTI |

See also: [incident report](#incident-report), [Request for Information (RFI)](#request-for-information-rfi)

### other local categories

Also: other alert category, local SOC buckets

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.4 Common Alert Categorizations](../modules/01-soc/04-alerts/04-categorizations/) | SOC, Hunter, CTI |

See also: [assigning a category and ruling out the adjacent one](#assigning-a-category-and-ruling-out-the-adjacent-one)

---

## P

### potential organizational impact

Also: impact if true, so what here, not because clause

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.4 Threat Relevance and Organizational Impact](../modules/03-cti/08-enrichment/04-relevance-impact/) | CTI, Hunter |

See also: [relevance to this environment](#relevance-to-this-environment), [reject impact that skips the path](#reject-impact-that-skips-the-path)

### relevance to this environment

Also: so what here, relevant to Harbor estate, mission asset platform

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.4 Threat Relevance and Organizational Impact](../modules/03-cti/08-enrichment/04-relevance-impact/) | CTI, Hunter |

TTP apply is [3.8.2 Extracting Applicable TTPs from Intelligence Reports](../modules/03-cti/08-enrichment/02-applicable-ttps/).

See also: [potential organizational impact](#potential-organizational-impact), [reject impact that skips the path](#reject-impact-that-skips-the-path)

### parent-child process

Also: PPID, parent process, InitiatingProcess, ParentImage

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.1 Process Activity](../modules/01-soc/01-endpoint/01-process-activity/) | SOC, Hunter, CTI |
| Used | [1.1.2 File System Activity](../modules/01-soc/01-endpoint/02-file-system-activity/) | SOC, Hunter, CTI |
| Used | [1.1.3 Network Activity (Endpoint)](../modules/01-soc/01-endpoint/03-network-activity/) | SOC, Hunter, CTI |
| Used | [1.1.4 Registry Activity](../modules/01-soc/01-endpoint/04-registry-activity/) | SOC, Hunter, CTI |
| Used | [1.1.5 Image and Driver Load Activity](../modules/01-soc/01-endpoint/05-image-driver-load/) | SOC, Hunter, CTI |

See also: [process activity](#process-activity), [PID, name, and command line](#pid-name-and-command-line), [initiating process (file events)](#initiating-process-file-events)

### PCAP collection points / sensors

Also: span-1, span-2, no OT span, where sensors sit

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.1 Environment Orientation](../modules/01-soc/08-site-specific/01-environment-orientation/) | SOC, Hunter, CTI |

See also: [how to download PCAP](#how-to-download-pcap), [edge firewall / choke points](#edge-firewall--choke-points)

### path, hashes, signed vs unsigned

Also: ImageLoaded path, loaded-image hash, Signed, SignatureStatus

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.5 Image and Driver Load Activity](../modules/01-soc/01-endpoint/05-image-driver-load/) | SOC, Hunter, CTI |

See also: [image and driver load activity](#image-and-driver-load-activity), [file hashes](#file-hashes)

### path, name, and extension

Also: FolderPath, FileName, TargetFilename, file extension, double extension

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.2 File System Activity](../modules/01-soc/01-endpoint/02-file-system-activity/) | SOC, Hunter, CTI |

See also: [file system activity](#file-system-activity), [file create / rename-move / delete / modify / read](#file-create--rename-move--delete--modify--read)

### path to the internet / network egress

Also: fw-edge-01, fw-guest, NAT egress

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.1 Environment Orientation](../modules/01-soc/08-site-specific/01-environment-orientation/) | SOC, Hunter, CTI |

See also: [email flow and related systems](#email-flow-and-related-systems), [edge firewall / choke points](#edge-firewall--choke-points)

### persistence techniques

Also: persistence, persist after reboot, autorun methods

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.1 Persistence Techniques](../modules/02-hunter/06-attacker-techniques/01-persistence/) | Hunter, SOC, CTI |
| Used | [2.6.2 Privilege Escalation Techniques](../modules/02-hunter/06-attacker-techniques/02-privilege-escalation/) | Hunter, SOC, CTI |

See also: [registry-based persistence](#registry-based-persistence), [scheduled-task persistence](#scheduled-task-persistence)

### PID, name, and command line

Also: ProcessId, process name, CommandLine, ProcessCommandLine

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.1 Process Activity](../modules/01-soc/01-endpoint/01-process-activity/) | SOC, Hunter, CTI |

See also: [process activity](#process-activity), [parent-child process](#parent-child-process)

### pivot

See [uid](#uid).

### pivot from a seed indicator to additional adversary infrastructure

Also: infra hop from a seed, additional adversary domain or IP, CTI pivot line

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/) | CTI, Hunter |

DTF records the PTA/P pivot from that seed in [3.7.4 Defender’s ThreatMesh Framework (DTF) for Infrastructure Discovery](../modules/03-cti/07-frameworks/04-dtf/). The product here is the generic hop sentence, not a DTF ID line. Zeek `uid` joins are [uid](#uid).

See also: [pivoting concepts and techniques](#pivoting-concepts-and-techniques), [reject a weak or uncited infra pivot](#reject-a-weak-or-uncited-infra-pivot)

### pivoting concepts and techniques

Also: seed shared property additional infra, one cited hop, stop rule

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/) | CTI, Hunter |

See also: [common data sources for infrastructure enrichment](#common-data-sources-for-infrastructure-enrichment), [pivot from a seed indicator to additional adversary infrastructure](#pivot-from-a-seed-indicator-to-additional-adversary-infrastructure)

### place a report or activity set on the Kill Chain

Also: place a report on the Kill Chain, activity-set progression, CTI Kill Chain product list

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.3 Cyber Kill Chain in Intelligence Analysis](../modules/03-cti/07-frameworks/03-kill-chain-cti/) | CTI, Hunter |

See also: [identify the Kill Chain stage of observed or reported activity](#identify-the-kill-chain-stage-of-observed-or-reported-activity), [using the Kill Chain to understand attack progression](#using-the-kill-chain-to-understand-attack-progression)

### planned service outages

Also: upcoming maintenance, planned outage window

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.7.2 Required Content of the Changeover Report](../modules/01-soc/07-shift-change/02-changeover-report/) | SOC, Hunter, CTI |

See also: [ongoing / occurred-during-shift outages](#ongoing--occurred-during-shift-outages), [producing a complete changeover report](#producing-a-complete-changeover-report)

### plan collection against an intelligence requirement

Also: collection plan line, first collection class, what you will not collect

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.8 Collection Sources and Methods](../modules/03-cti/01-core-intel/08-collection-sources/) | CTI, Hunter |
| Used | [3.12.2 Local Production and Approval Processes](../modules/03-cti/12-site-specific/02-local-production/) | CTI, Hunter |

See also: [collection source classes (OSINT, commercial, internal)](#collection-source-classes-osint-commercial-internal), [follow the local collection-request or approval path](#follow-the-local-collection-request-or-approval-path)

### local production and approval processes

Also: do not invent a local workflow, produce approve collect-request archive

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.12.2 Local Production and Approval Processes](../modules/03-cti/12-site-specific/02-local-production/) | CTI, Hunter |

See also: [follow the local collection-request or approval path](#follow-the-local-collection-request-or-approval-path), [document and archive products to local standards](#document-and-archive-products-to-local-standards)

### follow the local collection-request or approval path

Also: no send without the shown path, collection request is not a 3.1.8 plan

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.12.2 Local Production and Approval Processes](../modules/03-cti/12-site-specific/02-local-production/) | CTI, Hunter |

See also: [local production and approval processes](#local-production-and-approval-processes), [plan collection against an intelligence requirement](#plan-collection-against-an-intelligence-requirement)

### follow the local process for initiating and controlling a hunt

Also: do not open a hunt without the shown path, hunt control orientation

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.7.1 Hunt Control and Lead Management](../modules/02-hunter/07-site-specific/01-hunt-control/) | Hunter, SOC, CTI |

See also: [hunt initiation and control are site-specific](#hunt-initiation-and-control-are-site-specific)

### document a hunt according to local standards

Also: file the hunt on the shown form, classroom card is not the site form

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.7.2 Hunt Documentation Standards](../modules/02-hunter/07-site-specific/02-hunt-documentation/) | Hunter, SOC, CTI |

See also: [required hunt-documentation elements are site-specific](#required-hunt-documentation-elements-are-site-specific), [where hunts are documented is site-specific](#where-hunts-are-documented-is-site-specific)

### produce required hunt outputs and perform proper hand-off

Also: hunt hand-off line, do not send without the chart

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.7.3 Hunt Outputs and Hand-off](../modules/02-hunter/07-site-specific/03-hunt-outputs/) | Hunter, SOC, CTI |

See also: [expected hunt outputs are site-specific](#expected-hunt-outputs-are-site-specific), [hunt hand-off to SOC, IR, or CTI is site-specific](#hunt-hand-off-to-soc-ir-or-cti-is-site-specific)

### document and archive products to local standards

Also: official copy not personal folder, local archive path

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.12.2 Local Production and Approval Processes](../modules/03-cti/12-site-specific/02-local-production/) | CTI, Hunter |

See also: [local production and approval processes](#local-production-and-approval-processes), [follow the local collection-request or approval path](#follow-the-local-collection-request-or-approval-path)

### planning and direction

Also: direction, intelligence planning, requirements direction

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

How to write PIRs is [3.1.4 Intelligence Requirements](../modules/03-cti/01-core-intel/04-intelligence-requirements/), not this module.

See also: [intelligence lifecycle](#intelligence-lifecycle)

### policy scripts

Also: Zeek scripts, scripting layer, policy script interpreter

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

### prioritizing hunts

Also: hunt priority, rank hunts, why this hunt first

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |
| Used | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |

See also: [scoping a hunt](#scoping-a-hunt), [hunt development concepts](#hunt-development-concepts)

### Priority Intelligence Requirements (PIRs)

Also: PIR, ranked intelligence requirement

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.4 Intelligence Requirements](../modules/03-cti/01-core-intel/04-intelligence-requirements/) | CTI, Hunter |
| Used | [3.12.1 Local Intelligence Requirements and Priorities](../modules/03-cti/12-site-specific/01-local-priorities/) | CTI, Hunter |

Writing PIRs is 3.1.4. Obtaining *this section's current* list is [3.12.1 Local Intelligence Requirements and Priorities](../modules/03-cti/12-site-specific/01-local-priorities/).

See also: [purpose of intelligence requirements](#purpose-of-intelligence-requirements), [local PIRs are site-specific](#local-pirs-are-site-specific)

### local PIRs are site-specific

Also: every section has its own PIRs, do not invent a PIR list

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.12.1 Local Intelligence Requirements and Priorities](../modules/03-cti/12-site-specific/01-local-priorities/) | CTI, Hunter |

See also: [identify current local intelligence priorities](#identify-current-local-intelligence-priorities), [Priority Intelligence Requirements (PIRs)](#priority-intelligence-requirements-pirs)

### required hunt-documentation elements are site-specific

Also: hunt form varies, do not invent a hunt template

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.7.2 Hunt Documentation Standards](../modules/02-hunter/07-site-specific/02-hunt-documentation/) | Hunter, SOC, CTI |

See also: [where hunts are documented is site-specific](#where-hunts-are-documented-is-site-specific), [document a hunt according to local standards](#document-a-hunt-according-to-local-standards)

### where hunts are documented is site-specific

Also: hunt store, official hunt record, not Slack

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.7.2 Hunt Documentation Standards](../modules/02-hunter/07-site-specific/02-hunt-documentation/) | Hunter, SOC, CTI |

See also: [required hunt-documentation elements are site-specific](#required-hunt-documentation-elements-are-site-specific)

### expected hunt outputs are site-specific

Also: hunt done list, what a finished hunt must produce

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.7.3 Hunt Outputs and Hand-off](../modules/02-hunter/07-site-specific/03-hunt-outputs/) | Hunter, SOC, CTI |

See also: [hunt hand-off to SOC, IR, or CTI is site-specific](#hunt-hand-off-to-soc-ir-or-cti-is-site-specific)

### how local requirements drive analytic focus

Also: in focus vs parked vs ask, interesting is not assigned

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.12.1 Local Intelligence Requirements and Priorities](../modules/03-cti/12-site-specific/01-local-priorities/) | CTI, Hunter |

See also: [align analytic work to a stated local requirement](#align-analytic-work-to-a-stated-local-requirement), [how requirements drive collection and analysis](#how-requirements-drive-collection-and-analysis)

### identify current local intelligence priorities

Also: orientation line, obtain the current PIR list, do not invent PIRs

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.12.1 Local Intelligence Requirements and Priorities](../modules/03-cti/12-site-specific/01-local-priorities/) | CTI, Hunter |

See also: [local PIRs are site-specific](#local-pirs-are-site-specific), [align analytic work to a stated local requirement](#align-analytic-work-to-a-stated-local-requirement)

### align analytic work to a stated local requirement

Also: align Night Owl to a shown PIR, cannot mark in focus without a list

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.12.1 Local Intelligence Requirements and Priorities](../modules/03-cti/12-site-specific/01-local-priorities/) | CTI, Hunter |

See also: [how local requirements drive analytic focus](#how-local-requirements-drive-analytic-focus), [identify current local intelligence priorities](#identify-current-local-intelligence-priorities)

### privilege escalation techniques

Also: privilege escalation, privesc, elevation of privilege

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.2 Privilege Escalation Techniques](../modules/02-hunter/06-attacker-techniques/02-privilege-escalation/) | Hunter, SOC, CTI |

See also: [common Windows privilege escalation methods](#common-windows-privilege-escalation-methods), [persistence techniques](#persistence-techniques)

### process access (Sysmon Event ID 10)

Also: process access, Event ID 10, who touched whom, SourceImage TargetImage

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.1 Process Activity](../modules/01-soc/01-endpoint/01-process-activity/) | SOC, Hunter, CTI |

See also: [process activity](#process-activity), [Sysmon 1 / 5 / 10 and DeviceProcessEvents](#sysmon-1--5--10-and-deviceprocessevents)

### process activity

Also: process events, process telemetry, host process activity

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.1 Process Activity](../modules/01-soc/01-endpoint/01-process-activity/) | SOC, Hunter, CTI |

See also: [process create / terminate](#process-create--terminate), [parent-child process](#parent-child-process)

### process create / terminate

Also: ProcessCreated, ProcessTerminated, Sysmon Event ID 1, Sysmon Event ID 5

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.1 Process Activity](../modules/01-soc/01-endpoint/01-process-activity/) | SOC, Hunter, CTI |

See also: [process activity](#process-activity), [Sysmon 1 / 5 / 10 and DeviceProcessEvents](#sysmon-1--5--10-and-deviceprocessevents)

### processing and exploitation

Also: processing, exploitation, process and exploit

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

See also: [intelligence lifecycle](#intelligence-lifecycle), [information](#information)

### producing a complete changeover report

Also: five-bucket changeover, explicit none, reject missing-element draft

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.7.2 Required Content of the Changeover Report](../modules/01-soc/07-shift-change/02-changeover-report/) | SOC, Hunter, CTI |

See also: [open / in-progress investigations (changeover)](#open--in-progress-investigations-changeover), [urgent process or policy items](#urgent-process-or-policy-items)

### proto

See [5-tuple](#5-tuple).

### purpose and activities in each stage

Also: purpose of each lifecycle stage, activities in each stage

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

See also: [intelligence lifecycle](#intelligence-lifecycle), [stages of the intelligence lifecycle](#stages-of-the-intelligence-lifecycle)

### purpose and challenges of attribution

Also: why attribute, attribution challenges, false flags shared infra

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.7 Attribution](../modules/03-cti/01-core-intel/07-attribution/) | CTI, Hunter |
| Used | [3.11.1 Creating Finished Intelligence Products](../modules/03-cti/11-production/01-finished-products/) | CTI, Hunter |

See also: [levels of confidence in attribution](#levels-of-confidence-in-attribution), [produce a threat actor profile](#produce-a-threat-actor-profile)

### produce a threat actor profile

Also: honest Night Owl profile, unattributed actor profile, 3.11.1.2

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.11.1 Creating Finished Intelligence Products](../modules/03-cti/11-production/01-finished-products/) | CTI, Hunter |

See also: [types of finished intelligence products](#types-of-finished-intelligence-products), [purpose and challenges of attribution](#purpose-and-challenges-of-attribution)

### types of finished intelligence products

Also: activity note, assessment, defensive note, finished intel product types

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.11.1 Creating Finished Intelligence Products](../modules/03-cti/11-production/01-finished-products/) | CTI, Hunter |

See also: [structure and quality standards for a finished product](#structure-and-quality-standards-for-a-finished-product), [draft and evaluate a finished intelligence product](#draft-and-evaluate-a-finished-intelligence-product)

### structure and quality standards for a finished product

Also: BLUF facts assessment gaps action, quality fail T1486 and certainty

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.11.1 Creating Finished Intelligence Products](../modules/03-cti/11-production/01-finished-products/) | CTI, Hunter |

See also: [types of finished intelligence products](#types-of-finished-intelligence-products), [use estimative language in an analytic judgment](#use-estimative-language-in-an-analytic-judgment)

### draft and evaluate a finished intelligence product

Also: draft line, eval line, fail unearned who

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.11.1 Creating Finished Intelligence Products](../modules/03-cti/11-production/01-finished-products/) | CTI, Hunter |

See also: [structure and quality standards for a finished product](#structure-and-quality-standards-for-a-finished-product), [produce a threat actor profile](#produce-a-threat-actor-profile)

### purpose and core functions of the internal TIP

Also: intel store, have we seen this, Harbor TIP

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.1 Internal Threat Intelligence Platform](../modules/03-cti/03-tools/01-internal-tip/) | CTI, Hunter |

See also: [navigating and searching the internal TIP](#navigating-and-searching-the-internal-tip), [collection source classes (OSINT, commercial, internal)](#collection-source-classes-osint-commercial-internal)

### purpose of a structured shift change

Also: why structure changeover, prevent dropped cases at shift change

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.7.1 Shift Changeover Process](../modules/01-soc/07-shift-change/01-changeover-process/) | SOC, Hunter, CTI |

See also: [shift change participants](#shift-change-participants), [conducting or participating in a shift changeover](#conducting-or-participating-in-a-shift-changeover)

### purpose of DTF (discover additional adversary infrastructure)

Also: why DTF, ThreatMesh purpose, communicate and record pivots

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.4 Defender’s ThreatMesh Framework (DTF) for Infrastructure Discovery](../modules/03-cti/07-frameworks/04-dtf/) | CTI, Hunter |

See also: [DTF pivot tactics and pivots](#dtf-pivot-tactics-and-pivots), [how DTF complements ATT&CK, Diamond, and Kill Chain](#how-dtf-complements-attck-diamond-and-kill-chain)

### purpose of estimative language

Also: why estimative terms, comparable uncertainty

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.1 Estimative Language](../modules/03-cti/02-tradecraft/01-estimative-language/) | CTI, Hunter |

See also: [common estimative terms and their meaning](#common-estimative-terms-and-their-meaning), [how estimative language communicates confidence and uncertainty](#how-estimative-language-communicates-confidence-and-uncertainty)

### purpose of intelligence requirements

Also: why write a requirement, focus collection on a decision

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.4 Intelligence Requirements](../modules/03-cti/01-core-intel/04-intelligence-requirements/) | CTI, Hunter |

See also: [Priority Intelligence Requirements (PIRs)](#priority-intelligence-requirements-pirs), [how requirements drive collection and analysis](#how-requirements-drive-collection-and-analysis)

### purpose of structured analytic techniques

Also: why SAT, make thinking visible, do not lock first story

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.2 Structured Analytic Techniques](../modules/03-cti/02-tradecraft/02-structured-techniques/) | CTI, Hunter |

See also: [Analysis of Competing Hypotheses (ACH)](#analysis-of-competing-hypotheses-ach), [Key Assumptions Check](#key-assumptions-check)

### purpose of threat hunting

Also: why hunt exists, hunt purpose, purpose of hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.1 Purpose of Threat Hunting](../modules/02-hunter/01-purpose/) | Hunter, SOC, CTI |
| Used | [2.2.1 Hunt Types](../modules/02-hunter/02-methodology/01-hunt-types/) | Hunter, SOC, CTI |
| Used | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |

See also: [threat hunting in the security program](#threat-hunting-in-the-security-program)

### purpose of WHOIS and RDAP

Also: registration lookup, who holds the block

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.5.1 RDAP and WHOIS Concepts](../modules/03-cti/05-rdap-whois/) | CTI, Hunter |

See also: [key differences between WHOIS and RDAP](#key-differences-between-whois-and-rdap), [key RDAP/WHOIS fields for enrichment and attribution](#key-rdapwhois-fields-for-enrichment-and-attribution)

---

## Q

### qtype_name

Also: DNS query type, `qtype`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

Types taught: A, AAAA, CNAME, MX, TXT, NS, PTR, SOA, SRV, NULL.

SOA *field interpretation* and intel pivot are [3.6.1 Advanced DNS](../modules/03-cti/06-advanced-dns/).

### query

Also: DNS query, queried domain, `query`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

### query RDAP/WHOIS for a domain or IP

Also: RDAP first, WHOIS fallback

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.5.1 RDAP and WHOIS Concepts](../modules/03-cti/05-rdap-whois/) | CTI, Hunter |
| Used | [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/) | CTI, Hunter |

See also: [extract and interpret RDAP/WHOIS fields](#extract-and-interpret-rdapwhois-fields), [purpose of WHOIS and RDAP](#purpose-of-whois-and-rdap)

---

## R

### rapid triage of a CTI report

Also: rapid CTI triage, triage a report for hunting, hunt don’t hunt hand off

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.1 Assessing CTI for Hunting Value](../modules/02-hunter/04-cti-for-hunters/01-assessing-cti/) | Hunter, SOC, CTI |

See also: [assessing CTI for hunting value](#assessing-cti-for-hunting-value), [actionable for a hunt](#actionable-for-a-hunt)

### rcpt to

Also: rcptto, SMTP RCPT TO, envelope recipient

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.6 SMTP Engine](../modules/01-soc/02-zeek/06-smtp-engine/) | SOC, Hunter, CTI |

See also: [smtp log](#smtp-log), [mail from](#mail-from)

### recognizing persistence techniques in logs or telemetry

Also: recognize persistence, persistence in telemetry, persistence recognition

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.1 Persistence Techniques](../modules/02-hunter/06-attacker-techniques/01-persistence/) | Hunter, SOC, CTI |

See also: [persistence techniques](#persistence-techniques), [registry-based persistence](#registry-based-persistence)

### recognizing privilege escalation techniques in logs or telemetry

Also: recognize privilege escalation, privilege escalation in telemetry, privesc recognition

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.2 Privilege Escalation Techniques](../modules/02-hunter/06-attacker-techniques/02-privilege-escalation/) | Hunter, SOC, CTI |

See also: [privilege escalation techniques](#privilege-escalation-techniques), [indicators associated with privilege escalation](#indicators-associated-with-privilege-escalation)

### recording a close or escalate against the correct clock

Also: SLA record line, close vs escalate record

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.5 SLA / Response Time Goals](../modules/01-soc/04-alerts/05-sla-response-times/) | SOC, Hunter, CTI |

See also: [close/escalate clock (time to process)](#closeescalate-clock-time-to-process), [identifying which clock is at risk](#identifying-which-clock-is-at-risk)

### recording ATT&CK IDs from a report

Also: record ATT&CK IDs, copy printed ATT&CK, ATT&CK IDs if the report has them

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |
| Used | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |

Mapping hunts to ATT&CK is [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/).

See also: [extracting hunt leads from CTI](#extracting-hunt-leads-from-cti), [mapping hunts to ATT&CK](#mapping-hunts-to-attck)

### reject a neighbor ATT&CK ID

Also: reject the neighbor ID, neighbor technique reject, T1059.001 vs T1059.003

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.1 MITRE ATT&CK for CTI Analysis and Reporting](../modules/03-cti/07-frameworks/01-attck-cti/) | CTI, Hunter |

See also: [map a report or activity set to ATT&CK](#map-a-report-or-activity-set-to-attck), [ATT&CK techniques and sub-techniques](#attck-techniques-and-sub-techniques)

### reject a TTP that does not apply here

Also: reject Unix TTP on Windows Harbor, reject ESXi T1486, platform-miss TTP

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.2 Extracting Applicable TTPs from Intelligence Reports](../modules/03-cti/08-enrichment/02-applicable-ttps/) | CTI, Hunter |

See also: [extract applicable TTPs from an intelligence report](#extract-applicable-ttps-from-an-intelligence-report), [criteria for TTP applicability to the environment](#criteria-for-ttp-applicability-to-the-environment)

### reject a vendor group name with no shared objects

Also: APT name is not a link, Night Owl APT is not glue

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.3 IOC Handling and Enrichment Concepts](../modules/03-cti/08-enrichment/03-ioc-handling/) | CTI, Hunter |

See also: [link analysis and campaign tracking](#link-analysis-and-campaign-tracking)

### reject an unbounded tactic hunt

Also: reject hunt persistence, reject hunt TA0003

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.3 Hunt for Specific Persistence or Privilege Escalation Techniques](../modules/02-hunter/06-attacker-techniques/03-hunt-specific/) | Hunter, SOC, CTI |

See also: [hunt for a named persistence or privilege-escalation technique](#hunt-for-a-named-persistence-or-privilege-escalation-technique)

### reject hunting the wrong class (persist vs privesc)

Also: SYSTEM task is not a privesc hunt

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.3 Hunt for Specific Persistence or Privilege Escalation Techniques](../modules/02-hunter/06-attacker-techniques/03-hunt-specific/) | Hunter, SOC, CTI |

See also: [hunt for a named persistence or privilege-escalation technique](#hunt-for-a-named-persistence-or-privilege-escalation-technique)

### reject impact that skips the path

Also: reject pay-db-01 outage from WS-JLEE, jewel needs a path

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.4 Threat Relevance and Organizational Impact](../modules/03-cti/08-enrichment/04-relevance-impact/) | CTI, Hunter |

See also: [potential organizational impact](#potential-organizational-impact), [relevance to this environment](#relevance-to-this-environment)

### reject substituting a PIR or an attribution letter

Also: impact line is not a PIR, impact line is not 3.1.7

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.4 Threat Relevance and Organizational Impact](../modules/03-cti/08-enrichment/04-relevance-impact/) | CTI, Hunter |

See also: [relevance to this environment](#relevance-to-this-environment), [local PIRs are site-specific](#local-pirs-are-site-specific)

### reject a weak DTF pivot

Also: reject P0202 /24, reject invented P-code, distinctive NS vs shared hosting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.4 Defender’s ThreatMesh Framework (DTF) for Infrastructure Discovery](../modules/03-cti/07-frameworks/04-dtf/) | CTI, Hunter |

The generic hop reject (no PTA/P IDs) is [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/).

See also: [apply DTF from a known-bad seed](#apply-dtf-from-a-known-bad-seed), [reject a weak or uncited infra pivot](#reject-a-weak-or-uncited-infra-pivot)

### reject a weak or uncited infra pivot

Also: reject cloud /24 as infra, reject public NS hop, uncited vendor domain

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/) | CTI, Hunter |

The DTF-ID reject is [reject a weak DTF pivot](#reject-a-weak-dtf-pivot).

See also: [pivot from a seed indicator to additional adversary infrastructure](#pivot-from-a-seed-indicator-to-additional-adversary-infrastructure), [key RDAP/WHOIS fields for enrichment and attribution](#key-rdapwhois-fields-for-enrichment-and-attribution)

### reject an unobserved Kill Chain stage

Also: unobserved Weaponization, uncited Actions on Objectives, reject a Kill Chain stage not in the excerpt

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.3 Cyber Kill Chain in Intelligence Analysis](../modules/03-cti/07-frameworks/03-kill-chain-cti/) | CTI, Hunter |

See also: [place a report or activity set on the Kill Chain](#place-a-report-or-activity-set-on-the-kill-chain), [identifying the stage and rejecting the previous or next](#identifying-the-stage-and-rejecting-the-previous-or-next)

### reject filling Adversary from a vendor name

Also: vendor-name Adversary, Night Owl APT is not Adversary, reject vendor cluster name

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.2 Diamond Model Application in CTI](../modules/03-cti/07-frameworks/02-diamond-cti/) | CTI, Hunter |

See also: [apply the Diamond Model to an intelligence problem](#apply-the-diamond-model-to-an-intelligence-problem), [using Diamond for analysis and attribution](#using-diamond-for-analysis-and-attribution)

### related endpoint logs for an alert

Also: pull endpoint logs for an alert, what logs add

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.1 Alert Context and Investigation](../modules/01-soc/04-alerts/01-context-investigation/) | SOC, Hunter, CTI |

See also: [related PCAP versus alert fields](#related-pcap-versus-alert-fields), [process activity](#process-activity)

### related PCAP versus alert fields

Also: PCAP vs alert, what PCAP adds

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.1 Alert Context and Investigation](../modules/01-soc/04-alerts/01-context-investigation/) | SOC, Hunter, CTI |

See also: [related endpoint logs for an alert](#related-endpoint-logs-for-an-alert), [http log](#http-log)

### rcode_name

Also: DNS response code, `rcode`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

Codes taught: NOERROR, NXDOMAIN, SERVFAIL, REFUSED, FORMERR.

See also: [NXDOMAIN](#nxdomain)

### REJ

Also: rejected connection

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

See also: [conn_state](#conn_state), [scanning](#scanning)

### reactive hunt

Also: reactive hunting, spark hunt, hunt from IR ask

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.1 Hunt Types](../modules/02-hunter/02-methodology/01-hunt-types/) | Hunter, SOC, CTI |

Re-working an already-raised alert queue is SOC work, not this type.

See also: [hunt types](#hunt-types)

### registry activity

Also: registry events, registry telemetry, DeviceRegistryEvents

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.4 Registry Activity](../modules/01-soc/01-endpoint/04-registry-activity/) | SOC, Hunter, CTI |

See also: [hives and key → value](#hives-and-key--value), [registry set / delete / rename](#registry-set--delete--rename)

### registry set / delete / rename

Also: SetValue, CreateKey, DeleteKey, RenameKey, RegistryValueSet

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.4 Registry Activity](../modules/01-soc/01-endpoint/04-registry-activity/) | SOC, Hunter, CTI |

See also: [registry activity](#registry-activity), [Sysmon 12 / 13 / 14 and DeviceRegistryEvents](#sysmon-12--13--14-and-deviceregistryevents)

### registry-based persistence

Also: Run key persistence, RunOnce, Winlogon persistence, registry autorun

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.1 Persistence Techniques](../modules/02-hunter/06-attacker-techniques/01-persistence/) | Hunter, SOC, CTI |

See also: [persistence techniques](#persistence-techniques), [start menu / startup folder persistence](#start-menu--startup-folder-persistence), [common persistence locations (Run, Services)](#common-persistence-locations-run-services)

### RFI to intel

Also: ask intel for more work on that alert

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [0.3 How work can move](../modules/00-intro/03-how-work-moves/) | SOC, Hunter, CTI, DE |

SOC ticket-type depth is [1.6.1 Report Types](../modules/01-soc/06-reporting/01-report-types/). CTI receive/answer is [3.11.3 Handling RFIs](../modules/03-cti/11-production/03-rfi/).

See also: [how work can move from an alert](#how-work-can-move-from-an-alert), [Request for Information (RFI)](#request-for-information-rfi)

### Request for Information (RFI)

Also: RFI, information request to another team

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.6.1 Report Types](../modules/01-soc/06-reporting/01-report-types/) | SOC, Hunter, CTI |
| Used | [3.11.3 Handling RFIs](../modules/03-cti/11-production/03-rfi/) | CTI, Hunter |

CTI receive/answer is [3.11.3 Handling RFIs](../modules/03-cti/11-production/03-rfi/). This heading is the SOC ticket type.

See also: [incident report](#incident-report), [purpose and lifecycle of an RFI](#purpose-and-lifecycle-of-an-rfi)

### purpose and lifecycle of an RFI

Also: intelligence RFI inbox, receive evaluate prioritize respond

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.11.3 Handling RFIs](../modules/03-cti/11-production/03-rfi/) | CTI, Hunter |

See also: [evaluate and prioritize an RFI](#evaluate-and-prioritize-an-rfi), [Request for Information (RFI)](#request-for-information-rfi)

### evaluate and prioritize an RFI

Also: produce a response to an RFI, reject an out-of-scope or duplicate RFI

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.11.3 Handling RFIs](../modules/03-cti/11-production/03-rfi/) | CTI, Hunter |

See also: [purpose and lifecycle of an RFI](#purpose-and-lifecycle-of-an-rfi), [produce a threat actor profile](#produce-a-threat-actor-profile)

### requesting a tool to be installed

Also: SOFT-REQ, install Wireshark ticket

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.3 Tool Access and Requests](../modules/01-soc/08-site-specific/03-tool-access/) | SOC, Hunter, CTI |

See also: [accessing required tools and their URLs](#accessing-required-tools-and-their-urls), [requesting access (e.g., SIEM)](#requesting-access-eg-siem)

### requesting access (e.g., SIEM)

Also: ACCESS-REQ, SIEM 403, entitlement ticket

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.3 Tool Access and Requests](../modules/01-soc/08-site-specific/03-tool-access/) | SOC, Hunter, CTI |

See also: [accessing required tools and their URLs](#accessing-required-tools-and-their-urls), [requesting a tool to be installed](#requesting-a-tool-to-be-installed)

### routing a report (recipients, leadership, channel)

Also: route line, reject wrong reporting channel

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.6.3 Notification and Distribution](../modules/01-soc/06-reporting/03-notification-distribution/) | SOC, Hunter, CTI |

See also: [notification chart / matrix](#notification-chart--matrix), [approved reporting channels](#approved-reporting-channels)

---

## S

### S0

Also: SYN with no reply, unanswered SYN

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

See also: [conn_state](#conn_state), [scanning](#scanning)

### scanning

Also: port scan, `S0`/`REJ` volume

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

### scoping a hunt

Also: hunt scope, bound a hunt, who where how long

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |

See also: [prioritizing hunts](#prioritizing-hunts), [visibility gaps](#visibility-gaps)

### select the right structured analytic technique for a scenario

Also: KAC vs ACH vs neither, pick the SAT

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.2 Structured Analytic Techniques](../modules/03-cti/02-tradecraft/02-structured-techniques/) | CTI, Hunter |

See also: [when to apply ACH vs Key Assumptions Check](#when-to-apply-ach-vs-key-assumptions-check), [apply a structured analytic technique](#apply-a-structured-analytic-technique)

### select the appropriate external tool

Also: pick VT AnyRun Silent Push URLScan, reject neighbor tool

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/) | CTI, Hunter |

See also: [when to use each external tool in the intelligence process](#when-to-use-each-external-tool-in-the-intelligence-process), [enrich or pivot using an external tool](#enrich-or-pivot-using-an-external-tool)

### search and retrieve from the internal TIP

Also: retrieve line, open IND-1882

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.1 Internal Threat Intelligence Platform](../modules/03-cti/03-tools/01-internal-tip/) | CTI, Hunter |

See also: [navigating and searching the internal TIP](#navigating-and-searching-the-internal-tip), [use the TIP for enrichment or analysis](#use-the-tip-for-enrichment-or-analysis)

### scheduled-task persistence

Also: scheduled tasks, Task Scheduler persistence, event 4698, T1053.005

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.1 Persistence Techniques](../modules/02-hunter/06-attacker-techniques/01-persistence/) | Hunter, SOC, CTI |

See also: [persistence techniques](#persistence-techniques), [recognizing persistence techniques in logs or telemetry](#recognizing-persistence-techniques-in-logs-or-telemetry)

### self-signed certificate

Also: `subject` equals `issuer`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

### server_name

See [SNI](#sni).

### service

Also: `service`, Zeek-detected application protocol

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

### SF

Also: normal teardown, established and terminated

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

See also: [conn_state](#conn_state)

### shift change participants

Also: outgoing lead, incoming lead, who attends changeover

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.7.1 Shift Changeover Process](../modules/01-soc/07-shift-change/01-changeover-process/) | SOC, Hunter, CTI |

See also: [purpose of a structured shift change](#purpose-of-a-structured-shift-change), [conducting or participating in a shift changeover](#conducting-or-participating-in-a-shift-changeover)

### SIEM detection rules / correlation searches

Also: SIEM rule, analytics rule, correlation search, saved detection

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.4 SIEM Rules](../modules/01-soc/03-detection/04-siem-rules/) | SOC, Hunter, CTI |

See also: [turning log fields into detections](#turning-log-fields-into-detections), [creating a SIEM rule from log fields or from SIGMA](#creating-a-siem-rule-from-log-fields-or-from-sigma)

### SIGMA fields / selectors

Also: SIGMA modifiers, endswith, contains, SIGMA selection

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.1 SIGMA Rules](../modules/01-soc/03-detection/01-sigma-rules/) | SOC, Hunter, CTI |

See also: [SIGMA rule structure](#sigma-rule-structure), [SIGMA rules](#sigma-rules)

### SIGMA rule structure

Also: SIGMA logsource, SIGMA detection, SIGMA condition

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.1 SIGMA Rules](../modules/01-soc/03-detection/01-sigma-rules/) | SOC, Hunter, CTI |

See also: [SIGMA rules](#sigma-rules), [how SIGMA translates to SIEM queries](#how-sigma-translates-to-siem-queries)

### SIGMA rules

Also: Sigma, SIGMA YAML, generic detection format

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.1 SIGMA Rules](../modules/01-soc/03-detection/01-sigma-rules/) | SOC, Hunter, CTI |

See also: [SIGMA rule structure](#sigma-rule-structure), [creating a SIEM rule from log fields or from SIGMA](#creating-a-siem-rule-from-log-fields-or-from-sigma)

### Silent Push for hunting

Also: Silent Push, passive DNS for hunting, infra clustering for hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |
| Used | [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/) | CTI, Hunter |

See also: [tool capabilities for hunting](#tool-capabilities-for-hunting), [purpose, strengths, and weaknesses of Silent Push](#purpose-strengths-and-weaknesses-of-silent-push)

### purpose, strengths, and weaknesses of Silent Push

Also: Silent Push for intelligence, historical PDNS

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/) | CTI, Hunter |
| Used | [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/) | CTI, Hunter |
| Used | [3.9.3 Silent Push](../modules/03-cti/09-platforms/03-silent-push/) | CTI, Hunter |

See also: [Silent Push for hunting](#silent-push-for-hunting), [when to use each external tool in the intelligence process](#when-to-use-each-external-tool-in-the-intelligence-process)

### Silent Push core capabilities and use cases

Also: how to pivot and enrich indicators in Silent Push, Silent Push PDNS siblings NS

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.9.3 Silent Push](../modules/03-cti/09-platforms/03-silent-push/) | CTI, Hunter |

See also: [enrich an indicator using Silent Push](#enrich-an-indicator-using-silent-push), [purpose, strengths, and weaknesses of Silent Push](#purpose-strengths-and-weaknesses-of-silent-push)

### enrich an indicator using Silent Push

Also: Silent Push enrich line, pivot within Silent Push to identify additional infrastructure

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.9.3 Silent Push](../modules/03-cti/09-platforms/03-silent-push/) | CTI, Hunter |

See also: [Silent Push core capabilities and use cases](#silent-push-core-capabilities-and-use-cases), [pivot from a seed indicator to additional adversary infrastructure](#pivot-from-a-seed-indicator-to-additional-adversary-infrastructure)

### site-specific incident response processes

Also: IR card, Sev1 Sev2 Sev3, reject freelance containment

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.5 Incident Response Processes](../modules/01-soc/08-site-specific/05-incident-response/) | SOC, Hunter, CTI |

See also: [crown jewel / critical assets](#crown-jewel--critical-assets), [routing a report (recipients, leadership, channel)](#routing-a-report-recipients-leadership-channel)

### smtp log

Also: `smtp`, Zeek smtp

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |
| Taught | [1.2.6 SMTP Engine](../modules/01-soc/02-zeek/06-smtp-engine/) | SOC, Hunter, CTI |

1.2.1 teaches that the log exists. 1.2.6 teaches mailfrom, rcptto, subject, msg_id, and analysis.

### SNI

Also: Server Name Indication, `server_name`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

See also: [missing SNI](#missing-sni), [SNI vs certificate mismatch](#sni-vs-certificate-mismatch)

### SNI vs certificate mismatch

Also: SNI does not match subject, lookalike certificate

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

### source / dest IP and port, protocol, direction

Also: SourceIp, DestinationIp, RemoteIP, RemotePort, Initiated, LocalIP

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.3 Network Activity (Endpoint)](../modules/01-soc/01-endpoint/03-network-activity/) | SOC, Hunter, CTI |

See also: [network activity (endpoint)](#network-activity-endpoint), [host-observed vs Zeek](#host-observed-vs-zeek)

### source reliability scale

Also: Admiralty A–F, usually reliable, cannot be judged

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.3 Admiralty Code](../modules/03-cti/02-tradecraft/03-admiralty-code/) | CTI, Hunter |

See also: [information credibility scale](#information-credibility-scale), [assign Admiralty Code ratings](#assign-admiralty-code-ratings)

### SPAN

See [TAP / SPAN](#tap--span).

### ssl log

See [TLS / ssl log](#tls--ssl-log).

### ssdeep

Also: fuzzy hash, ssdeep score, classroom 50

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.4.1 Hashing and Similarity Concepts](../modules/03-cti/04-file-similarity/) | CTI, Hunter |

See also: [TLSH](#tlsh), [use file similarity hashes to identify related samples](#use-file-similarity-hashes-to-identify-related-samples)

### SOA records

Also: Start of Authority, MNAME, RNAME, zone serial

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.6.1 Advanced DNS Concepts](../modules/03-cti/06-advanced-dns/) | CTI, Hunter |
| Used | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

See also: [interpret an SOA record](#interpret-an-soa-record), [qtype_name](#qtype_name)

### SSLv3

See [TLS version](#tls-version).

### stages of the intelligence lifecycle

Also: lifecycle stages, six stages, intelligence cycle stages

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

See also: [intelligence lifecycle](#intelligence-lifecycle), [purpose and activities in each stage](#purpose-and-activities-in-each-stage)

### start clock (time to begin investigation)

Also: time to start an alert, start SLA

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.5 SLA / Response Time Goals](../modules/01-soc/04-alerts/05-sla-response-times/) | SOC, Hunter, CTI |

See also: [close/escalate clock (time to process)](#closeescalate-clock-time-to-process), [identifying which clock is at risk](#identifying-which-clock-is-at-risk)

### start menu / startup folder persistence

Also: startup folder, Start Menu Startup, All Users Startup, T1547.001 startup folder

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.1 Persistence Techniques](../modules/02-hunter/06-attacker-techniques/01-persistence/) | Hunter, SOC, CTI |

See also: [persistence techniques](#persistence-techniques), [registry-based persistence](#registry-based-persistence)

### STIX as hunt input

Also: STIX for hunters, read STIX for hunting, STIX report or bundle

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |
| Used | [3.10.1 Core STIX Objects](../modules/03-cti/10-stix/01-core-objects/) | CTI, Hunter |

See also: [hunt-relevant STIX objects](#hunt-relevant-stix-objects), [how a STIX bundle seeds a hunt](#how-a-stix-bundle-seeds-a-hunt)

### STIX objects a hunter uses

Also: indicator attack-pattern observed-data malware threat-actor intrusion-set relationship

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |
| Used | [3.10.1 Core STIX Objects](../modules/03-cti/10-stix/01-core-objects/) | CTI, Hunter |

Core STIX object inventory for production is [3.10.1 Core STIX Objects](../modules/03-cti/10-stix/01-core-objects/).

See also: [hunt-relevant STIX objects](#hunt-relevant-stix-objects), [STIX as hunt input](#stix-as-hunt-input)

### Indicator, Observed Data, and Malware (STIX)

Also: STIX indicator vs observed-data, STIX malware object

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.10.1 Core STIX Objects](../modules/03-cti/10-stix/01-core-objects/) | CTI, Hunter |

See also: [identify and label common STIX objects in a report](#identify-and-label-common-stix-objects-in-a-report), [STIX objects a hunter uses](#stix-objects-a-hunter-uses)

### Attack Pattern, Threat Actor, Intrusion Set, and Campaign (STIX)

Also: STIX attack-pattern, empty threat-actor, intrusion-set vs campaign

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.10.1 Core STIX Objects](../modules/03-cti/10-stix/01-core-objects/) | CTI, Hunter |

See also: [identify and label common STIX objects in a report](#identify-and-label-common-stix-objects-in-a-report), [reject filling Adversary from a vendor name](#reject-filling-adversary-from-a-vendor-name)

### Course of Action, Identity, Relationship, and Sighting (STIX)

Also: STIX course-of-action, STIX sighting vs indicator, STIX identity

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.10.1 Core STIX Objects](../modules/03-cti/10-stix/01-core-objects/) | CTI, Hunter |

See also: [identify and label common STIX objects in a report](#identify-and-label-common-stix-objects-in-a-report), [linking STIX objects to represent threat activity](#linking-stix-objects-to-represent-threat-activity)

### identify and label common STIX objects in a report

Also: label a STIX type, reject the neighbor STIX type

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.10.1 Core STIX Objects](../modules/03-cti/10-stix/01-core-objects/) | CTI, Hunter |

See also: [Indicator, Observed Data, and Malware (STIX)](#indicator-observed-data-and-malware-stix), [STIX as hunt input](#stix-as-hunt-input)

### structuring STIX for sharing and automation

Also: STIX bundle for sharing, STIX for automation

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.10.2 How STIX Objects Are Used in Intelligence Production](../modules/03-cti/10-stix/02-stix-production/) | CTI, Hunter |

See also: [use TAXII for sharing and consumption of intelligence](#use-taxii-for-sharing-and-consumption-of-intelligence), [how a STIX bundle seeds a hunt](#how-a-stix-bundle-seeds-a-hunt)

### linking STIX objects to represent threat activity

Also: STIX relationship_type, Night Owl STIX graph, explain a STIX scenario

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.10.2 How STIX Objects Are Used in Intelligence Production](../modules/03-cti/10-stix/02-stix-production/) | CTI, Hunter |

See also: [create and validate STIX objects](#create-and-validate-stix-objects), [Course of Action, Identity, Relationship, and Sighting (STIX)](#course-of-action-identity-relationship-and-sighting-stix)

### create and validate STIX objects

Also: valid STIX pattern, missing relationship_type, unearned threat-actor object

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.10.2 How STIX Objects Are Used in Intelligence Production](../modules/03-cti/10-stix/02-stix-production/) | CTI, Hunter |

See also: [linking STIX objects to represent threat activity](#linking-stix-objects-to-represent-threat-activity), [identify and label common STIX objects in a report](#identify-and-label-common-stix-objects-in-a-report)

### use TAXII for sharing and consumption of intelligence

Also: TAXII collection, publish STIX bundle, consume STIX, harbor-cti classroom collection

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.10.2 How STIX Objects Are Used in Intelligence Production](../modules/03-cti/10-stix/02-stix-production/) | CTI, Hunter |

TAXII is the channel. The bundle is the payload. Emailing a PDF is not TAXII.

See also: [structuring STIX for sharing and automation](#structuring-stix-for-sharing-and-automation), [navigating and searching the internal TIP](#navigating-and-searching-the-internal-tip)

### strategic intelligence

Also: strategic intel, strategic type, posture intelligence

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [intelligence types](#intelligence-types)

### SMTP subject

Also: smtp.subject, mail subject

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.6 SMTP Engine](../modules/01-soc/02-zeek/06-smtp-engine/) | SOC, Hunter, CTI |

See also: [smtp log](#smtp-log), [mail from](#mail-from)

### source and destination (weird)

Also: weird 5-tuple, weird id.orig_h, weird id.resp_h

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.8 Weird Engine](../modules/01-soc/02-zeek/08-weird-engine/) | SOC, Hunter, CTI |

See also: [weird log](#weird-log), [5-tuple](#5-tuple)

### subject

See [certificate subject / issuer](#certificate-subject--issuer).

### submit timelines by report type

Also: incident submit 30, RFI submit 60, informational before changeover

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.6.2 Reporting Timelines](../modules/01-soc/06-reporting/02-reporting-timelines/) | SOC, Hunter, CTI |

See also: [escalation timeline when more information is needed](#escalation-timeline-when-more-information-is-needed), [identifying which report timeline applies and whether it is at risk](#identifying-which-report-timeline-applies-and-whether-it-is-at-risk)

### Suricata rule options

Also: content, http.uri, http.user_agent, tls.sni, Suricata pcre

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.2 Suricata Rules](../modules/01-soc/03-detection/02-suricata-rules/) | SOC, Hunter, CTI |

See also: [Suricata rule structure](#suricata-rule-structure), [matching techniques: ASCII, hex, and regex](#matching-techniques-ascii-hex-and-regex)

### Suricata rule structure

Also: Suricata action, Suricata header, alert proto src dest

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.2 Suricata Rules](../modules/01-soc/03-detection/02-suricata-rules/) | SOC, Hunter, CTI |

See also: [Suricata rules](#suricata-rules), [Suricata rule options](#suricata-rule-options)

### Suricata rules

Also: Suricata signature, IDS rule, network signature

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.2 Suricata Rules](../modules/01-soc/03-detection/02-suricata-rules/) | SOC, Hunter, CTI |

See also: [how Suricata rules relate to Zeek](#how-suricata-rules-relate-to-zeek), [Suricata rule structure](#suricata-rule-structure)

### Sysmon 1 / 5 / 10 and DeviceProcessEvents

Also: DeviceProcessEvents, Sysmon process events, ActionType ProcessCreated

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.1 Process Activity](../modules/01-soc/01-endpoint/01-process-activity/) | SOC, Hunter, CTI |

See also: [process activity](#process-activity), [process create / terminate](#process-create--terminate), [process access (Sysmon Event ID 10)](#process-access-sysmon-event-id-10)

### Sysmon 11 / 23 / 26 and DeviceFileEvents

Also: DeviceFileEvents, Sysmon file events, ActionType FileCreated, FileDeleteDetected

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.2 File System Activity](../modules/01-soc/01-endpoint/02-file-system-activity/) | SOC, Hunter, CTI |

See also: [file system activity](#file-system-activity), [file create / rename-move / delete / modify / read](#file-create--rename-move--delete--modify--read)

### Sysmon 12 / 13 / 14 and DeviceRegistryEvents

Also: DeviceRegistryEvents, Sysmon registry events, SetValue, CreateKey, RenameValue

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.4 Registry Activity](../modules/01-soc/01-endpoint/04-registry-activity/) | SOC, Hunter, CTI |

See also: [registry activity](#registry-activity), [registry set / delete / rename](#registry-set--delete--rename)

### Sysmon 3 / 22 and DeviceNetworkEvents

Also: DeviceNetworkEvents, Sysmon network connection, Sysmon DNS query, Event ID 3, Event ID 22

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.3 Network Activity (Endpoint)](../modules/01-soc/01-endpoint/03-network-activity/) | SOC, Hunter, CTI |

See also: [network activity (endpoint)](#network-activity-endpoint), [host-observed vs Zeek](#host-observed-vs-zeek)

### Sysmon 6 / 7 and DeviceImageLoadEvents

Also: DeviceImageLoadEvents, Sysmon driver load, Sysmon image load, Event ID 6, Event ID 7

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.5 Image and Driver Load Activity](../modules/01-soc/01-endpoint/05-image-driver-load/) | SOC, Hunter, CTI |

See also: [image and driver load activity](#image-and-driver-load-activity), [user-mode image load vs kernel driver load](#user-mode-image-load-vs-kernel-driver-load)

---

## T

### TAP / SPAN

Also: network TAP, SPAN port, how Zeek sees traffic

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

### tactical intelligence

Also: tactical intel, tactical type

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [intelligence types](#intelligence-types), [technical intelligence](#technical-intelligence)

### trusted third-party access / federation

Also: vpn-vendor, idp-corp, federation access

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.1 Environment Orientation](../modules/01-soc/08-site-specific/01-environment-orientation/) | SOC, Hunter, CTI |

See also: [key network segments and data flow](#key-network-segments-and-data-flow), [identifying which orientation fact applies and rejecting the adjacent fact](#identifying-which-orientation-fact-applies-and-rejecting-the-adjacent-fact)

### TLSH

Also: trend locality sensitive hash, TLSH distance

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.4.1 Hashing and Similarity Concepts](../modules/03-cti/04-file-similarity/) | CTI, Hunter |

See also: [ssdeep](#ssdeep), [use file similarity hashes to identify related samples](#use-file-similarity-hashes-to-identify-related-samples)

### translate stakeholder questions into clear intelligence requirements

Also: rewrite a messy ask, translate are we safe

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.4 Intelligence Requirements](../modules/03-cti/01-core-intel/04-intelligence-requirements/) | CTI, Hunter |

See also: [develop or refine intelligence requirements](#develop-or-refine-intelligence-requirements), [purpose of intelligence requirements](#purpose-of-intelligence-requirements)

### types of attribution (activity group vs nation-state)

Also: activity group, cluster vs country, nation-state claim

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.7 Attribution](../modules/03-cti/01-core-intel/07-attribution/) | CTI, Hunter |

See also: [assess attribution statements for confidence and evidence](#assess-attribution-statements-for-confidence-and-evidence), [purpose and challenges of attribution](#purpose-and-challenges-of-attribution)

### technical intelligence

Also: technical intel, technical type, technical observables

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [intelligence types](#intelligence-types), [tactical intelligence](#tactical-intelligence)

### techniques to mitigate cognitive biases

Also: ACH to hunt an I, KAC a must-be, rewrite without the anchor

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.4 Cognitive Biases and Mitigation](../modules/03-cti/02-tradecraft/04-cognitive-biases/) | CTI, Hunter |

See also: [apply a mitigation technique](#apply-a-mitigation-technique), [common cognitive biases that affect analysis](#common-cognitive-biases-that-affect-analysis)

### threat hunting in the security program

Also: hunt in the program, hunt vs SOC vs CTI, explain hunt to the SOC lead

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.1 Purpose of Threat Hunting](../modules/02-hunter/01-purpose/) | Hunter, SOC, CTI |

See also: [purpose of threat hunting](#purpose-of-threat-hunting)

### TLS / ssl log

Also: `ssl` log, TLS log, Zeek TLS engine, ssl/tls

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

1.2.1 teaches that the log exists (Zeek names it `ssl`). 1.2.4 teaches fields and analysis.

### transformation from raw data to information to intelligence

Also: data to information to intelligence, how raw data becomes intelligence

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.1 Data, Information, and Intelligence](../modules/03-cti/01-core-intel/01-data-info-intel/) | CTI, Hunter |
| Used | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

See also: [data](#data), [information](#information), [intelligence](#intelligence)

### TTPs vs IOCs vs behaviors

Also: TTP vs IOC vs behavior, which can drive a hunt, method vs object vs pattern

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

See also: [hunt-suitable TTPs](#hunt-suitable-ttps), [hunt-suitable artifacts](#hunt-suitable-artifacts)

### turning STIX objects into hunt leads

Also: turn STIX objects into hunt leads, convert bundle leftovers to leads

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

See also: [how a STIX bundle seeds a hunt](#how-a-stix-bundle-seeds-a-hunt), [hunt question from CTI leads](#hunt-question-from-cti-leads)

### True Negative

Also: TN, quiet and benign, correctly no alert

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.2 Alert Classification](../modules/01-soc/04-alerts/02-classification/) | SOC, Hunter, CTI |

See also: [True Positive](#true-positive), [False Negative](#false-negative)

### True Positive

Also: TP, fired and bad

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.2 Alert Classification](../modules/01-soc/04-alerts/02-classification/) | SOC, Hunter, CTI |

See also: [False Positive](#false-positive), [classifying cases and citing evidence](#classifying-cases-and-citing-evidence)

### turning log fields into detections

Also: fields to detection, log fields into a SIEM rule

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.4 SIEM Rules](../modules/01-soc/03-detection/04-siem-rules/) | SOC, Hunter, CTI |

See also: [SIEM detection rules / correlation searches](#siem-detection-rules--correlation-searches), [creating a SIEM rule from log fields or from SIGMA](#creating-a-siem-rule-from-log-fields-or-from-sigma)

### tx_hosts / rx_hosts

Also: files tx_hosts, files rx_hosts, file sender, file receiver

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.7 Files Engine](../modules/01-soc/02-zeek/07-files-engine/) | SOC, Hunter, CTI |

See also: [files log](#files-log), [5-tuple](#5-tuple)

### TLS fingerprint

See [JA3](#ja3).

### TLS version

Also: `version`, TLSv13, TLSv12, TLSv11, TLSv10, SSLv3, deprecated TLS

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

### tool capabilities for hunting

Also: online tools for hunting, enrichment tools, VT AnyRun URLScan Silent Push

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |

See also: [VirusTotal for hunting](#virustotal-for-hunting), [AnyRun for hunting](#anyrun-for-hunting), [URLScan for hunting](#urlscan-for-hunting), [Silent Push for hunting](#silent-push-for-hunting)

### TXT

See [qtype_name](#qtype_name) and [DNS tunneling](#dns-tunneling).

---

## U

### uid

Also: Zeek uid, connection UID, pivot key, pivoting with uid to conn

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |
| Used | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |
| Used | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |
| Used | [1.2.5 HTTP Engine](../modules/01-soc/02-zeek/05-http-engine/) | SOC, Hunter, CTI |
| Used | [1.2.6 SMTP Engine](../modules/01-soc/02-zeek/06-smtp-engine/) | SOC, Hunter, CTI |
| Used | [1.2.7 Files Engine](../modules/01-soc/02-zeek/07-files-engine/) | SOC, Hunter, CTI |
| Used | [1.2.8 Weird Engine](../modules/01-soc/02-zeek/08-weird-engine/) | SOC, Hunter, CTI |

The obligation is created in 1.2.2: copy `uid` and search other Zeek logs. Later engines assume that habit. `files` joins with `conn_uids` (those values *are* connection `uid`s).

### unique patterns or behaviors suitable for hunting

Also: hunt-worthy pattern, unique hunt behavior, internal search pattern

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |
| Used | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |
| Used | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

See also: [hunt hypothesis](#hunt-hypothesis), [hunt development concepts](#hunt-development-concepts)

### upstream alerting hops

Also: Suricata to SIEM to alert, alert chain, name each hop

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.1 Alert Context and Investigation](../modules/01-soc/04-alerts/01-context-investigation/) | SOC, Hunter, CTI |

See also: [alert configuration (what would fire)](#alert-configuration-what-would-fire), [Suricata rules](#suricata-rules)

### urgent process or policy items

Also: urgent policy at changeover, do-not-close without IR

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.7.2 Required Content of the Changeover Report](../modules/01-soc/07-shift-change/02-changeover-report/) | SOC, Hunter, CTI |

See also: [producing a complete changeover report](#producing-a-complete-changeover-report), [open / in-progress investigations (changeover)](#open--in-progress-investigations-changeover)

### URI / URL

Also: http.uri, HTTP URL, host plus uri

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.5 HTTP Engine](../modules/01-soc/02-zeek/05-http-engine/) | SOC, Hunter, CTI |

See also: [http log](#http-log), [HTTP host](#http-host)

### URLScan for hunting

Also: urlscan.io, URLScan page scan, URLScan for hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |
| Used | [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/) | CTI, Hunter |

See also: [tool capabilities for hunting](#tool-capabilities-for-hunting), [purpose, strengths, and weaknesses of URLScan](#purpose-strengths-and-weaknesses-of-urlscan)

### purpose, strengths, and weaknesses of URLScan

Also: URLScan for intelligence, live page scan

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/) | CTI, Hunter |
| Used | [3.9.4 URLScan](../modules/03-cti/09-platforms/04-urlscan/) | CTI, Hunter |

See also: [URLScan for hunting](#urlscan-for-hunting), [when to use each external tool in the intelligence process](#when-to-use-each-external-tool-in-the-intelligence-process)

### URLScan core capabilities and use cases

Also: interpreting URLScan results for intelligence value, this page load

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.9.4 URLScan](../modules/03-cti/09-platforms/04-urlscan/) | CTI, Hunter |

See also: [submit or retrieve a URLScan result](#submit-or-retrieve-a-urlscan-result), [purpose, strengths, and weaknesses of URLScan](#purpose-strengths-and-weaknesses-of-urlscan)

### submit or retrieve a URLScan result

Also: retrieve existing URLScan, extract actionable intelligence from a URLScan report

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.9.4 URLScan](../modules/03-cti/09-platforms/04-urlscan/) | CTI, Hunter |

See also: [URLScan core capabilities and use cases](#urlscan-core-capabilities-and-use-cases), [purpose, strengths, and weaknesses of URLScan](#purpose-strengths-and-weaknesses-of-urlscan)

### use estimative language in an analytic judgment

Also: write a likely judgment, banned is will could

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.1 Estimative Language](../modules/03-cti/02-tradecraft/01-estimative-language/) | CTI, Hunter |

See also: [common estimative terms and their meaning](#common-estimative-terms-and-their-meaning), [interpret the likelihood expressed in an estimative statement](#interpret-the-likelihood-expressed-in-an-estimative-statement)

### use advanced DNS records to enrich or pivot

Also: pivot on NS and MNAME, unique TXT token

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.6.1 Advanced DNS Concepts](../modules/03-cti/06-advanced-dns/) | CTI, Hunter |
| Used | [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/) | CTI, Hunter |

See also: [SOA records](#soa-records), [other advanced DNS record types of intelligence value](#other-advanced-dns-record-types-of-intelligence-value), [pivot from a seed indicator to additional adversary infrastructure](#pivot-from-a-seed-indicator-to-additional-adversary-infrastructure)

### use a selected DTF pivot to guide the next lookup

Also: DTF lookup line, P0101.010 to RDAP NS, do not re-teach 3.5

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.4 Defender’s ThreatMesh Framework (DTF) for Infrastructure Discovery](../modules/03-cti/07-frameworks/04-dtf/) | CTI, Hunter |
| Used | [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/) | CTI, Hunter |

The generic hop sentence is [3.8.1 Identifying Additional Adversary Infrastructure from Seed Indicators](../modules/03-cti/08-enrichment/01-infra-pivot/).

See also: [apply DTF from a known-bad seed](#apply-dtf-from-a-known-bad-seed), [DTF pivot tactics and pivots](#dtf-pivot-tactics-and-pivots)

### use file similarity hashes to identify related samples

Also: related vs identical, ssdeep 50, same imphash different SHA256

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.4.1 Hashing and Similarity Concepts](../modules/03-cti/04-file-similarity/) | CTI, Hunter |

See also: [imphash](#imphash), [ssdeep](#ssdeep), [TLSH](#tlsh)

### use the TIP for enrichment or analysis

Also: add a sighting, link related indicator in TIP

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.1 Internal Threat Intelligence Platform](../modules/03-cti/03-tools/01-internal-tip/) | CTI, Hunter |

See also: [how the TIP supports enrichment, analysis, and production](#how-the-tip-supports-enrichment-analysis-and-production), [search and retrieve from the internal TIP](#search-and-retrieve-from-the-internal-tip)

### user-mode image load vs kernel driver load

Also: DLL load vs driver load, Event 7 vs Event 6, user-mode vs kernel

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.5 Image and Driver Load Activity](../modules/01-soc/01-endpoint/05-image-driver-load/) | SOC, Hunter, CTI |

See also: [image and driver load activity](#image-and-driver-load-activity), [Sysmon 6 / 7 and DeviceImageLoadEvents](#sysmon-6--7-and-deviceimageloadevents)

### User-Agent

Also: user_agent, HTTP User-Agent

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.5 HTTP Engine](../modules/01-soc/02-zeek/05-http-engine/) | SOC, Hunter, CTI |

See also: [http log](#http-log), [HTTP method](#http-method)

### using Diamond for analysis and attribution

Also: Diamond attribution, unknown adversary vertex

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.2 Diamond Model](../modules/01-soc/05-frameworks/02-diamond-model/) | SOC, Hunter, CTI |
| Used | [3.7.2 Diamond Model Application in CTI](../modules/03-cti/07-frameworks/02-diamond-cti/) | CTI, Hunter |

See also: [Diamond Model purpose](#diamond-model-purpose), [filling four vertices and naming the weakest](#filling-four-vertices-and-naming-the-weakest), [Diamond Model application in CTI](#diamond-model-application-in-cti)

### using the Kill Chain to understand attack progression

Also: Kill Chain progression, where you are in the intrusion

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.3 Cyber Kill Chain](../modules/01-soc/05-frameworks/03-cyber-kill-chain/) | SOC, Hunter, CTI |
| Used | [3.7.3 Cyber Kill Chain in Intelligence Analysis](../modules/03-cti/07-frameworks/03-kill-chain-cti/) | CTI, Hunter |

See also: [Cyber Kill Chain purpose](#cyber-kill-chain-purpose), [identifying the stage and rejecting the previous or next](#identifying-the-stage-and-rejecting-the-previous-or-next), [place a report or activity set on the Kill Chain](#place-a-report-or-activity-set-on-the-kill-chain)

### using ATT&CK to identify detection or visibility gaps

Also: ATT&CK detection gap, ATT&CK visibility gap, coverage gaps from a hunt map

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |

See also: [detection gaps](#detection-gaps), [visibility gaps](#visibility-gaps), [ATT&CK coverage analysis](#attck-coverage-analysis)

### using ATT&CK to support hunt prioritization

Also: ATT&CK-supported priority, rank hunts with ATT&CK

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |

See also: [prioritizing hunts](#prioritizing-hunts), [mapping hunts to ATT&CK](#mapping-hunts-to-attck)

### using MITRE ATT&CK for hunt planning

Also: ATT&CK for hunt planning, ATT&CK for hunting, framework application for hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |

See also: [mapping hunts to ATT&CK](#mapping-hunts-to-attck), [ATT&CK coverage analysis](#attck-coverage-analysis)

---

## V

### visibility gaps

Also: visibility gap, no telemetry, cannot see, blind segment

| Coverage | Module | Roles |
| Used | [2.6.2 Privilege Escalation Techniques](../modules/02-hunter/06-attacker-techniques/02-privilege-escalation/) | Hunter, SOC, CTI |
|----------|--------|-------|
| Taught | [2.1 Purpose of Threat Hunting](../modules/02-hunter/01-purpose/) | Hunter, SOC, CTI |
| Used | [2.2.1 Hunt Types](../modules/02-hunter/02-methodology/01-hunt-types/) | Hunter, SOC, CTI |
| Used | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |
| Used | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |
| Used | [2.4.1 Assessing CTI for Hunting Value](../modules/02-hunter/04-cti-for-hunters/01-assessing-cti/) | Hunter, SOC, CTI |
| Used | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |
| Used | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |
| Used | [2.6.1 Persistence Techniques](../modules/02-hunter/06-attacker-techniques/01-persistence/) | Hunter, SOC, CTI |

See also: [detection gaps](#detection-gaps), [activity missed by existing security mechanisms](#activity-missed-by-existing-security-mechanisms)

### VirusTotal for hunting

Also: VT, VirusTotal Relations, VirusTotal for hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |
| Used | [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/) | CTI, Hunter |

See also: [tool capabilities for hunting](#tool-capabilities-for-hunting), [purpose, strengths, and weaknesses of VirusTotal](#purpose-strengths-and-weaknesses-of-virustotal)

### purpose, strengths, and weaknesses of VirusTotal

Also: VT for intelligence, hash reputation, one hop not Relations

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/) | CTI, Hunter |
| Used | [3.9.1 VirusTotal (Relations and Behavior Tabs)](../modules/03-cti/09-platforms/01-virustotal/) | CTI, Hunter |

See also: [VirusTotal for hunting](#virustotal-for-hunting), [when to use each external tool in the intelligence process](#when-to-use-each-external-tool-in-the-intelligence-process)

### VirusTotal Relations tab for infrastructure pivoting

Also: use the Relations tab to identify additional adversary infrastructure, VT contacted domain

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.9.1 VirusTotal (Relations and Behavior Tabs)](../modules/03-cti/09-platforms/01-virustotal/) | CTI, Hunter |

See also: [VirusTotal Behavior tab for host and network events](#virustotal-behavior-tab-for-host-and-network-events), [purpose, strengths, and weaknesses of VirusTotal](#purpose-strengths-and-weaknesses-of-virustotal)

### VirusTotal Behavior tab for host and network events

Also: extract file, network, registry, and process events from the Behavior tab, VT Behavior four classes

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.9.1 VirusTotal (Relations and Behavior Tabs)](../modules/03-cti/09-platforms/01-virustotal/) | CTI, Hunter |

See also: [VirusTotal Relations tab for infrastructure pivoting](#virustotal-relations-tab-for-infrastructure-pivoting), [purpose, strengths, and weaknesses of VirusTotal](#purpose-strengths-and-weaknesses-of-virustotal)

---

## W

### weakest vertex constrains the intel product

Also: Diamond product constraint, weakest vertex drops a claim, Adversary empty so no group name

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.7.2 Diamond Model Application in CTI](../modules/03-cti/07-frameworks/02-diamond-cti/) | CTI, Hunter |

Naming the weakest on an incident card is [1.5.2 Diamond Model](../modules/01-soc/05-frameworks/02-diamond-model/).

See also: [filling four vertices and naming the weakest](#filling-four-vertices-and-naming-the-weakest), [apply the Diamond Model to an intelligence problem](#apply-the-diamond-model-to-an-intelligence-problem)

### what to drop from CTI

Also: drop no telemetry expired IOCs noise, what not to extract from a report

| Coverage | Module | Roles |
|----------|--------|-------|
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |
| Taught | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |

See also: [extracting hunt leads from CTI](#extracting-hunt-leads-from-cti), [visibility gaps](#visibility-gaps)

### what tool to use to view PCAP

Also: Wireshark viewer, tshark, not Zeek-as-PCAP

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.2 PCAP Handling](../modules/01-soc/08-site-specific/02-pcap-handling/) | SOC, Hunter, CTI |

See also: [how to download PCAP](#how-to-download-pcap), [requesting a tool to be installed](#requesting-a-tool-to-be-installed)

### when to apply ACH vs Key Assumptions Check

Also: locked story vs competing hyps, neither collect first

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.2.2 Structured Analytic Techniques](../modules/03-cti/02-tradecraft/02-structured-techniques/) | CTI, Hunter |

See also: [Analysis of Competing Hypotheses (ACH)](#analysis-of-competing-hypotheses-ach), [Key Assumptions Check](#key-assumptions-check)

### when to use each external tool in the intelligence process

Also: first external tool, hash vs sample vs history vs live URL

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.3.2 External Tools](../modules/03-cti/03-tools/02-external-tools/) | CTI, Hunter |

See also: [select the appropriate external tool](#select-the-appropriate-external-tool), [purpose, strengths, and weaknesses of VirusTotal](#purpose-strengths-and-weaknesses-of-virustotal)

### where and how to save investigation notes

Also: ticket worklog, fact vs hypothesis, reject desktop notes

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.8.4 Investigation Documentation](../modules/01-soc/08-site-specific/04-investigation-notes/) | SOC, Hunter, CTI |

See also: [changeover report record location](#changeover-report-record-location), [site-specific incident response processes](#site-specific-incident-response-processes)

### weird log

Also: `weird`, Zeek weird

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |
| Taught | [1.2.8 Weird Engine](../modules/01-soc/02-zeek/08-weird-engine/) | SOC, Hunter, CTI |

1.2.1 teaches that the log exists. 1.2.8 teaches `name`, the `notice` flag, and analysis.

### weird activity type (`name`)

Also: weird.name, weird type, dns_unmatched_reply, data_before_established

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.8 Weird Engine](../modules/01-soc/02-zeek/08-weird-engine/) | SOC, Hunter, CTI |

See also: [weird log](#weird-log), [weird notice flag](#weird-notice-flag)

### weird notice flag

Also: weird.notice, notice boolean on weird

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.8 Weird Engine](../modules/01-soc/02-zeek/08-weird-engine/) | SOC, Hunter, CTI |

This is a field on the `weird` row, not the `notice` log.

See also: [weird log](#weird-log), [weird activity type (`name`)](#weird-activity-type-name)

---

## X

### x509 log

Also: `x509`, certificate details log

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

Handshake metadata is taught in [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/). Full `x509` depth is a later topic if it becomes its own module.

---

## Y

### YARA rule structure

Also: YARA meta, YARA strings, YARA condition

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.3 YARA Rules](../modules/01-soc/03-detection/03-yara-rules/) | SOC, Hunter, CTI |

See also: [YARA rules](#yara-rules), [YARA strings and conditions](#yara-strings-and-conditions)

### YARA rules

Also: YARA, YARA signature, file pattern rule

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.3 YARA Rules](../modules/01-soc/03-detection/03-yara-rules/) | SOC, Hunter, CTI |

See also: [how YARA is used with files / memory](#how-yara-is-used-with-files--memory), [YARA rule structure](#yara-rule-structure)

### YARA strings and conditions

Also: YARA ascii, YARA hex, YARA regex, filesize, at 0

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.3.3 YARA Rules](../modules/01-soc/03-detection/03-yara-rules/) | SOC, Hunter, CTI |

See also: [YARA rules](#yara-rules), [matching techniques: ASCII, hex, and regex](#matching-techniques-ascii-hex-and-regex)

---

## Z

### Zeek

Also: Bro, network analysis framework

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

### Zeek vs signature-based IDS

Also: IDS, IPS, Snort, Suricata vs Zeek

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |
