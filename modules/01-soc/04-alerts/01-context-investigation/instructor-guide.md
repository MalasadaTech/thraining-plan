# Instructor Guide – Module 1.4.1 – Alert Context and Investigation

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.1.1 A / B / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- Hunter: 1.4.1.1 B / C / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- CTI: 1.4.1.1 A / A / B ; 1.4.1.2 1a / 1a / 2b ; 1.4.1.3 1a / 1a / 2b ; 1.4.1.4 1a / 1a / 2b ; 1.4.1.5 1a / 1a / 1a ; 1.4.1.6 1a / 1a / 1a  
**Estimated Time:** 30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Investigate the fired alert: context, configuration, hops, related host events, and PCAP versus the alert fields.

**Context (plain language):**

- What this lesson is for: SOC analysts work the object that fired — not write a new rule, not call TP/FP yet. They gather context so a gap is not treated as benign and a hop that is not there is not invented.
- How it hooks to the lesson before: 1.3.4 proposed the SIEM rule. In this lesson that rule has fired on `wscript` → encoded PowerShell.
- How it hooks to the lesson after: 1.4.2 is classification (TP/FP/TN/FN).
- Why we are doing it this way: all five tasks as what good looks like, not a lab. The first alert is the process create only. VirusTotal is a one-line lookup of a value you already have, not Relations.
- What we are *not* doing in this lesson: Classify. Author a rule. Invent a Suricata hop. Invent a PCAP. Relations / 2.9. Live-account lab. The Run key (hunt is 3.x). No lab.
- Extra step: none.

Use the same names as the student guide: **context**, **present**, **missing**, **configuration**, **upstream hops**, **endpoint logs**, and **PCAP**. Say **host event** or **host log**, not unexplained “host row.” Keep `jlee` as the given user. Do not require WS-JLEE as site policy. Do not tell the rest of the incident.

**Key Teaching Points:**
- Present / missing. A hash, IP, or domain you have goes to VirusTotal (**0.7**).
- Configuration is what would fire.
- Name each hop. SIEM-only is allowed.
- Endpoint logs must add or fail to add.
- PCAP is not applicable on a process-only alert.

**Common Student Challenges:**
- Treat missing context as benign. Why: a blank field feels like “nothing bad.” Example: writing “benign” because the parent process is empty.
- Invent a Suricata hop. Why: the classroom pattern includes Suricata. Example: naming a Suricata rule on this SIEM-only process alert.
- Invent a packet capture. Why: the task mentions PCAP. Example: writing a URI from a capture that does not exist on this process alert.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.4.1.1 – Alert context and investigation
- T: 1.4.1.2 – Review an alert and identify which context is present and which is missing (include VirusTotal on a hash, IP, or domain you have)
- T: 1.4.1.3 – Review the alert configuration and explain what would fire
- T: 1.4.1.4 – Trace an alert to its upstream detection logic and name each hop
- T: 1.4.1.5 – Collect related endpoint logs and state what they add (or fail to add)
- T: 1.4.1.6 – Collect related PCAP and state what it adds versus the alert fields

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

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

**Talking Points:**
- Open with the job: an alert fired, and you gather context before you classify it.
- Walk present versus missing. Missing is a gap. Do not invent a command line.
- Once a file event adds Temp `invoice.vbs` (or they have `203.0.113.88`), look that hash or IP up on VirusTotal. One line. Not Relations.
- Config: one sentence on what would fire. Hops: name each. This given is SIEM rule → SIEM alert.
- Pull related host events. A file event **adds** Temp `invoice.vbs`. If there is no parent in the tenant, the logs **fail to add** it.
- PCAP is not applicable on this process-only first alert. On a network alert, say what the capture adds versus the alert fields.
- If they classify TP: that is 1.4.2.
- If they invent Suricata: not on this given.
- If they open the Run key: hunt. Not this first pass.
- If they invent a PCAP: process-only. Not applicable.

---

## Knowledge Check – Answer Key

1. **The alert context is missing a parent process. That means the activity was benign. True or false?**  
   **Answer:** False. Missing is a gap.  
   **Explanation:** Present versus missing names what you have and what you do not. An empty parent is not evidence the activity was benign.

2. **Name the hops for a SIEM-only process alert.**  
   **Answer:** SIEM rule → SIEM alert.  
   **Explanation:** Name each hop that is on the given. Do not add a Suricata rule that is not there.

3. **You have the hash of Temp `invoice.vbs` and IP `203.0.113.88`. What do you look up on VirusTotal, and what is not this lesson?**  
   **Answer:** Look up the hash and the IP (and a domain if you have one). Not Relations or a pivot graph (**2.9**).  
   **Explanation:** VirusTotal here is a one-line lookup of a value you already have (**0.7**). Platform depth is later.

---

## Additional Instructor Resources

- Next: 1.4.2 Alert classification
