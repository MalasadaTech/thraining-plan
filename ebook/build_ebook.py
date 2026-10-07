#!/usr/bin/env python3
"""Build a derived Markdown book. Reads source files; never writes to them.

Usage: python3 build_ebook.py --source-root ../ --inventory inventory.json
The source root must contain modules/ and docs/. Outputs sit beside this script.
"""
import argparse
import collections
import hashlib
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit

OUT = Path(__file__).resolve().parent
LINK = re.compile(r'(?<!!)\[([^\]\n]+)\]\(([^\s)]+)\)')
FENCE = re.compile(r'^\s*(`{3,}|~{3,})')
PARTS = [
    ('I', 'Shared Foundations', '00-intro'),
    ('II', 'SOC Analyst', '01-soc'),
    ('III', 'Cyber Threat Intelligence', '02-cti'),
    ('IV', 'Threat Hunting', '03-hunter'),
    ('V', 'Detection Engineering', '04-de'),
    ('VI', 'Course Conclusion', 'course-summary'),
]
PART_INTROS = [
    'Begin with the work the four defensive roles share: understanding the environment, recognizing evidence, and handing useful products to the next analyst. These foundations give the later technical lessons a common purpose.',
    'The shared foundations now become an investigation. Read endpoint and network records closely, work out what an alert actually detected, and communicate a finding another analyst can use. Keep the observation separate from the conclusion as the evidence develops.',
    'An investigation often leaves a question that additional collection and analysis can answer. CTI begins with that requirement, then develops an assessment whose reasoning and limitations remain visible. The sequence is **Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**. The eight units below follow the current course organization.',
    'An assessment can suggest behavior worth searching for beyond the original incident. Hunting turns that lead into a bounded question, tests it against available telemetry, and produces a finding with a clear handoff. Follow **Question → Hypothesis → Evidence → Refine → Finding → Handoff**.',
    'Investigation and hunting can reveal a need for better coverage. Detection Engineering evaluates that need and maintains the resulting capability through **Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**. The decision may be to change existing coverage, add coverage, or explain why no new rule is justified.',
    'Bring the role-specific work back together. The final chapter traces how an observation becomes an assessment, a search, and a coverage decision—and how those decisions shape the next observation.',
]
GLOSSARY = [
    ('Activity set', 'A grouping of activity supported by assessed connections. Shared infrastructure can suggest a candidate relationship before it supports this grouping.', '2.5.7'),
    ('Admiralty Code', 'A notation that evaluates source reliability separately from the credibility of the information it provides.', '2.2.3'),
    ('Alert', 'A detection-generated item for investigation. The match identifies the rule’s condition; the investigation establishes what that activity means.', '1.4.1'),
    ('Applicability', 'Whether a reported behavior could operate against the organization’s technology or environment.', '2.6.1'),
    ('Attribution', 'An assessment connecting activity to an actor or responsible entity, with the supporting evidence and uncertainty stated.', '2.1.8'),
    ('Candidate relationship', 'A connection worth testing through further evidence. A shared characteristic alone does not establish common control or malicious activity.', '2.5.5'),
    ('Collection', 'Obtaining information from selected sources to answer an intelligence requirement, while preserving provenance and limitations.', '2.1.9'),
    ('Confidence', 'A judgment about the strength of the evidence and reasoning supporting an assessment. It is distinct from the likelihood of the assessed proposition.', '2.2.1'),
    ('Correlation', 'Comparing observations and relationships in context to determine which connections the evidence supports.', '2.5.7'),
    ('Data', 'Recorded observations or values before sufficient context has been added to explain their relevance.', '2.1.1'),
    ('Detection nomination', 'A proposed detection need with an evidence pointer that DE can evaluate and develop.', '4.3'),
    ('Detection lifecycle', 'The work of deciding on coverage, building or changing it, validating, deploying, monitoring, and improving or retiring it.', '4.6'),
    ('Diamond Model', 'A framework connecting adversary, capability, infrastructure, and victim within the evidence available for an event.', '2.3.2'),
    ('Dissemination', 'Delivering intelligence to the appropriate recipients through approved channels with its handling requirements and context intact.', '2.7.5'),
    ('Enrichment', 'Adding context and relationships to a seed to answer a defined question, rather than accumulating unrelated tool results.', '2.5.1'),
    ('Estimative language', 'Words used to express the assessed likelihood of a proposition while keeping that likelihood distinct from confidence.', '2.2.1'),
    ('Evidence boundary', 'The limit of what the available observation establishes. A further conclusion needs additional evidence or an explicitly qualified assessment.', '2.1.1'),
    ('False negative', 'Malicious or unauthorized activity that should have been detected under an established expectation but was missed; the classification needs supporting evidence.', '1.4.2'),
    ('False positive', 'An alert assessed as firing on benign or authorized activity rather than the malicious or unauthorized condition under investigation.', '1.4.2'),
    ('Finished intelligence', 'An assessed product organized for a recipient’s decision, with reasoning, evidence, uncertainty, and relevant implications.', '2.7.3'),
    ('Handoff', 'Passing a usable product to its next owner, including evidence, scope, uncertainty, and the action or decision needed.', '0.4'),
    ('Hash', 'A value used to identify or compare file content. An exact hash match and a similarity result answer different questions.', '2.5.2'),
    ('Hunt hypothesis', 'A testable expectation about activity and the evidence that should be observable within a defined scope.', '3.2.2'),
    ('Impact', 'The organizational consequence if the assessed activity affects relevant assets or operations.', '2.6.2'),
    ('Information', 'Observations connected with context so they describe a meaningful situation.', '2.1.1'),
    ('Intelligence', 'An evaluation of information that answers a relevant question and explains the evidence’s significance for a decision.', '2.1.1'),
    ('Intelligence requirement', 'A defined question or information need that directs collection and analysis toward a decision.', '2.1.4'),
    ('IOC handling', 'Managing indicators through their usefulness, evidence, relationships, and lifecycle, including keeping, linking, rejecting, or expiring them as appropriate.', '2.5.1'),
    ('Likelihood', 'How probable the analyst assesses a proposition to be, expressed separately from confidence in that assessment.', '2.2.1'),
    ('Pivot', 'Using a seed’s characteristic to discover another candidate object and recording why that relationship is worth pursuing.', '2.5.5'),
    ('Procedure', 'The specific implementation or pattern of behavior that makes a technique observable and a hunt selective.', '3.6.3'),
    ('Provenance', 'The source and context needed to trace an observation, including the object or report and relevant time.', '2.4.2'),
    ('Relevance', 'Why a threat finding matters to this organization given its assets, exposure, and circumstances.', '2.6.2'),
    ('RFI intake', 'Receiving and evaluating a question, clarifying the decision and scope, and assigning ownership and priority.', '2.1.5'),
    ('RFI closure', 'Providing a usable answer with reasoning and limitations, delivering it to the requester, and recording the response and follow-up status.', '2.7.4'),
    ('Sandbox observation', 'Behavior recorded during a particular controlled execution. It does not automatically establish behavior in the local environment.', '2.4.4'),
    ('Seed', 'The known starting object for an enrichment or infrastructure-discovery question.', '2.5.5'),
    ('Sensor visibility', 'What a sensor and its placement, configuration, and available fields can observe within the relevant scope.', '4.7'),
    ('Structured analytic technique', 'A repeatable way to organize reasoning, expose assumptions, or compare alternatives.', '2.2.2'),
    ('Threat hunting', 'A bounded, evidence-driven search that tests a question beyond the work owed by an existing alert investigation.', '3.1'),
    ('True positive', 'An alert supported by evidence of the malicious or unauthorized condition being evaluated, not merely by a successful rule match.', '1.4.2'),
    ('Tune request', 'A request to change an existing detection, supported by evidence of its current behavior and the desired improvement.', '4.4'),
    ('Visibility gap', 'A limit in available telemetry that prevents the intended observation; it is distinct from a detection missing activity it could observe.', '3.1'),
]

# Definitions refer to course usage; names that are not expanded by the course
# are identified as names rather than given invented acronym expansions.
ACRONYMS = [
    ('ACH', 'Analysis of Competing Hypotheses', '2.2.2'),
    ('AS', 'Autonomous system; an IP-infrastructure pivot context', '2.5.6'),
    ('API', 'Application programming interface; used here for platform access and exchange', '2.7.2'),
    ('APT', 'Advanced persistent threat; an actor label still requires evidence', '2.1.8'),
    ('ATT&CK', 'MITRE’s adversary-behavior knowledge base', '0.6.1'),
    ('CDN', 'Content delivery network; shared services affect infrastructure interpretation', '2.5.5'),
    ('CTI', 'Cyber Threat Intelligence', '2.0'),
    ('DE', 'Detection Engineering', '4.0'),
    ('DLL', 'Dynamic-link library; image-load and side-loading context', '1.1.6'),
    ('DNS', 'Domain Name System', '1.2.3'),
    ('DTF', 'Defender’s ThreatMesh Framework', '2.5.6'),
    ('DYA', 'Dixon, Yamada, & Associates; the fictional organization in A12', '0.8'),
    ('EDR', 'Endpoint detection and response', '4.2'),
    ('FN', 'False negative', '1.4.2'),
    ('FP', 'False positive', '1.4.2'),
    ('FQDN', 'Fully qualified domain name', '2.5.4'),
    ('FIRST', 'Publisher of the Traffic Light Protocol guidance cited by this course', '2.7.5'),
    ('HKCU', 'HKEY_CURRENT_USER; current-user registry hive', '1.1.5'),
    ('HKLM', 'HKEY_LOCAL_MACHINE; machine-wide registry hive', '1.1.5'),
    ('HKU', 'HKEY_USERS; registry hives by user security identifier', '1.1.5'),
    ('HTTP', 'Hypertext Transfer Protocol', '1.2.5'),
    ('HTTPS', 'HTTP protected by TLS', '1.2.4'),
    ('IA', 'Information Assurance; a blocking-owner example in A12', '0.3'),
    ('ICD', 'Intelligence Community Directive; used in references to ICD 203', '2.1.1'),
    ('ICANN', 'Organization cited for registration and RDAP transition guidance', '2.5.3'),
    ('IOC', 'Indicator of compromise', '2.5.1'),
    ('IP', 'Internet Protocol; addresses identify network endpoints in the examples', '1.1.4'),
    ('IR', 'Incident Response', '0.3'),
    ('JSON', 'JavaScript Object Notation; structured representation used in STIX examples', '2.7.2'),
    ('KQL', 'Kusto Query Language', '1.1.2'),
    ('MDE', 'Microsoft Defender for Endpoint', '1.1.2'),
    ('NIST', 'National Institute of Standards and Technology; source of incident-response references', '1.5.1'),
    ('NS', 'DNS nameserver record', '2.5.4'),
    ('ODNI', 'Office of the Director of National Intelligence; source of ICD 203', '2.1.1'),
    ('OASIS', 'Standards organization publishing the STIX and TAXII specifications cited here', '2.7.2'),
    ('OSINT', 'Open-source intelligence', '2.1.9'),
    ('OT', 'Operational technology', '2.6.2'),
    ('PCAP', 'Packet capture', '1.4.1'),
    ('PADNS', 'Passive DNS; the abbreviation used in the course’s Silent Push guide', '2.4.5'),
    ('PIR', 'Priority Intelligence Requirement', '2.1.4'),
    ('PRD', 'Pink River Dolphin; a vendor label in the fictional case, not proven attribution', '2.1.8'),
    ('PTA', 'Pivot Tactic in DTF', '2.5.6'),
    ('RDAP', 'Registration Data Access Protocol', '2.5.3'),
    ('RFI', 'Request for Information', '2.1.5'),
    ('RFC', 'Request for Comments; the technical documents cited for DNS and related protocols', '2.5.4'),
    ('RIR', 'Regional Internet Registry', '2.5.3'),
    ('SAN', 'Subject Alternative Name; certificate field used in infrastructure pivots', '2.5.6'),
    ('SCO', 'STIX Cyber-observable Object', '2.7.1'),
    ('SIEM', 'Security information and event management', '1.3.4'),
    ('SID', 'Security identifier in registry context; signature identifier in a Suricata rule', '1.1.5'),
    ('SLA', 'Service-level agreement; the course distinguishes different response clocks', '1.4.5'),
    ('SMTP', 'Simple Mail Transfer Protocol', '1.2.6'),
    ('SNI', 'Server Name Indication', '1.2.4'),
    ('SOA', 'Start of Authority; DNS record', '2.5.4'),
    ('SOC', 'Security Operations Center', '0.2'),
    ('SSL', 'Certificate-oriented label retained in DTF’s SSL pivot tactic; see the framework context', '2.5.6'),
    ('STIX', 'Structured Threat Information Expression', '2.7.1'),
    ('TAXII', 'Trusted Automated Exchange of Intelligence Information', '2.7.2'),
    ('TCP', 'Transmission Control Protocol', '1.2.2'),
    ('TIP', 'Threat Intelligence Platform', '2.4.1'),
    ('TLP', 'Traffic Light Protocol', '2.7.5'),
    ('TLS', 'Transport Layer Security', '1.2.4'),
    ('TN', 'True negative', '1.4.2'),
    ('TP', 'True positive', '1.4.2'),
    ('TTP', 'Tactics, techniques, and procedures', '2.6.1'),
    ('UAC', 'User Account Control', '3.6.2'),
    ('UID', 'Unique identifier; Zeek uses a connection uid to link related records', '1.2.1'),
    ('URI', 'Uniform Resource Identifier; used for the requested resource in HTTP records', '1.2.5'),
    ('URL', 'Uniform Resource Locator', '2.4.6'),
    ('VT', 'VirusTotal', '0.7'),
]

def slug(s):
    s = LINK.sub(lambda m: m[1], s).replace('`', '').replace('*', '').lower()
    return ''.join(c for c in s if c.isalnum() or c in '-_ ').replace(' ', '-')

def chapter_sort(n):
    return tuple(map(int, n.split('.'))) if n != 'conclusion' else (5,)

def strip_code(s):
    result=[]; fence=None
    for line in s.splitlines():
        m=FENCE.match(line)
        if m:
            if fence is None: fence=m[1][0]
            elif m[1][0]==fence: fence=None
            continue
        if fence is None: result.append(line)
    return '\n'.join(result)

def code_blocks(s):
    blocks=[]; buf=[]; fence=None
    for line in s.splitlines(keepends=True):
        m=FENCE.match(line)
        if fence is None and m:
            fence=m[1][0];buf=[line]
        elif fence is not None:
            buf.append(line)
            if m and m[1][0]==fence:blocks.append(''.join(buf));fence=None
    if fence is not None: raise ValueError('Unclosed code fence')
    return blocks

def external_links(s):
    return [(m[1],m[2]) for m in LINK.finditer(strip_code(s)) if m[2].startswith(('https://','http://'))]

def plain(s):
    s=LINK.sub(lambda m:m[1],s)
    s=re.sub(r'^#+\s+(?:\d+\.\s+)?','',s,flags=re.M)
    return re.sub(r'\s+',' ',s.replace('*','').replace('`','').replace('—','–')).strip()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,required=True)
    parser.add_argument('--inventory',type=Path)
    parser.add_argument('--date',default=date.today().isoformat())
    parser.add_argument('--snapshot-date', help='Date the canonical sources were retrieved; separate from build date')
    args=parser.parse_args()
    root=args.source_root.resolve()
    snapshot_label=args.snapshot_date or "not recorded"
    metadata={}
    if args.inventory:
        metadata={i['path']:i for i in json.loads(args.inventory.read_text())['items']}
    chapters=[]
    for p in root.glob('modules/**/student-guide.md'):
        raw=p.read_text(); first=raw.splitlines()[0]
        m=re.match(r'# Module (\d+(?:\.\d+)+)\s+[–—-]\s+(.+)',first)
        number,title=m.groups() if m else ('conclusion',first.removeprefix('# '))
        part=next(i for i,(_,_,folder) in enumerate(PARTS) if p.relative_to(root).parts[1]==folder)
        book_title=(number+' — '+title) if m else title
        chapters.append(dict(number=number,title=title,book_title=book_title,part=part,path=p,source='/thraining-plan/'+str(p.relative_to(root)),raw=raw,anchor=slug(book_title)))
    chapters.sort(key=lambda c:chapter_sort(c['number']))
    assert len(chapters)==108, f'Expected 108 lesson chapters, found {len(chapters)}; review manifest before changing expectation.'
    ids=[c['number'] for c in chapters]
    assert len(set(ids))==len(ids),'Duplicate chapter numbers'
    assert [sum(c['part']==i for c in chapters) for i in range(6)]==[12,28,41,16,10,1]
    part_titles=[f'Part {roman} — {name}' for roman,name,_ in PARTS]

    # Subunit advance-organizer / end-state wrappers are learner-facing synthesis,
    # but they do not add proficiency-mapped lesson IDs.
    wrappers=[]
    for kind in ('intro','summary'):
        for wp in root.glob(f'modules/*/*/{kind}.md'):
            raw=wp.read_text(); first=raw.splitlines()[0]
            m=re.match(r'# (\d+\.\d+)\s+[–—-]\s+(.+)',first)
            if not m: raise ValueError(f'Cannot parse wrapper heading: {wp}: {first}')
            unit,title=m.groups()
            part=next(i for i,(_,_,folder) in enumerate(PARTS) if wp.relative_to(root).parts[1]==folder)
            display=first.removeprefix('# ')
            wrappers.append(dict(unit=unit,kind=kind,title=title,display=display,part=part,path=wp,
                                 source='/thraining-plan/'+str(wp.relative_to(root)),raw=raw,anchor=slug(display)))
    wrappers.sort(key=lambda w:(w['part'],tuple(map(int,w['unit'].split('.'))),0 if w['kind']=='intro' else 1))
    assert len(wrappers)==36, f'Expected 36 subunit wrappers (18 intro + 18 summary), found {len(wrappers)}.'
    assert sum(w['kind']=='intro' for w in wrappers)==18 and sum(w['kind']=='summary' for w in wrappers)==18
    wrapper_by_unit={(w['part'],w['unit'],w['kind']):w for w in wrappers}
    assert len(wrapper_by_unit)==len(wrappers), 'Duplicate wrapper unit/kind'
    # A grouping with multiple direct child lessons needs one wrapper pair.
    grouped=collections.defaultdict(list)
    role_roots={root/'modules'/folder for _,_,folder in PARTS}
    for c in chapters:
        parent=c['path'].parent.parent
        if parent not in role_roots and parent!=root/'modules':grouped[parent].append(c)
    meaningful={folder:members for folder,members in grouped.items() if len(members)>1}
    assert {w['path'].parent for w in wrappers}==set(meaningful), 'Missing or unexpected wrapper grouping'
    for folder,members in meaningful.items():
        pair=[w for w in wrappers if w['path'].parent==folder]
        assert {w['kind'] for w in pair}=={'intro','summary'} and len(pair)==2, str(folder)
        assert len({w['unit'] for w in pair})==1, str(folder)
        assert all(c['number'].startswith(pair[0]['unit']+'.') for c in members), str(folder)
        assert all('no new proficiency mapping' in w['raw'] for w in pair), str(folder)


    byid={c['number']:c for c in chapters}

    # Learner practicals remain supporting content under their owning numbered lessons.
    # They do not create new proficiency-mapped chapter IDs, but the single-file ebook
    # embeds them and their small controlled lab assets so learner links remain usable.
    practical_specs=[
        ('3.2.1','modules/03-hunter/02-methodology/01-hunt-types/hunt-execution-practical.md',
         ['labs/hunt-execution-practical.csv']),
        ('3.3.1','modules/03-hunter/03-online-tools/external-tool-pivot-practical.md',[]),
        ('4.2','modules/04-de/02-sound-and-shop-requirements/detection-validation-practical.md',
         ['labs/de-validation-practical.csv','labs/de-validation-runner.py']),
    ]
    practicals=[]; embedded_assets=[]
    for parent_number,rel_path,asset_paths in practical_specs:
        pp=root/rel_path
        raw=pp.read_text(); first=raw.splitlines()[0]
        if not first.startswith('# '): raise ValueError(f'Cannot parse practical heading: {pp}: {first}')
        title=first[2:].strip(); parent=byid[parent_number]
        pobj=dict(parent_number=parent_number,title=title,part=parent['part'],path=pp,
                  source='/thraining-plan/'+str(pp.relative_to(root)),raw=raw,
                  anchor=slug(title),assets=[])
        for asset_rel in asset_paths:
            ap=root/asset_rel
            label='Lab Asset — '+ap.name
            aobj=dict(path=ap,source='/thraining-plan/'+str(ap.relative_to(root)),
                      label=label,anchor=slug(label),
                      raw=ap.read_text())
            pobj['assets'].append(aobj); embedded_assets.append(aobj)
        practicals.append(pobj)

    bypath={c['path']:c for c in chapters}
    bypath.update({w['path']:w for w in wrappers})
    bypath.update({x['path']:x for x in practicals})
    asset_by_path={x['path']:x for x in embedded_assets}
    aa='Appendix A — The Complete A12 Case Study';ab='Appendix B — Proficiency Mapping'
    audit=[]; link_edits=[]; unresolved=[]
    def ref(n,label=None):
        c=byid.get(n)
        if c is None:
            wrapper=next((w for w in wrappers if w['unit']==n and w['kind']=='intro'),None)
            if wrapper:return f'[{label or n}](#{wrapper["anchor"]})'
            candidates=[c for c in chapters if c['number'].startswith(n+'.')]
            if candidates:c=candidates[0]
        if c is None:
            candidates=[c for c in chapters if n.startswith(c['number']+'.')]
            if candidates:c=max(candidates,key=lambda c:len(c['number']))
        if c is None:
            m=re.fullmatch(r'([0-4])\.x',n)
            if m:return f'[{label or n}](#{slug(part_titles[int(m[1])])})'
            raise ValueError('Unknown module reference '+n)
        return f'[{label or n}](#{c["anchor"]})'
    def convert_links(s,p):
        def replace(m):
            label,url=m.groups()
            if url.startswith(('http://','https://','mailto:','#')):return m[0]
            target=(p.parent/unquote(url.split('#')[0])).resolve()
            if target in bypath:new='#'+bypath[target]['anchor']
            elif target in asset_by_path:new='#'+asset_by_path[target]['anchor']
            elif target.name=='README.md':
                candidates=[c for c in chapters if c['path'].is_relative_to(target.parent)]
                if not candidates:raise ValueError(f'No chapter for {url} in {p}')
                part=next((i for i,(_,_,f) in enumerate(PARTS) if target.parent==root/'modules'/f),None)
                wrapper=next((w for w in wrappers if w['path'].parent==target.parent and w['kind']=='intro'),None)
                new='#'+(slug(part_titles[part]) if part is not None else wrapper['anchor'] if wrapper else candidates[0]['anchor'])
            else:
                unresolved.append((str(p),url));return m[0]
            link_edits.append(dict(source=str(p.relative_to(root)),old=url,new=new))
            return f'[{label}]({new})'
        return LINK.sub(replace,s)
    def log(c,kind,text):audit.append(dict(chapter=c['number'],kind=kind,text=text))
    def edit(c,s,old,new,kind='editorial wording'):
        if old in s:
            affected=[l for l in s.splitlines() if old in l]
            log(c,kind,'\n'.join(affected) if affected else old);s=s.replace(old,new)
        return s
    def process(c):
        lines=c['raw'].splitlines(keepends=True)[1:]; keep=[]; mapping=[]; i=0
        while i<len(lines):
            l=lines[i]
            if re.match(r'^\*\*(Target Audience|Module Type):',l):
                mapping.append(l);log(c,'metadata moved to Appendix B',l);i+=1;continue
            if l.startswith('**Proficiency Focus:'):
                block=[l];i+=1
                while i<len(lines) and not lines[i].startswith('**Estimated Time:'):
                    block.append(lines[i]);i+=1
                mapping.extend(block);log(c,'mapping moved to Appendix B',''.join(block));continue
            if re.match(r'^(?:\*\*Mapped Proficiency Items?:\*\*|## Mapped Proficiency Items?)',l):
                block=[l];i+=1
                while i<len(lines) and not re.match(r'^## ',lines[i]):
                    block.append(lines[i]);i+=1
                assert all(not l.strip() or l.startswith('-') for l in block[1:]),c['source']
                mapping.extend(block);log(c,'mapping moved to Appendix B',''.join(block));continue
            if re.match(r'^(?:\*\*)?(?:Previous|Next):',l) or re.match(r'^\[[01]\.x module index\]',l):
                assert not any(url.startswith('http') for _,url in LINK.findall(l))
                log(c,'standalone navigation removed',l);i+=1;continue
            keep.append(l);i+=1
        body=''.join(keep)
        body=edit(c,body,'instructor-provided result','provided result')
        body=edit(c,body,'instructor-supplied static result','supplied static result')
        body=edit(c,body,'The goal of this summary is not to reteach each lesson.\n\nIt is to reconnect the pieces into one defensible hunt process.','This summary reconnects the pieces into one defensible hunt process.')
        body=edit(c,body,'The goal of this summary is not to reteach each lesson.\n\nIt is to reconnect the pieces into one maintained detection capability.','This summary reconnects the pieces into one maintained detection capability.')
        # Empty navigation sections contain no lesson prose.
        body=re.sub(r'^## Course Connections\s*(?=^## |\Z)','',body,flags=re.M)
        # Put the existing purpose before objectives where the source has both.
        purpose=re.search(r'^## (?:Why This Matters|Purpose)\n[\s\S]*?(?=^## |\Z)',body,re.M)
        obj=re.search(r'^## Learning Objectives\n',body,re.M)
        if purpose and obj and purpose.start()>obj.start():
            block=purpose[0];body=body[:purpose.start()]+body[purpose.end():]
            pos=body.index('## Learning Objectives');body=body[:pos]+block+'\n'+body[pos:]
            log(c,'purpose moved before learning objectives',block)
        output=[];inside=False;related=False
        for line in body.splitlines():
            if FENCE.match(line):inside=not inside;output.append(line);continue
            if inside:output.append(line);continue
            h=re.match(r'^(#+) (.*)',line)
            if h:
                level=len(h[1]); title=re.sub(r'^\d+\.\s+','',h[2])
                related=title in ('Related Modules','Course Connections')
                title={'Related Modules':'Related Reading','Course Connections':'Related Reading',
                       'Supporting Reference':'References and Further Reading','Supporting References':'References and Further Reading',
                       'A12 example':'A12 Case Study: Worked Example','A12 examples':'A12 Case Study: Worked Examples',
                       'A12 classroom example':'A12 Case Study: Classroom Example',
                       'Worked example':'Example','Knowledge check':'Knowledge Check'}.get(title,title)
                # Source's secondary H1 is a section, not a second book title.
                line='#'*min(6,max(2,level)+2)+' '+title
            elif related:
                m=re.match(r'^- (\d+(?:\.\d+)+)\s+[–—-]\s+(.+)',line)
                if m:
                    label=re.sub(r' \(previous\)$','',m[2])
                    if label!=m[2]:log(c,'navigation label simplified',line)
                    num=m[1]
                    if num=='2.7' and label=='Finished intelligence products':
                        log(c,'structural cross-reference corrected',line);num='2.7.3';label='Creating Finished Intelligence Products'
                    elif num=='2.4' and label.startswith('Platform enrichment'):
                        log(c,'structural cross-reference label updated',line);label='CTI Tools and Platforms'
                    line='- '+ref(num,num+' — '+label)
            output.append(line)
        body=convert_links('\n'.join(output),c['path'])
        body=re.sub(r'\n{3,}','\n\n',body).strip()
        c['mapping']=''.join(mapping).strip()
        c['body']=body
        assert code_blocks(c['raw'])==code_blocks(body),f'Code changed: {c["number"]}'
        assert collections.Counter(u for _,u in external_links(c['raw']))==collections.Counter(u for _,u in external_links(body)),f'External link occurrence changed: {c["number"]}'
        start=f'### {c["book_title"]}\n\n'
        return start+body+'\n'
    chapter_text={c['number']:process(c) for c in chapters}

    def process_practical(pobj):
        lines=pobj['raw'].splitlines()[1:]; output=[]; inside=False
        for line in lines:
            if FENCE.match(line): inside=not inside; output.append(line); continue
            if inside: output.append(line); continue
            h=re.match(r'^(#+) (.*)',line)
            if h:
                # Practical heading is H4 under the owning H3 chapter; source H2/H3
                # sections become H5/H6 so the numbered course hierarchy stays intact.
                line='#'*min(6,len(h[1])+3)+' '+h[2]
            output.append(line)
        body=convert_links('\n'.join(output),pobj['path'])
        body=re.sub(r'\n{3,}','\n\n',body).strip()
        rendered=f'#### {pobj["title"]}\n\n{body}\n'
        for asset in pobj['assets']:
            lang='csv' if asset['path'].suffix.lower()=='.csv' else 'python' if asset['path'].suffix.lower()=='.py' else 'text'
            rendered+=f'\n##### {asset["label"]}\n\nEmbedded from `{asset["source"]}` for this controlled practical.\n\n```{lang}\n{asset["raw"].rstrip()}\n```\n'
        pobj['body']=body
        assert all(block in rendered for block in code_blocks(pobj['raw'])), f'Practical code changed: {pobj["source"]}'
        assert collections.Counter(u for _,u in external_links(pobj['raw']))==collections.Counter(u for _,u in external_links(rendered)), f'Practical external link changed: {pobj["source"]}'
        return rendered

    practical_text={pobj['parent_number']:process_practical(pobj) for pobj in practicals}
    for parent_number,text in practical_text.items():
        chapter_text[parent_number]=chapter_text[parent_number].rstrip()+'\n\n'+text

    def process_wrapper(w):
        lines=w['raw'].splitlines(keepends=True)[1:]
        keep=[]; inside=False
        for line in lines:
            if re.match(r'^\*\*Module Type:',line):
                audit.append(dict(chapter=f"{w['unit']} {w['kind']}",kind='wrapper metadata removed',text=line))
                continue
            if re.match(r'^(?:\*\*)?(?:Previous|Next):',line):
                audit.append(dict(chapter=f"{w['unit']} {w['kind']}",kind='standalone navigation removed',text=line))
                continue
            keep.append(line)
        body=''.join(keep)
        output=[]
        for line in body.splitlines():
            if FENCE.match(line): inside=not inside; output.append(line); continue
            if inside: output.append(line); continue
            h=re.match(r'^(#+) (.*)',line)
            if h:
                level=len(h[1]); line='#'*min(6,max(2,level)+2)+' '+h[2]
            output.append(line)
        body=convert_links('\n'.join(output),w['path'])
        body=re.sub(r'\n{3,}','\n\n',body).strip()
        w['body']=body
        assert code_blocks(w['raw'])==code_blocks(body),f'Wrapper code changed: {w["source"]}'
        assert collections.Counter(u for _,u in external_links(w['raw']))==collections.Counter(u for _,u in external_links(body)),f'Wrapper external link changed: {w["source"]}'
        return f'### {w["display"]}\n\n{body}\n'
    wrapper_text={(w['part'],w['unit'],w['kind']):process_wrapper(w) for w in wrappers}

    def unit_of(number):
        if number=='conclusion': return None
        parts=number.split('.')
        return '.'.join(parts[:2]) if len(parts)>=2 else number

    part_sequence={}
    for i in range(6):
        seq=[]; intro_emitted=set(); part_ch=[c for c in chapters if c['part']==i]
        for idx,c in enumerate(part_ch):
            unit=unit_of(c['number']); key=(i,unit)
            if (i,unit,'intro') in wrapper_by_unit and key not in intro_emitted:
                seq.append(('wrapper',wrapper_by_unit[(i,unit,'intro')]))
                intro_emitted.add(key)
            seq.append(('chapter',c))
            next_unit=unit_of(part_ch[idx+1]['number']) if idx+1<len(part_ch) else None
            if (i,unit,'summary') in wrapper_by_unit and next_unit!=unit:
                seq.append(('wrapper',wrapper_by_unit[(i,unit,'summary')]))
        part_sequence[i]=seq
    reading_order=[(kind,obj) for i in range(6) for kind,obj in part_sequence[i]]
    assert len(reading_order)==len(chapters)+len(wrappers)
    assert len({obj['source'] for _,obj in reading_order})==len(reading_order)
    for folder,members in meaningful.items():
        start=next(i for i,(kind,obj) in enumerate(reading_order) if kind=='wrapper' and obj['path'].parent==folder and obj['kind']=='intro')
        end=next(i for i,(kind,obj) in enumerate(reading_order) if kind=='wrapper' and obj['path'].parent==folder and obj['kind']=='summary')
        actual=[obj['source'] for kind,obj in reading_order[start+1:end] if kind=='chapter']
        assert actual==[c['source'] for c in members], f'Incorrect wrapper order: {folder}'
        assert end-start-1==len(members), f'Unexpected content within {folder}'
    front=f'''# Defensive Cyber Operations

**SOC, Cyber Threat Intelligence, Threat Hunting, and Detection Engineering**

**MalasadaTech Training Plan – First Edition**  
**v0.2 Review Draft · Build date: {args.date}**  
Source snapshot date: {snapshot_label}.

Defensive work depends on more than recognizing a suspicious value. An analyst needs to explain what happened, decide which questions remain, and give the next person enough evidence to act. This book follows that work from shared foundations through SOC investigation, Cyber Threat Intelligence, Threat Hunting, and Detection Engineering.

The chapters combine technical examples with the decisions those examples support. You will read endpoint and network evidence, evaluate intelligence, develop scoped hunts, and consider how findings become maintained detection coverage.

## How to Use This Book

Read the shared foundations first, then follow the role tracks in order. Chapter numbers match the curriculum so you can return to a particular lesson during practice. The opening and closing chapters of each track provide orientation and integration. Multi-lesson subunits also include short advance-organizer introductions and end-state summaries so you can preview the structure before reading closely; the final course summary reconnects all four roles.

Use **Preview → Predict → Read → Confirm**: preview a subunit introduction and its end-state summary, predict how the lessons fit together, read the detail, then return to the summary to check your understanding.

At a worked example, pause before the explanation. Describe the observation in your own words, identify what remains unknown, and name the next useful question. Use the knowledge checks to test that reasoning. They are learner exercises; this manuscript does not add an instructor answer key.

Estimated times are retained from the course as planning guides. The CTI platform chapters use two passes: first retrieve and describe evidence, then return for interpretation during the relevant enrichment method. Their estimates cover both passes together. Use the example cards and records printed in the lessons where available. Controlled CSV/Python assets required by the embedded hunt and detection-validation practicals are included under their owning lessons. The external-platform pivot practical still requires approved live/public platform access or authorized training accounts; this book does not provide platform accounts.

Examples distinguish course facts from local operating requirements. Where a chapter asks for a local priority, approval path, sensor configuration, or response clock, obtain that information from the responsible organization. Classroom examples provide practice rather than an operating policy.

Callouts identify their purpose in plain language. **A12 Case Study** marks the recurring case; **Example** introduces a worked observation or decision; **Key Point**, **Evidence Boundary**, and **Remember** emphasize the reasoning to retain. **Knowledge Check** introduces questions for practice. Detailed role ratings and task mappings are collected in [Appendix B](#{slug(ab)}).

## The Course-Wide Learning Model

**Observe → Understand → Search → Improve Coverage → Observe Again**

The SOC investigates observed activity. CTI evaluates evidence against an intelligence requirement. Threat Hunting tests questions beyond the original alert. Detection Engineering decides how to improve and maintain coverage. Each role contributes a different product to the same defensive workflow.

> **Key Point:** Describe what the evidence shows first. Then decide what it means.

A useful product carries its observations, reasoning, scope, uncertainty, and next decision together. As you read, ask what another analyst could verify from the product and what they would still need to establish.

> **Evidence Boundary:** Keep an observed event separate from an assessment of its meaning. Explain the additional evidence needed for a stronger conclusion.

## Meet A12: The Recurring Case Study

A12 is a fictional incident at **Dixon, Yamada, & Associates (DYA)**, a law firm. Its recurring starting point is **WS-JLEE**, a workstation in Building C associated with the account **jlee**. Those names help you recognize the same case as the work moves between roles.

You will encounter the evidence progressively. The shared foundations introduce the environment and responsibilities; later chapters examine the case from the SOC, CTI, Threat Hunting, and Detection Engineering perspectives. Work with the evidence supplied for each exercise, and distinguish a proposed follow-up from an established finding.

> **A12 Case Study:** A12 is the recurring case study used throughout this book. You will encounter its evidence progressively as you move through SOC, CTI, Threat Hunting, and Detection Engineering. The complete case study is available in [Appendix A](#{slug(aa)}) after the main course.

## Contents
'''
    toc=[]
    for i,title in enumerate(part_titles):
        toc.append(f'- [{title}](#{slug(title)})')
        for typ,obj in part_sequence[i]:
            label=obj['display'] if typ=='wrapper' else obj['book_title']
            toc.append(f'  - [{label}](#{obj["anchor"]})')
    for title in [aa,ab,'Glossary','Acronyms and Technical Abbreviations','Consolidated References and Further Reading']:
        toc.append(f'- [{title}](#{slug(title)})')
    book=front+'\n'+'\n'.join(toc)+'\n\n'
    for i,title in enumerate(part_titles):
        book+=f'## {title}\n\n{PART_INTROS[i]}\n\n'
        if i in (1,2,3,4):book+=f'> **A12 Case Study:** Follow the evidence available at this stage of the case. The uninterrupted narrative appears in [Appendix A](#{slug(aa)}).\n\n'
        pieces=[]
        for typ,obj in part_sequence[i]:
            pieces.append(wrapper_text[(obj['part'],obj['unit'],obj['kind'])] if typ=='wrapper' else chapter_text[obj['number']])
        book+='\n'.join(pieces)+'\n'
    story_path=root/'docs/companion-story/story.md';story=story_path.read_text()
    narrative=convert_links(story,story_path)
    # Shift the standalone story's heading hierarchy beneath Appendix A.
    narrative=re.sub(r'^(#{1,6}) ',lambda m:'#'*min(6,len(m[1])+2)+' ',narrative,flags=re.M)
    narrative=re.sub(r'\n{3,}','\n\n',narrative).strip()
    book+=f'''## {aa}

Read this complete case after the main course to see how the same evidence moves between SOC, CTI, Threat Hunting, and Detection Engineering. The canonical narrative is reproduced here, with book navigation adapted from its source links.

{narrative}

'''
    legend_path=root/'docs/proficiency-legend.md';legend=legend_path.read_text()
    legend='\n'.join(legend.splitlines()[1:]).strip()
    legend=re.sub(r'^(#+) ',lambda m:'#'*(len(m[1])+1)+' ',legend,flags=re.M)
    book+=f'''## {ab}

These are the course’s existing proficiency requirements. Role ratings, task identifiers, and mapped knowledge and performance statements are retained from the student guides. The three ratings in a role entry correspond to the course’s 3-, 5-, and 7-level progression. The qualification rules below describe this curriculum’s model.

### Reading the Proficiency Codes

{legend}

### Chapter Mappings

'''
    for c in chapters:
        mapping=re.sub(r'^## Mapped Proficiency Items?', '**Mapped Proficiency Items:**',c['mapping'],flags=re.M)
        book+=f'#### Mapping — {c["book_title"]}\n\n{ref(c["number"],"Return to chapter")}\n\n{mapping}\n\n'
    book+='## Glossary\n\nDefinitions summarize how terms are used in this course. Follow the chapter link for the fuller explanation and evidence limits.\n\n'
    for term,definition,n in sorted(GLOSSARY):book+=f'**{term}.** {definition} See {ref(n)}.\n\n'
    book+='## Acronyms and Technical Abbreviations\n\nThis list covers the recurring operational vocabulary. Product and framework names retain the meaning used in the course; identifiers such as ATT&CK technique IDs and DTF pivot IDs are explained in their chapters.\n\n| Term | Course meaning | Chapter |\n|---|---|---|\n'
    for term,definition,n in sorted(ACRONYMS):book+=f'| {term} | {definition} | {ref(n)} |\n'
    book+=f'| CFETP | Career Field Education and Training Plan; the proficiency legend uses this style | [Appendix B](#{slug(ab)}) |\n| USAF | United States Air Force; named in the source proficiency-code legend | [Appendix B](#{slug(ab)}) |\n'
    book+='\n**Other technical notation.** DNS record labels (`A`, `AAAA`, `CNAME`, `MX`, `TXT`, `SRV`, `RNAME`, and `SERIAL`) are covered in '+ref('2.5.4')+'. File identifiers and similarity names (`MD5`, `SHA1`, `SHA256`, `ssdeep`, and `TLSH`) are covered in '+ref('2.5.2')+'. `JA3` is discussed with TLS evidence in '+ref('1.2.4')+'. Zeek `uid` and file identifiers are explained in '+ref('1.2.1')+' and '+ref('1.2.7')+'. Sigma and YARA are rule-language names; see '+ref('1.3.1')+' and '+ref('1.3.3')+'.\n\n'
    refs=collections.OrderedDict()
    reference_sources=[(c['raw'],c['number'],c['anchor']) for c in chapters]
    reference_sources += [(w['raw'],w['display'],w['anchor']) for w in wrappers]
    reference_sources += [(pobj['raw'],pobj['title'],pobj['anchor']) for pobj in practicals]
    reference_sources.append((story,'Appendix A',slug(aa)))
    for raw,label_used,anchor_used in reference_sources:
        for label,url in external_links(raw):
            entry=refs.setdefault(url,dict(label=label,uses=[]))
            use=(label_used,anchor_used)
            if use not in entry['uses']:entry['uses'].append(use)
    book+='## Consolidated References and Further Reading\n\nThe following list preserves the course’s linked sources, with one entry per exact URL and links back to the chapters that use it. Chapter-level references remain beside their explanations. URLs are reproduced from the curriculum; their live availability and current platform interfaces have not been independently revalidated for this Markdown edition.\n\n'
    groups=collections.defaultdict(list)
    for url,entry in refs.items():groups[urlsplit(url).netloc.lower().removeprefix('www.')].append((url,entry))
    for domain,entries in sorted(groups.items()):
        book+=f'### {domain}\n\n'
        for url,entry in entries:
            book+=f'- [{entry["label"]}]({url}) — used in '+', '.join(f'[{label}](#{anchor})' for label,anchor in entry['uses'])+'.\n'
        book+='\n'
    book=re.sub(r'\n{3,}','\n\n',book).rstrip()+'\n'
    # Validate the full assembly before replacing generated deliverables.

    # Independent structural checks and provenance, not a claim of external fact validation.
    clean=strip_code(book); headings=re.findall(r'^(#{1,6}) (.*)$',clean,re.M)
    counts=collections.Counter();anchors=set()
    for _,title in headings:
        base=slug(title);n=counts[base];counts[base]+=1
        anchors.add(base+('-'+str(n) if n else ''))
    broken=[u for _,u in LINK.findall(clean) if u.startswith('#') and unquote(u[1:]) not in anchors]
    assert not broken,broken
    assert not unresolved,unresolved
    assert sum(level=='#' for level,_ in headings)==1
    assert all(sum(title==c['book_title'] for _,title in headings)==1 for c in chapters)
    assert all(sum(title==w['display'] for _,title in headings)==1 for w in wrappers)
    assert all(c['raw']==c['path'].read_text() for c in chapters),'Canonical lesson input changed'
    assert all(w['raw']==w['path'].read_text() for w in wrappers),'Canonical wrapper input changed'
    assert all(pobj['raw']==pobj['path'].read_text() for pobj in practicals),'Canonical practical input changed'
    assert all(asset['raw']==asset['path'].read_text() for asset in embedded_assets),'Embedded lab asset input changed'
    assert story==story_path.read_text(), 'Canonical story input changed'
    assert code_blocks(story)==code_blocks(narrative), 'Story code changed'
    assert collections.Counter(external_links(story))==collections.Counter(external_links(narrative)), 'Story reference changed'
    table_errors=[]; table=[]
    for index,line in enumerate(clean.splitlines()+[''],1):
        if line.startswith('|'):table.append((index,line))
        elif table:
            widths={len(re.findall(r'(?<!\\)\|',row)) for _,row in table}
            if len(widths)>1:table_errors.append(table[0][0])
            table=[]
    assert not table_errors, f'Inconsistent table columns at lines {table_errors}'
    assert not re.search(r'\]\((?!https?://)[^)]*(?:student-guide|intro|summary|instructor-guide|slides|README)\.md',clean), 'Unconverted source navigation'

    code_blocks(book)
    # Check that every source content line survives, or is in an explicit edit log.
    # Formatting/link changes are normalized. Report unmatched lines for human review.
    losses=[]
    for c in chapters:
        content=plain(chapter_text[c['number']]+'\n'+c['mapping'])
        intentional='\n'.join(a['text'] for a in audit if a['chapter']==c['number'])
        for l in c['raw'].splitlines()[1:]:
            if not l.strip() or l.startswith('#') or re.fullmatch(r'[-* _]+',l):continue
            if plain(l) not in content and l not in intentional:
                losses.append({'chapter':c['number'],'line':l})
    story_survival=plain(narrative)
    story_losses=[l for l in story.splitlines()[1:] if l.strip() and not l.startswith('#') and plain(l) not in story_survival]
    assert not losses,losses
    assert not story_losses,story_losses
    practical_losses=[]
    for pobj in practicals:
        content=plain(practical_text[pobj['parent_number']])
        for l in pobj['raw'].splitlines()[1:]:
            if not l.strip() or l.startswith('#') or re.fullmatch(r'[-* _]+',l): continue
            if plain(l) not in content:
                practical_losses.append({'practical':pobj['source'],'line':l})
    assert not practical_losses,practical_losses
    wrapper_losses=[]
    for w in wrappers:
        content=plain(wrapper_text[(w['part'],w['unit'],w['kind'])])
        intentional='\n'.join(a['text'] for a in audit if a['chapter']==f"{w['unit']} {w['kind']}")
        for l in w['raw'].splitlines()[1:]:
            if not l.strip() or l.startswith('#') or re.fullmatch(r'[-* _]+',l): continue
            if plain(l) not in content and l not in intentional:
                wrapper_losses.append({'wrapper':w['source'],'line':l})
    assert not wrapper_losses,wrapper_losses
    unmapped=[c['number'] for c in chapters if 'no proficiency mapping' in c['raw']]
    assert len(unmapped)==10,unmapped
    expected_unmapped={'0.10','1.0','1.6','2.0','2.9','3.0','3.8','4.0','4.9','conclusion'}
    assert set(unmapped)==expected_unmapped
    assert all('Proficiency Focus' in c['mapping'] and 'Mapped Proficiency Item' in c['mapping'] for c in chapters if c['number'] not in expected_unmapped)
    review_path=OUT/'editorial-review.json'
    review=json.loads(review_path.read_text()) if review_path.exists() else {}
    tracked={str(obj['path'].relative_to(root)) for _,obj in reading_order}
    tracked.update(str(pobj['path'].relative_to(root)) for pobj in practicals)
    tracked.update(str(asset['path'].relative_to(root)) for asset in embedded_assets)
    tracked.update(['docs/story-bible.md','docs/skim-first-authoring-standard.md','docs/proficiency-legend.md'])
    tracked.update(str(path.relative_to(root)) for path in (root/'docs/companion-story').glob('*.md'))
    reviewed=review.get('source_sha256',{})
    review_changed=sorted(path for path in tracked if not (root/path).is_file() or reviewed.get(path)!=hashlib.sha256((root/path).read_bytes()).hexdigest())
    for path,digest in reviewed.items():
        if path not in tracked and (not (root/path).is_file() or hashlib.sha256((root/path).read_bytes()).hexdigest()!=digest):review_changed.append(path)
    review_current=bool(review.get('review_date')) and not review_changed
    review_status='Current for these source hashes' if review_current else 'Needs a new editorial review; structural success alone does not resolve A12 or voice questions'
    (OUT/'ebook-manuscript.md').write_text(book)

    a12_pattern=re.compile(r'\bA12\b|WS-JLEE|\bjlee\b|prd-updates|login-prd|nightowl|invoice\.vbs|\bUpdater\b|203\.0\.113\.88|Pink River Dolphin|Dixon, Yamada',re.I)
    manifest=f'''# Ebook Source Manifest

Build date: {args.date}. Source snapshot date: {snapshot_label}. The live `/thraining-plan/` files supplied the source; earlier exports and the GitHub mirror were not used. This is a derived publication, not a replacement curriculum.

## Inventory

108 proficiency-course lesson/conclusion chapters remain in numeric teaching order: Part I 12; Part II 28; Part III 41; Part IV 16; Part V 10; Part VI 1. In addition, 36 learner-facing subunit wrappers (18 introductions and 18 summaries) are inserted around meaningful multi-lesson groupings. Three learner practicals are embedded under their owning lessons, along with three small controlled lab assets. The wrappers and embedded practical sections add no new numbered proficiency chapters. All ten explicitly unmapped track/course introductions and summaries remain unmapped.

## Canonical A12 Source

- Complete narrative: `/thraining-plan/docs/companion-story/story.md`.
- Governing fact ledger: `/thraining-plan/docs/story-bible.md`.
- Appendix A uses the reconciled learner-facing story directly, with heading levels adapted for the book.
- Evidence decisions and the editorial review scope are recorded in [the canonical reconciliation review](../docs/a12-reconciliation-review.md). Review status for this source snapshot: **{review_status}**.
- No new host count, deployed rule, eradication result, or final attribution is invented.

## Chapter Sources in Teaching Order

References listed for each chapter are preserved in place and consolidated in the manuscript. “None linked” means no external Markdown hyperlink in that student guide, not that the subject lacks supporting literature. No student-guide image assets were referenced. Fenced technical examples stay inline. Case-marker detection also captures shared technical values in separate examples: an IP or filename overlap alone is not an assertion that the example is an A12 event.

'''
    manifest+='## Complete Learner Reading Order\n\n| Position | Kind | Learner content | Source |\n|---:|---|---|---|\n'
    for index,(kind,obj) in enumerate(reading_order,1):
        label=obj['display'] if kind=='wrapper' else obj['book_title']
        manifest+=f'| {index} | {obj["kind"] if kind=="wrapper" else "lesson"} | [{label}](ebook-manuscript.md#{obj["anchor"]}) | `{obj["source"]}` |\n'
    manifest+='\n'
    records=[]
    for i,title in enumerate(part_titles):
        manifest+=f'### {title}\n\n'
        for c in chapters:
            if c['part']!=i:continue
            raw=c['raw']; ext=external_links(raw);terms=sorted(set(m[0] for m in a12_pattern.finditer(raw)),key=str.lower)
            a12_sections=[];current='Opening'
            for l in raw.splitlines():
                if l.startswith('#'):current=l.lstrip('# ').strip()
                if a12_pattern.search(l) and current not in a12_sections:a12_sections.append(current)
            notes=[]
            if code_blocks(raw):notes.append(f'{len(code_blocks(raw))} fenced code block(s), preserved exactly')
            if re.search(r'^#### ',raw,re.M):notes.append('nested source headings retained within level 6')
            if '**Orientation now' in raw:notes.append('two-pass platform use retained; total time covers both passes')
            if c['number'] in expected_unmapped:notes.append('no proficiency mapping')
            if re.search(r'^# ',raw,re.M) and len(re.findall(r'^# ',raw,re.M))>1:notes.append('secondary source H1 demoted to a section')
            case_kind='Explicit case/name reference' if re.search(r'\bA12\b|WS-JLEE|\bjlee\b|Pink River Dolphin|Dixon, Yamada',raw,re.I) else ('Shared value only; review example context' if terms else 'No case marker identified')
            manifest+=f'#### {c["book_title"]}\n\n- Source: `{c["source"]}`\n- Manuscript: {ref(c["number"],"chapter").replace("](#","](ebook-manuscript.md#")}\n- Assets/images: none referenced.\n- A12 use: '+case_kind+'. '+(', '.join('`'+x+'`' for x in terms) if terms else 'No detected terms')+'.\n'
            if a12_sections:manifest+='- Significant A12 passages: '+'; '.join(a12_sections)+'.\n'
            manifest+='- Formatting/assembly notes: '+('; '.join(notes) if notes else 'standard student-guide structure; ratings moved to Appendix B')+'.\n- References: '+('; '.join(f'[{label}]({url})' for label,url in dict.fromkeys(ext)) if ext else 'none linked')+'.\n\n'
            meta=metadata.get(c['source'],{})
            records.append(dict(order=len(records)+1,part=PARTS[i][0],number=c['number'],title=c['title'],source_path=c['source'],library_file_id=meta.get('library_file_id'),version_id=meta.get('version_id'),modified_at=meta.get('modified_at'),sha256=hashlib.sha256(c['path'].read_bytes()).hexdigest(),anchor=c['anchor'],assets=[],references=[dict(label=l,url=u) for l,u in dict.fromkeys(ext)],a12_terms=terms,a12_sections=a12_sections,notes=notes))
    manifest+='## Subunit Wrapper Sources\n\nThese learner-facing advance organizers and summaries are inserted around meaningful multi-lesson subunits and add no proficiency requirements.\n\n'
    for w in wrappers:
        meta=metadata.get(w['source'],{})
        manifest+=f'- `{w["source"]}` — [{w["display"]}](ebook-manuscript.md#{w["anchor"]})\n'
    manifest+='\n## Embedded Learner Practicals and Lab Assets\n\nThe practicals below are embedded under their owning lessons so the single-file learner manuscript preserves the qualification workflow without creating new numbered chapters. Controlled CSV/Python assets are embedded as fenced blocks.\n\n'
    for pobj in practicals:
        manifest+=f'- `{pobj["source"]}` — [{pobj["title"]}](ebook-manuscript.md#{pobj["anchor"]}); owning lesson `{pobj["parent_number"]}`.\n'
        for asset in pobj['assets']:
            manifest+=f'  - `{asset["source"]}` — [{asset["label"]}](ebook-manuscript.md#{asset["anchor"]}).\n'
    manifest+='\n## Supporting Sources and Exclusions\n\nThe proficiency legend comes from `/thraining-plan/docs/proficiency-legend.md`. Module README files were consulted for structure, not inserted as learner chapters. Instructor guides, slides, repository maintenance instructions, old exports, and companion-story planning notes were excluded from the learner body. The front matter, Part introductions, glossary, and acronym list are editorial additions grounded in the curriculum. Subunit introductions and summaries are canonical learner-facing sources and are included in the manuscript. Learner practicals and their controlled lab assets are embedded under their owning lessons. An optional concept index was omitted because the detailed contents, glossary links, and chapter-linked bibliography provide reliable navigation without speculative index entries.\n'
    (OUT/'manifest.md').write_text(manifest)
    provenance={'build_date':args.date,'source_snapshot_date':args.snapshot_date,'chapters':records,'wrappers':[],'practicals':[],'embedded_lab_assets':[],'supporting_sources':[],'reading_order':[obj['source'] for _,obj in reading_order], 'editorial_review_current':review_current, 'metadata_note':'Library identifiers, versions, and timestamps describe retrieval. SHA-256 values identify the exact build inputs, including canonical edits made during this pass; saved bytes are verified after writeback.'}
    for w in wrappers:
        meta=metadata.get(w['source'],{})
        provenance['wrappers'].append(dict(part=PARTS[w['part']][0],unit=w['unit'],kind=w['kind'],title=w['display'],source_path=w['source'],library_file_id=meta.get('library_file_id'),version_id=meta.get('version_id'),modified_at=meta.get('modified_at'),sha256=hashlib.sha256(w['path'].read_bytes()).hexdigest(),anchor=w['anchor']))
    for pobj in practicals:
        meta=metadata.get(pobj['source'],{})
        provenance['practicals'].append(dict(parent_number=pobj['parent_number'],title=pobj['title'],source_path=pobj['source'],library_file_id=meta.get('library_file_id'),version_id=meta.get('version_id'),modified_at=meta.get('modified_at'),sha256=hashlib.sha256(pobj['path'].read_bytes()).hexdigest(),anchor=pobj['anchor'],assets=[a['source'] for a in pobj['assets']]))
    for asset in embedded_assets:
        meta=metadata.get(asset['source'],{})
        provenance['embedded_lab_assets'].append(dict(source_path=asset['source'],library_file_id=meta.get('library_file_id'),version_id=meta.get('version_id'),modified_at=meta.get('modified_at'),sha256=hashlib.sha256(asset['path'].read_bytes()).hexdigest(),anchor=asset['anchor']))
    for path in sorted(set((root/'docs/companion-story').glob('*.md')) | {root/'docs/story-bible.md',root/'docs/skim-first-authoring-standard.md',root/'docs/a12-reconciliation-review.md',legend_path}):
        library_path='/thraining-plan/'+str(path.relative_to(root));meta=metadata.get(library_path,{})
        provenance['supporting_sources'].append(dict(source_path=library_path,library_file_id=meta.get('library_file_id'),version_id=meta.get('version_id'),modified_at=meta.get('modified_at'),sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    (OUT/'source-provenance.json').write_text(json.dumps(provenance,indent=2,ensure_ascii=False)+'\n')
    (OUT/'editorial-audit.json').write_text(json.dumps({'edits':audit,'relative_links_converted':link_edits,'source_line_coverage_exceptions':losses,'wrapper_line_coverage_exceptions':wrapper_losses,'story_line_coverage_exceptions':story_losses},indent=2,ensure_ascii=False)+'\n')
    stats=dict(chapters=len(chapters),subunit_wrappers=len(wrappers),learner_practicals=len(practicals),embedded_lab_assets=len(embedded_assets),words=len(book.split()),external_occurrences=sum(len(external_links(c['raw'])) for c in chapters)+sum(len(external_links(w['raw'])) for w in wrappers)+sum(len(external_links(pobj['raw'])) for pobj in practicals),unique_external_urls=len(refs),internal_links=sum(u.startswith('#') for _,u in LINK.findall(clean)),code_blocks=sum(len(code_blocks(c['raw'])) for c in chapters)+sum(len(code_blocks(w['raw'])) for w in wrappers)+sum(len(code_blocks(pobj['raw'])) for pobj in practicals)+len(embedded_assets),unmapped=unmapped,nav_removed=sum(a['kind']=='standalone navigation removed' for a in audit),relative_links_converted=len(link_edits),a12_chapters=sum(bool(r['a12_terms']) for r in records),broken_internal_links=broken,wrapper_pairs=len(meaningful),reading_order_entries=len(reading_order),table_errors=table_errors,editorial_review_current=review_current,editorial_review_changed_sources=review_changed)
    (OUT/'build-results.json').write_text(json.dumps(stats,indent=2)+'\n')

    ebook_readme=f'''# Ebook manuscript build

This folder contains the derived learner publication for the training plan. The canonical curriculum remains under `modules/`, and the canonical A12 case sources remain under `docs/`.

## Primary learner artifact

- [ebook-manuscript.md](ebook-manuscript.md) — complete reviewable learner manuscript in teaching order
- [manifest.md](manifest.md) — lesson, wrapper, source, reference, and A12-use inventory
- [qa-report.md](qa-report.md) — structural/content QA for the current build
- [source-provenance.json](source-provenance.json) — source hashes and available Library metadata
- [editorial-audit.json](editorial-audit.json) — editorial/link transformations performed by the builder
- [build-results.json](build-results.json) — machine-readable build counts

## Build model

The manuscript contains **{len(chapters)} existing lesson/conclusion chapters** plus **{len(wrappers)} skim-first subunit wrappers** ({sum(w['kind']=='intro' for w in wrappers)} introductions and {sum(w['kind']=='summary' for w in wrappers)} summaries). It also embeds **{len(practicals)} learner practicals** and **{len(embedded_assets)} controlled lab assets** under their owning lessons. These additions do not create new numbered proficiency chapters.

The complete reconciled A12 story is inserted as **Appendix A** from `docs/companion-story/story.md`. Detailed proficiency mappings move to **Appendix B** so they remain available without interrupting normal reading.

## Rebuild

From this directory:

```bash
python build_ebook.py --source-root .. --date YYYY-MM-DD --snapshot-date YYYY-MM-DD
```

An optional inventory JSON can be supplied with `--inventory` when Library identifiers and modified/version metadata should be embedded in `source-provenance.json`. `--snapshot-date` records retrieval separately from the build date. The builder verifies each meaningful grouping has exactly one intro/summary pair and that its lessons fall between them in order. It preserves the canonical story, adapting only headings and links. External references from lessons, wrappers, and the story are consolidated.

[editorial-review.json](editorial-review.json) records the source hashes covered by the [canonical reconciliation review](../docs/a12-reconciliation-review.md). Changed or newly included sources mark editorial QA as needing review instead of repeating an old all-resolved claim. The builder never updates that review record automatically; refresh it only after an actual content/voice/skim review. Structural QA and editorial QA are reported separately.

## Gemini / NotebookLM use

The ebook manuscript is now the intended single learner upload for NotebookLM/Gemini notebook workflows. The older `exports/gemini-notebook/` split-export tree is deprecated and does not need to be rebuilt when the curriculum changes.

## Publishing status

This is still a Markdown review manuscript. DOCX/PDF/EPUB publication should be generated only after the content, structure, and editorial treatment are approved.
'''
    (OUT/'README.md').write_text(ebook_readme)

    if review_current:
        review_summary='The reviewed source snapshot resolves the seven prior A12 issues:\n\n'+'\n'.join(f'- **{item["id"]}:** {item["decision"]}' for item in review.get('decisions',[]))
        review_summary+='\n\n'+review.get('voice_summary','')
    else:
        review_summary='A12/voice conclusions require review before publication. Changed or unreviewed sources: '+(', '.join(review_changed) or 'review record unavailable')+'.'
    qa=f'''# Ebook QA Report

**Build date:** {args.date}  
**Status:** Markdown review build completed successfully.

## Structural validation

- Existing lesson/conclusion chapters: **{len(chapters)}**
- Skim-first subunit wrappers: **{len(wrappers)}** ({sum(w['kind']=='intro' for w in wrappers)} introductions + {sum(w['kind']=='summary' for w in wrappers)} summaries)
- Embedded learner practicals: **{len(practicals)}**
- Embedded controlled lab assets: **{len(embedded_assets)}**
- Parts: **6**
- Explicitly unmapped track/course bookends preserved: **{len(unmapped)}**
- Broken internal Markdown links: **{len(broken)}**
- Fenced code blocks preserved: **{stats['code_blocks']}**
- Relative source links converted to book anchors: **{len(link_edits)}**
- Source lesson line-coverage exceptions: **{len(losses)}**
- Wrapper line-coverage exceptions: **{len(wrapper_losses)}**
- A12 story line-coverage exceptions: **{len(story_losses)}**

The builder also verifies unique lesson identifiers, one occurrence of every lesson and wrapper heading, unchanged canonical source inputs during the build, code-block preservation, external-link occurrence preservation, and valid internal anchors.

## Skim-first structure

All **18 meaningful multi-lesson subunits** now appear in the manuscript with a learner-facing introduction and summary. These wrappers implement the course's **Preview → Predict → Read → Confirm** model and are placed around the existing lessons rather than treated as new proficiency chapters.

Detection Engineering has no additional lower-level multi-lesson grouping requiring another wrapper; its existing 4.0 introduction and 4.9 summary remain the appropriate framing layer.

## A12 and editorial review

**Review status:** {review_status}.

{review_summary}

The detailed decisions, live lesson references, voice scope, and 18-subunit skim results are in [the canonical reconciliation review](../docs/a12-reconciliation-review.md). The builder checks that this editorial review covers the current source hashes; it does not infer semantic correctness from a successful compile.

## Editorial / content checks

- Current reorganized CTI structure (2.1–2.8) is retained.
- All {len(meaningful)} wrapper pairs enclose exactly their intended lessons; the complete reading order is in the manifest.
- The complete canonical story becomes Appendix A through heading/link adaptation, with no phrase-based story rewrite or removal.
- Detailed proficiency mappings remain in Appendix B; wrappers and embedded practical sections add no new numbered requirements.
- The three approved learner practicals are embedded under their owning lessons; their small controlled CSV/Python assets are embedded as fenced blocks so the single-file learner artifact remains usable.
- External-link occurrences from lessons, wrappers, practicals, and the story are preserved; all are eligible for the consolidated bibliography.
- Table column checks pass. All generated internal anchors resolve.
- Instructor guides, answer keys, slides, and planning files are excluded from the learner body.
- Gemini split exports are outside the build. Canonical sources feed the ebook, which is the single learner upload.
- Live external website availability and platform-interface currency were not independently revalidated.

## Remaining publication work

This build is ready for content review with the editorial status above. Final publishing work—DOCX/PDF/EPUB styling, pagination, visual QA, and any refreshed live-platform reference checks—remains a later phase.
'''
    (OUT/'qa-report.md').write_text(qa)

    print(json.dumps(stats,indent=2))

if __name__=='__main__':main()
