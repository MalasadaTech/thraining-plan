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

### history

Also: `history`, Zeek history flags

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.2 Conn Engine](../modules/01-soc/02-zeek/02-conn-engine/) | SOC, Hunter |

3-level: awareness. 5- and 7-level: read the flag string.

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

### information

Also: organized data, context, parsed alert, rewritten log story

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.1 Data, Information, and Intelligence](../modules/03-cti/01-core-intel/01-data-info-intel/) | CTI, Hunter |
| Used | [3.1.2 Intelligence Lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) | CTI, Hunter |
| Used | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [data](#data), [intelligence](#intelligence)

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

---

## P

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

See also: [scoping a hunt](#scoping-a-hunt), [hunt development concepts](#hunt-development-concepts)

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

### strategic intelligence

Also: strategic intel, strategic type, posture intelligence

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [3.1.3 Intelligence Types](../modules/03-cti/01-core-intel/03-intelligence-types/) | CTI, Hunter |

See also: [intelligence types](#intelligence-types)

### subject

See [certificate subject / issuer](#certificate-subject--issuer).

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

See also: [hunt hypothesis](#hunt-hypothesis), [hunt development concepts](#hunt-development-concepts)

### URLScan for hunting

Also: urlscan.io, URLScan page scan, URLScan for hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |

See also: [tool capabilities for hunting](#tool-capabilities-for-hunting), [hunting leads from external tools](#hunting-leads-from-external-tools)

---

## V

### visibility gaps

Also: visibility gap, no telemetry, cannot see, blind segment

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.1 Purpose of Threat Hunting](../modules/02-hunter/01-purpose/) | Hunter, SOC, CTI |
| Used | [2.2.1 Hunt Types](../modules/02-hunter/02-methodology/01-hunt-types/) | Hunter, SOC, CTI |
| Used | [2.2.2 Hunt Development Concepts](../modules/02-hunter/02-methodology/02-hunt-development/) | Hunter, SOC, CTI |
| Used | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |

See also: [detection gaps](#detection-gaps), [activity missed by existing security mechanisms](#activity-missed-by-existing-security-mechanisms)

### VirusTotal for hunting

Also: VT, VirusTotal Relations, VirusTotal for hunting

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [2.3.1 Tool Capabilities for Hunting](../modules/02-hunter/03-online-tools/) | Hunter, SOC, CTI |

See also: [tool capabilities for hunting](#tool-capabilities-for-hunting), [hunting leads from external tools](#hunting-leads-from-external-tools)

---

## W

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
