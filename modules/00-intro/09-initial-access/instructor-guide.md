# Instructor Guide – Module 0.9 – Common Initial Access Paths

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared foundations)  
**Proficiency Focus:**  
- SOC: 0.9 A / B / C ; 0.9.1 2b / 3c / 4c  
- Hunter: 0.9 A / B / C ; 0.9.1 2b / 3c / 4c  
- CTI: 0.9 A / B / C ; 0.9.1 2b / 3c / 4c  
- DE: 0.9 A / B / B ; 0.9.1 1a / 2b / 3c  
**Estimated Time:** 25–35 minutes  
**Delivery Method:** Instructor-led explanation and evidence-reasoning discussion

## Context and Learning Arc

Learners have just completed 0.8, which gave them a map of email, Internet-facing systems, remote access, third-party trust, network paths, and evidence collection points. This lesson applies that environment map to the common ways an adversary may first gain or attempt to gain access.

The new capability is **bounded entry-path reasoning**. Learners should recognize the common families, identify what a supplied observation actually proves, and choose the next evidence needed. The lesson deliberately stops before detailed endpoint, Zeek, SOC investigation, CTI, hunt, or DE procedures; those come in the role tracks.

A12 is the final worked boundary: its initial-access mechanism remains unresolved because the canonical case does not provide evidence that selects one path. Under the spoiler-light A12 rule, do not preview the detailed process/network/registry observations that are introduced later in 1.x.

## Learning Objectives

1. Recognize common initial-access paths and connect them to the environment areas introduced in 0.8.
2. Distinguish exposure or delivery from an access attempt, successful access, and later execution.
3. Given a short scenario, identify the most defensible initial-access path—or leave it unresolved—and name the next evidence that would test the hypothesis.

**Mapped Proficiency Items:**
- K: 0.9 – Common initial access paths
- T: 0.9.1 – Identify the most defensible initial-access path from supplied evidence, preserve uncertainty, and name the next evidence needed

## Preparation

Read the [student guide](student-guide.md) and review the ATT&CK Initial Access technique list. Keep the emphasis on evidence strength rather than memorizing technique IDs. No live platform or lab is required.

## Suggested Timing

| Section | Time | Teaching purpose |
|---|---:|---|
| Preview and prediction | 3 min | Connect 0.8 terrain to possible entry paths. |
| Common entry-path families | 8–10 min | Build the practical map without turning it into an exhaustive ATT&CK lecture. |
| Evidence progression and sources | 7–9 min | Separate delivery/attempt/success/execution and choose useful next evidence. |
| A12 boundary example | 4–5 min | Practice leaving an unsupported entry path unresolved. |
| Knowledge check and summary | 5–7 min | Confirm evidence-based reasoning. |

## Teaching Notes

### Start from 0.8

Ask learners to name an environment area from 0.8, then ask how an adversary could try to enter through it. Examples: email → phishing; Internet-facing application → exploit attempt; remote access → valid-account use; trusted third party → trusted-relationship abuse.

The point is to connect attack paths to the environment, not to imply that every environment has every path.

### Teach families, then evidence progression

Use five practical families: phishing/malspam; public-facing exploitation; drive-by/web paths; valid accounts/remote services; trusted relationships/supply chain.

After each family, ask: **What would we have if the path were only exposed? What would show an attempt? What would move us toward successful access?**

This prevents labels such as “phishing” or “CVE exploit” from becoming conclusions stronger than the supplied records.

### Explain SEO poisoning and malvertising carefully

SEO poisoning, malicious advertising, and similar lures often explain how a user was directed toward malicious content. They are not automatically the final ATT&CK mapping for the access event. Have learners describe the observed web path, exploit, download, or user execution separately.

### Keep the generic phishing example separate from A12

Use `shipping-notice.js` for the generic mail-delivery example and identify it as a **separate classroom example — not A12**. The point is the evidence progression, not the recurring case.

### Use A12 as an intentionally incomplete, spoiler-light example

At 0.9, learners only need to know that suspicious activity will later be investigated on **WS-JLEE** and that the canonical entry path is unresolved.

Do **not** preview the later A12 process, network, or registry observations. Those facts are introduced in 1.x where learners are expected to interpret them.

The canonical case supplies no mail message, browser chain, public-facing exploit, login, or third-party record connecting the activity to one initial-access method.

The correct answer is **unresolved**, followed by the evidence that would test specific hypotheses. Reward that answer rather than encouraging a plausible story.

## Knowledge Check — Answer Key

### 1. Delivered malicious attachment, no endpoint evidence

**Expected answer:** Phishing/malspam is supported as a delivery path because the message and attachment reached the user. Opening, execution, successful access, and later compromise remain unproven. Next evidence could include click/open telemetry, file creation, or process activity around the delivery time.

### 2. Vulnerable public-facing application plus exploit-pattern request

**Expected answer:** The vulnerable condition and request support exposure plus an exploit attempt. To establish successful access, look for application/WAF response context, resulting sessions, abnormal child processes, file changes, authentication or service changes, or other host evidence consistent with exploitation.

### 3. A12 entry path

**Expected answer:** A12 initial access remains unresolved because no canonical mail, browser, public-facing exploit, authentication, or third-party record establishes the entry mechanism. The next evidence depends on the hypotheses being tested—mail/message data, browser/proxy records, identity/remote-access records, or other relevant collection.

## Skim-First Instructor Check

A learner skimming only the opening, headings, tables, bold terms, A12 section, and closing should be able to see:

- the five practical initial-access families;
- the evidence progression from exposure/delivery through successful access and later behavior;
- that the next collection source follows the unresolved question;
- that A12's entry path intentionally remains unresolved;
- that detailed A12 SOC evidence is intentionally deferred to 1.x.

## Course Connections

Previous: [0.8 – Environment / signal flow](../08-environment/01-orientation/student-guide.md)

Next: [0.10 – Shared Foundations Section Summary](../10-summary/student-guide.md)

## References and Further Reading

- [MITRE ATT&CK — Initial Access (TA0001)](https://attack.mitre.org/tactics/TA0001/)
- [CISA — #StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) — Includes common initial-access vectors and advanced social-engineering examples such as SEO/search poisoning.
- [MITRE ATT&CK — Phishing (T1566)](https://attack.mitre.org/techniques/T1566/)
- [MITRE ATT&CK — Drive-by Compromise (T1189)](https://attack.mitre.org/techniques/T1189/)
- [MITRE ATT&CK — Exploit Public-Facing Application (T1190)](https://attack.mitre.org/techniques/T1190/)
- [MITRE ATT&CK — Valid Accounts (T1078)](https://attack.mitre.org/techniques/T1078/)
- [MITRE ATT&CK — External Remote Services (T1133)](https://attack.mitre.org/techniques/T1133/)
- [MITRE ATT&CK — Trusted Relationship (T1199)](https://attack.mitre.org/techniques/T1199/)
- [MITRE ATT&CK — Supply Chain Compromise (T1195)](https://attack.mitre.org/techniques/T1195/)
