# Module 2.6.2 – Threat Relevance and Organizational Impact

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.6.2 B / C / C ; 2.6.2.1 3c / 4c / 4d  
- Hunter: 2.6.2 B / C / C ; 2.6.2.1 2b / 3c / 4c  
- SOC: 2.6.2 A / B / B ; 2.6.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Assess whether a threat finding is relevant to the organization's mission, assets, technologies, and exposure.
2. Describe the plausible organizational consequence if the finding is true while keeping evidence, uncertainty, and decision context visible.

**Mapped Proficiency Items:**
- K: 2.6.2 – Threat relevance and organizational impact
- T: 2.6.2.1 – Assess threat relevance and potential impact to the organization

## 1. Key Concepts

Intelligence becomes useful to an organization when the analyst explains **why the finding matters here**.

A technically interesting threat can still have low local relevance if the organization does not use the affected platform, expose the vulnerable service, operate the targeted mission, or possess the asset type in question.

This lesson separates two questions:

### Relevance

> **Does this finding meaningfully intersect our environment or mission?**

Useful relevance checks include:

- **Mission:** Does the threat affect something important to what the organization does?
- **Assets / identities:** Do we have the kinds of users, systems, data, applications, or services involved?
- **Platform / technology:** Do we run the affected technology?
- **Exposure / path:** Is there a realistic way the behavior or infrastructure could reach us?
- **Observed evidence:** Have we already seen related activity internally?

### Impact

> **If this finding is true here, what could change for the organization?**

Impact should describe a plausible consequence tied to the finding.

Examples:
- compromised user workstation;
- credential exposure;
- interruption of a business service;
- loss of sensitive client data;
- additional IR workload;
- need to isolate or patch an exposed system.

The impact statement should not become a dramatic worst-case story unless the evidence supports that escalation.

### Relevance, applicability, visibility, and impact are different

These concepts sit near one another, but they answer different questions.

| Concept | Question |
|---|---|
| **TTP applicability (2.6.1)** | Can this behavior occur in our environment? |
| **Visibility** | Can our current telemetry observe the applicable behavior? |
| **Threat relevance** | Does the finding intersect our mission, assets, technology, or exposure in a meaningful way? |
| **Impact** | What plausible organizational consequence follows if the finding is true here? |

A finding can be technically applicable but low relevance to the current requirement.

A finding can also be highly relevant while visibility is poor.

### Worked A12 example

Finding:

- encoded PowerShell on `WS-JLEE`;
- request to the update domain;
- Windows user workstation in DYA.

**Relevance:**

> The finding is relevant because DYA operates Windows user workstations and the behavior was observed on `WS-JLEE`.

**Impact:**

> If the update-domain activity represents payload delivery, the affected user workstation may require containment and further examination to determine whether a payload was successfully transferred or executed.

Notice what the impact statement does **not** claim:
- that payload execution is already proven;
- that the entire organization is compromised;
- that a nation-state conducted the activity.

The impact remains proportional to the evidence.

### Example of low relevance

A report describes wiping an industrial-control historian.

If DYA does not operate that technology, the finding may be:

> **Low / not currently relevant to this environment** because the required OT historian platform is absent.

That conclusion can change if the environment changes or if the report contains another behavior that does apply.

### Relevance should be requirement-aware

A finding can be relevant to the environment but still outside the immediate intelligence requirement.

For example, `login-prd.net` may be a useful infrastructure lead while the current requirement asks only whether the update domain delivered `update.exe` during A12.

The analyst can preserve the lead without allowing it to derail the current answer.

That is how relevance supports prioritization without erasing useful intelligence.

## 2. Knowledge Check

1. What is the difference between TTP applicability and threat relevance?
2. A behavior is applicable to Windows, but current telemetry cannot see it. Does that make the threat irrelevant? Why or why not?
3. For A12, write one relevance sentence and one impact sentence that stay within the evidence.

## 3. Summary

Relevance answers **does this matter here?**

Impact answers **what plausible consequence follows if it is true here?**

Keep those judgments tied to mission, assets, technology, exposure, and observed evidence. Preserve uncertainty rather than turning a relevant finding into a larger crisis than the evidence supports.

**Next:** [2.6 – Threat Assessment and Organizational Significance Summary](../summary.md).
