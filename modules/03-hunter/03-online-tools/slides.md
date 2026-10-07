# Module 3.3.1 – Tool Capabilities for Hunting  
## Slide Deck Content

**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 11

---

### Slide 1 – Title
**Title:** 3.3.1 – Tool Capabilities for Hunting  
**Subtitle:** Mentor-style, evidence-bound hunting tradecraft

---

### Slide 2 – External tools create candidates
Internal telemetry answers whether the activity occurred here.

---

### Slide 3 – VirusTotal
Relationships + sandbox behavior. External evidence, not internal proof.

---

### Slide 4 – ANY.RUN
IOC and event-field search across sandbox sessions.

---

### Slide 5 – Silent Push
Historical PADNS relationships; time and hosting density matter.

---

### Slide 6 – urlscan.io
Redirect/request/page artifacts from one browser scan.

---

### Slide 7 – Convert to internal test
Data source + fields + values + window/population + review context.

---

### Slide 8 – A12 predicate
resp_h 203.0.113.88 | resp_p 8080 | uri /update.exe | scoped time/population.

---

### Slide 9 – Actual platform use is separate evidence
`3.3.1.1` requires real search + pivot in:
- VirusTotal
- ANY.RUN
- urlscan.io
- Silent Push

Preserve seed, query, pivot, provenance, lead, and local test.

---

### Slide 10 – Knowledge Check
External vs internal evidence? Query-plan fields? A12 conversion?

---

### Slide 11 – Summary
Pivot externally; prove or disprove internally.


**References:** [VirusTotal Relationships](https://docs.virustotal.com/reference/relationships) | [VirusTotal File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours) | [ANY.RUN TI Lookup Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf) | [Silent Push DNS Data](https://help.silentpush.com/docs/dns-data) | [urlscan Result API](https://urlscan.io/docs/result/)
