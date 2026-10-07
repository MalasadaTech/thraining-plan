# 1.2 – Zeek Network Evidence: Introduction

**Module Type:** Subunit advance organizer — no new proficiency mapping  
**Estimated Time:** 5–10 minutes

## Why This Subunit Matters

Zeek turns observed network traffic into protocol-aware logs. The analyst skill is learning which log answers which question, how related records connect, and what the sensor can and cannot tell you about activity it observed.

## Connect to What You Already Know

Endpoint evidence showed what a host recorded locally. Zeek adds a network-sensor view, which can confirm, complement, or fail to observe parts of the same activity depending on where the sensor sits and what protocols are visible.

## What You Will Learn

| Lesson | What it contributes |
|---|---|
| **1.2.1 – Zeek Concepts** | Understand Zeek records, timestamps, UIDs, sensors, and evidence boundaries. |
| **1.2.2 – Conn Engine** | Use connection summaries to establish who talked to whom, when, and how much. |
| **1.2.3 – DNS Engine** | Use DNS records to understand name-resolution activity and answers. |
| **1.2.4 – TLS Engine** | Use TLS metadata to interpret encrypted-session context without assuming visibility into encrypted content. |
| **1.2.5 – HTTP Engine** | Use HTTP records to inspect requests and responses when HTTP is visible. |
| **1.2.6 – SMTP Engine** | Use SMTP records to understand mail-flow activity visible to the sensor. |
| **1.2.7 – Files Engine** | Use file-analysis records to connect transferred files with network activity when extraction or hashing is available. |
| **1.2.8 – Weird Engine** | Use protocol anomalies as investigative context rather than automatic proof of malicious activity. |

## What to Watch For

- Start with the network question, then choose the log that contains the relevant protocol evidence.
- Use shared identifiers such as Zeek UIDs and timing to connect records across logs.
- Keep sensor placement, encryption, logging configuration, and protocol visibility in mind before interpreting a missing field or missing record.

## Expected End State

By the end of this subunit, you should be able to:

- select the Zeek log that best answers a network-investigation question;
- interpret the core evidence each major Zeek log provides;
- connect related network records using shared context;
- explain how sensor visibility and protocol limits affect what Zeek can establish.

## How to Preview This Subunit

Read this introduction, then skim the [1.2 Summary](summary.md). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

**Next:** [1.2.1 – Zeek Concepts](01-concepts/student-guide.md)
