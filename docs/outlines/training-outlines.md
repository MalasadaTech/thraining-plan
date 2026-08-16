# Training Outlines – SOC Analyst, Threat Hunter, CTI Analyst

**Manning & Qualification Rules**
- 1-level: Never authorized to work on shift
- 3-level: Must never work alone; must be supervised/trained by at least a 7-level
- 5-level: May work a shift alone
- 7-level: Qualified to supervise and train 3-levels

These rules apply across SOC Analyst, Threat Hunter, and CTI Analyst roles.

---

# 1. SOC Analyst Fundamentals

**1.1 [K/T] Endpoint Logs**

Endpoint telemetry (Sysmon / MDE) vs network-sensor telemetry (Zeek, unit 1.2). Sysmon Event IDs and MDE tables encode the same activities; this unit is not Sysmon installation or configuration.

**1.1.1 [K] Process activity**  
a. Process create / terminate  
b. PID, name, command line  
c. Parent-child (PPID, parent name, parent command line)  
d. Integrity / user context (where logged)  
e. Hashes and original filename (where logged)  
f. Process access (Sysmon Event ID 10) as “who touched whom,” not a separate unit  
g. How this shows up: Sysmon 1 / 5 / 10; MDE `DeviceProcessEvents` (key fields: `ActionType`, `InitiatingProcess*`, `ProcessCommandLine`, SHA256)  

**1.1.1.1 [T] Process activity tasks**  
1. Analyze a process event (Sysmon or MDE) and accurately describe what occurred  
2. Create a SIEM query to detect specific process activity  

**1.1.2 [K] File system activity**  
a. Create / rename-move / delete / modify / read (where logged)  
b. Path, name, extension  
c. Hashes  
d. Initiating process  
e. How this shows up: Sysmon 11 / 23 / 26; MDE `DeviceFileEvents` (`ActionType`, `FolderPath`, `FileName`, SHA256, `InitiatingProcess*`)  

**1.1.2.1 [T] File system activity tasks**  
1. Analyze a file event (Sysmon or MDE) and accurately describe what occurred  
2. Create a SIEM query to detect specific file operations  

**1.1.3 [K] Network activity (endpoint)**  
a. Source / dest IP and port, protocol, direction  
b. Domain / URL when the endpoint logged them  
c. Initiating process (this is the point of 1.1 vs Zeek)  
d. How this shows up: Sysmon 3 (and 22 if DNS is logged here); MDE `DeviceNetworkEvents`  
e. This is host-observed activity. Protocol deep-dive is 1.2  

**1.1.3.1 [T] Network activity tasks**  
1. Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred  
2. Create a SIEM query to detect specific endpoint network activity  

**1.1.4 [K] Registry activity**  
a. Hives and key → value  
b. Set / delete / rename  
c. Common persistence locations (Run, Services) as examples, not a 2.6 dump  
d. Initiating process  
e. How this shows up: Sysmon 12 / 13 / 14; MDE `DeviceRegistryEvents`  

**1.1.4.1 [T] Registry activity tasks**  
1. Analyze a registry event (Sysmon or MDE) and accurately describe what occurred  
2. Create a SIEM query to detect specific registry operations  

**1.1.5 [K] Image and driver load activity**  
a. User-mode image load vs kernel driver load  
b. Path, hashes, signed vs unsigned (where logged)  
c. Initiating process  
d. How this shows up: Sysmon 6 / 7; MDE `DeviceImageLoadEvents`  

**1.1.5.1 [T] Image and driver load tasks**  
1. Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred  
2. Create a SIEM query to detect specific image or driver load activity  

**1.2 [K/T] Zeek and Zeek Engines**

Network-sensor telemetry. Host-observed process/file/network/registry/image activity is 1.1.

**1.2.1 [K] Zeek concepts**  
a. Zeek as a network analysis framework  
b. How Zeek uses engines (scripts/analyzers) to classify and extract protocol data  
c. How engines surface relevant applications and protocols  

**1.2.2 [K] Conn engine**  
a. Source IP (orig_h)  
b. Source port (orig_p)  
c. Destination IP (resp_h)  
d. Destination port (resp_p)  
e. Connection state / history  

**1.2.3 [T] Conn engine tasks**  
1. Analyze a Zeek conn log and accurately describe what occurred  
2. Create a SIEM query to detect specific connection activity  

**1.2.4 [K] DNS engine**  
a. DNS query (question)  
b. DNS response (answer)  
c. Common DNS record types (A, AAAA, MX, CNAME, NS, TXT, etc.)  
d. Source and destination fields in DNS logs  

**1.2.5 [T] DNS engine tasks**  
1. Analyze a Zeek DNS log and accurately describe what occurred  
2. Create a SIEM query to detect specific DNS activity  

**1.2.6 [K] TLS engine**  
a. Server Name Indication (SNI)  
b. Certificate subject / issuer  
c. JA3 / JA3S fingerprints (where available)  
d. TLS version  
e. Cipher suite  
f. Source and destination fields  

**1.2.7 [T] TLS engine tasks**  
1. Analyze a Zeek TLS log and accurately describe what occurred  
2. Create a SIEM query to detect specific TLS activity  

**1.2.8 [K] HTTP engine**  
a. Method (GET, POST, etc.)  
b. Host  
c. URI / URL  
d. User-Agent  
e. Status code  
f. Source and destination fields  

**1.2.9 [T] HTTP engine tasks**  
1. Analyze a Zeek HTTP log and accurately describe what occurred  
2. Create a SIEM query to detect specific HTTP activity  

**1.2.10 [K] SMTP engine**  
a. Mail from  
b. Rcpt to  
c. Subject  
d. Message ID  
e. Source and destination fields  

**1.2.11 [T] SMTP engine tasks**  
1. Analyze a Zeek SMTP log and accurately describe what occurred  
2. Create a SIEM query to detect specific SMTP activity  

**1.2.12 [K] Files engine**  
a. File name  
b. MIME type  
c. File hash (MD5, SHA1, SHA256)  
d. Source and destination fields  
e. Connection UID (linking to other Zeek logs)  

**1.2.13 [T] Files engine tasks**  
1. Analyze a Zeek files log and accurately describe what occurred  
2. Create a SIEM query to detect specific file transfer activity  

**1.2.14 [K] Weird engine**  
a. Weird activity type / notice  
b. Source and destination fields  
c. Connection UID (linking to other Zeek logs)  

**1.2.15 [T] Weird engine tasks**  
1. Analyze a Zeek weird log and accurately describe what occurred  
2. Create a SIEM query to detect specific weird activity  

**1.3 [T] Detection Engineering**

**1.3.1 [K] SIGMA rules**  
a. Purpose and structure of a SIGMA rule  
b. Common fields / selectors used in SIGMA  
c. How SIGMA translates to SIEM queries  

**1.3.2 [T] SIGMA tasks**  
1. Analyze an existing SIGMA rule and describe what it detects  
2. Create or modify a basic SIGMA rule  

**1.3.3 [K] Suricata rules**  
a. Rule structure (action, header, options)  
b. Common rule options (content, http.*, tls.*, etc.)  
c. Matching techniques: ASCII, hex, and regex  
d. How Suricata rules relate to Zeek / network logs  

**1.3.4 [T] Suricata tasks**  
1. Analyze an existing Suricata rule and describe what it detects  
2. Create or modify a basic Suricata rule  

**1.3.5 [K] YARA rules**  
a. Purpose and structure of a YARA rule  
b. Common string and condition usage  
c. Matching techniques: ASCII, hex, and regex  
d. How YARA is used with files / memory  

**1.3.6 [T] YARA tasks**  
1. Analyze an existing YARA rule and describe what it detects  
2. Create or modify a basic YARA rule  

**1.3.7 [K] SIEM rules**  
a. Structure of SIEM detection rules / correlation searches  
b. Common techniques for turning log fields into detections  
c. Matching techniques: regex and wildcards  

**1.3.8 [T] SIEM tasks**  
1. Analyze an existing SIEM rule and describe what it detects  
2. Create a basic SIEM detection rule from log fields or a SIGMA rule  

**1.4 [K/T] Alerts**

Alert handling. Detection *authoring* is 1.3. Each knowledge item has its own tasks; tasks apply the knowledge, they do not restate it.

**1.4.1 [K] Alert context and investigation**  
a. Viewing the context provided by the alert  
b. Reviewing the alert configuration  
c. Understanding upstream alerting (e.g., Suricata rule → SIEM correlation search → SIEM alert)  
d. Pulling related endpoint logs that led up to the event  
e. Pulling and reviewing PCAP for the network traffic that triggered the alert  

**1.4.1.1 [T] Alert investigation tasks**  
1. Review an alert and identify which context is present and which is missing  
2. Review the alert configuration and explain what would fire  
3. Trace an alert to its upstream detection logic and name each hop  
4. Collect related endpoint logs and state what they add (or fail to add)  
5. Collect related PCAP and state what it adds versus the alert fields  

**1.4.2 [K] Alert classification**  
a. True Positive  
b. False Positive  
c. True Negative  
d. False Negative  

**1.4.2.1 [T] Alert classification tasks**  
1. Classify given cases as TP, FP, TN, or FN and cite the evidence (include at least one missed detection as FN)  

**1.4.3 [K] Common false positive causes**  
a. Security analyst or tool activity (e.g., downloading/testing rules that are already deployed)  
b. Untuned or overly broad detection logic  

**1.4.3.1 [T] False positive cause tasks**  
1. Given a false positive, identify the cause class and what you would change  

**1.4.4 [K] Common alert categorizations**  
a. Scanning / Reconnaissance  
b. Root-level access  
c. User-level access  
d. Unsuccessful activity  
e. Other common categories (as used in your environment)  

**1.4.4.1 [T] Alert categorization tasks**  
1. Assign a category to an alert and justify why it is not the adjacent category  

**1.4.5 [K] Service Level Agreements / Response Time Goals**  
a. Maximum time allowed before an alert investigation must begin  
b. Required time to process an alert (close or escalate)  

**1.4.5.1 [T] SLA / Response Time tasks**  
1. Given timestamps, identify whether the start clock or the close/escalate clock is at risk  
2. Close or escalate an alert and record it against the correct clock  

**1.5 [K/T] Frameworks**

Shared analysis frameworks. Hunt *planning* with ATT&CK is 2.5. Attribution products are 3.11. Each framework has its own applying task.

**1.5.1 [K] MITRE ATT&CK**  
a. Purpose and structure of the ATT&CK framework  
b. Tactics  
c. Techniques and Sub-techniques  
d. How to map observed activity to ATT&CK  

**1.5.1.1 [T] ATT&CK tasks**  
1. Map an alert or observed activity to an ATT&CK tactic and technique (or sub-technique) and cite the evidence  

**1.5.2 [K] Diamond Model**  
a. Purpose of the Diamond Model  
b. The four core features (Adversary, Capability, Infrastructure, Victim)  
c. How the Diamond Model is used for analysis and attribution  

**1.5.2.1 [T] Diamond Model tasks**  
1. Apply the Diamond Model to an incident or set of indicators: fill the four vertices and state which vertex is weakest  

**1.5.3 [K] Cyber Kill Chain**  
a. Purpose of the Cyber Kill Chain  
b. The stages of the Kill Chain  
c. How the Kill Chain is used to understand attack progression  

**1.5.3.1 [T] Kill Chain tasks**  
1. Identify the Kill Chain stage of observed activity and why it is not the previous or next stage  

**1.6 [K/T] Reporting**

SOC reporting. Shift-change reports are **1.7**. Finished intel products are **3.11**. Alert start/close clocks are **1.4.5**. Each knowledge item has its own applying task.

**1.6.1 [K] Report types**  
a. Incident report  
b. Request for Information (RFI)  
c. Other common report types used in the environment  

**1.6.1.1 [T] Report type tasks**  
1. Identify the correct report type for a given situation and why it is not the adjacent type  

**1.6.2 [K] Reporting timeline requirements**  
a. Required timelines for submitting different report types  
b. Escalation timelines when additional information or actions are needed  

**1.6.2.1 [T] Reporting timeline tasks**  
1. Given a situation and timestamps, identify which report timeline applies (submit vs escalate-for-more-info) and whether it is at risk  

**1.6.3 [K] Notification and distribution**  
a. Notification chart / matrix (which teams or sections receive which reports)  
b. Requirement to notify leadership for awareness  
c. Approved reporting channels  

**1.6.3.1 [T] Notification and distribution tasks**  
1. Route a report: name the recipients, whether leadership gets awareness, and the approved channel (and reject the wrong channel)  

**1.7 [K/T] Shift Change**

SOC shift change. Reporting products are **1.6**. Site-specific tools and IR process are **1.8**. Each knowledge item has its own applying task.

**1.7.1 [K] Shift changeover process**  
a. Purpose and importance of a structured shift change  
b. Who should participate in the shift change  
c. Where the changeover report is recorded  

**1.7.1.1 [T] Shift changeover process tasks**  
1. Conduct or participate in a shift changeover  

**1.7.2 [K] Required content of the changeover report**  
a. Current open / in-progress investigations  
b. Newly opened, updated, or closed reports that occurred during the shift  
c. Upcoming planned service outages  
d. Ongoing service outages or outages that occurred during the shift  
e. Urgent process or policy items  

**1.7.2.1 [T] Changeover report content tasks**  
1. Produce a complete changeover report that includes all required elements  

**1.8 [K/T] Site-Specific Knowledge**

Classroom stand-ins only — overlay the live site card. Not reporting products (**1.6**), not shift change (**1.7**), not Zeek log reading (**1.2**). Each heading is its own teaching unit. Tasks apply the knowledge they sit under.

**1.8.1 [K] Environment orientation**  
a. Path to the internet / network egress points  
b. Key network segments and data flow  
c. Email flow and related systems  
d. Edge firewall architecture and key choke points  
e. Trusted third-party access / federation  
f. Crown jewel / critical assets  
g. PCAP collection points / sensors  

**1.8.1.1 [T] Environment orientation tasks**  
1. Identify which orientation fact applies to a given situation and why it is not the adjacent fact  

**1.8.2 [T] PCAP handling**  
1. How to download PCAP  
2. What tool to use to view PCAP  

**1.8.3 [T] Tool access and requests**  
1. How to access required tools and their URLs  
2. How to request tools to be installed (e.g., Wireshark)  
3. How to request access (e.g., SIEM or other platforms)  

**1.8.4 [T] Investigation documentation**  
1. Where and how to save investigation notes  

**1.8.5 [T] Incident response processes**  
1. Follow site-specific incident response processes  

---

# 2. Threat Hunter

**2.1 [K] Purpose of Threat Hunting**  
a. Identify malicious or suspicious activity missed by existing security mechanisms  
b. Identify detection and visibility gaps  

**2.1.1 [T] Tasks**  
1. Explain the purpose of threat hunting in the context of the security program  
2. Identify examples of activity that existing controls might miss  

**2.2 [K/T] Hunt Methodology**  

**2.2.1 [K] Hunt types**  
a. Intel-driven hunts  
b. Hypothesis-driven hunts  
c. Reactive hunts  
d. Anomaly-based hunts  

**2.2.2 [K] Hunt development concepts**  
a. Developing a hunt hypothesis  
b. Scoping a hunt  
c. Prioritizing hunts  
d. Identifying unique patterns or behaviors for internal searches  

**2.2.3 [T] Hunt methodology tasks**  
1. Develop and document a hunt hypothesis  
2. Scope and prioritize a hunt  
3. Identify unique patterns or behaviors suitable for hunting  
4. Execute an intel-driven hunt  
5. Execute a hypothesis-driven hunt  
6. Execute a reactive hunt  
7. Execute an anomaly-based hunt  

**2.3 [T] Online Tools & Enrichment**  

**2.3.1 [K] Tool capabilities for hunting**  
a. VirusTotal – strengths and limitations for hunting  
b. AnyRun – strengths and limitations for hunting  
c. URLScan – strengths and limitations for hunting  
d. Silent Push – strengths and limitations for hunting  

**2.3.2 [T] Online tools & enrichment tasks**  
1. Perform advanced querying and pivoting in VirusTotal, AnyRun, URLScan, and Silent Push  
2. Extract actionable hunting leads from external tool results  
3. Convert external findings into precise internal SIEM or Zeek queries  

**2.4 [K/T] CTI for Hunters**  

**2.4.1 [K] Assessing CTI for hunting value**  
a. Hunt-worthy vs awareness-only vs hand off to detections / IR  
b. Rapid triage of a report  
c. What “actionable for a hunt” means (question, telemetry, scope)  

**2.4.1.1 [T] Tasks**  
1. Triage a CTI report: hunt / don’t hunt / hand off, and say why  

**2.4.2 [K] Extracting hunt leads from CTI**  
a. TTPs vs IOCs vs behaviors — which can drive a hunt  
b. What to drop (no telemetry, expired IOCs, noise)  
c. Record ATT&CK IDs if the report has them (mapping hunts is 2.5)  

**2.4.2.1 [T] Tasks**  
1. Extract hunt-suitable TTPs from a CTI report  
2. Extract hunt-suitable artifacts (IOCs, patterns, behaviors)  
3. State the hunt question those leads support  

**2.4.3 [K] STIX as hunt input**  
a. Objects a hunter actually uses (indicator, attack-pattern, observed-data, malware, threat-actor / intrusion-set, relationship)  
b. How a STIX bundle seeds a hunt (not how to author STIX)  

**2.4.3.1 [T] Tasks**  
1. Identify hunt-relevant objects in a report or bundle  
2. Turn those objects into hunt leads  

**2.5 [K/T] Framework Application for Hunting**  

**2.5.1 [K] Using MITRE ATT&CK for hunt planning and coverage analysis**  
a. Mapping hunts to ATT&CK tactics and techniques  
b. Using ATT&CK to identify coverage gaps  
c. Using ATT&CK to prioritize hunt topics  

**2.5.2 [T] Framework application tasks**  
1. Map a hunt plan or hunt findings to MITRE ATT&CK  
2. Use ATT&CK to identify detection or visibility gaps  
3. Use ATT&CK to support hunt prioritization  

**2.6 [K/T] Attacker Techniques**  

**2.6.1 [K] Persistence techniques**  
a. Registry-based persistence  
b. Start menu / startup folder persistence  
c. Scheduled tasks  
d. Other common persistence methods  

**2.6.2 [K] Privilege escalation techniques**  
a. Common Windows privilege escalation methods  
b. Indicators associated with privilege escalation  

**2.6.3 [T] Attacker technique tasks**  
1. Recognize persistence techniques in logs or telemetry  
2. Recognize privilege escalation techniques in logs or telemetry  
3. Hunt for specific persistence or privilege escalation techniques  

**2.7 [T] Site-Specific Hunt Knowledge and Tasks**  

**2.7.1 [K] Hunt control and lead management**  
a. How hunts are initiated and controlled  
b. Lead management process  

**2.7.2 [K] Hunt documentation standards**  
a. Required elements of hunt documentation  
b. Where and how hunts are documented  

**2.7.3 [K] Hunt outputs and hand-off**  
a. Expected outputs of a hunt  
b. Hand-off process to SOC, IR, or CTI  

**2.7.4 [T] Site-specific hunt tasks**  
1. Follow the local process for initiating and controlling a hunt  
2. Document a hunt according to local standards  
3. Produce required hunt outputs and perform proper hand-off  

---

# 3. CTI Analyst

**3.1 [K] Core Intelligence Concepts**  
**3.1.1 [K] Difference between data, information, and intelligence**  
a. Definitions and distinctions  
b. How raw data becomes information and then intelligence  

**3.1.1.1 [T] Tasks**  
1. Correctly categorize examples as data, information, or intelligence  

**3.1.2 [K] Intelligence lifecycle**  
a. Stages of the intelligence lifecycle  
b. Purpose and activities in each stage  

**3.1.2.1 [T] Tasks**  
1. Identify which stage of the intelligence lifecycle a given activity belongs to  
2. Describe the flow of the intelligence lifecycle  

**3.1.3 [K] Intelligence types**  
a. Strategic  
b. Operational  
c. Tactical  
d. Technical  

**3.1.3.1 [T] Tasks**  
1. Correctly classify an intelligence product or requirement by type  

**3.1.4 [K] Intelligence requirements**  
a. Purpose of intelligence requirements  
b. Types of requirements (e.g., Priority Intelligence Requirements)  
c. How requirements drive collection and analysis  

**3.1.4.1 [T] Tasks**  
1. Identify or draft (develop or refine) a basic intelligence requirement  
2. Translate stakeholder questions into clear intelligence requirements  
3. Explain how a given requirement drives analytic work  

**3.1.5 [K] Ensuring intelligence is actionable**  
a. Characteristics of actionable intelligence  
b. Common reasons intelligence fails to be actionable  

**3.1.5.1 [T] Tasks**  
1. Evaluate whether a piece of intelligence is actionable and explain why  

**3.1.6 [K] Tailoring output to the audience**  
a. Importance of audience analysis  
b. Adjusting content, format, and detail level for different consumers  

**3.1.6.1 [T] Tasks**  
1. Adjust an intelligence product for a specified audience  

**3.1.7 [K] Attribution**  
a. Purpose and challenges of attribution  
b. Levels of confidence in attribution  
c. Types of attribution (e.g., activity group vs. nation-state)  

**3.1.7.1 [T] Tasks**  
1. Assess attribution statements for confidence and supporting evidence  

**3.1.8 [K] Collection sources and methods**  
a. OSINT  
b. Commercial  
c. Internal  

**3.1.8.1 [T] Tasks**  
1. Identify appropriate collection source classes for a given requirement  
2. Plan collection against an intelligence requirement  

Local request *process* (tickets, approval) is **3.12**. Tool *operation* is **3.3** / **2.3**.

**3.2 [K] Analytic Tradecraft**  
**3.2.1 [K] Estimative language**  
a. Purpose of estimative language  
b. Common estimative terms and their meaning  
c. How estimative language communicates confidence and uncertainty  

**3.2.1.1 [T] Tasks**  
1. Correctly use estimative language when writing an analytic judgment  
2. Interpret the confidence level expressed in an estimative statement  

**3.2.2 [K] Structured analytic techniques**  
a. Purpose of structured analytic techniques  
b. Common techniques (e.g., Analysis of Competing Hypotheses, Key Assumptions Check)  
c. When to apply different techniques  

**3.2.2.1 [T] Tasks**  
1. Apply a basic structured analytic technique to a given problem set  
2. Identify which structured analytic technique is most appropriate for a scenario  

**3.2.3 [K] Admiralty Code / source reliability & information credibility**  
a. Source reliability scale  
b. Information credibility scale  
c. How to combine reliability and credibility ratings  

**3.2.3.1 [T] Tasks**  
1. Assign Admiralty Code ratings to a source and a piece of information  
2. Explain the meaning of a given Admiralty Code rating  

**3.2.4 [K] Cognitive biases and mitigation**  
a. Common cognitive biases that affect analysis  
b. Impact of biases on intelligence products  
c. Techniques to mitigate cognitive biases  

**3.2.4.1 [T] Tasks**  
1. Identify potential cognitive bias in an analytic judgment  
2. Apply a mitigation technique to reduce bias in analysis  

**3.3 [T] Tools**  
**3.3.1 [K] Internal threat intelligence platform**  
a. Purpose and core functions of the internal TIP  
b. How to navigate and search the platform  
c. How the platform supports enrichment, analysis, and production  

**3.3.1.1 [T] Internal TIP tasks**  
1. Search and retrieve relevant intelligence from the internal platform  
2. Use the platform to support enrichment or analysis of an indicator or report  

**3.3.2 [K] External tools (VirusTotal, AnyRun, Silent Push, URLScan)**  
a. Primary purpose, strengths, and weaknesses of each tool  
b. When to use each tool in the intelligence process  

**3.3.2.1 [T] External tools tasks**  
1. Select the appropriate external tool for a given enrichment or analysis need  
2. Perform advanced enrichment and pivoting using external tools  

**3.4 [K/T] File Similarity & Hashing Techniques**  
**3.4.1 [K] Hashing and similarity concepts**  
a. imphash  
b. ssdeep  
c. TLSH  
d. Certificate / code-signing certificate information  

**3.4.1.1 [T] Tasks**  
1. Explain the purpose and use case of imphash, ssdeep, and TLSH  
2. Use file similarity hashes to identify related samples  
3. Extract and interpret certificate information from a file  

**3.5 [K/T] RDAP / WHOIS**  
**3.5.1 [K] RDAP and WHOIS concepts**  
a. Purpose of WHOIS and RDAP  
b. Key differences between WHOIS and RDAP  
c. Key fields useful for enrichment and attribution  

**3.5.1.1 [T] Tasks**  
1. Query RDAP/WHOIS for a domain or IP  
2. Extract and interpret relevant fields for enrichment or attribution  

**3.6 [K/T] Advanced DNS**  
**3.6.1 [K] Advanced DNS concepts**  
a. SOA records  
b. Other advanced DNS record types and their intelligence value  
c. How advanced DNS data supports enrichment and infrastructure analysis  

**3.6.1.1 [T] Tasks**  
1. Interpret an SOA record  
2. Use advanced DNS records to support enrichment or pivoting  

**3.7 [K/T] Frameworks**  
**3.7.1 [K] MITRE ATT&CK**  
a. Advanced application for intelligence analysis and TTP extraction  

**3.7.1.1 [T] Tasks**  
1. Map activity or reports to MITRE ATT&CK (tactic, technique or sub-technique, evidence; reject the neighbor ID)  

**3.7.2 [K] Diamond Model**  
a. Advanced application for analysis and attribution  

**3.7.2.1 [T] Tasks**  
1. Apply the Diamond Model to an intelligence problem (fill vertices from a report or activity set; name the weakest; reject a vendor-name Adversary fill)  

**3.7.3 [K] Cyber Kill Chain**  
a. Advanced application for understanding attack progression  

**3.7.3.1 [T] Tasks**  
1. Identify the Kill Chain stage of observed or reported activity (stage, reject previous/next; list only supported stages in the product; reject an unobserved stage)  

**3.7.4 [K] MalasadaTech Defender’s ThreatMesh Framework (DTF)**  
a. Purpose of DTF (pattern identification and defensive prioritization)  
b. Core components and scoring methodology  
c. How DTF is used to identify patterns across indicators, infrastructure, and adversary behavior  
d. How DTF scoring and pattern analysis feed enrichment and pivoting decisions  
e. Relationship of DTF to other frameworks (ATT&CK, Diamond Model, Cyber Kill Chain)  

**3.7.4.1 [T] Tasks**  
1. Apply DTF to identify patterns and score or prioritize indicators or infrastructure  

**3.7.4.2 [T] Tasks**  
1. Use DTF pattern analysis to guide enrichment and pivoting  

**3.7.4.3 [T] Tasks**  
1. Explain how DTF integrates with or complements ATT&CK, Diamond, and Kill Chain  

**3.7.5 [T] Framework application tasks**  
1. Apply MITRE ATT&CK, Diamond Model, and/or Cyber Kill Chain at an advanced level to an intelligence problem set  
2. Apply DTF to identify patterns and score/prioritize indicators or infrastructure  
3. Use DTF pattern analysis to guide enrichment and pivoting  
4. Explain how DTF integrates with or complements other frameworks  

**3.8 [T] Enrichment & Analysis**  
**3.8.1 [K] Identifying additional adversary infrastructure from seed indicators**  
a. Pivoting concepts and techniques  
b. Common data sources used for infrastructure enrichment  

**3.8.1.1 [T] Tasks**  
1. Pivot from a seed indicator to identify additional adversary infrastructure  

**3.8.2 [K] Extracting applicable TTPs from intelligence reports**  
a. How to identify relevant TTPs in a report  
b. Criteria for determining which TTPs are applicable to the environment  

**3.8.2.1 [T] Tasks**  
1. Extract applicable TTPs from an intelligence report  

**3.9 [T] Platform-Specific Skills**  

**3.9.1 [T] VirusTotal**  
a. Relations tab for infrastructure pivoting  
b. Behavior tab for extracting file, network, registry, and process events  

**3.9.1.1 [T] VirusTotal tasks**  
1. Use the Relations tab to identify additional adversary infrastructure from a seed indicator  
2. Use the Behavior tab to extract file, network, registry, and process events  

**3.9.2 [T] AnyRun**  
a. Searching submissions by tag, IP, domain, or hash  
b. Reviewing submissions for actionable intelligence  

**3.9.2.1 [T] AnyRun tasks**  
1. Search AnyRun submissions by tag, IP, domain, or hash  
2. Review an AnyRun submission and extract actionable intelligence  

**3.9.3 [T] Silent Push**  
a. Core capabilities and primary use cases  
b. How to pivot and enrich indicators  

**3.9.3.1 [T] Silent Push tasks**  
1. Enrich an indicator using Silent Push  
2. Pivot within Silent Push to identify additional infrastructure  

**3.9.4 [T] URLScan**  
a. Core capabilities and primary use cases  
b. How to interpret scan results for intelligence value  

**3.9.4.1 [T] URLScan tasks**  
1. Submit or retrieve a URLScan result  
2. Extract actionable intelligence from a URLScan report  

**3.10 [K] Common STIX Objects**  
**3.10.1 [K] Core STIX Objects**  
a. Indicator  
b. Observed Data  
c. Malware  
d. Attack Pattern  
e. Threat Actor  
f. Intrusion Set  
g. Campaign  
h. Course of Action  
i. Identity  
j. Relationship  
k. Sighting  

**3.10.2 [K] How STIX objects are used in intelligence production**  
a. Structuring intelligence for sharing and automation  
b. Linking objects to represent complex threat activity  

**3.10.3 [T] STIX tasks**  
1. Correctly identify and label common STIX objects in an intelligence report  
2. Create basic STIX-aligned relationships between objects  
3. Explain how a set of STIX objects represents a threat scenario  

**3.11 [T] Intelligence Production & Dissemination**  
**3.11.1 [K] Creating finished intelligence products**  
a. Types of finished intelligence products  
b. Structure and required elements of a finished product  
c. Quality and analytic standards  

**3.11.1.1 [T] Tasks**  
1. Draft a basic finished intelligence product  
2. Evaluate a finished product against quality and analytic standards  

**3.11.2 [K] Disseminating intelligence to the correct audiences**  
a. Audience identification  
b. Approved dissemination methods and channels  
c. Handling caveats and handling markings  

**3.11.2.1 [T] Tasks**  
1. Select the appropriate audience and dissemination method for a product  
2. Apply correct handling markings and caveats  

**3.11.3 [K] Handling RFIs**  
a. Purpose and lifecycle of an RFI  
b. How to evaluate, prioritize, and respond to an RFI  

**3.11.3.1 [T] Tasks**  
1. Evaluate and prioritize an RFI  
2. Produce a response to an RFI  

**3.12 [T] Site-Specific CTI Knowledge and Tasks**  
**3.12.1 [K] Local intelligence requirements and priorities**  
a. Current Priority Intelligence Requirements (PIRs) / intelligence priorities  
b. How local requirements drive analytic focus  

**3.12.1.1 [T] Tasks**  
1. Identify current local intelligence priorities  
2. Align analytic work to a stated local requirement  

**3.12.2 [K] Local production and approval processes**  
a. Workflow for producing intelligence products  
b. Required reviews and approval authorities  

**3.12.2.1 [T] Tasks**  
1. Follow the local production and approval process for an intelligence product  

**3.12.3 [K] Local dissemination channels and customers**  
a. Primary internal and external customers  
b. Approved dissemination channels and methods  

**3.12.3.1 [T] Tasks**  
1. Disseminate a product using the correct local channels and customers  
