# Module 4.7 – Sensor and Data Availability for Detection

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.7 A / B / B ; 4.7.1 2b / 3c / 3c ; 4.7.2 2b / 3c / 3c  
- SOC: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
- Hunter: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
- CTI: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Given “the detection never fired,” distinguish a **logic problem**, a **data-path problem**, a **coverage problem**, or a combination.
2. Explain why absent or unhealthy telemetry limits the conclusion you can draw from a silent detection.

**Mapped Proficiency Items:**
- K: 4.7 – Sensor availability and performance
- T: 4.7.1 – Given “the rule never fired,” check the rule, the sensor/data path, or both
- T: 4.7.2 – Reject treating missing telemetry as proof the activity did not happen

## 1. Key Concepts

A detection can only evaluate evidence that reaches it in the expected form.

When a rule is silent, the problem may be:
- the target behavior did not occur;
- the analytic logic missed it;
- the required data was not collected;
- data was collected but not transported;
- parsing/normalization changed;
- required fields were empty;
- the analytic did not cover the relevant host/user/network population;
- data arrived too late for the analytic's time logic.

That is why **“no alert” is not enough to explain what happened.**

### Think in a data path

A practical DE check moves through:

1. **Source / sensor** – was the underlying event recorded?
2. **Transport / ingestion** – did the event reach the platform?
3. **Parsing / normalization** – are the expected fields present and mapped?
4. **Coverage** – was the relevant host/user/network path actually monitored?
5. **Timeliness** – did the data arrive within the analytic window?
6. **Logic** – would the rule match the resulting event?

This is a troubleshooting model, not a requirement that DE administer every platform in the chain.

### “Dead” and “blind” are useful shorthand but incomplete

A sensor may be:
- **down** – no data;
- **blind to the target population** – it is healthy but does not cover the needed host/path;
- **degraded** – data arrives partially or late;
- **semantically broken** – events arrive but required fields/parsing changed.

The last two cases matter because a dashboard can say “sensor healthy” while the analytic still cannot operate correctly.

### Current ATT&CK terminology

MITRE ATT&CK changed its defensive model in **ATT&CK v18 (October 2025)**: the old **Data Sources** objects were deprecated, and ATT&CK now emphasizes **Detection Strategies** and platform-specific **Analytics** with explicit log-source information.

References:
- [MITRE ATT&CK – Analytics](https://attack.mitre.org/analytics/)
- [MITRE ATT&CK – Data Sources deprecation notice](https://attack.mitre.org/datasources/)

This course still uses the ordinary phrase **data source** in the generic engineering sense: the telemetry/log evidence a detection needs. Do not confuse that everyday phrase with ATT&CK's deprecated Data Source object type.

### External rule requirements are data assumptions

Sigma log sources similarly express what type of logs an analytic expects. A mismatch can make a valid rule ineffective. See [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html).

The engineering skill is to connect:

> detection logic → required fields → required telemetry → covered population

### A12 example

Suppose the encoded-PowerShell analytic does not fire during a safe replay.

Check:

- Was process creation captured on the test host?
- Does the event include the expected command-line field?
- Did the pipeline parse that field under the name the rule expects?
- Did the event arrive in time?
- Does the analytic include that host population?
- Does the condition match the replayed command?

If process events never arrived, you have a **visibility/data-path problem**.

If the event is present with the required fields but the condition misses it, you have a **logic problem**.

If both are wrong, fix both.

### Missing telemetry narrows the conclusion

If the endpoint sensor was absent for the relevant period, you can say:

> We lack the endpoint telemetry required to determine whether this analytic would have matched the activity on that host.

You cannot say:

> The activity did not happen.

That distinction protects later investigation and coverage reporting.

## 2. Knowledge Check

1. Name three places in the data path that can break a detection even when the rule logic is correct.
2. What is the difference between a healthy sensor and usable detection data?
3. ATT&CK deprecated its old Data Sources objects. Does that mean detection engineers no longer need to understand the telemetry their analytics depend on?

## 3. Summary

A silent detection can be a **behavior, logic, data, coverage, parsing, or timing** problem.

Trace the data path before concluding the rule failed—or that the activity never occurred.

Detection Engineering needs to understand telemetry dependencies even when another team administers the sensors and pipelines.

**Next:** **4.8 – Site-Specific Detection Engineering Knowledge**.

## Supporting References

- [MITRE ATT&CK – Analytics](https://attack.mitre.org/analytics/)
- [MITRE ATT&CK – Data Sources deprecation notice](https://attack.mitre.org/datasources/)
- [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html)
