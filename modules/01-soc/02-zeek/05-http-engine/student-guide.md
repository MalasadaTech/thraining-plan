# Module 1.2.5 – HTTP Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.5.1 A / B / C ; 1.2.5.2 2b / 3c / 4c ; 1.2.5.3 2b / 3c / 4c  
- Hunter: 1.2.5.1 B / C / C ; 1.2.5.2 3c / 4c / 4c ; 1.2.5.3 3c / 4c / 4c  
- CTI: 1.2.5.1 A / B / B ; 1.2.5.2 1a / 2b / 3c ; 1.2.5.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret HTTP method, host, URI, User-Agent, response status, and endpoints.
2. Describe the request and response without inventing content or execution.
3. Create or modify a query for specific HTTP activity.

**Mapped Proficiency Items:**
- K: 1.2.5.1 – HTTP engine
- T: 1.2.5.2 – Analyze a Zeek HTTP log and accurately describe what occurred
- T: 1.2.5.3 – Create a SIEM query to detect specific HTTP activity

## Why This Matters

An HTTP record helps explain what a client requested and what response status the sensor observed. Separating request details, server response, and any transferred content makes the resulting account more precise.

## 1. Reading HTTP fields

| Field | Meaning |
|---|---|
| `method` | Request method, such as GET, POST, PUT, or HEAD. |
| `host` | Recorded HTTP Host header; it is distinct from the destination IP. |
| `uri` | Requested URI, commonly a path and query. |
| `user_agent` | A client-supplied identification string, which can be changed or spoofed. |
| `status_code` | Observed response status. A 200 response does not establish benignness or execution. |
| Endpoint fields, `uid`, `trans_depth` | Connection context and the transaction's position within it. |

Host and URI help reconstruct the requested resource, but a complete URL also needs a supported scheme and any relevant port. Preserve missing components explicitly. Zeek needs visibility into HTTP content to parse it; encrypted HTTPS normally requires appropriate decryption visibility for comparable HTTP fields. The log does not supply the full body by default.

## 2. Working through the example

**Separate classroom HTTP record — not A12.** These values exist only to teach field interpretation and query scope.

The supplied record shows `GET /package.bin` from `192.0.2.10` to `198.51.100.60:8080`, `status_code=200`, and no recorded Host or User-Agent.

A supported description is: “The client requested `/package.bin` with GET from the supplied destination on port 8080 and received HTTP status 200; Host and User-Agent are unavailable in this record.” The path name does not establish the returned bytes. File-analysis records or retained content may help determine what was transferred, while endpoint evidence can address whether a file was saved or executed.

## 3. Creating a focused HTTP query

This KQL teaching example assumes an ingested table named `ZeekHttp`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekHttp
| where TimeGenerated > ago(1d)
| where method == "GET" and uri == "/package.bin"
| where ['id.resp_h'] == "198.51.100.60" and ['id.resp_p'] == 8080
| project TimeGenerated, uid, ['id.orig_h'], host, uri,
          user_agent, status_code
```

The equality test matches exactly `/package.bin`; it will not include a URI with an added query string. A substring or carefully scoped path expression changes that behavior. Choose the comparison that answers the stated question and explain the extra results it permits.

## Knowledge Check

1. How do the Host header, destination IP, and URI differ?
2. What does the example establish, and does it prove package.bin ran?
3. Would uri == "/package.bin" match /package.bin?id=1? How could you broaden it?

## Summary

An HTTP finding connects the request, response status, and endpoints. Preserve missing headers and distinguish a requested path from transferred content or endpoint execution.

## Course Connections

Previous: [1.2.4 – TLS Engine](../04-tls-engine/student-guide.md)

Next: [1.2.6 – SMTP Engine](../06-smtp-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — http.log](https://docs.zeek.org/en/current/reference/logs/http.html)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
