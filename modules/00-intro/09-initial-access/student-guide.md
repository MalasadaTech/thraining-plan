# Module 0.9 – Common Initial Access Paths

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared foundations)  
**Proficiency Focus:**  
- SOC: 0.9 A / B / C ; 0.9.1 2b / 3c / 4c  
- Hunter: 0.9 A / B / C ; 0.9.1 2b / 3c / 4c  
- CTI: 0.9 A / B / C ; 0.9.1 2b / 3c / 4c  
- DE: 0.9 A / B / B ; 0.9.1 1a / 2b / 3c  
**Estimated Time:** 25–35 minutes

## Why This Matters

Module 0.8 gave you the terrain: email paths, Internet-facing systems, remote access, third-party trust, network routes, and the places evidence may be collected. Initial access asks a different question: **how might an adversary first gain, or try to gain, a foothold through that terrain?**

The useful skill is separating an **entry-path hypothesis** from evidence that the path actually succeeded; memorizing attack names is secondary to that reasoning. A phishing message can be delivered without being opened. A vulnerable web server can receive exploit traffic without being compromised. A successful VPN login proves that an account was used, but it does not by itself prove the user was an adversary.

As you read, predict what evidence would move each example from *possible path* to *supported initial access*. The course principle still applies: **Describe what the evidence shows first. Then decide what it means.**

## Learning Objectives

By the end of this module, you will be able to:

1. Recognize common initial-access paths and connect them to the environment areas introduced in 0.8.
2. Distinguish exposure or delivery from an access attempt, successful access, and later execution.
3. Given a short scenario, identify the most defensible initial-access path—or leave it unresolved—and name the next evidence that would test the hypothesis.

**Mapped Proficiency Items:**
- K: 0.9 – Common initial access paths
- T: 0.9.1 – Identify the most defensible initial-access path from supplied evidence, preserve uncertainty, and name the next evidence needed

## 1. Initial access is an objective, not a verdict

MITRE ATT&CK uses **Initial Access** for techniques adversaries use to gain their first foothold in an environment. The tactic includes paths such as phishing, drive-by compromise, exploitation of public-facing applications, valid accounts, external remote services, trusted relationships, and supply-chain compromise.

That vocabulary helps describe *how access could occur*. It does not remove the need to prove what happened in the case in front of you. The same observation can sit at different points in the evidence progression:

**Exposure or delivery → interaction / access attempt → successful access → later execution or follow-on behavior**

For example, a malicious attachment in a mailbox establishes delivery. A process event showing the attachment launching code establishes something later in the chain. The first observation should not be rewritten as the second merely because the analyst expects one to lead to the other.

ATT&CK and the Cyber Kill Chain may both help describe the same incident from different angles. ATT&CK Initial Access names adversary entry techniques. The Kill Chain asks about progression such as Delivery and Exploitation. Use the framework that answers the question you are asking and keep the underlying observations visible.

## 2. Common entry paths

| Entry-path family | What it can look like | Evidence that may support it | Important boundary |
|---|---|---|---|
| **Phishing / malspam** | Attachment, link, or message delivered through email or another service | Message headers, gateway records, attachment/link metadata, click/open records, endpoint process/file evidence | Delivery does not prove the user opened it, code ran, or access succeeded. |
| **Public-facing exploitation** | Exploit attempt against an Internet-facing application, API, appliance, or service | WAF/app/service logs, exploit request, error/response patterns, vulnerable version context, resulting process/session/file changes | A CVE or vulnerable version establishes exposure; an exploit request establishes an attempt; neither alone proves compromise. |
| **Drive-by / watering hole / malicious web path** | User visits adversary-controlled or compromised web content; malvertising or search/SEO poisoning may steer the user there | Browser/proxy/DNS/HTTP records, redirect chain, downloaded content, exploit response, endpoint browser-child processes or files | A visit or redirect does not prove exploitation. SEO poisoning or malvertising often explains how the user was steered; map the actual access behavior supported by evidence. |
| **Valid account / external remote service** | VPN, webmail, cloud, remote desktop, Citrix, SSH, or another externally reachable service is used with an account | Authentication logs, MFA events, device/source context, session creation, remote-service records, authorization/context from the account owner | A successful login proves account use. It does not by itself establish that the account was stolen or the session was malicious. |
| **Trusted relationship / supply chain** | Third-party access, trusted identity, dependency, software update, or delivery mechanism is abused | Third-party/session records, software/update provenance, build/dependency evidence, package history, affected-version context | The existence of a trust path or dependency is exposure context. Evidence must connect that path to the actual intrusion. |

These families are a practical map rather than an exhaustive catalog. Real incidents can combine them. A phishing link can send a user to a malicious website; a compromised vendor account can use an external remote service; a watering-hole page can exploit a browser vulnerability. When paths overlap, describe each observed step rather than forcing the incident into one label too early.

## 3. Match the question to the evidence source

Module 0.8 introduced where activity may travel and where evidence may exist. Initial-access reasoning turns that orientation into a collection question.

| Hypothesis | Useful evidence sources |
|---|---|
| Phishing or malspam delivered the first artifact | Mail/security gateway, message trace, mailbox metadata, URL/attachment handling, endpoint file/process evidence |
| Internet-facing exploitation provided access | Public-facing application/service logs, WAF/reverse proxy, authentication/session records, process/file activity on the server, vulnerability/patch context |
| A web path led to client compromise | Proxy/DNS/HTTP, browser history where authorized, redirect/download records, endpoint process/file activity |
| A valid account or remote service was used | Identity provider, VPN/remote service, MFA, device/source context, account-owner validation, resulting session activity |
| A trusted third party or supply chain was involved | Third-party identity/session records, software/update/dependency provenance, vendor reporting, local installation/execution evidence |

The next source should answer the uncertainty you actually have. If you already know a message was delivered, another copy of the mail header may add little. The next useful question may be whether the user interacted with the message or whether an endpoint process followed it.

## 4. Work from evidence strength

A useful initial-access statement has four parts:

1. **Observation:** what the source actually recorded.
2. **Reasoning:** why that observation supports one path more than another.
3. **Bounded conclusion:** the strongest claim the evidence supports now.
4. **Next test:** the evidence that would strengthen, reject, or replace the hypothesis.

> **Scenario status: Separate classroom example — not A12.**

Example:

> The mail gateway recorded delivery of a message containing `shipping-notice.js` to the user. This supports phishing or malspam as a possible delivery path. The record does not establish that the attachment was opened or executed. Check endpoint file/process evidence and user-interaction telemetry for the message time before concluding that phishing produced host activity.

Another example:

> The VPN recorded a successful login for a valid employee account from an unfamiliar source. This establishes that the account authenticated through the remote service. Whether the session represents adversary access remains unresolved until authorization, MFA/device context, and resulting session activity are checked.

The bounded conclusion is useful because it tells the next analyst both what is known and what work remains.

## 5. A12: keep the entry path unresolved

At this point in the course, A12 is used to establish one shared-foundation fact: **suspicious activity will later be investigated on WS-JLEE, but the entry path is not known**.

Detailed A12 process, network, and registry observations are intentionally introduced later in the SOC track. Nothing available in the shared-foundation view establishes phishing, a malicious web path, public-facing exploitation, valid-account or remote-service abuse, or a trusted-third-party/supply-chain path.

The canonical case supplies no mail record tying the activity to phishing, no browser chain proving a drive-by path, no public-facing exploitation record, no authentication record establishing account-based entry, and no third-party or supply-chain evidence connecting those paths to A12.

So the defensible initial-access conclusion is:

> **A12 initial access remains unresolved.**

Leaving the path unresolved is the analytical answer supported by the current evidence. If reconstructing the entry path became important, the analyst would choose the next source based on the hypotheses being tested—for example mail/message records, browser/proxy history, identity/remote-access logs, or other case-relevant evidence.

## Knowledge Check

1. A mail gateway shows a malicious attachment was delivered, but you have no endpoint evidence yet. What initial-access conclusion can you support, and what remains unproven?
2. An Internet-facing application is vulnerable to a CVE and receives a request matching a published exploit pattern. What additional evidence would you want before concluding the exploit provided access?
3. For A12, no canonical mail, browser, public-facing exploit, authentication, or third-party record establishes how access began. What is the correct conclusion, and what evidence would you seek next?

## By This Point, You Should Be Able To…

You should now be able to recognize the major initial-access families, connect them to likely evidence sources, and place an observation at the correct point in the evidence progression. Most importantly, you should be comfortable leaving the entry path unresolved when the available evidence does not establish it, while still naming the next evidence that would make the hypothesis testable.

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
