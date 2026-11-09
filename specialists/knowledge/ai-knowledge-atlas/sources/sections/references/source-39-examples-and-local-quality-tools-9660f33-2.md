Draft202012Validator.check_schema(sc)
    e=list(Draft202012Validator(sc).iter_errors(data))
    print('PASS' if not e else 'FAIL',file,'against',schema)
    errors.extend(f'{file}: {x.message}' for x in e)
for e in errors:print(e)
sys.exit(1 if errors else 0)
```

---

## Original source: `10_quality_tools/check_markdown.py`

```python
#!/usr/bin/env python3
"""Read-only verification of local Markdown links and basic catalog discoverability.

Usage: python check_markdown.py /path/to/AI-Knowledge-Atlas
Exit: 0 pass, 1 broken links, 2 invalid directory.
Known limitations: simple inline links, not full CommonMark/HTML parser, remote URLs not checked.
"""
import argparse
from pathlib import Path
import re, sys, urllib.parse

LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
CODE_FENCE = re.compile(r'^\s*(```|~~~)')

def check(root):
    root=Path(root).resolve()
    if not root.is_dir():
        return 2, [f"missing directory: {root}"]
    files=sorted(root.rglob('*.md'))
    errors=[]
    counts={'files':len(files),'checked_local_links':0,'external_links_skipped':0}
    for p in files:
        fenced=False
        for n,line in enumerate(p.read_text(encoding='utf-8-sig').splitlines(),1):
            if CODE_FENCE.match(line):
                fenced=not fenced
                continue
            if fenced: continue
            for raw in LINK.findall(line):
                dest=raw.strip().split(' "',1)[0].strip('<>')
                if not dest or dest.startswith('#'): continue
                parsed=urllib.parse.urlsplit(dest)
                if parsed.scheme or dest.startswith('//'):
                    counts['external_links_skipped']+=1
                    continue
                target=urllib.parse.unquote(parsed.path)
                if not target or '{{' in target: continue
                counts['checked_local_links']+=1
                if target.startswith('/'):
                    q=(root/target.lstrip('/')).resolve()
                else:
                    q=(p.parent/target).resolve()
                try: q.relative_to(root)
                except ValueError:
                    errors.append(f'{p.relative_to(root)}:{n}: path escapes root: {dest}')
                    continue
                if not q.exists():
                    errors.append(f'{p.relative_to(root)}:{n}: missing target: {dest}')
    print('Files:',counts['files'],'Local links checked:',counts['checked_local_links'],'External links skipped:',counts['external_links_skipped'])
    for e in errors: print('ERROR:',e)
    return (1 if errors else 0),errors

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('root',help='Directory containing Markdown files')
    args=parser.parse_args()
    sys.exit(check(args.root)[0])
```

---

## Original source: `10_quality_tools/check_package.py`

```python
#!/usr/bin/env python3
"""Verify package manifest, checksums, required modules, content depth, and substantive feature coverage.

Usage: python check_package.py /path/to/extracted/package
No network access or external dependencies required.
"""
import argparse,hashlib,json,sys
from pathlib import Path

REQUIRED=[
 '00_COMPILED_INSTRUCTIONS.md','00_README.md',
 '01_core/02_trust_authority_and_scope.md',
 '02_helpers/08_gap_scoring_and_dedup.md',
 '02_helpers/09_claim_source_verification.md',
 '02_helpers/12_implementation_and_evaluation_router.md',
 '03_roles/06_self_heal_reporter.md',
 '04_contracts/knowledge_request.schema.json',
 '04_contracts/knowledge_response.schema.json',
 '04_contracts/gap_finding.schema.json',
 '04_contracts/batch_plan.schema.json',
 '05_templates/11_comparative_evaluation_protocol.md',
 '06_workflows/11_cross_agent_handoff_and_dedup.md',
 '07_state/05_invariant_and_regression_registry.md',
 '08_validation/06_self_heal_instructions.md',
 '08_validation/07_promised_component_matrix.md',
 '09_domain_playbooks/README.md',
 '10_quality_tools/check_markdown.py',
 '11_examples/README.md',
]

def check(root):
 root=Path(root).resolve()
 issues=[]
 manifest_path=root/'99_manifest.json'
 if not manifest_path.exists():return ['Missing 99_manifest.json']
 m=json.loads(manifest_path.read_text(encoding='utf-8'))
 listed={v['path']:v for v in m.get('files',[])}
 actual={str(p.relative_to(root)):p for p in root.rglob('*') if p.is_file() and p.name!='99_manifest.json'}
 for p in REQUIRED:
  if p not in actual:issues.append('Required module missing: '+p)
 for p in actual.keys()-listed.keys():issues.append('Unlisted file: '+p)
 for p in listed.keys()-actual.keys():issues.append('Manifest file missing: '+p)
 for p in actual.keys()&listed.keys():
  data=actual[p].read_bytes()
  h=hashlib.sha256(data).hexdigest()
  if h!=listed[p].get('sha256'):issues.append('Checksum mismatch: '+p)
  if len(data)<80:issues.append('Shallow/empty module: '+p)
 for letter in 'abcdefgh':
  matches=list((root/'09_domain_playbooks').glob(letter+'_*.md'))
  if len(matches)!=1:issues.append('Missing/duplicate domain playbook: '+letter)
  elif len(matches[0].read_text(encoding='utf-8').split())<200:issues.append('Domain playbook lacks detail: '+str(matches[0].name))
 for path in ['01_core','02_helpers','03_roles','04_contracts','05_templates','06_workflows','07_state','08_validation','09_domain_playbooks','10_quality_tools','11_examples']:
  if not (root/path).is_dir():issues.append('Missing category: '+path)
 return issues

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('root');args=a.parse_args()
 issues=check(args.root)
 if issues:
  for x in issues:print('FAIL:',x)
  sys.exit(1)
 print('PASS: manifest, sha256 files, category/modules, A-H coverage and minimum content-depth checks')
```

---

## Original source: `10_quality_tools/fixtures/bad/README.fixture`

```text
# Bad fixture

[Missing target](not-present.md) should produce a nonzero checker result.
```

---

## Original source: `10_quality_tools/fixtures/good/README.md`

# Good fixture

[Child](child.md) and [external](https://example.org) should not yield missing local links.

---

## Original source: `10_quality_tools/fixtures/good/child.md`

# Child fixture

Local Markdown link target used by the checker. This document intentionally contains a complete sentence so structural package validation does not mistake it for a missing content module.

---

## Original source: `10_quality_tools/smoke_test.py`

```python
#!/usr/bin/env python3
"""Smoke-test the Markdown checker using one positive and one negative fixture."""
from pathlib import Path
import subprocess,sys,tempfile
here=Path(__file__).resolve().parent
cmd=[sys.executable,str(here/'check_markdown.py')]
pos=subprocess.run(cmd+[str(here/'fixtures/good')],capture_output=True,text=True)
with tempfile.TemporaryDirectory() as td:
 (Path(td)/'README.md').write_text((here/'fixtures/bad/README.fixture').read_text(encoding='utf-8'),encoding='utf-8')
 neg=subprocess.run(cmd+[td],capture_output=True,text=True)
print('Positive fixture exit:',pos.returncode)
print('Negative fixture exit:',neg.returncode)
if pos.returncode!=0 or neg.returncode!=1:
 print('FAIL: expected positive 0 and negative 1')
 print(pos.stdout,pos.stderr,neg.stdout,neg.stderr)
 sys.exit(1)
print('PASS: Markdown check recognizes valid and missing local links')
```
