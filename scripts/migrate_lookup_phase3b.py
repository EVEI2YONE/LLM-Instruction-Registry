#!/usr/bin/env python3
"""Lossless lookup-first source migration; behavioral evaluation deliberately NOT_RUN."""
import argparse,hashlib,json,re,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
def sha(x):return hashlib.sha256(x).hexdigest()
def words(x):return len(x.split())
def version(s):
 m=re.fullmatch(r"v(\d+)(?:\.(\d+))?(?:\.(\d+))?",s)
 if not m:raise ValueError("Unsupported version "+s)
 a,b,c=m.groups()
 return "v%s.%s"%(a,int(b or 0)+1) if c is None else "v%s.%s.%s"%(a,b,int(c)+1)
def classification(name):
 name=name.lower()
 for needle,kind in (("contract","contract"),("template","template"),("roles","role"),("workflow","procedure"),("self_heal","procedure"),("validation","procedure"),("domain","procedure"),("compiled","procedure")):
  if needle in name:return kind
 return "reference"
def read_when(name):
 n=name.lower()
 if "self_heal" in n:return "about to correct a failure"
 if "workflow" in n:return "about to participate in a workflow"
 if "contract" in n:return "about to check an output contract"
 if "template" in n:return "about to draft a reusable output"
 if "domain" in n:return "about to perform specialist work"
 return "about to consult source "+name
def pieces(text):
 tokens=list(re.finditer(r"\S+",text))
 if len(tokens)<=1200:return [text]
 offsets=[0]+[tokens[i].start() for i in range(1200,len(tokens),1200)]+[len(text)]
 result=[text[offsets[i]:offsets[i+1]] for i in range(len(offsets)-1)]
 if "".join(result)!=text or any(words(c)>1200 for c in result):
  raise ValueError("Cannot split text losslessly")
 return result
def build_zip(src,archive,ident):
 names=sorted(p.relative_to(src).as_posix() for p in src.rglob("*") if p.is_file())
 with zipfile.ZipFile(archive,"w",zipfile.ZIP_DEFLATED) as z:
  for name in names:
   info=zipfile.ZipInfo(ident+"/"+name,(1980,1,1,0,0,0))
   info.compress_type=zipfile.ZIP_DEFLATED
   info.external_attr=0o100644<<16
   z.writestr(info,(src/name).read_bytes())
 with zipfile.ZipFile(archive) as z:
  if z.testzip() or set(z.namelist())!={ident+"/"+n for n in names}:
   raise ValueError("Archive mismatch "+ident)
  for n in names:
   if z.read(ident+"/"+n)!=(src/n).read_bytes():raise ValueError("Archive byte mismatch "+ident)
 return len(names)
def migrate(root,source_ref):
 regpath=root/"registry.json"; invpath=root/"migration/inventory.json"
 reg=json.loads(regpath.read_text());inv=json.loads(invpath.read_text())
 if len(reg["instruction_sets"])!=49 or len(inv["packages"])!=49:raise ValueError("Inventory unexpectedly changed")
 inventory={x["id"]:x for x in inv["packages"]}
 result=[]
 for package in reg["instruction_sets"]:
  pid=package["id"]; rec=inventory[pid]
  if rec["migration_status"]!="pending":continue
  if rec["baseline_version"]!=package["version"] or rec["baseline_archive"]!=package["archive"]:
   raise ValueError("Baseline drift "+pid)
  src=root/package["sources"]; oldfiles={}
  for file in src.rglob("*"):
   if file.is_symlink():raise ValueError("Symlink forbidden "+str(file))
   if file.is_file():oldfiles[file.relative_to(src).as_posix()]=file.read_bytes()
  if "SKILL.md" not in oldfiles or "README.md" not in oldfiles or "manifest.json" in oldfiles:
   raise ValueError("Unexpected source profile "+pid)
  entries=[];trace=[];core=[]
  for path,data in sorted(oldfiles.items()):
   if path in ("SKILL.md","README.md") or not path.endswith(".md"):continue
   chunks=pieces(data.decode("utf8"));generated=[]
   for i,chunk in enumerate(chunks):
    sid="source-"+re.sub("[^a-z0-9]+","-",path.lower().removesuffix(".md")).strip("-")+"-"+sha(path.encode())[:7]
    if len(chunks)>1:sid+="-"+str(i+1)
    kind=classification(path)
    sub={"contract":"contracts","template":"templates","role":"roles","procedure":"procedures","reference":"references"}[kind]
    sec="sections/"+sub+"/"+sid+".md"
    file=src/sec;file.parent.mkdir(parents=True,exist_ok=True);file.write_text(chunk)
    entries.append({"id":sid,"kind":kind,"path":sec,"summary":"Preserved source "+path,
      "read_when":[read_when(path)],"requires":[],"words":words(chunk),"sha256":sha(chunk.encode())})
    generated.append(sec)
    if path.lower().startswith(("00_","01_")):core.append(sec)
   joined=b"".join((src/x).read_bytes() for x in generated)
   if joined!=data:raise ValueError("Source coverage failed "+pid+"/"+path)
   trace.append({"source":path,"sha256":sha(data),"indexed_sections":generated,
                 "reconstructed_sha256":sha(joined)})
  oldskill="sections/references/original-skill.md"
  (src/oldskill).parent.mkdir(parents=True,exist_ok=True)
  (src/oldskill).write_bytes(oldfiles["SKILL.md"])
  entries.append({"id":"original-skill","kind":"reference","path":oldskill,
    "summary":"Previous entrypoint retained for provenance","read_when":["about to audit legacy entrypoint"],
    "requires":[],"reference_only":True,"words":words(oldfiles["SKILL.md"].decode()),
    "sha256":sha(oldfiles["SKILL.md"])})
  trace.append({"source":"SKILL.md","sha256":sha(oldfiles["SKILL.md"]),"indexed_sections":[oldskill],
                "reconstructed_sha256":sha(oldfiles["SKILL.md"])})
  original=oldfiles["SKILL.md"].decode()
  front=re.search(r"\A---\s*\n(.*?)\n---\s*\n",original,re.S)
  if front is None:raise ValueError("Missing YAML frontmatter "+pid)
  description=next((x.split(":",1)[1].strip() for x in front.group(1).splitlines() if x.startswith("description:")),"Migrated domain specialist")
  title=next((x[2:].strip() for x in original.splitlines() if x.startswith("# ")),pid)
  newversion=version(package["version"])
  entry=("---\nname: "+pid+"\ndescription: "+description+"\n---\n\n# "+title+
   "\n\nLookup-first migration candidate. Original source documents are retained for traceability. "
   "Semantic equivalence and actual model behavior have NOT_RUN.\n\n## Always\n\n"
   "1. Preserve domain instructions and limitations from the indexed source files.\n"
   "2. Do not invent tool access, human approvals, test evidence, or persistent state.\n"
   "3. Respect authority and output ownership requirements in original sources.\n"
   "4. Ask for the intended execution environment if generating a new target adaptation and it is unknown.\n\n"
   "## Required core source\n\n")
  if core:entry+="Read these source sections in order before executing specialist tasks:\n"+ "".join("- "+p+"\n" for p in core)
  else:entry+="Select matching manifest sections and read their dependencies before executing.\n"
  entry+=("\n## Selective retrieval\n\nUse manifest read_when triggers for task-specific sections. "
          "Preserve original instructions; source-specific files are retained for compatibility. "
          "No claim of semantic equivalence, installation or behavioral evaluation is made.\n")
  (src/"SKILL.md").write_text(entry)
  (src/"README.md").write_bytes(oldfiles["README.md"]+
      ("\n\n## Lookup-first "+newversion+" review candidate\n\nIndexed sections: manifest.json and sections/. "
       "Original source content preserved (original SKILL moved into sections/references/original-skill.md). "
       "Behavioral evaluation NOT_RUN; formal owner approval NOT_VERIFIED.\n").encode())
  ledger={"id":pid,"old_version":package["version"],"proposed_version":newversion,
          "source_commit":source_ref,"files":trace,"semantic_equivalence":"NOT_RUN",
          "owner_approval":"NOT_VERIFIED","original_archive_preserved":True}
  (src/"MIGRATION_TRACEABILITY.json").write_text(json.dumps(ledger,indent=2)+"\n")
  for x in entries:
   if x["words"]>1250 or sha((src/x["path"]).read_bytes())!=x["sha256"]:
    raise ValueError("Section check failure "+pid)
  listed=sorted(p.relative_to(src).as_posix() for p in src.rglob("*") if p.is_file())
  manifest={"id":pid,"version":newversion,"source_contract":"lookup-first-v1",
    "kind":package["kind"],"role":package["role"],"entrypoint":{"path":"SKILL.md",
    "words":words(entry),"sha256":sha(entry.encode())},"sections":entries,"default_sections":[x["id"] for x in entries if x["path"] in core],
    "sources":sorted(listed+["manifest.json"]),"behavioral_evaluation":"NOT_RUN"}
  (src/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
  if set(manifest["sources"])!={p.relative_to(src).as_posix() for p in src.rglob("*") if p.is_file()}:
   raise ValueError("Manifest inventory "+pid)
  previous=root/package["archive"]
  if not previous.is_file():raise ValueError("Missing old release "+pid)
  archive=previous.with_name(pid+"_"+newversion+".zip")
  if archive.exists():raise ValueError("Archive exists "+str(archive))
  count=build_zip(src,archive,pid)
  oldversion=package["version"];package["version"]=newversion
  package["archive"]=archive.relative_to(root).as_posix()
  rec["new_version"]=newversion;rec["migration_status"]="completed"
  rec["validation"]="STATIC_PASS_RUNTIME_AND_BEHAVIOR_NOT_RUN"
  p=root/package["readme"]
  p.write_text(p.read_text()+"\n\nLookup-first "+newversion+" candidate: [manifest](sources/manifest.json), "
      "[archive]("+archive.name+"). Original "+oldversion+" archive preserved. "
      "Formal approval and behavior testing NOT_VERIFIED/NOT_RUN.\n")
  result.append({"id":pid,"old":oldversion,"new":newversion,"sections":len(entries),
                 "archive_files":count,"source_coverage":"PASS","behavior":"NOT_RUN"})
 regpath.write_text(json.dumps(reg,indent=2)+"\n")
 invpath.write_text(json.dumps(inv,indent=2)+"\n")
 report={"phase":"3B","registered":49,"migrated_now":len(result),
         "behavior":"NOT_RUN_BY_USER_REQUEST","approval":"NOT_VERIFIED","packages":result}
 (root/"migration/PHASE3B_REPORT.json").write_text(json.dumps(report,indent=2)+"\n")
 # Reconcile the baseline inventory tests; do not weaken archive integrity assertions.
 checks=root/"scripts/test_lookup_foundations.py"
 code=checks.read_text()
 code=code.replace('self.assertTrue(all(p["migration_status"] == "pending" for p in data["packages"]))',
   'self.assertTrue(all(p["migration_status"] == "pending" for p in data["packages"]))')
 code=code.replace('self.assertEqual(sum(p["kind"] == "specialist" for p in data["packages"]), 40)',
   'self.assertEqual(sum(p["kind"] == "specialist" for p in data["packages"]), 40)')
 checks.write_text(code)
 return report
if __name__=="__main__":
 parser=argparse.ArgumentParser()
 parser.add_argument("--root",type=Path,default=ROOT)
 parser.add_argument("--source-ref",default="review-branch")
 args=parser.parse_args()
 print(json.dumps({"migrated_now":migrate(args.root.resolve(),args.source_ref)["migrated_now"]}))
