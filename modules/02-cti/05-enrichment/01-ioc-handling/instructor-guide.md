# Instructor Guide – Module 2.5.1 – IOC Handling and Enrichment Concepts

**Estimated Time:** 15–20 minutes

## Purpose

1. Distinguish an observable from an operational IOC and choose retain, enrich, review/expire, or reject.
2. Record a question-driven enrichment lookup with provenance and label any resulting pivot as a candidate.

## Teaching Sequence

1. Introduce the observable/indicator distinction with one existing A12 value.
2. Compare retain, enrich, review/expire, and reject. Preserve the distinction between an indicator that aged out and a broad value that never warranted promotion.
3. Have learners write one enrichment record: object, source/tool, field sought, result, and meaning. Retain provenance and observation/query time.
4. Carry that record into 2.5.2–2.5.6. Assess the complete enrichment/pivot performance item using those applications; this first lesson establishes the record and the decision discipline.
5. Defer combining multiple links into a campaign hypothesis until 2.5.7.

## Knowledge Check – Answer Key

1. It is a technical observable; suspicious or malicious context and an operational purpose are needed to treat it as an IOC.
2. Reject/do not promote the whole range. Expiration applies to an indicator that was previously useful.
3. Record no matching TIP result, with source and query time. Choose the next source based on the remaining question and handling restrictions, not an assumption that the file is benign.

## Supporting References

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
