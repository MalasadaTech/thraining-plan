# Module 2.2.3 – Admiralty Code

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.3 B / C / C ; 2.2.3.1 3c / 4c / 4d  
- Hunter: 2.2.3 A / B / B ; 2.2.3.1 1a / 2b / 3c  
- SOC: 2.2.3 A / A / B ; 2.2.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Rate **source reliability** (A–F) and **information credibility** (1–6).
2. Combine them into one Admiralty rating and say what it means.

**Mapped Proficiency Items:**
- K: 2.2.3 – Admiralty Code / source reliability and information credibility
- T: 2.2.3.1 – Assign Admiralty Code ratings and evaluate source reliability and credibility

---

## 1. Key Concepts

CTI analysts split **who said it** from **how well this piece checks out**. Estimative *likelihood* is **2.2.1**. Attribution *confidence* is **2.1.7**. This hour is the **Admiralty pair**. You do **not** invent a shop scale. You do **not** rate a nation-state.

**Classroom scales (standard Admiralty — this lesson only if your shop uses different letters):**

| Source reliability (letter) | Information credibility (number) |
|-----------------------------|----------------------------------|
| **A** completely reliable | **1** confirmed |
| **B** usually reliable | **2** probably true |
| **C** fairly reliable | **3** possibly true |
| **D** not usually reliable | **4** doubtful |
| **E** unreliable | **5** improbable |
| **F** cannot be judged | **6** cannot be judged |

A rating is **letter + number** (example **B2**). A is not “true.” 1 is not “trusted source.” They are two axes.

**What good looks like:**

- **Internal Zeek A record you pulled for A12:** source **B** (your sensor, usually reliable) · information **1** or **2** if it matches the host story. Not **A1** just because it is yours.
- **Anonymous public blog, one claim, no internals:** source **F** or **E** · information **5** or **6**. Do not promote it to **B2** because the title said INTEL.

---

## 2. Knowledge Check

1. A reliable source means the information is confirmed. True or false?
2. What are the two Admiralty axes?
3. Anonymous blog, no internals, “block these now.” Letter + number, and why.

---

## 3. Summary

Letter = source. Number = this piece. Combine them. Do not mix them with “likely.”

**Next:** **2.2.4** Cognitive biases and mitigation.

---

## 4. Related modules

- 2.2.2 – Structured analytic techniques (previous)
- 2.2.4 – Cognitive biases
- 2.2.1 – Estimative language
- 2.1.7 – Attribution confidence
