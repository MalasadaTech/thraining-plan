# Module 3.6.3 – Hunt for a Specific Persistence or Privilege-Escalation Technique

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.3 3c / 4c / 4d  
- SOC: 3.6.3 1a / 1a / 2b  
- CTI: 3.6.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Turn one named persistence or privilege-escalation technique into a bounded, telemetry-backed hunt.
2. Distinguish the ATT&CK technique from the **procedure-level pattern** that makes the hunt selective.

## Mapped Proficiency Item

- T: 3.6.3 – Hunt for specific persistence or privilege escalation techniques

## 1. Key Concepts

“Hunt persistence” is too broad.

A useful hunt names:

1. **Technique** – the behavioral category.
2. **Procedure/pattern** – what this threat actually did, or the behavior variant you intend to test.
3. **Scope** – population, time, telemetry.
4. **Expected evidence** – fields/events that would make a hit reviewable.

### A12 example

**Technique**
> [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)

**Relevant tactic/context**
> Persistence

**Observed procedure**
> HKCU Run value `Updater` → `%TEMP%\update.exe`

**Exact-observed hunt**
> Search user workstations for Run value `Updater` or the exact target path during the scoped window.

**Behavior-broadened hunt**
> Search for newly created/modified Run values that launch executables from user-writable Temp locations, then prioritize rare value names, unusual creators, unsigned files, and hosts related to A12.

The first search has high specificity but may miss variants.

The second can find variants but produces more benign candidates.

A mature hunt can use both layers.

### Wrong-class avoidance

A task that runs as SYSTEM is not automatically “privilege escalation.” The hunt should require evidence that the actor moved from a lower context to a higher one and, if naming a specific escalation method, evidence supporting that method.

### Hunt line

A concise hunt line can be:

> **T1547.001 / Persistence** — Windows user workstations, previous 14 days, registry + file telemetry; search exact `Updater → %TEMP%\update.exe` first, then broaden to rare Run values launching from user-writable Temp paths.

That hunt line is specific enough to **prepare an executable search**, but writing the line is not the same as executing the mapped task.

To demonstrate `3.6.3`, run both the exact-observed and behavior-broadened layers in [Practical E of the Hunt Execution Practical](../../02-methodology/01-hunt-types/hunt-execution-practical.md). Record the query/filter, returned hosts, benign near-neighbor, gaps, and bounded finding.

## 2. Knowledge Check

1. What is the difference between an ATT&CK technique and the procedure-level pattern used by the hunt?
2. What trade-off exists between exact-observed and behavior-broadened hunts?
3. Write an A12 T1547.001 hunt line with scope and telemetry.

## 3. Summary

Hunt one named technique through a procedure-level pattern.

Start exact when intelligence gives you exact evidence; broaden deliberately when you want variants. Keep the scope and required telemetry explicit.

**Next:** [3.6 – Attacker Techniques for Hunting Summary](../summary.md).

## Supporting Reference

- [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)
