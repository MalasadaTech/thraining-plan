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

### common Windows privilege escalation methods

Also: Windows privilege escalation, token theft, UAC bypass, service image abuse

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.2 Privilege Escalation Techniques](../modules/02-hunter/06-attacker-techniques/02-privilege-escalation/) | Hunter, SOC, CTI |

See also: [privilege escalation techniques](#privilege-escalation-techniques), [indicators associated with privilege escalation](#indicators-associated-with-privilege-escalation)

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

### convert external findings to internal queries

Also: convert to SIEM query, convert to Zeek query, internal query from enrichment

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |

See also: [hunting leads from external tools](#hunting-leads-from-external-tools), [tool capabilities for hunting](#tool-capabilities-for-hunting)

---

## D

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

See also: [file system activity](#file-system-activity), [hashes and original filename](#hashes-and-original-filename)

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

Depth on this log is a later module.

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

See also: [process activity](#process-activity), [PID, name, and command line](#pid-name-and-command-line), [file hashes](#file-hashes)

### history

Also: `history`, Zeek history flags

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

3-level: awareness. 5- and 7-level: read the flag string.

### how a STIX bundle seeds a hunt

Also: STIX bundle seeds a hunt, bundle as hunt seed, not how to author STIX

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

Authoring STIX is a later CTI item (3.10), not this module.

See also: [STIX as hunt input](#stix-as-hunt-input), [turning STIX objects into hunt leads](#turning-stix-objects-into-hunt-leads)

### http log

Also: `http`, Zeek http

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

Survey only. Field-level teaching is module 1.2.5 (not written yet).

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

### initiating process (file events)

Also: file initiating process, who touched the file, DeviceFileEvents InitiatingProcess

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.2 File System Activity](../modules/01-soc/01-endpoint/02-file-system-activity/) | SOC, Hunter, CTI |

See also: [file system activity](#file-system-activity), [parent-child process](#parent-child-process)

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

## L

### logging framework

Also: Zeek logs, TSV, JSON logs

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

---

## M

### mapping hunts to ATT&CK

Also: map a hunt plan to ATT&CK, map hunt findings to ATT&CK, ATT&CK tactics and techniques

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |

See also: [using MITRE ATT&CK for hunt planning](#using-mitre-attck-for-hunt-planning), [recording ATT&CK IDs from a report](#recording-attck-ids-from-a-report)

### missing SNI

Also: empty SNI, no `server_name`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

See also: [SNI](#sni)

### MX

See [qtype_name](#qtype_name).

---

## N

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

---

## P

### parent-child process

Also: PPID, parent process, InitiatingProcess, ParentImage

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.1.1 Process Activity](../modules/01-soc/01-endpoint/01-process-activity/) | SOC, Hunter, CTI |
| Used | [1.1.2 File System Activity](../modules/01-soc/01-endpoint/02-file-system-activity/) | SOC, Hunter, CTI |

See also: [process activity](#process-activity), [PID, name, and command line](#pid-name-and-command-line), [initiating process (file events)](#initiating-process-file-events)

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

### recording ATT&CK IDs from a report

Also: record ATT&CK IDs, copy printed ATT&CK, ATT&CK IDs if the report has them

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |
| Used | [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/) | Hunter, SOC, CTI |

Mapping hunts to ATT&CK is [2.5.1 Using MITRE ATT&CK for Hunt Planning](../modules/02-hunter/05-framework-application/).

See also: [extracting hunt leads from CTI](#extracting-hunt-leads-from-cti), [mapping hunts to ATT&CK](#mapping-hunts-to-attck)

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

### registry-based persistence

Also: Run key persistence, RunOnce, Winlogon persistence, registry autorun

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.6.1 Persistence Techniques](../modules/02-hunter/06-attacker-techniques/01-persistence/) | Hunter, SOC, CTI |

See also: [persistence techniques](#persistence-techniques), [start menu / startup folder persistence](#start-menu--startup-folder-persistence)

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

Depth on this log is a later module.

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

### subject

See [certificate subject / issuer](#certificate-subject--issuer).

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

Also: Zeek uid, connection UID, pivot key

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |
| Used | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |
| Used | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

The obligation is created in 1.2.2: copy `uid` and search other Zeek logs. Later engines assume that habit.

### unique patterns or behaviors suitable for hunting

Also: hunt-worthy pattern, unique hunt behavior, internal search pattern

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |
| Used | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |
| Used | [2.4.2 Extracting Hunt Leads from CTI](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) | Hunter, SOC, CTI |
| Used | [2.4.3 STIX as Hunt Input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) | Hunter, SOC, CTI |

See also: [hunt hypothesis](#hunt-hypothesis), [hunt development concepts](#hunt-development-concepts)

### URLScan for hunting

Also: urlscan.io, URLScan page scan, URLScan for hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |

See also: [tool capabilities for hunting](#tool-capabilities-for-hunting), [hunting leads from external tools](#hunting-leads-from-external-tools)

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

Depth on this log is a later module.

---

## X

### x509 log

Also: `x509`, certificate details log

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

Handshake metadata is taught in [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/). Full `x509` depth is a later topic if it becomes its own module.

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
