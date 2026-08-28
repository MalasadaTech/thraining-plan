# Module 1.3.3 – YARA Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.3.1 A / B / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 1a / 2b / 3c  
- Hunter: 1.3.3.1 B / C / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 2b / 3c / 4c  
- CTI: 1.3.3.1 A / B / B ; 1.3.3.2 1a / 2b / 3c ; 1.3.3.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what a YARA rule is for, name its blocks, and when it runs on a file vs memory.
2. Read an existing rule and say what it detects; propose a **basic** create or modify.

**Mapped Proficiency Items:**
- K: 1.3.3.1 – YARA rules
- T: 1.3.3.2 – Analyze an existing YARA rule and describe what it detects
- T: 1.3.3.3 – Create or modify a basic YARA rule

---

## 1. Key Concepts

SOC analysts match **byte patterns** on a file they already have, or on memory the shop already scans. A log can name a file, a hash, or a URI. It does not show the bytes inside. That is the job in this lesson: read a **YARA** rule so you can say what would hit those bytes, and propose a basic create or modify. **1.3.2** was Suricata on the wire. This lesson is the file (or memory). You do **not** deploy the rule. You do **not** dump memory. How detections run as a service is **4.x**.

**YARA** matches **byte patterns** in a file or in process memory. It is not SIGMA and not Suricata. It is not a SIEM query language.

```
rule RuleName
{
    meta:
        description = "..."
    strings:
        $a = "..."
    condition:
        $a
}
```

| Idea | What to read |
|------|----------------|
| **Purpose / structure** | `rule` name, `meta` (notes, not the match), `strings`, `condition`. A strings block with no real condition is not a useful proposal. |
| **Strings and condition** | Named patterns plus boolean (`and`, `or`, `filesize`, `uint16(0) == 0x5A4D`, `#s >= 2`). `$mz at 0` is the same *idea* as that `uint16` check: MZ at the start of the file. |
| **ASCII / hex / regex** | ASCII = `"update.exe" ascii nocase`. Hex = `{ 4D 5A }` (`MZ`) — not Suricata `content:"\|4d 5a\|"`. Regex = `/update\.(exe\|dll)/ nocase`. Regex is easy to over-match. |
| **Files vs memory** | **File** — disk or a saved extract. `at 0` and `filesize` can apply. **Memory** — a process the shop already scans. Drop `filesize` (it does not apply there, so the rule will not match). Drop `at 0` for a PE header; the image may not sit at the start of the region. If your shop does not scan memory, say so and stay on files. |

**What good looks like:**

- Analyze: name the strings, the condition, file vs memory, and what would fire. `{ 4D 5A } at 0` alone matches every PE, including Notepad.
- Given:

```
rule Train_UpdateExe
{
    meta:
        description = "PE that contains update.exe"
    strings:
        $mz = { 4D 5A }
        $name = "update.exe" ascii nocase
    condition:
        $mz at 0 and $name and filesize < 5MB
}
```

**What it detects:** a **file** that starts with MZ and contains `update.exe`, under 5 MB. That can fit a PE extract of `update.exe` (**1.2.7**) **if you scan those bytes**. It does not match a `files` log line. It is not a conviction.

- Modify / create: a **basic** file rule with one distinctive string **and** a header or size check. Tightening “MZ only” by adding `update.exe` is a modify. SOC **proposes**. DE reviews.

---

## 2. Knowledge Check

1. YARA is a SIEM query language. True or false?
2. The given rule above — what does it detect, in one sentence?
3. Why is `{ 4D 5A } at 0` alone a poor proposal?

---

## 3. Summary

YARA is meta + strings + condition. ASCII, hex, and regex. File rules may use `at 0` and `filesize`. Memory often must not. You propose. You do not deploy.

**Next:** **1.3.4** SIEM rules.

---

## 4. Related modules

- 1.3.2 – Suricata rules (previous)
- 1.2.7 – Files engine
- 1.3.4 – SIEM rules
- 4.x – How detections run as a service
