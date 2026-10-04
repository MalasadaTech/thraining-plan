# Instructor Guide – Module 3.3.1 – Tool Capabilities for Hunting

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.3.1 B / C / C ; 3.3.1.1–3.3.1.3 3c / 4c / 4d  
- SOC: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.3 1a / 2b / 3c  
- CTI: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 2b / 3c / 4c ; 3.3.1.3 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Purpose

Use this lesson to teach the reasoning skill in the student guide, not merely the vocabulary. Keep the A12 examples evidence-bound and connect findings to the next module rather than turning each lesson into a complete hunt exercise.

## Learning Objectives and Mapping

- K: 3.3.1 – Tool capabilities for hunting
- T: 3.3.1.1 – Perform advanced querying and pivoting in VirusTotal, ANY.RUN, urlscan.io, and Silent Push
- T: 3.3.1.2 – Extract actionable hunting leads from external tool results
- T: 3.3.1.3 – Convert external findings into precise internal SIEM or Zeek queries

## Suggested Timing

| Part | Time |
|---|---:|
| Context / prior-module connection | 3 min |
| Core concepts | 10–12 min |
| A12 or classroom application | 4–5 min |
| Knowledge check | 4 min |
| Summary / transition | 2 min |

## Teaching Notes

- Use the current vendor documentation links; avoid teaching stale UI navigation.
- Separate external evidence from internal occurrence.
- Treat the Zeek example as field predicates over Zeek data, not a universal Zeek query syntax.
- Require data source, fields, values, time/population and review context when converting a lead.

## Common Coaching Pattern

When a learner overstates the evidence, ask:

1. **What did we actually observe?**
2. **What does that observation support?**
3. **What additional evidence would be required for the stronger claim?**

For hunt modules, also ask whether the required telemetry exists and whether the search is bounded enough for a negative result to mean anything.

## Knowledge Check – Answer Key

### 1. Why isn't a VT relationship proof of internal activity?

**Expected answer:** It establishes an external dataset relationship, not that the relationship occurred in the local environment.

### 2. What belongs in an internal query plan?

**Expected answer:** Local data source, fields, exact values/relationship, time window/population, and review context.

### 3. Convert the A12 HTTP lead into fields and scope.

**Expected answer:** Example: Zeek HTTP data; id.resp_h=203.0.113.88, id.resp_p=8080/tcp, uri=/update.exe; scoped to A12-relevant user-workstation traffic and time window.

## Transition

Use the student's **Next** line to connect this lesson to the following module. Preserve unresolved visibility, detection, attribution, and scope gaps instead of solving them with assumptions.

## Supporting References

- [VirusTotal Relationships](https://docs.virustotal.com/reference/relationships)
- [VirusTotal File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours)
- [ANY.RUN TI Lookup Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf)
- [Silent Push DNS Data](https://help.silentpush.com/docs/dns-data)
- [urlscan Result API](https://urlscan.io/docs/result/)
