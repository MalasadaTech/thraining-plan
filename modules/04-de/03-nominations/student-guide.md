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

1. Say who can **nominate**, and what the nomination must contain (the **need** and a **pointer**; a drafted rule only if they have one).
2. Review a nomination: **accept** for work, **send back**, or **reject** — and say who still owes what.

**Mapped Proficiency Items:**
- K: 4.3 – Nominations from SOC, hunt, and CTI
- T: 4.3.1 – Review a nomination: accept, send back, or reject, and say who finishes what

---

## 1. Key Concepts

**4.2** was sound, the shop list, and closing the loop. This hour is the **nomination** itself.

**Who can nominate:** a **SOC analyst**, a **hunter**, or a **CTI analyst**.

A nomination can be a draft, a sketch, or “we need something on this.” It does **not** have to be production-ready.

**Clear enough to review** means two things are present:

- The **need** — what activity, where it showed up.
- **Context or a reference** — this came from an investigation or an intel **report**. The pointer is an investigation number, or the report title and URL.

A **drafted rule** goes with it **if the nominator has one**. It is **not** required. DE can finish the rule.

Do not invent a ticket name or a DYA form. The *kinds* of pointer are enough. The local form is **4.8**.

**DE review** is one of three:

| Review | What it means |
|--------|----------------|
| **Accept** for work | Need + pointer. DE will finish (including the rule if they did not send one). |
| **Send back** | Say what is missing (need, pointer, or both). The nominator still owes that. |
| **Reject** | Say why. Not DE work (a block, an investigation, or “write me SIGMA” as **1.3**). |

The bar is **“clear enough to review,”** not “ready to deploy.”

**What good looks like (4.3.1):** pick accept / send back / reject, say why, and name what the **nominator** still owes vs what **DE** will finish.

- Given: encoded PowerShell on workstations, plus the intel report title and URL. No drafted rule. **Accept.** DE finishes the rule.
- Given: the need, no pointer. **Send back.** Nominator owes the investigation number, or the report title and URL.
- Given: “Block this IP at the firewall.” **Reject.** That is a **block**, not a nomination.

Hunt and intel **packages** are **4.5**. Tunes on a *live* rule are **4.4**.

---

## 2. Knowledge Check

1. Who can nominate?
2. A nomination names the need and points at a report, but has no drafted rule. Accept or send back?
3. A nomination names the activity but has no investigation or report pointer. Accept, send back, or reject? Who still owes what?

---

## 3. Summary

SOC, hunt, and CTI nominate. Clear enough = the need plus a pointer. A drafted rule is extra if they have one. Accept, send back, or reject — and say who finishes what.

**Next:** **4.4** Tune requests from SOC.

---

## 4. Related modules

- 4.1 – What DE owns
- 4.2 – Making a detection sound and meeting shop requirements
- 4.4 – Tune requests from SOC
- 4.5 – Hunt and intel packages
- 4.8 – Site-specific DE knowledge (the local form)
