# Module 2.3.2 – Diamond Model Application in CTI

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.3.2 B / C / C ; 2.3.2.1 3c / 4c / 4d  
- Hunter: 2.3.2 B / C / C ; 2.3.2.1 3c / 4c / 4d  
- SOC: 2.3.2 A / B / B ; 2.3.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Populate the four Diamond Model core features from a report or activity set using evidence.
2. Identify which vertex is least developed and explain how that uncertainty constrains the intelligence product.

**Mapped Proficiency Items:**
- K: 2.3.2 – Diamond Model application in CTI
- T: 2.3.2.1 – Apply the Diamond Model to an intelligence problem

## 1. Key Concepts

The Diamond Model treats an intrusion **event** as relationships among four core features:

- **Adversary**
- **Capability**
- **Infrastructure**
- **Victim**

The original paper describes these features as the core of an intrusion event and uses the edges between them to support analysis, correlation, and discovery.

Reference: [The Diamond Model of Intrusion Analysis](https://www.threatintel.academy/diamond/)

### The four vertices

| Vertex | CTI question |
|---|---|
| **Adversary** | Who is responsible for or associated with the activity, at the level the evidence supports? |
| **Capability** | What capability, malware, tool, exploit, or method is being used? |
| **Infrastructure** | What infrastructure enables or carries the activity? |
| **Victim** | Who or what is being targeted or affected? |

A Diamond does not become invalid because one vertex is unknown. Incomplete knowledge is normal in intrusion analysis.

### Apply the model to A12

For the A12 activity set:

- `wscript.exe` launches encoded PowerShell;
- A12 includes a request for `/update.exe`; that path is a **candidate payload name**, not an established transferred or executed sample;
- the update domain and `203.0.113.88` appear in the infrastructure;
- `WS-JLEE` / `jlee` are the affected victim assets.

A defensible Diamond is:

| Vertex | A12 fill |
|---|---|
| **Adversary** | Unknown / unresolved activity cluster |
| **Capability** | Encoded PowerShell; requested `/update.exe` as a candidate payload name |
| **Infrastructure** | Update domain; `203.0.113.88` |
| **Victim** | `WS-JLEE`; `jlee`; DYA |

The **Adversary** vertex is the least developed.

That is useful analytical information. It tells the writer that the product can describe capability, infrastructure, and victim with more specificity than it can describe who is behind the activity.

### Vendor tracking names require source qualification

A vendor name such as “PRD APT” can be useful context if a source attributes the activity that way. But a tracking label is not automatically the same thing as independently established adversary identity.

A careful product can say:

> Vendor X tracks similar activity as “PRD APT.”

That preserves provenance.

It is stronger than silently changing the Diamond vertex to:

> Adversary = PRD APT

unless the product's own evidence and sourcing justify that conclusion.

This distinction keeps the Diamond useful as an analytical model rather than turning it into a place to copy labels.

### Relationships matter as much as the boxes

The Diamond Model is not just four fields. The edges represent relationships that analysts can test and pivot across.

For example:

- capability ↔ infrastructure: Which infrastructure delivered or controlled this capability?
- infrastructure ↔ victim: Which victim interacted with this infrastructure?
- adversary ↔ capability: What evidence connects this capability to an activity cluster?
- adversary ↔ infrastructure: What evidence links the infrastructure to the same cluster?

Those relationships often reveal where the next intelligence question should go.

### Classroom “weakest vertex”

This course uses **weakest vertex** as a practical checkpoint: identify which core feature has the least evidentiary support.

That phrase is a classroom aid, not a new fifth Diamond component. Its purpose is to make the analyst state where the model is least complete and avoid filling the gap with a guess.

## 2. Knowledge Check

1. What are the four core Diamond Model features?
2. In A12, why is the Adversary vertex less developed than Capability, Infrastructure, and Victim?
3. A vendor report calls the activity “PRD APT.” How can you preserve that information without presenting the vendor label as independently proven adversary identity?

## 3. Summary

The Diamond Model organizes an intrusion event around Adversary, Capability, Infrastructure, and Victim—and the relationships among them.

Use evidence to populate each vertex. Leave a vertex unresolved when the evidence is unresolved. In this course, naming the least-developed vertex helps keep uncertainty visible instead of completing the model with speculation.


## Supporting Reference

- [The Diamond Model of Intrusion Analysis](https://www.threatintel.academy/diamond/)

**Next:** [2.3.3 – Cyber Kill Chain in Intelligence Analysis](../03-kill-chain-cti/student-guide.md).
