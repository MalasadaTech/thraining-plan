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

### answers

Also: DNS answers, response records

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

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

---

## D

### DGA

Also: domain generation algorithm

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.3 DNS Engine](../modules/01-soc/02-zeek/03-dns-engine/) | SOC, Hunter |

See also: [NXDOMAIN](#nxdomain)

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

### event engine

Also: Zeek events, `connection_established`

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

---

## F

### files log

Also: `files`, Zeek files

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

Depth on this log is a later module.

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

---

## I

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

### policy scripts

Also: Zeek scripts, scripting layer, policy script interpreter

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

### proto

See [5-tuple](#5-tuple).

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

### subject

See [certificate subject / issuer](#certificate-subject--issuer).

---

## T

### TAP / SPAN

Also: network TAP, SPAN port, how Zeek sees traffic

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |

### TLS / ssl log

Also: `ssl` log, TLS log, Zeek TLS engine, ssl/tls

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.1 Zeek Concepts](../modules/01-soc/02-zeek/01-concepts/) | SOC, Hunter |
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

1.2.1 teaches that the log exists (Zeek names it `ssl`). 1.2.4 teaches fields and analysis.

### TLS fingerprint

See [JA3](#ja3).

### TLS version

Also: `version`, TLSv13, TLSv12, TLSv11, TLSv10, SSLv3, deprecated TLS

| Coverage | Module | Roles |
|----------|--------|-------|
| Taught | [1.2.4 TLS Engine](../modules/01-soc/02-zeek/04-tls-engine/) | SOC, Hunter |

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
