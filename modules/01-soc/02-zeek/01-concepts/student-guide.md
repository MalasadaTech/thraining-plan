# Module 1.2.1 – Zeek Concepts

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.1.1 A / B / C  
- Hunter: 1.2.1.1 B / C / C  
- CTI: 1.2.1.1 A / B / B  
**Estimated Time:** 15–20 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what Zeek is, and what an engine does.
2. Say why you pull PCAP when you already have a Zeek log.

**Mapped Proficiency Items:**
- K: 1.2.1.1 – Zeek concepts

---

## 1. Key Concepts

**1.1** was host rows. This unit is **network-sensor** telemetry. Zeek watches the wire and writes structured logs. It does **not** name the initiating process. That field was **1.1.4**.

**Zeek** is a network analysis framework. It is not primarily a signature IDS. It classifies traffic and writes logs you query in a SIEM.

**Engines** (scripts / analyzers) look at a flow, decide what protocol it is, and **extract** the fields for that protocol. Conn, DNS, TLS, HTTP, SMTP, files, and weird are later hours. This hour is only that they exist and that they **surface** applications and protocols as log rows.

**PCAP** is the usual next artifact. A Zeek log is an **extract**. You pull PCAP to **verify** a Zeek row or to **expand** what the log does not carry. This is not a PCAP analysis course. Not Wireshark. Not the site download path (**0.8** / retired tool access). Applying PCAP against an alert is **1.4.1**.

**What good looks like:** you can say Zeek is the sensor log, an engine extracted the protocol, and PCAP is how you check or fill a gap. You do not open `conn` fields yet (**1.2.2**).

---

## 2. Knowledge Check

1. Zeek is primarily a signature-based IDS. True or false?
2. What does an engine do?
3. You already have a Zeek row. Why pull PCAP?

---

## 3. Summary

Zeek writes structured logs from the wire. Engines extract protocol. PCAP verifies or expands the extract. The process name is on the host row, not here.

**Next:** **1.2.2** Conn engine.

---

## 4. Related modules

- 1.1.6 – Image and driver load (previous)
- 1.2.2 – Conn engine
- 1.1.4 – Host-observed network
- 1.4.1 – PCAP against an alert (later)
