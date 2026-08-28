# Instructor Guide – Module 2.8.3 – IOC Handling and Enrichment Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.3 B / C / C ; 2.8.3.1 3c / 4c / 4d ; 2.8.3.2 3c / 4c / 4d  
- Hunter: 2.8.3 B / C / C ; 2.8.3.1 3c / 4c / 4d ; 2.8.3.2 1a / 2b / 3c  
- SOC: 2.8.3 A / B / B ; 2.8.3.1 1a / 2b / 3c ; 2.8.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Handle the IOC as an object: keep, expire, enrich, or link. Same activity set only on shared objects. A vendor name is not a link.

**Context (plain language):**

- What this lesson is for: CTI analysts handle observables as objects they keep, expire, enrich, or link, so the shop does not store junk or treat a behavior as if it were an object.
- How it hooks to the lesson before: 2.8.2 was which TTPs apply here — behaviors, not objects.
- How it hooks to the lesson after: 2.8.4 is the “so what here” line — relevance and impact, not handling.
- Why we are doing it this way: the object on the desk is a different job from TTP extract and from impact. Tools are already taught; this lesson names the lookup and records it.
- What we are *not* doing in this lesson: TTP extract. VirusTotal Relations depth. Actor profile. Hop-sentence rewrite. No lab.
- Extra step: none.

Use the same names as the student guide: **IOC**, **TTP**, **keep**, **expire**, **enrich**, **link**, and **activity set**. **TIP** is the internal threat intelligence platform. **NS** is nameserver. **A record** is the IPv4 address the name resolves to. **PRD APT** is a vendor label, not a shared object. **Expire** covers reject: stale, uncited, or shared-infrastructure noise.

**Key Teaching Points:**
- An IOC is an observable. A TTP is a behavior.
- Keep cited current IOCs. Expire a whole `/24` as shared-infrastructure noise.
- Enrichment names the tool, the field, and what you hope to learn. It does not re-teach the tool.
- Same activity set only if you can cite shared objects. A vendor group name is not a link.

**Common Student Challenges:**
- Treat an IOC as a TTP. Why: reports mix hashes and techniques in one page. Example: writing T1059.001 when the object on the desk is the hash of `invoice.vbs`.
- Keep a whole `/24` because one listed IP sits in it. Why: the range looks like “their” network. Example: keeping `203.0.113.0/24` because `203.0.113.88` is cited.
- Link on a vendor name. Why: the PDF used one APT label on two IOCs. Example: “same set because both are PRD APT.”

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.8.3 – IOC handling and enrichment concepts
- T: 2.8.3.1 – Enrich and pivot on IOCs using internal and external tools
- T: 2.8.3.2 – Link analysis and campaign tracking

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Object, not TTP |
| Key Concepts            | 12 min    | Keep/expire; enrich line; link |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an observable landed on the desk, and you have to keep it, expire it, enrich it, or link it.
- Write IOC versus TTP. Stop. A hash is not a technique.
- Walk keep versus expire on the update domain / `203.0.113.88` versus the whole `203.0.113.0/24`.
- Walk the enrich line: hash of `invoice.vbs` → TIP first, then VirusTotal if still needed. Tool, field, what you hope to learn. Do not open Relations.
- Walk the sibling link: update domain + `login-prd.net` share a nameserver pair and the same A record — one activity set. Fail the “PRD APT” link.
- If they start listing ATT&CK IDs: that is 2.8.2. This lesson is the object.
- If they open the VirusTotal Relations tab: that is 2.9.1.
- If they write an impact sentence: that is 2.8.4.
- If they fill Adversary with “PRD APT”: that is 2.7.2, and it is still not a link here.

---

## Knowledge Check – Answer Key

1. **An IOC is the same thing as a TTP. True or false?**  
   **Answer:** False. An IOC is an observable you record, enrich, or expire. A TTP is a behavior.  
   **Explanation:** A hash, IP, or domain is an object. Encoded PowerShell is a behavior. They are not the same kind of thing.

2. **Do you keep or expire a whole `/24` that contains one bad IP?**  
   **Answer:** **Expire** it as shared-infrastructure noise.  
   **Explanation:** `203.0.113.0/24` is Example Cloud shared hosting. You may keep the cited current host `203.0.113.88`. The range is not a cited current IOC.

3. **Update domain + sibling that share a nameserver — same activity set or apart? Why is “PRD APT” not a link?**  
   **Answer:** **Same activity set** — cite the shared nameserver pair and the same A record. “PRD APT” is a vendor label, not a shared object.  
   **Explanation:** `login-prd.net` links because of objects you can point at (NS / A). A PDF group name with no shared object is not campaign tracking.

---

## Additional Instructor Resources

- Next: 2.8.4 Relevance and impact
