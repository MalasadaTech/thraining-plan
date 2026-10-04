# Module 1.2.8 – Weird Engine

- Interpret a weird type, notice flag, endpoints, and available UID.
- Describe the reported condition from the sensor’s viewpoint.
- Create or modify a query for a specific weird condition.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

A weird record reports an unexpected condition encountered by Zeek. It is useful because it points to traffic or visibility worth examining, but its meaning depends on the named condition and the surrounding evidence.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading an unexpected condition

Read the weird name, available endpoints/UID, and notice flag. The name describes an analysis condition.

**Speaker notes:** Distinguish the weird type from its notice flag and from an incident decision. A condition can warrant a ticket under local procedure without proving compromise.

---

## Reference — Reading an unexpected condition

| Field | What to examine |
|---|---|
| `name` | The specific unexpected condition reported by Zeek. |
| Endpoint fields | Connection endpoints when the condition is associated with a connection. |
| `uid` | Related connection identifier when available. |
| `notice` | Whether the condition also resulted in a notice under the applicable policy. |
| `addl` | Additional explanatory detail when supplied. |

**Speaker notes:** Distinguish the weird type from its notice flag and from an incident decision. A condition can warrant a ticket under local procedure without proving compromise. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example

Zeek reports data before observed establishment. That does not prove the endpoints skipped a handshake.

**Speaker notes:** Emphasize “observed” when discussing handshake progress. Ask what packet loss or midstream capture would change.

---

## Supplied example

The example records `name=data_before_established`, responder `203.0.113.88:8080`, and `uid=CTrain1`.

**Speaker notes:** Emphasize “observed” when discussing handshake progress. Ask what packet loss or midstream capture would change.

---

## Creating a focused weird query

Select the named condition and use available connection context to investigate its cause.

**Speaker notes:** Have learners explain the broader scope and the correlation limits of a missing UID.

---

## Reference — Creating a focused weird query

| where TimeGenerated > ago(1d)
| where name == "data_before_established"
| where ['id.resp_h'] == "203.0.113.88"
| project TimeGenerated, uid, name, ['id.orig_h'], ['id.resp_h'],

**Speaker notes:** Have learners explain the broader scope and the correlation limits of a missing UID. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused weird query

```kusto
ZeekWeird
| where TimeGenerated > ago(1d)
| where name == "data_before_established"
| where ['id.resp_h'] == "203.0.113.88"
| project TimeGenerated, uid, name, ['id.orig_h'], ['id.resp_h'],
          ['id.resp_p'], notice
```

**Speaker notes:** Have learners explain the broader scope and the correlation limits of a missing UID. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. What does a weird record establish?
2. Describe data_before_established without overstating what happened at the endpoints.
3. How would you broaden the query to that condition across all destinations, and what would you use to investigate matches?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

A weird record supplies a named condition and any available connection context. Use it to ask a focused follow-up question and separate the sensor’s observation from an explanation of its cause.

Previous: [1.2.7 – Files Engine](../07-files-engine/student-guide.md)

Next: [1.3.1 – SIGMA Rules](../../03-detection/01-sigma-rules/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Zeek — weird.log and notice.log](https://docs.zeek.org/en/current/reference/logs/weird-and-notice.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
