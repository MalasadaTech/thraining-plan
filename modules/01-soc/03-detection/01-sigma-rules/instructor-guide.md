# Instructor Guide – Module 1.3.1 – SIGMA Rules

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.1.1 A / B / C · 1.3.1.2 2b / 3c / 4c · 1.3.1.3 1a / 2b / 3c  
- Hunter: 1.3.1.1 B / C / C · 1.3.1.2 2b / 3c / 4c · 1.3.1.3 2b / 3c / 4c  
- CTI: 1.3.1.1 A / B / B · 1.3.1.2 1a / 2b / 3c · 1.3.1.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read SIGMA, describe what a rule detects, map it to a SIEM shape, and **propose** a basic rule. SOC does not deploy.

**Key Teaching Points:**
- Portable YAML, not a SIEM product.
- Structure: `logsource` + `detection` + `condition`.
- Selectors must match the logsource. `uri` on process_creation is a broken rule.
- Translation is table + `where` + boolean. Pipeline tools are optional.
- SOC create = **1a / 2b / 3c**. 3-level names the parts and fills a template.

**Common Student Challenges:**
- Treating SIGMA as already-in-the-SIEM.
- Writing “any PowerShell” and calling it done.
- Putting HTTP/Zeek fields on a Windows process rule.
- Asking how to run `sigmac` or commit to git.
- Opening Suricata / YARA / **1.4**.
- Grading SOC 3 as if they must ship production YAML.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard: logsource → table → `where`
- Answer key (this guide)

---

## Learning Objectives

1. Explain SIGMA purpose and structure.
2. Read fields / selectors.
3. Describe translation to a SIEM query.
4. Analyze an existing rule.
5. Create or modify a basic rule (propose only).

**Mapped Items:**
- K: 1.3.1.1 – SIGMA rules
- T: 1.3.1.2 – Analyze an existing SIGMA rule
- T: 1.3.1.3 – Create or modify a basic SIGMA rule

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Propose, don’t deploy |
| Purpose and structure          | 10 min   | Blocks on the board |
| Selectors + translation        | 14 min   | a–c |
| Walkthrough Examples           | 14 min   | Students first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~70 min** | Stretch Example 3 if they invent uri on process |

---

## Detailed Teaching Notes

### 1. Purpose and structure

**Talking Points:**
- SOC 3: A / 2b / **1a** — name the blocks; fill a template with guidance.
- SOC 5: B / 3c / **2b** — analyze cleanly; modify with help on the hardest part.
- SOC 7: C / 4c / **3c** — can train the analysis; competent proposal, still not DE deploy.
- Hunter: B / 2b at 3-level on both tasks; 5/7 reach C / 4c including create.
- CTI: A / B / B; analyze 1a / 2b / 3c; create **1a / 1a / 2b**. Do not grade CTI as Hunter 5.

**Question to ask:**  
“What telemetry does this rule even read?”

### 2. Selectors and translation

**Talking Points:**
- Walk outline a–c. Dual-map `Image` → `FileName`, `ParentImage` → `InitiatingProcessFileName`.
- `|contains` / `|endswith` / `|re` once each. Regex is a tool, not the lesson.
- Translation is four steps. Stop before vendor converter flags.

**Question to ask:**  
“If I delete `logsource`, can I still know the table?”

### 3. Examples

**Example 1:** Good scope. Tie to 1.1.2 Ex 2.  
**Example 2:** Broad = lead about the rule.  
**Example 3:** `uri` on process_creation. Do not write Suricata.

---

## Hands-On Exercise – Instructor Guidance

**How to run:** 14–16 minutes. Grade analysis + a basic YAML. Fail a deploy plan. Fail Suricata/YARA.

**Summaries:**
- Example 1: Encoded PowerShell from script host; useful/narrow; expected as a rule.
- Example 2: Any PowerShell create; too broad; lead.
- Example 3: `uri` on process_creation; broken mapping; lead.

**Office Spawns Cmd analysis:**  
Windows `process_creation`. Parent is Word/Excel/Outlook. Child is `cmd.exe` or `powershell.exe`. Condition = that selection. Fires on Office → shell. Does **not** require `-enc`.

**Create / modify (equivalent is fine):**

```yaml
title: Script Host or Office Spawns Shell
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    ParentImage|endswith:
      - '\wscript.exe'
      - '\cscript.exe'
      - '\winword.exe'
      - '\excel.exe'
      - '\outlook.exe'
    Image|endswith:
      - '\powershell.exe'
      - '\cmd.exe'
  condition: selection
falsepositives:
  - Macro-enabled business documents; some software updaters
```

A tightened Example 2 (add `-enc` **and** a parent) also passes.

**Translation example:**  
`DeviceProcessEvents` | where FileName in (powershell.exe, cmd.exe) | where InitiatingProcessFileName in (wscript.exe, cscript.exe, winword.exe, excel.exe, outlook.exe)

SOC 3 pass: names logsource + two selectors + a condition, even if YAML is messy. SOC 5: coherent YAML. Fail `Image: '*'` with no other selector.

---

## Knowledge Check – Answer Key

1. **What is SIGMA / not?**  
   **Answer:** A generic YAML detection format you translate into a SIEM query. It is not the SIEM, not Suricata, not YARA, and not a deployed alert.  
   **Explanation:** Outline a.

2. **Three blocks? logsource?**  
   **Answer:** `logsource`, `detection`, `condition`. `logsource` picks product/category/service — the table you will query.  
   **Explanation:** Structure.

3. **Modifiers?**  
   **Answer:** They change how the value is matched (`endswith` suffix, `contains` substring, `re` regex).  
   **Explanation:** Outline b.

4. **Translation? Who deploys?**  
   **Answer:** logsource → table, selectors → filters, condition → boolean. SOC **proposes**. Detection Engineering reviews and deploys. Full SIEM authorship is **1.3.4**.  
   **Explanation:** Outline c + matrix 1a/2b/3c.

5. **Why not any PowerShell?**  
   **Answer:** It matches expected daily use. A proposal needs another selector (parent, command line, path).  
   **Explanation:** Example 2.

---

## Additional Instructor Resources

- Local SIGMA style (title prefix, required tags) if you have one
- Next recommended module: 1.3.2 Suricata rules
