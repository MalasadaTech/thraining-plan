# Instructor Guide – Module 1.4.1 – Alert Context and Investigation

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.1.1 A / B / C · 1.4.1.2 2b / 3c / 4c · 1.4.1.3 2b / 3c / 4c · 1.4.1.4 2b / 3c / 4c · 1.4.1.5 2b / 3c / 4c · 1.4.1.6 2b / 3c / 4c  
- Hunter: 1.4.1.1 B / C / C · 1.4.1.2 2b / 3c / 4c · 1.4.1.3 2b / 3c / 4c · 1.4.1.4 2b / 3c / 4c · 1.4.1.5 2b / 3c / 4c · 1.4.1.6 2b / 3c / 4c  
- CTI: 1.4.1.1 A / A / B · 1.4.1.2 1a / 1a / 2b · 1.4.1.3 1a / 1a / 2b · 1.4.1.4 1a / 1a / 2b · 1.4.1.5 1a / 1a / 1a · 1.4.1.6 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to work an alert object: present vs missing context, what the config would fire, named upstream hops, what endpoint logs add, what PCAP adds versus the alert.

**Key Teaching Points:**
- Five tasks, five sentences. “I opened the alert” is not a task.
- Config = what would fire, not a new SIGMA.
- Hops: Suricata → SIEM → alert, or SIEM-only. Do not invent a hop.
- Logs/PCAP must change (or fail to change) the story.
- Do not classify (**1.4.2**). Do not author (**1.3**).

**Common Student Challenges:**
- Inventing a missing command line.
- Calling Example 2 an FP in this hour.
- Rewriting the Any-PowerShell SIGMA.
- “I pulled PCAP” on a process alert.
- Inventing a Suricata hop on a SIEM-only rule.
- Grading CTI on endpoint/PCAP (they are 1a).

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard: present | missing | hops
- Answer key (this guide)

---

## Learning Objectives

1. Present vs missing context.
2. What the configuration would fire.
3. Name each upstream hop.
4. What endpoint logs add or fail to add.
5. What PCAP adds versus the alert, or N/A.

**Mapped Items:** K 1.4.1.1 · T 1.4.1.2–1.4.1.6

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Not 1.3 / 1.4.2 |
| Context and configuration      | 12 min   | a–b |
| Hops, logs, PCAP               | 12 min   | c–e |
| Walkthrough Examples           | 14 min   | Students first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~70 min** | Stretch Ex 2 if they say FP |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: A / 2b — two-column present/missing + one-sentence config.
- Hunter already B / 2b at 3-level. Push “what logs add.”
- CTI: A / 1a on logs and PCAP. Do not run them through a pcap lab. 7-level A→B on K; 1a→2b on context/config/hops.

**Questions:**  
“What is *missing*?”  
“What would this config fire on that this alert did not show?”

**Examples:**  
Ex 1 = complete process card (baseline).  
Ex 2 = thin context + broad config; logs add explorer/Get-Help. Park 1.4.3.  
Ex 3 = three hops; logs fail; PCAP adds URI.

---

## Hands-On Exercise – Instructor Guidance

**How to run:** 14–16 minutes. Fail a TP/FP label. Fail a new YAML rule. Fail invented fields.

**Summaries:**
- Ex 1: Complete process alert; SIEM-only; logs add vbs path; PCAP N/A.
- Ex 2: Thin Any-PowerShell; missing cmdline/parent; logs add explorer + Get-Help.
- Ex 3: Suricata GET update.exe; three hops; no host process; PCAP adds URI.

**Example 2 card (key):**  
Present: device, powershell, title. Missing: cmdline, parent, user. Config: any powershell create. Hops: SIEM → alert. Logs add: explorer + Get-Help. PCAP N/A.

**Example 3 card (key):**  
Present: 5-tuple, sid, title. Missing: URI, process. Config: GET `/payload/update.exe`. Hops: sid 1000001 → SIEM → alert. Logs fail to add a process. PCAP adds GET URI, empty UA.

**Office/cmd card (key):**  
Present: host, user, child cmd, rule. Missing: parent on the pane. Config: Office → cmd/powershell. Hops: SIEM only. Logs add WINWORD. PCAP N/A.

---

## Knowledge Check – Answer Key

1. **Context vs config?**  
   **Answer:** Context is what arrived with the alert. Configuration is the detection object — what *would* fire.  
   **Explanation:** Outline a vs b.

2. **Missing?**  
   **Answer:** A field the investigation needs that the pane does not have. Write “missing.” Do not invent it.  
   **Explanation:** Task 1.

3. **Hops?**  
   **Answer:** Three-hop: Suricata sid → SIEM correlation → SIEM alert. One-hop: SIEM rule → SIEM alert.  
   **Explanation:** Outline c.

4. **Endpoint logs sentence?**  
   **Answer:** What they **add** (parent, cmdline) or **fail to add** (no row). Not “I queried.”  
   **Explanation:** Task 4.

5. **PCAP N/A vs contrast?**  
   **Answer:** N/A when the alert is not network / no capture exists. When you have PCAP, contrast method/URI/SNI with the alert fields.  
   **Explanation:** Task 5.

---

## Additional Instructor Resources

- Local alert-pane field list if you have one
- Next recommended module: 1.4.2 Alert classification
