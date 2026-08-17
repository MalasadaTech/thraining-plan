# Module 2.6.1 – Persistence Techniques  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 2.6.1 – Persistence Techniques  
**Subtitle:** Threat Hunter Training (SOC / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
2.5.1 mapped the hunt. This lesson is recognize the mechanism. Not privesc. Not hunt-for-specific.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain registry, startup-folder, scheduled-task, and other persistence
2. Recognize those methods in logs or telemetry
3. Mark a row expected, a lead, or untestable

**Mapped Items:**  
K: 2.6.1 | T: 2.6.1.1

**Speaker Notes:**  
Hunter 3 is already at principles (B / 3c). Recognition tops at 4c. SOC/CTI K is A / B / B.

---

### Slide 3 – Agenda
**Title:** Agenda

- What persistence is (and is not)
- Four classes (outline a–d)
- Proof fields in telemetry
- Three worked examples
- Identification practice
- Two recognition queries
- Knowledge check

**Speaker Notes:**  
2.6.2 is privesc. 2.6.3 is hunt-for-specific. Stay here.

---

### Slide 4 – Not Persistence
**Title:** These Are Not This Lesson

“They use persistence.”  
“UAC bypass / token impersonation.”  
“One `wscript.exe` launch.”  
“Hunt all of TA0003.”

**Key Point:** Name a class that will run again. Or it is not recognition.

**Speaker Notes:**  
Leave the slogans up. Kill them in Example 3.

---

### Slide 5 – Runs Again
**Title:** Persistence vs One-Off

| Persistence | Not |
|-------------|-----|
| Boot / logon / schedule | One process, one connection |
| Named autorun object | Privilege change alone (**2.6.2**) |
| Expected *or* lead | Slogan with no method |

**Analyst Tip:** Ask: will this fire without the operator?

**Speaker Notes:**  
Expected vendor Run keys still count as the class.

---

### Slide 6 – Four Classes
**Title:** Outline 2.6.1 a–d

| Class | Place |
|-------|--------|
| Registry | Run / RunOnce / Winlogon |
| Startup folder | User or All Users Startup |
| Scheduled task | Task create + trigger + command |
| Other | Service, WMI, logon script |

**Key Point:** You do not owe every Persistence technique in ATT&CK.

**Speaker Notes:**  
Write one proof field under each row live.

---

### Slide 7 – Proof Fields
**Title:** What Recognition Looks Like

**Registry:** hive + key + value + data  
**Startup:** folder path + file/lnk + target  
**Task:** name + run-as + trigger + command  
**Other:** say which other

**Analyst Tip:** No telemetry for that class → visibility gap. Do not guess.

**Speaker Notes:**  
ATT&CK IDs are labels if already mapped (2.5.1). Not the deliverable.

---

### Slide 8 – Expected vs Lead
**Title:** Same Class, Different Call

| Class | Expected | Lead |
|-------|----------|------|
| Registry | Signed updater in `Program Files` | Run → `%APPDATA%` |
| Startup | Documented user shortcut | New All Users `.lnk` |
| Task | Named IT job | SYSTEM + `C:\Users\Public\` |
| Other | Known GPO script | New WMI consumer |

**Key Point:** Recognition ≠ incident. Recognition ≠ hunt (**2.6.3**).

**Speaker Notes:**  
Force “lead, not incident” on Example 2.

---

### Slide 9 – Example 1: Expected Run Key
**Title:** Example 1 – Vendor Update

- Class: **registry** (`HKLM\...\Run`)
- Path: `C:\Program Files\Vendor\update.exe`
- Call: **expected** — still that class

**Interpretation:**  
Recognized. Not an incident. Not a hunt.

**Speaker Notes:**  
Students score the card before you reveal the interpretation.

---

### Slide 10 – Example 2: SYSTEM Task
**Title:** Example 2 – 4698 vs whoami

**4698:** `\Microsoft\Windows\UpdateCheck`, SYSTEM, `C:\Users\Public\update.bat`  
**whoami:** one `cmd.exe` — not persistence

**Interpretation:**  
Task = scheduled-task **lead**. SYSTEM ≠ automatic privesc.

**Speaker Notes:**  
Park 2.6.3 execute. Park 2.6.2.

---

### Slide 11 – Example 3: Wrong Class
**Title:** Example 3 – UAC vs WMI

**A:** UAC / token = “persistence.”  
**B:** WMI filter + CommandLine consumer → `sync.vbs` at logon = **other**.

**Interpretation:**  
A is **2.6.2**. B names other + proof.

**Speaker Notes:**  
They must say “WMI” (or service / logon script), not only “other.”

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Slogan with no class
- One-off script = persistence
- SYSTEM task = privesc
- Whole ATT&CK Persistence tactic
- Hunt plan instead of recognition
- Guessing a method with no logs

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide (reason each).
3. Two recognition pseudo-queries (Run key; 4698).
4. One recognition card: class, proof, expected vs lead.

**Speaker Notes:**  
Park privesc, hunt-for-specific, SIEM execute. Review with the Instructor Guide key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. Persistence vs one-off?
2. One registry location + proof field?
3. Startup folder vs Run key?
4. What makes a scheduled-task log a lead?
5. One other method; one non-persistence?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Persistence = runs again.
- Four classes: registry, startup folder, scheduled task, other.
- Class + proof field. Expected still counts.
- One-off ≠ persistence. Privesc is **2.6.2**.
- No telemetry → visibility gap.
- Next: privilege escalation (**2.6.2**). Hunt-for-specific is **2.6.3**.

**Speaker Notes:**  
Do not open a 2.6.2 token lab.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 2.6.2 – Privilege escalation techniques

**Resources:**
- Student Guide for this module
- Module 2.5.1 – ATT&CK for hunt planning
- Module 2.6.3 – Hunt for a specific technique (later)

**Speaker Notes:**  
Park local hunt control (2.7).

---

### Slide 17 – Quick Reference (Optional)
**Title:** Persistence Classes — Quick Reference

| Class | Proof |
|-------|--------|
| Registry | Run / RunOnce / Winlogon value data |
| Startup folder | File or `.lnk` in Startup + target |
| Scheduled task | Create/update + trigger + run-as + command |
| Other | Service / WMI consumer / logon script |

**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Optional handout. Not a full ATT&CK catalog.
