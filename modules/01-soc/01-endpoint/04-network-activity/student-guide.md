# Module 1.1.4 – Network Activity (Endpoint)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.4.1 A / B / C ; 1.1.4.2 2b / 3c / 4c ; 1.1.4.3 2b / 3c / 4c  
- Hunter: 1.1.4.1 A / B / B ; 1.1.4.2 1a / 2b / 3c ; 1.1.4.3 1a / 2b / 3c  
- CTI: 1.1.4.1 A / A / A ; 1.1.4.2 1a / 1a / 1a ; 1.1.4.3 1a / 1a / 1a  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret endpoint network addresses, operations, direction, names, and process context.
2. Describe the supplied event with its evidence limits.
3. Create or modify a query for specific endpoint network activity.

**Mapped Proficiency Items:**
- K: 1.1.4.1 – Network activity (endpoint) concepts
- T: 1.1.4.2 – Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.4.3 – Create a SIEM query to detect specific endpoint network activity

## Why This Matters

Endpoint network events connect network activity to a process on a device. That process context can help explain a connection that a network sensor sees only as traffic between addresses.

## 1. Reading the endpoint view

| Detail | What it contributes |
|---|---|
| Local and remote address/port | MDE `LocalIP`, `LocalPort`, `RemoteIP`, and `RemotePort` identify the endpoints. Local/remote alone does not establish who initiated. |
| Protocol and operation | Read the protocol and `ActionType` to distinguish the recorded connection outcome. |
| Direction | Sysmon 3 `Initiated` helps identify whether the process initiated the connection; interpret direction using the source's semantics. |
| Process | Sysmon `Image` or MDE `InitiatingProcess*` associates the activity with a process. |
| Name information | Sysmon 22 `QueryName` records DNS queries when collected. MDE `RemoteUrl` may contain a URL or FQDN; a blank field does not establish that DNS was unused. |

Sysmon 3 concerns network connections; Sysmon 22 concerns DNS queries. MDE uses `DeviceNetworkEvents` for network connections and related observations. Its table and action coverage should be checked locally. A DNS lookup and a subsequent connection are separate observations.

## 2. Working through the example

A supplied MDE event records `ConnectionSuccess`, `Protocol=Tcp`, `RemoteIP=203.0.113.88`, `RemotePort=443`, and initiating process `powershell.exe` with command line `powershell.exe -enc …`. `RemoteUrl` is blank.

A supported description is: “The endpoint recorded a successful TCP connection associated with PowerShell to the remote endpoint `203.0.113.88:443`; no remote URL or FQDN is recorded.” The port alone does not establish HTTPS or Command and Control. The abbreviated command does not establish hidden-window execution. Use source-specific direction evidence before adding “outbound” to the finding.

## 3. Creating a focused network query

The following KQL example illustrates the requested search. Confirm the table, fields, and supported `ActionType` values in your environment before using it. Adjust the time range to the investigation.

```kusto
DeviceNetworkEvents
| where Timestamp > ago(1d)
| where ActionType == "ConnectionSuccess"
| where InitiatingProcessFileName =~ "powershell.exe"
| where RemoteIP == "203.0.113.88" and RemotePort == 443
| project Timestamp, DeviceName, Protocol, LocalIP, LocalPort,
          RemoteIP, RemotePort, RemoteUrl, InitiatingProcessCommandLine
```

This looks for successful connections associated with PowerShell to the specified endpoint. It is an exact destination search for the example, not a general detector for malicious PowerShell. A DNS question instead calls for a DNS-capable source and its query-name field.

## Knowledge Check

1. What does endpoint network evidence add to a native Zeek connection record?
2. What can you say about the supplied TCP/443 event when RemoteUrl is blank?
3. How would you modify the query to find the same destination used by any process?

## Summary

Endpoint network evidence helps connect a process to a recorded network operation. Describe the outcome, endpoints, protocol, and available names, then use a focused query to investigate the chosen pattern.

## Course Connections

Previous: [1.1.3 – File System Activity](../03-file-system-activity/student-guide.md)

Next: [1.1.5 – Registry Activity](../05-registry-activity/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceNetworkEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicenetworkevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
