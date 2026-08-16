# Module 1.8.2 – PCAP Handling

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.8.2.1 2b / 3c / 4c · 1.8.2.2 2b / 3c / 4c  
- Hunter: 1.8.2.1 3c / 4c / 4c · 1.8.2.2 3c / 4c / 4c  
- CTI: 1.8.2.1 1a / 1a / 2b · 1.8.2.2 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name **how to download** PCAP for a given case (self-serve vs ticket).
2. Name **which tool** you use to view it.
3. Reject the wrong store and the wrong tool.

**Mapped Proficiency Items:**
- T: 1.8.2.1 – How to download PCAP
- T: 1.8.2.2 – What tool to use to view PCAP

---

## 1. Key Concepts

You already know **where sensors sit** (**1.8.1.g**). This hour is **get the file** and **open it**. Zeek `conn`/`http` logs are not PCAP (**1.2**). Installing Wireshark is **1.8.3**.

**Classroom PCAP card (this lesson only):**

| Clock | How you get the file |
|-------|----------------------|
| **Last 24 hours** | Self-serve UI **`https://pcap.harbor.internal`** — pick sensor + time + 5-tuple, Export |
| **Older than 24 hours** | Ticket **`PCAP-REQ`** to the sensor team. Pickup: `\\soc-pcap\export\<case>\` |
| **No sensor** | You **cannot** download. Say the **1.8.1** gap (Harbor: no span on `fw-ot`). |

**View tool (outline 2):** **Wireshark** (interactive). **tshark** if you only have a shell.  
**Not a viewer:** Notepad, Excel, a browser, “just read the Zeek log.”

| This lesson | Other |
|-------------|-------|
| Path + viewer | Which sensor exists — **1.8.1.g** |
| Not Zeek fields | **1.2** |
| Not “install Wireshark” | **1.8.3.2** |

The task is a **get line**:

`sensor | clock (hot/warm/none) | download path | view tool | rejected`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| A12 14:00 span-1, still hot → UI + Wireshark | Exporting `conn.log` and calling it PCAP |
| Seven-day-old session → `PCAP-REQ` + share | Self-serve UI for warm storage |
| ot-hist-01 → **none** (no sensor) | Inventing a span-2 download |

---

## 2. Detailed Walkthrough / Examples

Now = **15:00** same day unless stated.

### Example 1: Hot A12 on span-1 (Expected)

**Need:** packets for `WS-JLEE` → `203.0.113.88:8080` at 14:05. Sensor from **1.8.1**: **span-1**.

**Download:** Hot (55 min old) → **`https://pcap.harbor.internal`**, sensor span-1, export.  
**View:** **Wireshark**.  
**Reject:** Opening the Zeek `http` log as the PCAP.

### Example 2: Zeek Log Is Not PCAP (Lead)

**Draft:** “I pulled `conn.log` for the uid from the SIEM. That’s the PCAP.”

**Correct:** Download from the **PCAP UI** (or `PCAP-REQ` if warm). View in **Wireshark**.  
**Reject:** Zeek logs. They are **1.2**, useful, not packets.  
**Lead:** Right time window. Wrong store. Wrong tool.

### Example 3: Warm + No OT Sensor (Lead)

**Need:** packets from **seven days ago** on `ot-hist-01`.

**Download:** Sensor = **none** (**1.8.1.g**). There is no file to export. A `PCAP-REQ` cannot create a span.  
**If** the ask were seven-day **span-1** (internet): **`PCAP-REQ`**, pickup `\\soc-pcap\export\<case>\`, still **Wireshark**.  
**Lead:** Warm vs none are different fails. Name which.

---

## 3. Hands-On Exercise

**Objective:** Write the get line (path + tool) and reject the wrong pair.

**Use the Harbor PCAP card.** Now = 15:00 today.

**Instructions:**

1. One sentence each for Examples 1–3: path + tool + rejected.
2. For each item, write the **get line**.

   - A. span-2, WS-JLEE ↔ `dc-01`, 14:40 today.
   - B. span-1, same 5-tuple, **six days** ago.
   - C. Someone opened the `.pcap` in Notepad because “it’s text.”
   - D. OT historian, any time. They want you to hit the UI anyway.

3. Do not analyze the payloads. Do not file a 1.8.3 install ticket unless you *label* that Wireshark is missing (that is a different unit).
4. If the sensor does not exist, the download path is **none**.

**Expected Outcome:**
- Three example summaries
- Four get lines
- No Zeek field drill, no IR

---

## 4. Knowledge Check

1. When do you use the **UI** vs **`PCAP-REQ`**?
2. What do you do if **1.8.1** says there is **no sensor**?
3. What is the Harbor **view** tool? Name one thing that is **not**.
4. Why is a Zeek log not a PCAP download?
5. Who owns live-org paths if they differ from Harbor?

---

## 5. Summary

- Hot UI / warm ticket / no sensor = none.
- View in Wireshark (or tshark). Not Zeek-as-PCAP.
- Next: tool URLs and request tickets (**1.8.3**).

---

## 6. References & Further Reading

- Related modules:
  - 1.8.1 – Environment orientation (sensors)
  - 1.8.3 – Tool access and requests (next)
  - 1.2.2 – Conn engine (not PCAP)
- Local PCAP SOP (optional — substitutes Harbor paths)
