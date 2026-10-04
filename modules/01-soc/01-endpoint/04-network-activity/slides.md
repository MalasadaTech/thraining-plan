# Module 1.1.4 – Network Activity (Endpoint)

- Interpret endpoint network addresses, operations, direction, names, and process context.
- Describe the supplied event with its evidence limits.
- Create or modify a query for specific endpoint network activity.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

Endpoint network events connect network activity to a process on a device. That process context can help explain a connection that a network sensor sees only as traffic between addresses.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Reading the endpoint view

Read outcome, endpoints, protocol, direction evidence, names, and associated process. Local/remote does not by itself establish initiation.

**Speaker notes:** Distinguish local/remote from source/destination and initiation. Use Sysmon Initiated as one concrete source-specific example.

---

## Reference — Reading the endpoint view

| Detail | What it contributes |
|---|---|
| Local and remote address/port | MDE `LocalIP`, `LocalPort`, `RemoteIP`, and `RemotePort` identify the endpoints. Local/remote alone does not establish who initiated. |
| Protocol and operation | Read the protocol and `ActionType` to distinguish the recorded connection outcome. |
| Direction | Sysmon 3 `Initiated` helps identify whether the process initiated the connection; interpret direction using the source's semantics. |
| Process | Sysmon `Image` or MDE `InitiatingProcess*` associates the activity with a process. |
| Name information | Sysmon 22 `QueryName` records DNS queries when collected. MDE `RemoteUrl` may contain a URL or FQDN; a blank field does not establish that DNS was unused. |

**Speaker notes:** Distinguish local/remote from source/destination and initiation. Use Sysmon Initiated as one concrete source-specific example. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Working through the example

PowerShell is associated with a recorded successful TCP connection to 203.0.113.88:443. The record lacks a URL/FQDN.

**Speaker notes:** Have learners build the sentence from supplied fields; discuss why a commonly used port is insufficient to identify application behavior.

---

## Supplied example

A supplied MDE event records `ConnectionSuccess`, `Protocol=Tcp`, `RemoteIP=203.0.113.88`, `RemotePort=443`, and initiating process `powershell.exe` with command line `powershell.exe -enc …`. `RemoteUrl` is blank.

**Speaker notes:** Have learners build the sentence from supplied fields; discuss why a commonly used port is insufficient to identify application behavior.

---

## Creating a focused network query

Search the specified process and destination. A connection query and a DNS query answer different questions.

**Speaker notes:** Ask what broadens when the process filter is removed. This tests query reasoning without requiring a live connection or tenant.

---

## Reference — Creating a focused network query

| where Timestamp > ago(1d)
| where ActionType == "ConnectionSuccess"
| where InitiatingProcessFileName =~ "powershell.exe"
| where RemoteIP == "203.0.113.88" and RemotePort == 443
| project Timestamp, DeviceName, Protocol, LocalIP, LocalPort,

**Speaker notes:** Ask what broadens when the process filter is removed. This tests query reasoning without requiring a live connection or tenant. Use the surrounding student-guide explanation to interpret the table and its limits.

---

## Worked example — Creating a focused network query

```kusto
DeviceNetworkEvents
| where Timestamp > ago(1d)
| where ActionType == "ConnectionSuccess"
| where InitiatingProcessFileName =~ "powershell.exe"
| where RemoteIP == "203.0.113.88" and RemotePort == 443
| project Timestamp, DeviceName, Protocol, LocalIP, LocalPort,
          RemoteIP, RemotePort, RemoteUrl, InitiatingProcessCommandLine
```

**Speaker notes:** Ask what broadens when the process filter is removed. This tests query reasoning without requiring a live connection or tenant. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Knowledge check

1. What does endpoint network evidence add to a native Zeek connection record?
2. What can you say about the supplied TCP/443 event when RemoteUrl is blank?
3. How would you modify the query to find the same destination used by any process?

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

Endpoint network evidence helps connect a process to a recorded network operation. Describe the outcome, endpoints, protocol, and available names, then use a focused query to investigate the chosen pattern.

Previous: [1.1.3 – File System Activity](../03-file-system-activity/student-guide.md)

Next: [1.1.5 – Registry Activity](../05-registry-activity/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceNetworkEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicenetworkevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
