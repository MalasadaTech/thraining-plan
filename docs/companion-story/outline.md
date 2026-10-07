# A12 companion-story outline

Use the [story bible](../story-bible.md) for facts and claim limits. The [finished story](story.md) is a standalone learner case, organized around **Evidence → Reasoning → Bounded Conclusion → Action**. It adds synthesis rather than proficiency requirements.

## Reader outcome

The learner should be able to trace evidence between roles, explain the purpose of each product, and identify what additional evidence would justify a stronger conclusion. Open with a short preview inviting the reader to predict those handoffs; close with a product table and an end-state check.

## Nine-stage narrative

| Stage | Evidence or input | Reasoning and bounded conclusion | Action / product |
|---|---|---|---|
| 1. Process alert | WS-JLEE / jlee; `wscript.exe` → encoded PowerShell | The rule matched the recorded pattern; authorization, maliciousness, and the earlier initial-access path remain unresolved. The process record does not tell whether access began through mail, web, exploitation, credential use, or a third party. | Explain the alert and its actual SIEM lineage; identify collection questions, including which evidence would test an initial-access hypothesis if that question matters. |
| 2. Context | Temp `invoice.vbs` and hash; process-associated connection; HTTP request | The request establishes attempted retrieval. The initial classification and request-coverage question remain open. | Record observations by source. VT result is not supplied; an ANY.RUN hash search may retrieve an existing report. |
| 3. Incident route | Supported process/file/network observations | Response can proceed while analytical questions remain open. | SOC routes the host to Sam and tailors a concise leadership update. |
| 4. RFI intake | Request for `/update.exe` from the update domain | The requester asks whether payload delivery succeeded; transfer evidence is missing. | Jordan owns the bounded RFI; priority and routing use the actual local process. |
| 5. CTI answer | Request during suspicious activity | Likely attempted payload delivery; transfer and execution unresolved. ATT&CK describes behavior, Diamond organizes entities, Kill Chain examines supported progression. PRD remains a vendor label. | Return the answer available now, evidence basis, uncertainty, and follow-up need. |
| 6. Infrastructure candidate | `login-prd.net` shares the uncommon NS pair and observed A during the relevant period | Candidate relationship requiring corroboration. The Example Cloud `/24` is too broad to promote. | Preserve the hop and next test; reject the broad range. |
| 7. Protective-control review | Candidate, observation period, provenance, and limitations | Operational action depends on the owner's local threshold. | Refer the candidate for review; the final action remains unspecified. |
| 8. Hunt development | PowerShell-set HKCU Run `Updater` → `%TEMP%\update.exe`; supporting case artifacts | Configuration is observed; target execution and additional affected hosts remain unresolved. | Form a bounded hypothesis and package the evidence, scope, and questions. |
| 9. DE review | Need and case/hunt evidence pointer | Check existing coverage, data availability, and whether detection work is justified. | Present add/change/reuse/no-new-rule/data-gap/routing possibilities; the actual outcome remains open. |

## Presentation and factual continuity

Preserve DYA, Building C, WS-JLEE, `jlee` / `BUILDINGC\jlee`, Sam, Jordan, the established process/file/registry/network values, and the sibling candidate. Present later evidence when its operational use becomes relevant. Keep supplied sandbox cards and hypothetical deployment exercises distinct from local A12 observations.

Use explanatory paragraphs to connect stages. Tables should clarify evidence or decisions. Place optional lesson links at the end so the narrative reads independently. The ending states what remains open: successful transfer/execution, other affected hosts, protective-control action, DE outcome, incident closure, and attribution.
