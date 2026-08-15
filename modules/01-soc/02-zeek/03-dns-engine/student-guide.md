# Module 1.2.3 – DNS Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3-level (A/2b) → 5-level (B/3c) → 7-level (C/4c)  
- Hunter: Starts higher (B/3c → C/4c)  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of the Zeek `dns` log and why it is critical for detection and hunting.
2. Identify and interpret the most important fields in a `dns` log entry.
3. Recognize common DNS query types and response codes.
4. Analyze a `dns` log entry and accurately describe what occurred.
5. Create basic SIEM queries to detect suspicious DNS activity.

**Mapped Proficiency Items:**
- K: 1.2.3.1 – DNS engine
- T: 1.2.3.2 – Analyze a Zeek DNS log and accurately describe what occurred
- T: 1.2.3.3 – Create a SIEM query to detect specific DNS activity

---

## 1. Key Concepts

### 1.1 Purpose of the dns Log

The Zeek `dns` log records DNS queries and responses observed on the network. Because almost every network connection begins with a DNS lookup, this log provides excellent early visibility into:

- Domains being contacted
- Potential command-and-control (C2) channels
- DNS tunneling / data exfiltration
- Malware using domain generation algorithms (DGAs)
- Phishing and malicious infrastructure

DNS is often one of the highest-value logs for both alert triage and proactive hunting.

### 1.2 Key Fields

Here are the fields you must know well:

| Field            | Description                                      | Why It Matters |
|------------------|--------------------------------------------------|----------------|
| `ts`             | Timestamp of the query                           | When it happened |
| `uid`            | Unique connection identifier                     | Links to `conn` and other logs |
| `id.orig_h`      | Client (source) IP that issued the query         | Who is asking |
| `id.resp_h`      | DNS server IP                                    | Which resolver was used |
| `proto`          | Transport protocol (usually udp)                 | Mostly UDP, sometimes TCP |
| `query`          | The domain name being looked up                  | **Most important field** |
| `qtype_name`     | Query type (A, AAAA, CNAME, MX, TXT, etc.)       | What kind of record |
| `qclass_name`    | Query class (almost always C_INTERNET)           | Rarely interesting |
| `rcode_name`     | Response code (NOERROR, NXDOMAIN, SERVFAIL…)     | Success or failure |
| `answers`        | List of answers returned                         | What the domain resolved to |
| `ttls`           | Time-to-live values for the answers              | Caching behavior |
| `rejected`       | Whether the query was rejected                   | Policy or error indicator |
| `AA`             | Authoritative Answer flag                        | Whether the response came from an authoritative server |

**Most critical fields for daily work:**  
`query`, `qtype_name`, `rcode_name`, `answers`, `id.orig_h`, `uid`

### 1.3 Common Query Types (qtype_name)

| Type     | Meaning                              | Typical Use / Notes |
|----------|--------------------------------------|---------------------|
| **A**      | IPv4 address                         | Most common |
| **AAAA**   | IPv6 address                         | Increasingly common |
| **CNAME**  | Canonical name (alias)               | Domain pointing to another domain |
| **MX**     | Mail exchange                        | Email routing |
| **TXT**    | Text record                          | Often used for verification, SPF, or tunneling |
| **NS**     | Name server                          | Delegation |
| **PTR**    | Reverse lookup (IP → name)           | Useful for investigation |
| **SOA**    | Start of Authority                   | Zone information |
| **SRV**    | Service location                     | Service discovery |

**Analyst tip:** High volumes of unusual query types (especially TXT or NULL) can indicate DNS tunneling.

### 1.4 Common Response Codes (rcode_name)

| Code         | Meaning                          | Typical Interpretation |
|--------------|----------------------------------|------------------------|
| **NOERROR**    | Successful response              | Domain exists and answered |
| **NXDOMAIN**   | Non-existent domain              | Domain does not exist (common with DGAs or typos) |
| **SERVFAIL**   | Server failure                   | Resolver or authoritative server problem |
| **REFUSED**    | Query refused                    | Policy or access control |
| **FORMERR**    | Format error                     | Malformed query |

**Hunting note:** A host generating large numbers of NXDOMAIN responses is a classic DGA or mistyped-domain indicator.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Successful Lookup

```
ts: 2026-08-14T19:12:05.456Z
uid: CXyZaBcDeFgHiJkL
id.orig_h: 10.10.50.23
id.resp_h: 10.10.1.53
query: www.example.com
qtype_name: A
rcode_name: NOERROR
answers: ["93.184.216.34"]
ttls: [3600]
```

**Interpretation:**  
Internal host successfully resolved `www.example.com` to an IPv4 address. Normal behavior.

### Example 2: NXDOMAIN (Non-existent Domain)

```
id.orig_h: 10.10.50.88
query: kjh3g4f9d2s1a0.example-malware.com
qtype_name: A
rcode_name: NXDOMAIN
answers: []
```

**Interpretation:**  
The domain does not exist. This could be a typo, a retired domain, or part of a domain-generation algorithm (DGA) used by malware.

### Example 3: Suspicious TXT Query Volume

```
id.orig_h: 10.10.22.17
query: longstringdatahere.tunnel.example.com
qtype_name: TXT
rcode_name: NOERROR
answers: ["v=encodedpayload..."]
```

**Interpretation:**  
TXT records are sometimes abused for DNS tunneling or covert channels. A single TXT query is not automatically malicious, but high frequency or unusually long queries deserve investigation.

---

## 3. Hands-On Exercise

**Objective:** Practice interpreting DNS logs and writing simple detection logic.

**Instructions:**

1. Review the three examples above and write a one-sentence summary for each.
2. Write a SIEM-style pseudo-query that would find:
   - Hosts generating a high number of NXDOMAIN responses
   - Unusual volumes of TXT queries from a single host
3. Explain how you would pivot from a suspicious DNS query to the related network connection using the `uid`.

**Expected Outcome:**
- Accurate short summaries
- Two useful pseudo-queries
- Correct understanding of the `uid` pivot to the `conn` log (and potentially other logs)

---

## 4. Knowledge Check

1. What is the primary purpose of the Zeek `dns` log?
2. Which field contains the domain name that was queried?
3. What does the response code `NXDOMAIN` indicate?
4. Name two query types that are sometimes abused for data tunneling.
5. Why is the `uid` field important when analyzing DNS activity?

---

## 5. Summary

- The `dns` log provides early and high-value visibility into domains being contacted.
- Critical fields: `query`, `qtype_name`, `rcode_name`, `answers`, `id.orig_h`, and `uid`.
- NXDOMAIN spikes and unusual query types (TXT, NULL, etc.) are strong hunting leads.
- Always pivot with `uid` to the corresponding `conn` log (and other protocol logs) for full context.
- DNS is one of the best logs for detecting C2, DGAs, phishing infrastructure, and tunneling.

---

## 6. References & Further Reading

- Zeek dns.log documentation: https://docs.zeek.org/en/current/scripts/base/protocols/dns/main.zeek.html
- Related modules:
  - 1.2.1 – Zeek Concepts
  - 1.2.2 – Conn Engine
  - 1.2.5 – HTTP Engine
  - 1.2.4 – TLS Engine
