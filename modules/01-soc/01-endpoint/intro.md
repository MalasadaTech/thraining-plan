# 1.1 – Endpoint Activity: Introduction

**Module Type:** Subunit advance organizer — no new proficiency mapping  
**Estimated Time:** 5–10 minutes

## Why This Subunit Matters

Endpoint telemetry records what programs, files, network connections, registry changes, and loaded components did on a host. SOC analysts need to recognize which evidence type can answer a question and how to combine several event types into a defensible picture of host activity.

## Connect to What You Already Know

The SOC orientation introduced the evidence-to-handoff workflow. This subunit begins the evidence side of that workflow by showing what endpoint records can reveal and where each record type has limits.

## What You Will Learn

| Lesson | What it contributes |
|---|---|
| **1.1.1 – Endpoint Activity** | Build the map of endpoint evidence types and the questions they can answer. |
| **1.1.2 – Process Activity** | Interpret process creation, parent-child relationships, command lines, users, and execution context. |
| **1.1.3 – File System Activity** | Interpret file creation, modification, deletion, paths, and hashes. |
| **1.1.4 – Network Activity (Endpoint)** | Connect outbound or inbound network activity to the host and, where available, the initiating process. |
| **1.1.5 – Registry Activity** | Interpret registry changes as host configuration and persistence evidence when the relevant keys and values are present. |
| **1.1.6 – Image and Driver Load Activity** | Interpret loaded modules and drivers as additional execution and trust context. |

## What to Watch For

- Match the question to the endpoint evidence type most likely to answer it.
- Preserve what a field actually says; an event can show that something happened without proving intent or maliciousness.
- Combine events by host, user, process, time, and other shared context rather than treating each record as a complete incident by itself.

## Expected End State

By the end of this subunit, you should be able to:

- identify the major endpoint evidence types and the questions each can answer;
- read common process, file, network, registry, image, and driver-load fields in context;
- connect related endpoint events without overstating what any one event proves;
- recognize when missing telemetry limits the conclusion.

## How to Preview This Subunit

Read this introduction, then skim the [1.1 Summary](summary.md). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

**Next:** [1.1.1 – Endpoint Activity](01-endpoint-activity/student-guide.md)
