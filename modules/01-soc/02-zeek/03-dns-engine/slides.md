# Module 1.2.3 – DNS Engine

- Interpret DNS question, response, record type, and endpoints.
- Describe a DNS observation and distinguish it from later communication.
- Create or modify a query for specific DNS activity.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

DNS evidence connects a question about a name to the response observed on the network. Distinguishing the resolver from the returned address helps prevent a common error when moving from a lookup to a connection investigation.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading a DNS transaction

Separate querying endpoint, resolver, requested name/type, and answer. Review the response code when interpreting missing answers.

**Speaker notes:** Use a resolver address different from the returned address. Ask learners to describe what each address does.

---

## Reference — Reading a DNS transaction

| Field | Meaning |
|---|---|
| `query` | The requested name. |
| `qtype_name` | The requested record type. |
| `answers` | Observed answer values, which may contain addresses or names. |
| `rcode_name` | Response code, where recorded, useful when interpreting an empty answer. |
| `id.orig_h` | The querying endpoint visible to the sensor. |
| `id.resp_h` | The DNS server contacted, often a recursive resolver. |
| `uid` | Connection identifier for related records; multiple DNS transactions may share it. |

**Speaker notes:** Use a resolver address different from the returned address. Ask learners to describe what each address does. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example

The client asks 192.0.2.53 for update.example and receives 203.0.113.88. A later connection needs separate evidence.

**Speaker notes:** Point out that the query type asks a question while the answer and response code describe the observed reply.

---

## Supplied example

The example records `192.0.2.10` asking resolver `192.0.2.53` for an A record for `update.example`, with `answers=["203.0.113.88"]` and `rcode_name=NOERROR`.

**Speaker notes:** Point out that the query type asks a question while the answer and response code describe the observed reply.

---

## Creating a focused DNS query

Query the name and record type. Adding AAAA broadens the question to IPv6 records for the same name.

**Speaker notes:** Have learners explain why adding AAAA broadens record types without broadening the requested domain.

---

## Reference — Creating a focused DNS query

| where TimeGenerated > ago(1d)
| where query =~ "update.example" and qtype_name == "A"
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],

**Speaker notes:** Have learners explain why adding AAAA broadens record types without broadening the requested domain. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused DNS query

```kusto
ZeekDns
| where TimeGenerated > ago(1d)
| where query =~ "update.example" and qtype_name == "A"
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],
          query, qtype_name, answers, rcode_name
```

**Speaker notes:** Have learners explain why adding AAAA broadens record types without broadening the requested domain. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. Where do you find the DNS server and the returned address?
2. Describe the example and explain whether it proves a connection to the answer.
3. Modify the query for both IPv4 and IPv6 questions for the same name.

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

A DNS description identifies the observed client, resolver, question, type, and response. It supplies a lead for subsequent activity rather than proving that the client contacted the returned address.

Previous: [1.2.2 – Conn Engine](../02-conn-engine/student-guide.md)

Next: [1.2.4 – TLS Engine](../04-tls-engine/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Zeek — dns.log](https://docs.zeek.org/en/current/reference/logs/dns.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
