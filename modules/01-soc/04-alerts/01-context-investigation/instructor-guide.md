# Instructor Guide – Module 1.4.1 – Alert Context and Investigation

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.1.1 A / B / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- Hunter: 1.4.1.1 B / C / C ; 1.4.1.2–1.4.1.6 2b / 3c / 4c  
- CTI: 1.4.1.1 A / A / B ; 1.4.1.2–1.4.1.4 1a / 1a / 2b ; 1.4.1.5–1.4.1.6 1a / 1a / 1a  
**Estimated Time:** 30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Investigate the fired alert: context, config, hops, related host rows, PCAP versus alert fields.

**Context (plain language):**

- What this hour is for: SOC analysts work the object that fired — not write a new rule, not call TP/FP yet.
- How it hooks to the hour before: 1.3.4 proposed the SIEM rule. This hour that rule has fired on wscript → encoded PowerShell.
- How it hooks to the hour after: 1.4.2 is classification (TP/FP/TN/FN).
- Why we are doing it this way: Short 0.x / 4.x voice. All five tasks as what good looks like. Story bible: the first alert is the process create only. Run key waits for hunt. PCAP is apply-versus-alert, not a download course.
- What we are *not* doing this hour: Classify. Author a rule. Invent a Suricata hop. Invent a PCAP. Relations / 3.9. Night Owl / Harbor architecture. No lab.
- Extra step: none.

Keep `jlee` as the given user. Do not require WS-JLEE as site policy. Do not tell the PRD plot.

**Key Teaching Points:**
- Present / missing. Hash, IP, or domain you have → VirusTotal (**0.7**).
- Config = what would fire.
- Name each hop. SIEM-only is allowed.
- Endpoint logs must add or fail to add.
- PCAP not applicable on a process-only alert.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.4.1.1 ; T 1.4.1.2–1.4.1.6

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | The object that fired |
| Key Concepts            | 20 min    | Five jobs; one given |
| Knowledge Check         | 5 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~30 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Walk present/missing, then VT on the hash or `203.0.113.88` once you have it. Then config, hops. Pull the file row as “adds invoice.vbs.” PCAP N/A on this first alert.

If they classify TP: “1.4.2.”  
If they invent Suricata: “Not on this given.”  
If they open Run\\Updater: “Hunt. Not this first pass.”  
If they invent a PCAP: “Process-only. Not applicable.”

---

## Knowledge Check – Answer Key

1. **Missing parent means benign. True or false?**  
   **Answer:** False. Missing is a gap.  
   **Explanation:** Outline a / task 1.

2. **Hops for a SIEM-only process alert?**  
   **Answer:** SIEM rule → SIEM alert.  
   **Explanation:** Outline c / task 3.

3. **Hash of invoice.vbs and IP 203.0.113.88 — what on VT, and what is not this hour?**  
   **Answer:** Look up the hash and the IP (and a domain if you have one). Not Relations / a pivot graph (**3.9**).  
   **Explanation:** Outline a / task 1 / **0.7**.

---

## Additional Instructor Resources

- Next: 1.4.2 Alert classification
