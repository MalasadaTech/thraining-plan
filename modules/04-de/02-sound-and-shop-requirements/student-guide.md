# Module 4.2 – Making a Detection Sound and Meeting Shop Requirements

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.2 B / C / C ; 4.2.1 3c / 4c / 4d ; 4.2.2 3c / 4c / 4c ; 4.2.3 3c / 4c / 4c  
- SOC: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
- Hunter: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
- CTI: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Define the behavior a detection should recognize and state **positive, negative, and data-availability test expectations** before deployment.
2. Check the actual local requirements list without confusing an external rule format with shop policy.
3. Close the loop with the nominator by recording the disposition and any important change to the original need.

**Mapped Proficiency Items:**
- K: 4.2 – Making a detection sound and meeting shop requirements
- T: 4.2.1 – Test a draft or change: what must fire and what must not
- T: 4.2.2 – Mark which shop requirements are met and which are still missing
- T: 4.2.3 – Write the close-the-loop note to the nominator

## 1. Key Concepts

A detection is ready for production because its **behavior, data assumptions, and test results are understood**—not merely because the query parses.

For this course, a sound detection should answer three questions:

1. **What should match?**
2. **What similar activity should not match?**
3. **What data must exist for the analytic to work?**

### Positive tests: what must fire

Use one or more known examples of the intended behavior.

For A12, if the analytic is designed around suspicious encoded PowerShell, a positive test should reproduce or safely emulate the relevant process/command behavior and verify that the detection matches the expected fields.

A positive test demonstrates:

> Under these test conditions, the analytic recognized the behavior it was designed to detect.

It does not prove that every future variation will be detected.

### Negative tests: what must not fire

Test realistic benign or near-neighbor activity.

Examples:
- a sanctioned administration script;
- a backup process that resembles part of the malicious pattern;
- a legitimate PowerShell command without the suspicious combination the analytic requires.

The goal is not “zero false positives forever.” The goal is to understand the boundary between:
- intended detection;
- expected benign activity;
- acceptable review volume.

Sigma's documentation explicitly treats false-positive context and filters as part of detection engineering. See:
- [Sigma Rules – false positives and rule metadata](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html)
- [Sigma Filters](https://sigmahq.io/docs/meta/)

### Data-availability test: can the analytic actually see its inputs?

A correct logical condition still fails if the required data is missing, delayed, parsed differently, or absent on part of the environment.

Before deployment, verify:
- required log/event source exists;
- required fields are populated;
- field normalization matches the analytic;
- the intended host/user/network population is covered;
- the data arrives within the timeframe the analytic expects.

The Sigma log-source guidance illustrates the same principle: detection logic must be applied to the correct logs and fields. See [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html).

### Test the behavior, not only the exact IOC

Behavior-focused validation is more durable than replaying one exact malicious value.

The Center for Threat-Informed Defense recommends continuous adversary emulation as a way to validate whether real adversary behaviors are observable and detected in the environment. See [CTID – Continuous Emulation as Detection Validation](https://ctid.mitre.org/blog/2025/08/04/lessons-from-sharepoint-vulnerability-cve-2025-53770/).

That does not mean every rule needs a full red-team exercise. It means the test should represent the **behavioral claim** the detection is making.

### Shop requirements are local

External formats can show common metadata categories, but they do not define your organization's deployment policy.

For example, Sigma supports fields such as IDs, status, description, references, log source, false-positive notes, level, and tags. See [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html).

Your shop may require some, all, or different fields.

Use the **actual local list** from 4.8 and mark:
- met;
- missing;
- not applicable, if the local process permits it.

### Close the loop

A close-the-loop note should tell the nominator what happened to the need.

Useful dispositions include:

- **Shipped** – detection deployed.
- **Changed** – the original idea was modified; explain the meaningful change.
- **Sent back** – additional information is needed.
- **Retired / superseded** – the work or existing analytic no longer remains active.

Example:

> **Changed:** We kept the encoded-PowerShell behavior but removed the host-specific IOC so the analytic can detect similar execution across workstations. Positive and benign-control tests passed. Deployment follows the local change path.

That feedback is more useful than simply writing “done.”

## 2. Knowledge Check

1. What three categories of test expectation should be clear before deployment?
2. Why can a logically correct detection still fail operationally?
3. A Sigma field exists in the public specification. Does that automatically make it a mandatory local field?

## 3. Summary

Sound detection engineering tests the intended behavior, realistic non-target behavior, and the data path that makes the analytic possible.

External formats can inform design, but the organization's actual requirements list determines what is required locally.

Close the loop so the nominator knows whether the original defensive need was shipped, changed, sent back, or superseded.

**Next:** **4.3 – Nominations from SOC, Hunt, and CTI**.

## Supporting References

- [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html)
- [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html)
- [Sigma Filters](https://sigmahq.io/docs/meta/)
- [Center for Threat-Informed Defense – Continuous Emulation as Detection Validation](https://ctid.mitre.org/blog/2025/08/04/lessons-from-sharepoint-vulnerability-cve-2025-53770/)
