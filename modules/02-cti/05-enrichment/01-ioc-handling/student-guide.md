# Module 2.5.1 – IOC Handling and Enrichment Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter and SOC Analyst (supporting context)  
**Proficiency Focus:**  
- CTI: 2.5.1 B / C / C ; 2.5.1.1 3c / 4c / 4d  
- Hunter: 2.5.1 B / C / C ; 2.5.1.1 3c / 4c / 4d  
- SOC: 2.5.1 A / B / B ; 2.5.1.1 1a / 2b / 3c  
**Estimated Time:** 15–20 minutes

## Learning Objectives

1. Distinguish an observable from an operational IOC and choose retain, enrich, review/expire, or reject.
2. Record a question-driven enrichment lookup with provenance and label any resulting pivot as a candidate.

**Mapped Proficiency Items:**
- K: 2.5.1 – IOC handling and enrichment concepts
- T: 2.5.1.1 – Enrich and pivot on IOCs using internal and external tools

## 1. Key Concepts

Analysts work with technical values such as hashes, domains, IP addresses, URLs, filenames, and certificates.

Those values are **observables**: technical facts that can be recorded and related to higher-level intelligence.

An observable becomes operationally useful as an **indicator / IOC** when the analyst has enough context to associate it with suspicious or malicious activity and use it for detection, investigation, enrichment, or tracking.

The distinction matters because **not every observable is malicious**.

The STIX 2.1 standard makes a similar distinction:
- Cyber-observable Objects represent observed technical facts.
- An Indicator contains a detection pattern intended to identify suspicious or malicious activity.

Reference: [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### IOC is a practical course term

Operational teams often use **IOC** broadly for malicious or suspicious technical indicators such as hashes, domains, IPs, and URLs.

This course uses that familiar term, but keeps the evidence boundary visible:

> `203.0.113.88` is an observable value.

It becomes a useful IOC when the case/reporting connects that address to the activity strongly enough for an operational purpose.

### Four lifecycle decisions

| Decision | Meaning |
|---|---|
| **Retain / keep** | Evidence and provenance support continuing to use the indicator. |
| **Enrich** | Gather context that may change confidence, scope, relationships, or utility. |
| **Review / expire** | A previously valid indicator has aged, changed ownership, lost relevance, or reached the end of its useful validity. |
| **Reject / do not promote** | The candidate never had enough specificity or malicious context to become a useful IOC. |

This makes an important distinction:

A shared cloud `/24` containing one malicious address is usually **too broad to promote as an IOC**.

That is different from expiring a domain that was previously a strong indicator but is no longer useful.

STIX Indicators explicitly support `valid_from` and optional `valid_until`, reinforcing the idea that indicator utility can have a time window. See the [STIX 2.1 specification](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html), which defines Indicator validity with `valid_from` and optional `valid_until`.

### Preserve provenance

For each retained indicator, keep enough context to answer:

- What is the value and type?
- What source connected it to malicious/suspicious activity?
- When was it observed or reported?
- What case, report, malware, or activity does it relate to?
- How confident are we in that relationship?
- Is the indicator still useful?

A raw value without provenance is easy to misuse later.

### Enrichment should answer a question

A useful enrichment record states:

`object | source/tool | field or relationship sought | result | analytic meaning`

Example:

> `invoice.vbs SHA256 | internal TIP | prior sightings / linked reports | none found | no prior TIP context`

Then, if needed:

> `invoice.vbs SHA256 | public malware repository | detections / metadata | ... | adds external context`

The purpose is not to touch every tool. It is to retrieve information that could change the analysis.

### A first enrichment record

Start with a value already in the case. State what you need to learn, select the source, and retain the result with its provenance. If a lookup reveals another object, record it as a candidate and explain the relationship; the later method lessons teach how to test that lead.

For A12, a TIP lookup with no matching hash means **no matching TIP result was returned**. It does not establish that the file is benign or absent from the environment. An external lookup should answer a defined remaining question and comply with the site's handling rules.

Preserve this enrichment record through the following lessons. Use [2.5.7 – Correlation and Link Analysis](../07-correlation/student-guide.md) to combine the resulting evidence into a supported activity-set or campaign assessment.

## 2. Knowledge Check

1. Why is a raw IP address not automatically an IOC?
2. One bad IP sits inside a busy cloud /24. Should you promote the whole range, expire it, or reject it as too broad?
3. A TIP lookup returns no matching hash. Write the result and identify what should guide the next lookup.

## 3. Summary

Keep provenance, manage validity, and enrich to answer a question. Preserve candidate relationships for testing in the following method lessons.

## Supporting References

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

**Next:** [2.5.2 – Hashing and Similarity Concepts](../02-file-similarity/student-guide.md).
