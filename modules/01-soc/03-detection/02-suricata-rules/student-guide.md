# Module 1.3.2 – Suricata Rules

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.2.1 A / B / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 1a / 2b / 3c  
- Hunter: 1.3.2.1 B / C / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 2b / 3c / 4c  
- CTI: 1.3.2.1 A / B / B ; 1.3.2.2 1a / 2b / 3c ; 1.3.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret rule action, header, options, and text/hex/regex matching.
2. Describe a rule’s traffic and match conditions.
3. Create or modify a basic rule and relate a hit to other network evidence.

**Mapped Proficiency Items:**
- K: 1.3.2.1 – Suricata rules
- T: 1.3.2.2 – Analyze an existing Suricata rule and describe what it detects
- T: 1.3.2.3 – Create or modify a basic Suricata rule

## Why This Matters

Suricata rules express conditions to inspect in network traffic. Reading the protocol, direction, and inspection buffer helps explain why a signature matched and whether its meaning agrees with the analyst’s description.

## 1. Understanding header and options

A rule begins with an action, followed by protocol, source address/port, direction, destination address/port, and options. This lesson uses the `alert` action. Options include the message, signature identifier (`sid`), revision (`rev`), and match conditions.

`content` can represent literal text or bytes, such as `content:"|4d 5a|";`. A `pcre` expression can match variable text, but its scope and performance need care. Sticky buffers such as `http.method`, `http.uri`, `http.user_agent`, and `tls.sni` select which parsed data subsequent tests inspect.

`$HOME_NET` and `$EXTERNAL_NET` are configured variables. Their actual values determine scope; `$EXTERNAL_NET` is not necessarily defined as the complement of `$HOME_NET`. Confirm them when explaining a rule's direction.

## 2. Reading a basic proposal

```suricata
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"TRAINING HTTP update path"; flow:established,to_server; http.method; content:"GET"; bsize:3; http.uri; content:"/update.exe"; sid:1000001; rev:1;)
```

The rule alerts on established client-to-server HTTP traffic matching the configured network variables, an exact three-byte GET method, and a normalized URI containing `/update.exe`. The URI content test is a substring: `/folder/update.exe` also fits. This is a classroom example, and its SID is illustrative; operational proposals need an unused identifier from local practice.

A matching Zeek HTTP record may provide request context if Zeek observed and parsed the same traffic. Correlate time and the five-tuple (source/destination IPs and ports plus protocol), accounting for sensor location and translation. A Suricata hit does not guarantee a Zeek record exists.

## 3. Modifying the matching scope

If the intended target is exactly `/update.exe`, add `bsize:11;` after its URI content test. This excludes longer normalized URI strings, including query strings. If those should be included, the proposal needs a different, explicitly described condition.

A raw `content:"GET"` test on general TCP traffic searches for bytes without the HTTP-method context. Choosing the protocol buffer makes the intent clearer and reduces unrelated matches. For each modification, explain a match and a nonmatch, then pass the proposal for review and testing.

## Knowledge Check

1. What do the header and sticky buffer each control?
2. Does the example match /folder/update.exe? Explain.
3. Modify the URI test for exactly /update.exe and name an excluded request.

## Summary

A clear Suricata proposal identifies the traffic scope and the exact buffer and pattern inspected. Explain what matches, what does not, and what related network evidence could add.

## Course Connections

Previous: [1.3.1 – SIGMA Rules](../01-sigma-rules/student-guide.md)

Next: [1.3.3 – YARA Rules](../03-yara-rules/student-guide.md)

[1.x module index](../../README.md)

## References and Further Reading

- [Suricata — Rule format](https://docs.suricata.io/en/latest/rules/intro.html)
- [Suricata — HTTP keywords](https://docs.suricata.io/en/latest/rules/http-keywords.html)
