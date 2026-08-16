# Module 1.3.4 – SIEM Rules

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.4.1 A / B / C · 1.3.4.2 2b / 3c / 4c · 1.3.4.3 1a / 2b / 3c  
- Hunter: 1.3.4.1 B / C / C · 1.3.4.2 2b / 3c / 4c · 1.3.4.3 2b / 3c / 4c  
- CTI: 1.3.4.1 A / B / B · 1.3.4.2 1a / 2b / 3c · 1.3.4.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the structure of a SIEM detection rule / correlation search (name, table, logic, window, output).
2. Turn log fields into a detection (and apply regex / wildcards).
3. Analyze an existing SIEM rule and state what it detects.
4. Create a **basic** SIEM detection from **log fields** or from a **SIGMA** rule (propose only).

**Mapped Proficiency Items:**
- K: 1.3.4.1 – SIEM rules
- T: 1.3.4.2 – Analyze an existing SIEM rule and describe what it detects
- T: 1.3.4.3 – Create a basic SIEM detection rule from log fields or a SIGMA rule

---

## 1. Key Concepts

### 1.1 Structure of a SIEM detection / correlation search

A **SIEM rule** is a saved search (or analytics / correlation rule) that runs on ingested logs and can create an **alert**. This lesson is the **rule object**. Opening the alert, tracing upstream, and PCAP are **1.4**.

| Piece | What to read | Why it matters |
|-------|----------------|----------------|
| **Name / description** | What a teammate thinks it does | Must match the logic |
| **Table / source** | `DeviceProcessEvents`, `http`, Sysmon 1, … | Wrong table = silent miss |
| **Logic** | Filters, joins, thresholds | What actually fires |
| **Window / schedule** | Last 5 minutes vs 24 hours; lookback | Correlation needs a time box |
| **Output** | Fields in the alert, severity | **1.4** consumes this |

**Correlation** means more than one condition or more than one table in a window (process create **and** a connect, count > N). A single-table filter is still a detection rule. You do not need a join to propose a basic rule.

| This lesson | Other |
|-------------|-------|
| Saved detection logic | SIGMA YAML — **1.3.1** (input) |
| Fields → `where` / regex / wildcards | Host / Zeek field teaching — **1.1** / **1.2** |
| Propose the rule | Alert investigation — **1.4** |

SOC **proposes**. Detection Engineering reviews and deploys. Create ceiling is **1a / 2b / 3c**.

### 1.2 Fields → detections; regex and wildcards; from SIGMA

**Turning log fields into detections (outline b)**

1. Name the **table**.
2. Pick **fields** you already know (`FileName`, `ProcessCommandLine`, `InitiatingProcessFileName`, `uri`, `user_agent`, …).
3. Add **specificity** (parent, token, path, dest) so it is not “all PowerShell.”
4. Optionally **count** or **join** in a window.
5. List **output fields** an analyst needs.

**Matching (outline c)**

| Technique | Looks like | Use |
|-----------|------------|-----|
| Equality / list | `FileName == "powershell.exe"` | Exact names |
| **Wildcard** | `FolderPath matches @"*\\Temp\\*"` or `has @"\Temp\"` | Simple path / suffix. `*` = any run of chars (product syntax varies) |
| **Regex** | `ProcessCommandLine matches regex @"(?i)-e(nc\|ncodedcommand)"` | Variation. Costly and easy to get wrong |

Use a wildcard or `has` when a substring/path is enough. Use regex when the token actually varies. Empty field → do not regex it into existence.

**From a SIGMA rule (task 2, second path):**  
Same four steps as **1.3.1**: logsource → table, selectors → `where`, condition → boolean, filters → extra `where`. Then wrap it as a **named SIEM rule** (schedule, title, output). You are not required to run a converter.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Table + 2–3 fields + a window | `DeviceProcessEvents` with no `where` |
| Wildcard on `\Temp\` | Regex that re-implements `endswith` |
| SIGMA `ParentImage` → `InitiatingProcessFileName` | SIGMA `uri` left on a process table |
| Title matches the logic | “Malware” title on a count of all 443 |

---

## 2. Detailed Walkthrough / Examples

### Example 1: From SIGMA (Expected)

**SIGMA (from 1.3.1 Example 1, shortened):** process_creation, powershell + `-enc` + script-host parent.

**SIEM rule (proposed):**

```
Name: Encoded PowerShell from script host
Source: DeviceProcessEvents
Window: 5 minutes
Logic:
  FileName =~ "powershell.exe"
  and ProcessCommandLine has_any ("-enc", "-EncodedCommand")
  and InitiatingProcessFileName in ("wscript.exe", "cscript.exe")
Output: Timestamp, DeviceName, AccountName, ProcessCommandLine,
        InitiatingProcessCommandLine
```

**What it detects:** The **1.1.1** Example 2 create. Mapped from SIGMA, not freehand magic.

**Interpretation:** Expected *as a rule*. Propose this. Do not deploy. Do not open the alert console (**1.4**).

### Example 2: No Filter (Lead)

```
Name: Process activity
Source: DeviceProcessEvents
Window: 24 hours
Logic: (none)
Output: *
```

**What it detects:** Every process create in a day.

**Interpretation:** Lead **about the rule**. A table is not a detection. Add fields.

### Example 3: From Log Fields, Wildcard + Threshold (Lead if Untuned)

```
Name: HTTP GET exe
Source: Zeek http
Window: 15 minutes
Logic:
  method == "GET"
  and uri matches @"*.exe*"
  | summarize count() by id.orig_h
  | where count_ > 1
```

**What it detects:** More than one GET whose URI wildcard-matches `.exe` per orig in 15 minutes. Would include **1.2.5** Example 3. The `*` wildcard is enough; a regex is not required.

**Interpretation:** Reasonable field-based start. Lead if `> 1` is untested (software updates). Document the wildcard. Tighten with `id.resp_h` or a URI path before you call it done.

---

## 3. Hands-On Exercise

**Objective:** Practice reading SIEM detections and proposing one from fields **or** SIGMA.

**Instructions:**

1. Summarize each example: what it detects, expected vs lead (as a *rule*).
2. **Analyze** this rule. Table, logic, window, what fires:

```
Name: Office to shell
Source: DeviceProcessEvents
Window: 5 minutes
Logic:
  InitiatingProcessFileName in ("winword.exe", "excel.exe", "outlook.exe")
  and FileName in ("cmd.exe", "powershell.exe")
```

3. **Create one** basic proposed rule, **either**:
   - **From log fields:** Zeek `http` POST + PowerShell User-Agent (1.2.5 Ex 2), **or**
   - **From SIGMA:** translate the “Office Spawns Cmd” YAML from **1.3.1** into a SIEM-shaped rule.
   Include name, source table, logic, window, and three output fields.
4. In one sentence, say whether you used a **wildcard**, a **regex**, or neither — and why.

**Expected Outcome:**
- Three summaries
- One analysis
- One proposed SIEM rule (from fields **or** SIGMA)
- One matching-technique note

Do not deploy. Do not write the **1.4** investigation playbook.

---

## 4. Knowledge Check

1. What pieces make up a SIEM detection / correlation search?
2. What does it mean to turn **log fields** into a detection?
3. When do you use a **wildcard** vs a **regex**?
4. How do you create a SIEM rule **from a SIGMA rule**?
5. Who deploys the rule, and why is an unfiltered table not a detection?

---

## 5. Summary

- SIEM rule = named logic on a table (or join), in a window, with outputs.
- Start from fields you already know, or translate SIGMA (logsource → table, selectors → `where`).
- Wildcards for simple paths; regex when the token varies.
- SOC proposes (1a / 2b / 3c). Unit **1.3** ends here. Next unit: **1.4** Alerts.

---

## 6. References & Further Reading

- Local SIEM rule / analytics-rule template used in class
- Related modules:
  - 1.3.1 – SIGMA rules
  - 1.3.2 – Suricata rules
  - 1.3.3 – YARA rules (previous)
  - 1.4.1 – Alert context and investigation (next)
