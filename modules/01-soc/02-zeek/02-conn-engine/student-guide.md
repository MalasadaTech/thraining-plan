# Module 1.2.2 – Conn Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.2.1 A / B / C ; 1.2.2.2 2b / 3c / 4c ; 1.2.2.3 2b / 3c / 4c  
- Hunter: 1.2.2.1 B / C / C ; 1.2.2.2 3c / 4c / 4c ; 1.2.2.3 3c / 4c / 4c  
- CTI: 1.2.2.1 A / A / B ; 1.2.2.2 1a / 1a / 2b ; 1.2.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret connection endpoints, state, history, and identifiers.
2. Describe a connection using the supplied evidence.
3. Create or modify a query for specific connection activity.

**Mapped Proficiency Items:**
- K: 1.2.2.1 – Conn engine
- T: 1.2.2.2 – Analyze a Zeek conn log and accurately describe what occurred
- T: 1.2.2.3 – Create a SIEM query to detect specific connection activity

## Why This Matters

A connection record gives you a network-level starting point: the endpoints, transport, and progress Zeek observed. That description helps you select the related protocol records without assigning a purpose to the traffic too early.

## 1. Reading connection fields

| Field | Meaning |
|---|---|
| `uid` | Connection identifier used to relate records from the same Zeek observation context. |
| `id.orig_h`, `id.orig_p` | Originator address and port from the sensor's view. |
| `id.resp_h`, `id.resp_p` | Responder address and port. |
| `proto`, `service` | Transport and identified application service when available. Port alone does not establish service. |
| `conn_state` | A summary of observed connection progress. Interpret it for the protocol. |
| `history` | Encoded observations; case distinguishes the originator and responder sides. |

For the TCP examples, `SF` indicates normal establishment and termination; `S0` indicates an attempt with no reply observed; `REJ` indicates rejection. In history, letters such as S, H, F, and R concern SYN, SYN-ACK, FIN, and reset observations, with lowercase representing the responder. An originator can be external to your network. Partial capture can limit what the state tells you.

## 2. Working through the example

The supplied record shows originator `192.0.2.10:51000`, responder `203.0.113.88:443`, `proto=tcp`, `conn_state=SF`, and `uid=CTrain1`.

Describe it as: “Zeek observed a TCP connection from `192.0.2.10:51000` to `203.0.113.88:443` with normal establishment and termination.” The addresses, ports, protocol, and state support that description. Look for `CTrain1` in relevant protocol logs to learn more. The record alone does not identify a process, establish HTTPS, or prove a malicious purpose.

## 3. Creating a focused connection query

This KQL teaching example assumes an ingested table named `ZeekConn`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekConn
| where TimeGenerated > ago(1d)
| where ['id.resp_h'] == "203.0.113.88"
| where ['id.resp_p'] == 443 and proto == "tcp"
| where conn_state == "SF"
| project TimeGenerated, uid, ['id.orig_h'], ['id.orig_p'],
          ['id.resp_h'], ['id.resp_p'], conn_state, history
```

The query selects the specified responder, port, transport, and state. Change the state to `S0` to investigate attempts for which the sensor observed no response; the results would not establish why a response was absent.

## Knowledge Check

1. How do originator and responder differ from internal and external?
2. Describe the supplied record and name the pivot identifier.
3. Modify the query for unanswered attempts and explain the limit.

## Summary

A connection finding describes the endpoints, transport, and observed progress. Use the connection identifier to seek related records and keep explanations of purpose or failure tied to additional evidence.

## Course Connections

Previous: [1.2.1 – Zeek Concepts](../01-concepts/student-guide.md)

Next: [1.2.3 – DNS Engine](../03-dns-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — conn.log](https://docs.zeek.org/en/current/reference/logs/conn.html)
