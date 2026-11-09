#!/usr/bin/env python3
"""Stage all pending registry packages from browsable sources; no release writes."""
import argparse, hashlib, json, re, zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
def hash_bytes(x): return hashlib.sha256(x).hexdigest()
def stage(root, out):
    root=root.resolve(); out=out.resolve()
    if root==out or root in out.parents: raise ValueError("output must be outside repository")
    inv=json.loads((root/"migration/inventory.json").read_text())
    reg={x["id"]:x for x in json.loads((root/"registry.json").read_text())["instruction_sets"]}
    if inv["count"]!=len(inv["packages"]) or set(reg)!={x["id"] for x in inv["packages"]}:
        raise ValueError("registry inventory mismatch")
    if out.exists() and list(out.iterdir()): raise ValueError("output not empty")
    out.mkdir(parents=True,exist_ok=True)
    records=[]
    for r in inv["packages"]:
        if r["migration_status"]!="pending": continue
        ident=r["id"]; pkg=reg[ident]
        if pkg["version"]!=r["baseline_version"] or pkg["archive"]!=r["baseline_archive"]:
            raise ValueError("baseline drift "+ident)
        source=root/r["baseline_sources"]
        originals=sorted(p for p in source.rglob("*") if p.is_file() or p.is_symlink())
        if not (source/"SKILL.md").is_file(): raise ValueError("missing entrypoint "+ident)
        folder=out/ident; folder.mkdir()
        mappings=[]; sections=[]
        for orig in originals:
            if orig.is_symlink() or not orig.resolve().is_relative_to(source.resolve()):
                raise ValueError("unsafe source")
            rel=orig.relative_to(source).as_posix()
            data=orig.read_bytes(); readable=orig.suffix.lower() in (".md",".json")
            target=("sections/references/original/" if readable else "original/")+rel
            p=folder/target; p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(data)
            mappings.append({"source":rel,"candidate":target,"sha256":hash_bytes(data)})
            if readable:
                sid="original-"+re.sub("[^a-z0-9]+","-",rel.lower()).strip("-")+"-"+hash_bytes(rel.encode())[:8]
                sections.append({"id":sid,"kind":"reference","path":target,
                  "summary":"Preserved original source: "+rel,
                  "read_when":["inspect original source "+rel],"requires":[],
                  "reference_only":True,"words":len(data.decode("utf8").split()),
                  "sha256":hash_bytes(data)})
        entry="---\nname: "+ident+"\ndescription: Review-only source migration candidate, not approved or installed.\n---\n\n"
        entry+="# Migration review candidate\n\nNOT FOR DEPLOYMENT. Preserve original source files and reconcile all normative rules with the Meta-LLM Orchestrator before generating an environment-tailored specialist. No execution, installation, or approval is implied.\n"
        (folder/"SKILL.md").write_text(entry)
        trace={"id":ident,"registered_version":pkg["version"],"baseline_archive":pkg["archive"],
               "mappings":mappings,"original_bytes":"PRESERVED","semantic_equivalence":"NOT_RUN",
               "formal_approval":"NOT_VERIFIED","release":"NOT_RUN"}
        (folder/"MIGRATION_TRACEABILITY.json").write_text(json.dumps(trace,indent=2)+"\n")
        sources=sorted([x["candidate"] for x in mappings]+["SKILL.md","manifest.json","MIGRATION_TRACEABILITY.json"])
        manifest={"id":ident,"version":"review-from-"+pkg["version"],"source_contract":"lookup-first-v1",
                  "entrypoint":{"path":"SKILL.md","words":len(entry.split()),"sha256":hash_bytes(entry.encode())},
                  "sections":sections,"sources":sources}
        (folder/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
        actual={p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()}
        if set(sources)!=actual: raise ValueError("inventory mismatch "+ident)
        for mapping in mappings:
            if (folder/mapping["candidate"]).read_bytes()!=(source/mapping["source"]).read_bytes():
                raise ValueError("source mismatch "+ident)
        with zipfile.ZipFile(out/(ident+".review-only.zip"),"w",zipfile.ZIP_DEFLATED) as z:
            for p in sorted(actual): z.write(folder/p,arcname=ident+"/"+p)
        with zipfile.ZipFile(out/(ident+".review-only.zip")) as z:
            if z.testzip() or set(z.namelist())!={ident+"/"+p for p in actual}:
                raise ValueError("zip mismatch "+ident)
            for p in actual:
                if z.read(ident+"/"+p)!=(folder/p).read_bytes(): raise ValueError("zip byte mismatch")
        records.append({"id":ident,"sources":len(originals),"integrity":"PASS","semantic":"NOT_RUN","approved":False})
    report={"registry_count":inv["count"],"staged":len(records),"migrations_completed":0,
            "registry_mutations":0,"review_only":True,"packages":records}
    (out/"MIGRATION_REPORT.json").write_text(json.dumps(report,indent=2)+"\n")
    return report
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=ROOT)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(stage(args.root,args.output)))
