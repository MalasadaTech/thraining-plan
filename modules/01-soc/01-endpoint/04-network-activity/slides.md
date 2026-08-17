# Module 1.1.4 – Network Activity (Endpoint)  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.4 – Network Activity (Endpoint)  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Host-network rows. Who on this device talked. Not Zeek. Not Sysmon install.

---

### Slide 2 – What this hour is
**Title:** What this hour is

SOC analysts read **host** network rows: which **process** talked, and to where.

Not a process create (**1.1.2**).  
Not Zeek (**1.2**). Zeek does not name the process.

**Speaker Notes:**  
Daily alert work: describe the host-network row. Registry waits.

---

### Slide 3 – Address, direction, name
**Title:** IP, port, direction, name when logged

**Source / dest / protocol / direction** — who talked to whom. `Initiated=true` = this process started it.

**Domain / URL** — when the endpoint logged them. Empty ≠ no DNS.

**Speaker Notes:**  
Outline a–b. Port 443 does not make an unexpected initiator “expected.”

---

### Slide 4 – Who talked
**Title:** Initiating process

Sysmon `Image`. MDE `InitiatingProcess*`.

This is the point of **1.1** vs Zeek.  
A `conn` row will not give you this field.

**Speaker Notes:**  
Outline c / e. Do not teach JA3 or `uid` here.

---

### Slide 5 – How it shows up
**Title:** Sysmon and MDE

Sysmon **3** (connect). Sysmon **22** (DNS, if in the feed).

MDE `DeviceNetworkEvents` `ActionType`:  
**ConnectionSuccess** — this process completed a connection.

Same story. Different names. Full `ActionType` list is in the Defender portal — do not invent values.

**Speaker Notes:**  
Outline d. No Event 22 in the feed → “DNS not logged on the endpoint.”

---

### Slide 6 – What good looks like
**Title:** Describe it. Query something specific.

One sentence: which process, to which IP/port, which direction.

**Given:** `powershell.exe -enc …` `ConnectionSuccess` → `203.0.113.88:443`, no URL.

A query names a **specific** pattern — initiator + dest port or remote IP.  
Not “all connections.”

**Speaker Notes:**  
They should see this row before the knowledge check. Hidden encoded PowerShell connected outbound 443. URL not logged. Do not tell the PRD plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A Zeek `conn` row names the initiating process. True or false?  
2. `powershell.exe -enc …` has `ConnectionSuccess` to `203.0.113.88:443` and no `RemoteUrl`. In one sentence, what occurred?  
3. A SIEM query that matches every `DeviceNetworkEvents` row is a good “specific endpoint network” query. True or false?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions for the whole lesson. Stop.

---

### Slide 8 – Summary
**Title:** Summary

Which process talked, to where.  
Direction and initiator tell the story.  
A missing name is a gap.  
Zeek does not name the process.  
A query is specific.

**Next:** **1.1.5** Registry activity

**Speaker Notes:**  
That hour is the registry row on the same host telemetry.
