# Module 2.4.6 – urlscan.io

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.6 B / C / C ; 2.4.6.1 3c / 4c / 4c  
- Hunter: 2.4.6 A / B / B ; 2.4.6.1 2b / 3c / 4c  
- SOC: 2.4.6 A / A / B ; 2.4.6.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## How to use this platform guide

**Orientation now (about 5 minutes):** retrieve an instructor-provided result, identify the scan URL/time, visited page, and one request or redirect, and state one limitation. The first pass is about finding and recording evidence.

**Application with [2.5.5](../../05-enrichment/05-infra-pivot/student-guide.md):** return to the detailed concepts, worked example, and knowledge check below when studying web-infrastructure relationships. The lesson's total estimated time includes both passes; this is one lesson delivered in two parts. Complete its platform performance check during the application pass.

## Learning Objectives

By the end of this module, you will be able to:

1. Explain what a urlscan.io result captures about one browser scan of a URL.
2. Retrieve or interpret a scan result and extract page, redirect, requested-host, IP, certificate, and response evidence without treating one scan as permanent truth about the site.

**Mapped Proficiency Items:**
- K: 2.4.6 – URLScan
- T: 2.4.6.1 – Submit or retrieve a URLScan result and extract actionable intelligence

## 1. Key Concepts

urlscan.io loads a URL in a browser environment and records information about that scan.

The Result API includes data such as:
- submitted and final URL;
- page title;
- primary IP;
- whether the page redirected;
- requested domains, IPs, and URLs;
- HTTP requests/responses;
- certificate information;
- screenshot and DOM when stored;
- service verdicts.

References:
- [urlscan.io API Documentation](https://urlscan.io/docs/api/)
- [urlscan.io Result API Reference](https://urlscan.io/docs/result/)

### One scan is one observation

A urlscan result describes **that scan at that time under that scan environment**.

Web content can vary by:
- time;
- geography;
- cookies/session state;
- user agent;
- authentication;
- server-side logic;
- anti-bot or anti-analysis behavior.

Therefore:

> The scan observed a redirect to `example-login.test`.

is defensible.

> The URL always redirects there.

requires more evidence.

### Requested hosts are useful pivot candidates

The browser may contact many domains and IP addresses while rendering a page.

Those can include:
- first-party infrastructure;
- CDNs;
- analytics;
- advertising;
- fonts;
- third-party scripts;
- malicious payload or redirect infrastructure.

A requested host should therefore be **classified before being treated as adversary infrastructure**.

The fact that a page loaded Google Fonts, a CDN, or common analytics does not make those services part of the malicious campaign.

### Redirect chain is often more useful than the screenshot

A screenshot tells you what the rendered page looked like.

The redirect and request data can show:
- where the browser started;
- where it ended;
- which intermediate URLs were visited;
- which infrastructure delivered content.

For infrastructure analysis, those machine-readable relationships may be more useful than the visual appearance alone.

### Search existing scans before submitting

urlscan's documentation recommends searching for existing scans before resubmitting.

A classroom course can safely work from static result cards without sending live organizational URLs to an external service.

If live submission is ever used operationally, **scan visibility matters**. urlscan supports visibility settings, and analysts should follow organizational policy before submitting sensitive, internal, tokenized, or otherwise private URLs.

Reference: [urlscan.io API Documentation – Submission and visibility](https://urlscan.io/docs/api/)

### Separate classroom example — not A12

This static result is **training-only**. Its redirect/page/contact details are not facts of A12.

Suppose the result card shows:

- tasked URL: `https://sync-gateway.example/start`;
- final URL: `/download`;
- title: `Software Update`;
- requested host: `cdn-lab.example`;
- primary IP: `198.51.100.77`;
- redirect occurred;
- screenshot stored.

Valid observations:

> The scan redirected from the submitted URL to `/download`.

> The scan contacted `cdn-lab.example` and `198.51.100.77`.

> The rendered page title was `Software Update`.

These facts become candidates for enrichment. They do not by themselves prove that every host contacted is adversary-owned or that every visitor receives the same page.

## 2. Knowledge Check

1. Why should one urlscan result be described as an observation rather than permanent truth about a URL?
2. A page requests a common analytics domain and a rare host from the supplied classroom card. Should both automatically become adversary infrastructure? Why or why not?
3. Name three useful fields or evidence types you can extract from a urlscan result.

## 3. Summary

urlscan records one browser scan of a URL.

Use page metadata, redirects, requested domains/IPs/URLs, responses, certificates, screenshot, and DOM as evidence from that scan. Classify third-party dependencies before promoting them to adversary infrastructure, and follow organizational policy before submitting sensitive URLs.


## Supporting References

- [urlscan.io API Documentation](https://urlscan.io/docs/api/)
- [urlscan.io Result API Reference](https://urlscan.io/docs/result/)
- [urlscan.io Quickstart](https://docs.urlscan.io/guides/quickstart)

**Next:** [2.4 – CTI Tools and Platforms Summary](../summary.md).
