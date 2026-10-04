# Module 2.7.4 – RFI Responses and Closure

**Target Audience:** CTI Analyst (primary); Threat Hunter and SOC Analyst (supporting context)  
**Proficiency Focus:**  
- CTI: 2.7.4 B / C / C ; 2.7.4.1 3c / 4c / 4d  
- Hunter: 2.7.4 A / A / B ; 2.7.4.1 1a / 1a / 2b  
- SOC: 2.7.4 A / A / A ; 2.7.4.1 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes

## Learning Objectives

1. Write a direct RFI response that separates the supported answer from unresolved evidence gaps.
2. Check the response against the original requirement and record closure or agreed follow-up.

**Mapped Proficiency Items:**
- K: 2.7.4 – RFI responses and closure
- T: 2.7.4.1 – Produce an evidence-based RFI response and close or record follow-up

## 1. Key Concepts

Return to the intake record from [2.1.5](../../01-core-intel/05-rfi-intake/student-guide.md). Check whether the question, deadline, or handling constraints changed during the work. If they did, clarify and record the change with the requester.

The assessment in 2.6 now supports a direct answer. A response can be brief when the question is narrow; it does not need to become a full actor profile.

Answer the question that was asked.

A useful response normally includes:

- direct answer / key judgment;
- evidence basis;
- uncertainty or limitation;
- relevant next implication or unresolved requirement.

Do not make the recipient search through a long actor history to find a two-sentence answer.

### Complete the A12 RFI

**Question:**
> Was the update domain the host that successfully delivered the payload in A12?

**Evidence available:**
- `WS-JLEE` requested `/update.exe` from the update domain during suspicious activity.
- The update domain resolves to the infrastructure already associated with the case.
- Available evidence does not establish successful download or execution of `/update.exe`.

**Response:**
> We assess the update domain was **likely used for attempted payload delivery** in A12. `WS-JLEE` requested `/update.exe` from that destination during the suspicious activity, but available evidence does not establish that the file was successfully downloaded or executed.

That response answers the question while preserving the evidence boundary.

### When the RFI cannot be fully answered

A useful partial response can say:

> Current evidence is insufficient to determine whether the payload was successfully delivered. Confirmation would require response/file-transfer evidence or a resulting file/artifact on the host.

That is better than filling the gap with confidence language unsupported by the evidence.

### Close the loop

An RFI is complete when the requestor receives:
- the answer available now;
- the uncertainty/gaps;
- any agreed follow-up.

If a new question emerges, record it as a new/follow-on requirement rather than silently expanding the original RFI forever.


Confirm the response uses the approved audience and channel in [2.7.5](../05-dissemination/student-guide.md), and archive the answer and agreed follow-up through the local process in [2.8.2](../../08-site-specific/02-local-production/student-guide.md).

## 2. Knowledge Check

1. Write a two-sentence A12 response that distinguishes attempted payload delivery from successful delivery.
2. What should a useful response contain when evidence cannot fully answer the question?
3. How should you handle a new question that arises when the requester receives the answer?

## 3. Summary

Answer the original question as far as the evidence allows. Preserve uncertainty and record closure or the next agreed requirement.

**Next:** [2.7.5 – Disseminating Intelligence to the Correct Audiences](../05-dissemination/student-guide.md).
