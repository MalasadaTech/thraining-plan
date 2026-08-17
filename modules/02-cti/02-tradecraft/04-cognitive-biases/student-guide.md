# Module 2.2.4 – Cognitive Biases and Mitigation

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.4 B / C / C ; 2.2.4.1 3c / 4c / 4d  
- Hunter: 2.2.4 A / B / B ; 2.2.4.1 1a / 2b / 3c  
- SOC: 2.2.4 A / A / A ; 2.2.4.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name common biases that warp a product, and what they do to it.
2. Spot a bias in a judgment and name a **mitigation** you already have (**2.2.2**).

**Mapped Proficiency Items:**
- K: 2.2.4 – Cognitive biases and mitigation
- T: 2.2.4.1 – Identify cognitive bias in a judgment and apply a mitigation technique

---

## 1. Key Concepts

CTI analysts name the **bias** so they can apply a method, not a pep talk. Techniques are **2.2.2**. This hour is the **distortion**. You do **not** invent a new SAT. You do **not** diagnose the author.

| Bias | What it looks like | What it does to the product |
|------|--------------------|-----------------------------|
| **Confirmation** | You keep the evidence that fits the first story | Alternatives never get a fair look |
| **Anchoring** | The first vendor name or first number sticks | Later internals cannot move the call |
| **Availability** | The last incident you saw becomes this one | **A12** gets treated as “the last campaign” with no link |

**Mitigation** is a method you already have: **Key Assumptions Check** or **ACH** (**2.2.2**). “Be more objective” is not a mitigation.

**What good looks like:**

- **Spot:** “Vendor PDF says PRD APT, so high nation-state.” **Anchoring** (and confirmation). First label stuck.
- **Mitigate:** Key Assumptions Check — “vendor name = who they are.” That assumption breaks. You do not need a new technique.

---

## 2. Knowledge Check

1. “Be more objective” is a mitigation technique. True or false?
2. Name two biases from this hour.
3. “Vendor PDF says PRD APT, so high nation-state.” Bias, and one mitigation.

---

## 3. Summary

Name the bias. Apply a method you already have. Do not pep-talk it away.

**Next:** **2.3.1** Internal threat intelligence platform.

---

## 4. Related modules

- 2.2.3 – Admiralty Code (previous)
- 2.2.2 – Structured analytic techniques (the mitigations)
- 2.3.1 – Internal TIP
- 2.1.7 – Attribution
