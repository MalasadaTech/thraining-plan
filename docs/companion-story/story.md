# A12 — Following the Evidence Across Four Defensive Roles

Dixon, Yamada, & Associates (**DYA**) is the fictional law firm used throughout this course. In Building C, the workstation **WS-JLEE** (`10.10.8.40`) is associated with `jlee` / `BUILDINGC\jlee`. The investigation involving that workstation is **A12**. A vendor report uses the tracking label **Pink River Dolphin (PRD)**; that name tells us how the vendor describes activity, while the identity of the actor responsible for this case remains unresolved.

You have already encountered parts of A12 in the lessons. This retelling brings them together so you can follow how an observation becomes an investigation, an intelligence question, a hunt lead, and a detection-coverage review. As you read, watch what each role receives, how it reasons from that evidence, and what the next person needs to continue. The case becomes more useful through these handoffs even when some questions remain unanswered.

Before reading closely, skim the nine stages and the closing product table. Try to predict where the evidence supports an observation, where an analyst must make an assessment, and where another source would be needed. Return to the table afterward and check whether you can explain why each product has a different purpose.

One question stays open from the beginning: **how access first occurred**. The case later shows `invoice.vbs` in a Temp path and the process activity that followed, but those observations do not identify the entry mechanism. A phishing message, malicious web path, public-facing exploit, valid-account session, or trusted-third-party path would require its own supporting evidence. Treat those as hypotheses unless the case supplies that evidence.

## 1. Start with the process event behind the alert

The first record in the SOC queue is a SIEM alert for `wscript.exe` launching `powershell.exe -enc ...` on **WS-JLEE** as `jlee`. The rule has matched a process pattern involving an encoded-command argument. An analyst can verify that pattern from the recorded fields and explain why the rule selected the event.

Understanding the match is the beginning of the investigation. The encoded argument alone leaves the command's behavior and authorization unresolved. Several other useful details, including a related destination, URI, and file hash, are absent from the initial alert. Their absence tells the analyst what additional evidence to seek before drawing a broader conclusion about the activity.

The analyst records the host, account, time, rule identity, parent process, and child command line, then traces how the alert was produced. In this example, endpoint telemetry reaches an ingested table, the SIEM rule evaluates the event, and the SIEM creates the alert. Tracing that path makes it possible to connect the alert to the actual logic and data that produced it. A Suricata stage would belong in a different detection path only if the source records showed one.

The next collection step follows the question. At this stage the analyst needs related host records. Packet capture may become useful once a network flow and a question about that flow have been identified.

## 2. Add context while keeping the classification open

The analyst collects related endpoint records for **WS-JLEE** and the case time window. The broader case includes `wscript.exe` running `invoice.vbs` from a Temp path and launching encoded PowerShell. A file event supplies the `invoice.vbs` artifact and a hash. Endpoint network telemetry associates the PowerShell process with an outbound connection to `203.0.113.88:8080`.

Zeek adds the protocol view: an HTTP `GET` request with Host `prd-updates.net` and URI `/update.exe`. Correlating the host, time, and connection context allows the analyst to read these records together while retaining what each source actually observes.

| Source | What it contributes | Question still open |
|---|---|---|
| Process evidence | The Script Host–PowerShell chain and recorded command-line context | What was authorized, and what did the encoded command do? |
| File evidence | Temp `invoice.vbs` and its recorded hash | What does further analysis establish about the file? |
| Endpoint network evidence | A process-associated connection to `203.0.113.88:8080` | What was exchanged over that connection? |
| Zeek HTTP evidence | A request to `prd-updates.net` for `/update.exe` | Did a response transfer the file, and did the file execute? |

Retained packets, if available, could help answer a specific traffic question. The analyst would record which flow and time were examined and what the packets added. The case does not supply a packet-capture result that confirms transfer, so the request remains the established network observation.

The file hash also provides a possible enrichment starting point. An approved VirusTotal lookup would preserve the exact queried value, report reference, time, and result. For this case, the record is **lookup result not supplied**. There is no supplied service verdict to interpret as either malicious or benign, and no live lookup was performed for this publication.

A hash could also locate an existing ANY.RUN report. That retrieval can be useful without possessing a sample for a new detonation. Submitting a file for a new run is a separate workflow with its own input and handling requirements. The analyst chooses between those actions by asking which result could resolve the current uncertainty.

The combined evidence gives the analyst a reason to investigate and escalate, while the **malicious/unauthorized target-condition assessment remains unresolved**. A true-positive label would require evidence of that condition in addition to the rule match. Preserving the unresolved classification lets another analyst see both the suspicious pattern and the work still needed to assess it.

There is also no supplied alert specifically for the `/update.exe` request. This raises a **coverage question**. Establishing a false negative would require the assessed target condition, an expectation that a detector should cover it, evidence that the necessary telemetry reached that detector, and a checked alert outcome for the relevant scope and time. Those conditions have not been established here, so the case carries the question forward for review.

## 3. Give incident response and leadership the products they need

SOC opens the incident record and routes the affected host to **Sam** in Incident Response. The handoff includes the observed process chain, related file and network records, and the questions that remain open. Sam can work from those observations while further analysis continues.

The leadership update has a narrower purpose. It can explain that **WS-JLEE**, associated with `jlee`, generated a suspicious Script Host–PowerShell alert and that investigation identified Temp `invoice.vbs`. Detailed hashes, registry paths, and subsequent enrichment belong in the technical record where the receiving analysts can use them. Selecting detail by audience makes the update easier to act on without weakening the evidence retained in the case.

The course uses classroom response clocks and approved-ticket examples to teach timely routing. Actual deadlines, recipients, and approval paths come from the learner's organization. A12 demonstrates why those routes matter without assigning DYA a complete operating policy.

Escalation and analytical certainty answer different questions. The observed activity can warrant response while the team continues to establish authorization, delivery, and scope. Recording that uncertainty in the handoff helps Sam understand the basis for the referral.

## 4. Turn the network question into a bounded RFI

SOC now has enough context to ask CTI a focused question:

> **Was the update domain the host that successfully delivered the payload in A12?**

**Jordan** owns this Request for Information, or **RFI**. The existing incident supplies the scope: WS-JLEE, the update domain, `/update.exe`, and the relevant case window. The question asks CTI to distinguish an attempted retrieval from a successful delivery.

At intake, Jordan can explain why the question matters and identify the missing evidence. The HTTP request supports an attempted retrieval, while confirmation of delivery would require response, transfer, or resulting host-artifact evidence. The requester and Jordan clarify the needed-by time and any handling restrictions through the actual request process.

Because the question supports an active incident, the classroom example gives it priority over routine background reading, subject to the organization's priorities. That reasoning establishes a useful next action without inventing a universal queue rule. If analysis later raises a separate question about infrastructure control or actor identity, it can be recorded as a follow-on requirement with its own scope.

## 5. Answer the RFI with a judgment the evidence can support

Jordan evaluates the request alongside the suspicious host activity. Requesting an executable-looking resource from the associated destination during that activity supports an assessment of the domain's likely delivery role. Successful transfer and execution remain separate questions because the supplied records do not show those outcomes.

A useful response is:

> We assess that the update domain was **likely used for attempted payload delivery** in A12. WS-JLEE requested `/update.exe` from that destination during the suspicious activity, but current evidence does not establish successful transfer or execution of the file.

The answer gives the requester an assessment now and identifies what additional evidence would be needed to answer the successful-delivery question fully. “Likely” expresses the probability of the assessed role. Any confidence statement should separately explain the strength and limitations of the sources supporting that judgment.

Frameworks help Jordan make the reasoning easier to inspect. ATT&CK provides a behavioral description for the observed PowerShell execution through **T1059.001 – PowerShell**. The mapping describes the observed behavior; the authorization assessment still depends on the investigation. Mapping **T1105 – Ingress Tool Transfer** would require evidence of transfer beyond the request currently available.

The Diamond Model organizes the entities and relationships:

| Vertex | Supported A12 content |
|---|---|
| **Victim** | WS-JLEE, `jlee`, and DYA |
| **Capability** | Encoded PowerShell; `/update.exe` as the requested candidate payload name |
| **Infrastructure** | `prd-updates.net` and `203.0.113.88` |
| **Adversary** | Unresolved; PRD remains a vendor tracking label rather than an independently established actor identity |

The unfilled adversary identity helps the reader see where attribution would require further evidence. The Cyber Kill Chain offers another view, focused on progression, but assigning a stage still requires evidence of the role the activity played. A process launch or request cannot establish every later stage simply because the names suggest an attack sequence.

Jordan returns the bounded answer with its evidence and remaining collection need. That closes the communication loop for the answer available now while allowing any agreed follow-up to remain visible.

## 6. Use infrastructure overlap to generate a testable candidate

CTI can also enrich the destination already associated with A12. Registration and DNS information identify the nameserver pair `ns1.cdn-test.net` and `ns2.cdn-test.net`. The supplied SOA RNAME is `hostmaster.cdn-test.net`, which provides zone-contact context. These fields help the analyst choose further lookups; their presence alone does not identify the responsible actor.

A second name, **`login-prd.net`**, shares the uncommon nameserver pair and the observed A address `203.0.113.88` during the relevant period. The overlap is specific enough to investigate as **candidate related infrastructure**. Its value comes from the shared features, their timing, and the question they make testable.

A concise record is:

| Seed | Shared characteristics | Candidate | Next analytical step |
|---|---|---|---|
| `prd-updates.net` | Uncommon NS pair and the same observed A address during the relevant period | `login-prd.net` | Compare registration and DNS history, hosting context, and independent evidence that could strengthen or weaken the relationship |

Several objects can share a provider or service without sharing an operator. The next lookup therefore tests that alternative alongside the possible operational connection. Common control would require corroboration; an activity-set or campaign assessment would additionally need evidence of related activity. Actor attribution is a further judgment with its own evidentiary burden.

The address also sits inside **Example Cloud's `203.0.113.0/24`**. The allocation tells the analyst about the hosting range, but one case address gives too little specificity to treat all neighboring addresses as A12 infrastructure. The range is **rejected as too broad for promotion**. Expiration would describe a different lifecycle situation in which a previously valid indicator had lost its usefulness.

The result of this enrichment is a documented candidate and a next question. The record retains both the observed overlap and the limits of the relationship claim so later analysis can revise it without losing its history.

## 7. Let the protective-control owner evaluate the candidate

The candidate may be relevant to a protective-control decision because the organization is investigating activity involving related infrastructure. CTI packages the object, shared characteristics, relevant observation period, and uncertainty for the function responsible for those controls. Depending on the organization, that may be a firewall team or an Information Assurance function.

The receiving owner applies local thresholds and considers the consequences of blocking, monitoring, or taking no action. CTI's contribution is the assessment and its basis; the control owner's contribution is the authorized operational decision. Keeping both visible prevents the candidate from quietly becoming a confirmed malicious destination as it moves through a ticket.

The canonical case leaves the final control action unspecified. Sam continues to own the host response, and Jordan's intelligence record remains available to support the decision. The same evidence can later inform detection work without turning a control request into a completed detection change.

## 8. Build a hunt around the observed registry configuration

Threat Hunting uses the case to ask whether related behavior or artifacts appear elsewhere in the environment. At this stage, the course brings forward registry evidence that was not required to explain the initial process alert: PowerShell set the current-user Run value **`Updater`** to **`%TEMP%\update.exe`**.

That observation establishes a configured persistence mechanism. The target file's existence, its successful launch, and persistence taking effect remain unresolved. This distinction gives the hunter a concrete search lead while keeping the result of that configuration open.

A bounded hypothesis could be:

> If related A12 persistence configurations exist on other user workstations, we expect to find the `Updater` Run value pointing to `%TEMP%\update.exe`, or related case artifacts, within the selected time window.

The hunter begins with the observed value and target path, then may broaden deliberately to relevant variants. Registry and file telemetry determine what the search can test. `invoice.vbs` and the domain/address/request pattern provide additional case leads, with matches evaluated in their own context. A filename or registry-value hit is a candidate for investigation before it becomes a finding of another affected host.

ATT&CK's **T1547.001 – Registry Run Keys / Startup Folder** helps describe the technique associated with the configuration. The practical hunt still needs a defined population, time window, evidence sources, and reviewable results. Those details make it possible for another hunter to repeat the work and understand the limits of a negative result.

The package records the question, scope, look-fors, telemetry, findings if established, and visibility or coverage questions. Any new evidence of affected hosts would go to the incident-response process. A12 leaves the hunt's host count and search results unspecified, so the handoff preserves the question and available evidence without implying that an outbreak has been found.

## 9. Give Detection Engineering a need and an evidence pointer

The case and hunt package provide **a need and an evidence pointer** for Detection Engineering: assess whether current coverage adequately addresses the relevant behavior, using the documented process, registry, and network observations. A completed production rule is not required from the nominator; DE first evaluates the coverage question.

The engineer checks whether an existing analytic can be reused, whether the necessary telemetry reaches the detection system, and whether the requested behavior falls within the intended coverage. This review can distinguish a gap in analytic logic from a collection or visibility problem. It can also show that the current coverage is already adequate.

| Possible review result | Reasoning that would support it |
|---|---|
| **Reuse or no new rule** | Existing coverage already addresses the need adequately. |
| **Change** | An existing analytic needs a supported improvement. |
| **Add** | The behavior warrants detection and available telemetry can support coverage that is currently missing. |
| **Data or visibility gap** | The needed evidence is absent, incomplete, or not reaching the detection system. |
| **Route to another owner** | The requested outcome concerns blocking, containment, or another function. |

The unalerted request remains a question within that review, rather than a pre-established false negative. If the review later establishes the required target condition, coverage expectation, telemetry, and failed alert outcome, the classification can be updated with that basis.

The case ends with the package available for this coverage review. It supplies no completed review outcome, deployed analytic, validation result, eradication, or final incident resolution. Keeping that endpoint explicit allows the later engineering lessons to explore possible follow-through without presenting their practice conditions as events that happened in A12.

## What you should be able to explain afterward

The same observations support several products because the roles need to answer different questions. Each handoff should preserve the evidence and reasoning while making the next decision clear.

| Role | Question carried forward | Product at this point in A12 |
|---|---|---|
| **SOC** | What happened, what remains uncertain, and who needs the case? | Investigation record, incident route, concise leadership update, and RFI |
| **CTI** | What role did the destination likely play, and what relationship is worth testing? | Attempted-delivery assessment, explicit transfer/execution gap, and candidate infrastructure record |
| **Threat Hunting** | Where else could the supported behavior or artifacts appear within a bounded scope? | Search hypothesis and package retaining its evidence, scope, and unresolved results |
| **Detection Engineering** | Is a coverage change justified, and can the available data support it? | Need and evidence pointer for coverage/visibility review; outcome still open |
| **Incident Response** | What host-response work is required? | Continued ownership of the affected host by Sam |
| **Protective-control owner** | Does the candidate justify an action under local policy? | Evidence for a control review; action still open |

By this point, you should be able to trace the observations through those products, explain why the RFI answer stops at attempted delivery, and distinguish a useful hunt or infrastructure lead from a confirmed finding. You should also be able to name the additional evidence needed for a TP, an FN, successful transfer, or a stronger infrastructure relationship.

The course principle applies throughout: **Describe what the evidence shows first. Then decide what it means.** A clear account of what remains uncertain gives the next analyst a reliable place to continue.

## Related course reading

- [Alert context and investigation — 1.4.1](../../modules/01-soc/04-alerts/01-context-investigation/student-guide.md) and [classification — 1.4.2](../../modules/01-soc/04-alerts/02-classification/student-guide.md).
- [RFI intake — 2.1.5](../../modules/02-cti/01-core-intel/05-rfi-intake/student-guide.md) and [response and closure — 2.7.4](../../modules/02-cti/07-production/04-rfi-response/student-guide.md).
- [Analytical frameworks — 2.3](../../modules/02-cti/03-frameworks/intro.md), [ANY.RUN — 2.4.4](../../modules/02-cti/04-platforms/04-anyrun/student-guide.md), and [IOC handling — 2.5.1](../../modules/02-cti/05-enrichment/01-ioc-handling/student-guide.md).
- [Infrastructure pivots — 2.5.5](../../modules/02-cti/05-enrichment/05-infra-pivot/student-guide.md) and [correlation — 2.5.7](../../modules/02-cti/05-enrichment/07-correlation/student-guide.md).
- [Technique-focused hunting — 3.6.3](../../modules/03-hunter/06-attacker-techniques/03-hunt-specific/student-guide.md) and [DE package review — 4.5](../../modules/04-de/05-hunt-and-intel-packages/student-guide.md).
