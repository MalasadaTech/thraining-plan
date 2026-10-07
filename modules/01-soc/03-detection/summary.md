# 1.3 – Detection Rules: Summary

**Module Type:** Subunit synthesis / end-state check — no new proficiency mapping  
**Estimated Time:** 5–10 minutes

## What This Subunit Built

**Evidence source → rule conditions → match → investigation → tuning or change when justified**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

## By This Point, You Should Be Able To

- explain what evidence each rule family is designed to evaluate;
- read the main parts of SIGMA, Suricata, YARA, and SIEM detection logic;
- describe why a rule matched without equating the match with maliciousness;
- make or assess a simple rule change while preserving its intended detection purpose.

## How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **1.3.1 – SIGMA Rules** | Read and modify portable detection logic that describes log-event conditions. |
| **1.3.2 – Suricata Rules** | Read and modify network-signature logic over packet or protocol evidence. |
| **1.3.3 – YARA Rules** | Read and modify pattern-matching logic for files, memory, or other scanned content. |
| **1.3.4 – SIEM Rules** | Read and modify analytic logic in the local query/detection environment. |

## Check Your Understanding

Ask yourself:

1. Why does knowing the evidence layer matter before you interpret a detection rule?
2. What is the difference between explaining why a rule matched and deciding what the matched activity means?
3. When you change one condition in a rule, what should you consider about the activity the rule will now include or exclude?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

## Where This Leads Next

The next learning unit is **1.4 – Alert Investigation and Assessment: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

**Next:** [1.4 – Alert Investigation and Assessment: Introduction](../04-alerts/intro.md)
