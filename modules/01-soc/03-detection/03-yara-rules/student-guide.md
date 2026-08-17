# Module 1.3.3 – YARA Rules

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.3.1 A / B / C · 1.3.3.2 2b / 3c / 4c · 1.3.3.3 1a / 2b / 3c  
- Hunter: 1.3.3.1 B / C / C · 1.3.3.2 2b / 3c / 4c · 1.3.3.3 2b / 3c / 4c  
- CTI: 1.3.3.1 A / B / B · 1.3.3.2 1a / 2b / 3c · 1.3.3.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of a YARA rule and its structure (`meta`, `strings`, `condition`).
2. Read common string and condition usage, including ASCII, hex, and regex.
3. Say how YARA is used against **files** and against **memory** (where your site scans).
4. Analyze an existing YARA rule and state what it detects.
5. Create or modify a **basic** YARA rule (propose only).

**Mapped Proficiency Items:**
- K: 1.3.3.1 – YARA rules
- T: 1.3.3.2 – Analyze an existing YARA rule and describe what it detects
- T: 1.3.3.3 – Create or modify a basic YARA rule

---

## 1. Key Concepts

### 1.1 Purpose and structure

**YARA** matches **byte patterns** in a file or in process memory. It is not SIGMA (log detections) and not Suricata (network signatures).

You scan something you already have: an extracted file (**1.2.7**), a disk path, or a memory image your site collects. This lesson does **not** teach how to dump memory or how to write malware.

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

| Block | What it is |
|-------|------------|
| `rule Name` | Identifier. No spaces. |
| `meta` | Human notes (`description`, `author`). Not part of the match. |
| `strings` | Named patterns (`$mz`, `$s1`, …) |
| `condition` | Boolean over those strings (and `filesize`, `uint16(0)`, …) |

A rule with strings and no condition (or `condition: true`) is not a useful proposal.

| This lesson | Other |
|-------------|-------|
| Pattern match on bytes | Host file *event* — **1.1.3** |
| Scan a file Zeek extracted | `files` log fields — **1.2.7** |
| Mention of memory scan | Memory-acquisition how-to — out of scope |

### 1.2 Strings, conditions, files vs memory

**Strings and conditions (outline b)**

| Idea | Example | Meaning |
|------|---------|---------|
| ASCII | `$s = "update.exe" ascii nocase` | Text, optional case-insensitive |
| Hex | `$mz = { 4D 5A }` | Raw bytes. `$mz at 0` = MZ at start of file |
| Regex | `$r = /checkin\.[a-z0-9-]+/ nocase` | Variation. Easy to over-match |
| Combine | `uint16(0) == 0x5A4D and $s` | PE-ish header **and** a string |
| Count | `#s >= 2` | String appears at least twice |

**Matching techniques (outline c)** are the same three words as Suricata — different syntax. Hex in YARA is `{ 4D 5A }`, not `content:"|4d 5a|"`. Regex is `/pattern/` as a string, not `pcre:`.

**Files vs memory (outline d)**

| Target | What you scan | Condition habit |
|--------|---------------|-----------------|
| **File** | Bytes on disk or an extracted object (`fuid` / path) | `uint16(0) == 0x5A4D`, `filesize < 2MB`, `$s` |
| **Memory** | Process address space your platform already exposes | Often **drop** `at 0` / `filesize` — headers may not sit at offset 0 in a dump |

If your tenant does not do memory YARA, write “memory scan not used here” and stay on files. Do not invent a dump.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Header check **and** a distinctive string | `$mz at 0` alone (every PE) |
| `ascii nocase` on a name you can explain | Regex that matches half the internet |
| File rule with `filesize` cap | File-only conditions on a memory scan |
| Description matches the condition | `meta` says “beacon” but condition is only `MZ` |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Useful File Rule (Expected)

```
rule BuildingC_Train_UpdateExeName
{
    meta:
        description = "Training: PE with update.exe string"
    strings:
        $mz = { 4D 5A }
        $name = "update.exe" ascii nocase
    condition:
        $mz at 0 and $name and filesize < 5MB
}
```

**What it detects:** A **file** that starts with MZ and contains `update.exe`, under 5 MB. Fits the **1.2.7** Example 2 transfer *if you scan that extracted object*.

**Interpretation:** Expected *as a rule*: header + distinctive string + size cap. Not a conviction. Many legitimate updaters contain that name.

### Example 2: MZ Only (Lead)

```
rule BuildingC_Train_AnyPE
{
    strings:
        $mz = { 4D 5A }
    condition:
        $mz at 0
}
```

**What it detects:** Every DOS/PE file. Notepad matches.

**Interpretation:** Lead **about the rule**. Hex is used correctly; the **condition** is too broad. Add a string, hash-adjacent token, or path context outside YARA (SIEM / files log).

### Example 3: Memory vs File (Lead if Misapplied)

```
rule BuildingC_Train_NightowlString
{
    meta:
        description = "Training: nightowl checkin string"
    strings:
        $s = "checkin.nightowl-updates.net" ascii nocase
    condition:
        $s
}
```

**What it detects:** That hostname string **anywhere** in the scanned bytes — a file **or** memory, depending on the scanner.

**Interpretation:** Useful string. Lead if you attach `filesize` / `$mz at 0` and then run it **only in memory** (those file conditions fail or lie). For a **file** scan of an HTTP extract, add `$mz at 0` if you only want executables. For **memory**, leave the string and drop `at 0`. Say which target you mean.

---

## 3. Hands-On Exercise

**Objective:** Practice reading YARA and proposing a basic rule.

**Instructions:**

1. Summarize each example: what it matches, expected vs lead (as a *rule*).
2. **Analyze** this rule. Strings, condition, file vs memory, what fires:

```
rule BuildingC_Train_InvoiceJpgName
{
    strings:
        $mz = { 4D 5A }
        $n = "invoice.jpg" ascii nocase
    condition:
        $mz at 0 and $n
}
```

3. **Modify** Example 2 **or create** a basic file rule that requires MZ at 0 **and** one distinctive ASCII string from this unit’s stories (`update.exe` or `invoice.jpg` or `nightowl-updates`). Include `meta.description` and a `filesize` cap.
4. In two sentences: where would you run it (extracted **file** from **1.2.7**, disk path, or memory — pick one your site has) and what you would **not** add for that target.

**Expected Outcome:**
- Three summaries
- One analysis
- One basic rule (create or modify)
- One file-vs-memory note

---

## 4. Knowledge Check

1. What is YARA for, and how is it different from SIGMA and Suricata?
2. What belongs in `meta`, `strings`, and `condition`?
3. Show the YARA shape of ASCII, hex, and regex.
4. How does a **file** scan differ from a **memory** scan in what you put in the condition?
5. Who deploys the rule, and why is “MZ at 0 only” a poor proposal?

---

## 5. Summary

- YARA = byte patterns in a file or in memory. Structure: meta + strings + condition.
- ASCII `{text}`, hex `{ 4D 5A }`, regex `/pattern/` — same three techniques as Suricata, different syntax.
- File rules may use `at 0` and `filesize`. Memory rules often must not.
- SOC proposes (1a / 2b / 3c). Next: SIEM rules (**1.3.4**).

---

## 6. References & Further Reading

- YARA documentation (writing rules) — as used in class
- Related modules:
  - 1.1.3 – File system activity
  - 1.2.7 – Files engine
  - 1.3.2 – Suricata rules (previous)
  - 1.3.4 – SIEM rules (next)
