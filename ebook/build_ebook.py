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
import unicodedata
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
# Bridges are written for the book. Source lesson explanations remain intact.
BRIDGES = {
    '0.6.1': ('0.6 — Frameworks', 'With the roles and handoffs established, the next three chapters introduce complementary ways to organize behavior, relationships, and attack progression. Keep the question each framework answers in view.'),
    '1.1.1': ('1.1 — Endpoint Evidence', 'Start with the events a host records. The individual event types become more useful when you can connect them without claiming more than their fields show.'),
    '1.2.1': ('1.2 — Network Evidence', 'Endpoint evidence names activity from the host’s perspective. Network evidence adds what a sensor observed on the wire; compare those perspectives and retain the limits of each.'),
    '1.3.1': ('1.3 — Detection Logic', 'You can now read the evidence that detections consume. Next, examine how a rule selects activity and what its match does—and does not—establish.'),
    '1.4.1': ('1.4 — Alert Investigation', 'A rule match starts the investigation. Use the available records to evaluate the activity, assign a defensible classification, and identify what still needs attention.'),
    '1.5.1': ('1.5 — Reporting and Handoff', 'An investigation becomes useful to others through its product. Choose the report, timing, and route that fit the decision and recipient.'),
    '2.1.1': ('2.1 — Intelligence Foundations and Requirements', 'Start by distinguishing recorded values, contextual information, and assessed intelligence. That distinction supports the requirements and RFI intake work that follows.'),
    '2.2.1': ('2.2 — Analytical Tradecraft', 'A clear requirement gives analysis a direction. Tradecraft helps you evaluate the evidence, consider alternatives, and express judgments with appropriate uncertainty.'),
    '2.3.1': ('2.3 — Analytical Frameworks', 'Use the reasoning habits from the previous unit to organize behavior and relationships. The frameworks provide structure while the evidence determines which claims belong in it.'),
    '2.4.1': ('2.4 — CTI Tools and Platforms', 'Before deeper enrichment, become familiar with where evidence can be retrieved and how its provenance is recorded. The platform guides use two passes: orientation here, then detailed interpretation alongside the relevant method in 2.5.'),
    '2.5.1': ('2.5 — Technical Enrichment and Discovery', 'Return to the platform evidence with a specific analytical method. Preserve the seed, time, and relationship behind each candidate so later correlation can test the connection.'),
    '2.6.1': ('2.6 — Threat Assessment and Organizational Significance', 'Candidate relationships now need an assessment of what matters in this environment. Keep applicability, visibility, relevance, and impact distinct as you develop that assessment.'),
    '2.7.1': ('2.7 — Intelligence Production and Dissemination', 'An assessment needs a usable form and an intended recipient. This unit carries the reasoning into structured objects, finished products, RFI closure, and dissemination.'),
    '2.8.1': ('2.8 — Local Application', 'Apply the analytical workflow through the organization’s actual priorities, approval process, and channels. The exercises ask you to obtain local answers where the course cannot supply them.'),
    '3.2.1': ('3.2 — Hunt Methodology', 'With the purpose of hunting established, choose how the hunt begins and develop a testable plan. Scope and expected evidence make the search reviewable.'),
    '3.4.1': ('3.4 — CTI as a Hunt Input', 'External research provides possible leads. Evaluate whether a lead is worth hunting, translate it into observable behavior, and retain the evidence behind any structured intelligence input.'),
    '3.6.1': ('3.6 — Attacker Techniques', 'Framework labels help organize the plan. Technique-focused hunting now requires the procedure, telemetry, and scope that make the search selective.'),
    '3.7.1': ('3.7 — Local Hunt Practice', 'A technically useful search still needs ownership, documentation, and a recipient. Follow the local process so findings and limitations survive the handoff.'),
}

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
    parser.add_argument('--date',default='2026-10-03')
    args=parser.parse_args()
    root=args.source_root.resolve()
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
    assert len(chapters)==107, f'Expected 107 chapters, found {len(chapters)}; review manifest before changing expectation.'
    ids=[c['number'] for c in chapters]
    assert len(set(ids))==len(ids),'Duplicate chapter numbers'
    assert [sum(c['part']==i for c in chapters) for i in range(6)]==[11,28,41,16,10,1]
    byid={c['number']:c for c in chapters}; bypath={c['path']:c for c in chapters}
    part_titles=[f'Part {roman} — {name}' for roman,name,_ in PARTS]
    aa='Appendix A — The Complete A12 Case Study';ab='Appendix B — Proficiency Mapping'
    audit=[]; link_edits=[]; unresolved=[]
    def ref(n,label=None):
        c=byid.get(n)
        if c is None:
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
            elif target.name=='README.md':
                candidates=[c for c in chapters if c['path'].is_relative_to(target.parent)]
                if not candidates:raise ValueError(f'No chapter for {url} in {p}')
                part=next((i for i,(_,_,f) in enumerate(PARTS) if target.parent==root/'modules'/f),None)
                new='#'+(slug(part_titles[part]) if part is not None else candidates[0]['anchor'])
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
        if c['number'] in BRIDGES:
            unit,bridge=BRIDGES[c['number']];start+=f'**{unit}**\n\n{bridge}\n\n'
        return start+body+'\n'
    chapter_text={c['number']:process(c) for c in chapters}
    front=f'''# Defensive Cyber Operations

**SOC, Cyber Threat Intelligence, Threat Hunting, and Detection Engineering**

**MalasadaTech Training Plan – First Edition**  
**v0.1 Review Draft · Build date: {args.date}**  
Curriculum snapshot: current course files retrieved 2026-10-02.

Defensive work depends on more than recognizing a suspicious value. An analyst needs to explain what happened, decide which questions remain, and give the next person enough evidence to act. This book follows that work from shared foundations through SOC investigation, Cyber Threat Intelligence, Threat Hunting, and Detection Engineering.

The chapters combine technical examples with the decisions those examples support. You will read endpoint and network evidence, evaluate intelligence, develop scoped hunts, and consider how findings become maintained detection coverage.

## How to Use This Book

Read the shared foundations first, then follow the role tracks in order. Chapter numbers match the curriculum so you can return to a particular lesson during practice. The opening and closing chapters of each track provide orientation and integration; the final course summary reconnects all four roles.

At a worked example, pause before the explanation. Describe the observation in your own words, identify what remains unknown, and name the next useful question. Use the knowledge checks to test that reasoning. They are learner exercises; this manuscript does not add an instructor answer key.

Estimated times are retained from the course as planning guides. The CTI platform chapters use two passes: first retrieve and describe evidence, then return for interpretation during the relevant enrichment method. Their estimates cover both passes together. Use the example cards and records printed in the lessons where available; some activities also require a supplied report or an authorized environment. This book does not include a separate live lab or platform accounts.

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
        for c in chapters:
            if c['part']==i:toc.append(f'  - [{c["book_title"]}](#{c["anchor"]})')
    for title in [aa,ab,'Glossary','Acronyms and Technical Abbreviations','Consolidated References and Further Reading']:
        toc.append(f'- [{title}](#{slug(title)})')
    book=front+'\n'+'\n'.join(toc)+'\n\n'
    for i,title in enumerate(part_titles):
        book+=f'## {title}\n\n{PART_INTROS[i]}\n\n'
        if i in (1,2,3,4):book+=f'> **A12 Case Study:** Follow the evidence available at this stage of the case. The uninterrupted narrative appears in [Appendix A](#{slug(aa)}).\n\n'
        book+='\n'.join(chapter_text[c['number']] for c in chapters if c['part']==i)+'\n'
    story_path=root/'docs/companion-story/story.md';story=story_path.read_text()
    maint='Nothing in this file is a second plot. If a later lesson needs a new fact, add it to the [story bible](../story-bible.md) first.'
    assert maint in story
    narrative=story.replace(maint,'')
    audit.append(dict(chapter='Appendix A',kind='maintainer-only closing instruction removed',text=maint))
    story_reference_edits={
        'Jordan receives, evaluates, prioritizes, and answers (**2.7.4**).':
        'Jordan receives, evaluates, prioritizes, and answers (intake: **2.1.5**; response: **2.7.4**).',
        '(**0.3 f**)':'(**0.3**)',
    }
    for old,new in story_reference_edits.items():
        assert old in narrative
        audit.append(dict(chapter='Appendix A',kind='structural cross-reference corrected',text=old,replacement=new))
        narrative=narrative.replace(old,new)
    narrative=re.sub(r'^# ', '### ',narrative,flags=re.M)
    narrative=re.sub(r'^## ', '#### ',narrative,flags=re.M)
    # Repair nested bold markers without changing labels, numbers, or facts.
    narrative=re.sub(r'\*\*([^*\n]+)\(\*\*([\d.]+)\*\*\)([.:]?)\*\*',r'**\1(\2)\3**',narrative)
    narrative=re.sub(r'\*\*(\d+(?:\.\d+)+(?:\.x)?)\*\*',lambda m:ref(m[1]),narrative)
    # The remaining group labels and task numbers route to their owning chapter.
    narrative=re.sub(r'(?<![\d/#])\b([0-4]\.x)\b',lambda m:ref(m[1]),narrative)
    narrative=re.sub(r'\n{3,}','\n\n',narrative).strip()
    book+=f'''## {aa}

The following narrative preserves the established A12 story, including its nine original stages and closing handoffs. Read it after the main course to see how the same case moves between desks.

> **Review note:** Some judgments in this established narrative are stronger than the evidence boundaries taught in the revised chapters. Those differences remain visible for review and are documented in [the QA report](qa-report.md#a12-consistency-review). The narrative has not been rewritten to resolve them.

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
    for c in chapters:
        for label,url in external_links(c['raw']):
            entry=refs.setdefault(url,dict(label=label,chapters=[]))
            if c['number'] not in entry['chapters']:entry['chapters'].append(c['number'])
    book+='## Consolidated References and Further Reading\n\nThe following list preserves the course’s linked sources, with one entry per exact URL and links back to the chapters that use it. Chapter-level references remain beside their explanations. URLs are reproduced from the curriculum; their live availability and current platform interfaces have not been independently revalidated for this Markdown edition.\n\n'
    groups=collections.defaultdict(list)
    for url,entry in refs.items():groups[urlsplit(url).netloc.lower().removeprefix('www.')].append((url,entry))
    for domain,entries in sorted(groups.items()):
        book+=f'### {domain}\n\n'
        for url,entry in entries:
            book+=f'- [{entry["label"]}]({url}) — used in '+', '.join(ref(n) for n in entry['chapters'])+'.\n'
        book+='\n'
    book=re.sub(r'\n{3,}','\n\n',book).rstrip()+'\n'
    (OUT/'ebook-manuscript.md').write_text(book)

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
    assert all(c['raw']==c['path'].read_text() for c in chapters),'Canonical input changed'
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
    story_check=story
    for old,new in story_reference_edits.items():story_check=story_check.replace(old,new)
    story_losses=[l for l in story_check.splitlines()[1:] if l.strip() and not l.startswith('#') and l!=maint and plain(l) not in story_survival]
    assert not losses,losses
    assert not story_losses,story_losses
    unmapped=[c['number'] for c in chapters if 'no proficiency mapping' in c['raw']]
    assert len(unmapped)==10,unmapped
    expected_unmapped={'0.9','1.0','1.6','2.0','2.9','3.0','3.8','4.0','4.9','conclusion'}
    assert set(unmapped)==expected_unmapped
    assert all('Proficiency Focus' in c['mapping'] and 'Mapped Proficiency Item' in c['mapping'] for c in chapters if c['number'] not in expected_unmapped)
    a12_pattern=re.compile(r'\bA12\b|WS-JLEE|\bjlee\b|prd-updates|login-prd|nightowl|invoice\.vbs|\bUpdater\b|203\.0\.113\.88|Pink River Dolphin|Dixon, Yamada',re.I)
    manifest=f'''# Ebook Source Manifest

Build date: {args.date}. Source snapshot retrieved: 2026-10-02. The live `/thraining-plan/` files supplied the source; earlier exports and the GitHub mirror were not used. This is a derived publication, not a replacement curriculum.

## Inventory

107 student-facing chapters, in numeric teaching order: Part I 11; Part II 28; Part III 41; Part IV 16; Part V 10; Part VI 1. Unit headings are not additional chapters. All ten explicitly unmapped introductions/summaries remain unmapped. Chapter identifiers and subordinate proficiency task identifiers are distinct.

## Canonical A12 Source

- Complete narrative: `/thraining-plan/docs/companion-story/story.md`.
- Source selection: `/thraining-plan/docs/companion-story/README.md` identifies `story.md` as the finished retelling and the story bible as the governing fact ledger.
- Fact ledger used for consistency review: `/thraining-plan/docs/story-bible.md`.
- Appendix A preserves all narrative stages and the close. Only the final maintainer instruction about adding future facts to the bible is omitted; malformed nested bold is repaired and cross-references are adapted.
- Established uncertainties remain unresolved. No new host count, rule deployment, eradication result, or final attribution has been added.
- See [qa-report.md](qa-report.md#a12-consistency-review) for narrative/lesson discrepancies.

## Chapter Sources in Teaching Order

References listed for each chapter are preserved in place and consolidated in the manuscript. “None linked” means no external Markdown hyperlink in that student guide, not that the subject lacks supporting literature. No student-guide image assets were referenced. Fenced technical examples stay inline. Case-marker detection also captures shared technical values in separate examples: an IP or filename overlap alone is not an assertion that the example is an A12 event.

'''
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
    manifest+='## Supporting Sources and Exclusions\n\nThe proficiency legend comes from `/thraining-plan/docs/proficiency-legend.md`. Module README files were consulted for structure, not inserted as learner chapters. Instructor guides, slides, repository maintenance instructions, old exports, and companion-story planning notes were excluded from the learner body. The front matter, Part introductions, short unit bridges, glossary, and acronym list are editorial additions grounded in the student guides. An optional concept index was omitted because the detailed contents, glossary links, and chapter-linked bibliography provide reliable navigation without speculative index entries.\n'
    (OUT/'manifest.md').write_text(manifest)
    provenance={'build_date':args.date,'source_snapshot_date':'2026-10-02','chapters':records,'supporting_sources':[]}
    for path in [story_path,root/'docs/story-bible.md',root/'docs/companion-story/README.md',legend_path]:
        library_path='/thraining-plan/'+str(path.relative_to(root));meta=metadata.get(library_path,{})
        provenance['supporting_sources'].append(dict(source_path=library_path,library_file_id=meta.get('library_file_id'),version_id=meta.get('version_id'),modified_at=meta.get('modified_at'),sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    (OUT/'source-provenance.json').write_text(json.dumps(provenance,indent=2,ensure_ascii=False)+'\n')
    (OUT/'editorial-audit.json').write_text(json.dumps({'edits':audit,'relative_links_converted':link_edits,'source_line_coverage_exceptions':losses,'story_line_coverage_exceptions':story_losses},indent=2,ensure_ascii=False)+'\n')
    stats=dict(chapters=len(chapters),words=len(book.split()),external_occurrences=sum(len(external_links(c['raw'])) for c in chapters),unique_external_urls=len(refs),internal_links=sum(u.startswith('#') for _,u in LINK.findall(clean)),code_blocks=sum(len(code_blocks(c['raw'])) for c in chapters),unmapped=unmapped,nav_removed=sum(a['kind']=='standalone navigation removed' for a in audit),relative_links_converted=len(link_edits),a12_chapters=sum(bool(r['a12_terms']) for r in records),broken_internal_links=broken)
    (OUT/'build-results.json').write_text(json.dumps(stats,indent=2)+'\n')
    print(json.dumps(stats,indent=2))

if __name__=='__main__':main()
