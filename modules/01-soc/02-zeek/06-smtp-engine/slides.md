# Module 1.2.6 – SMTP Engine

- Interpret SMTP envelope addresses, subject, Message-ID, and endpoints.
- Describe a transaction without assuming delivery or user action.
- Create or modify a query for specific SMTP activity.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

SMTP records describe mail transactions visible to a network sensor. They help identify envelope addresses and selected headers while leaving mailbox delivery, user action, and attachment behavior to other evidence.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading a mail transaction

Envelope sender and recipients differ from message headers. Message-ID supplies context rather than a file hash.

**Speaker notes:** Use two distinct sender identities to illustrate envelope versus header. Explain that neither alone proves authenticity.

---

## Reference — Reading a mail transaction

| Field | Meaning |
|---|---|
| `mailfrom` | Envelope sender supplied during the SMTP transaction. This differs from the displayed From header. |
| `rcptto` | Envelope recipients, potentially more than one. |
| `subject` | Recorded Subject header when available. |
| `msg_id` | Message-ID header when available; useful context, not a file hash or guaranteed unique identity. |
| Endpoint fields and `uid` | The communicating systems and connection context. |

**Speaker notes:** Use two distinct sender identities to illustrate envelope versus header. Explain that neither alone proves authenticity. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example

The observed transaction contains the supplied addresses and subject. Delivery and user action need additional evidence.

**Speaker notes:** Ask what would support “delivered” or “opened.” Learners should name additional evidence, not assume it from the subject.

---

## Supplied example

The supplied transaction records envelope sender `sender@example.net`, recipient `jlee@example.org`, subject `Invoice`, and Message-ID `<train-1@example.net>` between two mail systems.

**Speaker notes:** Ask what would support “delivered” or “opened.” Learners should name additional evidence, not assume it from the subject.

---

## Creating a focused SMTP query

Search the chosen sender and subject; confirm recipient data types before writing a membership test.

**Speaker notes:** Discuss why array and string recipient searches differ. Keep the worked query on verified scalar fields.

---

## Reference — Creating a focused SMTP query

| where TimeGenerated > ago(1d)
| where mailfrom =~ "sender@example.net"
| where subject contains "Invoice"
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],

**Speaker notes:** Discuss why array and string recipient searches differ. Keep the worked query on verified scalar fields. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused SMTP query

```kusto
ZeekSmtp
| where TimeGenerated > ago(1d)
| where mailfrom =~ "sender@example.net"
| where subject contains "Invoice"
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],
          mailfrom, rcptto, subject, msg_id
```

**Speaker notes:** Discuss why array and string recipient searches differ. Keep the worked query on verified scalar fields. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. How does mailfrom differ from a displayed From header?
2. Describe the example without claiming mailbox delivery.
3. Modify the query for the same sender regardless of subject.

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

SMTP evidence describes the observed mail transaction and selected headers. Use it to develop a precise lead while keeping delivery, user action, and attachment behavior tied to their own evidence.

Previous: [1.2.5 – HTTP Engine](../05-http-engine/student-guide.md)

Next: [1.2.7 – Files Engine](../07-files-engine/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Zeek — smtp.log](https://docs.zeek.org/en/current/reference/logs/smtp.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
