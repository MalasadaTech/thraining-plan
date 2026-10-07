# 1.3 – Detection Rules: Introduction

**Module Type:** Subunit advance organizer — no new proficiency mapping  
**Estimated Time:** 5–10 minutes

## Why This Subunit Matters

SOC analysts encounter detection logic written for different evidence layers. Understanding the rule language helps you explain why an alert fired, recognize what data the rule depends on, and make bounded changes without confusing a match with a completed investigation.

## Connect to What You Already Know

The endpoint and Zeek subunits established the evidence that detections can evaluate. This subunit shows how several common rule types express conditions over that evidence.

## What You Will Learn

| Lesson | What it contributes |
|---|---|
| **1.3.1 – SIGMA Rules** | Read and modify portable detection logic that describes log-event conditions. |
| **1.3.2 – Suricata Rules** | Read and modify network-signature logic over packet or protocol evidence. |
| **1.3.3 – YARA Rules** | Read and modify pattern-matching logic for files, memory, or other scanned content. |
| **1.3.4 – SIEM Rules** | Read and modify analytic logic in the local query/detection environment. |

## What to Watch For

- Identify the evidence layer before interpreting the rule.
- Separate rule conditions from the investigative conclusion that follows a match.
- When modifying a rule, understand which condition changes and what new activity the change would include or exclude.

## Expected End State

By the end of this subunit, you should be able to:

- explain what evidence each rule family is designed to evaluate;
- read the main parts of SIGMA, Suricata, YARA, and SIEM detection logic;
- describe why a rule matched without equating the match with maliciousness;
- make or assess a simple rule change while preserving its intended detection purpose.

## How to Preview This Subunit

Read this introduction, then skim the [1.3 Summary](summary.md). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

**Next:** [1.3.1 – SIGMA Rules](01-sigma-rules/student-guide.md)
