# Module 1.2.5 – HTTP Engine

- Interpret HTTP method, host, URI, User-Agent, response status, and endpoints.
- Describe the request and response without inventing content or execution.
- Create or modify a query for specific HTTP activity.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

An HTTP record helps explain what a client requested and what response status the sensor observed. Separating request details, server response, and any transferred content makes the resulting account more precise.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading HTTP fields

Read method, Host, URI, User-Agent, response status, endpoints, and transaction context.

**Speaker notes:** Explain why Host plus URI can still leave scheme or port uncertain. Emphasize that User-Agent is a claim made by the client.

---

## Reference — Reading HTTP fields

| Field | Meaning |
|---|---|
| `method` | Request method, such as GET, POST, PUT, or HEAD. |
| `host` | Recorded HTTP Host header; it is distinct from the destination IP. |
| `uri` | Requested URI, commonly a path and query. |
| `user_agent` | A client-supplied identification string, which can be changed or spoofed. |
| `status_code` | Observed response status. A 200 response does not establish benignness or execution. |
| Endpoint fields, `uid`, `trans_depth` | Connection context and the transaction's position within it. |

**Speaker notes:** Explain why Host plus URI can still leave scheme or port uncertain. Emphasize that User-Agent is a claim made by the client. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example — separate classroom record

**Not A12.**

GET /package.bin receives status 200. That establishes neither the returned file’s identity nor its execution.

**Speaker notes:** Ask what evidence would establish file contents and what would establish execution. Preserve the distinction between the two.

---

## Supplied example — separate classroom record

The supplied record shows `GET /package.bin` from `192.0.2.10` to `198.51.100.60:8080`, `status_code=200`, and no recorded Host or User-Agent.

**Speaker notes:** Ask what evidence would establish file contents and what would establish execution. Preserve the distinction between the two.

---

## Creating a focused HTTP query

Exact URI and path-plus-query matching return different results. Choose and explain the intended comparison.

**Speaker notes:** Compare exact path, path-plus-query, and a different path containing the same filename. Have learners explain their intended scope.

---

## Reference — Creating a focused HTTP query

| where TimeGenerated > ago(1d)
| where method == "GET" and uri == "/package.bin"
| where ['id.resp_h'] == "198.51.100.60" and ['id.resp_p'] == 8080
| project TimeGenerated, uid, ['id.orig_h'], host, uri,

**Speaker notes:** Compare exact path, path-plus-query, and a different path containing the same filename. Have learners explain their intended scope. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused HTTP query

```kusto
ZeekHttp
| where TimeGenerated > ago(1d)
| where method == "GET" and uri == "/package.bin"
| where ['id.resp_h'] == "198.51.100.60" and ['id.resp_p'] == 8080
| project TimeGenerated, uid, ['id.orig_h'], host, uri,
          user_agent, status_code
```

**Speaker notes:** Compare exact path, path-plus-query, and a different path containing the same filename. Have learners explain their intended scope. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. How do the Host header, destination IP, and URI differ?
2. What does the example establish, and does it prove package.bin ran?
3. Would uri == "/package.bin" match /package.bin?id=1? How could you broaden it?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

An HTTP finding connects the request, response status, and endpoints. Preserve missing headers and distinguish a requested path from transferred content or endpoint execution.

Previous: [1.2.4 – TLS Engine](../04-tls-engine/student-guide.md)

Next: [1.2.6 – SMTP Engine](../06-smtp-engine/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Zeek — http.log](https://docs.zeek.org/en/current/reference/logs/http.html)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
