# Module 2.11.2 – Disseminating intelligence to the correct audiences

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.11.2 B / C / C ; 2.11.2.1 3c / 4c / 4c ; 2.11.2.2 3c / 4c / 4d ; 2.11.2.3 3c / 4c / 4c  
- Hunter: 2.11.2 A / B / B ; 2.11.2.1 1a / 2b / 3c ; 2.11.2.2 1a / 2b / 3c ; 2.11.2.3 1a / 2b / 3c  
- SOC: 2.11.2 A / A / B ; 2.11.2.1 1a / 1a / 2b ; 2.11.2.2 1a / 1a / 2b ; 2.11.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the **audience**, an **approved channel**, and a **handling marking**, and apply a **handling caveat**.
2. Tailor the same **A12** product for a technical audience and for leadership, and reject the wrong channel.

**Mapped Proficiency Items:**
- K: 2.11.2 – Disseminating intelligence to the correct audiences
- T: 2.11.2.1 – Select audience and method and apply correct handling markings
- T: 2.11.2.2 – Tailor products to different audiences (technical, leadership, etc.)
- T: 2.11.2.3 – Disseminate intelligence products through approved channels

---

## 1. Key Concepts

CTI analysts **send the finished product** to the people who can use it, on a path the shop already approved, with a label that says who else may see it. A judged answer that only lives in a private chat is not disseminated. Leadership that never sees the one-liner cannot act. That is the job in this lesson: name the audience, the approved channel, and the handling marking — then send that version.

**2.11.1** wrote the product. **2.1.6** is how you change content, format, and detail for a named reader. You do not change the judgment. This lesson is the **send**. SOC report routing is **1.5.3**. Local customer lists are **2.12.3**. The TLP labels and channels in this lesson are **classroom stand-ins** — not live org policy.

| Idea | What it is |
|------|------------|
| **Audience** | Who owns the next decision. **IR / SOC** (technical) vs **leadership** (awareness) |
| **Channel** | How it travels. **Ticket** or **approved intel channel**. Reject personal SMS, private chat, and public post |
| **Handling marking** | A label that says who may see this product |
| **Handling caveat** | An extra instruction the label does not say (for example, no hash on the leadership send) |

**Classroom card (this lesson only — not live org policy):**

| Label | Meaning in this lesson |
|-------|------------------------|
| **TLP:AMBER** | Need-to-know inside the organization. Not a public post |
| **TLP:CLEAR** | No restriction. Do not use this on a product that names a live host |

**TLP** here means Traffic Light Protocol used as a practice label. If your shop has a real marking card, use that card. Do not invent a DYA color such as `TLP-RED-DYA`.

A one-liner is still marked. Right people on the wrong path still fails.

**What good looks like:**

**Given:** the finished **A12** product from **2.11.1**. IR has **WS-JLEE** / `jlee`. The update domain is **likely** the payload host. Temp `invoice.vbs` is on the host. Same facts. Two sends.

- **Technical (IR / SOC):** audience IR + SOC. Channel: ticket. Marking: **TLP:AMBER** (classroom). Caveat: need-to-know inside the shop. Detail: host, `invoice.vbs`, update domain.
- **Leadership:** audience duty lead (awareness). Channel: approved channel. Marking: still **TLP:AMBER** (classroom). Caveat: **no hash**, no file path. One line: IR has the host; treat the update domain as the payload host.
- **Reject:** personal SMS or private chat “so leadership sees it faster.”

Do not rewrite the judgment so leadership likes it (**2.1.6**). Do not invent a customer list (**2.12.3**).

---

## 2. Knowledge Check

1. Personal SMS is fine if leadership needs it fast. True or false?
2. What three things do you name to route a product?
3. **A12** to IR vs leadership — one difference in detail, and one rejected channel.

---

## 3. Summary

Audience, approved channel, and handling marking. Same facts, different detail. A caveat can still restrict the send. No SMS. Classroom TLP is not live org policy.

**Next:** **2.11.3** Handling RFIs.

---

## 4. Related modules

- 2.11.1 – Creating finished intelligence products (previous)
- 2.11.3 – Handling RFIs
- 2.1.6 – Tailoring output to the audience
- 1.5.3 – Notification and distribution
- 2.12.3 – Local dissemination channels and customers
