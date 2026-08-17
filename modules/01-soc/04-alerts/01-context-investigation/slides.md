# Module 1.4.1 – Alert Context and Investigation  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.4.1 – Alert Context and Investigation  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
The object that fired. Not a new rule. Not TP/FP.

---

### Slide 2 – What this hour is
**Title:** What this hour is

The first alert is **`wscript` → encoded PowerShell**.

Investigate that object.  
Do **not** write the rule. Do **not** classify.

**Speaker Notes:**  
1.3.4 proposed the SIEM rule. It fired.

---

### Slide 3 – Context and config
**Title:** Present, missing, what would fire

**Context** — two columns: present / missing.  
Hash, IP, or domain you have → **VirusTotal** (**0.7**).  
Missing is a gap, not benign. Not Relations (**3.9**).

**Config** — one sentence: what would fire.

**Speaker Notes:**  
Outline a–b. Do not invent a command line.

---

### Slide 4 – Hops, host rows, PCAP
**Title:** Upstream, endpoint logs, PCAP

**Hops** — name each. SIEM-only is allowed. Do not invent Suricata.

**Endpoint logs** — what they **add** or **fail to add**. Temp `invoice.vbs` can add. Run key waits.

**PCAP** — what it adds versus alert fields. Process-only → **not applicable**.

**Speaker Notes:**  
Outline c–e. Why PCAP is 1.2.1. Sensors are 0.8.

---

### Slide 5 – Not this hour
**Title:** Not this hour

No TP/FP (**1.4.2**).  
No new SIGMA.  
No invented capture.

**Speaker Notes:**  
Hunt the Run key later.

---

### Slide 6 – What good looks like
**Title:** Five products

Present: host, user, `-enc`, parent `wscript`.  
VT: hash of `invoice.vbs` and/or `203.0.113.88` — one-line result.  
Config: that trio fires.  
Hops: SIEM rule → SIEM alert.  
Host logs: **add** Temp `invoice.vbs`.  
PCAP: **not applicable** on this first alert.

**Speaker Notes:**  
Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. Missing parent process means the activity was benign. True or false?  
2. Name the hops for a SIEM-only process alert.  
3. You have the hash of Temp `invoice.vbs` and IP `203.0.113.88`. What do you look up on VirusTotal, and what is **not** this hour?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Present vs missing. Hash / IP / domain → **VT**.  
What the config would fire.  
Name each hop.  
Logs and PCAP must add — or you say they failed.

**Next:** **1.4.2** Alert classification

**Speaker Notes:**  
TP / FP / TN / FN next.
