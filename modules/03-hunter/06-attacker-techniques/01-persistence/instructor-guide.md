# Instructor Guide – Module 3.6.1 – Persistence Techniques

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.1 B / C / C ; 3.6.1.1 3c / 4c / 4c  
- SOC: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
- CTI: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Recognize four persistence classes in telemetry. Name the class and the field that proves it. Not a tactic hunt. Not privilege escalation. Not a registry-event write-up.

**Context (plain language):**

- What this lesson is for: Hunters name the method that will run again after reboot, logon, or a time trigger, and the field that proves it, so they do not confuse a one-off run with autorun.
- How it hooks to the lesson before: 3.5.1 mapped the classroom hunt to Persistence / Run keys. This lesson is that mechanism in telemetry.
- How it hooks to the lesson after: 3.6.2 is privilege escalation — elevation, not autorun.
- Why we are doing it this way: 1.1.5 taught reading the registry event (what changed, who changed it). This lesson is hunt persistence — recognize the class.
- What we are *not* doing in this lesson: Named-technique hunt (3.6.3). Privilege escalation (3.6.2). Registry-event field reading as the product (1.1.5). ATT&CK remapping (3.5). Hunt cards and hunt-type execute (3.2). Local hunt tickets (3.7). No lab.
- Extra step: none.

Use the same names as the student guide: **persistence**, **registry-based**, **start menu / startup folder**, **scheduled tasks**, and **other common methods** (**service**, **WMI** subscription, **logon script**). The product is **class** plus **proof**, or a **visibility gap**. The given uses course-fiction names (`WS-JLEE`, Run **`Updater`**, Temp `invoice.vbs`). Do not turn it into the intro plot or a hunt of every Run key.

**Key Teaching Points:**
- Persistence is a method that will run again. A one-off process is not persistence.
- Four classes. Name the one you see. Under other, say which method.
- 1.1.5 describes the registry set. This lesson names the class.
- Class plus proof, or a visibility gap. Do not invent a method.

**Common Student Challenges:**
- Treat a one-off `wscript` launch as persistence. Why: it ran, so it feels like the story. Example: writing “`invoice.vbs` persisted” from a process create.
- Stop after a 1.1.5 registry write-up. Why: hive, key, and initiator already feel complete. Example: “PowerShell set HKCU Run `Updater`” with no class.
- Hunt all Run keys, or write “hunt persistence.” Why: recognition is this lesson; a scoped hunt is 3.6.3. Example: searching every Run value, or hunting the whole Persistence tactic.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 3.6.1 – Persistence techniques
- T: 3.6.1.1 – Recognize persistence techniques in logs or telemetry

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Runs again; not a registry write-up |
| Key Concepts            | 12 min    | Four classes; given Run key |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert or a hunt lead names a host, and you have to say whether something will run again — and which method that is.
- Walk the four-class table. Stop. Services, WMI subscriptions, and logon scripts live under other; name the one you see. Do not inventory every persistence technique.
- Stop on 1.1.5: hive, key, value, and who changed it are already taught. This lesson is the class.
- Walk the given: HKCU Run **`Updater`** → `%TEMP%\update.exe` on **WS-JLEE**. One sentence: registry-based persistence. Proof is the value name plus the payload path.
- If they call the `wscript` launch persistence: that is one-off execution. The Run key is persistence.
- If they hunt all Run keys or say “hunt persistence”: that is 3.6.3.
- If they call the Run key privilege escalation: it starts as the user. Elevation is 3.6.2.
- If they skip a vendor Run key because it sits under `Program Files`: still persistence as a method.

---

## Knowledge Check – Answer Key

1. **A one-off `wscript invoice.vbs` is persistence. True or false?**  
   **Answer:** False. One-off execution is not persistence.  
   **Explanation:** Persistence is a method that will run again. The Run key is the persistence, not the first `wscript` launch.

2. **Name the four persistence classes.**  
   **Answer:** Registry-based. Start menu / startup folder. Scheduled tasks. Other common methods (service, WMI subscription, or logon script).  
   **Explanation:** Those four are the classes this lesson names. Under other, say which method you see.

3. **Class + proof for HKCU Run `Updater` → `%TEMP%\update.exe`.**  
   **Answer:** Registry-based persistence. Proof: value name **`Updater`** plus payload path `%TEMP%\update.exe`.  
   **Explanation:** Windows will launch that path at logon. Class plus the field that proves it is the product.

---

## Additional Instructor Resources

- Next: 3.6.2 Privilege escalation techniques
