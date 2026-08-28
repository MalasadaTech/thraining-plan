# Module 1.4.1 – Alert Context and Investigation  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.4.1 – Alert Context and Investigation  
**Subtitle:** Work the object that fired  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is the start of alert handling. The object in the queue already fired. You do not write a new rule. You do not classify TP or FP yet.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

An alert is the **object that fired**.

SOC analysts gather **context** on that object before they classify it.

This lesson is that first pass.

**Speaker Notes:**  
This slide is the student intro. The job is to say what the alert already shows, what it does not, and what related host logs or a packet capture add. Classification is the next lesson.

---

### Slide 3 – Present, missing, VirusTotal
**Title:** Present, missing, VirusTotal

**Context** is two lists: **present** and **missing**.

Host, user, time, rule name, and the field the rule keys on.

If you have a hash, IP, or domain, look it up on **VirusTotal**. Write the one-line result.

Missing is a **gap**, not benign. Do not open Relations (**2.9**).

**Speaker Notes:**  
Name the gap. Do not fill it with a guess. VirusTotal here is reputation on a value you already have. Relations is later.

---

### Slide 4 – Config and hops
**Title:** What would fire, and each hop

**Configuration** — one sentence: what would fire.

**Upstream hops** — name each hop from detection logic to the alert.

Classroom pattern: Suricata rule → SIEM correlation search → SIEM alert.

Some alerts are **SIEM-only**. Do not invent a Suricata hop.

**Speaker Notes:**  
Walk configuration first, then hops. The given in this course is a SIEM rule that fired a SIEM alert. Inventing Suricata adds a hop that is not on the given.

---

### Slide 5 – Endpoint logs and PCAP
**Title:** What logs and PCAP add

**Endpoint logs** — pull related host events for that host and window. State what they **add** or **fail to add**. Opening the table is not the task.

**PCAP** — for a network alert, state what the capture adds versus the alert fields.

If the alert is process-only and there is no capture, write **PCAP not applicable**.

**Speaker Notes:**  
A file event can add Temp invoice.vbs. The Run key waits for hunt. Why you pull PCAP is 1.2.1. Sensors are 0.8. Do not invent a packet capture.

---

### Slide 6 – The first alert
**Title:** The first alert

The first alert is **`wscript` → encoded PowerShell** as `jlee`.

**Present:** host, user, `-enc`, parent `wscript`.  
**VirusTotal:** hash of `invoice.vbs` and/or IP `203.0.113.88` — one line.  
**Config:** PowerShell with `-enc` and parent `wscript` fires.  
**Hops:** SIEM rule → SIEM alert.  
**Host logs:** add Temp `invoice.vbs`.  
**PCAP:** not applicable on this process alert.

**Speaker Notes:**  
Show this given before the knowledge check. Do not tell the rest of the incident. Do not classify.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. The alert context is missing a parent process. That means the activity was benign. True or false?  
2. Name the hops for a SIEM-only process alert.  
3. You have the hash of Temp `invoice.vbs` and IP `203.0.113.88`. What do you look up on VirusTotal, and what is **not** this lesson?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Present versus missing. A hash, IP, or domain you have goes to **VirusTotal**.  
Say what the configuration would fire.  
Name each hop.  
Logs and PCAP must add something — or you say they failed to.

**Next:** **1.4.2** Alert classification

**Speaker Notes:**  
TP, FP, TN, and FN are next. Stay off classification until that lesson.
