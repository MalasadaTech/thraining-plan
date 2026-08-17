# Module 2.12.3 – Local Dissemination Channels and Customers

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.12.3 B / C / C ; 2.12.3.1 3c / 4c / 4c  
- Hunter: 2.12.3 A / A / B ; 2.12.3.1 1a / 1a / 2b  
- SOC: 2.12.3 A / A / A ; 2.12.3.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that **local customers and channels** exist at the shop, and how you **obtain** that chart.
2. Route a product using **that** chart — or record that you **do not have it yet**. Do not invent a customer list.

**Mapped Proficiency Items:**
- K: 2.12.3 – Local dissemination channels and customers
- T: 2.12.3.1 – Disseminate a product using the correct local channels and customers

---

## 1. Key Concepts

CTI analysts send the finished product to **this shop’s** customers on **this shop’s** channels. Classroom routing is **2.11.2**. This hour is the **local chart**. Environment / sensors are **0.8**. Do not invent a DYA distro.

| You do | You do not |
|--------|------------|
| Obtain the customer / channel chart | Invent `soc-aware@dya` as policy |
| Use the names **on that chart** | Use SMS because it is faster (**2.11.2**) |
| Write **do not have the chart yet** | Fill a Harbor/DYA recipient list |

**What good looks like:** “I obtain the local customer/channel chart. If it names IR + an intel ticket path, I use those names for the **A12** product. If there is no chart: **I do not have the chart yet.**”

This closes **2.x** CTI. Hunt is **3.x**.

---

## 2. Knowledge Check

1. You should invent a DYA distro so the class has recipients. True or false?
2. How does this hour differ from **2.11.2**?
3. You have not been shown a chart. What do you write, and what channel do you still **reject**?

---

## 3. Summary

Obtain the local chart. Use those names. Or write not yet. Do not invent recipients. CTI `2.x` ends. Hunt is `3.x`.

**Next:** **3.1.1** Purpose of threat hunting.

---

## 4. Related modules

- 2.12.2 – Local produce/approve (previous)
- 2.11.2 – Classroom dissemination
- 0.8 – Environment / sensors
- 3.1.1 – Purpose of threat hunting
