# Module 2.7.3 – Creating Finished Intelligence Products

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.3 B / C / C ; 2.7.3.1 3c / 4c / 4d ; 2.7.3.2 3c / 4c / 4d  
- Hunter: 2.7.3 A / B / B ; 2.7.3.1 1a / 2b / 3c ; 2.7.3.2 1a / 2b / 3c  
- SOC: 2.7.3 A / A / B ; 2.7.3.1 1a / 1a / 2b ; 2.7.3.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Draft a short finished intelligence product that answers a requirement and evaluate it against clear analytic standards.
2. Produce a concise actor or activity profile that distinguishes what is known, what is assessed, and what remains unresolved.

**Mapped Proficiency Items:**
- K: 2.7.3 – Creating finished intelligence products
- T: 2.7.3.1 – Draft a finished product and evaluate it against standards
- T: 2.7.3.2 – Produce a threat actor profile

## 1. Key Concepts

A **finished intelligence product** is the usable result of analysis: it answers a defined question with evidence-based judgments and enough context for the intended customer to understand what matters.

A list of indicators, a TIP export, or a STIX bundle may support the product, but none is automatically a finished analytic product.

### Product type follows the question

Common classroom product types include:

| Product | Best fit |
|---|---|
| **Assessment** | A judged answer to a specific intelligence question. |
| **Activity / actor profile** | A structured description of a tracked cluster or actor, including behavior, infrastructure, targeting, confidence, and gaps. |
| **RFI response** | A bounded answer to a Request for Information. Intake and priority are taught in 2.1.5; response and closure are taught in 2.7.4. |

The product should match the requirement rather than trying to combine every format into one document.

### A compact finished-product structure

A short CTI product should normally make these elements easy to find:

1. **Requirement / question** – What are we answering?
2. **Key judgment** – What do we assess?
3. **Evidence / source basis** – What observations and reporting support the judgment?
4. **Uncertainty / confidence** – How strong is the evidence and what remains unknown?
5. **Relevance / implications** – Why does this matter to the customer or decision?

That structure is a classroom implementation of broader analytic-tradecraft principles rather than a claim that every organization must use these exact headings.

### Quality is more than formatting

ODNI's **ICD 203 – Analytic Standards** provides a useful reference for evaluating analytic products. Among other tradecraft expectations, it emphasizes:

- describing source quality and credibility;
- explaining uncertainty;
- distinguishing underlying information from assumptions and judgments;
- considering alternatives when relevant;
- demonstrating customer relevance and implications;
- using clear and logical reasoning.

References:
- [ODNI – ICD 203, Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)
- [ODNI – Objectivity and Analytic Standards](https://www.dni.gov/index.php/how-we-work/objectivity)

This course applies those ideas to CTI without pretending the classroom format is an official IC template.

### Facts and judgments should remain distinguishable

A useful product makes it possible for the reader to see what was **observed** and what the analyst **assesses**.

For A12:

**Observed**
- `WS-JLEE` requested `/update.exe` from the update domain during suspicious activity.
- Encoded PowerShell occurred on the workstation.

**Judgment**
> We assess that the update domain was **likely** used for attempted payload delivery in A12.

**Uncertainty**
> Available evidence does not establish that `/update.exe` was successfully downloaded or executed.

That is stronger tradecraft than writing:

> The domain was the payload host.

because the latter removes an important evidence boundary.

### The “so what” should be proportional

The product should explain why the judgment matters without escalating beyond the evidence.

For A12:

> The domain should remain in scope for the A12 investigation and retrospective review because the workstation requested a payload-like path from it during the suspicious activity.

That tells the consumer why the judgment matters without claiming enterprise-wide compromise or actor identity.

### Activity profile before actor identity

A profile does not require a real-world nation-state attribution.

When identity is unresolved, profile the **activity cluster** you can support.

A concise A12 profile could contain:

- **Tracking scope:** A12-associated activity cluster
- **Observed behavior:** encoded PowerShell; request for `/update.exe`
- **Infrastructure:** update domain / `203.0.113.88`; distinctive DNS characteristics where supported
- **Victim:** `WS-JLEE` / DYA
- **Assessment:** likely attempted payload delivery
- **Attribution:** unresolved
- **Gaps:** successful download/execution not established

If a vendor calls similar activity “PRD APT,” preserve that as source-attributed context rather than silently changing “Attribution: unresolved” into a country or government actor.

### Evaluate the draft against the question

A useful review asks:

- Does the product actually answer the requirement?
- Can the reader distinguish evidence from judgment?
- Is uncertainty explicit?
- Are major claims traceable to source/evidence?
- Are alternatives or important gaps acknowledged?
- Is the relevance or implication clear?
- Is attribution no stronger than the evidence?

A polished document that fails those questions is still analytically weak.

## 2. Demonstration Exercise — Non-A12 Threat Actor Profile

This exercise is **not part of A12**. It uses a separate training-only evidence set so you can practice the approved threat-actor-profile task without inventing attribution for the recurring case.

### Training evidence set: SILVER KITE

You are supporting a fictional regional manufacturer. Four independent reports over six months describe the same tracked actor, **SILVER KITE**, with the following corroborated characteristics:

- repeatedly targets aerospace and advanced-manufacturing organizations in the United States and Japan;
- obtains initial access through spearphishing attachments and exploitation of externally exposed VPN appliances;
- uses PowerShell for discovery and staging, then deploys a custom backdoor consistently identified in the supplied reporting as **KiteDoor**;
- creates scheduled tasks for persistence and commonly archives collected engineering documents before exfiltration;
- uses short-lived VPS infrastructure registered through multiple providers;
- has targeted organizations for technical drawings, proprietary manufacturing data, and program documentation;
- two high-confidence sources attribute the activity to the same named actor, while **no supplied evidence supports a government sponsor, nationality, or legal identity**.

### Required output

Produce a concise threat actor profile that includes:

1. **Tracking identity and scope** — what SILVER KITE represents and the reporting period.
2. **Targeting** — sectors/regions and the information apparently sought.
3. **Observed behavior** — the major access, execution, persistence, collection, and exfiltration behaviors supported by the evidence.
4. **Infrastructure/tooling** — what is known and what remains too weak to claim.
5. **Key judgments and confidence** — at least one analytic judgment with its evidence basis.
6. **Attribution boundary and gaps** — explicitly state what the supplied evidence does **not** establish.

Then evaluate your draft against the finished-product standards taught above: requirement fit, evidence-versus-judgment separation, uncertainty, traceability, relevance, and bounded attribution.

**Demonstration note:** producing the profile demonstrates task `2.7.3.2`. When you draft it as a finished product and evaluate it against the standards above, the same event can also produce evidence for `2.7.3.1`. The evaluator records each task separately under the qualification/sign-off standard; lesson completion alone is not automatic sign-off.

## 3. Knowledge Check

1. Why is a TIP export or IOC list not automatically a finished intelligence product?
2. Name four elements that should be easy to find in a short finished product.
3. Write a three-line A12 activity profile that keeps attribution unresolved and preserves the download/execution evidence gap.

## 4. Summary

A finished intelligence product is a judged answer to a requirement, not a data dump.

Make the question, judgment, source basis, uncertainty, and relevance easy to see. Evaluate the product for analytic quality as well as presentation quality.

When actor identity is unresolved, profile the activity cluster you can defend rather than inventing attribution.


## Supporting References

- [ODNI – ICD 203, Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)
- [ODNI – Objectivity and Analytic Standards](https://www.dni.gov/index.php/how-we-work/objectivity)

**Next:** [2.7.4 – RFI Responses and Closure](../04-rfi-response/student-guide.md).
