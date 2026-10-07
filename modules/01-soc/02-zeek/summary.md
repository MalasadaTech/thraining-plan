# 1.2 – Zeek Network Evidence: Summary

**Module Type:** Subunit synthesis / end-state check — no new proficiency mapping  
**Estimated Time:** 5–10 minutes

## What This Subunit Built

**Network question → protocol/log selection → related records → visibility check → network conclusion**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

## By This Point, You Should Be Able To

- select the Zeek log that best answers a network-investigation question;
- interpret the core evidence each major Zeek log provides;
- connect related network records using shared context;
- explain how sensor visibility and protocol limits affect what Zeek can establish.

## How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **1.2.1 – Zeek Concepts** | Understand Zeek records, timestamps, UIDs, sensors, and evidence boundaries. |
| **1.2.2 – Conn Engine** | Use connection summaries to establish who talked to whom, when, and how much. |
| **1.2.3 – DNS Engine** | Use DNS records to understand name-resolution activity and answers. |
| **1.2.4 – TLS Engine** | Use TLS metadata to interpret encrypted-session context without assuming visibility into encrypted content. |
| **1.2.5 – HTTP Engine** | Use HTTP records to inspect requests and responses when HTTP is visible. |
| **1.2.6 – SMTP Engine** | Use SMTP records to understand mail-flow activity visible to the sensor. |
| **1.2.7 – Files Engine** | Use file-analysis records to connect transferred files with network activity when extraction or hashing is available. |
| **1.2.8 – Weird Engine** | Use protocol anomalies as investigative context rather than automatic proof of malicious activity. |

## Check Your Understanding

Ask yourself:

1. Which Zeek log would you start with to establish the basic endpoints and duration of a connection?
2. Why can a TLS log describe an encrypted session without revealing the application content inside it?
3. What does a shared UID allow you to do during an investigation?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

## Where This Leads Next

The next learning unit is **1.3 – Detection Rules: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

**Next:** [1.3 – Detection Rules: Introduction](../03-detection/intro.md)
