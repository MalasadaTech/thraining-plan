# Module 1.3.2 – Suricata Rules

- Interpret rule action, header, options, and text/hex/regex matching.
- Describe a rule’s traffic and match conditions.
- Create or modify a basic rule and relate a hit to other network evidence.

**Speaker notes:** Explain the purpose of the lesson and the understanding learners should demonstrate.

---

## Why this matters

Suricata rules express conditions to inspect in network traffic. Reading the protocol, direction, and inspection buffer helps explain why a signature matched and whether its meaning agrees with the analyst’s description.

**Speaker notes:** Connect the topic to the evidence or decision learners encountered in the previous lesson.

---

## Understanding header and options

Read action, header, variables, flow, and buffer-specific tests. Actual variable values determine network scope.

**Speaker notes:** Explain the variables from actual configuration or label their values unspecified. Distinguish text, hex, and regex as matching representations.

---

## Reading a basic proposal

The example matches GET and a URI containing /update.exe. A longer URI can also match.

**Speaker notes:** Read the rule by action, header, flow, method, then URI. Emphasize that bsize on the method and a substring on the URI have different effects.

---

## Worked example — Reading a basic proposal

```suricata
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"TRAINING HTTP update path"; flow:established,to_server; http.method; content:"GET"; bsize:3; http.uri; content:"/update.exe"; sid:1000001; rev:1;)
```

**Speaker notes:** Read the rule by action, header, flow, method, then URI. Emphasize that bsize on the method and a substring on the URI have different effects. Use the student guide for the stated input, schema assumptions, and interpretation limits. The code is a teaching example for discussion, not a deployment instruction.

---

## Modifying the matching scope

Adding URI bsize:11 requires the exact-length URI. Explain whether query strings should be included.

**Speaker notes:** Use exact path, longer path, and query-string cases to evaluate the change. Production deployment and packet replay are outside this worked discussion.

---

## Knowledge check

1. What do the header and sticky buffer each control?
2. Does the example match /folder/update.exe? Explain.
3. Modify the URI test for exactly /update.exe and name an excluded request.

**Speaker notes:** Ask learners to explain their reasoning. Use the [instructor answer key](instructor-guide.md#knowledge-check--answer-key) for feedback.

---

## Summary and next step

A clear Suricata proposal identifies the traffic scope and the exact buffer and pattern inspected. Explain what matches, what does not, and what related network evidence could add.

Previous: [1.3.1 – SIGMA Rules](../01-sigma-rules/student-guide.md)

Next: [1.3.3 – YARA Rules](../03-yara-rules/student-guide.md)

[1.x module index](../../README.md)

**Speaker notes:** Resolve any remaining uncertainty from the check and connect the next lesson.

---

## References and Further Reading

- [Suricata — Rule format](https://docs.suricata.io/en/latest/rules/intro.html)
- [Suricata — HTTP keywords](https://docs.suricata.io/en/latest/rules/http-keywords.html)

**Speaker notes:** The linked primary sources support definitions and technical details. Check the deployed version and local schema for operational use.
