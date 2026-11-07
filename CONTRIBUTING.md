# Contributing instruction sets

Each instruction system has a unique lowercase kebab-case directory under `instruction-sets/`: `instruction-sets/<id>/README.md`, `instruction-sets/<id>/<id>_vN.zip`, and `instruction-sets/<id>/sources/README.md`.

Each ZIP must be **repacked**, not merely renamed: extract the original archive; normalize its extracted content under one folder named `<id>`; create a fresh ZIP with that folder as the single top-level directory; validate the ZIP and its entries.

Maintain a current version in `registry.json`; one canonical archive per ID. Keep prior releases in explicitly labeled history if necessary. Document any change to the packaged content and preserve provenance.

Update the root catalog and registry with each addition. Do not publish placeholder archives (the AI Knowledge Atlas original remains unavailable). Never check in secrets or unapproved private source documents.

The `scripts/rebuild_registry.py` script performs a **one-time migration** of the legacy `packages/` hierarchy on the migration branch. After that migration, add new packages directly under `instruction-sets/`; do not rerun the one-time migration script when `packages/` is absent.
