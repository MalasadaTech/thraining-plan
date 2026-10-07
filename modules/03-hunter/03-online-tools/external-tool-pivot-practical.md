# External Tool Pivot Practical — VirusTotal, ANY.RUN, urlscan.io, and Silent Push

**Purpose:** demonstrate task `3.3.1.1` by actually querying and pivoting in the four named external platforms. Planning a query or interpreting a screenshot does not by itself demonstrate this task.

## Delivery model

This is an evaluator-led practical. The evaluator supplies one approved seed per platform at delivery time so the exercise does not depend on stale public results. The seed may be a hash, domain, IP, URL, or other object appropriate to the platform and the learner's access level.

Use an approved training account, free/public access where permitted, or another authorized account. Do not submit sensitive organizational artifacts to public services merely to complete the exercise.

For every platform, preserve:

1. seed value and timestamp;
2. query/search used;
3. at least one pivot performed;
4. result object or report identifier/URL when policy permits;
5. one hunt-relevant lead extracted from the result;
6. provenance wording that identifies the external source;
7. the internal telemetry/data source and field relationship you would use to test the lead locally.

## Station A — VirusTotal

Use the supplied seed to perform a search, inspect relevant relationships and/or behavior, pivot to a related object, and extract one lead that could be tested internally.

A valid result shows more than the seed lookup: the learner must use a relationship, behavior, or other supported pivot and explain why the resulting object is a candidate rather than proof of internal occurrence.

## Station B — ANY.RUN

Use the supplied seed in the available search/TI workflow, review the returned submission or TI context, pivot through at least one behavior or related observable, and extract a hunt lead. Preserve the relevant submission/report identifier when allowed.

## Station C — urlscan.io

Retrieve or search for the supplied URL/domain result, inspect request/redirect/infrastructure artifacts, pivot to one related object or result, and identify a lead that can be represented as local HTTP/DNS/TLS fields.

## Station D — Silent Push

Use the supplied seed to inspect passive-DNS or related infrastructure context, perform at least one infrastructure pivot, and record the time/hosting-density context needed before using the result as a hunt lead.

## Required final output

Create a four-row evidence table with one row per platform:

| Platform | Seed | Query/pivot | Extracted lead | Provenance statement | Internal test |
|---|---|---|---|---|---|

The internal test should name the local source, fields/relationship, and time/population. It does not have to prove the activity occurred; the purpose is to convert an external candidate into a precise local test.

## Evaluator criteria

A satisfactory demonstration requires the learner to actually use all four platforms and preserve enough evidence to reproduce the reasoning. The evaluator should confirm:

- the learner performed a real search/query and at least one pivot in each platform;
- the pivot selected is supported by what the platform actually shows;
- the learner does not turn an external relationship/verdict into proof of local activity;
- the extracted lead is internally queryable;
- provenance, time, and infrastructure-sharing context are preserved where relevant;
- the local test is precise enough to hand to a hunter/SIEM user.

At higher proficiency, expect better pivot selection, faster recognition of weak/common-infrastructure relationships, and adaptation when the first pivot is unproductive. Qualification/sign-off remains a separate evaluator action under the course standard.
