# Module 1.2.2 – Conn Engine

- Interpret connection endpoints, state, history, and identifiers.
- Describe a connection using the supplied evidence.
- Create or modify a query for specific connection activity.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

A connection record gives you a network-level starting point: the endpoints, transport, and progress Zeek observed. That description helps you select the related protocol records without assigning a purpose to the traffic too early.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading connection fields

Read originator, responder, transport, state, history, and UID. Originator is a connection role, not a synonym for internal.

**Speaker notes:** Read endpoint pairs together and use the case of history letters to distinguish direction. Keep state explanations grounded in the TCP example.

---

## Reference — Reading connection fields

| Field | Meaning |
|---|---|
| `uid` | Connection identifier used to relate records from the same Zeek observation context. |
| `id.orig_h`, `id.orig_p` | Originator address and port from the sensor's view. |
| `id.resp_h`, `id.resp_p` | Responder address and port. |
| `proto`, `service` | Transport and identified application service when available. Port alone does not establish service. |
| `conn_state` | A summary of observed connection progress. Interpret it for the protocol. |
| `history` | Encoded observations; case distinguishes the originator and responder sides. |

**Speaker notes:** Read endpoint pairs together and use the case of history letters to distinguish direction. Keep state explanations grounded in the TCP example. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example

The example records TCP to 203.0.113.88:443 with normal establishment and termination. CTrain1 is the connection pivot.

**Speaker notes:** Have learners cite proto before calling it TCP. Ask what evidence would be needed to name an application or process.

---

## Supplied example

The supplied record shows originator `192.0.2.10:51000`, responder `203.0.113.88:443`, `proto=tcp`, `conn_state=SF`, and `uid=CTrain1`.

**Speaker notes:** Have learners cite proto before calling it TCP. Ask what evidence would be needed to name an application or process.

---

## Creating a focused connection query

Select destination, transport, and state. S0 means no response observed; it does not explain why.

**Speaker notes:** Use SF and S0 to show that changing a predicate changes the question. Explain sensor visibility as a possible limit.

---

## Reference — Creating a focused connection query

| where TimeGenerated > ago(1d)
| where ['id.resp_h'] == "203.0.113.88"
| where ['id.resp_p'] == 443 and proto == "tcp"
| where conn_state == "SF"
| project TimeGenerated, uid, ['id.orig_h'], ['id.orig_p'],

**Speaker notes:** Use SF and S0 to show that changing a predicate changes the question. Explain sensor visibility as a possible limit. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused connection query

```kusto
ZeekConn
| where TimeGenerated > ago(1d)
| where ['id.resp_h'] == "203.0.113.88"
| where ['id.resp_p'] == 443 and proto == "tcp"
| where conn_state == "SF"
| project TimeGenerated, uid, ['id.orig_h'], ['id.orig_p'],
          ['id.resp_h'], ['id.resp_p'], conn_state, history
```

**Speaker notes:** Use SF and S0 to show that changing a predicate changes the question. Explain sensor visibility as a possible limit. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. How do originator and responder differ from internal and external?
2. Describe the supplied record and name the pivot identifier.
3. Modify the query for unanswered attempts and explain the limit.

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

A connection finding describes the endpoints, transport, and observed progress. Use the connection identifier to seek related records and keep explanations of purpose or failure tied to additional evidence.

Previous: [1.2.1 – Zeek Concepts](../01-concepts/student-guide.md)

Next: [1.2.3 – DNS Engine](../03-dns-engine/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Zeek — conn.log](https://docs.zeek.org/en/current/reference/logs/conn.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
