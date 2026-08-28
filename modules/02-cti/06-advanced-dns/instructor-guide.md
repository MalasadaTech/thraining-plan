# Instructor Guide – Module 2.6.1 – Advanced DNS Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.6.1 B / C / C ; 2.6.1.1 3c / 4c / 4d  
- Hunter: 2.6.1 B / C / C ; 2.6.1.1 2b / 3c / 4c  
- SOC: 2.6.1 A / A / B ; 2.6.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read an SOA so you can say who runs the zone, then use NS and related records to enrich or pivot. Shared cloud is not “theirs.”

**Context (plain language):**

- What this lesson is for: CTI analysts read the records a zone publishes so they can see who runs a name and whether another name shares that control.
- How it hooks to the lesson before: 2.5.1 pulled registration and planted the NS pair `ns1.cdn-test.net` / `ns2.cdn-test.net`. This lesson reads the zone itself.
- How it hooks to the lesson after: 2.7.1 maps behavior (ATT&CK), not DNS records. The hop *sentence* is 2.8.1.
- Why we are doing it this way: after registration names the NS pair, interpret who operates the zone and pivot to a sibling before anyone claims shared hosting.
- What we are *not* doing in this lesson: Zeek `dns` fields or DGA (1.2.3). RDAP redo (2.5). Silent Push passive DNS (0.7). Hop-sentence format (2.8.1). No lab.
- Extra step: none.

Use the same names as the student guide: **authoritative DNS**, **SOA**, **MNAME**, **RNAME**, **serial**, **NS**, **MX**, **TXT**, **SRV**, and **sibling** (a related name). **Authoritative DNS** means the records the zone publishes, not a Zeek log of who looked up a name on the wire. **RNAME** is the responsible mailbox written as a DNS name. Do not collapse MNAME onto `hostmaster.cdn-test.net` — that string is the RNAME. The given uses course-fiction names (`login-prd.net`, `cdn-test.net`, `203.0.113.88`). Do not turn it into the intro plot.

**Key Teaching Points:**
- SOA is MNAME (primary nameserver), RNAME (operator mailbox), and serial (a change counter, not a hash).
- NS, MX, TXT, and SRV show who else is tied to the zone, not a full mail class.
- Same NS plus same A can be a sibling. A shared `/24` is not theirs.

**Common Student Challenges:**
- Treat this lesson as a Zeek `dns` log. Why: both mention DNS. Example: writing `id.orig_h` or `qtype_name` from an SOA instead of MNAME / RNAME / serial.
- Treat the serial as a file hash. Why: it is a number next to a domain. Example: “the zone hash is the SOA serial.”
- Claim the whole prefix from one A. Why: the address sits in that `/24`. Example: “all of `203.0.113.0/24` is theirs.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.6.1 – Advanced DNS concepts (SOA and other records of intel value)
- T: 2.6.1.1 – Interpret an SOA record and use advanced DNS data to enrich or pivot

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Who runs the zone; not a Zeek log |
| Key Concepts            | 14 min    | SOA fields; other records; sibling vs `/24` |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~23 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert or an RFI names a domain, and you have to say who runs that zone before you enrich or pivot.
- Write SOA as three fields. MNAME is the primary nameserver. RNAME is the mailbox (`hostmaster.cdn-test.net` means `hostmaster` at `cdn-test.net`). Serial is a zone-change counter. Do not call the serial a hash. Do not call the RNAME a country.
- Walk NS, MX, TXT, and SRV as “who else is tied to this zone.” Stop. This is not an MX or SPF class.
- Walk the given: RNAME `hostmaster.cdn-test.net` is who runs the zone. Sibling `login-prd.net` with the same NS pair and same A `203.0.113.88` is a related name. Reject the whole `203.0.113.0/24`.
- If they open a Zeek `dns` log: that is 1.2.3. This lesson is the published zone, not who asked for a name on the wire.
- If they re-query RDAP for registrar and created date: 2.5 is done. Use the NS pair you already have.
- If they write a hop sentence with four slots: that product is 2.8.1. Today is the DNS facts that feed it.

---

## Knowledge Check – Answer Key

1. **The SOA serial is a file hash. True or false?**  
   **Answer:** False. The serial is a zone-change counter. Operators raise it when zone data changes.  
   **Explanation:** A hash identifies file bytes. The SOA serial only tells you the zone was updated. It is not SHA256 and not “the zone’s hash.”

2. **What two SOA fields do you read first, and what does each one mean?**  
   **Answer:** **MNAME** is the primary nameserver. **RNAME** is the responsible mailbox, written as a DNS name. Serial is also on the record; it is not a hash.  
   **Explanation:** For this lesson’s given, RNAME `hostmaster.cdn-test.net` means `hostmaster` at `cdn-test.net`. That is who runs the zone, not a country. Do not treat `hostmaster.cdn-test.net` as the MNAME.

3. **Same NS + same A on `login-prd.net` — what can you say, and what must you not say about `203.0.113.0/24`?**  
   **Answer:** You can say related name / sibling — same NS pair and same A `203.0.113.88`. You must not say the whole Example Cloud prefix `203.0.113.0/24` is theirs.  
   **Explanation:** Shared hosting is not ownership. One address in a cloud `/24` is not the prefix.

---

## Additional Instructor Resources

- Next: 2.7.1 ATT&CK for CTI
