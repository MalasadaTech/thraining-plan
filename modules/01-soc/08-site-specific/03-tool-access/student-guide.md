# Module 1.8.3 – Tool Access and Requests

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.8.3.1 2b / 3c / 4c · 1.8.3.2 2b / 3c / 4c · 1.8.3.3 2b / 3c / 4c  
- Hunter: 1.8.3.1 3c / 4c / 4c · 1.8.3.2 3c / 4c / 4c · 1.8.3.3 3c / 4c / 4c  
- CTI: 1.8.3.1 2b / 3c / 4c · 1.8.3.2 2b / 3c / 4c · 1.8.3.3 2b / 3c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Open a required tool by its **URL**.
2. File an **install** request when the binary is missing.
3. File an **access** request when you have the URL but no entitlement.
4. Reject the neighbor action (random download, shared password).

**Mapped Proficiency Items:**
- T: 1.8.3.1 – How to access required tools and their URLs
- T: 1.8.3.2 – How to request tools to be installed
- T: 1.8.3.3 – How to request access (e.g., SIEM)

---

## 1. Key Concepts

This hour is **how you get onto the tool**. PCAP *export* is **1.8.2**. Where notes live is **1.8.4**.

**Classroom tool card (this lesson only):**

| Tool | URL / path | If you cannot use it |
|------|------------|----------------------|
| SIEM | `https://siem.harbor.internal` | **`ACCESS-REQ`** to SOC-IT |
| EDR | `https://edr.harbor.internal` | **`ACCESS-REQ`** |
| PCAP UI | `https://pcap.harbor.internal` | **`ACCESS-REQ`** (login) — old export is **1.8.2** `PCAP-REQ` |
| Tickets | `https://ticket.harbor.internal` | **`ACCESS-REQ`** |
| Wireshark | Local install | **`SOFT-REQ`** to desktop IT |
| Editor | Local | **`SOFT-REQ`** |

Three actions — pick **one**:

| Action | When | Not |
|--------|------|-----|
| **Open the URL** | You have the account and the link | Guessing a bookmark |
| **`SOFT-REQ`** | The **program is not on the box** | Download from a random mirror |
| **`ACCESS-REQ`** | The URL works; **you get 403 / no account** | Using Pat’s laptop / shared password |

| This lesson | Other |
|-------------|-------|
| Open / install / entitle | Export the pcap **file** — **1.8.2** |
| Not where notes are saved | **1.8.4** |
| Not the IR page step | **1.8.5** |

The task is an **access line**:

`need | action (open / SOFT-REQ / ACCESS-REQ) | URL or ticket | rejected neighbor`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| SIEM in browser → open URL | SIEM 403 → ACCESS-REQ (not SOFT-REQ) |
| No Wireshark → SOFT-REQ | Wireshark from an unofficial site |
| No EDR account → ACCESS-REQ | “Use Pat’s session” |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Open SIEM (Expected)

**Need:** query DeviceProcessEvents for `WS-JLEE`. You have a SIEM account.

**Action:** **Open** `https://siem.harbor.internal`.  
**Reject:** Emailing a teammate “can you run this for me” as the *only* path when you have access.

### Example 2: Wireshark from a Mirror (Lead)

**Need:** view the A12 pcap. Wireshark is not installed.

**Action:** **`SOFT-REQ`** to desktop IT.  
**Reject:** Download from a random internet mirror.  
**Lead:** Right tool (**1.8.2.2**). Wrong *how you get the binary*.

### Example 3: EDR 403 (Lead)

**Need:** isolate check on `WS-JLEE`. EDR URL loads. You get **403**.

**Action:** **`ACCESS-REQ`** (entitlement).  
**Reject:** **`SOFT-REQ`** (it is not a missing install). Reject using Pat’s logged-in browser.  
**Lead:** Right URL. Wrong request type if they file SOFT-REQ.

---

## 3. Hands-On Exercise

**Objective:** Write the access line and reject the neighbor action.

**Use the Harbor tool card.**

**Instructions:**

1. One sentence each for Examples 1–3: action + rejected.
2. For each item, write the **access line**.

   - A. You need the ticket system. You have a login.
   - B. tshark/Wireshark missing on a new SOC laptop.
   - C. PCAP UI 403. You need to *look* at hot exports (not a 6-day retrieval).
   - D. Teammate pastes their SIEM password in chat “so you can keep moving.”

3. Do not export PCAP (**1.8.2**). Do not write the IR isolate step (**1.8.5**).
4. If two tickets could be argued, pick the one the *blocker* is (no binary vs no login).

**Expected Outcome:**
- Three example summaries
- Four access lines
- No PCAP get-line redo, no notes path

---

## 4. Knowledge Check

1. When do you **open the URL** instead of filing a ticket?
2. What ticket gets **Wireshark** onto a laptop? What do you **not** do?
3. SIEM **403** — which ticket, and why not `SOFT-REQ`?
4. How is `ACCESS-REQ` for the PCAP **UI** different from **1.8.2** `PCAP-REQ`?
5. Why is a shared password not an access request?

---

## 5. Summary

- Open / `SOFT-REQ` / `ACCESS-REQ`. Reject the neighbor.
- Next: where investigation notes go (**1.8.4**).

---

## 6. References & Further Reading

- Related modules:
  - 1.8.2 – PCAP handling (previous)
  - 1.8.4 – Investigation documentation (next)
- Local tool / IAM catalog (optional — substitutes Harbor URLs)
