# Instructor Guide – Module 1.3.3 – YARA Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.3.1 A / B / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 1a / 2b / 3c  
- Hunter: 1.3.3.1 B / C / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 2b / 3c / 4c  
- CTI: 1.3.3.1 A / B / B ; 1.3.3.2 1a / 2b / 3c ; 1.3.3.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

## Teaching Purpose

YARA examines content supplied to a scanner, such as a file or process memory. Understanding what bytes and conditions a rule tests helps you distinguish a content match from a filename, log entry, or conclusion about maliciousness.

## Learning Objectives

1. Interpret YARA structure, text/hex/regex patterns, and conditions.
2. Describe what a rule matches in its intended input.
3. Create or modify a basic file rule and explain file-versus-memory limits.

**Mapped Proficiency Items:**
- K: 1.3.3.1 – YARA rules
- T: 1.3.3.2 – Analyze an existing YARA rule and describe what it detects
- T: 1.3.3.3 – Create or modify a basic YARA rule

## Preparation and Scope

Use the [student guide](student-guide.md) and [slide source](slides.md). Review the worked example and expected answers before teaching. Use the supplied fictional evidence for discussion; no live system access or new lab is required. Learners should produce the requested basic modification and explain a match and nonmatch. Operational deployment follows the later Detection Engineering track and local change procedures.

Use the proficiency levels above to adjust prompting and explanation depth. The module focuses on its mapped knowledge and tasks; the linked next lesson develops the next step.

## Suggested Timing

| Section | Minutes | Focus |
|---|---|---|
| Opening | 2 | Connect the lesson to its purpose. |
| Explanation and worked example | 17 | Read the supplied evidence and demonstrate the reasoning. |
| Knowledge check and feedback | 6 | Complete the interpretation or modification tasks. |
| Summary and transition | 2 | Consolidate the result and connect the next lesson. |
| **Total** | **27** | |

## Detailed Teaching Notes

### 1. Understanding the rule structure

Identify which blocks are optional and which condition is mandatory. Distinguish a string embedded in content from the object’s filename.

**Key point to reinforce:** YARA tests supplied content. The condition is required; metadata and strings are optional.

### 2. Reading a basic file rule

Ask whether a benign file could match. Explain why MZ is a preliminary byte check rather than a full PE parser.

**Key point to reinforce:** The example matches MZ-prefixed files containing update.exe and smaller than 5 MB. It does not test the filename.

### 3. Modifying a rule and choosing the input

Have learners write the count condition and explain the changed behavior. Discuss memory semantics without adding a memory-acquisition exercise.

**Key point to reinforce:** Change the occurrence count to alter matching. File-size and offset semantics differ for process-memory scans.

## Knowledge Check — Answer Key

### 1. What does the teaching rule match, and does the filename itself matter?

**Expected answer:** It matches supplied file bytes beginning with MZ, containing update.exe, and smaller than 5 MB. The filesystem filename is not tested.

### 2. Modify the rule to require two occurrences of the name.

**Expected answer:** Use `$mz at 0 and #name >= 2 and filesize < 5MB` as the condition.

### 3. Why should the same rule not be assumed to work as intended on process memory?

**Expected answer:** filesize is undefined for a process scan and offsets refer to virtual addresses; input-specific adaptation and testing are needed.

## Assessment Guidance

Accept equivalent wording when it preserves the evidence and reasoning. For a query or rule modification, check the selected source, changed predicate or condition, and the learner’s explanation of what now matches. For an interpretation or routing decision, ask which supplied fact or classroom requirement supports it. Do not require an operational result from a system learners have not been given.

## Closing and Transition

A YARA description explains the supplied input, patterns, and condition. Basic modifications should have predictable matching behavior, and file versus memory use requires attention to input semantics.

Previous: [1.3.2 – Suricata Rules](../02-suricata-rules/student-guide.md)

Next: [1.3.4 – SIEM Rules](../04-siem-rules/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [YARA — Writing rules](https://yara.readthedocs.io/en/stable/writingrules.html)
- [YARA — Command-line input options](https://yara.readthedocs.io/en/stable/commandline.html)
