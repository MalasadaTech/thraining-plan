# Module 1.2.8 – Weird Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.8.1 A / B / C ; 1.2.8.2 2b / 3c / 4c ; 1.2.8.3 2b / 3c / 4c  
- Hunter: 1.2.8.1 B / C / C ; 1.2.8.2 3c / 4c / 4c ; 1.2.8.3 3c / 4c / 4c  
- CTI: 1.2.8.1 A / A / A ; 1.2.8.2 1a / 1a / 1a ; 1.2.8.3 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret a weird type, notice flag, endpoints, and available UID.
2. Describe the reported condition from the sensor’s viewpoint.
3. Create or modify a query for a specific weird condition.

**Mapped Proficiency Items:**
- K: 1.2.8.1 – Weird engine
- T: 1.2.8.2 – Analyze a Zeek weird log and accurately describe what occurred
- T: 1.2.8.3 – Create a SIEM query to detect specific weird activity

## Why This Matters

A weird record reports an unexpected condition encountered by Zeek. It is useful because it points to traffic or visibility worth examining, but its meaning depends on the named condition and the surrounding evidence.

## 1. Reading an unexpected condition

| Field | What to examine |
|---|---|
| `name` | The specific unexpected condition reported by Zeek. |
| Endpoint fields | Connection endpoints when the condition is associated with a connection. |
| `uid` | Related connection identifier when available. |
| `notice` | Whether the condition also resulted in a notice under the applicable policy. |
| `addl` | Additional explanatory detail when supplied. |

Weird records may reflect unusual protocol behavior, malformed traffic, sensor visibility gaps, or other analysis conditions. Some do not have a complete connection context. Use the recorded type to develop a question rather than treating “weird” as a severity or malware label.

## 2. Working through the example

The example records `name=data_before_established`, responder `203.0.113.88:8080`, and `uid=CTrain1`.

A supported description is: “Zeek reported data before it had observed an established TCP connection for the supplied flow.” This wording preserves the sensor's viewpoint: it does not prove that the endpoints themselves skipped a handshake. Examine the connection history and, if available, the relevant packets to understand whether traffic behavior or incomplete visibility explains the record.

## 3. Creating a focused weird query

This KQL teaching example assumes an ingested table named `ZeekWeird`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekWeird
| where TimeGenerated > ago(1d)
| where name == "data_before_established"
| where ['id.resp_h'] == "203.0.113.88"
| project TimeGenerated, uid, name, ['id.orig_h'], ['id.resp_h'],
          ['id.resp_p'], notice
```

The query selects a named condition at the example destination. If the record has no UID, use the available endpoints and time to seek context, acknowledging a less certain correlation. A resulting lead can justify investigation even before an incident determination is possible.

## Knowledge Check

1. What does a weird record establish?
2. Describe data_before_established without overstating what happened at the endpoints.
3. How would you broaden the query to that condition across all destinations, and what would you use to investigate matches?

## Summary

A weird record supplies a named condition and any available connection context. Use it to ask a focused follow-up question and separate the sensor’s observation from an explanation of its cause.

## Course Connections

Previous: [1.2.7 – Files Engine](../07-files-engine/student-guide.md)

Next: [1.2 – Zeek Network Evidence Summary](../summary.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — weird.log and notice.log](https://docs.zeek.org/en/current/reference/logs/weird-and-notice.html)
