# Module 4.3 – Nominations from SOC, hunt, and CTI

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.3 B / C / C ; 4.3.1 3c / 4c / 4d  
- SOC: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
- Hunter: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
- CTI: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say who can **nominate**, and that the draft need not be production-ready.
2. Review a nomination: **accept** for work, **send back**, or **reject** — and say who still owes what.

**Mapped Proficiency Items:**
- K: 4.3 – Nominations from SOC, hunt, and CTI
- T: 4.3.1 – Review a nomination: accept, send back, or reject, and say who finishes what

---

## 1. Key Concepts

**4.2** was sound, the shop list, and closing the loop. This hour is the **nomination** itself.

**Who can nominate:** a **SOC analyst**, a **hunter**, or a **CTI analyst**.

A nomination can be a draft, a sketch, or “we need something on this.” It does **not** have to be production-ready.

**DE review** is one of three:

| Review | What it means |
|--------|----------------|
| **Accept** for work | Clear enough to review. DE will finish. |
| **Send back** | Say what is missing. The nominator still owes that. |
| **Reject** | Say why. Not DE work (a block, an investigation, or “write me SIGMA” as **1.3**). |

The bar for the nominator is **“clear enough to review,”** not “ready to deploy.”

**What good looks like (4.3.1):** pick accept / send back / reject, say why, and name what the **nominator** still owes vs what **DE** will finish.

- Given: “We keep missing encoded PowerShell on workstations.” **Accept.** Nominator owes nothing required. DE finishes.
- Given: “Make a rule.” **Send back.** Nominator owes the activity (what, where).
- Given: “Block this IP at the firewall.” **Reject.** That is a **block**, not a nomination.

Do not invent a ticket name. Hunt and intel **packages** are **4.5**. Tunes on a *live* rule are **4.4**.

---

## 2. Knowledge Check

1. Who can nominate?
2. The nominator bar is “ready to deploy.” True or false?
3. Someone says “Make a rule” and names no activity. Accept, send back, or reject? Who still owes what?

---

## 3. Summary

SOC, hunt, and CTI nominate. A sketch is enough if it is clear enough to review. Accept, send back, or reject — and say who finishes what.

**Next:** **4.4** Tune requests from SOC.

---

## 4. Related modules

- 4.1 – What DE owns
- 4.2 – Making a detection sound and meeting shop requirements
- 4.4 – Tune requests from SOC
- 4.5 – Hunt and intel packages
