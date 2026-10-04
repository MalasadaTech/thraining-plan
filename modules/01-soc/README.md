# SOC Modules — 1.x

This sequence develops the evidence and decisions used in SOC work: interpret endpoint and network observations, read and propose detections, investigate and assess alerts, then report and route the result. Module IDs, proficiency mappings, and lesson time ranges are preserved.

## Review path

| Unit | Focus |
|---|---|
| 1.0 | Orientation to the SOC evidence-to-handoff workflow. |
| 1.1 | Endpoint activity and focused queries. |
| 1.2 | Zeek observations, evidence limits, and focused queries. |
| 1.3 | Reading and modifying basic detection rules. |
| 1.4 | Investigation, classification, causes, categories, and response-time goals. |
| 1.5 | Report purpose, timing, and distribution. |
| 1.6 | Section synthesis: reconnect evidence, investigation, and handoff; bridge into CTI. |

## Module index

| Module | Student guide | Instructor guide | Slides |
|---|---|---|---|
| 1.0 – SOC Analyst Fundamentals | [Read](00-intro/student-guide.md) | [Teach](00-intro/instructor-guide.md) | [Present](00-intro/slides.md) |
| 1.1.1 – Endpoint activity (the map) | [Read](01-endpoint/01-endpoint-activity/student-guide.md) | [Teach](01-endpoint/01-endpoint-activity/instructor-guide.md) | [Present](01-endpoint/01-endpoint-activity/slides.md) |
| 1.1.2 – Process Activity | [Read](01-endpoint/02-process-activity/student-guide.md) | [Teach](01-endpoint/02-process-activity/instructor-guide.md) | [Present](01-endpoint/02-process-activity/slides.md) |
| 1.1.3 – File System Activity | [Read](01-endpoint/03-file-system-activity/student-guide.md) | [Teach](01-endpoint/03-file-system-activity/instructor-guide.md) | [Present](01-endpoint/03-file-system-activity/slides.md) |
| 1.1.4 – Network Activity (Endpoint) | [Read](01-endpoint/04-network-activity/student-guide.md) | [Teach](01-endpoint/04-network-activity/instructor-guide.md) | [Present](01-endpoint/04-network-activity/slides.md) |
| 1.1.5 – Registry Activity | [Read](01-endpoint/05-registry-activity/student-guide.md) | [Teach](01-endpoint/05-registry-activity/instructor-guide.md) | [Present](01-endpoint/05-registry-activity/slides.md) |
| 1.1.6 – Image and Driver Load Activity | [Read](01-endpoint/06-image-driver-load/student-guide.md) | [Teach](01-endpoint/06-image-driver-load/instructor-guide.md) | [Present](01-endpoint/06-image-driver-load/slides.md) |
| 1.2.1 – Zeek Concepts | [Read](02-zeek/01-concepts/student-guide.md) | [Teach](02-zeek/01-concepts/instructor-guide.md) | [Present](02-zeek/01-concepts/slides.md) |
| 1.2.2 – Conn Engine | [Read](02-zeek/02-conn-engine/student-guide.md) | [Teach](02-zeek/02-conn-engine/instructor-guide.md) | [Present](02-zeek/02-conn-engine/slides.md) |
| 1.2.3 – DNS Engine | [Read](02-zeek/03-dns-engine/student-guide.md) | [Teach](02-zeek/03-dns-engine/instructor-guide.md) | [Present](02-zeek/03-dns-engine/slides.md) |
| 1.2.4 – TLS Engine | [Read](02-zeek/04-tls-engine/student-guide.md) | [Teach](02-zeek/04-tls-engine/instructor-guide.md) | [Present](02-zeek/04-tls-engine/slides.md) |
| 1.2.5 – HTTP Engine | [Read](02-zeek/05-http-engine/student-guide.md) | [Teach](02-zeek/05-http-engine/instructor-guide.md) | [Present](02-zeek/05-http-engine/slides.md) |
| 1.2.6 – SMTP Engine | [Read](02-zeek/06-smtp-engine/student-guide.md) | [Teach](02-zeek/06-smtp-engine/instructor-guide.md) | [Present](02-zeek/06-smtp-engine/slides.md) |
| 1.2.7 – Files Engine | [Read](02-zeek/07-files-engine/student-guide.md) | [Teach](02-zeek/07-files-engine/instructor-guide.md) | [Present](02-zeek/07-files-engine/slides.md) |
| 1.2.8 – Weird Engine | [Read](02-zeek/08-weird-engine/student-guide.md) | [Teach](02-zeek/08-weird-engine/instructor-guide.md) | [Present](02-zeek/08-weird-engine/slides.md) |
| 1.3.1 – SIGMA Rules | [Read](03-detection/01-sigma-rules/student-guide.md) | [Teach](03-detection/01-sigma-rules/instructor-guide.md) | [Present](03-detection/01-sigma-rules/slides.md) |
| 1.3.2 – Suricata Rules | [Read](03-detection/02-suricata-rules/student-guide.md) | [Teach](03-detection/02-suricata-rules/instructor-guide.md) | [Present](03-detection/02-suricata-rules/slides.md) |
| 1.3.3 – YARA Rules | [Read](03-detection/03-yara-rules/student-guide.md) | [Teach](03-detection/03-yara-rules/instructor-guide.md) | [Present](03-detection/03-yara-rules/slides.md) |
| 1.3.4 – SIEM Rules | [Read](03-detection/04-siem-rules/student-guide.md) | [Teach](03-detection/04-siem-rules/instructor-guide.md) | [Present](03-detection/04-siem-rules/slides.md) |
| 1.4.1 – Alert Context and Investigation | [Read](04-alerts/01-context-investigation/student-guide.md) | [Teach](04-alerts/01-context-investigation/instructor-guide.md) | [Present](04-alerts/01-context-investigation/slides.md) |
| 1.4.2 – Alert Classification | [Read](04-alerts/02-classification/student-guide.md) | [Teach](04-alerts/02-classification/instructor-guide.md) | [Present](04-alerts/02-classification/slides.md) |
| 1.4.3 – Common False Positive Causes | [Read](04-alerts/03-false-positive-causes/student-guide.md) | [Teach](04-alerts/03-false-positive-causes/instructor-guide.md) | [Present](04-alerts/03-false-positive-causes/slides.md) |
| 1.4.4 – Common Alert Categorizations | [Read](04-alerts/04-categorizations/student-guide.md) | [Teach](04-alerts/04-categorizations/instructor-guide.md) | [Present](04-alerts/04-categorizations/slides.md) |
| 1.4.5 – SLA / Response Time Goals | [Read](04-alerts/05-sla-response-times/student-guide.md) | [Teach](04-alerts/05-sla-response-times/instructor-guide.md) | [Present](04-alerts/05-sla-response-times/slides.md) |
| 1.5.1 – Report Types | [Read](05-reporting/01-report-types/student-guide.md) | [Teach](05-reporting/01-report-types/instructor-guide.md) | [Present](05-reporting/01-report-types/slides.md) |
| 1.5.2 – Reporting Timeline Requirements | [Read](05-reporting/02-reporting-timelines/student-guide.md) | [Teach](05-reporting/02-reporting-timelines/instructor-guide.md) | [Present](05-reporting/02-reporting-timelines/slides.md) |
| 1.5.3 – Notification and Distribution | [Read](05-reporting/03-notification-distribution/student-guide.md) | [Teach](05-reporting/03-notification-distribution/instructor-guide.md) | [Present](05-reporting/03-notification-distribution/slides.md) |
| 1.6 – SOC Analyst Section Summary | [Read](06-summary/student-guide.md) | [Teach](06-summary/instructor-guide.md) | [Present](06-summary/slides.md) |

## What changed in this pass

All 26 student guides, instructor guides, slide sources, and lesson indexes were revised together. Connected explanations replace repeated boundary reminders; worked examples show what the evidence supports; knowledge checks now require interpretation and, where mapped, an actual query or rule modification.

Technical corrections include endpoint operation and direction limits, current and legacy Zeek file-log fields, TLS establishment and visibility, query comparison semantics, detection-versus-maliciousness classification, privilege context, and complete timing calculations. Named technical references link to primary documentation.

## Teaching and validation notes

Examples use fictional hosts, documentation addresses, and example domains. The KQL for MDE uses documented table and field names, subject to the locally supported event types. Zeek and Sysmon query examples explicitly declare classroom table and ingestion assumptions. They require schema mapping before operational use. Queries and rules were reviewed as teaching examples; they were not executed against a live tenant or deployed to a sensor.

The review checked all 79 questions against their answer keys and slide sources, preserved the existing proficiency mappings, and resolved 546 internal source links. YAML examples were parsed successfully; live query and detection-engine execution remain outside this review.

The lesson sequence uses worked examples and written discussion checks; no new labs were added. Classroom timing and notification charts remain instructional assumptions rather than workplace policy. Exported documents have not been refreshed and may still contain earlier wording.
