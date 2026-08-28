# Module 1.1.4 – Network Activity (Endpoint)  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 25–30 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.4 – Network Activity (Endpoint)  
**Subtitle:** Which process on this device talked  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
1.1.3 was the file event on the same host. This lesson is the host-network kind. It is not Zeek and not how to install Sysmon.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

SOC analysts read **host-network** events to see which process on this device talked, and to where.

The point versus Zeek is the initiating process.  
Not Zeek. Not how to install Sysmon.

**Speaker Notes:**  
This is daily alert work: describe the endpoint network log. Registry and Zeek wait for later lessons.

---

### Slide 3 – Address, direction, name
**Title:** IP, port, direction, name when logged

**Source / dest / protocol / direction** — who talked to whom. `Initiated=true` = this process started it.

**Domain / URL** — when the endpoint logged them. Empty ≠ no DNS.

**Speaker Notes:**  
Walk address and direction first. Port 443 does not make an unexpected initiator “expected.” A missing name is a gap, not proof that DNS never happened.

---

### Slide 4 – Who talked
**Title:** Initiating process

Sysmon `Image`. MDE `InitiatingProcess*`.

This is the point of this lesson versus Zeek.  
A `conn` log will not give you this field.

**Speaker Notes:**  
The host-network event names who opened the socket. Do not teach JA3 or Zeek `uid` here.

---

### Slide 5 – How it shows up
**Title:** Sysmon and MDE

Sysmon **3** (connect). Sysmon **22** (DNS, if in the feed).

MDE `DeviceNetworkEvents` `ActionType`:  
**ConnectionSuccess** (this process completed a connection).

Same activity. Different field names.  
The full `ActionType` list is in the Defender portal — do not invent values.

**Speaker Notes:**  
DNS on the endpoint is Sysmon 22 when that event is in the feed. No Event 22 → “DNS not logged on the endpoint.” Do not teach Sysmon install.

---

### Slide 6 – Describe it. Query something specific.
**Title:** Describe it. Query something specific.

One sentence: which process, to which IP/port, which direction.

**Given:** `powershell.exe -enc …` `ConnectionSuccess` → `203.0.113.88:443`, no URL.

A query names a **specific** pattern — initiator + dest port or remote IP.  
Not “all connections.”

**Speaker Notes:**  
Show this given before the knowledge check. One sentence: hidden encoded PowerShell connected outbound 443. URL not logged. Do not tell the intro plot.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. A Zeek `conn` log names the initiating process. True or false?  
2. `powershell.exe -enc …` has `ConnectionSuccess` to `203.0.113.88:443` and no `RemoteUrl`. In one sentence, what occurred?  
3. A SIEM query that matches every endpoint network event is a good “specific endpoint network activity” query. True or false?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

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
1.1.5 is the registry event on the same host telemetry. Stay off this host-network event when you get there.
