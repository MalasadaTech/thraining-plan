# Instructor Guide – Module 1.3.3 – YARA Rules

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.3.1 A / B / C · 1.3.3.2 2b / 3c / 4c · 1.3.3.3 1a / 2b / 3c  
- Hunter: 1.3.3.1 B / C / C · 1.3.3.2 2b / 3c / 4c · 1.3.3.3 2b / 3c / 4c  
- CTI: 1.3.3.1 A / B / B · 1.3.3.2 1a / 2b / 3c · 1.3.3.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read a YARA rule, describe the match, choose file vs memory conditions, and propose a basic rule. No memory-dump lab. No malware authoring.

**Key Teaching Points:**
- Bytes, not logs (SIGMA) and not packets (Suricata).
- `meta` / `strings` / `condition`.
- ASCII, hex `{ 4D 5A }`, regex `/.../`.
- File: `at 0`, `filesize` OK. Memory: often drop those.
- SOC create **1a / 2b / 3c**.

**Common Student Challenges:**
- MZ-only rules.
- File conditions on a memory scan.
- Writing exploit or packer labs.
- Asking how to dump LSASS / process memory.
- Confusing YARA with a SIEM query.
- Grading SOC 3 as malware RE.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard: file vs memory condition
- Answer key (this guide)

---

## Learning Objectives

1. Explain purpose and structure.
2. Read strings and conditions (ASCII / hex / regex).
3. Files vs memory.
4. Analyze an existing rule.
5. Create or modify a basic rule (propose only).

**Mapped Items:**
- K: 1.3.3.1 – YARA rules
- T: 1.3.3.2 – Analyze an existing YARA rule
- T: 1.3.3.3 – Create or modify a basic YARA rule

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Not SIGMA/Suricata |
| Purpose and structure          | 10 min   | |
| Strings, matching, files/mem   | 14 min   | b–d |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~70 min** | Stretch Example 2 if they keep MZ-only |

---

## Detailed Teaching Notes

### 1. Purpose and structure

**Talking Points:**
- Same 3/5/7 split as SIGMA/Suricata.
- If the site has no memory YARA, say so and stay on files.
- `meta` never matches.

**Question to ask:**  
“Are we scanning a file or memory?”

### 2. Strings, matching, files vs memory

**Talking Points:**
- Walk b–d. Hex = MZ only. Regex one example.
- `uint16(0) == 0x5A4D` is the same idea as `$mz at 0` (endian). Either is fine.
- Memory: no dump demo. Condition change only.

**Question to ask:**  
“If I delete the string and leave MZ, what still matches?”

### 3. Examples

**Example 1:** MZ + update.exe + size. Tie to 1.2.7 Ex 2.  
**Example 2:** MZ only.  
**Example 3:** String-only; file vs memory.

---

## Hands-On Exercise – Instructor Guidance

**How to run:** 14–16 minutes. Fail shellcode. Fail memory-acquisition steps.

**Summaries:**
- Example 1: PE + `update.exe` + size; useful; expected as a rule; not a verdict.
- Example 2: any MZ; too broad; lead.
- Example 3: nightowl string; target-dependent; lead if file conditions used on memory.

**Invoice.jpg analysis:**  
Hex MZ at 0 AND ASCII `invoice.jpg`. File-oriented (offset 0). Would fire on **1.2.7** Example 3 *if that extract is scanned*. Not a host Event 11.

**Create / modify (equivalent is fine):**

```
rule BuildingC_Train_InvoiceJpgPE
{
    meta:
        description = "Training: PE containing invoice.jpg"
    strings:
        $mz = { 4D 5A }
        $n = "invoice.jpg" ascii nocase
    condition:
        $mz at 0 and $n and filesize < 5MB
}
```

A tightened Example 2 with any distinctive string + size also passes.

**Target note:** File extract / disk → keep `at 0` + `filesize`. Memory → string only (or platform-specific modules, out of scope).

SOC 3 pass: names strings + condition + one extra constraint. SOC 5: coherent rule + target.

---

## Knowledge Check – Answer Key

1. **YARA vs SIGMA vs Suricata?**  
   **Answer:** YARA matches **bytes** in a file or memory. SIGMA is a **log** detection. Suricata is a **network** signature.  
   **Explanation:** Outline a.

2. **meta / strings / condition?**  
   **Answer:** `meta` = notes (not matched). `strings` = named patterns. `condition` = when the rule fires.  
   **Explanation:** Structure.

3. **ASCII / hex / regex shapes?**  
   **Answer:** ASCII `$s = "update.exe" ascii`. Hex `$mz = { 4D 5A }`. Regex `$r = /checkin\.[a-z0-9-]+/`.  
   **Explanation:** Outline c.

4. **File vs memory?**  
   **Answer:** File scans can use `$mz at 0` and `filesize`. Memory often will not have the header at offset 0 — drop those or you miss / mislead.  
   **Explanation:** Outline d.

5. **Deploy? MZ-only?**  
   **Answer:** DE deploys. SOC proposes (1a / 2b / 3c). MZ-only matches every PE.  
   **Explanation:** Example 2 + matrix.

---

## Additional Instructor Resources

- Local YARA scan points (extract share, EDR module) if you have a list
- Next recommended module: 1.3.4 SIEM rules
