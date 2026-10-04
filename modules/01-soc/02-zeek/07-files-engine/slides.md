# Module 1.2.7 – Files Engine

- Interpret file names, MIME types, hashes, direction, and connection identifiers.
- Describe observed file content without assuming endpoint creation.
- Create or modify a query using the file-log schema actually available.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

Zeek file analysis connects observed network content to the flow that carried it. It can help explain a download or attachment, while the available fields also show whether hashes or extracted bytes exist for further examination.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading file-analysis records

Distinguish file FUID, connection UID, hash, and extracted object. Current and legacy direction fields differ.

**Speaker notes:** Compare the two schema representations rather than teaching old fields as universal. Keep file identity, connection identity, hash, and extracted object distinct.

---

## Reference — Reading file-analysis records

| Field or representation | What it contributes |
|---|---|
| `fuid` | File-analysis identifier; this is different from a connection UID. |
| `filename`, `mime_type` | A supplied filename when available and an assessment of content type. These may disagree. |
| `md5`, `sha1`, `sha256` | Hashes when the relevant analysis is enabled and values are available. |
| Current `uid`, endpoint fields, `is_orig` | Connection context; `is_orig=false` indicates the responder supplied the content, and true indicates the originator. |
| Legacy `tx_hosts`, `rx_hosts`, `conn_uids` | Sender/receiver sets and connection identifiers in older or compatibility-enabled schemas. Check which representation your feed uses. |
| Completeness and extraction fields | Observed/missing byte information and extraction details help assess what was actually available. |

**Speaker notes:** Compare the two schema representations rather than teaching old fields as universal. Keep file identity, connection identity, hash, and extracted object distinct. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example

With is_orig=false, the responder supplies the content. A network observation does not establish a host Temp path.

**Speaker notes:** Ask learners to determine sender from is_orig and explain the missing endpoint-path claim. Use the related HTTP record only for what it actually adds.

---

## Supplied example

Suppose a record identifies executable-type content with `mime_type=application/x-dosexec`, `fuid=FTrain1`, `uid=CTrain1`, originator `192.0.2.10`, responder `203.0.113.88`, and `is_orig=false`. A related HTTP record associates it with `/update.exe`.

**Speaker notes:** Ask learners to determine sender from is_orig and explain the missing endpoint-path claim. Use the related HTTP record only for what it actually adds.

---

## Creating a focused file-analysis query

Query content type and supported sender/direction fields. Preserve completeness and extraction limitations.

**Speaker notes:** Confirm that learners change both direction and the sender-address field. Do not require nonexistent legacy columns in a current feed.

---

## Reference — Creating a focused file-analysis query

| where TimeGenerated > ago(1d)
| where mime_type == "application/x-dosexec"
| where ['id.resp_h'] == "203.0.113.88" and is_orig == false
| project TimeGenerated, fuid, uid, ['id.orig_h'], ['id.resp_h'],

**Speaker notes:** Confirm that learners change both direction and the sender-address field. Do not require nonexistent legacy columns in a current feed. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused file-analysis query

```kusto
ZeekFiles
| where TimeGenerated > ago(1d)
| where mime_type == "application/x-dosexec"
| where ['id.resp_h'] == "203.0.113.88" and is_orig == false
| project TimeGenerated, fuid, uid, ['id.orig_h'], ['id.resp_h'],
          mime_type, is_orig
```

**Speaker notes:** Confirm that learners change both direction and the sender-address field. Do not require nonexistent legacy columns in a current feed. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. How do fuid and uid differ?
2. Who supplied the content when is_orig=false in the example, and does it establish a Temp file on the host?
3. Modify the query for files supplied by the originator and identify the legacy equivalent.

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

File-analysis records describe observed network content and its connection context. Check the schema, direction, completeness, and available hashes or extracted bytes before choosing the next pivot.

Previous: [1.2.6 – SMTP Engine](../06-smtp-engine/student-guide.md)

Next: [1.2.8 – Weird Engine](../08-weird-engine/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Zeek — files.log](https://docs.zeek.org/en/current/reference/logs/files.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
