# Instructor Guide – Module 2.11.2 – Disseminating intelligence to the correct audiences

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.11.2 B / C / C ; 2.11.2.1 3c / 4c / 4c ; 2.11.2.2 3c / 4c / 4d ; 2.11.2.3 3c / 4c / 4c  
- Hunter: 2.11.2 A / B / B ; 2.11.2.1 1a / 2b / 3c ; 2.11.2.2 1a / 2b / 3c ; 2.11.2.3 1a / 2b / 3c  
- SOC: 2.11.2 A / A / B ; 2.11.2.1 1a / 1a / 2b ; 2.11.2.2 1a / 1a / 2b ; 2.11.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Route the finished product: audience, approved channel, handling marking, and caveat. Reject SMS. Classroom TLP is a stand-in, not live org policy.

**Context (plain language):**

- What this lesson is for: CTI analysts send the finished product to the people who can use it, on a path the shop already approved, with a label that says who else may see it.
- How it hooks to the lesson before: 2.11.1 wrote the finished product. This lesson is the send.
- How it hooks to the lesson after: 2.11.3 is answering the RFI itself.
- Why we are doing it this way: the product exists; the remaining job is who, how, and with which marking. A classroom TLP and channel card is a stand-in so the route task has something to apply. Overlay a real shop card if they have one. It is not live org policy.
- What we are *not* doing in this lesson: Invent a DYA TLP scheme or customer list. Rewrite the judgment. SOC ticket types. STIX or TAXII. RFI handling. Local approval. No lab.
- Extra step: none.

Use the same names as the student guide: **audience**, **approved channel**, **handling marking**, **handling caveat**, and **TLP:AMBER**. **TLP** means Traffic Light Protocol used as a practice label. Do not invent `TLP-RED-DYA`. Do not tell the PRD plot. Leadership gets a short awareness line, not the hash.

**Key Teaching Points:**
- Name audience, approved channel, and marking before you send.
- Ticket or approved intel channel. Personal SMS, private chat, and public post fail.
- Leadership: still marked, no hash. Same facts as the IR send.

**Common Student Challenges:**
- Send via SMS because it is faster. Why: they think speed beats the approved path. Example: texting the duty lead instead of the ticket.
- Invent a DYA marking. Why: they want a house color. Example: writing `TLP-RED-DYA` instead of the classroom card or the shop’s real card.
- Change the judgment when they tailor. Why: they think leadership needs certainty. Example: dropping **likely** so the one-liner sounds proven.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.11.2 – Disseminating intelligence to the correct audiences
- T: 2.11.2.1 – Select audience and method and apply correct handling markings
- T: 2.11.2.2 – Tailor products to different audiences (technical, leadership, etc.)
- T: 2.11.2.3 – Disseminate intelligence products through approved channels

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Send the finished product on an approved path |
| Key Concepts            | 12 min    | Audience, channel, marking; two A12 routes |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: the finished product has to reach the people who can use it, on a path the shop already approved, with a label that says who else may see it.
- Write audience, channel, marking, and caveat. Stop there. Do not invent a customer list.
- Walk the classroom card. **TLP:AMBER** is need-to-know inside the organization. **TLP:CLEAR** is not for a product that names a live host. These names are lesson-only.
- Overlay a real shop card if they have one. If they invent `TLP-RED-DYA`, send them back to the classroom card or their shop card.
- Walk the two **A12** sends from the student guide. Same facts. IR gets host, `invoice.vbs`, and domain on a ticket. Leadership gets one line, no hash, still marked, still on an approved channel.
- If they defend personal SMS, it is the right people on the wrong path.
- If they rewrite the judgment for leadership, that is 2.1.6 / 2.11.1. This lesson does not change **likely**.
- If they start listing local customers, that is 2.12.3. Obtain the chart later. Do not invent one here.
- If they treat this as SOC incident routing, 1.5.3 already taught that chart. This lesson is the finished intel product.

---

## Knowledge Check – Answer Key

1. **Personal SMS is fine if leadership needs it fast. True or false?**  
   **Answer:** False.  
   **Explanation:** Speed does not approve the path. Personal SMS, private chat, and public post fail even when the duty lead is the right person.

2. **What three things do you name to route a product?**  
   **Answer:** Audience, approved channel, and handling marking.  
   **Explanation:** Who owns the next decision, how it travels, and who else may see it. A caveat can still restrict the send after those three are named.

3. **A12 to IR vs leadership — one difference in detail, and one rejected channel?**  
   **Answer:** IR gets host, `invoice.vbs`, and the update domain. Leadership gets one line and no hash. Reject personal SMS or private chat.  
   **Explanation:** Same facts, different detail. Both sends stay on an approved channel and stay marked.

---

## Additional Instructor Resources

- Next: 2.11.3 Handling RFIs
