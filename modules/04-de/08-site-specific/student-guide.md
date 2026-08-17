# Module 4.8 – Site-specific DE knowledge

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.8.1 B / C / C ; 4.8.1.1 3c / 4c / 4c ; 4.8.2 B / C / C ; 4.8.2.1 3c / 4c / 4c ; 4.8.2.2 3c / 4c / 4c  
- SOC: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1 1a / 1a / 1a ; 4.8.2.2 1a / 1a / 1a  
- Hunter: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1 1a / 1a / 1a ; 4.8.2.2 1a / 1a / 1a  
- CTI: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1 1a / 1a / 1a ; 4.8.2.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that **local policy** exists — a requirements list, and a review / deploy / retire path — and that it **varies by shop**.
2. **Obtain** that policy, **follow** only what you were shown, and **reject** inventing a list, change board, or ticket name.

**Mapped Proficiency Items:**
- K: 4.8.1 – Local detection requirements
- T: 4.8.1.1 – Identify whether you have the local list and align only to a list you were shown
- K: 4.8.2 – Local review, deploy, and retire paths
- T: 4.8.2.1 – Follow the local path you were shown (or record that you do not have it yet)
- T: 4.8.2.2 – Reject inventing a change board or ticket name as policy

---

## 1. Key Concepts

Every shop has its own DE **policy**. This course does **not** publish DYA’s. This hour is **obtain-and-follow**. You do not invent policy.

**4.2** said shop requirements (meta fields, naming, IDs, tags, logging) are a *list*. **4.6** said you retire and deploy. This hour is *this shop’s* list and *this shop’s* path.

**Local detection requirements.** Required meta fields, naming, and other deploy checks. They **vary by shop**. Obtain the current list. Do **not** invent one.

**Local review, deploy, and retire paths.** How a change is reviewed and deployed. How a retire is recorded. Obtain the path. Do **not** invent a change board or a ticket name.

**What good looks like:**

- Given: someone showed you the list. Align the nomination or change **only** to that list. Mark met vs missing.
- Given: no one has shown you the list or the path. Record that you **do not have it yet**. Do not fill the gap with made-up fields or a made-up ticket.
- Given: you invent “change board X” or a ticket name and treat it as policy. **Reject.**

Do not write the rule (**1.3**). Do not invent DYA policy.

---

## 2. Knowledge Check

1. This course publishes the DYA field list and deploy path. True or false?
2. You do not have the local requirements list. Do you invent the fields?
3. You invent a change board or ticket name and treat it as policy. Follow it, or reject?

---

## 3. Summary

Local policy exists. It varies by shop. Obtain the list and the path. Follow only what you were shown. Do not invent policy.

**Next:** Section 4 is complete.

---

## 4. Related modules

- 4.2 – Making a detection sound and meeting shop requirements
- 4.6 – Detection lifecycle
- 4.7 – Sensor availability and performance
