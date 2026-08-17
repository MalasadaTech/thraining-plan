# Instructor Guide – Module 1.1.4 – Network Activity (Endpoint)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.4.1 A / B / C ; 1.1.4.2 2b / 3c / 4c ; 1.1.4.3 2b / 3c / 4c  
- Hunter: 1.1.4.1 A / B / B ; 1.1.4.2 1a / 2b / 3c ; 1.1.4.3 1a / 2b / 3c  
- CTI: 1.1.4.1 A / A / A ; 1.1.4.2 1a / 1a / 1a ; 1.1.4.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a host-network row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read host network rows to see which process on this device talked, and to where.
- How it hooks to the hour before: 1.1.3 was the file row (`wscript` created Temp `update.exe`). This hour is the connect on the same host telemetry.
- How it hooks to the hour after: 1.1.5 is the registry row. Zeek protocol fields are 1.2.
- Why we are doing it this way: Short 0.x / 4.x voice. Tasks stay as what good looks like. No lab this pass.
- What we are *not* doing this hour: Zeek `conn` / `dns` / JA3 (1.2). Sysmon install. Process-create or file-create write-ups. No lab.
- Extra step: none.

The point of this hour versus Zeek is **who on the host**. Do not invent MDE `ActionType` values. Encoded PowerShell → `203.0.113.88:443` continues the 1.1.2 / 1.1.3 given — do not tell the PRD plot.

**Key Teaching Points:**
- Host-observed connect or DNS, not Zeek.
- Initiating process is why the row exists next to Zeek.
- Event 3 is a connect. Event 22 is DNS, and only if the feed has it.
- A query is specific, not “all connections.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.1.4.1 ; T 1.1.4.2 ; T 1.1.4.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Who talked — not Zeek |
| Key Concepts            | 16 min    | Fields a–e; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Walk the field table. Stop on initiating process: that is the 1.1 vs 1.2 split.

If they paste a Zeek `conn` and ask who did it: “Not on that row. This hour.”  
If they describe the process create of `wscript`: “1.1.2.”  
If they open the Temp file create: “1.1.3.”  
If they write `DeviceNetworkEvents` with no filter: “Not specific.”

---

## Knowledge Check – Answer Key

1. **A Zeek `conn` row names the initiating process. True or false?**  
   **Answer:** False. Zeek sees the wire. The process is on the host row (Sysmon 3 / `DeviceNetworkEvents`).  
   **Explanation:** Outline c / e.

2. **Encoded PowerShell `ConnectionSuccess` to 203.0.113.88:443, no URL. What occurred?**  
   **Answer:** Hidden encoded PowerShell successfully connected outbound TCP/443 to that IP. URL not logged.  
   **Explanation:** Outline a–c and 1.1.4.1 task 1.

3. **A query that matches every host-network event is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (initiator + dest port or remote IP).  
   **Explanation:** 1.1.4.1 task 2.

---

## Additional Instructor Resources

- Next: 1.1.5 Registry activity
