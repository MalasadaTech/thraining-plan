# Module 3.3.1 – Tool Capabilities for Hunting

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.3.1 B / C / C ; 3.3.1.1–3.3.1.3 3c / 4c / 4d  
- SOC: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.3 1a / 2b / 3c  
- CTI: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 2b / 3c / 4c ; 3.3.1.3 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Use VirusTotal, ANY.RUN, urlscan.io, and Silent Push outputs to identify hunt-relevant pivots.
2. Convert an external finding into a precise **internal query plan** that names the local data source, fields, value, and time window.

## Mapped Proficiency Items

- K: 3.3.1 – Tool capabilities for hunting
- T: 3.3.1.1 – Perform advanced querying and pivoting in VirusTotal, ANY.RUN, urlscan.io, and Silent Push
- T: 3.3.1.2 – Extract actionable hunting leads from external tool results
- T: 3.3.1.3 – Convert external findings into precise internal SIEM or Zeek queries

## 1. Key Concepts

External tools provide **context and candidates**. Internal telemetry tells you whether the activity occurred in your environment.

| Tool | Hunt-relevant strength | Important limit |
|---|---|---|
| **VirusTotal** | Object relationships and sandbox behavior can expose related files, domains, IPs, processes, files, registry, and network events. | A relationship or sandbox event is external evidence, not proof it occurred internally. |
| **ANY.RUN** | TI Lookup can search IOCs and sandbox event fields such as processes, registry activity, commands, mutexes, and network events. | A threat label or one sandbox session is not the internal hunt result. |
| **urlscan.io** | A scan can expose redirects, requested domains/IPs/URLs, page metadata, certificates, and HTTP artifacts. | One browser scan is time/environment specific and may include unrelated third-party services. |
| **Silent Push** | Passive DNS can expose historical domain/IP and other DNS relationships. | Provider-observed PADNS associations require time and hosting-density context. |

### Supporting documentation

- [VirusTotal Relationships](https://docs.virustotal.com/reference/relationships)
- [VirusTotal File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours)
- [ANY.RUN TI Lookup Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf)
- [Silent Push DNS Data](https://help.silentpush.com/docs/dns-data)
- [urlscan Result API](https://urlscan.io/docs/result/)

### What makes a good hunt lead?

A hunt lead should be **internally queryable** and retain enough context to avoid becoming a blind IOC search.

Examples:

- destination `203.0.113.88`, TCP port `8080`, URI `/update.exe`;
- registry value `Updater` under a Run key, pointing to a user-writable path;
- a dropped filename plus parent process or hash;
- a rare domain paired with an observed time window.

A detection count, verdict label, or screenshot can provide context but is not itself the internal search.

### Convert the finding into an internal query plan

Write:

1. **Local data source** – e.g., Zeek `http.log`, EDR process events, registry telemetry.
2. **Fields** – the fields that express the lead.
3. **Values/relationship** – the exact artifact or behavior.
4. **Time window / population** – where and when to search.
5. **Expected review context** – what would make a hit interesting or benign.

Example:

> **Data source:** Zeek HTTP telemetry  
> **Predicate:** `id.resp_h = 203.0.113.88`, `id.resp_p = 8080/tcp`, `uri = /update.exe`  
> **Window:** A12 window ± 14 days across user-workstation traffic  
> **Review:** identify originating hosts, repeated requests, response metadata, and associated file/process evidence.

Those are **field constraints**, not a claim that Zeek itself has a universal query language. The exact SIEM syntax depends on where your Zeek data is stored.

### Preserve external-source provenance

Phrase the lead as:

> VirusTotal behavior report observed...

or:

> Silent Push PADNS associated...

Then ask whether internal telemetry contains the same or related activity.

### Platform use must be demonstrated separately

This lesson teaches what the four platforms can contribute and how to turn their results into internal hunt leads. That preparation does **not** by itself satisfy `3.3.1.1`, whose approved verb is **perform**.

Use the [External Tool Pivot Practical](external-tool-pivot-practical.md) to demonstrate actual searching and pivoting in VirusTotal, ANY.RUN, urlscan.io, and Silent Push. The practical requires preserved provenance and a local test derived from each platform result.

## 2. Knowledge Check

1. Why is a VirusTotal relationship useful but not proof of internal activity?
2. What four or five elements make an external finding into a good internal query plan?
3. Convert `203.0.113.88:8080` + `/update.exe` into a Zeek/SIEM field predicate and scope.

## 3. Summary

External tools generate context and candidates. Hunting converts them into precise internal tests.

Carry forward the artifact **and** its context, then search the local telemetry that can actually answer the question.

**Next:** [3.4 – CTI as Hunt Input Preview](../04-cti-for-hunters/intro.md).
