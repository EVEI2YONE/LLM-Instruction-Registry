# Version, package and publish

Read when about to produce an installable ZIP, update registered package metadata, create a PR or make a release artifact.

1. Pin the repository and read `docs/PUBLISHING.md`, package ownership and version history. Choose a new semantic registry version for changed behavior; keep the stable package ID. Never overwrite released binary ZIPs.
2. Build sources as one canonical tree with `manifest.json` and `SKILL.md`; list every source including adapters, tools, templates and agent metadata in the manifest inventory. Render lookup tables from that same manifest. Avoid hand-maintained compiled canonical sources.
3. Validate the complete section/dependency graph, paths, hashes, word counts, entrypoint tables, source inventory, source encoding, document links and target-native adapter limitations before packaging.
4. Package a **real** ZIP with exactly `<id>/` as its root and all canonical sources below it, preserving bytes. Verify CRC, unsafe paths, symlinks and a full source-to-ZIP byte comparison. For GitHub-only writes, use binary Git blob/base64, tree, commit and update ref; never upload a string pretending to be an archive.
5. Update only the correct registry item, canonical README/version navigation, applicable tests, source archive path and URLs. Prefer one reviewable branch/PR, clear change evidence and no unrelated specialist changes.
6. Preserve old ZIPs and source provenance. A pure move should ideally keep the original blob identity; reconstruction from unavailable older source must be disclosed as such.
7. After committing, run `python3 scripts/search_registry.py validate`, unit tests, ZIP inventory and workspace-specific tests. Read final changed-file list and CI results. Record exactly which tests are `PASS`, `FAIL`, `BLOCKED` or `NOT_RUN`.
8. Do not merge, install, deploy, grant tool access or claim remote execution without the user's authority and observed tool results. A new registered package does not mean an actual hosted service has been deployed.
