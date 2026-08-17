# Module 3.5.1 – Using MITRE ATT&CK for Hunt Planning

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 3c / 4c / 4d  
- SOC: 3.5.1 A / B / B ; 3.5.1.1–3.5.1.2 1a / 2b / 3c ; 3.5.1.3 1a / 1a / 2b  
- CTI: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Map **this hunt** (plan or findings) to ATT&CK tactics and techniques.
2. Use that map to name a **detection** or **visibility** gap and to **support** priority.

**Mapped Proficiency Items:**
- K: 3.5.1 – Using MITRE ATT&CK for hunt planning and coverage analysis
- T: 3.5.1.1 – Map a hunt plan or hunt findings to MITRE ATT&CK
- T: 3.5.1.2 – Use ATT&CK to identify detection or visibility gaps
- T: 3.5.1.3 – Use ATT&CK to support hunt prioritization

---

## 1. Key Concepts

**3.4.2** taught you to *copy* an ATT&CK ID when a report already printed it. Shared-floor ATT&CK is **0.6.1**. CTI mapping is **2.7.1**. This hour is **map this hunt**, then name gaps and rank work.

You map **this hunt**, not the whole enterprise.

| You write | You do not |
|-----------|------------|
| Method you will search → tactic + technique | Color every Navigator cell because a group was named |
| What you observed → the technique that describes *that* method | Invent an ID so the card looks complete |

| Gap | Meaning |
|-----|---------|
| **Detection gap** | Telemetry exists; no analytic covers that technique in this scope |
| **Visibility gap** | You cannot see the technique here — name it, do not hunt it as written |

ATT&CK **supports** priority. It does not replace scope, blast radius, or freshness. “The tactic is red” is not a reason.

**What good looks like:**

- **Map:** A12 hunt for HKCU Run **`Updater`** → **TA0003** Persistence / **T1547.001** Run keys.
- **Detection gap:** registry telemetry exists; no analytic on value name `Updater`.
- **Visibility gap:** no registry logging on that class — not a hunt.
- **Priority:** open incident + FN download + mapped technique you can see. Not “Persistence is always first.”

How the Run key *works* on disk is **3.6.1**. Full card format is **3.2.2**.

---

## 2. Knowledge Check

1. Copying T1547.001 off a report is a coverage analysis. True or false?
2. What is the difference between a detection gap and a visibility gap?
3. Map the A12 Run-**`Updater`** hunt to one tactic and one technique, and say whether that is a detection gap or a visibility gap if registry logs exist and no analytic fires.

---

## 3. Summary

Map this hunt. Name the gap. ATT&CK supports priority; it does not replace it.

**Next:** **3.6.1** Persistence techniques.

---

## 4. Related modules

- 3.4.3 – STIX input (previous)
- 3.6.1 – Persistence recognition
- 0.6.1 – Shared ATT&CK
- 2.7.1 – CTI ATT&CK
- 3.2.2 – Hunt card
