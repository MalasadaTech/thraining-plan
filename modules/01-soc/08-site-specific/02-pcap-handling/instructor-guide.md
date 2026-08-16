# Instructor Guide – Module 1.8.2 – PCAP Handling

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.8.2.1 2b / 3c / 4c · 1.8.2.2 2b / 3c / 4c  
- Hunter: 1.8.2.1 3c / 4c / 4c · 1.8.2.2 3c / 4c / 4c  
- CTI: 1.8.2.1 1a / 1a / 2b · 1.8.2.2 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach hot vs warm download and the view tool. Force a **get line** plus rejected store/tool. Do not teach Zeek fields or Wireshark install.

**Key Teaching Points:**
- Harbor paths are a stand-in. Overlay the site SOP if you have one.
- No sensor → no download. That is 1.8.1, not a ticket that invents packets.
- Hunter 3-level is already **3c**. CTI is **1a** / **1a** / **2b**. Do not collapse CTI to SOC 2b.
- Zeek log ≠ PCAP is the usual lead.

**Common Student Challenges:**
- conn.log as PCAP.
- Self-serve on warm storage.
- Notepad as a viewer.
- Hitting the UI for OT.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site PCAP SOP
- Answer key (this guide)

---

## Learning Objectives

1. Download path (hot / warm / none).
2. View tool vs not.
3. Get line + reject.

**Mapped Items:** T 1.8.2.1 · T 1.8.2.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 1.2 / 1.8.1-as-export / 1.8.3 |
| Hot / warm / viewer            | 14 min   | tasks 1–2 |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~64 min** | Stretch Ex 2 if they defend Zeek |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: 2b — copy the card row for this timestamp.
- If Wireshark is missing, point at **1.8.3.2** and come back. Do not teach the install ticket here.

**Question:**  
“span-2 was down 13:10–13:40 (1.7.2). Can `PCAP-REQ` recover that window?” (No. The sensor was dark. Ticket cannot invent packets.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail Zeek-as-PCAP. Fail Notepad. Fail OT UI.

**Summaries:**
- Ex 1: hot UI span-1 + Wireshark.
- Ex 2: wrong store / wrong tool.
- Ex 3: OT = none; seven-day internet would be PCAP-REQ.

**Cases:**

| Item | Sensor | Clock | Path | Tool | Reject |
|------|--------|-------|------|------|--------|
| A | span-2 | Hot | `pcap.harbor.internal` | Wireshark | Zeek / span-1-only |
| B | span-1 | Warm (6d) | **`PCAP-REQ`** → `\\soc-pcap\export\<case>\` | Wireshark | Hot UI |
| C | as given | — | (file already in hand) | **Wireshark** (or tshark) | Notepad |
| D | **none** | — | **none** | — | UI anyway |

---

## Knowledge Check – Answer Key

1. **UI vs PCAP-REQ?**  
   **Answer:** Harbor: last 24h → UI. Older → `PCAP-REQ` and the share.  
   **Explanation:** Task 1.

2. **No sensor?**  
   **Answer:** No download. Name the **1.8.1** gap. A ticket cannot create a span.  
   **Explanation:** Fence / Example 3.

3. **View tool / not?**  
   **Answer:** Wireshark (tshark if headless). Not Notepad, Excel, browser, Zeek log.  
   **Explanation:** Task 2.

4. **Why not Zeek?**  
   **Answer:** Zeek is parsed logs (**1.2**), not packets.  
   **Explanation:** Example 2.

5. **Live-org paths?**  
   **Answer:** Site PCAP SOP. Classroom UI / share / 24h are for this lesson.  
   **Explanation:** Same pattern as 1.6.2 / 1.7.

---

## Additional Instructor Resources

- Site PCAP SOP
- Next recommended module: 1.8.3 Tool access and requests
