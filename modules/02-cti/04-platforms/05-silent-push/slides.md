# Module 2.4.5 – Silent Push
## Slide Deck Content

**Total Suggested Slides:** 8

**Delivery:** Slides 1–2 support initial orientation. Complete the remaining material and knowledge check with 2.5.4; the combined delivery uses the stated lesson time.

### Slide 1 – Title
**Silent Push**  
Historical DNS as infrastructure evidence

### Slide 2 – What PADNS answers
- domain → observed IPs/records
- IP → observed domains
- NS/MX/CNAME/etc. relationships
- change over time

Reference: [Silent Push DNS Data](https://help.silentpush.com/docs/dns-data)

### Slide 3 – PADNS vs authoritative DNS
**Authoritative:** zone publishes now  
**PADNS:** provider observed over time

### Slide 4 – Time matters
Same IP + same period → stronger

Same IP years apart → weaker

### Slide 5 – Density matters
Dedicated/rare infrastructure → stronger candidate

Shared cloud/CDN → weaker candidate

### Slide 6 – A12
Update domain + `login-prd.net`  
same `203.0.113.88`  
overlapping period

→ candidate relationship

### Slide 7 – Knowledge Check
1. PADNS vs authoritative?  
2. Why overlap matters?  
3. Same-IP result: strongest first conclusion?

### Slide 8 – Summary
**Historical relationship + time + density + corroboration**


Reference: [PADNS Lookups](https://help.silentpush.com/v1/docs/perform-passive-dns-scans-and-record-specific-lookups)

**Next:** [2.4.6 – urlscan.io](../06-urlscan/student-guide.md).
