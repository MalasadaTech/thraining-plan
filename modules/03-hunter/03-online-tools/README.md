# Tool Capabilities for Hunting

**Path:** `modules/03-hunter/03-online-tools`  
**Primary role:** Threat Hunter  
**Secondary:** SOC Analyst, CTI Analyst  
**Time:** about 20–25 minutes

## Proficiency focus

- Hunter: 3.3.1 B / C / C ; 3.3.1.1–3.3.1.3 3c / 4c / 4d  
- SOC: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.3 1a / 2b / 3c  
- CTI: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 2b / 3c / 4c ; 3.3.1.3 1a / 2b / 3c

## Mapped proficiency items

- K: 3.3.1 – Tool capabilities for hunting
- T: 3.3.1.1 – Perform advanced querying and pivoting in VirusTotal, ANY.RUN, urlscan.io, and Silent Push
- T: 3.3.1.2 – Extract actionable hunting leads from external tool results
- T: 3.3.1.3 – Convert external findings into precise internal SIEM or Zeek queries

## Concepts taught

- external-tool pivots
- hunt leads
- internal query conversion
- VirusTotal
- ANY.RUN
- urlscan.io
- Silent Push
- external evidence limitations
- distinction between platform-use preparation and demonstrated querying/pivoting

## Artifacts

- [student-guide.md](student-guide.md)
- [instructor-guide.md](instructor-guide.md)
- [slides.md](slides.md)
- [external-tool-pivot-practical.md](external-tool-pivot-practical.md) — evaluator-led platform demonstration for `3.3.1.1`
- `assets/` — unchanged

## Supporting references

- [VirusTotal Relationships](https://docs.virustotal.com/reference/relationships)
- [VirusTotal File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours)
- [ANY.RUN TI Lookup Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf)
- [Silent Push DNS Data](https://help.silentpush.com/docs/dns-data)
- [urlscan Result API](https://urlscan.io/docs/result/)

## Revision status

Aligned to the explanatory mentor voice used across the revised CTI track. The module preserves evidence boundaries, distinguishes visibility from detection coverage, and avoids treating course examples or local-process placeholders as facts that have not been established.
