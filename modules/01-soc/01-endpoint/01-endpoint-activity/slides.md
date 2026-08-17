# Module 1.1.1 – Endpoint activity (the map)  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 15–20 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 1.1.1 – Endpoint activity  
**Subtitle:** SOC Analyst (Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Start of the SOC analyst block. This hour is the map of host rows. Not how to read a process create.

---

### Slide 2 – What this hour is
**Title:** What this hour is

An alert will point at a **host**.

Before you describe a row, know **which kind of row** it is.

This hour is that map.

**Speaker Notes:**  
You wanted this in front of process / file / registry. Do not teach fields today.

---

### Slide 3 – Five kinds
**Title:** What a host leaves

**Process** — a program ran, ended, or touched another.  
**File** — a file changed.  
**Registry** — a key or value changed.  
**Host-network** — this host talked.  
**Image / driver load** — a DLL or driver loaded.

**Speaker Notes:**  
Outline a. One line each. Stop.

---

### Slide 4 – Same activities, two encodings
**Title:** Sysmon and MDE

Two encodings of the **same** activities.  
Not two different stories.

This course uses both as examples.  
Not how to install Sysmon.

**Speaker Notes:**  
Outline b. Do not dump Event IDs.

---

### Slide 5 – One type at a time
**Title:** The map, then one row

This hour is only the map.

Endpoint telemetry. Zeek is **1.2**.

An alert points at a host. Know the **kind** before you describe it.

**Speaker Notes:**  
Outline c–e. Walk the three student-guide givens if you need them.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Sysmon and MDE are two different stories. True or false?  
2. “A program started on the host.” Which activity type is that?  
3. “This host connected to an IP and port.” Process, or host-network?

**Speaker Notes:**  
Answers only in the instructor guide. Three questions for the whole lesson. Stop.

---

### Slide 7 – Summary
**Title:** Summary

Five kinds of host rows.  
Sysmon and MDE encode the same activities.  
Know the kind before you describe the row.

**Speaker Notes:**  
Process row is next.

---

### Slide 8 – Next
**Title:** Next

**1.1.2** Process activity

**Speaker Notes:**  
That hour is who ran what. The alert beat (`wscript` → `powershell -enc`) lives there.
