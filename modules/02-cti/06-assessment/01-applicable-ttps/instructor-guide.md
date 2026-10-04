# Instructor Guide – Module 2.6.1 – Extracting Applicable TTPs from Intelligence Reports

**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Purpose

Teach learners to extract behavior from reporting, assess **applicability**, and then assess **visibility separately**.

Reference:
- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
- [T1059.001 – PowerShell](https://attack.mitre.org/techniques/T1059/001/)

## Critical Teaching Distinction

Do not teach:

> no telemetry = not applicable

Teach:

> applicability asks whether the behavior can occur here; visibility asks whether we can observe it.

An applicable-but-invisible TTP becomes a telemetry/collection gap.

## Suggested Timing

| Part | Time |
|---|---:|
| TTP vs IOC | 4 min |
| Behavior extraction | 5 min |
| Applicability | 5 min |
| Visibility | 5 min |
| Knowledge check | 4 min |

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Copies every ATT&CK ID from the report. | Require the procedure/how behind each retained item. |
| Treats lack of visibility as non-applicable. | Separate platform/path from telemetry. |
| Keeps platform-specific behavior for a platform not present. | Ask what local asset can execute the behavior. |
| Re-maps ATT&CK IDs in this lesson. | If mapping is disputed, refer back to 2.3.1. |

## Knowledge Check – Answer Key

1. Applicability describes whether the behavior can occur here; visibility describes whether current telemetry can observe it.
2. Yes, it is applicable because Windows is present. Record the missing command-line/PowerShell telemetry as a visibility gap.
3. Mark it not applicable to the current environment because the required platform is absent.

## Instructor References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
- [T1059.001 – PowerShell](https://attack.mitre.org/techniques/T1059/001/)
