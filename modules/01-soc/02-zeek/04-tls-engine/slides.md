# Module 1.2.4 – TLS Engine

- Interpret SNI, certificate information, optional fingerprints, version, cipher, and endpoints.
- Describe TLS activity using the observed establishment state.
- Create or modify a query for specific TLS activity.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

TLS can conceal application content while leaving some handshake information visible. Reading that information carefully helps describe the observed session without treating a hostname, certificate, or fingerprint as a verdict.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading TLS evidence

Read visible SNI, certificate information, optional fingerprints, version, cipher, and establishment state.

**Speaker notes:** Distinguish client-indicated name, certificate identity, and fingerprint. Explain why unavailable fields can reflect encryption or collection.

---

## Reference — Reading TLS evidence

| Field or feature | Interpretation |
|---|---|
| `server_name` | Observed Server Name Indication (SNI), when visible. It is distinct from a certificate subject. |
| `subject`, `issuer` | Certificate identity fields where available; detailed certificate records may be linked through `x509.log`. |
| `version`, `cipher` | Observed TLS negotiation details. |
| `established` | Zeek's indication that the TLS session was successfully established. Version and cipher alone should not substitute for that assessment. |
| JA3 / JA3S | Optional client/server fingerprints when the deployment collects them. A shared fingerprint does not uniquely identify malware. |
| Endpoint fields and `uid` | Identify the observed connection and related records. |

**Speaker notes:** Distinguish client-indicated name, certificate identity, and fingerprint. Explain why unavailable fields can reflect encryption or collection. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example

Established=true supports the example’s session-state claim. Missing SNI leaves the requested name unavailable.

**Speaker notes:** Compare the example with the established field removed. Ask learners to revise their sentence accordingly.

---

## Supplied example

A record shows `192.0.2.10` communicating with `203.0.113.88:443`, a recorded TLS version and cipher, `established=true`, and no `server_name`.

**Speaker notes:** Compare the example with the established field removed. Ask learners to revise their sentence accordingly.

---

## Creating a focused TLS query

A hostname query only matches records with that visible, populated field. Preserve the visibility limit.

**Speaker notes:** Explain that a populated-field search has a visibility prerequisite. A blank field cannot be filled by choosing a more complex query.

---

## Reference — Creating a focused TLS query

| where TimeGenerated > ago(1d)
| where ['id.resp_h'] == "203.0.113.88" and ['id.resp_p'] == 443
| where established == true
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],

**Speaker notes:** Explain that a populated-field search has a visibility prerequisite. A blank field cannot be filled by choosing a more complex query. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused TLS query

```kusto
ZeekTls
| where TimeGenerated > ago(1d)
| where ['id.resp_h'] == "203.0.113.88" and ['id.resp_p'] == 443
| where established == true
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],
          server_name, version, cipher, established
```

**Speaker notes:** Explain that a populated-field search has a visibility prerequisite. A blank field cannot be filled by choosing a more complex query. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. How does SNI differ from the certificate subject?
2. What supports calling the example an established TLS session?
3. Modify the query to search for visible SNI update.example and explain a blind spot.

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

TLS records describe the visible handshake and session state. State which names, certificate details, and fingerprints are available, and keep encrypted application behavior separate from those observations.

Previous: [1.2.3 – DNS Engine](../03-dns-engine/student-guide.md)

Next: [1.2.5 – HTTP Engine](../05-http-engine/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Zeek — ssl.log](https://docs.zeek.org/en/current/reference/logs/ssl.html)
- [Zeek — x509.log](https://docs.zeek.org/en/current/reference/logs/x509.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
