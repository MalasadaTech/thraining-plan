# Module 2.4.6 – urlscan.io
## Slide Deck Content

**Total Suggested Slides:** 8

**Delivery:** Slides 1–2 support initial orientation. Complete the remaining material and knowledge check with 2.5.5; the combined delivery uses the stated lesson time.

### Slide 1 – Title
**urlscan.io**  
One browser scan, many useful artifacts

### Slide 2 – What the result can contain
- final URL
- title
- primary IP
- redirects
- requested hosts/IPs/URLs
- HTTP data
- certificates
- screenshot / DOM

Reference: [Result API](https://urlscan.io/docs/result/)

### Slide 3 – One scan = one observation
Time and environment matter.

Say:
**this scan observed...**

Not:
**this URL always...**

### Slide 4 – Requested hosts need classification
Could be:
- first party
- CDN
- analytics
- third party
- malicious infrastructure

Contact alone ≠ actor ownership.

### Slide 5 – Redirects matter
Submitted URL  
→ intermediate  
→ final URL

Useful for infrastructure analysis.

### Slide 6 – Submission safety
Search existing scans first.

Classroom: static result card.

Operational submission: follow policy and visibility rules.

Reference: [API docs](https://urlscan.io/docs/api/)

### Slide 7 – Knowledge Check
1. Why time-bound wording?  
2. Common analytics + rare A12 host: treat the same?  
3. Three useful result fields?

### Slide 8 – Summary
**Scan evidence → classify dependencies → enrich candidates**

**Next:** [2.5.1 – IOC Handling and Enrichment Concepts](../../05-enrichment/01-ioc-handling/student-guide.md).
