# Training Outlines – SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer

**Manning & Qualification Rules**
- 1-level: Never authorized to work on shift
- 3-level: Must never work alone; must be supervised/trained by at least a 7-level
- 5-level: May work a shift alone
- 7-level: Qualified to supervise and train 3-levels

These rules apply across SOC Analyst, Threat Hunter, CTI Analyst, and Detection Engineer roles.

**Stay in this lesson:** a short note under a unit or child says what this hour is *not*. It is not extra syllabus. Follow it when writing or revising the lesson. How to write the lesson is [generate-module.md](../generate-module.md).

**Teach order:** `0` (includes `0.6`–`0.8`) → SOC `1` → **CTI `2`** → hunt `3` → DE `4`. This file is in that order. Folders: `02-cti`, `03-hunter`.

---

# 0. Front door

Everyone (SOC, Hunter, CTI, DE). Lessons live under `modules/00-intro/`. This whole section is taught **before SOC 1.1**. One possible way work moves. Not “the” way every shop runs. No DYA ticket names, PIR lists, or approval chains.

Write only the asked child unless asked for the whole intro. Frameworks are **`0.6`**. Tool survey is **`0.7`**. Environment / signal flow is **`0.8`**. Retired from this block: `1.7`, `1.8.3`, `1.8.4`, `1.8.5` (and `1.8.2`). The companion story at the end is this outline again, as one incident.

**0.1 [K] How this course is laid out**  
Stay in this lesson: the map of the course. Not what a SOC is (`0.2`). Not the jobs (`0.3`). Not the hand-off (`0.4.1`).

a. Front door, then shared hours that apply to every role, then four tracks: SOC analyst, CTI, hunting, detection engineers  
b. Inside SOC, detections *are* before the alert queue. SOC ends at reporting (`1.5`). The RFI is the door into CTI  
c. After this intro and still before SOC: frameworks, tool survey, and environment / signal flow. Those apply to everyone. Role-local hunt / CTI / DE lists come later and differ by shop  
d. This course uses one company and one adversary as fiction. Those names come in the next hour. After the lessons, a companion story retells the same flow as one incident  

**0.2 [K] What a SOC is**  
a. A place that watches for bad or suspicious activity and starts the response  
b. It is a team sport: more than one job sits in or next to the SOC  
c. This course uses one company (DYA) and one adversary (PRD). Those are fiction, not your site’s policy  

**0.3 [K] Jobs in one sentence**  
a. **SOC analyst** — work the alert in front of you; start the hand-offs  
b. **Incident response** — contain and recover (this course points at them; it does not train IR)  
c. **CTI analyst** — answer the RFI; add context; find more of the adversary  
d. **Threat hunter** — look for more activity the alerts missed, from a hunt package or a hypothesis  
e. **Detection engineer** — turn what we learned into lasting rules  
f. **Firewall / IA** — block what intel names (a hand-off, not a track in this course)  

**0.4 [K] How work can move**  
a. An analyst gets an alert and triages it  
b. They send it to incident response and notify leadership  
c. They ask intel for more work on that alert (an RFI)  
d. Intel works the RFI, enriches it, and may find more adversary infrastructure  
e. Extra infrastructure can go to whoever blocks (firewall / IA)  
f. Intel can also hand hunters a hunt package  
g. That same package can go to detection engineers to write or tune rules (MDE, YARA, Suricata, SIGMA, and so on)  

**0.4.1 [T] Tasks**  
1. Given a step in the flow, name the next hand-off and whose product it is (not how your site files the ticket)

**0.5 [K] Where the jobs lightly overlap**  
a. Everyone may look at the same host, log, or domain  
b. The *product* is different: close/escalate an alert vs an intel note vs a hunt vs a rule  
c. Asking the next desk is not doing that desk’s whole job  
d. A smaller shop may have one person fill more than one of these jobs. This outline still names the jobs separately so each *product* stays clear, even if the same person writes two of them.  

**0.6 [K/T] Frameworks**  
Taught after `0.5`, still before SOC. All four roles. Lessons live under `modules/00-intro/06-frameworks/`. Do not copy them into a role folder. Write only the asked child. Hunt *planning* is **3.5**. CTI depth is **2.7**. Actor products are **2.11**. DTF is **2.7.4**. This hour is a one-line activity, not an alert pane (**1.4**).

**0.6.1.1 [K] MITRE ATT&CK**  
Stay in this lesson: purpose, structure, and one map with a cited field. Not hunt planning (**3.5**). Not **2.7.1**. Not Diamond (**0.6.2**). Not Kill Chain (**0.6.3**).

a. Purpose: a shared language for adversary **behavior** (label what you saw)  
b. Structure: Enterprise matrix — tactics as columns, techniques and sub-techniques as cells  
c. Tactic = *why* (the goal). Technique / sub-technique = *how* (named way, e.g. `T1059` / `T1059.001`)  
d. How to map: read the row; name tactic + technique or sub-technique; cite one field; if two IDs fit, pick the primary and reject the neighbor. An ID with no cited field is not a map  

**0.6.1.2 [T] ATT&CK tasks**  
1. Map observed activity to an ATT&CK tactic and technique (or sub-technique) and cite the evidence  

**0.6.2.1 [K] Diamond Model**  
Stay in this lesson: four vertices and the weakest one. Not attribution (**2.11**). Not **2.7.2**. Not ATT&CK IDs (**0.6.1**).

a. Purpose: organize what you know so you can see what you do **not** know. Not a verdict  
b. The four vertices: Adversary, Capability, Infrastructure, Victim  
c. Fill all four from evidence you have. Name the **weakest** vertex (least evidence) — that is the next question, not a guess. A vendor or course-fiction name is not Adversary evidence  

**0.6.2.2 [T] Diamond Model tasks**  
1. Apply the Diamond Model to an incident or set of indicators: fill the four vertices and state which vertex is weakest  

**0.6.3.1 [K] Cyber Kill Chain**  
Stay in this lesson: this row’s stage, and why it is not the previous or next. Not ATT&CK (**0.6.1**). Not Diamond (**0.6.2**). Not **2.7.3**.

a. Purpose: stage attack **progression**. A staging tool, not a complete model of every intrusion  
b. The seven stages, in order: Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Actions on Objectives  
c. Place **this row** on one stage. Reject the previous or next stage you did not see. Do not invent the rest of the chain  

**0.6.3.2 [T] Kill Chain tasks**  
1. Identify the Kill Chain stage of observed activity and why it is not the previous or next stage  

**0.7 [K] External tools (VirusTotal, AnyRun, Silent Push, URLScan)**  
Taught after `0.6`, still before SOC. All four roles. Lessons live under `modules/00-intro/07-tool-survey/`. Stay in this lesson: purpose, strengths, weaknesses, and when to pick. Do not teach TIP nav (`2.3.1`) or platform depth (`2.9`). Not a live vendor account.

a. Primary purpose, strengths, and weaknesses of each tool  
b. When to use each tool  

**0.7.1 [T] External tools tasks**  
1. Select the appropriate external tool for a given enrichment or analysis need  

**0.8 [K] Environment / signal flow**  
Taught after `0.7`, still before SOC. All four roles. Lessons live under `modules/00-intro/08-environment/`. Stay in this lesson: why every role must know the site’s infrastructure and how signal flows, and how to tell two *kinds* of fact apart. These are questions you take to **your shop**. Do **not** invent a site card, spans, ticket names, or DYA / Harbor architecture. Not Zeek field reading (`1.2`). Not host-observed network (`1.1.4`). **Retired:** `1.7`, `1.8.2`, `1.8.3`, `1.8.4`, `1.8.5`.

a. Path to the internet / network egress points  
b. Key network segments and data flow  
c. Email flow and related systems  
d. Edge firewall architecture and key choke points  
e. Trusted third-party access / federation  
f. Crown jewel / critical assets  
g. PCAP collection points / sensors  

**0.8.1 [T] Environment / signal flow tasks**  
1. Identify which kind of fact applies to a given situation and why it is not the adjacent kind  

---

# 1. SOC Analyst Fundamentals

After the full `00` block (`0.1`–`0.8`). This section is **1.1** → **1.2** → **1.3** → **1.4** → **1.5**. **SOC ends at 1.5 reporting.** The RFI is the door into CTI. Next section in this file is **3. CTI** (not 2. Hunt).

**1.1 [K/T] Endpoint Logs**

Endpoint telemetry (Sysmon / MDE) vs network-sensor telemetry (Zeek, unit 1.2). Sysmon Event IDs and MDE tables encode the same activities; this unit is not Sysmon installation or configuration. One map hour, then five activity units. Write only the asked child. `1.1.4` is **host-observed** network (initiating process → IP/port/domain). Protocol deep-dive is `1.2`. Do not merge the two.

**1.1.1 [K] Endpoint activity (the map)**  
Stay in this lesson: name the five kinds of host rows. Do not teach process fields, Sysmon install, or Zeek (**1.2**). One activity type per later child.

a. A host leaves **rows** when something happens on it — a program runs, a file changes, a registry key is written, the host talks, or an image/driver loads  
b. **Sysmon** and **MDE** are two encodings of those same activities, not two different stories. This course uses both as examples  
c. You will learn **one activity type at a time**. This hour is only the map  
d. This is **endpoint** telemetry. Protocol deep-dive is Zeek (**1.2**)  
e. An alert will point at a host. You need to know **which kind of row** you are looking at before you describe it  

**1.1.1.1 [T] Tasks**  
1. Given a one-line description, name the activity type: process, file, registry, host-network, or image/driver load  

**1.1.2 [K] Process activity**  
a. Process create / terminate  
b. PID, name, command line  
c. Parent-child (PPID, parent name, parent command line)  
d. Integrity / user context (where logged)  
e. Hashes and original filename (where logged)  
f. Process access (Sysmon Event ID 10) as “who touched whom,” not a separate unit  
g. How this shows up: Sysmon 1 / 5 / 10; MDE `DeviceProcessEvents` (key fields: `ActionType` — `ProcessCreated`, `OpenProcess`; `InitiatingProcess*`, `ProcessCommandLine`, SHA256). The full `ActionType` list is in the Defender portal schema — do not invent values.  

**1.1.2.1 [T] Process activity tasks**  
1. Analyze a process event (Sysmon or MDE) and accurately describe what occurred  
2. Create a SIEM query to detect specific process activity  

**1.1.3 [K] File system activity**  
a. Create / rename-move / delete / modify / read (where logged)  
b. Path, name, extension  
c. Hashes  
d. Initiating process  
e. How this shows up: Sysmon 11 / 23 / 26; MDE `DeviceFileEvents` (`ActionType`, `FolderPath`, `FileName`, SHA256, `InitiatingProcess*`)  

**1.1.3.1 [T] File system activity tasks**  
1. Analyze a file event (Sysmon or MDE) and accurately describe what occurred  
2. Create a SIEM query to detect specific file operations  

**1.1.4 [K] Network activity (endpoint)**  
a. Source / dest IP and port, protocol, direction  
b. Domain / URL when the endpoint logged them  
c. Initiating process (this is the point of 1.1 vs Zeek)  
d. How this shows up: Sysmon 3 (and 22 if DNS is logged here); MDE `DeviceNetworkEvents`  
e. This is host-observed activity. Protocol deep-dive is 1.2  

**1.1.4.1 [T] Network activity tasks**  
1. Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred  
2. Create a SIEM query to detect specific endpoint network activity  

**1.1.5 [K] Registry activity**  
a. Hives and key → value  
b. Set / delete / rename  
c. Common persistence locations (Run, Services) as examples, not a 3.6 dump  
d. Initiating process  
e. How this shows up: Sysmon 12 / 13 / 14; MDE `DeviceRegistryEvents`  

**1.1.5.1 [T] Registry activity tasks**  
1. Analyze a registry event (Sysmon or MDE) and accurately describe what occurred  
2. Create a SIEM query to detect specific registry operations  

**1.1.6 [K] Image and driver load activity**  
a. User-mode image load vs kernel driver load  
b. Path, hashes, signed vs unsigned (where logged)  
c. Initiating process  
d. How this shows up: Sysmon 6 / 7; MDE `DeviceImageLoadEvents`  

**1.1.6.1 [T] Image and driver load tasks**  
1. Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred  
2. Create a SIEM query to detect specific image or driver load activity  

**1.2 [K/T] Zeek and Zeek Engines**

Network-sensor telemetry. Host-observed process/file/network/registry/image activity is 1.1. Stay in this lesson: this is not a PCAP analysis course. PCAP is mentioned on **1.2.1** (why you pull it). Applying PCAP against an alert is **1.4.1**. Where sensors sit is **0.8.g**. Download / view is **1.8.3** if the shop lists them.

**1.2.1 [K] Zeek concepts**  
Stay in this lesson: what Zeek is, how engines extract, and that PCAP is the usual next artifact. Not Wireshark. Not site download path. Not **1.4.1**.

a. Zeek as a network analysis framework  
b. How Zeek uses engines (scripts/analyzers) to classify and extract protocol data  
c. How engines surface relevant applications and protocols  
d. PCAP is normally pulled to verify a Zeek log or to expand / provide context the log does not carry  

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

Rule *syntax* and a first read/write. How detections are run as a service is **4.x**. Write only the asked child (SIGMA, Suricata, YARA, or SIEM).

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

Alert handling. Detection *authoring* is 1.3. Five units: investigate (`1.4.1`), classify (`1.4.2`), FP causes (`1.4.3`), categorize (`1.4.4`), SLA clocks (`1.4.5`). Do not collapse FP causes into classification. Do not write the next `1.4` child when asked for one. Each knowledge item has its own tasks; tasks apply the knowledge, they do not restate it. **1.4.1.e** applies PCAP against the alert. Why you pull PCAP is **1.2.1**. Sensors are **0.8.g**. Download / view is **1.8.3** if the shop lists them.

**1.4.1 [K] Alert context and investigation**  
Stay in this lesson: gather context, including VirusTotal on a hash, IP, or domain you already have (**0.7**). Not platform depth / Relations (**2.9**). Not a live-account lab.

a. Viewing the context provided by the alert, and looking up a hash, IP, or domain you have on VirusTotal  
b. Reviewing the alert configuration  
c. Understanding upstream alerting (e.g., Suricata rule → SIEM correlation search → SIEM alert)  
d. Pulling related endpoint logs that led up to the event  
e. Pulling and reviewing PCAP for the network traffic that triggered the alert  

**1.4.1.1 [T] Alert investigation tasks**  
1. Review an alert and identify which context is present and which is missing (include VirusTotal on a hash, IP, or domain you have)  
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

**1.5 [K/T] Reporting**

Last SOC hour. Sits at the **SOC / CTI seam** after alerts (`1.4`). Three units — do not collapse them. The RFI type is the door into CTI. Finished intel products are **2.11**. Alert start/close clocks are **1.4.5**. Each knowledge item has its own applying task. **`1.7` is retired.**

**1.5.1 [K] Report types**  
a. Incident report  
b. Request for Information (RFI)  
c. Other common report types used in the environment  

**1.5.1.1 [T] Report type tasks**  
1. Identify the correct report type for a given situation and why it is not the adjacent type  

**1.5.2 [K] Reporting timeline requirements**  
a. Required timelines for submitting different report types  
b. Escalation timelines when additional information or actions are needed  

**1.5.2.1 [T] Reporting timeline tasks**  
1. Given a situation and timestamps, identify which report timeline applies (submit vs escalate-for-more-info) and whether it is at risk  

**1.5.3 [K] Notification and distribution**  
a. Notification chart / matrix (which teams or sections receive which reports)  
b. Requirement to notify leadership for awareness  
c. Approved reporting channels  

**1.5.3.1 [T] Notification and distribution tasks**  
1. Route a report: name the recipients, whether leadership gets awareness, and the approved channel (and reject the wrong channel)  

---

# 2. CTI Analyst

Taught after SOC reporting (`1.5`). Hunt is **3.x** and comes after this section.

**2.1 [K] Core Intelligence Concepts**  

Eight children (`2.1.1`–`2.1.8`). Write only the asked child unless asked for the rest of `2.1`. Collection *source classes* are `2.1.8` (not the lifecycle collection *stage* in `2.1.2`). Audience tailoring is `2.1.6`; finished production is `2.11`. Actor profile is `2.11.1.2`. Local collection *request process* is `2.12.2.1`.

**2.1.1 [K] Difference between data, information, and intelligence**  
a. Definitions and distinctions  
b. How raw data becomes information and then intelligence  

**2.1.1.1 [T] Tasks**  
1. Correctly categorize examples as data, information, or intelligence  

**2.1.2 [K] Intelligence lifecycle**  
a. Stages of the intelligence lifecycle  
b. Purpose and activities in each stage  

**2.1.2.1 [T] Tasks**  
1. Identify which stage of the intelligence lifecycle a given activity belongs to  
2. Describe the flow of the intelligence lifecycle  

**2.1.3 [K] Intelligence types**  
a. Strategic  
b. Operational  
c. Tactical  
d. Technical  

**2.1.3.1 [T] Tasks**  
1. Correctly classify an intelligence product or requirement by type  

**2.1.4 [K] Intelligence requirements**  
a. Purpose of intelligence requirements  
b. Types of requirements (e.g., Priority Intelligence Requirements)  
c. How requirements drive collection and analysis  

**2.1.4.1 [T] Tasks**  
1. Identify or draft (develop or refine) a basic intelligence requirement  
2. Translate stakeholder questions into clear intelligence requirements  
3. Explain how a given requirement drives analytic work  

**2.1.5 [K] Ensuring intelligence is actionable**  
a. Characteristics of actionable intelligence  
b. Common reasons intelligence fails to be actionable  

**2.1.5.1 [T] Tasks**  
1. Evaluate whether a piece of intelligence is actionable and explain why  

**2.1.6 [K] Tailoring output to the audience**  
a. Importance of audience analysis  
b. Adjusting content, format, and detail level for different consumers  

**2.1.6.1 [T] Tasks**  
1. Adjust an intelligence product for a specified audience  

**2.1.7 [K] Attribution**  
a. Purpose and challenges of attribution  
b. Levels of confidence in attribution  
c. Types of attribution (e.g., activity group vs. nation-state)  

**2.1.7.1 [T] Tasks**  
1. Assess attribution statements for confidence and supporting evidence  

**2.1.8 [K] Collection sources and methods**  
a. OSINT  
b. Commercial  
c. Internal  

**2.1.8.1 [T] Tasks**  
1. Identify appropriate collection source classes for a given requirement  
2. Plan collection against an intelligence requirement  

Local request *process* (tickets, approval) is **2.12**. Tool *operation* is **2.3** / **3.3**.

**2.2 [K] Analytic Tradecraft**  

Four children. Write only the asked child. Attribution *confidence* (low/medium/high) is `2.1.7`; this unit is *likelihood terms*. Source letters are `2.2.3`.

**2.2.1 [K] Estimative language**  
a. Purpose of estimative language  
b. Common estimative terms and their meaning  
c. How estimative language communicates confidence and uncertainty  

**2.2.1.1 [T] Tasks**  
1. Correctly use estimative language when writing an analytic judgment  
2. Interpret the confidence level expressed in an estimative statement  

**2.2.2 [K] Structured analytic techniques**  
a. Purpose of structured analytic techniques  
b. Common techniques (e.g., Analysis of Competing Hypotheses, Key Assumptions Check)  
c. When to apply different techniques  

**2.2.2.1 [T] Tasks**  
1. Apply a basic structured analytic technique to a given problem set  
2. Identify which structured analytic technique is most appropriate for a scenario  

**2.2.3 [K] Admiralty Code / source reliability & information credibility**  
a. Source reliability scale  
b. Information credibility scale  
c. How to combine reliability and credibility ratings  

**2.2.3.1 [T] Tasks**  
1. Assign Admiralty Code ratings to a source and a piece of information  
2. Explain the meaning of a given Admiralty Code rating  

**2.2.4 [K] Cognitive biases and mitigation**  
a. Common cognitive biases that affect analysis  
b. Impact of biases on intelligence products  
c. Techniques to mitigate cognitive biases  

**2.2.4.1 [T] Tasks**  
1. Identify potential cognitive bias in an analytic judgment  
2. Apply a mitigation technique to reduce bias in analysis  

**2.3 [T] Tools**  

The external-tool survey is **`0.7`**. Do not re-teach it here. Write only the asked child. Do not turn `2.3.1` into VirusTotal / Silent Push (`0.7`, `2.9`) or STIX authoring (`2.10`). Classroom TIP names are stand-ins. Advanced enrichment / pivot is **2.9**.

**2.3.1 [K] Internal threat intelligence platform**  
a. Purpose and core functions of the internal TIP  
b. How to navigate and search the platform  
c. How the platform supports enrichment, analysis, and production  

**2.3.1.1 [T] Internal TIP tasks**  
1. Search and retrieve relevant intelligence from the internal platform  
2. Use the platform to support enrichment or analysis of an indicator or report

**2.4 [K/T] File Similarity & Hashing Techniques**  

One teaching unit (`2.4.1`) — imphash, ssdeep, TLSH, and code-signing. Not VT Relations (`2.9`). Not cryptographic identity-only hashes (`1.2.7` MD5/SHA). Classroom match thresholds are stand-ins.

**2.4.1 [K] Hashing and similarity concepts**  
a. imphash  
b. ssdeep  
c. TLSH  
d. Certificate / code-signing certificate information  

**2.4.1.1 [T] Tasks**  
1. Explain the purpose and use case of imphash, ssdeep, and TLSH  
2. Use file similarity hashes to identify related samples  
3. Extract and interpret certificate information from a file  

**2.5 [K/T] RDAP / WHOIS**  

One teaching unit (`2.5.1`). Not SOA / advanced DNS (`2.6`). Not Silent Push PDNS (`0.7`). Redacted registrant is not “no intel” and is not nation-state attribution (`2.1.7`).

**2.5.1 [K] RDAP and WHOIS concepts**  
a. Purpose of WHOIS and RDAP  
b. Key differences between WHOIS and RDAP  
c. Key fields useful for enrichment and attribution  

**2.5.1.1 [T] Tasks**  
1. Query RDAP/WHOIS for a domain or IP  
2. Extract and interpret relevant fields for enrichment or attribution  

**2.6 [K/T] Advanced DNS**  

One teaching unit (`2.6.1`) — interpret SOA and use other records for enrichment/pivot. Do not re-teach Zeek `dns` fields or DGA (`1.2.3`). Not RDAP (`2.5`). Not Silent Push PDNS (`0.7`).

**2.6.1 [K] Advanced DNS concepts**  
a. SOA records  
b. Other advanced DNS record types and their intelligence value  
c. How advanced DNS data supports enrichment and infrastructure analysis  

**2.6.1.1 [T] Tasks**  
1. Interpret an SOA record  
2. Use advanced DNS records to support enrichment or pivoting  

**2.7 [K/T] Frameworks**  

Four children. Write only the asked child. Do not write lumped outline `2.7.5` as one module. Do not re-teach the shared-floor frameworks (`0.6`) or hunt planning (`3.5`). DTF is real PTA/P discovery IDs from [defenders-threatmesh-framework](https://github.com/MalasadaTech/defenders-threatmesh-framework). Product is the DTF ID line. No scoring. Do not invent P-codes. Do not teach every P-code. Generic hop sentence is `2.8.1`. Applicable-to-environment TTP extract is `2.8.2`. Actor profile is `2.11`.

**2.7.1 [K] MITRE ATT&CK**  
a. Advanced application for intelligence analysis and TTP extraction  

**2.7.1.1 [T] Tasks**  
1. Map activity or reports to MITRE ATT&CK (tactic, technique or sub-technique, evidence; reject the neighbor ID)  

**2.7.2 [K] Diamond Model**  
a. Advanced application for analysis and attribution  

**2.7.2.1 [T] Tasks**  
1. Apply the Diamond Model to an intelligence problem (fill vertices from a report or activity set; name the weakest; reject a vendor-name Adversary fill)  

**2.7.3 [K] Cyber Kill Chain**  
a. Advanced application for understanding attack progression  

**2.7.3.1 [T] Tasks**  
1. Identify the Kill Chain stage of observed or reported activity (stage, reject previous/next; list only supported stages in the product; reject an unobserved stage)  

**2.7.4 [K] MalasadaTech Defender’s ThreatMesh Framework (DTF)**  
a. Purpose of DTF (discover additional adversary infrastructure; communicate and record pivots)  
b. Core components: pivot tactics (PTA) and pivots (P), ATT&CK-like structure  
c. How DTF identifies related infrastructure from a known-bad seed (shared registration, domain, DNS, IP, SSL, or HTTP characteristics)  
d. How a selected DTF pivot guides the next enrichment or lookup  
e. Relationship of DTF to ATT&CK, Diamond Model, and Cyber Kill Chain (discovery vs behavior vs know/don’t-know vs progression)  

**2.7.4.1 [T] Tasks**  
1. Apply DTF: pick tactic + pivot (or sub-pivot), cite the characteristic, reject the weak neighbor  

**2.7.4.2 [T] Tasks**  
1. Use a selected DTF pivot to name the next enrichment or lookup  

**2.7.4.3 [T] Tasks**  
1. Explain how DTF integrates with or complements ATT&CK, Diamond, and Kill Chain  

**2.7.5 [T] Framework application tasks**  
1. Apply MITRE ATT&CK, Diamond Model, and/or Cyber Kill Chain at an advanced level to an intelligence problem set  
2. Apply DTF: pick tactic + pivot, cite the characteristic, reject the weak neighbor  
3. Use a selected DTF pivot to name the next enrichment or lookup  
4. Explain how DTF integrates with or complements other frameworks  

**2.8 [T] Enrichment & Analysis**  

Write only the asked child. `2.8.1` writes the generic hop sentence from a seed — not RDAP (`2.5`), SOA (`2.6`), or Silent Push tool choice (`0.7`). The DTF ID line is `2.7.4`. `2.8.2` is apply-to-this-environment, not ATT&CK mapping (`2.7.1`) and not organizational impact (`2.8.4`). `2.8.3` handles the IOC as an object (keep / expire / enrich / link). `2.8.4` is the “so what here” line. Use only real ATT&CK IDs. VT Relations depth is `2.9`. Actor profile is `2.11`.

**2.8.1 [K] Identifying additional adversary infrastructure from seed indicators**  
a. Pivoting concepts and techniques  
b. Common data sources used for infrastructure enrichment  

**2.8.1.1 [T] Tasks**  
1. Pivot from a seed indicator to identify additional adversary infrastructure  

**2.8.2 [K] Extracting applicable TTPs from intelligence reports**  
a. How to identify relevant TTPs in a report  
b. Criteria for determining which TTPs are applicable to the environment  

**2.8.2.1 [T] Tasks**  
1. Extract applicable TTPs from an intelligence report  

**2.8.3 [K] IOC handling and enrichment concepts**  
a. What an IOC is (an observable you record, enrich, or expire) versus a TTP  
b. Handling rules: keep cited current IOCs; reject stale, uncited, or shared-infrastructure noise  
c. Enrichment uses internal and external tools already taught — this hour selects and records the enrichment; it does not re-teach the tool  
d. Link analysis and campaign tracking: connect handled IOCs into one activity set or keep them apart  

**2.8.3.1 [T] Tasks**  
1. Enrich and pivot on IOCs using internal and external tools (name the tool/field and what you hope to learn)  

**2.8.3.2 [T] Tasks**  
1. Perform link analysis / campaign tracking: same activity set vs separate (cite the shared objects; reject a vendor group name with no link)  

**2.8.4 [K] Threat relevance and organizational impact**  
a. Relevance: does this finding apply to this environment (mission / assets / platform)  
b. Potential impact: what would change here if the finding is true  
c. Relevance and impact are not TTP applicability (2.8.2), not a PIR (2.1.4 / 2.12.1), and not attribution (2.1.7)  

**2.8.4.1 [T] Tasks**  
1. Assess threat relevance and potential impact to the organization  

**2.9 [K/T] Platform-Specific Skills**  

Four children. Write only the asked child unless asked for all of `2.9`. Do not re-teach the `0.7` survey (purpose / when to pick). Hunt conversion to SIEM/Zeek is `3.3.1`. Conceptual infra hop is `2.8.1`. File-similarity hashes are `2.4`. Applicable TTPs are `2.8.2`. Classroom result cards are lesson-only — do not require a live vendor account.

**2.9.1 [K] VirusTotal**  
a. Relations tab for infrastructure pivoting  
b. Behavior tab for extracting file, network, registry, and process events  

**2.9.1.1 [T] VirusTotal tasks**  
1. Use the Relations tab to identify additional adversary infrastructure from a seed indicator  
2. Use the Behavior tab to extract file, network, registry, and process events  

**2.9.2 [K] AnyRun**  
a. Searching submissions by tag, IP, domain, or hash  
b. Reviewing submissions for actionable intelligence  

**2.9.2.1 [T] AnyRun tasks**  
1. Search AnyRun submissions by tag, IP, domain, or hash  
2. Review an AnyRun submission and extract actionable intelligence  

**2.9.3 [K] Silent Push**  
a. Core capabilities and primary use cases  
b. How to pivot and enrich indicators  

**2.9.3.1 [T] Silent Push tasks**  
1. Enrich an indicator using Silent Push  
2. Pivot within Silent Push to identify additional infrastructure  

**2.9.4 [K] URLScan**  
a. Core capabilities and primary use cases  
b. How to interpret scan results for intelligence value  

**2.9.4.1 [T] URLScan tasks**  
1. Submit or retrieve a URLScan result  
2. Extract actionable intelligence from a URLScan report  

**2.10 [K] Common STIX Objects**  

Two children. Write only the asked child unless asked for all of `2.10`. Do not write lumped outline `2.10.3` as one module. Hunt-facing STIX *input* is `3.4.3`. Finished narrative products are `2.11`. TIP retrieve is `2.3.1`. Use real STIX 2.1 object and relationship types. Do not invent types. Classroom bundles/collections are lesson-only — do not stand up a TAXII server.

**2.10.1 [K] Core STIX Objects**  
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

**2.10.1.1 [T] Tasks**  
1. Correctly identify and label common STIX objects in an intelligence report  

**2.10.2 [K] How STIX objects are used in intelligence production**  
a. Structuring intelligence for sharing and automation  
b. Linking objects to represent complex threat activity  

**2.10.2.1 [T] Tasks**  
1. Create basic STIX-aligned relationships between objects  
2. Explain how a set of STIX objects represents a threat scenario  

**2.10.2.2 [T] Tasks**  
1. Create and validate STIX objects  

**2.10.2.3 [T] Tasks**  
1. Use TAXII for sharing and consumption of intelligence  

**2.10.3 [T] STIX tasks**  
1. Correctly identify and label common STIX objects in an intelligence report  
2. Create basic STIX-aligned relationships between objects  
3. Explain how a set of STIX objects represents a threat scenario  

**2.11 [K/T] Intelligence Production & Dissemination**  

Three children. Write only the asked child unless asked for all of `2.11`. Audience *rewrite* floor is `2.1.6`. Attribution *assessment* is `2.1.7`. STIX bundle/TAXII is `2.10`. SOC ticket types/routing are `1.5`. Local approval and customer lists are `2.12`. Classroom markings/channels/RFI queue are lesson-only — not live org policy.

**2.11.1 [K] Creating finished intelligence products**  
a. Types of finished intelligence products  
b. Structure and required elements of a finished product  
c. Quality and analytic standards  

**2.11.1.1 [T] Tasks**  
1. Draft a basic finished intelligence product  
2. Evaluate a finished product against quality and analytic standards  

**2.11.1.2 [T] Tasks**  
1. Produce a threat actor profile  

**2.11.2 [K] Disseminating intelligence to the correct audiences**  
a. Audience identification  
b. Approved dissemination methods and channels  
c. Handling caveats and handling markings  

**2.11.2.1 [T] Tasks**  
1. Select the appropriate audience and dissemination method for a product  
2. Apply correct handling markings and caveats  

**2.11.2.2 [T] Tasks**  
1. Tailor products to different audiences (technical, leadership, etc.)  

**2.11.2.3 [T] Tasks**  
1. Disseminate intelligence products through approved channels  

**2.11.3 [K] Handling RFIs**  
a. Purpose and lifecycle of an RFI  
b. How to evaluate, prioritize, and respond to an RFI  

**2.11.3.1 [T] Tasks**  
1. Evaluate and prioritize an RFI  
2. Produce a response to an RFI  

**2.12 [K/T] Site-Specific CTI Knowledge and Tasks**  

Write only the asked child unless asked for all of `2.12`. Do **not** invent PIRs, approval chains, archive paths, or customer lists. Every org/section has its own; a new analyst obtains them early. PIR *concept* is `2.1.4`. Collection *planning* is `2.1.8`. Finished draft is `2.11.1`. Classroom TLP/channels are `2.11.2`. Environment / signal flow is **`0.8`**. Tool access (`1.8.3`) is retired.

**2.12.1 [K] Local intelligence requirements and priorities**  
a. Current Priority Intelligence Requirements (PIRs) / intelligence priorities  
b. How local requirements drive analytic focus  

**2.12.1.1 [T] Tasks**  
1. Identify current local intelligence priorities  
2. Align analytic work to a stated local requirement  

**2.12.2 [K] Local production and approval processes**  
a. Workflow for producing intelligence products  
b. Required reviews and approval authorities  

**2.12.2.1 [T] Tasks**  
1. Follow the local process for requesting collection or producing and approving an intelligence product  

**2.12.2.2 [T] Tasks**  
1. Document and archive intelligence products according to local standards  

**2.12.3 [K] Local dissemination channels and customers**  
a. Primary internal and external customers  
b. Approved dissemination channels and methods  

**2.12.3.1 [T] Tasks**  
1. Disseminate a product using the correct local channels and customers  

---

# 3. Threat Hunter

Taught after CTI (`2.x`).

**3.1 [K] Purpose of Threat Hunting**  
a. Identify malicious or suspicious activity missed by existing security mechanisms  
b. Identify detection and visibility gaps  

**3.1.1 [T] Tasks**  
1. Explain the purpose of threat hunting in the context of the security program  
2. Identify examples of activity that existing controls might miss  

**3.2 [K/T] Hunt Methodology**  

**3.2.1 [K] Hunt types**  
a. Intel-driven hunts  
b. Hypothesis-driven hunts  
c. Reactive hunts  
d. Anomaly-based hunts  

**3.2.2 [K] Hunt development concepts**  
a. Developing a hunt hypothesis  
b. Scoping a hunt  
c. Prioritizing hunts  
d. Identifying unique patterns or behaviors for internal searches  

**3.2.3 [T] Hunt methodology tasks**  
1. Develop and document a hunt hypothesis  
2. Scope and prioritize a hunt  
3. Identify unique patterns or behaviors suitable for hunting  
4. Execute an intel-driven hunt  
5. Execute a hypothesis-driven hunt  
6. Execute a reactive hunt  
7. Execute an anomaly-based hunt  

**3.3 [T] Online Tools & Enrichment**  

**3.3.1 [K] Tool capabilities for hunting**  
a. VirusTotal – strengths and limitations for hunting  
b. AnyRun – strengths and limitations for hunting  
c. URLScan – strengths and limitations for hunting  
d. Silent Push – strengths and limitations for hunting  

**3.3.2 [T] Online tools & enrichment tasks**  
1. Perform advanced querying and pivoting in VirusTotal, AnyRun, URLScan, and Silent Push  
2. Extract actionable hunting leads from external tool results  
3. Convert external findings into precise internal SIEM or Zeek queries  

**3.4 [K/T] CTI for Hunters**  

**3.4.1 [K] Assessing CTI for hunting value**  
a. Hunt-worthy vs awareness-only vs hand off to detections / IR  
b. Rapid triage of a report  
c. What “actionable for a hunt” means (question, telemetry, scope)  

**3.4.1.1 [T] Tasks**  
1. Triage a CTI report: hunt / don’t hunt / hand off, and say why  

**3.4.2 [K] Extracting hunt leads from CTI**  
a. TTPs vs IOCs vs behaviors — which can drive a hunt  
b. What to drop (no telemetry, expired IOCs, noise)  
c. Record ATT&CK IDs if the report has them (mapping hunts is 3.5)  

**3.4.2.1 [T] Tasks**  
1. Extract hunt-suitable TTPs from a CTI report  
2. Extract hunt-suitable artifacts (IOCs, patterns, behaviors)  
3. State the hunt question those leads support  

**3.4.3 [K] STIX as hunt input**  
a. Objects a hunter actually uses (indicator, attack-pattern, observed-data, malware, threat-actor / intrusion-set, relationship)  
b. How a STIX bundle seeds a hunt (not how to author STIX)  

**3.4.3.1 [T] Tasks**  
1. Identify hunt-relevant objects in a report or bundle  
2. Turn those objects into hunt leads  

**3.5 [K/T] Framework Application for Hunting**  

**3.5.1 [K] Using MITRE ATT&CK for hunt planning and coverage analysis**  
a. Mapping hunts to ATT&CK tactics and techniques  
b. Using ATT&CK to identify coverage gaps  
c. Using ATT&CK to prioritize hunt topics  

**3.5.2 [T] Framework application tasks**  
1. Map a hunt plan or hunt findings to MITRE ATT&CK  
2. Use ATT&CK to identify detection or visibility gaps  
3. Use ATT&CK to support hunt prioritization  

**3.6 [K/T] Attacker Techniques**  

Three children. Write only the asked child. Recognition of persistence is `3.6.1`; recognition of privilege escalation is `3.6.2`. `3.6.3` is a scoped hunt for **one named** technique — not “hunt persistence.” Hunt-type execute is `3.2.1`. Hunt card format is `3.2.2`. ATT&CK remapping is `3.5`. Local hunt control is `3.7`.

**3.6.1 [K] Persistence techniques**  
a. Registry-based persistence  
b. Start menu / startup folder persistence  
c. Scheduled tasks  
d. Other common persistence methods  

**3.6.2 [K] Privilege escalation techniques**  
a. Common Windows privilege escalation methods  
b. Indicators associated with privilege escalation  

**3.6.3 [T] Attacker technique tasks**  
1. Recognize persistence techniques in logs or telemetry  
2. Recognize privilege escalation techniques in logs or telemetry  
3. Hunt for specific persistence or privilege escalation techniques  

**3.7 [T] Site-Specific Hunt Knowledge and Tasks**  

Write only the asked child unless asked for all of `3.7`. Do **not** invent local hunt tickets, templates, output lists, or hand-off charts. Every site has its own; a new hunter obtains them early. Classroom stand-ins are lesson-only — not live org policy. Hunt *development* is `3.2.2`. Hunt-for-specific is `3.6.3`. SOC tickets / IR are `1.5` / `1.8.5`.

**3.7.1 [K] Hunt control and lead management**  
a. How hunts are initiated and controlled  
b. Lead management process  

**3.7.2 [K] Hunt documentation standards**  
a. Required elements of hunt documentation  
b. Where and how hunts are documented  

**3.7.3 [K] Hunt outputs and hand-off**  
a. Expected outputs of a hunt  
b. Hand-off process to SOC, IR, or CTI  

**3.7.4 [T] Site-specific hunt tasks**  
1. Follow the local process for initiating and controlling a hunt  
2. Document a hunt according to local standards  
3. Produce required hunt outputs and perform proper hand-off  

---

# 4. Detection Engineer

Taught last: intro → shared floor → SOC → CTI → hunting → this section. Rule *syntax* and a first read/write are **1.3**. This section is how detections are run as a service. Environment / signal flow (`0.8`) was in the `00` block.

SOC, hunt, and CTI may **nominate** a detection. The nomination does not need to be perfect. DE reviews it, makes it sound, tunes it, meets shop requirements (meta fields and the like), and deploys.

Extra adversary infrastructure from intel is a **block** for firewall / IA, not a DE job. “We blocked X — do we still need a rule?” is lifecycle, not running the firewall.

Do not invent DYA meta-field lists, change boards, or deploy tickets. Those vary by site (**4.8**). Write only the asked `4.1`–`4.7` child. `4.8` is one teaching unit when asked for `4.8` or both children.

**4.1 [K] What DE owns**  
a. DE owns the set of detections: new, change, retire, deploy  
b. SOC, hunt, and CTI nominate; the draft need not be perfect  
c. **1.3** is how a rule works; this section is how we run them  
d. Firewall / IA blocks; DE does not  

**4.1.1 [T] Tasks**  
1. Given a piece of work, say whether it is DE, a nominator, **1.3**, or a block (firewall / IA)  
2. Reject treating a rough nomination as “not DE’s problem” and reject treating a block request as a DE deploy  

**4.2 [K] Making a detection sound and meeting shop requirements**  
a. Sound: fires on the intended activity; does not fire on what it must not  
b. Test before it goes live (what must fire; what must not)  
c. Shop requirements DE owns: required meta fields, naming, IDs, tags, logging — the *list* is local (**4.8**)  
d. Close the loop with the nominator (and SOC): shipped, changed, sent back, or retired  

**4.2.1 [T] Tasks**  
1. Test a draft or change: state what must fire and what must not  
2. Mark which shop requirements are met and which are still missing (do not invent the field list)  
3. Write the close-the-loop note to the nominator  

**4.3 [K] Nominations from SOC, hunt, and CTI**  
a. Who can nominate (SOC analyst, hunter, CTI analyst)  
b. A nomination can be a draft, a sketch, or “we need something on this” — it does not have to be production-ready  
c. DE review: accept for work, send back with what is missing, or reject with why  
d. The bar for the nominator is “clear enough to review,” not “ready to deploy”  
e. A nomination that is clear enough to review names the need and points at context or a reference (investigation or intel report). A drafted rule is included if the nominator has one — it is not required.  

**4.3.1 [T] Tasks**  
1. Review a nomination and accept it for work, send it back, or reject it — and say why  
2. Name what the nominator still owes vs what DE will finish  

**4.4 [K] Tune requests from SOC**  

Same desk as nominations, different inbox. “Missing context” in **a** is about the *rule*, not the pointer in **d**. Not investigation, a block, or IR containment. Not a new nomination (**4.3**).

a. Requests on *live* rules (noisy, brittle, missing context)  
b. Same desk as nominations; different inbox  
c. Possible answers: tune the logic, add an exception, replace the rule, leave it, or retire it  
d. A tune request that is clear enough to review names which live rule and points at context or a reference (investigation or intel report). Do not invent a DYA form.  

**4.4.1 [T] Tasks**  
1. Given a SOC tune request, pick tune / exception / replace / leave / retire and cite why  
2. Reject a request that is really an investigation, a block, or IR containment  

**4.5 [K] Hunt and intel packages**  
a. Packages from CTI and from hunters are both inputs  
b. Review for chances to add or change a detection  
c. “No new rule” is a valid product  
d. A package is not a finished detection — treat it like a nomination (**4.3**)  

**4.5.1 [T] Tasks**  
1. Review a hunt or intel package and name one add, one change, or “no new rule”  
2. Reject turning the package into a block list (that is firewall / IA)  

**4.6 [K] Detection lifecycle**  

Standing call on a live rule you already own. Not the tune *inbox* (**4.4**). A block is not automatic retire. “Sensor gone” is a reason here; how to check a dead sensor is **4.7**.

a. When to modify  
b. When to retire  
c. When to leave a rule alone  
d. Reasons: still useful, too noisy, threat gone, sensor gone, a nomination replaced it, already blocked so the rule may not be needed  

**4.6.1 [T] Tasks**  
1. Given a live rule and a reason, call modify / retire / leave and cite the reason  
2. Given “we blocked this infrastructure,” decide whether the matching rule still earns its keep  

**4.7 [K] Sensor availability and performance**  

Lighter. Sometimes DE. Not a vendor-admin or architecture course.

a. Sometimes DE watches whether sensors are up and seeing the right place (MDE, Zeek, IDS)  
b. A dead or blind sensor is not “no threat”  
c. This is not a vendor admin or architecture course  

**4.7.1 [T] Tasks**  
1. Given a “the rule never fired” report, say whether you would check the rule, the sensor, or both  
2. Reject treating a down sensor as proof the activity did not happen  

**4.8 [K/T] Site-specific DE knowledge**  

One teaching unit when asked for `4.8` or both children. Local **policy** exists and varies by shop. Obtain-and-follow. Do **not** invent a field list, change board, ticket name, or DYA policy.

**4.8.1 [K] Local detection requirements**  
a. Required meta fields, naming, and other deploy checks  
b. These vary by shop; obtain the current list — do not invent one  

**4.8.1.1 [T] Tasks**  
1. Identify that you do or do not have the local requirements list  
2. Align a nomination or change only to a list you were actually shown  

**4.8.2 [K] Local review, deploy, and retire paths**  
a. How a change is reviewed and deployed  
b. How a retire is recorded  

**4.8.2.1 [T] Tasks**  
1. Follow the local path you were shown (or record that you do not have it yet)  
2. Reject inventing a change board or ticket name as policy  
