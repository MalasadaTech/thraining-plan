# Module 4.6 – Detection lifecycle

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.6 B / C / C ; 4.6.1 3c / 4c / 4d ; 4.6.2 3c / 4c / 4d  
- SOC: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
- Hunter: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
- CTI: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Given a live rule and a reason, call **modify**, **retire**, or **leave**.
2. Given “we **blocked** this infrastructure,” decide whether the matching rule still earns its keep.

**Mapped Proficiency Items:**
- K: 4.6 – Detection lifecycle
- T: 4.6.1 – Call modify / retire / leave and cite the reason
- T: 4.6.2 – Given a block, decide whether the matching rule still earns its keep

---

## 1. Key Concepts

**4.5** was a package (add, change, or no new rule).

DE’s normal work includes **managing** the detections you already own. You regularly review whether they still earn their keep, need an update, or should come out. This hour is that review: **modify**, **retire**, or **leave**. Cite the reason. This is not the tune *inbox* (**4.4**).

| Call | When |
|------|------|
| **Modify** | The rule should stay, but not as it is (too noisy, or a nomination replaced part of it). |
| **Retire** | The rule should come out (threat gone, sensor gone, a nomination replaced it, or it no longer earns its keep). |
| **Leave** | Still useful. Do not change it because someone is tired of it. |

**Reasons** you cite:

- still useful
- too noisy
- threat gone
- sensor gone
- a nomination replaced it
- already **blocked**, so the rule *may* not be needed

“Sensor gone” is a reason here. How to check a dead sensor is **4.7**.

**A block is not automatic retire.** Firewall / IA blocked the infrastructure. Ask: does this rule still earn its keep? Keep it if it still watches something else (other hosts, other paths). Retire it if it only existed for what is now blocked.

**What good looks like:**

- Given: live rule, still the right activity, too noisy. **Modify.** Reason: too noisy.
- Given: live rule, still catching the intended activity; SOC is tired of it. **Leave.** Reason: still useful.
- Given: “We blocked this IP.” **Not automatic retire.** Decide if the matching rule still earns its keep.

Do not write the rule (**1.3**). Do not invent a ticket.

---

## 2. Knowledge Check

1. Name the three lifecycle calls.
2. “We blocked this infrastructure” means you must retire the matching rule. True or false?
3. A live rule still catches the intended activity. SOC wants it gone because it is busy. Modify, retire, or leave?

---

## 3. Summary

Managing live detections is regular DE work. Modify, retire, or leave — and cite the reason. A block is not automatic retire. Ask whether the rule still earns its keep.

**Next:** **4.7** Sensor availability and performance.

---

## 4. Related modules

- 4.4 – Tune requests from SOC
- 4.5 – Hunt and intel packages
- 4.7 – Sensor availability and performance
- 4.1 – What DE owns
