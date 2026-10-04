# Module 3.1 – Purpose of Threat Hunting

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.1.1 B / C / C ; 3.1.1.1 3c / 4c / 4c ; 3.1.1.2 3c / 4c / 4d  
- SOC: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
- CTI: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain why threat hunting exists alongside alerting, incident response, CTI, and detection engineering.
2. Distinguish **uncovered activity**, a **detection gap**, a **visibility gap**, and a true **false negative**.

## Mapped Proficiency Items

- K: 3.1.1 – Purpose of Threat Hunting
- T: 3.1.1.1 – Explain the purpose of threat hunting in the context of the security program
- T: 3.1.1.2 – Identify examples of activity that existing controls might miss

## 1. Key Concepts

Threat hunting searches deliberately for suspicious or malicious activity that has **not already been adequately surfaced by existing controls**.

That makes hunting complementary to the SOC rather than a replacement for it. The SOC responds to alerts and cases that are already visible. A hunt asks a broader question:

> What relevant activity could exist in the environment even though no useful alert brought it to us?

A good hunt can produce several kinds of value:

- previously unknown affected hosts or accounts;
- evidence that an incident is broader than first understood;
- a reusable behavioral pattern;
- a **detection gap** for detection engineering;
- a **visibility gap** for telemetry owners;
- a new intelligence lead for CTI;
- evidence that the searched-for behavior was not found **within the tested scope and available visibility**.

### Four concepts that should stay separate

| Concept | Meaning |
|---|---|
| **Uncovered activity** | Relevant activity that was not already surfaced by an alert or case. |
| **Detection gap** | The needed telemetry exists, but current detections do not adequately cover the behavior. |
| **Visibility gap** | The telemetry needed to test the behavior is missing or insufficient. |
| **False negative** | A control that was expected to detect the activity failed to produce the expected detection. |

The distinction matters.

If HTTP telemetry shows `GET /update.exe` but the organization has **no detection designed to alert on that behavior**, the absence of an alert is a **coverage/detection gap**, not automatically a false negative.

If an existing analytic was explicitly designed to detect that exact behavior and the event satisfied its conditions but no alert was generated, then the event may represent a **false negative**.

### A12 example

The original A12 case began with a process alert on `WS-JLEE`.

Additional telemetry shows:

- `GET /update.exe` to `203.0.113.88:8080`;
- HKCU Run value `Updater` pointing to `%TEMP%\update.exe`.

A hunt can ask whether similar artifacts appear on **other hosts**.

Possible outcomes:

- more affected hosts are found;
- registry telemetry exists but no analytic covers the pattern → **detection gap**;
- some host classes do not collect registry telemetry → **visibility gap**;
- an existing rule should have alerted on the exact event but failed → investigate a possible **false negative**.

The hunt output should preserve these distinctions instead of describing every unalerted event as a failed detection.

## 2. Knowledge Check

1. Why is threat hunting complementary to the SOC rather than a replacement for it?
2. What is the difference between a detection gap and a visibility gap?
3. HTTP telemetry contains `GET /update.exe`, but no analytic is designed to alert on that pattern. Is the missing alert automatically a false negative? Explain.

## 3. Summary

Threat hunting searches beyond what existing alerts have already surfaced.

Its value is not limited to finding compromise. Hunts also expose coverage and visibility gaps and generate reusable defensive knowledge.

Call something a **false negative** only when a control was expected to detect it and failed.

**Next:** **3.2.1 – Hunt Types**.
