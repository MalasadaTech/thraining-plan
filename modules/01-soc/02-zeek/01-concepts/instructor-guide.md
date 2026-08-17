# Instructor Guide – Module 1.2.1 – Zeek Concepts

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:** SOC A→B→C | Hunter B→C  
**Estimated Time:** 45–60 minutes  
**Delivery Method:** Instructor-led (recommended)

---

## Module Overview for Instructors

**Purpose of this module:**  
Establish a solid conceptual foundation for Zeek before students dive into individual log types. Students must understand *what* Zeek is and *why* it matters before they start analyzing specific fields.

**Key Teaching Points:**
- Zeek is **not** just another IDS — emphasize the difference early.
- Focus on the mental model: Traffic → Events → Scripts → Logs → SIEM.
- Students only need a high-level understanding of log types at this stage; depth comes in later modules.
- Tie everything back to practical value for triage and hunting.
- Mention PCAP once: normally pulled to verify or expand a Zeek log. Not a Wireshark hour. Not the site download path.

**Common Student Challenges:**
- Confusing Zeek with Snort/Suricata (signature-based tools).
- Thinking they need to learn the Zeek scripting language right away (they don’t).
- Overwhelm from the number of log types — keep the focus on the top 6–7.

**Required Materials / Access:**
- Student Guide
- Slide Deck (once created)
- Optional: Live Zeek logs or screenshots for demonstration

---

## Learning Objectives

By the end of this module, students will be able to:

1. Explain what Zeek is and how it differs from traditional signature-based IDS/IPS.
2. Describe the core components of the Zeek architecture (events, scripts, logs).
3. Identify the primary Zeek log types and the kind of activity each captures.
4. Explain why Zeek logs are highly valuable for both alert triage and threat hunting.

**Mapped Proficiency Items:**
- K: 1.2.1.1 – Zeek concepts

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Set expectations |
| What is Zeek + Comparison      | 10 min   | Use the comparison table heavily |
| Core Architecture              | 8 min    | Keep the mental model simple |
| Primary Log Types              | 12 min   | Walk through the table; do not go deep on fields yet |
| Why Zeek Matters               | 6 min    | Connect to real SOC/hunting work |
| Hands-On Exercise              | 10 min   | Individual or pair work |
| Knowledge Check & Discussion   | 6 min    | |
| Summary & Questions            | 4 min    | |
| **Total**                      | **~60 min** | |

---

## Detailed Teaching Notes

### 1. What is Zeek?

**Talking Points:**
- Originally named Bro (Berkeley Network Monitor).
- Renamed to Zeek in 2018.
- It is a **network analysis framework**, not primarily an IDS.
- It generates logs by understanding protocols, not by matching signatures.

**What to emphasize:**
- Many new analysts assume Zeek = Snort. Correct this early.
- Zeek can raise notices (alerts), but its greatest value is the rich logs.

**Question to ask the class:**
- “If you already have Suricata or a commercial IDS, why would you also want Zeek?”

### 2. Core Architecture

**Talking Points:**
- Event Engine watches traffic and generates events.
- Scripts decide what to do with those events.
- Logging framework writes the structured output analysts actually use.

**Teaching tip:**  
Draw or show a simple three-box diagram:  
`Network Traffic → Event Engine → Scripts → Logs → SIEM`

Avoid going into the Zeek scripting language itself. That is out of scope for this module.

### 3. Primary Log Types

**Talking Points:**
- Walk through the table in the Student Guide.
- Highlight that `conn` is the foundation — almost every investigation starts there or references it.
- `dns`, `http`, and `ssl` are the next most frequently used in most SOCs.
- `weird` is underrated and often useful for detecting evasion or protocol abuse.

**What *not* to do:**  
Do not start explaining individual fields (e.g., `id.orig_h`, `method`, `uri`). That belongs in the dedicated engine modules.

### 4. Why Zeek Matters

**Talking Points:**
- Alert triage: Zeek often provides the context that turns a vague alert into a clear picture.
- Hunting: Structured, consistent logs are ideal for writing hunts.
- Retrospective investigation: Even when no alert fired, the data is still there.

**Real-world connection:**  
Ask experienced analysts in the room (if any) to share a time when Zeek logs helped them resolve an investigation faster.

---

## Hands-On Exercise – Instructor Guidance

**Objective:** Reinforce high-level understanding.

**How to run it:**
- Give students 8–10 minutes.
- Allow them to use the Student Guide.
- After time is up, ask 2–3 students to share their answers.

**What good answers look like:**
- Logs commonly chosen: conn, dns, http, ssl, files, weird
- Use cases should be realistic (C2, phishing, malware download, data exfil, etc.)
- Distinction from IDS should clearly mention logs vs alerts or protocol analysis vs signatures

---

## Knowledge Check – Answer Key

1. **True or False: Zeek is primarily a signature-based intrusion detection system.**  
   **Answer:** False  
   **Explanation:** Zeek is a network analysis framework that produces rich logs. While it can generate notices, its primary strength is protocol analysis and logging.

2. **Which Zeek component is responsible for generating events from network traffic?**  
   **Answer:** The Event Engine  
   **Explanation:** The Event Engine observes traffic and raises events that scripts can act upon.

3. **Name three Zeek log types that are especially valuable for threat hunting.**  
   **Answer:** Any three of: conn, dns, http, ssl/tls, files, weird, notice  
   **Explanation:** These provide the structured data most useful for hypothesis-driven and anomaly-based hunts.

4. **Why are Zeek logs often more useful for investigation than a simple IDS alert?**  
   **Answer:** Zeek logs contain rich protocol detail and context (methods, hosts, URIs, certificates, byte counts, etc.), whereas many IDS alerts only indicate that a signature matched.

---

## Additional Instructor Resources

- Official Zeek documentation: https://docs.zeek.org
- Log files reference: https://docs.zeek.org/en/current/script-reference/log-files.html
- Next recommended modules after this one:
  - 1.2.2 Conn Engine
  - 1.2.3 DNS Engine
  - 1.2.5 HTTP Engine
