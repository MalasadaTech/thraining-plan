# Instructor Guide – Module 1.3.2 – Suricata Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.2.1 A / B / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 1a / 2b / 3c  
- Hunter: 1.3.2.1 B / C / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 2b / 3c / 4c  
- CTI: 1.3.2.1 A / B / B ; 1.3.2.2 1a / 2b / 3c ; 1.3.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a Suricata rule and propose a basic create or modify. Do not deploy it.

**Context (plain language):**

- What this hour is for: SOC analysts need to read a network signature the same way they read SIGMA — what fires, and is it specific.
- How it hooks to the hour before: 1.3.1 was host YAML. This hour is the wire signature for GET /update.exe (1.2.5).
- How it hooks to the hour after: 1.3.3 is YARA — files / memory, not packets.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–d only. SOC create is 1a/2b/3c.
- What we are *not* doing this hour: Deploy. IPS drop policy. Exploit payloads. Zeek scripts. No lab.
- Extra step: none.

Use `/update.exe` GET. Hex example is `MZ` only. No BUILDINGC / Night Owl names. Do not tell the PRD plot.

**Key Teaching Points:**
- Action, header, options.
- HTTP/TLS buffers, not raw TCP for HTTP strings.
- ASCII / hex / regex.
- Suricata hit + Zeek row = same session, different job.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.3.2.1 ; T 1.3.2.2 ; T 1.3.2.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Network signature, not YAML |
| Key Concepts            | 16 min    | Structure, options, Zeek |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Walk action / header / options. Read the given rule. Contrast with `tcp any any` + `GET`.

If they open SIGMA: “That was 1.3.1.”  
If they want drop: “Alert only this hour.”  
If they paste shellcode: “Stop. MZ is enough hex.”

---

## Knowledge Check – Answer Key

1. **A Suricata rule is action, header, and options. True or false?**  
   **Answer:** True.  
   **Explanation:** Outline a.

2. **The given rule — what does it detect?**  
   **Answer:** Outbound HTTP GET whose URI contains /update.exe.  
   **Explanation:** Outline b and 1.3.4 task 1.

3. **Why is content GET on tcp any any a poor proposal?**  
   **Answer:** Those three bytes match anywhere in any TCP session. Use the HTTP buffer and a specific URI.  
   **Explanation:** Outline b–c / 1.3.4 task 2.

---

## Additional Instructor Resources

- Next: 1.3.3 YARA rules
