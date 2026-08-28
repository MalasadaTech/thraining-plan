# Instructor Guide – Module 1.2.1 – Zeek Concepts

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.1.1 A / B / C  
- Hunter: 1.2.1.1 B / C / C  
- CTI: 1.2.1.1 A / B / B  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name what Zeek is, what an engine does, and why PCAP is the usual next artifact.

**Context (plain language):**

- What this lesson is for: An alert can name traffic on the wire, not only a host. Before you describe that traffic, you have to know what Zeek is — a framework that watched the wire and wrote structured fields. This lesson names what Zeek is, what an engine does, and why you still pull PCAP.
- How it hooks to the lesson before: 1.1 was host and endpoint activity (logs from the host). 1.1.4 named the initiating process. Zeek will not.
- How it hooks to the lesson after: 1.2.2 is the conn engine — first log fields.
- Why we are doing it this way: name the network-sensor log before anyone reads a conn field. PCAP is a mention, not a course.
- What we are *not* doing in this lesson: Wireshark. Site download path. Applying PCAP against an alert (1.4.1). A catalog of every log. TAP / SPAN names (sensors are 0.8). Conn fields (`orig_h`). No lab.
- Extra step: none.

Use the same names as the student guide: **Zeek**, **engine**, **extract**, **surface**, and **PCAP**. **Engine** means a script or analyzer. **Surface** means the application or protocol shows up as a log you can query.

**Key Teaching Points:**
- Framework, not signature IDS.
- Engines extract and surface protocol.
- PCAP verifies or expands the extract.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.2.1.1 – Zeek concepts

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Network-sensor logs, not host logs |
| Key Concepts            | 10 min    | Framework, engine, PCAP |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert can name traffic on the wire, and you have to know what that Zeek log is before you describe it.
- 1.1 was host and endpoint activity (logs from the host). This unit is network-sensor telemetry. Zeek does not name the initiating process.
- Walk framework, then engine, then PCAP. Stop before conn fields.
- If they ask who started the socket: that is 1.1.4. It is not on this log.
- If they open Wireshark: that is not this lesson. PCAP is why you pull it, not how you read it.
- If they start TAP or SPAN names: that is 0.8. Do not invent the site.
- If they apply PCAP against an alert: that is 1.4.1.

---

## Knowledge Check – Answer Key

1. **Zeek is primarily a signature-based IDS. True or false?**  
   **Answer:** False. It is a network analysis framework that writes structured logs.  
   **Explanation:** Zeek classifies traffic and extracts fields. A signature IDS matches payloads against rules. That is not what Zeek is for in this lesson.

2. **What does an engine do?**  
   **Answer:** Classify the protocol and extract fields. That is how applications and protocols show up as logs.  
   **Explanation:** An engine is a script or analyzer. It looks at a flow, decides the protocol, and writes the fields you query. Conn, DNS, and the rest wait for later lessons.

3. **Why pull PCAP if you already have a Zeek log?**  
   **Answer:** To verify the extract, or to expand what the log does not carry.  
   **Explanation:** A Zeek log is the fields an engine already wrote. PCAP is the packet capture you use to check those fields or to fill a gap. This lesson does not teach Wireshark or how to download the file.

---

## Additional Instructor Resources

- Next: 1.2.2 Conn engine
