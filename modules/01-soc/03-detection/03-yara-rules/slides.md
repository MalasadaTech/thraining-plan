# Module 1.3.3 – YARA Rules  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.3.3 – YARA Rules  
**Subtitle:** Byte patterns in a file or in memory  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.3.2 was the network signature. This lesson is YARA: read a byte-pattern rule and propose a basic one. It is not SIGMA, not Suricata, and not how to dump memory.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts match **byte patterns** on a file they already have.

A log can name the file. It does not show the bytes inside.

Read a rule. Propose a basic create or modify.  
Not a SIEM query. Not how to dump memory. Not deploy.

**Speaker Notes:**  
This slide is the student intro. The job is to say what a YARA rule would hit, then propose a basic one. Suricata stays on the wire. SIEM is the next lesson.

---

### Slide 3 – Purpose and structure
**Title:** Purpose and structure

**YARA** matches bytes in a file or in process memory.

A useful rule needs **`strings`** and a real **`condition`**.  
**`meta`** is notes, not the match.

**Speaker Notes:**  
Name the three blocks, then stop. A rule with strings and `condition: true` is not a useful proposal. Deploy is not this lesson.

---

### Slide 4 – ASCII, hex, regex
**Title:** ASCII, hex, regex

**ASCII** — `"update.exe" ascii nocase`.  
**Hex** — `{ 4D 5A }` (`MZ`). Not Suricata `content:"|4d 5a|"`.  
**Regex** — `/update\.(exe|dll)/ nocase`. Easy to over-match.

Named patterns plus a boolean: `and`, `or`, `filesize`, `at 0`.

**Speaker Notes:**  
Same three techniques as Suricata, different syntax. If they paste pipe-hex from last lesson, switch them to braces. Regex is a technique, not a requirement on every rule.

---

### Slide 5 – File vs memory
**Title:** File vs memory

**File** — disk or a saved extract. `at 0` and `filesize` can apply.

**Memory** — a process the shop already scans. Drop `filesize`. Drop `at 0` for a PE header.

If your shop does not scan memory, say so and stay on files.

**Speaker Notes:**  
`filesize` does not apply on a process scan, so that condition will not match. MZ at offset 0 assumes the scanned blob starts with the PE. Do not teach how to acquire memory.

---

### Slide 6 – Read it. Propose a basic one.
**Title:** Read it. Propose a basic one.

**Given:** MZ at 0 **and** `"update.exe"`, `filesize < 5MB`.

**Detects:** a PE file that contains that name, under 5 MB.

`{ 4D 5A } at 0` alone matches Notepad.

SOC **proposes**. DE reviews.

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: a file that starts with MZ and contains update.exe, under 5 MB. It can fit a 1.2.7 extract if you scan those bytes. It is not a files-log match and not a conviction. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. YARA is a SIEM query language. True or false?  
2. The given rule — what does it detect, in one sentence?  
3. Why is `{ 4D 5A } at 0` alone a poor proposal?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Meta + strings + condition.  
ASCII / hex / regex.  
File rules may use `at 0` and `filesize`. Memory often must not.  
You propose. You do not deploy.

**Next:** **1.3.4** SIEM rules

**Speaker Notes:**  
1.3.4 is log fields or a SIGMA rule, not bytes. Stay off YARA syntax when you get there.
