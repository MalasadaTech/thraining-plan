# Module 2.1.7 – Tailoring Output to the Audience

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.7 B / C / C ; 2.1.7.1 3c / 4c / 4d  
- Hunter: 2.1.7 A / B / B ; 2.1.7.1 1a / 2b / 3c  
- SOC: 2.1.7 A / A / B ; 2.1.7.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain why **audience analysis** should happen before an intelligence product is written or delivered.
2. Adjust the **content**, **format**, and **level of detail** of an intelligence product for a specified audience while preserving the underlying facts and analytic judgment.

**Mapped Proficiency Items:**
- K: 2.1.7 – Tailoring output to the audience
- T: 2.1.7.1 – Adjust an intelligence product for a specified audience

## 1. Key Concepts

An intelligence product is useful only if the intended reader can understand it and use it for the decision they own. The same assessment may therefore need to be presented differently to leadership, SOC, IR, threat hunters, or detection engineers.

Tailoring does **not** mean changing the evidence or softening the judgment to match what a reader wants to hear. It means deciding which parts of the same underlying analysis each audience needs, how much detail they can use, and what format makes the decision easiest to understand.

Before writing, ask:

- **Who is the consumer?**
- **What decision or action do they own?**
- **What do they already know?**
- **Which facts, caveats, and details do they need in order to use the assessment correctly?**

### Three things you adjust

| Element | What it means |
|---|---|
| **Content** | Which facts, implications, and supporting details the reader needs for their decision |
| **Format** | The shape of the product: short summary, paragraph, table, technical appendix, briefing, or other appropriate form |
| **Level of detail** | How much technical depth, evidence, and supporting context the reader needs |

The underlying evidence and analytic judgment should remain consistent across versions. Tailoring changes the **presentation and emphasis**, not the truth of the assessment.

### Follow the same A12 assessment for two audiences

Use the assessment developed earlier in the course:

> We assess that the update domain likely supported attempted payload delivery during A12. WS-JLEE requested `/update.exe` from that destination during the suspicious activity. Successful download and execution remain unresolved.

A leadership version might say:

> **A12 involved suspicious PowerShell activity on WS-JLEE and an external domain that likely supported attempted payload delivery. IR has the affected host; the immediate evidence gap is whether the requested file was successfully delivered or executed.**

This version preserves the assessment and uncertainty while emphasizing impact, ownership, and the decision-relevant gap. Leadership usually does not need every path, hash, or request field in the main line.

An IR / SOC version could retain more technical detail:

> **WS-JLEE requested `/update.exe` from the update domain during the A12 activity. CTI assesses the domain likely supported attempted payload delivery. Review the related network, file, and process evidence to determine whether the transfer completed and whether the file executed.**

This version emphasizes the host, request path, evidence, and next investigative step because those details are directly useful to the technical consumer.

### Same facts does not mean identical wording

Good tailoring may change the order of information, the amount of supporting evidence, the terminology, and the prominence of caveats.

For leadership, the analyst may lead with the implication and decision point. For IR, the analyst may lead with the affected host and evidence. For a hunter, the analyst may emphasize behavioral patterns and observables. The assessment should still be traceable back to the same evidence and judgment.

### Avoid two opposite errors

**Too much detail:** A leadership product can become harder to use when the main message is buried under hashes, file paths, raw logs, or platform-specific fields.

**Too little detail:** A technical team may be unable to act if the product reduces everything to a one-line “so what” without the host, artifacts, behavior, or evidence they need.

Tailoring is therefore a balance between **relevance and sufficiency**. Give the reader enough to make the right decision without forcing them to reconstruct the analysis from irrelevant detail.

### Tailoring and dissemination are related, but different

Tailoring concerns the **content and presentation** of the product. Dissemination also includes how and where the product is delivered. Later modules cover channels and finished-product mechanics in more depth.

## 2. Knowledge Check

1. Tailoring means changing the analytic judgment so that it is more acceptable to leadership. True or false? Explain.
2. What three elements of a product can you adjust for a specified audience?
3. Using the A12 assessment, write one short leadership version and list two additional details you would retain or add for IR / SOC.

## 3. Summary

Audience analysis begins with the consumer's decision. Once you know who will use the product and what they need to do, you can adjust the content, format, and level of detail without changing the underlying evidence or analytic judgment.

Leadership usually needs implications, ownership, and decision-relevant uncertainty. Technical consumers usually need more of the host, behavior, artifact, and evidence detail that allows them to investigate or respond.

The goal is not to make every reader see the same words. The goal is to make every reader receive the **same supported assessment in a form they can use correctly**.


## 4. Related Modules

- 2.1.6 – Ensuring intelligence is actionable (previous)
- 2.1.8 – Attribution
- 2.7.5 – Dissemination channels
- 1.5 – SOC reporting and routing

**Next:** [2.1.8 – Attribution](../08-attribution/student-guide.md).
