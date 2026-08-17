# Module 1.3.1 – SIGMA Rules

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.1.1 A / B / C · 1.3.1.2 2b / 3c / 4c · 1.3.1.3 1a / 2b / 3c  
- Hunter: 1.3.1.1 B / C / C · 1.3.1.2 2b / 3c / 4c · 1.3.1.3 2b / 3c / 4c  
- CTI: 1.3.1.1 A / B / B · 1.3.1.2 1a / 2b / 3c · 1.3.1.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of a SIGMA rule and its structure (title, logsource, detection, condition).
2. Read common SIGMA fields / selectors and say what telemetry they bind to.
3. Describe how a SIGMA detection becomes a SIEM query (without deploying it).
4. Analyze an existing SIGMA rule and state what it detects.
5. Create or modify a **basic** SIGMA rule (SOC proposes; Detection Engineering deploys).

**Mapped Proficiency Items:**
- K: 1.3.1.1 – SIGMA rules
- T: 1.3.1.2 – Analyze an existing SIGMA rule and describe what it detects
- T: 1.3.1.3 – Create or modify a basic SIGMA rule

---

## 1. Key Concepts

### 1.1 Purpose and structure

**SIGMA** is a generic, YAML detection format. You write **what to look for** once. A converter (or a human) turns it into a SIEM-specific query. SIGMA is **not** a SIEM, **not** Suricata, and **not** YARA.

SOC’s job in this unit is to **read** a rule and **propose** a basic one. You do not push it to production. That ceiling is why create/modify is **1a / 2b / 3c** for SOC.

| This lesson | Later / other |
|-------------|---------------|
| Generic YAML detection | SIEM analytics / correlation — **1.3.4** |
| Process / file / registry *selectors* | Host field depth — **1.1** |
| “How it becomes a query” | Alert triage — **1.4** |

**Structure (outline a)** — the parts you must name:

| Block | What it is |
|-------|------------|
| `title` / `description` | What a teammate thinks this rule does |
| `logsource` | Which telemetry (`product`, `category`, `service`) |
| `detection` | Named selections + a `condition` |
| `falsepositives` / `level` | Expected noise and severity *hints* — not a verdict |
| `tags` | Optional ATT&CK or product tags. Mapping hunts is **2.5**, not this hour. |

A rule without `logsource` + `detection` + `condition` is not a SIGMA detection. Empty `falsepositives` → write “not documented,” not “no FPs.”

### 1.2 Fields / selectors and translation to SIEM

**Selectors (outline b)** live under `detection`. Each name (`selection`, `filter_main`, …) is a set of field/value tests.

| Selector idea | SIGMA example | What it means |
|---------------|---------------|----------------|
| Exact / suffix | `Image\|endswith: '\powershell.exe'` | Process image ends with that name |
| Contains | `CommandLine\|contains: '-enc'` | Substring on the command line |
| List | `InitiatingProcessFileName: - wscript.exe - cscript.exe` | Any of these parents |
| Regex | `CommandLine\|re: '(?i)-e(nc\|ncodedcommand)'` | Pattern (use sparingly) |
| Filter | `filter_admin:` + `condition: selection and not filter_admin` | Exclude known-good |

Field **names** follow the logsource. `Image` / `CommandLine` on `process_creation` are the process row from **1.1.2**. Do not invent a Zeek `uid` on a Windows process rule.

**How SIGMA becomes a SIEM query (outline c):**

1. `logsource` → the table (`DeviceProcessEvents`, Sysmon Event 1, …).
2. Each selection → `where` predicates (`endswith` → `endswith`, `contains` → `has` / `contains`).
3. `condition` → boolean combination (`and` / `or` / `not`).
4. Filters → extra `where` / `!in`.

You will **write the mapping in words or pseudo-KQL**. Running `sigmac` / pipelines is not a sign-off item. Full SIEM rule authorship is **1.3.4**.

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Tight `logsource` + 2–3 selectors + a named filter | `Image\|endswith: '\powershell.exe'` alone |
| Condition you can say in one sentence | Condition you cannot explain |
| `falsepositives` names a real admin path | Empty FP note on a noisy selector |
| Field names match the logsource | `query` / `uri` on a process_creation rule |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Useful, Narrow Rule (Expected)

```yaml
title: Encoded PowerShell from Script Host
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith: '\powershell.exe'
    CommandLine|contains:
      - '-enc'
      - '-EncodedCommand'
    ParentImage|endswith:
      - '\wscript.exe'
      - '\cscript.exe'
  condition: selection
falsepositives:
  - Rare admin packages that wrap a script host
level: high
```

**What it detects:** A **process create** where PowerShell has an encoded command line **and** the parent is `wscript`/`cscript`. Same story as **1.1.2** Example 2.

**SIEM shape (not deployed):**  
`DeviceProcessEvents` / Sysmon 1 → `FileName == powershell.exe` and command line contains `-enc` and `InitiatingProcessFileName` in (`wscript.exe`, `cscript.exe`).

**Interpretation:** Expected *as a rule*: scoped, explainable, tied to a logsource. Not an incident by itself.

### Example 2: Over-Broad Rule (Lead)

```yaml
title: Any PowerShell
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith: '\powershell.exe'
  condition: selection
level: high
```

**What it detects:** Every PowerShell process create. Helpdesk, user consoles, installers, and encoded C2 all match.

**Interpretation:** Lead **about the rule**. Too broad to propose as-is. Modify it (parent, command-line token, path) before you hand it to DE. Do not deploy.

### Example 3: Wrong Logsource / Missing Selector (Lead)

```yaml
title: Nightowl HTTP Beacon
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    uri|contains: '/api/v1/beacon'
  condition: selection
```

**What it detects:** As written, **nothing reliable**. `uri` is an HTTP field (**1.2.5**), not a process-create field. The 1.2.5 beacon was `POST` + PowerShell UA on the **wire**.

**Interpretation:** Lead. Name the mismatch. A correct SIGMA for that *host* story would use process + command line (1.1.2) or wait for **1.3.4** / a network logsource — do not invent a Zeek field on this Windows category. Do not write a Suricata rule here (**1.3.2**).

---

## 3. Hands-On Exercise

**Objective:** Practice reading SIGMA and proposing a basic rule.

**Instructions:**

1. Review the three examples. One sentence each: what it detects, and expected vs lead (as a *rule*).
2. **Analyze** this rule. Say logsource, selectors, condition, and what would fire:

```yaml
title: Office Spawns Cmd
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    ParentImage|endswith:
      - '\winword.exe'
      - '\excel.exe'
      - '\outlook.exe'
    Image|endswith:
      - '\cmd.exe'
      - '\powershell.exe'
  condition: selection
```

3. **Modify** Example 2 **or create** a basic rule that detects **script-host or Office** creating `powershell.exe` / `cmd.exe` (reuse **1.1.2**). Include `logsource`, `detection`, `condition`, and one `falsepositives` line.
4. In two sentences, translate *your* rule (or Example 1) into a SIEM-style pseudo-query. Do not deploy anything. Do not write Suricata or YARA.

**Expected Outcome:**
- Three short summaries
- One analysis that names logsource + condition
- One basic YAML rule (create or modify)
- One translation to a SIEM shape

---

## 4. Knowledge Check

1. What is SIGMA for, and what is it *not*?
2. Which three blocks must a detection have (`logsource`, `detection`, `condition`)? What does `logsource` control?
3. What does a modifier like `|endswith` or `|contains` do?
4. How does a SIGMA rule become a SIEM query? Who deploys it in this program?
5. Why is “any `powershell.exe`” a poor proposal?

---

## 5. Summary

- SIGMA = portable YAML detection. Structure: logsource + named selections + condition.
- Selectors bind to fields on that logsource. Wrong field = broken rule.
- Translation: logsource → table, selectors → `where`, condition → boolean. **1.3.4** is the SIEM rule.
- SOC **proposes** a basic rule (1a / 2b / 3c). DE reviews and deploys.
- Next: Suricata rules (**1.3.2**). Alerts are **1.4**.

---

## 6. References & Further Reading

- SIGMA specification (rule format) — as used in class
- Related modules:
  - 1.1.2 – Process activity
  - 1.3.2 – Suricata rules (next)
  - 1.3.4 – SIEM rules
  - 1.4.1 – Alert context and investigation
