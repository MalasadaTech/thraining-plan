# Module 2.6.2 – Privilege Escalation Techniques  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 2.6.2 – Privilege Escalation Techniques  
**Subtitle:** Threat Hunter Training (SOC / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
2.6.1 was persistence (runs again). This lesson is recognize the elevation. Not hunt-for-specific.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain common Windows privilege-escalation methods and their indicators
2. Recognize those methods in logs or telemetry
3. Mark a row expected, a lead, or untestable

**Mapped Items:**  
K: 2.6.2 | T: 2.6.2.1

**Speaker Notes:**  
Hunter 3 is already at principles (B / 3c). Recognition tops at 4c. SOC/CTI K is A / B / B.

---

### Slide 3 – Agenda
**Title:** Agenda

- What privilege escalation is (and is not)
- Common Windows methods (outline a)
- Indicators (outline b)
- Three worked examples
- Identification practice
- Two recognition queries
- Knowledge check

**Speaker Notes:**  
2.6.1 is persistence. 2.6.3 is hunt-for-specific. Stay here.

---

### Slide 4 – Not This Lesson
**Title:** These Are Not Privilege Escalation

“They use privesc.”  
“SYSTEM scheduled task in Public.”  
“Process was already SYSTEM.”  
“Hunt all of TA0004.”

**Key Point:** Privilege must **change**. Name the method. Or it is not recognition.

**Speaker Notes:**  
Leave the slogans up. Kill them in Examples 2 and 3.

---

### Slide 5 – Privilege Changes
**Title:** Escalation vs Already Privileged

| Escalation | Not |
|------------|-----|
| Medium → High or SYSTEM | Started as SYSTEM |
| Token / UAC / hijacked service | Autorun that *starts* privileged (**2.6.1**) |
| Expected *or* lead | Slogan with no method |

**Analyst Tip:** Ask: did privilege change without the operator already being admin?

**Speaker Notes:**  
Expected consented UAC still counts as the method.

---

### Slide 6 – Four Method Families
**Title:** Outline 2.6.2 a

| Method | Idea |
|--------|------|
| Token | Steal / impersonate a privileged token |
| UAC bypass | High IL without a real consent |
| Service / image abuse | Hijack something that runs as SYSTEM |
| Other | Potato / pipe / named exploit — say which |

**Key Point:** You do not owe every Privilege Escalation technique in ATT&CK.

**Speaker Notes:**  
Write one indicator under each row live (outline b).

---

### Slide 7 – Indicators
**Title:** Outline 2.6.2 b

**Token:** who opened whose token + child identity  
**UAC:** auto-elevate parent + payload + consent yes/no  
**Service:** image path + who changed it + run-as  
**Always:** integrity / run-as **changed**

**Analyst Tip:** No integrity, token, or service-path logs → visibility gap. Do not guess.

**Speaker Notes:**  
ATT&CK IDs are labels if already mapped (2.5.1). Not the deliverable.

---

### Slide 8 – Expected vs Lead
**Title:** Same Method, Different Call

| Method | Expected | Lead |
|--------|----------|------|
| UAC | Signed installer, clicked Yes | `fodhelper` → Public exe, no consent |
| Token | Documented admin tool | User `helpdesk.exe` → SYSTEM `cmd` |
| Service | Ticketed path change | SYSTEM binary under `C:\Users\Public` |

**Key Point:** Recognition ≠ incident. Recognition ≠ hunt (**2.6.3**).

**Speaker Notes:**  
A row can be service abuse *and* persistence. Name both.

---

### Slide 9 – Example 1: Consented UAC
**Title:** Example 1 – Vendor Setup

- Method: **UAC elevation** (consented)
- Signed `VendorSetup.exe`, user clicked Yes, High IL
- Call: **expected** — still that method

**Interpretation:**  
Recognized. Not an incident. Not a hunt.

**Speaker Notes:**  
Students score the card before you reveal the interpretation.

---

### Slide 10 – Example 2: Token vs 4698
**Title:** Example 2 – Elevation vs Persistence

**14:03:** `helpdesk.exe` (user) + SYSTEM token → `cmd.exe` SYSTEM  
**02:17 4698:** task *starts* as SYSTEM + Public bat

**Interpretation:**  
14:03 = **token** lead. 4698 = **2.6.1**, not this class.

**Speaker Notes:**  
Park 2.6.3 execute. Force: SYSTEM ≠ privesc.

---

### Slide 11 – Example 3: Wrong Class
**Title:** Example 3 – Task vs fodhelper

**A:** New SYSTEM task in Public = “privilege escalation.”  
**B:** `fodhelper.exe` → `sync.exe`, High IL, no consent = **UAC bypass**.

**Interpretation:**  
A is **2.6.1**. B names method + indicator.

**Speaker Notes:**  
They must say “UAC bypass,” not only “privesc.”

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Slogan with no method
- Already-SYSTEM process = escalation
- SYSTEM task = privesc
- Whole ATT&CK Privilege Escalation tactic
- Hunt plan instead of recognition
- Guessing a method with no integrity/token logs

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide (reason each).
3. Two recognition pseudo-queries (user→SYSTEM; auto-elevate parents).
4. One recognition card: method, indicator, expected vs lead.

**Speaker Notes:**  
Park persistence labs, hunt-for-specific, exploit writing, SIEM execute. Review with the Instructor Guide key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. Escalation vs already privileged?
2. One Windows method + indicator?
3. UAC bypass vs consented elevation?
4. Why is a SYSTEM scheduled task not automatically privesc?
5. One non-privesc; what if you cannot see tokens?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Privilege escalation = privilege **changes**.
- Four families: token, UAC bypass, service abuse, other.
- Method + indicator. Expected still counts.
- Already SYSTEM / autorun-as-SYSTEM → not this class (**2.6.1** if it persists).
- No telemetry → visibility gap.
- Next: hunt for a specific technique (**2.6.3**).

**Speaker Notes:**  
Do not open a 2.6.3 hunt lab.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 2.6.3 – Hunt for a specific persistence or privilege-escalation technique

**Resources:**
- Student Guide for this module
- Module 2.6.1 – Persistence techniques
- Module 2.5.1 – ATT&CK for hunt planning

**Speaker Notes:**  
Park local hunt control (2.7).

---

### Slide 17 – Quick Reference (Optional)
**Title:** Privilege Escalation — Quick Reference

| Method | Indicator |
|--------|-----------|
| Token | User parent + privileged token / SYSTEM child |
| UAC bypass | Auto-elevate parent + payload + no consent |
| Service abuse | SYSTEM image path on a user-writable file |
| Other | Named pipe / potato / exploit — say which |

**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Optional handout. Not a full ATT&CK catalog.
