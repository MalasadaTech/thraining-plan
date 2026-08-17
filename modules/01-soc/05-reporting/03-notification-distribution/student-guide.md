# Module 1.5.3 – Notification and Distribution

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C ; 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 A / B / B ; 1.5.3.2 2b / 3c / 4c  
- CTI: 1.5.3.1 B / C / C ; 1.5.3.2 3c / 4c / 4c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a notification chart: **who**, **leadership awareness**, **approved channel**.
2. Route a report: name recipients, whether leadership gets awareness, the approved channel, and **reject the wrong channel**.

**Mapped Proficiency Items:**
- K: 1.5.3.1 – Notification and distribution
- T: 1.5.3.2 – Route a report: name recipients, leadership awareness, and the approved channel

---

## 1. Key Concepts

SOC analysts put the record on an **approved path** so IR and leadership actually see the case, and so the CTI question lands as an RFI, not a text. You already know the **type** (**1.5.1**) and the **clock** (**1.5.2**). This hour is **who** and **how**. You do **not** pick the type again. You do **not** score the 30 / 60. You do **not** write the body. **1.7** is retired — not a 1.5 channel.

**Classroom chart (this lesson only — not a live shop matrix):**

| Type | Recipients | Leadership awareness | Approved channel |
|------|------------|----------------------|------------------|
| **Incident** | SOC queue + **IR** | **Yes** — duty SOC lead | **Ticket** (the case system) |
| **RFI** | The **named team** (CTI, hunt, or IT) | **No**, unless they asked or the chart says so | **Ticket** or **approved RFI form** |

If your shop has a real chart, use it. The obligation is **who + leadership yes/no + approved channel**, not these names. If your shop has an **other** type, it has its own row — do not invent one here.

**Leadership awareness** is a yes/no on the chart. It is not “email the CEO.” Duty SOC lead counts. The leadership product is a short awareness flag, not the file hash.

**Approved** (classroom): ticket, approved RFI form.  
**Not approved** (classroom): personal SMS, private chat, personal mail off-domain.

Right people on the **wrong path** still fails.

The route is four facts: **recipients**, **leadership yes/no**, **channel**, **rejected channel**.

**What good looks like:**

- **Incident, ticket:** First IR handoff for **A12** (`WS-JLEE` / `jlee`, `wscript` → `-enc`, Temp `invoice.vbs`). Recipients **SOC + IR**. Leadership **yes**. Channel **ticket**. Reject: personal email or chat to the IR analyst only.
- **RFI, not SMS:** **A12** exists. Ask CTI to work the update domain. Recipients **CTI**. Leadership **no**. Channel **ticket or RFI form**. Reject: texting a CTI friend. Right team, wrong path.

---

## 2. Knowledge Check

1. This hour is when the report is due. True or false?
2. What three things does the notification chart tell you?
3. First IR handoff for **A12**. Recipients, leadership yes/no, channel, and one rejected channel?

---

## 3. Summary

Chart: who, leadership, channel. Reject the unofficial path. This closes **1.5**. SOC ends.

**Next:** **3.1.1** Data, information, and intelligence. The RFI is the door into CTI.

---

## 4. Related modules

- 1.5.2 – Reporting timeline requirements (previous)
- 1.5.1 – Report types
- 3.1.1 – Data, information, and intelligence
- 3.11 – Intelligence production (not a 1.5 route)
