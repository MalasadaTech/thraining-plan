# Module 2.4.1 – Hashing and Similarity Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.1 B / C / C ; 2.4.1.1 3c / 4c / 4d ; 2.4.1.2 3c / 4c / 4c  
- Hunter: 2.4.1 A / B / B ; 2.4.1.1 1a / 2b / 3c ; 2.4.1.2 1a / 2b / 3c  
- SOC: 2.4.1 A / A / B ; 2.4.1.1 1a / 1a / 2b ; 2.4.1.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what **imphash**, **ssdeep**, and **TLSH** are for, and use a similarity hash to name a related sample.
2. Extract and interpret **code-signing** fields from a file.

**Mapped Proficiency Items:**
- K: 2.4.1 – Hashing and similarity concepts
- T: 2.4.1.1 – Use file similarity hashes to identify related samples
- T: 2.4.1.2 – Extract and interpret certificate / code-signing information from a file

---

## 1. Key Concepts

A sample usually arrives as a file or a hash. **SHA256** tells you that exact file. A one-byte change makes MD5 / SHA look brand new. CTI still has to find a **cousin** of `update.exe` and say **who claimed the binary**. That is the job in this lesson: use a similarity hash to name a related sample, and read the code-signing fields. Cryptographic identity hashes (MD5 / SHA) are **1.2.7**. VirusTotal Relations is **2.9**. Classroom match thresholds are stand-ins, not shop policy.

| Tool | What it captures | What a match means |
|------|------------------|--------------------|
| **imphash** | The PE import table — which Windows libraries and functions the file lists. PE files only. | Same imphash → related compile or packer family. Not the same file. |
| **ssdeep** | A fuzzy digest of the file bytes. Score 0–100; **higher** is closer. | Near-duplicate when a few bytes change. |
| **TLSH** | A locality-sensitive digest of the file bytes. Distance; **lower** is closer. | Another fuzzy cousin. Do not read the number like ssdeep. |
| **Code-signing** | Signer, issuer, validity dates — or **unsigned**. | Who claimed the binary. Unsigned is a fact, not malware and not a country. |

**imphash** does not hash the whole file. Two files can share an imphash and still have different SHA256 values. Packed binaries often share the packer's import table, so the same imphash can mean the same packer, not the same family.

**ssdeep** and **TLSH** both look at bytes, not the import table. They score in **opposite** directions: a high ssdeep score is close; a low TLSH distance is close. This classroom treats **ssdeep 50 or higher** and **TLSH distance 30 or lower** as related. Those numbers are stand-ins. A weak ssdeep score is **not related** unless your shop card says otherwise. Do not invent a 90% cutoff as policy.

**Code-signing** is the signature **on the file**, not a TLS certificate (**1.2.4**). Extract signer, issuer, and valid dates as separate facts — do not swap issuer for signer. Empty signing fields means **unsigned**. Signed is not “trusted.” Unsigned is not “malware” and is not nation-state (**2.1.7**).

**What good looks like:**

- **Related sample:** given two PE files, same **imphash** as `update.exe`, different SHA256 → related compile (or packer family). Not the same file. Given ssdeep **20** against `update.exe` → **not related** on the classroom card.
- **Certificate:** extract signer / issuer / valid dates (or **unsigned**). Do not upgrade “unsigned” to nation-state (**2.1.7**).

Do not treat a SHA256 miss as “no cousin.” Do not open a Relations graph (**2.9**).

---

## 2. Knowledge Check

1. Same imphash means the two files are byte-identical. True or false?
2. What does ssdeep (or TLSH) find that SHA256 does not?
3. You extract “unsigned” from `update.exe`. What did you learn, and what must you **not** claim?

---

## 3. Summary

Similarity finds cousins when SHA256 does not match. imphash is the PE import table, not the whole file. ssdeep scores high when close; TLSH distance is low when close. Code-signing is who claimed the file. Unsigned is a fact, not attribution.

**Next:** **2.5.1** RDAP / WHOIS.

---

## 4. Related modules

- 2.3.1 – Internal TIP (previous)
- 2.5.1 – RDAP / WHOIS
- 1.2.7 – MD5 / SHA (identity hashes, not this lesson)
- 2.9 – VirusTotal Relations
- 2.1.7 – Attribution
