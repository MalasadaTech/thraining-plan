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

SOC analysts **read** a byte-pattern rule and **propose** a basic one. **1.3.2** was Suricata (the wire). This hour is YARA. You scan a file you already have (**1.2.7**) or memory your site already collects. You do **not** deploy it. You do **not** dump memory.

**YARA** matches **byte patterns** in a file or in process memory. It is not SIGMA and not Suricata.

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
| **Purpose / structure** | `rule` name, `meta` (notes, not the match), `strings`, `condition`. Strings with no real condition is not a useful proposal |
| **Strings and condition** | Named patterns + boolean (`and`, `or`, `filesize`, `uint16(0)`, `#s >= 2`) |
| **ASCII / hex / regex** | ASCII = `"update.exe" ascii nocase`. Hex = `{ 4D 5A }` (`MZ`). Regex = `/update\\.(exe\|dll)/ nocase`. Same three techniques as Suricata, different syntax |
| **Files vs memory** | **File** — disk or a Zeek extract. `uint16(0) == 0x5A4D` and `filesize` can apply. **Memory** — drop `at 0` / `filesize`; headers may not sit at offset 0. If your shop does not scan memory, say so and stay on files |

**What good looks like:**

- Analyze: name the strings, the condition, file vs memory, and what would fire. `MZ at 0` alone matches every PE.
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

**What it detects:** a **file** that starts with MZ and contains `update.exe`, under 5 MB. Fits the **1.2.7** extract *if you scan that object*. Not a conviction.

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
