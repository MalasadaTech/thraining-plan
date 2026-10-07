# 1.1 – Endpoint Activity: Summary

**Module Type:** Subunit synthesis / end-state check — no new proficiency mapping  
**Estimated Time:** 5–10 minutes

## What This Subunit Built

**Host question → relevant event type → field interpretation → cross-event context → bounded conclusion**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

## By This Point, You Should Be Able To

- identify the major endpoint evidence types and the questions each can answer;
- read common process, file, network, registry, image, and driver-load fields in context;
- connect related endpoint events without overstating what any one event proves;
- recognize when missing telemetry limits the conclusion.

## How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **1.1.1 – Endpoint Activity** | Build the map of endpoint evidence types and the questions they can answer. |
| **1.1.2 – Process Activity** | Interpret process creation, parent-child relationships, command lines, users, and execution context. |
| **1.1.3 – File System Activity** | Interpret file creation, modification, deletion, paths, and hashes. |
| **1.1.4 – Network Activity (Endpoint)** | Connect outbound or inbound network activity to the host and, where available, the initiating process. |
| **1.1.5 – Registry Activity** | Interpret registry changes as host configuration and persistence evidence when the relevant keys and values are present. |
| **1.1.6 – Image and Driver Load Activity** | Interpret loaded modules and drivers as additional execution and trust context. |

## Check Your Understanding

Ask yourself:

1. If you need to know which process opened a network connection, which endpoint evidence is most useful?
2. Why is a file hash useful context without automatically proving that the file is malicious?
3. What shared context can help you determine whether process, file, and registry events belong to the same activity?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

## Where This Leads Next

The next learning unit is **1.2 – Zeek Network Evidence: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

**Next:** [1.2 – Zeek Network Evidence: Introduction](../02-zeek/intro.md)
