# Module 1.2.1 – Zeek Concepts

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.1.1 A / B / C  
- Hunter: 1.2.1.1 B / C / C  
- CTI: 1.2.1.1 A / B / B  
**Estimated Time:** 15–20 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain Zeek’s purpose and the role of analyzers and scripts.
2. Distinguish network-sensor records from endpoint evidence.
3. Explain when PCAP can verify or expand a logged observation.

**Mapped Proficiency Items:**
- K: 1.2.1.1 – Zeek concepts

## Why This Matters

Network-sensor evidence describes traffic visible at an observation point. Zeek turns that traffic into structured records that analysts can search and connect. Understanding how those records are produced helps you choose the right log and recognize when additional evidence is needed.

## 1. How traffic becomes a log

Zeek is a network analysis framework. Protocol analyzers interpret observed traffic, and scripts use events from that analysis to create logs and other outputs. This course uses “engine” as an introductory label for these analysis and logging components; it is not a claim that every log comes from a separate protocol engine.

Connection records summarize flows. Protocol logs describe observations such as DNS transactions, TLS handshakes, HTTP requests, and SMTP transactions. File analysis records observed content, while weird records describe unexpected conditions encountered during analysis. These records expose different aspects of activity that a SIEM can make searchable.

## 2. Relating Zeek to endpoint evidence

A native Zeek record generally identifies network endpoints, times, and protocol details. An endpoint record may identify the responsible operating-system process. To connect them, examine the host/address relationship, time, ports, protocol, and available identifiers.

The sensor's placement matters. Traffic outside its view, encrypted content, packet loss, and configuration choices can limit what Zeek records. A missing protocol log therefore needs a coverage explanation before it can support a conclusion about the activity.

## 3. When packet capture helps

A packet capture (PCAP) contains captured packets rather than only the fields selected for a log. If retained for the relevant flow, it may help verify a parsed value, examine a header, or recover visible content omitted from the log.

For example, a connection log identifies two endpoints, but an available cleartext HTTP capture may reveal the requested URI. An encrypted capture may still leave application content unreadable. Capture availability, completeness, and decryption context determine what can be added. Request the relevant time and flow through the site's collection process and explain the question the capture is intended to answer.

## Knowledge Check

1. How do analyzers and scripts contribute to Zeek logs?
2. What can endpoint evidence add to a Zeek connection record?
3. When would PCAP add information, and when might it not?

## Summary

Zeek supplies structured observations from network traffic. Choose a log according to the question, account for the sensor’s view, and use retained PCAP when it can add relevant evidence.

## Course Connections

Previous: [1.1.6 – Image and Driver Load Activity](../../01-endpoint/06-image-driver-load/student-guide.md)

Next: [1.2.2 – Conn Engine](../02-conn-engine/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Zeek — Log files](https://docs.zeek.org/en/master/reference/zeekscript/log-files.html)
- [Zeek — conn.log](https://docs.zeek.org/en/current/reference/logs/conn.html)
