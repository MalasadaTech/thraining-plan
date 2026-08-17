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

- What this hour is for: SOC analysts need the map of network-sensor logs before they read a `conn` row. This hour is that map.
- How it hooks to the hour before: 1.1 closed on host rows. 1.1.4 named the initiating process. Zeek will not.
- How it hooks to the hour after: 1.2.2 is the conn engine — first log fields.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–d only. PCAP is a mention, not a course.
- What we are *not* doing this hour: Wireshark. Site download path. Apply-versus-alert (1.4.1). A catalog of every log. No lab.
- Extra step: none.

Do not invent TAP / SPAN names. Sensors are **0.8**. Do not teach `orig_h` today.

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

**Mapped Items:** K 1.2.1.1

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Wire, not host |
| Key Concepts            | 10 min    | Framework, engine, PCAP |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write framework → engine → PCAP. Stop before conn fields.

If they ask who started the socket: “1.1.4. Not on this row.”  
If they open Wireshark: “Not this hour. PCAP is why, not how.”  
If they start TAP names: “0.8. Do not invent the site.”

---

## Knowledge Check – Answer Key

1. **Zeek is primarily a signature-based IDS. True or false?**  
   **Answer:** False. It is a network analysis framework that writes structured logs.  
   **Explanation:** Outline a.

2. **What does an engine do?**  
   **Answer:** Classify the protocol and extract fields. That is how applications and protocols show up as log rows.  
   **Explanation:** Outline b–c.

3. **Why pull PCAP if you already have a Zeek row?**  
   **Answer:** To verify the extract, or to expand what the log does not carry.  
   **Explanation:** Outline d.

---

## Additional Instructor Resources

- Next: 1.2.2 Conn engine
