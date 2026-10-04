# Module 2.5.5 – Identifying Additional Adversary Infrastructure  
## Slide Deck Content

**Total Suggested Slides:** 8

### Slide 1 – Title
**Title:** Infrastructure Pivoting  
**Subtitle:** Turn a seed into a defensible candidate

### Slide 2 – Seed → candidate
A **seed** is already connected to the intelligence problem.

A **pivot** uses a shared characteristic to find a **candidate**.

Candidate does not mean confirmed ownership.

### Slide 3 – Hop sentence
`seed | shared characteristic | candidate | why worth pursuing`

Keep the reasoning beside the pivot.

### Slide 4 – Distinctiveness
Weak:
- public DNS provider
- shared cloud IP
- common issuer
- generic title

Stronger:
- rare NS pair
- uncommon certificate feature
- multiple independent overlaps

### Slide 5 – A12 example
Update domain  
→ uncommon `ns1/ns2.cdn-test.net`  
→ `login-prd.net`

Add same observed A address → stronger candidate.

### Slide 6 – Reject the range expansion
One bad IP inside `203.0.113.0/24` does not make the entire `/24` adversary-owned.

### Slide 7 – Name the next test
NS → other domains + registration timing  
IP → historical DNS / hosting density  
Certificate → SAN/fingerprint reuse  
HTTP → title/resource distinctiveness

### Slide 8 – Knowledge Check
1. Four hop fields?  
2. Same public DNS provider: enough?  
3. Why is uncommon NS + same A stronger than same `/24`?


**Reference:** [DTF](https://github.com/MalasadaTech/defenders-threatmesh-framework)

**Next:** [2.5.6 – MalasadaTech Defender's ThreatMesh Framework (DTF)](../06-dtf/student-guide.md).
