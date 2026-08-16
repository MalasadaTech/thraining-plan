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

See also: [tool capabilities for hunting](#tool-capabilities-for-hunting), [hunting leads from external tools](#hunting-leads-from-external-tools)

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

See also: [ATT&CK techniques and sub-techniques](#attck-techniques-and-sub-techniques), [mapping observed activity to ATT&CK](#mapping-observed-activity-to-attck)

### ATT&CK techniques and sub-techniques

Also: ATT&CK technique, sub-technique, T1059.001

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.1 MITRE ATT&CK](../modules/01-soc/05-frameworks/01-attck/) | SOC, Hunter, CTI |

See also: [ATT&CK tactics](#attck-tactics), [MITRE ATT&CK purpose and structure](#mitre-attck-purpose-and-structure)

### ATT&CK coverage analysis

Also: ATT&CK coverage, coverage analysis for hunting, Navigator as a view

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |

See also: [mapping hunts to ATT&CK](#mapping-hunts-to-attck), [using ATT&CK to identify detection or visibility gaps](#using-attck-to-identify-detection-or-visibility-gaps)

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

### certificate subject / issuer

Also: `subject`, `issuer`, CN, certificate name

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

See also: [self-signed certificate](#self-signed-certificate), [SNI vs certificate mismatch](#sni-vs-certificate-mismatch)

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

Collection *sources* (OSINT, commercial, internal) are a later item (3.1.8), not this module.

See also: [intelligence lifecycle](#intelligence-lifecycle), [data](#data)

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

### common persistence locations (Run, Services)

Also: Run key, RunOnce, Services key, registry persistence locations as examples

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.4 Registry Activity](../modules/01-soc/01-endpoint/04-registry-activity/) | SOC, Hunter, CTI |

Persistence *techniques* are [2.6.1 Persistence Techniques](../modules/02-hunter/06-attacker-techniques/01-persistence/).

See also: [registry activity](#registry-activity), [registry-based persistence](#registry-based-persistence)

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

### Cyber Kill Chain purpose

Also: Kill Chain, Lockheed Martin Kill Chain

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.3 Cyber Kill Chain](../modules/01-soc/05-frameworks/03-cyber-kill-chain/) | SOC, Hunter, CTI |

See also: [Kill Chain stages](#kill-chain-stages), [identifying the stage and rejecting the previous or next](#identifying-the-stage-and-rejecting-the-previous-or-next)

---

## D

### Diamond Model purpose

Also: Diamond Model, intrusion diamond

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.2 Diamond Model](../modules/01-soc/05-frameworks/02-diamond-model/) | SOC, Hunter, CTI |

See also: [Diamond vertices: Adversary, Capability, Infrastructure, Victim](#diamond-vertices-adversary-capability-infrastructure-victim)

### Diamond vertices: Adversary, Capability, Infrastructure, Victim

Also: Adversary vertex, Capability vertex, Infrastructure vertex, Victim vertex

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.2 Diamond Model](../modules/01-soc/05-frameworks/02-diamond-model/) | SOC, Hunter, CTI |

See also: [filling four vertices and naming the weakest](#filling-four-vertices-and-naming-the-weakest), [using Diamond for analysis and attribution](#using-diamond-for-analysis-and-attribution)

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

Production and dissemination *process* depth is unit 3.11, not this module.

See also: [intelligence lifecycle](#intelligence-lifecycle)

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

### empty SNI

See [missing SNI](#missing-sni).

### evaluation and feedback

Also: feedback, evaluation, intelligence feedback loop

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

See also: [intelligence lifecycle](#intelligence-lifecycle)

### event engine

Also: Zeek events, `connection_established`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

### extracting hunt leads from CTI

Also: extract hunt leads, pull leads from a report, CTI extract for hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

See also: [hunt-suitable TTPs](#hunt-suitable-ttps), [hunt-suitable artifacts](#hunt-suitable-artifacts), [what to drop from CTI](#what-to-drop-from-cti)

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

See also: [Diamond vertices: Adversary, Capability, Infrastructure, Victim](#diamond-vertices-adversary-capability-infrastructure-victim)

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

### how a STIX bundle seeds a hunt

Also: STIX bundle seeds a hunt, bundle as hunt seed, not how to author STIX

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

Authoring STIX is a later CTI item (3.10), not this module.

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

### hunt development concepts

Also: developing a hunt, hunt intake card, hunt planning card

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |

See also: [hunt hypothesis](#hunt-hypothesis), [scoping a hunt](#scoping-a-hunt), [prioritizing hunts](#prioritizing-hunts)

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

### identifying the stage and rejecting the previous or next

Also: Kill Chain neighbor stage, not previous not next

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.3 Cyber Kill Chain](../modules/01-soc/05-frameworks/03-cyber-kill-chain/) | SOC, Hunter, CTI |

See also: [Kill Chain stages](#kill-chain-stages), [using the Kill Chain to understand attack progression](#using-the-kill-chain-to-understand-attack-progression)

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

### Kill Chain stages

Also: Reconnaissance Delivery Exploitation Installation C2 Actions on Objectives, Weaponization

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.3 Cyber Kill Chain](../modules/01-soc/05-frameworks/03-cyber-kill-chain/) | SOC, Hunter, CTI |

See also: [Cyber Kill Chain purpose](#cyber-kill-chain-purpose)

---

## L

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

### mapping observed activity to ATT&CK

Also: map an alert to ATT&CK, tactic plus technique plus cite

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.1 MITRE ATT&CK](../modules/01-soc/05-frameworks/01-attck/) | SOC, Hunter, CTI |

Hunt planning maps are [2.5.1](../modules/02-hunter/05-framework-application/).

See also: [ATT&CK tactics](#attck-tactics), [mapping hunts to ATT&CK](#mapping-hunts-to-attck)

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

See also: [ATT&CK tactics](#attck-tactics), [mapping observed activity to ATT&CK](#mapping-observed-activity-to-attck)

### MX

See [qtype_name](#qtype_name).

---

## N

### network activity (endpoint)

Also: host network activity, endpoint network, DeviceNetworkEvents, Sysmon Event ID 3

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.3 Network Activity (Endpoint)](../modules/01-soc/01-endpoint/03-network-activity/) | SOC, Hunter, CTI |

See also: [host-observed vs Zeek](#host-observed-vs-zeek), [source / dest IP and port, protocol, direction](#source--dest-ip-and-port-protocol-direction)

### notice log

Also: `notice`, Zeek notices

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

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

### other local categories

Also: other alert category, local SOC buckets

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.4.4 Common Alert Categorizations](../modules/01-soc/04-alerts/04-categorizations/) | SOC, Hunter, CTI |

See also: [assigning a category and ruling out the adjacent one](#assigning-a-category-and-ruling-out-the-adjacent-one)

---

## P

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

### planning and direction

Also: direction, intelligence planning, requirements direction

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

How to write PIRs is a later item (3.1.4), not this module.

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

### proto

See [5-tuple](#5-tuple).

### purpose and activities in each stage

Also: purpose of each lifecycle stage, activities in each stage

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |

See also: [intelligence lifecycle](#intelligence-lifecycle), [stages of the intelligence lifecycle](#stages-of-the-intelligence-lifecycle)

### purpose of threat hunting

Also: why hunt exists, hunt purpose, purpose of hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.1 Purpose of Threat Hunting](../modules/02-hunter/01-purpose/) | Hunter, SOC, CTI |
| Used | [2.2.1 Hunt Types](../modules/02-hunter/02-methodology/01-hunt-types/) | Hunter, SOC, CTI |
| Used | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |

See also: [threat hunting in the security program](#threat-hunting-in-the-security-program)

---

## Q

### qtype_name

Also: DNS query type, `qtype`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

Types taught: A, AAAA, CNAME, MX, TXT, NS, PTR, SOA, SRV, NULL.

### query

Also: DNS query, queried domain, `query`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

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

See also: [tool capabilities for hunting](#tool-capabilities-for-hunting), [hunting leads from external tools](#hunting-leads-from-external-tools)

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

### SPAN

See [TAP / SPAN](#tap--span).

### ssl log

See [TLS / ssl log](#tls--ssl-log).

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

See also: [hunt-relevant STIX objects](#hunt-relevant-stix-objects), [how a STIX bundle seeds a hunt](#how-a-stix-bundle-seeds-a-hunt)

### STIX objects a hunter uses

Also: indicator attack-pattern observed-data malware threat-actor intrusion-set relationship

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

Core STIX object inventory for production is a later CTI item (3.10), not this module.

See also: [hunt-relevant STIX objects](#hunt-relevant-stix-objects), [STIX as hunt input](#stix-as-hunt-input)

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

### technical intelligence

Also: technical intel, technical type, technical observables

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [intelligence types](#intelligence-types), [tactical intelligence](#tactical-intelligence)

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

See also: [tool capabilities for hunting](#tool-capabilities-for-hunting), [hunting leads from external tools](#hunting-leads-from-external-tools)

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

See also: [Diamond Model purpose](#diamond-model-purpose), [filling four vertices and naming the weakest](#filling-four-vertices-and-naming-the-weakest)

### using the Kill Chain to understand attack progression

Also: Kill Chain progression, where you are in the intrusion

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.5.3 Cyber Kill Chain](../modules/01-soc/05-frameworks/03-cyber-kill-chain/) | SOC, Hunter, CTI |

See also: [Cyber Kill Chain purpose](#cyber-kill-chain-purpose), [identifying the stage and rejecting the previous or next](#identifying-the-stage-and-rejecting-the-previous-or-next)

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

See also: [tool capabilities for hunting](#tool-capabilities-for-hunting), [hunting leads from external tools](#hunting-leads-from-external-tools)

---

## W

### what to drop from CTI

Also: drop no telemetry expired IOCs noise, what not to extract from a report

| Coverage | Module | Roles |
|----------|--------|-------|
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |
| Taught | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |

See also: [extracting hunt leads from CTI](#extracting-hunt-leads-from-cti), [visibility gaps](#visibility-gaps)

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
