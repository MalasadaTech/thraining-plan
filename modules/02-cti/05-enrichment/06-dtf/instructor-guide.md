# Instructor Guide – Module 2.5.6 – Defender's ThreatMesh Framework (DTF)

**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Build on the previous pivot

Bring the hop record from [2.5.5](../05-infra-pivot/student-guide.md). Keep the existing evidence and distinctiveness assessment; this lesson adds a valid PTA/P-ID and uses that classification to select the next lookup. File-similarity and behavioral relationships remain separate from the infrastructure-focused DTF record.

## Purpose

Teach learners to record infrastructure-discovery pivots with valid DTF identifiers, while separating **candidate discovery** from **proof of common control**.

References:
- [DTF repository](https://github.com/MalasadaTech/defenders-threatmesh-framework)
- [Current DTF matrix](https://github.com/MalasadaTech/defenders-threatmesh-framework/blob/main/matrix.md)

## Current IDs Used in This Lesson

- PTA0001 – Domain
- PTA0002 – IP
- PTA0003 – SSL
- PTA0004 – Application
- P0101.010 – Registration: Name Server
- P0103.003 – DNS: IP Address
- P0103.004 – DNS: SOA RName
- P0202 – Proximity

These are present in the current matrix. Do not invent IDs.

## Key Teaching Points

### A DTF pivot creates a candidate

Same NS or same IP can be a valid pivot, but the candidate still needs corroboration.

Ask:
- How common is the shared characteristic?
- Is it a public/shared service?
- Do other independent features converge?

### P0202 is contextual

Do not teach “P0202 = bad pivot.”

Teach:
- adjacency can be useful in dedicated or tightly controlled infrastructure;
- adjacency across a dense public cloud range is weak by itself.

### The next lookup tests the pivot

P0101.010 → find other domains on that NS.  
P0103.003 → passive DNS / domain intelligence for the address.  
P0103.004 → other zones with the same RNAME.  
P0202 → adjacent-address investigation only when context justifies it.

## Framework Comparison

ATT&CK = behavior  
Diamond = event relationships  
Kill Chain = progression  
DTF = infrastructure discovery

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Invents a P-code. | Return to the live matrix. |
| Treats same NS as proof. | Ask how distinctive the NS is. |
| Treats same IP as proof. | Ask whether the address is shared hosting. |
| Rejects P0202 categorically. | Separate validity of the pivot from quality of the evidence in this specific range. |
| Adds ATT&CK IDs to the DTF line. | Ask whether the line describes behavior or discovery. |

## Knowledge Check – Answer Key

1. **PTA0001 / P0101.010**. Strength depends on distinctiveness and corroboration.
2. **PTA0001 / P0103.003**. Next lookup: passive DNS/domain intelligence for other names using the address.
3. P0202 is a valid pivot; the shared-cloud `/24` example is weak because adjacency in that environment is not distinctive enough to support a strong relationship.

## Instructor References

- [Defender's ThreatMesh Framework](https://github.com/MalasadaTech/defenders-threatmesh-framework)
- [DTF Matrix](https://github.com/MalasadaTech/defenders-threatmesh-framework/blob/main/matrix.md)
