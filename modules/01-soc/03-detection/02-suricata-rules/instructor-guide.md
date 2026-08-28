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

- What this lesson is for: SOC analysts read a network signature to see what on the wire would fire — protocol, direction, and the string or buffer it looks for — and whether that match is specific.
- How it hooks to the lesson before: 1.3.1 was portable YAML for host logs (SIGMA). This lesson is the wire signature.
- How it hooks to the lesson after: 1.3.3 is YARA — files and memory, not packets.
- Why we are doing it this way: after host YAML, read one network signature so they can say what fires before they open file signatures or SIEM authorship.
- What we are *not* doing in this lesson: Deploy. IPS drop policy. Exploit payloads. Zeek scripts. SIGMA YAML. YARA. No lab.
- Extra step: none.

Use the same names as the student guide: **action**, **header**, **options**, **content**, and **5-tuple**. Use the GET `/update.exe` given. Hex example is `MZ` only. `$HOME_NET` is a site variable — do not invent the range. Do not tell the PRD plot.

**Key Teaching Points:**
- Action, header, options. This lesson is `alert` only.
- Put HTTP and TLS strings in the matching buffer, not on raw TCP.
- ASCII, hex, and regex are techniques. Regex is easy to over-match.
- A Suricata hit and a Zeek log can be the same session. Different job.

**Common Student Challenges:**
- Treat Suricata and Zeek as the same product. Why: both sit on the wire. Example: putting Zeek field `uri` in a Suricata rule, or writing “the http log fired.”
- Put `content:"GET"` on `tcp any any`. Why: GET is three bytes anywhere in the stream. Example: proposing that as a detection for a download of `/update.exe`.
- Ship or drop the rule. Why: SOC create is a proposal. Example: writing `drop` or asking for a production push.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.3.2.1 – Suricata rules
- T: 1.3.2.2 – Analyze an existing Suricata rule and describe what it detects
- T: 1.3.2.3 – Create or modify a basic Suricata rule

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Network signature, not host YAML |
| Key Concepts            | 16 min    | Structure, options, Zeek |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a Suricata rule, and you have to say what it matches and whether the match is specific.
- Walk action, header, and options. This lesson is `alert` only.
- `$HOME_NET` and `$EXTERNAL_NET` are site variables. Do not invent the range.
- Walk HTTP and TLS buffers. A string in the wrong buffer is a different match.
- Walk ASCII, hex (`MZ` only), and regex. Stop anyone who pastes an exploit payload.
- Same session, different job: Suricata says the signature matched; Zeek parsed the fields. Join with time plus the 5-tuple.
- Walk the given: outbound HTTP GET whose URI contains `/update.exe`. One sentence.
- If they open SIGMA YAML: that was 1.3.1.
- If they want `drop` or a production push: you propose. Detection Engineering reviews. How detections run as a service is 4.x.
- If they write `content:"GET"` on `tcp any any`: that is not a specific proposal.

---

## Knowledge Check – Answer Key

1. **Suricata and Zeek do the same job on a session. True or false?**  
   **Answer:** False. Suricata says this signature matched. Zeek parsed the session. The same traffic can produce both.  
   **Explanation:** Join them with time plus the 5-tuple. Do not put Zeek field names in the Suricata rule.

2. **The given rule — what does it detect, in one sentence?**  
   **Answer:** Outbound HTTP GET whose URI contains `/update.exe`.  
   **Explanation:** Action is `alert`. Header is HTTP from `$HOME_NET` to `$EXTERNAL_NET`. Options put `GET` in `http.method` and `/update.exe` in `http.uri`.

3. **Why is `content:"GET"` on `tcp any any` a poor proposal?**  
   **Answer:** Those three bytes match anywhere in any TCP session. Use the HTTP buffer and a specific URI.  
   **Explanation:** Tightening “any GET” by adding `http.uri` is a modify. A basic proposal names a specific content in the right buffer.

---

## Additional Instructor Resources

- Next: 1.3.3 YARA rules
