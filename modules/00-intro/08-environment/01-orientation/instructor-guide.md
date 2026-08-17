# Instructor Guide – Module 1.8.1 – Environment Orientation

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.8.1.1 A / B / C · 1.8.1.2 2b / 3c / 4c  
- Hunter: 1.8.1.1 B / C / C · 1.8.1.2 2b / 3c / 4c  
- CTI: 1.8.1.1 A / B / B · 1.8.1.2 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the seven orientation facts. Force **fact + rejected neighbor**. Do not teach PCAP export or IR.

**Key Teaching Points:**
- Harbor is a stand-in. Overlay the site card if you have one.
- Two facts can be true; the task is the one the *question* asks.
- No sensor on OT is a **g** answer, not a promise of 1.8.2.
- CTI 3-level task is **1a**. Do not collapse to SOC 2b.

**Common Student Challenges:**
- “Everything is egress.”
- Treating email as raw NAT.
- Assuming span-2 sees OT.
- Calling `10.10.8.90` the vendor VPN because “scanner.”
- Opening 1.8.2 / 1.8.5.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site architecture card
- Answer key (this guide)

---

## Learning Objectives

1. Seven facts on the card.
2. Which fact + reject neighbor.

**Mapped Items:** K 1.8.1.1 · T 1.8.1.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 1.8.2 / 1.2 / 1.8.5 |
| Seven facts                    | 16 min   | a–g |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~64 min** | Stretch Ex 2 if they say “internet” |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: A / 2b — copy the row and name the neighbor.
- Overlay real names (`CIRT span`, `PCI VLAN`) if you can.

**Question:**  
“If span-2 is down (1.7.2 Zeek drop), which *orientation* fact changed — and which download path is now 1.8.2’s problem?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail “it’s the network” with no letter. Fail OT PCAP from span-2.

**Summaries:**
- Ex 1: egress + span-1; not OT; not email.
- Ex 2: email path; not raw egress.
- Ex 3: sensor gap on fw-ot; not span-2.

**Cases:**

| Item | Fact | Reject | Why |
|------|------|--------|-----|
| A | **Crown jewel (f)** `pay-db-01` | Ordinary server segment only | Card names it a jewel. Segment (b) is also true; the *question* is criticality. |
| B | **Egress (a)** via **`fw-guest`** | fw-edge user NAT | Guest is a different door. |
| C | **User segment (b)** `10.10.8.0/24` | Third-party `10.10.90.0/24` | `.8.90` is on the user VLAN, not `vpn-vendor`. |
| D | **Sensor (g)** **`span-2`** | span-1 (internet only) | Host ↔ DC is east-west on core. |

---

## Knowledge Check – Answer Key

1. **Seven facts?**  
   **Answer:** Egress, segments/data flow, email, choke points, third-party, crown jewels, PCAP sensors.  
   **Explanation:** Outline a–g.

2. **Guest vs user egress?**  
   **Answer:** Guest → `fw-guest`. User/server → `fw-edge-01`.  
   **Explanation:** Outline a.

3. **Email ≠ egress?**  
   **Answer:** Mail takes `mail-edge` → filter → `mail-int`. Raw NAT is a different fact.  
   **Explanation:** Outline c vs a; Example 2.

4. **OT sensor?**  
   **Answer:** Harbor: **none** on `fw-ot`. Say the gap. Do not invent span-2 coverage.  
   **Explanation:** Outline g; Example 3.

5. **Why not “describe the network”?**  
   **Answer:** That restates the K. Sign-off is pick the fact and reject the neighbor.  
   **Explanation:** Task.

---

## Additional Instructor Resources

- Site architecture card
- Next recommended module: 1.8.3 Tool access (shared floor). Why you pull PCAP is 1.2.1.
