# Module 4.5 – Hunt and intel packages

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.5 B / C / C ; 4.5.1 3c / 4c / 4d ; 4.5.2 3c / 4c / 4c  
- SOC: 4.5 A / A / B ; 4.5.1 1a / 1a / 2b ; 4.5.2 1a / 1a / 2b  
- Hunter: 4.5 A / B / B ; 4.5.1 1a / 2b / 3c ; 4.5.2 1a / 2b / 2b  
- CTI: 4.5 A / B / B ; 4.5.1 1a / 2b / 3c ; 4.5.2 1a / 2b / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Treat a hunt or intel **package** like a **nomination** — not a finished detection.
2. Name one **add**, one **change**, or **no new rule**, and reject turning the package into a **block** list.

**Mapped Proficiency Items:**
- K: 4.5 – Hunt and intel packages
- T: 4.5.1 – Review a package: one add, one change, or no new rule
- T: 4.5.2 – Reject turning the package into a block list

---

## 1. Key Concepts

**4.4** was a tune on a *live* rule. This hour is a **package** from **CTI** or from **hunters**. Both are inputs.

A package is **not** a finished detection. Treat it like a **nomination** (**4.3**): it must be clear enough to review — the **need**, and a **pointer**. The package itself is often the pointer (the hunt package, or the intel **report** title and URL). A drafted rule if they have one — not required. If the need or pointer is missing, **send it back**.

Then review for a chance to add or change a detection. **“No new rule”** is a valid product.

| Product | What it means |
|---------|----------------|
| One **add** | A new detection this package supports. |
| One **change** | A live rule should change because of this package. |
| **No new rule** | Nothing to add or change. That is still a finished review. |

**Reject** turning the package into a **block** list. Extra infrastructure goes to whoever **blocks** (firewall / IA). That is not a DE deploy.

**What good looks like:**

- Given: a hunt package with the need and the package as the pointer; activity we do not detect. **Add.**
- Given: an intel report we already cover; no gap. **No new rule.**
- Given: a list of IPs to put on the firewall. **Reject.** That is a block list.

Do not write the rule (**1.3**). Do not invent a ticket. Tunes are **4.4**. When to retire in general is **4.6**.

---

## 2. Knowledge Check

1. A package is a finished detection. True or false?
2. Name the three valid review products for a package.
3. A package is a list of IPs to put on the firewall. Add a rule, or reject?

---

## 3. Summary

Packages come from CTI and from hunters. Treat them like a nomination. Add, change, or no new rule. A block list is not DE.

**Next:** **4.6** Detection lifecycle.

---

## 4. Related modules

- 4.3 – Nominations from SOC, hunt, and CTI
- 4.4 – Tune requests from SOC
- 4.6 – Detection lifecycle
- 0.3 – How work can move
