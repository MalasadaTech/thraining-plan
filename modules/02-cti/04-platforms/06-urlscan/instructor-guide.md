# Instructor Guide – Module 2.4.6 – urlscan.io

**Estimated Time:** 20–25 minutes

## Two-pass delivery

Spend about 5 minutes here on retrieval and evidence capture: the scan URL/time, visited page, and one request or redirect. Use a supplied static result if a live account or permitted query is unavailable. Reserve the remaining stated lesson time and the knowledge check for 2.5.5, alongside web-infrastructure relationships. Do not mark the platform task complete after orientation alone.

Use the first two slides for orientation; use the remaining slides and worked example during the paired method lesson. Reuse the same result in both passes.

## Purpose

Teach learners to interpret a browser-scan result as a time-bounded observation and extract useful web infrastructure without promoting every third-party dependency into adversary infrastructure.

## Current Capability Note

urlscan results can include page metadata, requested domains/IPs/URLs, redirects, request/response details, certificates, screenshots, DOM snapshots, and service verdicts.

References:
- [API Documentation](https://urlscan.io/docs/api/)
- [Result API Reference](https://urlscan.io/docs/result/)

## Key Teaching Points

### One scan is not timeless truth
State:
> this scan observed...

Avoid:
> this URL always...

### Classify requested hosts
Common CDN, analytics, fonts, or advertising infrastructure may be incidental.

### Submission visibility matters
The lesson uses static cards. Operational live submission should follow local policy, especially for internal or sensitive URLs.

### Machine-readable evidence matters
Redirect chains and requested hosts often provide stronger infrastructure pivots than screenshots alone.

## Practice-Card Boundary

The static urlscan result is **separate classroom evidence, not A12**. Its redirect, title, hosts, and IP exist only for the exercise and must not be promoted into the recurring case.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Treats every contacted domain as adversary infrastructure. | Identify third-party dependencies and assess distinctiveness. |
| Treats screenshot as the whole result. | Examine redirects, requests, IPs, certs, and page metadata. |
| Treats one scan as permanent site behavior. | Tie the claim to scan time/environment. |
| Submits sensitive URL casually. | Use classroom cards; operational submission follows organizational policy/visibility settings. |

## Knowledge Check – Answer Key

1. Web content and routing can change by time/environment; the result describes one scan.
2. No. Common analytics is likely third-party infrastructure; the rare host from the supplied classroom card is a candidate that merits enrichment.
3. Examples: final URL, title, redirect status/chain, requested domains/IPs/URLs, primary IP, certificate data, screenshot, DOM, HTTP responses.

## References

- [urlscan.io API Documentation](https://urlscan.io/docs/api/)
- [urlscan.io Result API](https://urlscan.io/docs/result/)
- [urlscan.io Quickstart](https://docs.urlscan.io/guides/quickstart)
