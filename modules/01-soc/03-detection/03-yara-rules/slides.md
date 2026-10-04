# Module 1.3.3 – YARA Rules

- Interpret YARA structure, text/hex/regex patterns, and conditions.
- Describe what a rule matches in its intended input.
- Create or modify a basic file rule and explain file-versus-memory limits.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

YARA examines content supplied to a scanner, such as a file or process memory. Understanding what bytes and conditions a rule tests helps you distinguish a content match from a filename, log entry, or conclusion about maliciousness.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Understanding the rule structure

YARA tests supplied content. The condition is required; metadata and strings are optional.

**Speaker notes:** Identify which blocks are optional and which condition is mandatory. Distinguish a string embedded in content from the object’s filename.

---

## Reading a basic file rule

The example matches MZ-prefixed files containing update.exe and smaller than 5 MB. It does not test the filename.

**Speaker notes:** Ask whether a benign file could match. Explain why MZ is a preliminary byte check rather than a full PE parser.

---

## Worked example — Reading a basic file rule

```yara
rule Training_Update_Marker
{
    meta:
        description = "Teaching example: MZ prefix and update.exe string"
    strings:
        $mz = { 4D 5A }
        $name = "update.exe" ascii nocase
    condition:
        $mz at 0 and $name and filesize < 5MB
}
```

**Speaker notes:** Ask whether a benign file could match. Explain why MZ is a preliminary byte check rather than a full PE parser. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Modifying a rule and choosing the input

Change the occurrence count to alter matching. File-size and offset semantics differ for process-memory scans.

**Speaker notes:** Have learners write the count condition and explain the changed behavior. Discuss memory semantics without adding a memory-acquisition exercise.

---

## Knowledge check

1. What does the teaching rule match, and does the filename itself matter?
2. Modify the rule to require two occurrences of the name.
3. Why should the same rule not be assumed to work as intended on process memory?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

A YARA description explains the supplied input, patterns, and condition. Basic modifications should have predictable matching behavior, and file versus memory use requires attention to input semantics.

Previous: [1.3.2 – Suricata Rules](../02-suricata-rules/student-guide.md)

Next: [1.3.4 – SIEM Rules](../04-siem-rules/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [YARA — Writing rules](https://yara.readthedocs.io/en/stable/writingrules.html)
- [YARA — Command-line input options](https://yara.readthedocs.io/en/stable/commandline.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
