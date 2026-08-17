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
- T: 2.4.1.2 – Extract and interpret certificate / code-signing information

---

## 1. Key Concepts

CTI analysts use **similarity** so they can find a cousin of `update.exe` without needing an identical SHA256. Cryptographic identity hashes (MD5 / SHA) are **1.2.7**. VT Relations is **2.9**. Classroom match thresholds are stand-ins, not shop policy.

| Hash | What it captures | Use |
|------|------------------|-----|
| **imphash** | PE import table | Related compile / packer family — not “same file” |
| **ssdeep** | Fuzzy bytes | Near-duplicate when a few bytes change |
| **TLSH** | Locality-sensitive digest | Another fuzzy cousin; compare scores, do not invent a cutoff as policy |
| **Code-signing** | Signer, issuer, validity | Who claimed the binary; unsigned is a fact, not proof of malware |

**What good looks like:**

- **Related sample:** given two PE rows, same **imphash** as `update.exe` → related compile. Not the same SHA256. A weak ssdeep score is **not related** unless your shop card says otherwise.
- **Certificate:** extract signer / issuer / valid dates (or **unsigned**). Do not upgrade “unsigned” to nation-state (**2.1.7**).

---

## 2. Knowledge Check

1. Same imphash means the two files are byte-identical. True or false?
2. What does ssdeep (or TLSH) find that SHA256 does not?
3. You extract “unsigned” from `update.exe`. What did you learn, and what must you **not** claim?

---

## 3. Summary

Similarity finds cousins. Code-signing is who claimed the file. Unsigned is a fact, not attribution.

**Next:** **2.5.1** RDAP / WHOIS.

---

## 4. Related modules

- 2.3.1 – Internal TIP (previous)
- 2.5.1 – RDAP / WHOIS
- 1.2.7 – MD5 / SHA (identity, not this hour)
- 2.9 – VT Relations
