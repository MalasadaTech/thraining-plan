# Instructor Guide – Module 2.3.1 – MITRE ATT&CK for CTI Analysis and Reporting

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.3.1 B / C / C ; 2.3.1.1 3c / 4c / 4c  
- Hunter: 2.3.1 B / C / C ; 2.3.1.1 3c / 4c / 4c  
- SOC: 2.3.1 A / B / B ; 2.3.1.1 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Teach learners to map reported or observed behavior to ATT&CK using the evidence as the starting point.

The central teaching habit is **evidence → behavior → ATT&CK mapping**. Learners should not begin with an ID and search the case for something that sounds close.

This is the CTI application of ATT&CK. The shared-floor lesson introduced the framework; this module teaches how an analyst creates a defensible mapping in a report.

## Learning Objectives

1. Map behavior from a report or activity set to an ATT&CK tactic and the most specific technique or sub-technique supported by the evidence.
2. Explain the evidence for the mapping and distinguish it from a nearby ATT&CK choice that would require evidence the product does not contain.

**Mapped Proficiency Items:**
- K: 2.3.1 – MITRE ATT&CK for CTI analysis and reporting
- T: 2.3.1.1 – Map activity or reports to MITRE ATT&CK

## Suggested Timing

| Part | Time | Purpose |
|---|---:|---|
| Introduction | 3 min | Establish evidence-first mapping. |
| ATT&CK elements | 5 min | Tactic, technique, sub-technique, procedure/evidence. |
| PowerShell example | 5 min | Map T1059.001 precisely. |
| File-transfer example | 5 min | Show when T1105 is and is not supported. |
| Knowledge check | 4 min | Apply evidence boundaries. |
| Summary | 2 min | Reinforce reusable mapping format. |
| **Total** | **24 min** | |

## Detailed Teaching Notes

### Start with the evidence

Use `wscript.exe` → `powershell.exe -enc`.

Ask learners what behavior is directly observable before asking for an ID.

The correct path is:
1. PowerShell execution is visible.
2. ATT&CK identifies that behavior as T1059.001.
3. Execution is the applicable tactic for this mapping.

Reference: [MITRE ATT&CK – T1059.001](https://attack.mitre.org/techniques/T1059/001/).

### Teach specificity without overfitting

If PowerShell is explicit, prefer the PowerShell sub-technique over the broader interpreter technique. If the specific interpreter is not known, do not invent it just to produce a more detailed ID.

### Use T1105 to teach evidence quality

MITRE defines T1105 as transferring tools or files from an external system into a compromised environment.

Reference: [MITRE ATT&CK – T1105](https://attack.mitre.org/techniques/T1105/).

A request path named `/update.exe` is suggestive but does not alone prove successful transfer. A completed response, resulting file, or other corroborating evidence makes the mapping stronger.

### Keep separate behaviors separate

PowerShell execution and tool transfer can coexist in the same activity set. They remain two behaviors with two mappings.

Do not collapse the entire attack narrative into one ATT&CK ID.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Maps future behavior that is not in the evidence. | Ask what event or sentence demonstrates the behavior now. |
| Copies a vendor ATT&CK list without checking it. | Require one evidence citation for each mapped behavior. |
| Uses a parent technique when the sub-technique is explicit. | Ask whether the evidence identifies the specific implementation. |
| Treats an HTTP request as confirmed transfer. | Ask what proves the file actually moved into the environment. |

## Knowledge Check – Answer Key

1. **PowerShell example:** Execution / **T1059.001 PowerShell**, citing the PowerShell process and `-enc` command line.
2. **T1105 evidence:** A response/file creation/download artifact or other evidence establishing external-to-victim file transfer.
3. **Specificity:** The mapping should preserve the most detail the evidence actually supports without inventing detail the product does not contain.

## Instructor References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [T1059.001 – PowerShell](https://attack.mitre.org/techniques/T1059/001/)
- [T1105 – Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)
