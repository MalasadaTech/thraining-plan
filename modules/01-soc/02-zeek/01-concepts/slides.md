# Module 1.2.1 – Zeek Concepts  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 15–20 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 1.2.1 – Zeek Concepts  
**Subtitle:** Network-sensor logs from the wire  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.1 was host and endpoint activity — logs from the host. This unit is network-sensor telemetry. This lesson does not teach conn fields or Wireshark.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

An alert can name traffic on the **wire**, not only a host.

**1.1** was host and endpoint activity — logs from the host.  
This unit is **network-sensor** telemetry.

Zeek writes structured logs. It does **not** name the initiating process.

**Speaker Notes:**  
This slide is the student intro. Analysts read Zeek when the work is on the wire. Name what Zeek is before anyone opens conn fields.

---

### Slide 3 – What Zeek is
**Title:** A network analysis framework

Not primarily a signature IDS.

It classifies traffic and writes logs you query in a SIEM.

**Speaker Notes:**  
Stay on what Zeek is. Do not teach Bro history as a unit. Do not turn this into a Suricata lesson.

---

### Slide 4 – Engines
**Title:** Engines extract protocol

An **engine** (script / analyzer) looks at a flow, decides the protocol, and **extracts** the fields.

That is how applications and protocols **surface** as logs you can query.

Conn, DNS, TLS, HTTP, SMTP, files, and weird are later lessons.

**Speaker Notes:**  
Surface means the application or protocol shows up as a log. Do not walk `orig_h`. Those fields are 1.2.2.

---

### Slide 5 – PCAP
**Title:** Why pull PCAP

A Zeek log is an **extract**.

Pull **PCAP** (a packet capture) to **verify** that extract, or to **expand** what the log does not carry.

Not Wireshark. Not the site download path.

**Speaker Notes:**  
PCAP is why you pull the packets, not how you read them. Sensors are 0.8. Applying PCAP against an alert is 1.4.1.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Zeek is primarily a signature-based IDS. True or false?  
2. What does an engine do?  
3. You already have a Zeek log. Why pull PCAP?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Framework, not signature IDS.  
Engines extract protocol.  
PCAP verifies or expands the extract.

**Next:** **1.2.2** Conn engine

**Speaker Notes:**  
1.2.2 is the conn log on the same network-sensor telemetry. Stay off conn fields until then.
