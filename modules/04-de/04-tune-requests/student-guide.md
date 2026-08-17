# Module 4.4 – Tune requests from SOC

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.4 B / C / C ; 4.4.1 3c / 4c / 4d ; 4.4.2 3c / 4c / 4c  
- SOC: 4.4 A / B / B ; 4.4.1 1a / 2b / 3c ; 4.4.2 1a / 2b / 2b  
- Hunter: 4.4 A / A / B ; 4.4.1 1a / 1a / 2b ; 4.4.2 1a / 1a / 2b  
- CTI: 4.4 A / A / B ; 4.4.1 1a / 1a / 2b ; 4.4.2 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that a **tune request** is about a *live* rule, on a **different inbox**, and that it must name **which rule** and a **pointer**.
2. Pick **tune**, **exception**, **replace**, **leave**, or **retire**, and reject a request that is really an investigation, a **block**, or IR containment.

**Mapped Proficiency Items:**
- K: 4.4 – Tune requests from SOC
- T: 4.4.1 – Pick tune / exception / replace / leave / retire and cite why
- T: 4.4.2 – Reject a request that is investigation, a block, or IR containment

---

## 1. Key Concepts

After rules are **live**, SOC will ask DE to change them. That ask is a **tune request**, not a new nomination. This hour is that inbox.

**4.3** was a **nomination** (something new). A tune is about a rule that is already live — noisy, brittle, or missing context.

“Missing context” here means the **rule** fires without enough of the picture. It is not the pointer below.

Same desk as nominations. **Different inbox.** Do not treat a tune as a new nomination.

**Clear enough to review** means two things are present:

- **Which live rule.**
- **Context or a reference** — this came from an investigation or an intel **report**. The pointer is an investigation number, or the report title and URL.

Do not invent a ticket name or a DYA form. The *kinds* of pointer are enough. The local form is **4.8**. If the pointer is missing, **send it back**. You cannot cite why without it.

**Possible answers** (only after it is clear enough):

| Answer | What it means |
|--------|----------------|
| **Tune** the logic | Change the rule so it still catches the intended activity and fires less on the rest. |
| Add an **exception** | Leave the rule; carve out what must not fire. |
| **Replace** the rule | This live rule is the wrong shape. A different rule should take its place. |
| **Leave** it | The rule is doing its job. Do not change it because someone is tired of the alert. |
| **Retire** it | This live rule should come out. When to retire in general is **4.6**. |

**Reject** a request that is really:

- an **investigation** (“go look at the host”)
- a **block** (“stop this IP at the firewall”)
- **IR containment** (“take the host off the network”)

**What good looks like:**

- Given: the live rule fires on a nightly backup *and* on the intended encoded PowerShell, plus an investigation number. **Tune** or **exception**. Keep the intended fire.
- Given: which live rule, no pointer. **Send back.** SOC owes the investigation number, or the report title and URL.
- Given: “This rule is noisy — investigate the host” or “block that IP.” **Reject.** Not a tune.

Do not write the rule (**1.3**). Hunt and intel **packages** are **4.5**.

---

## 2. Knowledge Check

1. A tune request and a nomination are the same inbox. True or false?
2. A tune request names the live rule but has no investigation or report pointer. Pick a tune answer, or send it back?
3. SOC says a live rule is noisy and asks you to investigate the host. Tune or reject?

---

## 3. Summary

Tunes are about *live* rules. Same desk, different inbox. Clear enough = which rule plus a pointer. Then tune, exception, replace, leave, or retire — and reject investigation, block, or IR.

**Next:** **4.5** Hunt and intel packages.

---

## 4. Related modules

- 4.3 – Nominations from SOC, hunt, and CTI
- 4.5 – Hunt and intel packages
- 4.6 – Detection lifecycle
- 4.8 – Site-specific DE knowledge (the local form)
- 1.3 – Detection authoring (how a rule works)
