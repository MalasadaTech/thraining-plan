# Module 1.2.1 – Zeek Concepts

- Explain Zeek’s purpose and the role of analyzers and scripts.
- Distinguish network-sensor records from endpoint evidence.
- Explain when PCAP can verify or expand a logged observation.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

Network-sensor evidence describes traffic visible at an observation point. Zeek turns that traffic into structured records that analysts can search and connect. Understanding how those records are produced helps you choose the right log and recognize when additional evidence is needed.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## How traffic becomes a log

Analyzers interpret traffic; scripts use events to produce structured records. Different logs expose different observations.

**Speaker notes:** Explain analyzer versus logging script without introducing a scripting course. Use conn, DNS, and files as examples of different record purposes.

---

## Relating Zeek to endpoint evidence

Correlate sensor and endpoint evidence using supported identity, timing, and flow details. Account for visibility.

**Speaker notes:** Ask what makes two records plausibly related and what could break the association, such as address translation or time differences.

---

## Supplied example

A native Zeek record generally identifies network endpoints, times, and protocol details. An endpoint record may identify the responsible operating-system process. To connect them, examine the host/address relationship, time, ports, protocol, and available identifiers.

**Speaker notes:** Ask what makes two records plausibly related and what could break the association, such as address translation or time differences.

---

## When packet capture helps

Retained PCAP can add headers or visible content. Missing, partial, or encrypted capture may leave the question unresolved.

**Speaker notes:** Compare an IP-and-port alert with a cleartext request. Then change only the visibility to encrypted traffic and ask how the possible answer changes.

---

## Knowledge check

1. How do analyzers and scripts contribute to Zeek logs?
2. What can endpoint evidence add to a Zeek connection record?
3. When would PCAP add information, and when might it not?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

Zeek supplies structured observations from network traffic. Choose a log according to the question, account for the sensor’s view, and use retained PCAP when it can add relevant evidence.

Previous: [1.1.6 – Image and Driver Load Activity](../../01-endpoint/06-image-driver-load/student-guide.md)

Next: [1.2.2 – Conn Engine](../02-conn-engine/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Zeek — Log files](https://docs.zeek.org/en/master/reference/zeekscript/log-files.html)
- [Zeek — conn.log](https://docs.zeek.org/en/current/reference/logs/conn.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
