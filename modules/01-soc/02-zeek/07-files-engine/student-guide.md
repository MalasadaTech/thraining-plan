# Module 1.2.7 – Files Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.7.1 A / B / C ; 1.2.7.2 2b / 3c / 4c ; 1.2.7.3 2b / 3c / 4c  
- Hunter: 1.2.7.1 B / C / C ; 1.2.7.2 3c / 4c / 4c ; 1.2.7.3 3c / 4c / 4c  
- CTI: 1.2.7.1 A / A / B ; 1.2.7.2 1a / 1a / 2b ; 1.2.7.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret file names, MIME types, hashes, direction, and connection identifiers.
2. Describe observed file content without assuming endpoint creation.
3. Create or modify a query using the file-log schema actually available.

**Mapped Proficiency Items:**
- K: 1.2.7.1 – Files engine
- T: 1.2.7.2 – Analyze a Zeek files log and accurately describe what occurred
- T: 1.2.7.3 – Create a SIEM query to detect specific file transfer activity

## Why This Matters

Zeek file analysis connects observed network content to the flow that carried it. It can help explain a download or attachment, while the available fields also show whether hashes or extracted bytes exist for further examination.

## 1. Reading file-analysis records

| Field or representation | What it contributes |
|---|---|
| `fuid` | File-analysis identifier; this is different from a connection UID. |
| `filename`, `mime_type` | A supplied filename when available and an assessment of content type. These may disagree. |
| `md5`, `sha1`, `sha256` | Hashes when the relevant analysis is enabled and values are available. |
| Current `uid`, endpoint fields, `is_orig` | Connection context; `is_orig=false` indicates the responder supplied the content, and true indicates the originator. |
| Legacy `tx_hosts`, `rx_hosts`, `conn_uids` | Sender/receiver sets and connection identifiers in older or compatibility-enabled schemas. Check which representation your feed uses. |
| Completeness and extraction fields | Observed/missing byte information and extraction details help assess what was actually available. |

A `files.log` record does not guarantee that Zeek saved a file to disk or captured its complete content. Extraction and hashing are configuration-dependent. A network file observation also does not establish an endpoint filesystem path.

## 2. Working through the example

**Separate classroom file-analysis record — not A12.** It intentionally pairs with the separate HTTP training record from 1.2.5.

Suppose a record identifies executable-type content with `mime_type=application/x-dosexec`, `fuid=FTrain1`, `uid=CTrain1`, originator `192.0.2.10`, responder `198.51.100.60`, and `is_orig=false`. A related HTTP record associates it with `/package.bin`.

The supported account is that Zeek observed executable-type content supplied by the responder to the originator in that HTTP context. Use `CTrain1` for the connection and `FTrain1` for file references such as an HTTP `resp_fuids` entry. In a legacy record, `tx_hosts` and `rx_hosts` supply direction and `conn_uids` supplies the connection pivot. State separately whether a hash, complete bytes, or an extracted object is available.

## 3. Creating a focused file-analysis query

This KQL teaching example assumes an ingested table named `ZeekFiles`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekFiles
| where TimeGenerated > ago(1d)
| where mime_type == "application/x-dosexec"
| where ['id.resp_h'] == "198.51.100.60" and is_orig == false
| project TimeGenerated, fuid, uid, ['id.orig_h'], ['id.resp_h'],
          mime_type, is_orig
```

This example uses the current endpoint/direction representation and selects executable-type content sent by the specified responder. A legacy feed needs equivalent membership tests against `tx_hosts` and suitable `conn_uids` output. Searching hashes requires a populated hash column; the file-analysis identifier is not a substitute for a hash.

## Knowledge Check

1. How do fuid and uid differ?
2. Who supplied the content when is_orig=false in the example, and does it establish a Temp file on the host?
3. Modify the query for files supplied by the originator and identify the legacy equivalent.

## Summary

File-analysis records describe observed network content and its connection context. Check the schema, direction, completeness, and available hashes or extracted bytes before choosing the next pivot.

## Course Connections

Previous: [1.2.6 – SMTP Engine](../06-smtp-engine/student-guide.md)

Next: [1.2.8 – Weird Engine](../08-weird-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — files.log](https://docs.zeek.org/en/current/reference/logs/files.html)
