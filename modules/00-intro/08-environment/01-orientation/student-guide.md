# Module 0.8 – Environment / signal flow

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.8 A / B / C ; 0.8.1 2b / 3c / 4c  
- Hunter: 0.8 B / C / C ; 0.8.1 2b / 3c / 4c  
- CTI: 0.8 A / B / B ; 0.8.1 1a / 2b / 3c  
- DE: 0.8 A / B / B ; 0.8.1 2b / 3c / 4c  
**Estimated Time:** 20 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the seven kinds of environment facts every role must obtain from their shop.
2. Given a situation, say which kind applies and why it is not the adjacent kind.

**Mapped Proficiency Items:**
- K: 0.8 – Environment / signal flow  
  SOC A / B / C · Hunter B / C / C · CTI A / B / B · DE A / B / B
- T: 0.8.1 – Identify which kind of fact applies and why it is not the adjacent kind  
  SOC 2b / 3c / 4c · Hunter 2b / 3c / 4c · CTI 1a / 2b / 3c · DE 2b / 3c / 4c

---

## 1. Key Concepts

Every desk will look at the same host or log. You must know **where your site can see and where it cannot**. This course does not give you those answers. You get them from **your shop**. If you invent a network, a firewall name, or a sensor you were not shown, you are not doing this hour.

**Why this matters.** A SOC close, a hunt, an intel note, and a detection all depend on the same visibility. If you do not know the egress, the email path, or whether a sensor exists, you will treat a gap as “nothing happened.”

**Seven kinds of facts to obtain** (the answers live at your site, not here):

| Kind | The question you take to your shop |
|------|------------------------------------|
| **Egress** | How does traffic leave for the internet? |
| **Segments** | What are the main pieces, and how does data move between them? |
| **Email** | How does mail enter and leave? |
| **Choke points** | Where can the shop block or see at the edge? |
| **Third-party / federation** | Who else is trusted onto the network? |
| **Crown jewels** | Which assets must not be guessed? |
| **PCAP / sensors** | Where is there a sensor, and where is there not? |

| This lesson | Other |
|-------------|-------|
| Which *kind* of fact | Zeek field reading — **1.2** |
| Where a sensor sits | Host-observed network on the endpoint — **1.1.4** |
| Obtain the fact from your shop | Invented site card / classroom network — not this hour |

**What good looks like (0.8.1):** a user clicked a link and the host talked to the internet. The question “how did it leave?” is **egress**. It is not **email** unless you are asking how a message arrived. It is not **sensors** unless you are asking whether anything could have recorded that path. You do not name a firewall you were not shown.

---

## 2. Knowledge Check

1. Why must every role know where the site can see?
2. What is the difference between an egress question and an email question?
3. You need to know whether any sensor could have seen a host talk. Which kind of fact is that, and why is it not a Zeek-field question?

---

## 3. Summary

Seven kinds of questions. Obtain the answers from your shop. Name the kind that applies and reject the neighbor. Do not invent the network.

**Next:** **1.1.1** Endpoint activity (the map).

---

## 4. Related modules

- 0.7 – External tools (previous)
- 1.1.1 – Endpoint activity (next)
- 1.2 – Zeek (later)
- 1.1.4 – Host-observed network (later)
