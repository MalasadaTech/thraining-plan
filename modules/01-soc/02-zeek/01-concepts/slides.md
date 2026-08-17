# Module 1.2.1 – Zeek Concepts  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 15–20 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 1.2.1 – Zeek Concepts  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Start of the Zeek unit. Map hour. Not conn fields. Not Wireshark.

---

### Slide 2 – What this hour is
**Title:** What this hour is

**1.1** was host rows. This unit is the **wire**.

Zeek writes structured logs.  
It does **not** name the initiating process.

**Speaker Notes:**  
That field was 1.1.4. Stay on the sensor.

---

### Slide 3 – What Zeek is
**Title:** A network analysis framework

Not primarily a signature IDS.

It classifies traffic and writes logs you query in a SIEM.

**Speaker Notes:**  
Outline a. Stop. Do not teach Bro history as a unit.

---

### Slide 4 – Engines
**Title:** Engines extract

An engine decides the protocol and **extracts** the fields.

That is how applications and protocols **surface** as log rows.

Conn, DNS, TLS, HTTP come later. Not today.

**Speaker Notes:**  
Outline b–c. Do not walk `orig_h`.

---

### Slide 5 – PCAP
**Title:** Why pull PCAP

A Zeek log is an **extract**.

Pull PCAP to **verify** the row, or to **expand** what the log does not carry.

Not Wireshark. Not the download path. Not **1.4.1**.

**Speaker Notes:**  
Outline d. Sensors are 0.8. Apply-versus-alert is later.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Zeek is primarily a signature-based IDS. True or false?  
2. What does an engine do?  
3. You already have a Zeek row. Why pull PCAP?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Framework, not signature IDS.  
Engines extract protocol.  
PCAP verifies or expands the extract.

**Next:** **1.2.2** Conn engine

**Speaker Notes:**  
That hour is orig_h / orig_p / resp_h / resp_p / state.
