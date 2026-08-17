# Module 3.7.3 – Hunt Outputs and Hand-off

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.3 B / C / C ; 3.7.3.1 3c / 4c / 4c  
- SOC: 3.7.3 A / A / B ; 3.7.3.1 1a / 1a / 2b  
- CTI: 3.7.3 A / A / B ; 3.7.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that **what a finished hunt must produce** and **who it is handed to** (SOC, IR, or CTI) **varies by site**.
2. **Hand off** only on the path you were shown — or record that you **do not have the chart yet**. Do not invent a recipient.

**Mapped Proficiency Items:**
- K: 3.7.3 – Hunt outputs and hand-off
- T: 3.7.3.1 – Produce required hunt outputs and perform proper hand-off

---

## 1. Key Concepts

**3.7.2** was where the hunt is *written down*. This hour is what **leaves** the hunt: the required output and the **hand-off**.

This course **does not** publish a DYA output list or recipient chart. You still know *that* hunts often go to SOC, IR, CTI, or DE (**4.x**). You do **not** know *this site’s* names, queues, or “always IR if A12.”

| Path | You will be shown (locally) | You do **not** do this hour |
|------|-----------------------------|-----------------------------|
| **Outputs** | What “done” always includes here | Invent “always file an incident report” |
| **Hand-off** | Which team and which local channel | Invent `soc@` as policy |

**What good looks like:** “I obtain the output list and the hand-off chart from [role the instructor names, or my lead]. The A12 package (more hosts, the gap) goes **where that chart says**. If none was shown: **I do not have the local chart yet.** I do **not** email a made-up queue.”

The hunt product is still a **package**, not a rewrite of the SOC ticket (**3.1**). Who receives the package is a **site** fact.

---

## 2. Knowledge Check

1. You should email a made-up SOC queue so the hunt is “handed off.” True or false?
2. What two things does this hour obtain?
3. If no chart was shown, what do you write — and what do you **not** send?

---

## 3. Summary

Obtain outputs and the hand-off chart. Follow it. Or write “not yet” and do not send.

Hunt 3.x ends here. **Next track:** **4.x** Detection Engineer.

---

## 4. Related modules

- 3.7.2 – Documentation (previous)
- 3.1 – Hunt product is a package
- 1.5 – SOC reporting
- 4.x – DE takes a nominated gap
