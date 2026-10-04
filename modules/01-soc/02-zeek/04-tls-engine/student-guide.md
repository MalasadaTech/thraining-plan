# Module 1.2.4 – TLS Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.4.1 A / B / C ; 1.2.4.2 2b / 3c / 4c ; 1.2.4.3 2b / 3c / 4c  
- Hunter: 1.2.4.1 B / C / C ; 1.2.4.2 3c / 4c / 4c ; 1.2.4.3 3c / 4c / 4c  
- CTI: 1.2.4.1 A / A / B ; 1.2.4.2 1a / 1a / 2b ; 1.2.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret SNI, certificate information, optional fingerprints, version, cipher, and endpoints.
2. Describe TLS activity using the observed establishment state.
3. Create or modify a query for specific TLS activity.

**Mapped Proficiency Items:**
- K: 1.2.4.1 – TLS engine
- T: 1.2.4.2 – Analyze a Zeek TLS log and accurately describe what occurred
- T: 1.2.4.3 – Create a SIEM query to detect specific TLS activity

## Why This Matters

TLS can conceal application content while leaving some handshake information visible. Reading that information carefully helps describe the observed session without treating a hostname, certificate, or fingerprint as a verdict.

## 1. Reading TLS evidence

Zeek records TLS information in `ssl.log`; the name is historical.

| Field or feature | Interpretation |
|---|---|
| `server_name` | Observed Server Name Indication (SNI), when visible. It is distinct from a certificate subject. |
| `subject`, `issuer` | Certificate identity fields where available; detailed certificate records may be linked through `x509.log`. |
| `version`, `cipher` | Observed TLS negotiation details. |
| `established` | Zeek's indication that the TLS session was successfully established. Version and cipher alone should not substitute for that assessment. |
| JA3 / JA3S | Optional client/server fingerprints when the deployment collects them. A shared fingerprint does not uniquely identify malware. |
| Endpoint fields and `uid` | Identify the observed connection and related records. |

Encryption, TLS version, encrypted Client Hello, capture quality, and configuration affect visibility. A blank SNI or certificate field does not establish that no name or certificate existed. TLS 1.3 can conceal certificate details from a passive sensor.

## 2. Working through the example

A record shows `192.0.2.10` communicating with `203.0.113.88:443`, a recorded TLS version and cipher, `established=true`, and no `server_name`.

Describe it as: “Zeek reports an established TLS session between the supplied endpoints with the recorded version and cipher; SNI is unavailable in this record.” If `established` were absent, limit the conclusion to the observed handshake details. Even an established session does not reveal the encrypted HTTP path or prove the application's purpose.

## 3. Creating a focused TLS query

This KQL teaching example assumes an ingested table named `ZeekTls`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekTls
| where TimeGenerated > ago(1d)
| where ['id.resp_h'] == "203.0.113.88" and ['id.resp_p'] == 443
| where established == true
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],
          server_name, version, cipher, established
```

This searches for established TLS sessions to the example endpoint. To ask about a hostname instead, use `server_name =~ "update.example"`; that query only finds records where the name is visible and populated.

## Knowledge Check

1. How does SNI differ from the certificate subject?
2. What supports calling the example an established TLS session?
3. Modify the query to search for visible SNI update.example and explain a blind spot.

## Summary

TLS records describe the visible handshake and session state. State which names, certificate details, and fingerprints are available, and keep encrypted application behavior separate from those observations.

## Course Connections

Previous: [1.2.3 – DNS Engine](../03-dns-engine/student-guide.md)

Next: [1.2.5 – HTTP Engine](../05-http-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — ssl.log](https://docs.zeek.org/en/current/reference/logs/ssl.html)
- [Zeek — x509.log](https://docs.zeek.org/en/current/reference/logs/x509.html)
