# Module tracker

The working tracker is [tracker.csv](tracker.csv). Add a row there when you start a module, and update the status columns as artifacts land.

## Status values

| Status | Meaning |
|--------|---------|
| Not Started | Work has not begun |
| In Progress | Actively being developed |
| Review | Draft complete, needs review |
| Complete | Finished and approved |
| Deferred | Intentionally postponed |

## Folder mapping

Module IDs in the CSV are teaching-unit IDs (same as the matrix), not outline K/T headings.

| Module ID | Folder |
|-----------|--------|
| 0.1 | [modules/00-intro/01-what-a-soc-is](../modules/00-intro/01-what-a-soc-is/) |
| 0.2 | [modules/00-intro/02-jobs-in-one-sentence](../modules/00-intro/02-jobs-in-one-sentence/) |
| 0.3 | [modules/00-intro/03-how-work-moves](../modules/00-intro/03-how-work-moves/) |
| 0.4 | [modules/00-intro/04-where-jobs-overlap](../modules/00-intro/04-where-jobs-overlap/) |
| 0.5 | [modules/00-intro/05-course-layout](../modules/00-intro/05-course-layout/) |
| 1.1.1 | [modules/01-soc/01-endpoint/01-endpoint-activity](../modules/01-soc/01-endpoint/01-endpoint-activity/) |
| 1.1.2 | [modules/01-soc/01-endpoint/02-process-activity](../modules/01-soc/01-endpoint/02-process-activity/) |
| 1.1.3 | [modules/01-soc/01-endpoint/03-file-system-activity](../modules/01-soc/01-endpoint/03-file-system-activity/) |
| 1.1.4 | [modules/01-soc/01-endpoint/04-network-activity](../modules/01-soc/01-endpoint/04-network-activity/) |
| 1.1.5 | [modules/01-soc/01-endpoint/05-registry-activity](../modules/01-soc/01-endpoint/05-registry-activity/) |
| 1.1.6 | [modules/01-soc/01-endpoint/06-image-driver-load](../modules/01-soc/01-endpoint/06-image-driver-load/) |
| 1.2.1 | [modules/01-soc/02-zeek/01-concepts](../modules/01-soc/02-zeek/01-concepts/) |
| 1.2.2 | [modules/01-soc/02-zeek/02-conn-engine](../modules/01-soc/02-zeek/02-conn-engine/) |
| 1.2.3 | [modules/01-soc/02-zeek/03-dns-engine](../modules/01-soc/02-zeek/03-dns-engine/) |
| 1.2.4 | [modules/01-soc/02-zeek/04-tls-engine](../modules/01-soc/02-zeek/04-tls-engine/) |
| 1.2.5 | [modules/01-soc/02-zeek/05-http-engine](../modules/01-soc/02-zeek/05-http-engine/) |
| 1.2.6 | [modules/01-soc/02-zeek/06-smtp-engine](../modules/01-soc/02-zeek/06-smtp-engine/) |
| 1.2.7 | [modules/01-soc/02-zeek/07-files-engine](../modules/01-soc/02-zeek/07-files-engine/) |
| 1.2.8 | [modules/01-soc/02-zeek/08-weird-engine](../modules/01-soc/02-zeek/08-weird-engine/) |
| 1.3.1 | [modules/01-soc/03-detection/01-sigma-rules](../modules/01-soc/03-detection/01-sigma-rules/) |
| 1.3.2 | [modules/01-soc/03-detection/02-suricata-rules](../modules/01-soc/03-detection/02-suricata-rules/) |
| 1.3.3 | [modules/01-soc/03-detection/03-yara-rules](../modules/01-soc/03-detection/03-yara-rules/) |
| 1.3.4 | [modules/01-soc/03-detection/04-siem-rules](../modules/01-soc/03-detection/04-siem-rules/) |
| 1.4.1 | [modules/01-soc/04-alerts/01-context-investigation](../modules/01-soc/04-alerts/01-context-investigation/) |
| 1.4.2 | [modules/01-soc/04-alerts/02-classification](../modules/01-soc/04-alerts/02-classification/) |
| 1.4.3 | [modules/01-soc/04-alerts/03-false-positive-causes](../modules/01-soc/04-alerts/03-false-positive-causes/) |
| 1.4.4 | [modules/01-soc/04-alerts/04-categorizations](../modules/01-soc/04-alerts/04-categorizations/) |
| 1.4.5 | [modules/01-soc/04-alerts/05-sla-response-times](../modules/01-soc/04-alerts/05-sla-response-times/) |
| 1.5.1 | [modules/01-soc/05-frameworks/01-attck](../modules/01-soc/05-frameworks/01-attck/) |
| 1.5.2 | [modules/01-soc/05-frameworks/02-diamond-model](../modules/01-soc/05-frameworks/02-diamond-model/) |
| 1.5.3 | [modules/01-soc/05-frameworks/03-cyber-kill-chain](../modules/01-soc/05-frameworks/03-cyber-kill-chain/) |
| 1.6.1 | [modules/01-soc/06-reporting/01-report-types](../modules/01-soc/06-reporting/01-report-types/) |
| 1.6.2 | [modules/01-soc/06-reporting/02-reporting-timelines](../modules/01-soc/06-reporting/02-reporting-timelines/) |
| 1.6.3 | [modules/01-soc/06-reporting/03-notification-distribution](../modules/01-soc/06-reporting/03-notification-distribution/) |
| 1.7.1 | [modules/01-soc/07-shift-change/01-changeover-process](../modules/01-soc/07-shift-change/01-changeover-process/) |
| 1.7.2 | [modules/01-soc/07-shift-change/02-changeover-report](../modules/01-soc/07-shift-change/02-changeover-report/) |
| 1.8.1 | [modules/01-soc/08-site-specific/01-environment-orientation](../modules/01-soc/08-site-specific/01-environment-orientation/) |
| 1.8.2 | [modules/01-soc/08-site-specific/02-pcap-handling](../modules/01-soc/08-site-specific/02-pcap-handling/) |
| 1.8.3 | [modules/01-soc/08-site-specific/03-tool-access](../modules/01-soc/08-site-specific/03-tool-access/) |
| 1.8.4 | [modules/01-soc/08-site-specific/04-investigation-notes](../modules/01-soc/08-site-specific/04-investigation-notes/) |
| 1.8.5 | [modules/01-soc/08-site-specific/05-incident-response](../modules/01-soc/08-site-specific/05-incident-response/) |
| 2.1 | [modules/02-hunter/01-purpose](../modules/02-hunter/01-purpose/) |
| 2.2.1 | [modules/02-hunter/02-methodology/01-hunt-types](../modules/02-hunter/02-methodology/01-hunt-types/) |
| 2.2.2 | [modules/02-hunter/02-methodology/02-hunt-development](../modules/02-hunter/02-methodology/02-hunt-development/) |
| 2.3.1 | [modules/02-hunter/03-online-tools](../modules/02-hunter/03-online-tools/) |
| 2.4.1 | [modules/02-hunter/04-cti-for-hunters/01-assessing-cti](../modules/02-hunter/04-cti-for-hunters/01-assessing-cti/) |
| 2.4.2 | [modules/02-hunter/04-cti-for-hunters/02-extracting-leads](../modules/02-hunter/04-cti-for-hunters/02-extracting-leads/) |
| 2.4.3 | [modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input](../modules/02-hunter/04-cti-for-hunters/03-stix-as-hunt-input/) |
| 2.5.1 | [modules/02-hunter/05-framework-application](../modules/02-hunter/05-framework-application/) |
| 2.6.1 | [modules/02-hunter/06-attacker-techniques/01-persistence](../modules/02-hunter/06-attacker-techniques/01-persistence/) |
| 2.6.2 | [modules/02-hunter/06-attacker-techniques/02-privilege-escalation](../modules/02-hunter/06-attacker-techniques/02-privilege-escalation/) |
| 2.6.3 | [modules/02-hunter/06-attacker-techniques/03-hunt-specific](../modules/02-hunter/06-attacker-techniques/03-hunt-specific/) |
| 2.7.1 | [modules/02-hunter/07-site-specific/01-hunt-control](../modules/02-hunter/07-site-specific/01-hunt-control/) |
| 2.7.2 | [modules/02-hunter/07-site-specific/02-hunt-documentation](../modules/02-hunter/07-site-specific/02-hunt-documentation/) |
| 2.7.3 | [modules/02-hunter/07-site-specific/03-hunt-outputs](../modules/02-hunter/07-site-specific/03-hunt-outputs/) |
| 3.1.1 | [modules/03-cti/01-core-intel/01-data-info-intel](../modules/03-cti/01-core-intel/01-data-info-intel/) |
| 3.1.2 | [modules/03-cti/01-core-intel/02-intelligence-lifecycle](../modules/03-cti/01-core-intel/02-intelligence-lifecycle/) |
| 3.1.3 | [modules/03-cti/01-core-intel/03-intelligence-types](../modules/03-cti/01-core-intel/03-intelligence-types/) |
| 3.1.4 | [modules/03-cti/01-core-intel/04-intelligence-requirements](../modules/03-cti/01-core-intel/04-intelligence-requirements/) |
| 3.1.5 | [modules/03-cti/01-core-intel/05-actionable-intelligence](../modules/03-cti/01-core-intel/05-actionable-intelligence/) |
| 3.1.6 | [modules/03-cti/01-core-intel/06-tailoring-audience](../modules/03-cti/01-core-intel/06-tailoring-audience/) |
| 3.1.7 | [modules/03-cti/01-core-intel/07-attribution](../modules/03-cti/01-core-intel/07-attribution/) |
| 3.1.8 | [modules/03-cti/01-core-intel/08-collection-sources](../modules/03-cti/01-core-intel/08-collection-sources/) |
| 3.2.1 | [modules/03-cti/02-tradecraft/01-estimative-language](../modules/03-cti/02-tradecraft/01-estimative-language/) |
| 3.2.2 | [modules/03-cti/02-tradecraft/02-structured-techniques](../modules/03-cti/02-tradecraft/02-structured-techniques/) |
| 3.2.3 | [modules/03-cti/02-tradecraft/03-admiralty-code](../modules/03-cti/02-tradecraft/03-admiralty-code/) |
| 3.2.4 | [modules/03-cti/02-tradecraft/04-cognitive-biases](../modules/03-cti/02-tradecraft/04-cognitive-biases/) |
| 3.3.1 | [modules/03-cti/03-tools/01-internal-tip](../modules/03-cti/03-tools/01-internal-tip/) |
| 3.3.2 | [modules/03-cti/03-tools/02-external-tools](../modules/03-cti/03-tools/02-external-tools/) |
| 3.4.1 | [modules/03-cti/04-file-similarity](../modules/03-cti/04-file-similarity/) |
| 3.5.1 | [modules/03-cti/05-rdap-whois](../modules/03-cti/05-rdap-whois/) |
| 3.6.1 | [modules/03-cti/06-advanced-dns](../modules/03-cti/06-advanced-dns/) |
| 3.7.1 | [modules/03-cti/07-frameworks/01-attck-cti](../modules/03-cti/07-frameworks/01-attck-cti/) |
| 3.7.2 | [modules/03-cti/07-frameworks/02-diamond-cti](../modules/03-cti/07-frameworks/02-diamond-cti/) |
| 3.7.3 | [modules/03-cti/07-frameworks/03-kill-chain-cti](../modules/03-cti/07-frameworks/03-kill-chain-cti/) |
| 3.7.4 | [modules/03-cti/07-frameworks/04-dtf](../modules/03-cti/07-frameworks/04-dtf/) |
| 3.8.1 | [modules/03-cti/08-enrichment/01-infra-pivot](../modules/03-cti/08-enrichment/01-infra-pivot/) |
| 3.8.2 | [modules/03-cti/08-enrichment/02-applicable-ttps](../modules/03-cti/08-enrichment/02-applicable-ttps/) |
| 3.8.3 | [modules/03-cti/08-enrichment/03-ioc-handling](../modules/03-cti/08-enrichment/03-ioc-handling/) |
| 3.8.4 | [modules/03-cti/08-enrichment/04-relevance-impact](../modules/03-cti/08-enrichment/04-relevance-impact/) |
| 3.9.1 | [modules/03-cti/09-platforms/01-virustotal](../modules/03-cti/09-platforms/01-virustotal/) |
| 3.9.2 | [modules/03-cti/09-platforms/02-anyrun](../modules/03-cti/09-platforms/02-anyrun/) |
| 3.9.3 | [modules/03-cti/09-platforms/03-silent-push](../modules/03-cti/09-platforms/03-silent-push/) |
| 3.9.4 | [modules/03-cti/09-platforms/04-urlscan](../modules/03-cti/09-platforms/04-urlscan/) |
| 3.10.1 | [modules/03-cti/10-stix/01-core-objects](../modules/03-cti/10-stix/01-core-objects/) |
| 3.10.2 | [modules/03-cti/10-stix/02-stix-production](../modules/03-cti/10-stix/02-stix-production/) |
| 3.11.1 | [modules/03-cti/11-production/01-finished-products](../modules/03-cti/11-production/01-finished-products/) |
| 3.11.2 | [modules/03-cti/11-production/02-dissemination](../modules/03-cti/11-production/02-dissemination/) |
| 3.11.3 | [modules/03-cti/11-production/03-rfi](../modules/03-cti/11-production/03-rfi/) |
| 3.12.1 | [modules/03-cti/12-site-specific/01-local-priorities](../modules/03-cti/12-site-specific/01-local-priorities/) |
| 3.12.2 | [modules/03-cti/12-site-specific/02-local-production](../modules/03-cti/12-site-specific/02-local-production/) |
| 3.12.3 | [modules/03-cti/12-site-specific/03-local-dissemination](../modules/03-cti/12-site-specific/03-local-dissemination/) |
| 4.1 | [modules/04-de/01-what-de-owns](../modules/04-de/01-what-de-owns/) |
| 4.2 | [modules/04-de/02-sound-and-shop-requirements](../modules/04-de/02-sound-and-shop-requirements/) |
| 4.3 | [modules/04-de/03-nominations](../modules/04-de/03-nominations/) |
| 4.4 | [modules/04-de/04-tune-requests](../modules/04-de/04-tune-requests/) |
| 4.5 | [modules/04-de/05-hunt-and-intel-packages](../modules/04-de/05-hunt-and-intel-packages/) |
| 4.6 | [modules/04-de/06-detection-lifecycle](../modules/04-de/06-detection-lifecycle/) |
| 4.7 | [modules/04-de/07-sensors](../modules/04-de/07-sensors/) |
| 4.8 | [modules/04-de/08-site-specific](../modules/04-de/08-site-specific/) |
