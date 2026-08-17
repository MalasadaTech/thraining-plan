# Training Plan

Curriculum for SOC Analysts, Threat Hunters, and CTI Analysts. Content is organized so each teaching module is one folder, grouped by role and unit.

## Layout

```
docs/
  outlines/training-outlines.md   # source list of knowledge and task items
  proficiency-legend.md           # CFETP-style 3/5/7 levels and codes
  matrices/                       # combined + per-role proficiency matrices
  tracker.csv                     # module status (edit this)
  tracker.md                      # status legend and folder mapping
  concept-index.md                # taught concepts → module (book-style index)
  contributing.md                 # how to add a requirement and a module
  generate-module.md              # AI instructions to write a Gate 2 module
  story-bible.md                  # living classroom fiction (PRD / DYA)
  companion-story/                # outline, plan, finished A12 story
  todo.md                         # review and follow-up list

templates/                        # proposal + module writing templates
modules/
  00-intro/<unit>/<module>/       # front door + shared hours (everyone, before SOC)
  01-soc/<unit>/<module>/
  02-cti/<unit>/<module>/         # taught after SOC; IDs 2.x
  03-hunter/<unit>/<module>/      # taught after CTI; IDs 3.x
  04-de/<module>/                 # Detection Engineer
labs/                             # reusable sample logs and PCAP
```

Do not put more than three path levels under `modules/` (`role / unit / module`).

## Numbering

Two ID systems exist. Do not mix them in filenames.

| System | Example | Use for |
|--------|---------|---------|
| **Matrix item** (canonical) | `1.2.2.1`, `1.2.2.2` | Proficiency tracking, mapped items in guides |
| **Outline heading** | `1.2.2` Conn knowledge, `1.2.3` Conn tasks | Curriculum design only |

A **module** is a teaching unit. It may cover one outline knowledge item plus its matching tasks. **Teach order:** full `00-intro` first (`0.1` layout → `0.2`–`0.5` → `0.6` / `0.7` / `0.8`) → SOC `1.1`–`1.4` → **SOC ends at `1.5` reporting** → CTI → hunt → DE. Map: [modules/00-intro/README.md](modules/00-intro/README.md). **Retired:** `1.7`, `1.8.2`–`1.8.5`.

Folder names are not dotted IDs:

| Folder | Matrix items | Outline headings |
|--------|----------------|------------------|
| `modules/00-intro/01-course-layout` | `0.1` | `0.1` a–d |
| `modules/00-intro/02-what-a-soc-is` | `0.2` | `0.2` a–c |
| `modules/00-intro/03-jobs-in-one-sentence` | `0.3` | `0.3` a–f |
| `modules/00-intro/04-how-work-moves` | `0.4` / `0.4.1` | `0.4` a–g + `0.4.1` |
| `modules/00-intro/05-where-jobs-overlap` | `0.5` | `0.5` a–d |
| `modules/01-soc/01-endpoint/01-endpoint-activity` | `1.1.1.1`–`1.1.1.2` | `1.1.1` + `1.1.1.1` |
| `modules/01-soc/01-endpoint/02-process-activity` | `1.1.2.1`–`1.1.2.3` | `1.1.2` + `1.1.2.1` |
| `modules/01-soc/01-endpoint/03-file-system-activity` | `1.1.3.1`–`1.1.3.3` | `1.1.3` + `1.1.3.1` |
| `modules/01-soc/01-endpoint/04-network-activity` | `1.1.4.1`–`1.1.4.3` | `1.1.4` + `1.1.4.1` |
| `modules/01-soc/01-endpoint/05-registry-activity` | `1.1.5.1`–`1.1.5.3` | `1.1.5` + `1.1.5.1` |
| `modules/01-soc/01-endpoint/06-image-driver-load` | `1.1.6.1`–`1.1.6.3` | `1.1.6` + `1.1.6.1` |
| `modules/01-soc/02-zeek/01-concepts` | `1.2.1.1` | `1.2.1` |
| `modules/01-soc/02-zeek/02-conn-engine` | `1.2.2.1`–`1.2.2.3` | `1.2.2` + `1.2.3` |
| `modules/01-soc/02-zeek/03-dns-engine` | `1.2.3.1`–`1.2.3.3` | `1.2.4` + `1.2.5` |
| `modules/01-soc/02-zeek/04-tls-engine` | `1.2.4.1`–`1.2.4.3` | `1.2.6` + `1.2.7` |
| `modules/01-soc/02-zeek/05-http-engine` | `1.2.5.1`–`1.2.5.3` | `1.2.8` + `1.2.9` |
| `modules/01-soc/02-zeek/06-smtp-engine` | `1.2.6.1`–`1.2.6.3` | `1.2.10` + `1.2.11` |
| `modules/01-soc/02-zeek/07-files-engine` | `1.2.7.1`–`1.2.7.3` | `1.2.12` + `1.2.13` |
| `modules/01-soc/02-zeek/08-weird-engine` | `1.2.8.1`–`1.2.8.3` | `1.2.14` + `1.2.15` |
| `modules/01-soc/03-detection/01-sigma-rules` | `1.3.1.1`–`1.3.1.3` | `1.3.1` + `1.3.2` |
| `modules/01-soc/03-detection/02-suricata-rules` | `1.3.2.1`–`1.3.2.3` | `1.3.3` + `1.3.4` |
| `modules/01-soc/03-detection/03-yara-rules` | `1.3.3.1`–`1.3.3.3` | `1.3.5` + `1.3.6` |
| `modules/01-soc/03-detection/04-siem-rules` | `1.3.4.1`–`1.3.4.3` | `1.3.7` + `1.3.8` |
| `modules/01-soc/04-alerts/01-context-investigation` | `1.4.1.1`–`1.4.1.6` | `1.4.1` + `1.4.1.1` |
| `modules/01-soc/04-alerts/02-classification` | `1.4.2.1`–`1.4.2.2` | `1.4.2` + `1.4.2.1` |
| `modules/01-soc/04-alerts/03-false-positive-causes` | `1.4.3.1`–`1.4.3.2` | `1.4.3` + `1.4.3.1` |
| `modules/01-soc/04-alerts/04-categorizations` | `1.4.4.1`–`1.4.4.2` | `1.4.4` + `1.4.4.1` |
| `modules/01-soc/04-alerts/05-sla-response-times` | `1.4.5.1`–`1.4.5.3` | `1.4.5` + `1.4.5.1` |
| `modules/00-intro/06-frameworks/01-attck` | `0.6.1.1`–`0.6.1.2` | `0.6.1.1` + `0.6.1.2` (00.06) |
| `modules/00-intro/06-frameworks/02-diamond-model` | `0.6.2.1`–`0.6.2.2` | `0.6.2.1` + `0.6.2.2` (00.06) |
| `modules/00-intro/06-frameworks/03-cyber-kill-chain` | `0.6.3.1`–`0.6.3.2` | `0.6.3.1` + `0.6.3.2` (00.06) |
| `modules/01-soc/05-reporting/01-report-types` | `1.5.1.1`–`1.5.1.2` | `1.5.1` + `1.5.1.1` |
| `modules/01-soc/05-reporting/02-reporting-timelines` | `1.5.2.1`–`1.5.2.2` | `1.5.2` + `1.5.2.1` |
| `modules/01-soc/05-reporting/03-notification-distribution` | `1.5.3.1`–`1.5.3.2` | `1.5.3` + `1.5.3.1` |
| `modules/00-intro/08-environment/01-orientation` | `0.8` / `0.8.1` | `0.8` + `0.8.1` (00.08) |
| `modules/02-cti/01-core-intel/01-data-info-intel` | `2.1.1` / `2.1.1.1` | `2.1.1` + `2.1.1.1` |
| `modules/02-cti/01-core-intel/02-intelligence-lifecycle` | `2.1.2` / `2.1.2.1` | `2.1.2` + `2.1.2.1` |
| `modules/02-cti/01-core-intel/03-intelligence-types` | `2.1.3` / `2.1.3.1` | `2.1.3` + `2.1.3.1` |
| `modules/02-cti/01-core-intel/04-intelligence-requirements` | `2.1.4` / `2.1.4.1`–`2.1.4.3` | `2.1.4` + `2.1.4.1` |
| `modules/02-cti/01-core-intel/05-actionable-intelligence` | `2.1.5` / `2.1.5.1` | `2.1.5` + `2.1.5.1` |
| `modules/02-cti/01-core-intel/06-tailoring-audience` | `2.1.6` / `2.1.6.1` | `2.1.6` + `2.1.6.1` |
| `modules/02-cti/01-core-intel/07-attribution` | `2.1.7` / `2.1.7.1` | `2.1.7` + `2.1.7.1` |
| `modules/02-cti/01-core-intel/08-collection-sources` | `2.1.8` / `2.1.8.1`–`2.1.8.2` | `2.1.8` + `2.1.8.1` |
| `modules/02-cti/02-tradecraft/01-estimative-language` | `2.2.1` / `2.2.1.1` | `2.2.1` + `2.2.1.1` |
| `modules/02-cti/02-tradecraft/02-structured-techniques` | `2.2.2` / `2.2.2.1` | `2.2.2` + `2.2.2.1` |
| `modules/02-cti/02-tradecraft/03-admiralty-code` | `2.2.3` / `2.2.3.1` | `2.2.3` + `2.2.3.1` |
| `modules/02-cti/02-tradecraft/04-cognitive-biases` | `2.2.4` / `2.2.4.1` | `2.2.4` + `2.2.4.1` |
| `modules/02-cti/03-tools/01-internal-tip` | `2.3.1` / `2.3.1.1` | `2.3.1` + `2.3.1.1` |
| `modules/00-intro/07-tool-survey/01-external-tools` | `0.7` / `0.7.1` | `0.7` + `0.7.1` (00.07) |
| `modules/02-cti/04-file-similarity` | `2.4.1` / `2.4.1.1`–`2.4.1.2` | `2.4.1` + `2.4.1.1` |
| `modules/02-cti/05-rdap-whois` | `2.5.1` / `2.5.1.1` | `2.5.1` + `2.5.1.1` |
| `modules/02-cti/06-advanced-dns` | `2.6.1` / `2.6.1.1` | `2.6.1` + `2.6.1.1` |
| `modules/02-cti/07-frameworks/01-attck-cti` | `2.7.1` / `2.7.1.1` | `2.7.1` + `2.7.1.1` |
| `modules/02-cti/07-frameworks/02-diamond-cti` | `2.7.2` / `2.7.2.1` | `2.7.2` + `2.7.2.1` |
| `modules/02-cti/07-frameworks/03-kill-chain-cti` | `2.7.3` / `2.7.3.1` | `2.7.3` + `2.7.3.1` |
| `modules/02-cti/07-frameworks/04-dtf` | `2.7.4` / `2.7.4.1`–`2.7.4.3` | `2.7.4` + `2.7.4.1` |
| `modules/02-cti/08-enrichment/01-infra-pivot` | `2.8.1` / `2.8.1.1` | `2.8.1` + `2.8.1.1` |
| `modules/02-cti/08-enrichment/02-applicable-ttps` | `2.8.2` / `2.8.2.1` | `2.8.2` + `2.8.2.1` |
| `modules/02-cti/08-enrichment/03-ioc-handling` | `2.8.3` / `2.8.3.1`–`2.8.3.2` | `2.8.3` + `2.8.3.1` |
| `modules/02-cti/08-enrichment/04-relevance-impact` | `2.8.4` / `2.8.4.1` | `2.8.4` + `2.8.4.1` |
| `modules/02-cti/09-platforms/01-virustotal` | `2.9.1` / `2.9.1.1` | `2.9.1` + `2.9.1.1` |
| `modules/02-cti/09-platforms/02-anyrun` | `2.9.2` / `2.9.2.1` | `2.9.2` + `2.9.2.1` |
| `modules/02-cti/09-platforms/03-silent-push` | `2.9.3` / `2.9.3.1` | `2.9.3` + `2.9.3.1` |
| `modules/02-cti/09-platforms/04-urlscan` | `2.9.4` / `2.9.4.1` | `2.9.4` + `2.9.4.1` |
| `modules/02-cti/10-stix/01-core-objects` | `2.10.1` / `2.10.1.1` | `2.10.1` + `2.10.1.1` |
| `modules/02-cti/10-stix/02-stix-production` | `2.10.2` / `2.10.2.1`–`2.10.2.3` | `2.10.2` + `2.10.2.1` |
| `modules/02-cti/11-production/01-finished-products` | `2.11.1` / `2.11.1.1`–`2.11.1.2` | `2.11.1` + `2.11.1.1` |
| `modules/02-cti/11-production/02-dissemination` | `2.11.2` / `2.11.2.1`–`2.11.2.3` | `2.11.2` + `2.11.2.1` |
| `modules/02-cti/11-production/03-rfi` | `2.11.3` / `2.11.3.1` | `2.11.3` + `2.11.3.1` |
| `modules/02-cti/12-site-specific/01-local-priorities` | `2.12.1` / `2.12.1.1` | `2.12.1` + `2.12.1.1` |
| `modules/02-cti/12-site-specific/02-local-production` | `2.12.2` / `2.12.2.1`–`2.12.2.2` | `2.12.2` + `2.12.2.1` |
| `modules/02-cti/12-site-specific/03-local-dissemination` | `2.12.3` / `2.12.3.1` | `2.12.3` + `2.12.3.1` |
| `modules/03-hunter/01-purpose` | `3.1.1` / `3.1.1.1` / `3.1.1.2` | `3.1` + `3.1.1` |
| `modules/03-hunter/02-methodology/01-hunt-types` | `3.2.1` / `3.2.1.1`–`3.2.1.4` | `3.2.1` + `3.2.3` tasks 4–7 |
| `modules/03-hunter/02-methodology/02-hunt-development` | `3.2.2` / `3.2.2.1`–`3.2.2.3` | `3.2.2` + `3.2.3` tasks 1–3 |
| `modules/03-hunter/03-online-tools` | `3.3.1` / `3.3.1.1`–`3.3.1.3` | `3.3.1` + `3.3.2` tasks 1–3 |
| `modules/03-hunter/04-cti-for-hunters/01-assessing-cti` | `3.4.1` / `3.4.1.1` | `3.4.1` + `3.4.1.1` |
| `modules/03-hunter/04-cti-for-hunters/02-extracting-leads` | `3.4.2` / `3.4.2.1`–`3.4.2.3` | `3.4.2` + `3.4.2.1` tasks 1–3 |
| `modules/03-hunter/04-cti-for-hunters/03-stix-as-hunt-input` | `3.4.3` / `3.4.3.1`–`3.4.3.2` | `3.4.3` + `3.4.3.1` tasks 1–2 |
| `modules/03-hunter/05-framework-application` | `3.5.1` / `3.5.1.1`–`3.5.1.3` | `3.5.1` + `3.5.2` tasks 1–3 |
| `modules/03-hunter/06-attacker-techniques/01-persistence` | `3.6.1` / `3.6.1.1` | `3.6.1` + `3.6.3` task 1 |
| `modules/03-hunter/06-attacker-techniques/02-privilege-escalation` | `3.6.2` / `3.6.2.1` | `3.6.2` + `3.6.3` task 2 |
| `modules/03-hunter/06-attacker-techniques/03-hunt-specific` | `3.6.3` | `3.6.3` task 3 |
| `modules/03-hunter/07-site-specific/01-hunt-control` | `3.7.1` / `3.7.1.1` | `3.7.1` + `3.7.4` task 1 |
| `modules/03-hunter/07-site-specific/02-hunt-documentation` | `3.7.2` / `3.7.2.1` | `3.7.2` + `3.7.4` task 2 |
| `modules/03-hunter/07-site-specific/03-hunt-outputs` | `3.7.3` / `3.7.3.1` | `3.7.3` + `3.7.4` task 3 |
| `modules/04-de/01-what-de-owns` | `4.1` / `4.1.1` | `4.1` a–d + `4.1.1` |
| `modules/04-de/02-sound-and-shop-requirements` | `4.2` / `4.2.1`–`4.2.3` | `4.2` a–d + `4.2.1` |
| `modules/04-de/03-nominations` | `4.3` / `4.3.1` | `4.3` a–e + `4.3.1` |
| `modules/04-de/04-tune-requests` | `4.4` / `4.4.1`–`4.4.2` | `4.4` a–d + `4.4.1` |
| `modules/04-de/05-hunt-and-intel-packages` | `4.5` / `4.5.1`–`4.5.2` | `4.5` a–d + `4.5.1` |
| `modules/04-de/06-detection-lifecycle` | `4.6` / `4.6.1`–`4.6.2` | `4.6` a–d + `4.6.1` |
| `modules/04-de/07-sensors` | `4.7` / `4.7.1`–`4.7.2` | `4.7` a–c + `4.7.1` |
| `modules/04-de/08-site-specific` | `4.8.1` / `4.8.1.1` ; `4.8.2` / `4.8.2.1`–`4.8.2.2` | `4.8.1` + `4.8.2` |

Record the mapping in each module `README.md`.

## Changing the curriculum

Do not start with a student guide. Approve the requirement first, then build the lesson.

1. Propose with [templates/requirement-proposal.md](templates/requirement-proposal.md).
2. Follow the two gates in [docs/contributing.md](docs/contributing.md) (matrix/outline/tracker, then guides, concepts, and the index).
3. To generate a lesson with an AI tool, use the matrix ID for **that lesson** (a unit such as `1.2.5`, or a cluster child such as `2.1.1` — not cluster `2.1`): `Follow docs/generate-module.md and generate teaching-unit <ID> (<Title>) for me to review. Do not invent IDs.`

Shared topics live under `modules/00-intro/`. Do not copy those lessons into each role.
