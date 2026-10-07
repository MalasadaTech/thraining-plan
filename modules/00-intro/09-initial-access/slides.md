# Module 0.9 – Common Initial Access Paths

## Why this matters

The environment tells you **where access could happen**. Initial-access reasoning asks **which path the evidence supports**.

Watch the progression:

**Exposure / delivery → attempt → successful access → later execution**

**Speaker notes:** Connect directly to 0.8. Ask learners to predict what evidence would be needed to move from a possible path to supported access.

---

## Five practical entry-path families

- Phishing / malspam
- Public-facing exploitation
- Drive-by / watering-hole / malicious web path
- Valid accounts / external remote services
- Trusted relationships / supply chain

**Speaker notes:** These are a practical map, not an exhaustive ATT&CK catalog. Real incidents can combine families.

---

## Phishing: delivery is only the first observation

Message delivered → user interaction? → file/process activity? → successful access?

A malicious attachment in a mailbox establishes delivery. It does not establish execution.

**Speaker notes:** Reinforce the evidence progression. Mail records and endpoint records answer different questions.

---

## Public-facing exploitation: vulnerable is not compromised

A CVE or vulnerable version establishes exposure.

An exploit-pattern request supports an attempt.

Successful access needs resulting evidence.

**Speaker notes:** Ask learners what application, WAF, session, process, or file evidence could move the conclusion forward.

---

## Web paths: separate the lure from the access event

Watering holes, malvertising, and search/SEO poisoning can steer a user to malicious content.

Then ask what happened:

visit → redirect/download → exploit or user action → resulting host behavior

**Speaker notes:** Avoid teaching “SEO poisoning” as if it were automatically the ATT&CK technique that completed access. Map the behavior actually observed.

---

## Accounts and remote services

A successful VPN, cloud, or remote-service login proves **account use**.

Authorization and adversary control require context:

- source/device
- MFA
- account-owner validation
- resulting session activity

**Speaker notes:** This is an important non-malware entry path. Keep “login happened” separate from “account was compromised.”

---

## Third-party and supply-chain paths

A trusted connection, dependency, or update mechanism can become an entry path.

The relationship itself is exposure context. Evidence must connect it to the incident.

**Speaker notes:** Tie this back to 0.8 third-party access/federation and to software provenance where relevant.

---

## Choose the next evidence for the unresolved question

| Hypothesis | Useful next evidence |
|---|---|
| Phishing | Mail/message + endpoint interaction |
| Public-facing exploit | App/WAF + host/session evidence |
| Web path | Proxy/browser + endpoint evidence |
| Valid account | Auth/MFA/device + session activity |
| Third party / supply chain | Trust/session or package/update provenance + local evidence |

**Speaker notes:** The goal is not “collect everything.” Pick the source that can change the conclusion.

---

## A12: initial access remains unresolved

At this point:
- suspicious activity will later be investigated on `WS-JLEE`;
- detailed process, network, and registry evidence is intentionally introduced in 1.x.

Not supplied:
- mail path tying the activity to phishing
- browser chain
- public-facing exploit evidence
- account/remote-service entry evidence
- third-party/supply-chain link

**Conclusion:** **A12 initial access remains unresolved.**

**Speaker notes:** Reward the unresolved answer. Do not preview later SOC evidence. Ask learners which evidence source they would request for two different entry-path hypotheses.

---

## Knowledge check

1. A malicious attachment was delivered, but there is no endpoint evidence. What can you conclude?
2. A vulnerable web app receives an exploit-pattern request. What evidence would establish more than an attempt?
3. A12 has no canonical mail, browser, exploit, authentication, or third-party record establishing entry. What is the correct conclusion, and what would you request next?

**Speaker notes:** Use the instructor guide answer key. Require the evidence boundary and next evidence, not only the path label.

---

## By this point, you should be able to…

Recognize common entry paths, state the strongest step the evidence supports, and choose the next evidence that would test the hypothesis.

When the evidence does not identify the entry path, **leave it unresolved and explain what would resolve it.**

Previous: [0.8 – Environment / signal flow](../08-environment/01-orientation/student-guide.md)  
Next: [0.10 – Shared Foundations Section Summary](../10-summary/student-guide.md)

**Speaker notes:** Confirm the learner can move from an entry-path label to evidence, reasoning, bounded conclusion, and next action.

---

## References and further reading

- [MITRE ATT&CK — Initial Access (TA0001)](https://attack.mitre.org/tactics/TA0001/)
- [CISA — #StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) — Includes common initial-access vectors and advanced social-engineering examples such as SEO/search poisoning.
- [MITRE ATT&CK — Phishing (T1566)](https://attack.mitre.org/techniques/T1566/)
- [MITRE ATT&CK — Drive-by Compromise (T1189)](https://attack.mitre.org/techniques/T1189/)
- [MITRE ATT&CK — Exploit Public-Facing Application (T1190)](https://attack.mitre.org/techniques/T1190/)
- [MITRE ATT&CK — Valid Accounts (T1078)](https://attack.mitre.org/techniques/T1078/)
- [MITRE ATT&CK — External Remote Services (T1133)](https://attack.mitre.org/techniques/T1133/)
- [MITRE ATT&CK — Trusted Relationship (T1199)](https://attack.mitre.org/techniques/T1199/)
- [MITRE ATT&CK — Supply Chain Compromise (T1195)](https://attack.mitre.org/techniques/T1195/)

**Speaker notes:** Use ATT&CK as the primary reference for the shared technique vocabulary. The lesson's core outcome is evidence reasoning, not memorization of IDs.
