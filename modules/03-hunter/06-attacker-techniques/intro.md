# 3.6 – Attacker Techniques for Hunting: Introduction

**Module Type:** Subunit advance organizer — no new proficiency mapping  
**Estimated Time:** 5–10 minutes

## Why This Subunit Matters

Technique knowledge helps hunters turn broad adversary behaviors into concrete, observable search ideas. The useful level is specific enough to map to telemetry and distinguish suspicious patterns from the large amount of legitimate activity that may use the same mechanism.

## Connect to What You Already Know

The framework-application lesson showed how ATT&CK and other models can structure a hunt. This subunit applies that thinking to technique families that frequently produce huntable host evidence.

## What You Will Learn

| Lesson | What it contributes |
|---|---|
| **3.6.1 – Persistence** | Recognize persistence mechanisms and narrow them into observable patterns suitable for hunting. |
| **3.6.2 – Privilege Escalation** | Recognize privilege-escalation behaviors and the host context needed to search for them meaningfully. |
| **3.6.3 – Hunt-Specific Technique Development** | Turn a named technique into a unique pattern, bounded scope, and evidence-backed hunt line. |

## What to Watch For

- Move from a broad tactic or technique name to a concrete observable pattern.
- Use environment and baseline context to distinguish common administrative behavior from a hunt-worthy pattern.
- Keep the hunt scope narrow enough that the result answers a question rather than producing an unbounded list of matches.

## Expected End State

By the end of this subunit, you should be able to:

- identify concrete persistence and privilege-escalation behaviors that can produce hunt leads;
- translate a technique into a specific observable pattern and telemetry requirement;
- bound the search by scope, time, assets, users, or other relevant context;
- explain why hunting an entire tactic is usually less useful than testing a specific behavioral hypothesis.

## How to Preview This Subunit

Read this introduction, then skim the [3.6 Summary](summary.md). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

**Next:** [3.6.1 – Persistence](01-persistence/student-guide.md)
