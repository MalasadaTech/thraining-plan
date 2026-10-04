# Module 0.6.2 – Diamond Model

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.2.1 A / B / C ; 0.6.2.2 2b / 3c / 4c  
- Hunter: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- CTI: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- DE: 0.6.2.1 A / B / B ; 0.6.2.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Describe the four Diamond Model vertices.
2. Organize a simple event using the available evidence.
3. Identify the weakest-supported vertex and explain the evidence gap.

**Mapped Proficiency Items:**
- K: 0.6.2.1 – Diamond Model
- T: 0.6.2.2 – Apply the Diamond Model to an incident or set of indicators

## Why This Matters

The Diamond Model helps you organize what is known about an intrusion event and identify useful questions about what is missing. Its four vertices keep the activity, the systems involved, and the responsible party visible in one view.

## 1. The four vertices

| Vertex | Question it helps answer |
|---|---|
| Adversary | Who is responsible for the activity? |
| Capability | What tools or techniques were used? |
| Infrastructure | What systems or services enabled the activity? |
| Victim | Who or what was targeted or affected? |

The model connects these elements within an event. For example, an adversary may use a capability through infrastructure against a victim. An investigation may begin with evidence for only some of those elements.

## 2. Organizing a small example

Suppose an endpoint event shows PowerShell running on a workstation, and a related network event records that process contacting a domain identified in the investigation as suspicious.

| Vertex | What can be recorded | Basis or limitation |
|---|---|---|
| Adversary | Unknown. | These events do not identify the responsible party. |
| Capability | PowerShell execution. | The endpoint process event records the interpreter. |
| Infrastructure | The contacted domain, provisionally associated with the activity. | The network event establishes contact; the domain's role still needs assessment. |
| Victim | The observed workstation. | The endpoint and network records identify the host. |

This organizes the observations without treating contact as proof that the domain is attacker-controlled. More evidence may refine the domain's role or the assessment of the event.

## 3. Using gaps to guide a question

The weakest-supported vertex highlights a gap in the available evidence. In this example, the adversary vertex is unknown. A vendor's actor label may suggest a lead, but evaluating attribution requires the evidence and reasoning behind that label.

The next question should also serve the investigation's purpose. If the immediate concern is whether other workstations contacted the domain, checking that exposure may be more useful than attempting attribution. The model helps you see gaps and choose a relevant question; it does not require every vertex to be completed before action can continue.

## Knowledge Check

1. Name the four Diamond Model vertices and what each describes.
2. How would you organize the PowerShell and domain-contact example?
3. Which vertex is weakest in the example, and must it be resolved first?

## Summary

The Diamond Model organizes an event around adversary, capability, infrastructure, and victim. Populate it from evidence, mark uncertainty, and use the gaps to develop questions that matter to the investigation.

## Course Connections

Previous: [0.6.1 – MITRE ATT&CK](../01-attck/student-guide.md)

Next: [0.6.3 – Cyber Kill Chain](../03-cyber-kill-chain/student-guide.md)

## References and Further Reading

- [Sergio Caltagirone — The Diamond Model](https://www.activeresponse.org/the-diamond-model/) — Author resource for the model introduced by Caltagirone, Pendergast, and Betz in 2013.
