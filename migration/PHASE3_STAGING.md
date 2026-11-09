# Phase 3: complete-catalog migration staging

Status: REVIEW ONLY. The frozen inventory contains 49 packages, including one previously migrated Meta-LLM; 48 packages are pending.

Run `python3 scripts/stage_lookup_migration.py --output /tmp/phase3-candidates`. The PR workflow uploads candidate archives and traceability for review.

The script reads every pending package's registered **browsable sources** rather than copying a similar released ZIP. It preserves original bytes under an indexed review candidate, builds a ZIP, and reports source-to-candidate equivalence. This is an inventory and audit stage, **not** a functional lookup-first migration. No sources, registered versions, historical archives or registry metadata are changed.

Each candidate still requires a separate normative-rule mapping, conflict and governance review, canonical schema validation, target-aware package generation, owner approval, and actual behavioral evaluation before becoming a published version. Source-byte preservation does not demonstrate semantic equivalence. The existing specialist binaries remain usable.
