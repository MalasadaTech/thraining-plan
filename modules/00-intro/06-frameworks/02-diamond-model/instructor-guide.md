# Instructor Guide – Module 0.6.2 – Diamond Model

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.2.1 A / B / C ; 0.6.2.2 2b / 3c / 4c  
- Hunter: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- CTI: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- DE: 0.6.2.1 A / B / B ; 0.6.2.2 1a / 2b / 2b  
**Estimated Time:** 15 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

The Diamond Model helps you organize what is known about an intrusion event and identify useful questions about what is missing. Its four vertices keep the activity, the systems involved, and the responsible party visible in one view.

Teach this as a shared introductory lesson using the supplied examples and discussion. Match the depth to the proficiency levels above. The focus is the mapped knowledge and task; operational procedures are developed in the later role tracks.

## Learning Objectives

1. Describe the four Diamond Model vertices.
2. Organize a simple event using the available evidence.
3. Identify the weakest-supported vertex and explain the evidence gap.

**Mapped Proficiency Items:**
- K: 0.6.2.1 – Diamond Model
- T: 0.6.2.2 – Apply the Diamond Model to an incident or set of indicators

## Preparation

Read the [student guide](student-guide.md) and use [slides.md](slides.md) to support the explanation. Review the answer key before teaching so the discussion and feedback reinforce the same concepts. This lesson uses discussion and worked examples; no lab is required.

## Suggested Timing

| Section | Time | Teaching purpose |
|---|---|---|
| Opening and purpose | 2 min | Connect this lesson to the previous topic. |
| Explanation and worked examples | 7 min | Use the three teaching sections below. |
| Knowledge check and feedback | 4 min | Ask for reasoning as well as an answer. |
| Summary and transition | 2 min | Consolidate the lesson and introduce the next topic. |
| **Total** | **15 min** | |

## Detailed Teaching Notes

### 1. The four vertices

Introduce each vertex as a question analysts can answer from evidence. Explain that a partially filled model is useful because it makes uncertainty visible. Avoid implying that every investigation can identify the adversary.

**Student-facing emphasis:** Adversary: responsible party. Capability: tools or techniques. Infrastructure: enabling systems or services. Victim: targeted or affected entity.

### 2. Organizing a small example

Trace each entry to its source. Ask what the network event proves: contact occurred. Then ask what remains uncertain: ownership, purpose, and relevance. This distinction prevents the diagram from making an inference appear established.

**Student-facing emphasis:** Capability: observed PowerShell execution. Infrastructure: contacted domain; role still under assessment. Victim: observed workstation. Adversary: unknown from these events.

### 3. Using gaps to guide a question

Ask learners to distinguish the largest evidence gap from the highest-priority next step. Vendor research can supply evidence; a label without its basis cannot resolve attribution. Keep the discussion at the four-vertex level.

**Student-facing emphasis:** Identify the weakest-supported vertex. Explain what evidence is missing. Choose the next question according to the investigation’s purpose.

## Knowledge Check — Answer Key

### 1. Name the four Diamond Model vertices and what each describes.

**Expected answer:** Adversary: responsible party; capability: tools or techniques; infrastructure: enabling systems or services; victim: targeted or affected entity.

**Feedback and assessment:** Accept equivalent plain-language descriptions when the four roles remain distinct.

### 2. How would you organize the PowerShell and domain-contact example?

**Expected answer:** Capability is observed PowerShell execution; infrastructure is the contacted domain with its role provisional; victim is the workstation; adversary is unknown. Cite the endpoint and network events for the observed entries.

**Feedback and assessment:** The answer should retain the uncertainty about the domain’s role and adversary identity.

### 3. Which vertex is weakest in the example, and must it be resolved first?

**Expected answer:** Adversary is unsupported by these events. It need not be resolved first; the next question should also reflect the investigation’s purpose, such as finding other exposed hosts.

**Feedback and assessment:** Look for an evidence gap and a reasoned priority, rather than a requirement to attribute every event.

## Closing and Transition

The Diamond Model organizes an event around adversary, capability, infrastructure, and victim. Populate it from evidence, mark uncertainty, and use the gaps to develop questions that matter to the investigation.

Previous: [0.6.1 – MITRE ATT&CK](../01-attck/student-guide.md)

Next: [0.6.3 – Cyber Kill Chain](../03-cyber-kill-chain/student-guide.md)

## References and Further Reading

- [Sergio Caltagirone — The Diamond Model](https://www.activeresponse.org/the-diamond-model/) — Author resource for the model introduced by Caltagirone, Pendergast, and Betz in 2013.
