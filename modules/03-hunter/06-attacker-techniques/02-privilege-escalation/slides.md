# Module 3.6.2 – Privilege Escalation Techniques  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 3.6.2 – Privilege Escalation Techniques  
**Subtitle:** A privilege change, not an autorun  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
3.6.1 named persistence — something that will run again. This lesson is the privilege change. It is not a named-technique hunt.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

Hunters read host telemetry to see whether an actor **gained a higher privilege** than they started with.

Persistence will **run again**. Elevation is a **privilege change**.

This lesson names the method and the indicator.

**Speaker Notes:**  
This slide is the student intro. If they call a Run key elevation, they hunt the wrong class. Do not open a named-technique hunt today.

---

### Slide 3 – Elevation is a privilege change
**Title:** Elevation is a privilege change

Typically standard user → administrator or **SYSTEM**.

The A12 Run key **`Updater`** starts as the logged-on user. That is **not** elevation.

A SYSTEM scheduled task is persistence unless you also see **how** a non-privileged actor got SYSTEM.

A process that was **already** SYSTEM is not elevation.

**Speaker Notes:**  
Keep them on the change, not the autorun. If they start mapping ATT&CK, that is 3.5. If they start hunting the class, that is 3.6.3.

---

### Slide 4 – Methods and the indicator
**Title:** Methods and the indicator

**Token theft / impersonation** — user-context parent → SYSTEM or High-integrity child. The parent is not auto-elevate.

**UAC bypass** — an auto-elevate binary (Windows raises it without a real prompt) launches an unexpected payload. No real consent.

**Privileged service / image abuse** — service image in a user-writable path, or a non-privileged user creates a SYSTEM service.

**Other** — a method you can point at, plus a SYSTEM spawn. Say which.

If you cannot see integrity, tokens, or the image path, name a **visibility gap**.

**Speaker Notes:**  
Walk method then indicator. Auto-elevate versus not is how they tell UAC bypass from token theft. Do not dump exploit names into Other.

---

### Slide 5 – Recognize it
**Title:** Recognize it

One line: method + indicator.

**Given:** user `helpdesk.exe` → `cmd.exe` as SYSTEM, no consent. **Token theft.**

**Given:** `fodhelper.exe` → unknown executable, no consent. **UAC bypass.**

**Given:** HKCU Run **`Updater`**. **Not** this class.

Do not hunt the whole class. That is **3.6.3**.

**Speaker Notes:**  
These two elevation lines are classroom examples, not A12 facts. Show them before the knowledge check. One sentence each. The Run key stays in 3.6.1.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. HKCU Run **`Updater`** is privilege escalation. True or false?  
2. Name two privilege-escalation methods.  
3. User `helpdesk.exe` → SYSTEM `cmd.exe`, no consent: method + indicator.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Elevation is a privilege change, not an autorun.  
Name the method and the indicator, or name a visibility gap.

**Next:** **3.6.3** Hunt one named technique

**Speaker Notes:**  
3.6.3 is one named method with a unique pattern. Stay off that hunt unless it is scheduled.
