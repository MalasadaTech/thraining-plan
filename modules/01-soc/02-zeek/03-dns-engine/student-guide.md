# Module 1.2.3 – DNS Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.3.1 A / B / C ; 1.2.3.2 2b / 3c / 4c ; 1.2.3.3 2b / 3c / 4c  
- Hunter: 1.2.3.1 B / C / C ; 1.2.3.2 3c / 4c / 4c ; 1.2.3.3 3c / 4c / 4c  
- CTI: 1.2.3.1 A / B / B ; 1.2.3.2 1a / 2b / 3c ; 1.2.3.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret DNS question, response, record type, and endpoints.
2. Describe a DNS observation and distinguish it from later communication.
3. Create or modify a query for specific DNS activity.

**Mapped Proficiency Items:**
- K: 1.2.3.1 – DNS engine
- T: 1.2.3.2 – Analyze a Zeek DNS log and accurately describe what occurred
- T: 1.2.3.3 – Create a SIEM query to detect specific DNS activity

## Why This Matters

DNS evidence connects a question about a name to the response observed on the network. Distinguishing the resolver from the returned address helps prevent a common error when moving from a lookup to a connection investigation.

## 1. Reading a DNS transaction

| Field | Meaning |
|---|---|
| `query` | The requested name. |
| `qtype_name` | The requested record type. |
| `answers` | Observed answer values, which may contain addresses or names. |
| `rcode_name` | Response code, where recorded, useful when interpreting an empty answer. |
| `id.orig_h` | The querying endpoint visible to the sensor. |
| `id.resp_h` | The DNS server contacted, often a recursive resolver. |
| `uid` | Connection identifier for related records; multiple DNS transactions may share it. |

A requests an IPv4 address; AAAA an IPv6 address; MX a mail exchanger; NS a name server; TXT text data; and CNAME a canonical-name alias. A response can include an alias chain. The responder address is the server asked, while returned addresses belong in the answer data. A blank answer needs interpretation using the response code and capture context.

## 2. Working through the example

The example records `192.0.2.10` asking resolver `192.0.2.53` for an A record for `update.example`, with `answers=["203.0.113.88"]` and `rcode_name=NOERROR`.

A supported description is: “The observed client asked `192.0.2.53` for the IPv4 address of `update.example` and received `203.0.113.88`.” A subsequent connection to that address would be separate evidence. If the observed client is itself a resolver, additional records may be needed to identify the original endpoint behind the request.

## 3. Creating a focused DNS query

This KQL teaching example assumes an ingested table named `ZeekDns`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekDns
| where TimeGenerated > ago(1d)
| where query =~ "update.example" and qtype_name == "A"
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],
          query, qtype_name, answers, rcode_name
```

This selects questions for one name and record type. To include IPv6 questions, use `qtype_name in ("A", "AAAA")`. Compare actual answer values and response codes rather than assuming every matching question received an address.

## Knowledge Check

1. Where do you find the DNS server and the returned address?
2. Describe the example and explain whether it proves a connection to the answer.
3. Modify the query for both IPv4 and IPv6 questions for the same name.

## Summary

A DNS description identifies the observed client, resolver, question, type, and response. It supplies a lead for subsequent activity rather than proving that the client contacted the returned address.

## Course Connections

Previous: [1.2.2 – Conn Engine](../02-conn-engine/student-guide.md)

Next: [1.2.4 – TLS Engine](../04-tls-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — dns.log](https://docs.zeek.org/en/current/reference/logs/dns.html)
