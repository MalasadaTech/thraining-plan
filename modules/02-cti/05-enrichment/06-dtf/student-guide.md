# Module 2.5.6 – MalasadaTech Defender's ThreatMesh Framework (DTF)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.6 B / C / C ; 2.5.6.1 3c / 4c / 4d ; 2.5.6.2 3c / 4c / 4d ; 2.5.6.3 3c / 4c / 4c  
- Hunter: 2.5.6 A / B / B ; 2.5.6.1 1a / 2b / 3c ; 2.5.6.2 1a / 2b / 3c ; 2.5.6.3 1a / 2b / 3c  
- SOC: 2.5.6 A / A / B ; 2.5.6.1 1a / 1a / 2b ; 2.5.6.2 1a / 1a / 2b ; 2.5.6.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

## Build on the previous pivot

Bring the hop record from [2.5.5](../05-infra-pivot/student-guide.md). Keep the existing evidence and distinctiveness assessment; this lesson adds a valid PTA/P-ID and uses that classification to select the next lookup. File-similarity and behavioral relationships remain separate from the infrastructure-focused DTF record.

## Learning Objectives

1. Explain DTF's purpose and select a valid Pivot Tactic (PTA) and Pivot (P) from a known-bad infrastructure seed.
2. Use the pivot's shared characteristic to identify a candidate, assess whether the relationship is distinctive enough to pursue, and name the next enrichment step.
3. Explain how DTF complements ATT&CK, Diamond, and the Cyber Kill Chain.

**Mapped Proficiency Items:**
- K: 2.5.6 – Defender’s ThreatMesh Framework (DTF) for infrastructure discovery
- T: 2.5.6.1 – Apply DTF: select a pivot tactic and pivot from a seed and reject the weak neighbor
- T: 2.5.6.2 – Use a selected DTF pivot to guide the next enrichment or lookup
- T: 2.5.6.3 – Explain how DTF integrates with or complements ATT&CK, Diamond, and Kill Chain

## 1. Key Concepts

The **Defender's ThreatMesh Framework (DTF)** organizes ways defenders can pivot from known malicious infrastructure to discover additional candidate infrastructure.

The framework is inspired by ATT&CK's matrix structure, but its job is different: **DTF is about discovery pivots, not adversary behavior**.

References:
- [Defender's ThreatMesh Framework repository](https://github.com/MalasadaTech/defenders-threatmesh-framework)
- [Current DTF matrix](https://github.com/MalasadaTech/defenders-threatmesh-framework/blob/main/matrix.md)

### Pivot tactics and pivots

The current DTF matrix contains four Pivot Tactics:

| Pivot Tactic | Name | Examples of pivot families |
|---|---|---|
| **PTA0001** | Domain | Registration, domain characteristics, DNS |
| **PTA0002** | IP | Reverse lookup, proximity, AS |
| **PTA0003** | SSL | Issuer, SAN, certificate timing |
| **PTA0004** | Application | HTTP title, embedded code, resources |

Under each tactic are specific Pivot IDs.

Examples confirmed in the current matrix:

- **P0101.010 – Registration: Name Server**
- **P0103.003 – DNS: IP Address**
- **P0103.004 – DNS: SOA RName**
- **P0202 – Proximity**

Use the IDs that actually exist in the framework rather than inventing a code for an interesting idea.

### Classify the existing A12 hops

Use the candidate relationships already evaluated in 2.5.5. Add the DTF classification without changing the strength of the evidence:

| Existing hop | DTF classification | What the classification adds |
|---|---|---|
| Update domain → shared `ns1.cdn-test.net` → `login-prd.net` | **PTA0001 / P0101.010 – Registration: Name Server** | Names the characteristic used to discover the candidate. |
| Update domain → shared `203.0.113.88` → candidate domain | **PTA0001 / P0103.003 – DNS: IP Address** | Names the DNS-address pivot so another analyst can reproduce it. |

A framework code labels the discovery method. It does not upgrade a candidate into confirmed adversary infrastructure. Carry forward the hosting context, timing, and corroboration assessment from the previous lesson.

### Proximity is not automatically wrong

**P0202 – Proximity** is a valid DTF pivot.

The problem is not the pivot itself. The problem is using it without considering hosting context.

For example:

- checking nearby IPs around a known dedicated adversary server may be productive;
- declaring an entire busy cloud `/24` adversary-owned because one bad IP appears inside it is not supported.

So the classroom `/24` example is **rejected as a strong relationship**, not because P0202 is an invalid pivot, but because shared-cloud proximity is too weak in that scenario.

### The pivot should name the next lookup

The selected pivot should lead naturally to a next enrichment action.

| DTF pivot | Useful next step |
|---|---|
| **P0101.010 – Name Server** | Search domain/passive-DNS data for other domains using the same NS; optionally enrich the NS's registrable domain with RDAP. |
| **P0103.003 – DNS: IP Address** | Search passive DNS or domain intelligence for other names associated with the address. |
| **P0103.004 – DNS: SOA RName** | Search for other zones publishing the same distinctive RNAME and compare additional DNS/registration features. |
| **P0202 – Proximity** | Examine nearby addresses only when network context makes adjacency meaningful. |

The DTF line records **why** you pivoted. The next lookup tests whether the candidate relationship survives further scrutiny.

### DTF complements the other frameworks

| Framework | Primary question |
|---|---|
| **ATT&CK** | What adversary behavior is being performed? |
| **Diamond Model** | What are the Adversary, Capability, Infrastructure, and Victim relationships in this event? |
| **Cyber Kill Chain** | Where does supported activity sit in attack progression? |
| **DTF** | What infrastructure characteristic can we pivot on to discover additional candidates? |

They can all describe different aspects of the same investigation without replacing one another.

### A concise DTF record

A practical format is:

`seed | PTA | P-ID | shared characteristic | candidate | why this is worth pursuing | next lookup`

Example:

`update-domain | PTA0001 | P0101.010 | ns1.cdn-test.net | login-prd.net | uncommon NS overlap | search other domains using NS`

That is enough for another analyst to understand and repeat the pivot.

## 2. Knowledge Check

1. The update domain and `login-prd.net` share `ns1.cdn-test.net`. Which DTF PTA/P-ID describes the pivot, and what determines whether the relationship is strong?
2. Two suspicious names resolve to the same `203.0.113.88`. Which DTF pivot applies, and what is a useful next lookup?
3. Why is rejecting the entire shared-cloud `/24` different from saying **P0202 Proximity** is an invalid pivot?

## 3. Summary

DTF gives defenders a repeatable vocabulary for infrastructure discovery.

Use a real PTA/P-ID, preserve the characteristic that produced the candidate, evaluate how distinctive that characteristic is, and name the next lookup that will test the relationship.

A pivot discovers **candidates**. Corroborating evidence turns candidates into defensible infrastructure relationships.


## Supporting References

- [Defender's ThreatMesh Framework](https://github.com/MalasadaTech/defenders-threatmesh-framework)
- [DTF Matrix](https://github.com/MalasadaTech/defenders-threatmesh-framework/blob/main/matrix.md)

**Next:** [2.5.7 – Correlation, Link Analysis, and Campaign Tracking](../07-correlation/student-guide.md).
