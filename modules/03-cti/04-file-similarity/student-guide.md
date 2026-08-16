# Module 3.4.1 – Hashing and Similarity Concepts

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.4.1 A / A / B · 3.4.1.1 1a / 1a / 2b · 3.4.1.2 1a / 1a / 2b  
- Hunter: 3.4.1 A / B / B · 3.4.1.1 1a / 2b / 3c · 3.4.1.2 1a / 2b / 3c  
- CTI: 3.4.1 B / C / C · 3.4.1.1 3c / 4c / 4d · 3.4.1.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the **purpose and use case** of **imphash**, **ssdeep**, and **TLSH**.
2. **Use** those similarity hashes to say whether two samples are related (and which hash decided it).
3. **Extract and interpret** code-signing / certificate fields from a file.

**Mapped Proficiency Items:**
- K: 3.4.1 – Hashing and similarity concepts (imphash, ssdeep, TLSH, code-signing certificates)
- T: 3.4.1.1 – Use file similarity hashes to identify related samples
- T: 3.4.1.2 – Extract and interpret certificate / code-signing information from a file

---

## 1. Key Concepts

**SHA256 / MD5** answer “is this the *same bytes*?” (**1.2.7** files log). This hour is **related, not identical** — plus **who signed it**. VirusTotal may *display* these values (**3.3.2**); you still have to **interpret** them.

**Similarity hashes (outline a–c):**

| Hash | What it summarizes | Use when | Do not treat as |
|------|--------------------|----------|-----------------|
| **imphash** | PE **import table** (which APIs the binary asks for) | Same import set → possible same family, builder, or packer | Proof they are the same file (SHA256 does that). Useless on non-PE. Shared generic imports can collide |
| **ssdeep** | Fuzzy / piecewise file similarity | Two files look *mostly* the same after small edits | Identity. A **0** score is not “related.” Classroom: score **≥ 50** = similar enough to call related (stand-in) |
| **TLSH** | Another fuzzy / locality-sensitive digest | Same job as ssdeep; compare **TLSH to TLSH** | Mixing a TLSH distance with an ssdeep score as if they were the same scale |

**Classroom related-line:**  
`samples | which hash | related? | why | what you still do not know`

Same SHA256 → *identical*, not a similarity finding. Say that and stop.

**Certificates (outline d):**

| Field | What you read |
|-------|----------------|
| **Signed?** | Signed vs unsigned. Unsigned is common for malware *and* for some legit tools |
| **Subject / issuer** | Who claims to have signed; who issued the cert |
| **Serial / thumbprint** | Pivot value — same stolen cert on other samples |
| **Validity** | Not-before / not-after. Expired or not-yet-valid is a *fact*, not automatically malicious |
| **Chain / trust** | “Subject says Microsoft” is not trusted if the issuer is not a real Microsoft CA |

**Interpret-line:**  
`signed? | subject | issuer | validity | what it supports | what it does not`

| This lesson | Other |
|-------------|-------|
| Similarity + cert *meaning* | Where you *looked* it up (VT) — **3.3.2** |
| Not MD5/SHA as the whole story | **1.2.7** |
| Not Relations graphs | **3.9** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Same imphash, different SHA256 → related imports | SHA256 match called “ssdeep related” |
| ssdeep 12 → **not** related on the classroom card | Signed + “Microsoft” in subject → trusted |
| Expired self-signed → state the facts | Mixing TLSH “distance 30” with ssdeep 30 |

---

## 2. Detailed Walkthrough / Examples

**Classroom samples (Night Owl set):**

| ID | SHA256 (short) | imphash | ssdeep vs S1 | TLSH vs S1 | Cert |
|----|----------------|---------|--------------|------------|------|
| **S1** `update.exe` | `6734f374…` | `imph-A1` | — | — | Unsigned |
| **S2** | `aa11bb22…` | `imph-A1` | **72** | close | Unsigned |
| **S3** | `cc33dd44…` | `imph-B9` | **8** | far | Signed. Subject `Microsoft Windows`, issuer `CN=Harbor Test CA`, expired |
| **S4** | `6734f374…` | `imph-A1` | 100 | identical | Unsigned |

### Example 1: Same Imports, Different Bytes (Expected)

**S1 vs S2.** SHA256 differs. imphash **matches**. ssdeep **72** (≥ 50). TLSH close.

**Related?** **Yes** — same import table + fuzzy scores. Likely same family/builder.  
**Not:** identical files. You still need behavior (**3.3.2** AnyRun) if the PIR is “what does it do?”

### Example 2: SHA256 “Similarity” (Lead)

**Draft:** “S1 and S4 are ssdeep-related.”

**Fail.** Same SHA256 → they are the **same file**. That is identity, not a similarity pivot.  
**Lead:** Do not spend a 3.4.1.1 sentence on a duplicate hash.

### Example 3: Pretty Subject, Bad Trust (Lead)

**S3 cert:** Subject looks like Microsoft. Issuer is **Harbor Test CA**. Expired.

**Interpret:** Signed, **not** a trusted Microsoft chain. Subject string is decoration. Expired.  
**Related to S1?** imphash differs, ssdeep **8** → **not** related on similarity. The cert does not make it Night Owl *or* legit.  
**Lead:** “Signed” ≠ good. “Microsoft” in subject ≠ Microsoft issued it.

---

## 3. Hands-On Exercise

**Objective:** Call related vs not, and interpret a cert.

**Use the classroom table and ≥ 50 ssdeep rule.**

**Instructions:**

1. One sentence each for Examples 1–3: related/identity/cert.
2. **Similarity** (3.4.1.1): `samples | hash used | related? | why`.

   - A. S1 vs S2.  
   - B. S1 vs S3.  
   - C. S1 vs S4.

3. **Cert** (3.4.1.2): write the **interpret line** for S3, and for:

   - D. Signed. Subject `Harbor IT`, issuer `Harbor IT` (self-signed), valid dates cover today.  
   - E. Unsigned (S1).

4. Do not open a VT Relations graph. Do not treat MD5 as a similarity hash. Do not call D “trusted” just because it is valid today.
5. If two hashes disagree (imphash match, ssdeep 8), **say both** and do not force a single yes.

**Expected Outcome:**
- Three example summaries
- Three related-lines
- Two cert interpret-lines (S3 + D; E is unsigned)
- No 3.9 graph, no AnyRun detonation

---

## 4. Knowledge Check

1. What question does **imphash** answer that **SHA256** does not?
2. When is **ssdeep** the right hash, and what does classroom **≥ 50** mean?
3. Why must you compare **TLSH to TLSH**, not to an ssdeep score?
4. Why is a file with subject `Microsoft Windows` not automatically trusted?
5. Where do you go if you need **behavior** of `update.exe`, not similarity?

---

## 5. Summary

- imphash = imports. ssdeep / TLSH = fuzzy similarity. SHA256 = identity.
- Related ≠ identical. Signed ≠ trusted.
- Next: **3.5** RDAP / WHOIS.

---

## 6. References & Further Reading

- Related modules:
  - 3.3.2 – External tools (previous)
  - 1.2.7 – Files engine (MD5/SHA identity)
  - 3.9 – VT Relations / Behavior
  - 3.5.1 – RDAP / WHOIS (next)
- Local malware-analysis SOP (optional — ssdeep threshold / cert store names)
