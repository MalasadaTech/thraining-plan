# Module 1.1.1 – Endpoint activity (the map)  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 15–20 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.1 – Endpoint activity  
**Subtitle:** Overview of host activity types  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This is the start of the SOC analyst track. This lesson names the five kinds of host activity. It does not teach how to read a process-create event.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

An alert usually names a **host**.

That host generated a **log**. Before you describe it, know **what kind of activity** it is.

This lesson is the overview.

**Speaker Notes:**  
This slide is the student intro. Name the kinds before anyone reads process, file, or registry fields. Do not teach fields today.

---

### Slide 3 – Five kinds of host activity
**Title:** Five kinds of host activity

A host generates **logs** when something happens on it.

**Process** — a program ran, ended, or touched another.  
**File** — a file changed.  
**Registry** — a key or value changed.  
**Host-network** — this host talked.  
**Image / driver load** — a DLL or driver loaded.

**Speaker Notes:**  
One line each. Stop. Host-network is the host logging a talk, not Zeek. If they ask about SIEM tables, a log line is an event; in a SIEM it often shows up as a row.

---

### Slide 4 – Same activities, two tools
**Title:** Sysmon and MDE

Two tools. Same five kinds of activity.  
Different field names — not two different sets of facts.

This course uses both as examples.  
This is not how to install Sysmon.

**Speaker Notes:**  
Do not dump Event IDs. The point is that Sysmon and MDE are two encodings of the same host activity.

---

### Slide 5 – Overview now, one kind next
**Title:** Overview now, one kind next

This lesson only names the five kinds.  
The next lessons each cover one kind in detail.

This is **endpoint** telemetry — logs from the host.  
Protocol deep-dive is Zeek (**1.2**).

Name the **kind** before you describe the event.

**Speaker Notes:**  
Keep them on the overview. If you need the classify-the-line examples, use the three givens in the student guide.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Sysmon and MDE are two different stories. True or false?  
2. “A program started on the host.” Which activity type is that?  
3. “This host connected to an IP and port.” Process, or host-network?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Five kinds of host activity.  
Sysmon and MDE record the same kinds with different names.  
Name the kind before you describe the event.

**Speaker Notes:**  
Process activity is next. That lesson is who ran what, not another overview.

---

### Slide 8 – Next
**Title:** Next

**1.1.2** Process activity

**Speaker Notes:**  
1.1.2 is who ran what. The `wscript` → `powershell -enc` example lives there, not here.
