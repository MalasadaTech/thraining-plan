# Module 3.12.3 – Local Dissemination Channels and Customers

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.12.3 A / A / A · 3.12.3.1 1a / 1a / 1a  
- Hunter: 3.12.3 A / A / B · 3.12.3.1 1a / 1a / 2b  
- CTI: 3.12.3 B / C / C · 3.12.3.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. State that **customers and channels are local** — every section posts its own list.
2. Treat obtaining that list as **early orientation**.
3. **Disseminate** only on what the *site* list allows — after you have it.
4. **Reject** using the **3.11.2** classroom TLP card as this section’s customer list, and reject inventing recipients.

**Mapped Proficiency Items:**
- K: 3.12.3 – Local dissemination channels and customers
- T: 3.12.3.1 – Disseminate a product using the correct local channels and customers

---

## 1. Key Concepts

**3.11.2** taught *generic* audience / TLP / “not Slack.” This hour is **your section’s** customer and channel list. SOC routing is **1.6.3**. TAXII is **3.10.2**. Local *approval* is **3.12.2**.

This course **does not** name your customers. Do not invent a roster (“always send to [agency]”). A new analyst asks and records the list.

**Customers and channels (outline a–b) — what exists, not the names:**

| You will be shown (locally) | You do **not** do this hour |
|-----------------------------|-----------------------------|
| Who inside is a **customer** of this section | Invent a partner list |
| Which **channels** that list allows | Treat 3.11.2 classroom TIP/DL/ticket/brief as *this site’s* list |
| Any extra **caveat** the site adds on top of TLP | Invent a classification system |

**3.11.2 still applies as a floor:** personal Slack and public posts are still wrong unless the *local* list you were actually shown says otherwise. This packet does not say otherwise.

**Orientation line:**  
`who I asked | where they pointed | I have / do not have the local customer-channel list | next step`

**Send line:**  
`product | list I was actually shown | channel/customer from that list | I send / I still need the list / I invented a recipient (fail)`

No list shown → **do not send**.

| This lesson | Other |
|-------------|-------|
| *This section’s* list | Classroom TLP + generic approved-vs-Slack — **3.11.2** |
| Not SOC notification matrix | **1.6.3** |
| Not TAXII collection | **3.10.2** |
| Not approval/archive | **3.12.2** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| “Asked lead; no customer list in this packet; I will not send” | “Send to [invented agency] and the CEO DL” |
| Wait for the local list | “3.11.2 said TIP + ticket, so that *is* our list” |

---

## 2. Detailed Walkthrough / Examples

**Work on the desk:** Night Owl activity note, approved locally *if* 3.12.2 was shown — otherwise still waiting. Either way you still need **customers**.

### Example 1: Honest Orientation (Expected)

**Ask:** lead — who gets our products, on which channels.  
**Shown:** nothing in *this* packet.  
**Send:** do not send. Get the list.

### Example 2: 3.11.2 Card as Local Policy (Lead)

**Draft:** “3.11.2 said TIP and SOC ticket. That is our customer list. I sent it.”

**Fail.** 3.11.2 is the *generic* classroom card. This hour requires the **section** list.  
**Lead:** Training example ≠ site policy (same as PIR-1).

### Example 3: Invented Recipient (Lead)

**Draft:** “Always copy [external agency] and post internally.”

**Fail.** Invented customers.  
**Lead:** You do not know the local list until someone shows it.

---

## 3. Hands-On Exercise

**Objective:** Orient to the local customer/channel list. Send only from a list you were shown.

**This packet contains no customer roster. That is intentional.**

**Instructions:**

1. One sentence each for Examples 1–3.
2. **Orient:** one **orientation line** (you do not have the local list in this packet).
3. **Send** (task): **send lines** for:

   - A. Night Owl note, no local list shown.  
   - B. “Use the 3.11.2 classroom channels as our official list.”  
   - C. “Add [an agency you invented] as a standing customer.”  
   - D. Instructor overlays a real site list (if they do). Send *only* on that text. If they do not, write “still need the list.”

4. Do not invent customers. Do not re-teach TLP. Do not skip **3.12.2** approval by sending.
5. Slack/public remains reject unless a *shown* local list says otherwise — this packet does not.

**Expected Outcome:**
- Three example summaries
- One orientation line
- Four send lines (A–C fail or “need the list”; D only if overlaid)
- No invented roster

---

## 4. Knowledge Check

1. How is this hour **different** from **3.11.2**?
2. What belongs on an **orientation line**?
3. Can you send if no local list has been shown?
4. Why is “always copy [agency]” a fail here?
5. If Slack is on a **real** local list your lead showed you, what do you do?

---

## 5. Summary

- Obtain the local customer/channel list. Send only from that list. Do not invent it. Do not substitute the 3.11.2 classroom card.
- This closes unit **3.12** and the CTI `3.x` track in this curriculum.

---

## 6. References & Further Reading

- Related modules:
  - 3.12.2 – Local production/approval (previous)
  - 3.11.2 – Generic markings and approved-vs-Slack
  - 1.6.3 – SOC routing
- Your lead and the customer/channel list they name (not this repo)
