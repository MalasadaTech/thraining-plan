# Module 2.6.1 – Extracting Applicable TTPs from Intelligence Reports

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.6.1 B / C / C ; 2.6.1.1 3c / 4c / 4d  
- Hunter: 2.6.1 B / C / C ; 2.6.1.1 3c / 4c / 4d  
- SOC: 2.6.1 A / B / B ; 2.6.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Extract concrete adversary behaviors from an intelligence report rather than copying an IOC list or unsupported ATT&CK table.
2. Evaluate whether each behavior is **applicable to the environment**, then assess **visibility separately** so a telemetry gap is not mistaken for non-applicability.

**Mapped Proficiency Items:**
- K: 2.6.1 – Extracting applicable TTPs from intelligence reports
- T: 2.6.1.1 – Extract applicable TTPs from an intelligence report

## 1. Key Concepts

A report may contain dozens of ATT&CK IDs, indicators, malware names, and narrative claims. The analyst's job is to extract the behaviors that matter to the local environment.

A **TTP** describes how an adversary operates. A hash, IP address, or domain is an observable/indicator, not a TTP.

ATT&CK is the reference vocabulary for the behaviors in this lesson:
- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
- [T1059.001 – PowerShell](https://attack.mitre.org/techniques/T1059/001/)

### Start with the behavior, not the printed ID

A report line such as:

> The malware launched encoded PowerShell with `-enc`.

contains a concrete procedure.

If the report also labels it **T1059.001**, the analyst can verify that mapping against ATT&CK. If the vendor's ID is missing or questionable, the mapping exercise belongs to 2.3.1.

This lesson asks a different question:

> **Does this behavior apply to our environment?**

### Applicability and visibility are separate filters

This course treats them as two distinct questions.

#### 1. Applicability

A behavior is applicable when the environment contains the systems, services, access paths, or conditions needed for the behavior to occur.

Useful checks include:

- **Platform:** Do we run the affected operating system, application, identity system, cloud service, or device type?
- **Exposure / path:** Can the behavior reach or execute against something we actually operate?
- **Preconditions:** Are the required features or configuration present?

#### 2. Visibility

If the behavior is applicable, ask whether current telemetry can observe it.

Visibility can be:

- **Visible** – existing telemetry can support hunting/detection.
- **Partially visible** – some evidence exists but important fields are missing.
- **Not currently visible** – the behavior can happen here, but the required telemetry is absent.

A visibility gap does **not** make the TTP non-applicable.

It means:

> applicable behavior + collection/telemetry gap

That distinction prevents the organization from ignoring a real exposure merely because current tools cannot see it.

### Classroom environment

DYA is a law firm with Windows workstations. `WS-JLEE` is a Windows user workstation.

Example:

**Report behavior:** encoded PowerShell / T1059.001  
**Applicability:** yes — Windows workstations are present.  
**Visibility:** assess separately based on available process/script/PowerShell telemetry.

MITRE lists PowerShell as a Windows technique under Execution. See [T1059.001](https://attack.mitre.org/techniques/T1059/001/).

Example:

**Report behavior:** destructive action against an OT historian appliance  
**Applicability:** no, if DYA does not operate OT historian systems.  
**Visibility:** not evaluated because the required platform is absent.

### A simple extraction table

| Report behavior | ATT&CK reference | Applicable? | Why? | Visibility |
|---|---|---|---|---|
| Encoded PowerShell | T1059.001 | Yes | Windows endpoints present | Visible / partial / gap |
| OT historian wipe | Report-specific | No | No OT historian environment | N/A |
| ESXi-only behavior | Relevant ATT&CK technique | No if no ESXi | Required platform absent | N/A |

This keeps three decisions separate:
1. What behavior did the report describe?
2. Can it occur here?
3. Can we currently observe it?

### Validate Vendor ATT&CK Mappings Against the Reported Behavior

A vendor's technique list can be useful, but the local extract should remain tied to the report's actual procedures.

If the report lists an ID with no described behavior, mark it for validation rather than treating it as a finished local TTP extract.

The most useful output is a short set of behaviors with clear applicability and visibility status—not the longest possible ATT&CK list.

## 2. Knowledge Check

1. Why are applicability and visibility separate questions?
2. Encoded PowerShell appears in a report. DYA runs Windows, but current telemetry cannot capture PowerShell command lines. Is the TTP applicable? What else should be recorded?
3. A report describes an ESXi-only technique, and DYA has no ESXi systems. How should it be handled?

## 3. Summary

Extract behaviors from the report first.

Then ask **applicability**: can this behavior occur in the environment?

Only after that ask **visibility**: can current telemetry observe it?

A visibility gap is not the same thing as non-applicability. Keep the distinction visible so collection gaps can be addressed instead of silently removing relevant behavior from the intelligence package.


## Supporting References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
- [T1059.001 – PowerShell](https://attack.mitre.org/techniques/T1059/001/)

**Next:** [2.6.2 – Threat Relevance and Organizational Impact](../02-relevance-impact/student-guide.md).
