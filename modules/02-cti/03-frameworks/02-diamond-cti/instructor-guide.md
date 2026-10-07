# Instructor Guide – Module 2.3.2 – Diamond Model Application in CTI

**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Purpose

Help learners use the Diamond Model as an evidence-backed representation of an intrusion event rather than as a four-box form that must be completely filled.

Reference: [The Diamond Model of Intrusion Analysis](https://www.threatintel.academy/diamond/)

## Key Teaching Points

- The four core features are Adversary, Capability, Infrastructure, and Victim.
- Incomplete vertices are acceptable.
- Relationships among vertices are analytically important.
- A vendor tracking name can be recorded with provenance without being silently promoted to independently established adversary identity.
- “Weakest vertex” is a classroom checkpoint for evidentiary gaps, not a formal fifth component of the model.

## A12 Walkthrough

**Adversary:** unresolved activity cluster  
**Capability:** encoded PowerShell / requested `/update.exe` as a candidate payload name  
**Infrastructure:** update domain / `203.0.113.88`  
**Victim:** `WS-JLEE` / `jlee` / DYA

Ask learners why Adversary is the least developed. The answer should be about evidence, not about whether a vendor has published a name.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Treats every vertex as mandatory. | Explain that incomplete knowledge is normal; preserve the gap. |
| Copies a vendor label into Adversary as fact. | Require source attribution and ask what evidence independently establishes identity. |
| Treats the Diamond as four unrelated boxes. | Ask what edge relationship connects two vertices and what it tells the analyst. |
| Turns the lesson into an actor profile. | Return to one intrusion event and its four core features. |

## Knowledge Check – Answer Key

1. Adversary, Capability, Infrastructure, Victim.
2. A12 has direct evidence for capability, infrastructure, and victim; the responsible adversary remains unresolved.
3. Attribute the claim to the vendor or source rather than presenting the tracking label as independently proven identity.

## Instructor Reference

- [The Diamond Model of Intrusion Analysis](https://www.threatintel.academy/diamond/)
