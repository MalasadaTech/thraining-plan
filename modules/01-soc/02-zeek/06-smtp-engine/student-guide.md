# Module 1.2.6 – SMTP Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.6.1 A / B / C ; 1.2.6.2 2b / 3c / 4c ; 1.2.6.3 2b / 3c / 4c  
- Hunter: 1.2.6.1 B / C / C ; 1.2.6.2 3c / 4c / 4c ; 1.2.6.3 3c / 4c / 4c  
- CTI: 1.2.6.1 A / A / B ; 1.2.6.2 1a / 1a / 2b ; 1.2.6.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret SMTP envelope addresses, subject, Message-ID, and endpoints.
2. Describe a transaction without assuming delivery or user action.
3. Create or modify a query for specific SMTP activity.

**Mapped Proficiency Items:**
- K: 1.2.6.1 – SMTP engine
- T: 1.2.6.2 – Analyze a Zeek SMTP log and accurately describe what occurred
- T: 1.2.6.3 – Create a SIEM query to detect specific SMTP activity

## Why This Matters

SMTP records describe mail transactions visible to a network sensor. They help identify envelope addresses and selected headers while leaving mailbox delivery, user action, and attachment behavior to other evidence.

## 1. Reading a mail transaction

| Field | Meaning |
|---|---|
| `mailfrom` | Envelope sender supplied during the SMTP transaction. This differs from the displayed From header. |
| `rcptto` | Envelope recipients, potentially more than one. |
| `subject` | Recorded Subject header when available. |
| `msg_id` | Message-ID header when available; useful context, not a file hash or guaranteed unique identity. |
| Endpoint fields and `uid` | The communicating systems and connection context. |

These values describe the observed transaction and claims within it. A familiar sender name or subject does not authenticate the sender. Encryption, including a STARTTLS transition, may limit which portions the sensor can parse. A missing header can reflect absence in the message, collection limits, or parsing visibility.

## 2. Working through the example

The supplied transaction records envelope sender `sender@example.net`, recipient `jlee@example.org`, subject `Invoice`, and Message-ID `<train-1@example.net>` between two mail systems.

Describe it as: “Zeek observed an SMTP transaction with the recorded envelope sender and recipient, subject `Invoice`, and the supplied Message-ID.” Without a relevant acceptance result or delivery record, avoid claiming successful mailbox delivery. The transaction also does not establish that the user opened the message or that its attachment was malicious.

## 3. Creating a focused SMTP query

This KQL teaching example assumes an ingested table named `ZeekSmtp`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekSmtp
| where TimeGenerated > ago(1d)
| where mailfrom =~ "sender@example.net"
| where subject contains "Invoice"
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],
          mailfrom, rcptto, subject, msg_id
```

This selects transactions using an envelope sender and subject substring. For a recipient search, first confirm whether `rcptto` was ingested as an array or string and use the appropriate membership operation. Sender or subject matches remain leads requiring context.

## Knowledge Check

1. How does mailfrom differ from a displayed From header?
2. Describe the example without claiming mailbox delivery.
3. Modify the query for the same sender regardless of subject.

## Summary

SMTP evidence describes the observed mail transaction and selected headers. Use it to develop a precise lead while keeping delivery, user action, and attachment behavior tied to their own evidence.

## Course Connections

Previous: [1.2.5 – HTTP Engine](../05-http-engine/student-guide.md)

Next: [1.2.7 – Files Engine](../07-files-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — smtp.log](https://docs.zeek.org/en/current/reference/logs/smtp.html)
