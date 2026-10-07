# 2.3 – Analytical Frameworks: Summary

**Module Type:** Subunit synthesis / end-state check — no new proficiency mapping  
**Estimated Time:** 5–10 minutes  

## What This Subunit Built

The three frameworks in this subunit give you complementary ways to organize adversary activity. **ATT&CK classifies supported behavior. The Diamond Model organizes entities and relationships. The Cyber Kill Chain organizes supported progression.**

The skill is not simply remembering the names of the frameworks. It is recognizing which analytical question each one helps answer, then keeping the framework tied to the evidence that justified the mapping.

## By This Point, You Should Be Able To

- explain the different analytical purpose of ATT&CK, the Diamond Model, and the Cyber Kill Chain;
- choose a framework based on the question you need to answer;
- map behavior to the most specific ATT&CK technique or sub-technique the evidence supports;
- populate Adversary, Capability, Infrastructure, and Victim from available evidence while leaving unresolved vertices unresolved;
- use the Cyber Kill Chain to describe supported attack progression without filling missing stages by assumption;
- preserve the evidence and uncertainty behind every framework mapping.

## How the Pieces Fit Together

| Analytical question | Framework | Useful output | Evidence boundary to preserve |
|---|---|---|---|
| **What behavior does the evidence demonstrate?** | MITRE ATT&CK | Supported tactic / technique / sub-technique tied to the observation | A plausible technique is not a supported technique until the behavior in its definition is demonstrated. |
| **What entities and relationships make up the event?** | Diamond Model | Adversary, Capability, Infrastructure, Victim, and the relationships among them | An unknown vertex can remain unknown; a vendor label or candidate relationship does not automatically establish identity. |
| **Where does this activity fit in intrusion progression?** | Cyber Kill Chain | Supported stage or stages of the intrusion | A process, download, or network event needs surrounding context before it proves a particular stage. |

One piece of evidence may appear in all three views, but the framework does not change what the evidence itself says.

## Integrated A12 Example

Consider several facts already used in the A12 training scenario:

- `wscript.exe` launches encoded PowerShell on **WS-JLEE**;
- the update domain and `203.0.113.88` are associated with the activity;
- the affected victim includes **WS-JLEE** / `jlee`;
- the adversary identity remains unresolved.

Each framework organizes those facts differently.

### ATT&CK

The observed PowerShell behavior supports **T1059.001 – PowerShell** because the process evidence directly shows PowerShell execution.

The mapping remains tied to the process observation. It does not, by itself, prove what the PowerShell process did afterward.

### Diamond Model

The same activity can populate parts of the Diamond:

- **Victim:** `WS-JLEE` / `jlee` / DYA
- **Capability:** encoded PowerShell and other supported tooling or behavior
- **Infrastructure:** the supported update-domain infrastructure
- **Adversary:** unresolved at the level currently supported by the evidence

The incomplete Adversary vertex is useful because it shows where the analysis has less support.

### Cyber Kill Chain

The process chain alone does not tell you exactly which Kill Chain stage the activity represents. Stage assignment depends on the role the behavior played in the surrounding intrusion.

This is why the Kill Chain lesson asks you to use context rather than translating a process name directly into a stage.

## A Practical Selection Rule

When you are deciding which framework to use, start with the question:

- **Behavior?** Start with ATT&CK.
- **Entities and relationships?** Start with the Diamond Model.
- **Progression?** Start with the Cyber Kill Chain.

You may use more than one when the intelligence problem needs more than one view.

## Check Your Understanding

Ask yourself:

1. If two analysts map the same PowerShell event differently, can I explain which ATT&CK definition the evidence actually supports?
2. If the infrastructure and victim are well established but the actor is not, can I leave the Diamond adversary vertex unresolved and explain why?
3. If I observe a file download but do not know whether the payload executed or persisted, can I explain why I should not automatically call the activity Installation?
4. Can I explain why using three frameworks on one activity does not create three independent pieces of evidence?

If you can answer those questions clearly, you have the mental model this subunit is intended to build.

## Where This Leads Next

The next subunit, **2.4 CTI Tools and Platforms**, shifts from organizing evidence to retrieving and examining it in the systems analysts use for CTI work.

The framework lessons give you analytical questions to ask. The platform lessons help you obtain and inspect information that may answer those questions. The same evidence-first rule still applies: **the platform returns information; the analyst decides what that information supports.**

**Next:** [2.4 – CTI Tools and Platforms: Introduction](../04-platforms/intro.md).
