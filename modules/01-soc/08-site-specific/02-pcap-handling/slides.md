# Module 1.8.2 – PCAP Handling  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.8.2 – PCAP Handling  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Get the file. Open it. Overlay site SOP if you have one.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. How to download (hot / warm / none)
2. Which tool views it
3. Reject the wrong store and tool

**Mapped Items:**  
T: 1.8.2.1 | T: 1.8.2.2

**Speaker Notes:**  
CTI is 1a / 1a / 2b.

---

### Slide 3 – Agenda
**Title:** Agenda

- Harbor PCAP card
- Three examples
- Four get lines
- Knowledge check

**Speaker Notes:**  
1.8.3 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Where the sensor **sits** (**1.8.1.g**)  
Zeek fields (**1.2**)  
Install Wireshark (**1.8.3**)  
Payload analysis

**Key Point:** Path + viewer.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Download
**Title:** Hot vs Warm vs None

**≤24h:** `https://pcap.harbor.internal`  
**Older:** ticket `PCAP-REQ` → `\\soc-pcap\export\<case>\`  
**No sensor:** **none**

**Speaker Notes:**  
Task 1.

---

### Slide 6 – View
**Title:** Open the File

**Wireshark.** tshark if headless.  
Not Notepad. Not Excel. Not “the Zeek log.”

**Speaker Notes:**  
Task 2.

---

### Slide 7 – Get Line
**Title:** Five Fields

`sensor | hot/warm/none | path | tool | rejected`

**Speaker Notes:**  
Both tasks in one line.

---

### Slide 8 – Sensor Reminder
**Title:** You Cannot Export a Missing Span

Harbor: **no** sensor on `fw-ot`.  
`PCAP-REQ` does not create packets.

**Speaker Notes:**  
1.8.1.g fence.

---

### Slide 9 – Example 1: Hot A12
**Title:** Example 1 – span-1 Today

UI + Wireshark.  
Not the `http` log.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Zeek
**Title:** Example 2 – conn.log Is Not PCAP

Right window. Wrong store. Wrong tool.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3: Warm / None
**Title:** Example 3 – Two Different Fails

OT = **none**.  
Seven-day internet = **`PCAP-REQ`**.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Zeek as PCAP  
- Hot UI on day-6  
- Notepad  
- UI for OT  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use the site SOP if posted.  
Keep: how you get it + what opens it.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize Ex 1–3.
2. A–D: get line.
3. No payload analysis.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. UI vs PCAP-REQ?
2. No sensor — what then?
3. View tool — and one that is not?
4. Why not Zeek?
5. Who owns live-org paths?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Hot UI / warm ticket / no sensor = none.
- Wireshark, not Zeek-as-PCAP.
- Next: **1.8.3** tool URLs and request tickets.

**Speaker Notes:**  
Do not open 1.8.3 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** PCAP — Quick Reference

| Clock | Path | View |
|-------|------|------|
| ≤24h | pcap.harbor.internal | Wireshark |
| Older | PCAP-REQ → share | Wireshark |
| No sensor | none | — |

**Coming next:** Module 1.8.3 – Tool access

**Footer:** SOC / Hunter / CTI Training Program
