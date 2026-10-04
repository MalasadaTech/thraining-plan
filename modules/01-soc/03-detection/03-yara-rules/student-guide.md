# Module 1.3.3 – YARA Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.3.1 A / B / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 1a / 2b / 3c  
- Hunter: 1.3.3.1 B / C / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 2b / 3c / 4c  
- CTI: 1.3.3.1 A / B / B ; 1.3.3.2 1a / 2b / 3c ; 1.3.3.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret YARA structure, text/hex/regex patterns, and conditions.
2. Describe what a rule matches in its intended input.
3. Create or modify a basic file rule and explain file-versus-memory limits.

**Mapped Proficiency Items:**
- K: 1.3.3.1 – YARA rules
- T: 1.3.3.2 – Analyze an existing YARA rule and describe what it detects
- T: 1.3.3.3 – Create or modify a basic YARA rule

## Why This Matters

YARA examines content supplied to a scanner, such as a file or process memory. Understanding what bytes and conditions a rule tests helps you distinguish a content match from a filename, log entry, or conclusion about maliciousness.

## 1. Understanding the rule structure

A YARA rule has a name and a required `condition`. Optional `meta` entries describe it, while a `strings` section defines named text, hexadecimal, or regular-expression patterns used by the condition. Not every valid rule needs strings or metadata.

Text such as `"update.exe" ascii nocase` matches that content without case sensitivity. Hexadecimal `{ 4D 5A }` matches the bytes MZ. A regex such as `/update\.(exe|dll)/ nocase` allows alternatives. Conditions can combine patterns with AND/OR, positions such as `$mz at 0`, a count such as `#name >= 2`, or a file-size test.

The scanner must receive the relevant bytes. A network file log that names a hash is not the same input as an extracted file.

## 2. Reading a basic file rule

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

The rule matches files smaller than 5 MB whose first two bytes are MZ and whose content includes `update.exe`. It does not test the filesystem name. MZ is consistent with a DOS/PE-style header but alone does not validate a complete PE file. The string is intentionally simple for teaching and is not a distinctive malware-family signature.

A benign file could satisfy every condition. Explain a hit as a content match and use additional analysis to determine its significance.

## 3. Modifying a rule and choosing the input

To require two occurrences of the example name, replace `$name` with `#name >= 2` in the condition. This changes a measurable property of the content; it still does not make the rule a reliable maliciousness verdict.

File and process-memory scans have different semantics. `filesize` is undefined during a process-memory scan, and offsets in memory are virtual addresses rather than file-relative positions. Adapt and test a rule for its intended input instead of assuming a file rule will work unchanged in memory. The basic proposal here remains a file rule for review by Detection Engineering.

## Knowledge Check

1. What does the teaching rule match, and does the filename itself matter?
2. Modify the rule to require two occurrences of the name.
3. Why should the same rule not be assumed to work as intended on process memory?

## Summary

A YARA description explains the supplied input, patterns, and condition. Basic modifications should have predictable matching behavior, and file versus memory use requires attention to input semantics.

## Course Connections

Previous: [1.3.2 – Suricata Rules](../02-suricata-rules/student-guide.md)

Next: [1.3.4 – SIEM Rules](../04-siem-rules/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [YARA — Writing rules](https://yara.readthedocs.io/en/stable/writingrules.html)
- [YARA — Command-line input options](https://yara.readthedocs.io/en/stable/commandline.html)
