# Todo

Do these first (course order and story):

- [x] Put section 0 (How a SOC can operate) in the training outline
- [x] Write the section 0 intro lesson: what a SOC is, how it can run, the jobs, and where they lightly overlap (one-sentence hand-offs; no fake DYA ticket system)
- [x] Write 0.1 What a SOC is (first small review cycle)
- [x] Write 0.2 Jobs in one sentence (first after 0.1; path is now 0.3)
- [x] Write 0.3 How work can move (after 0.2 is reviewed)
- [x] Write 0.4 Where the jobs lightly overlap (after 0.3 is reviewed)
- [x] Write 0.5 How this course is laid out (after 0.4 is reviewed; DYA / PRD highlighted)
- [ ] Teach in this order (lesson IDs can stay as they are): intro → SOC analyst → CTI → hunting → detection engineers
- [ ] Keep detections before alerts inside the SOC analyst block (current 1.3 then 1.4)
- [x] Add a detection-engineers section after the threat hunters section (outline 4.x; matrix/lessons later)
- [x] Write 4.x stay-in-lesson notes in generate-module.md
- [x] Write 4.1 What DE owns (first DE review cycle)
- [x] Write 4.2 Making a detection sound and meeting shop requirements
- [x] Write 4.3 Nominations from SOC, hunt, and CTI
- [x] Write 4.4 Tune requests from SOC
- [ ] Put the full incident flow in the companion story: SOC alert → triage → IR + leadership notify → RFI to intel → hunt package, block list to firewall/IA, and a request to write detections. Firewall/IA is a hand-off, not a new course unless we decide we want that track.
- [ ] As we review and revise the outline, make the outline follow that same flow, so the companion story is a re-read of the outline as one combined story

Then:

- [x] Explore a fictional back story — an ongoing theme, like the Night Owl story and Harbor company already in the lessons
- [x] Review for chances to re-order things
- [ ] Keep [docs/story-bible.md](story-bible.md) current as training develops
- [ ] Decide leftover Harbor map items that do not fit a law firm (OT, payroll)
- [ ] Rename Night Owl → Pink River Dolphin (PRD) and Harbor → Dixon, Yamada, & Associates (DYA) in the lessons
- [ ] Write the companion story (see the outline below)
- [ ] Review for chances to combine content (for example, ATT&CK in every role — one frameworks section up front, with role-specific parts underneath)
- [ ] Review everything and make sure it makes sense
- [ ] Check the reference links that are already there
- [ ] Look for places to add more reference links

## Companion story outline (for later)

Saved here so we do not lose the flow. Use [docs/story-bible.md](story-bible.md) for names and facts (PRD, DYA, `jlee`, `WS-JLEE`). Do not invent hunt tickets, PIR lists, or approval chains.

When we revise the training outline, it should follow this same sequence. The companion story comes after the outline. It should feel like reading the outline again, but as one combined story — not a different plot.

1. A SOC analyst gets an alert.
2. They triage it.
3. They forward it to incident response and do their leadership notifications.
4. They RFI the CTI team for more work on that alert.
5. The CTI analyst works the RFI.
6. While doing that, they enrich it and find more adversary infrastructure.
7. That extra infrastructure goes to a firewall or IA team to block / blacklist.
8. CTI also gives the hunt team a hunt package so they can look for more of the same activity.
9. The hunt package also goes to detection engineers so they can write the right rules (MDE, YARA, Suricata, SIGMA, and so on).
