# Adding or updating an instruction set

The registry is an index of **real, verified artifacts**, not placeholder ZIPs.

## New package checklist

1. Choose a unique lowercase kebab-case ID (for example, `feature-planning-director`).
2. Create `<id>/README.md`, `<id>/<id>.zip`, and `<id>/sources/README.md`.
3. Use an original ZIP whose contents and version you can verify. Do not fabricate missing releases.
4. In the package README document: purpose, intended audience, capabilities, limitations, usage, canonical release/version, archive path, sources, and relationship to the progenitor if applicable.
5. Add a single `instruction_sets[]` record to `registry.json` with `id`, `name`, `description`, `version`, `status`, `role`, `tags`, `readme`, `archive`, and `sources`. Add the package to the root README catalog.
6. Check that all registered paths exist, each package slug and ZIP basename match, the archive is a valid ZIP, and no two IDs collide.

## Versioning and updating

A package folder is a **stable lookup name**, while the registry's `version` identifies the current canonical release. Record release notes and original filename/provenance in the package README. If historical archives are retained later, put them under a clearly marked `history/` subfolder, never register them as a second current release.

Preserve integrity when moving a ZIP: prefer reusing its exact blob rather than re-zipping it. Replace canonical archives only with verified original bytes and explicitly describe the update.

## Sources

The `sources/` directory holds optional research references, provenance notes, external URLs, documents, or transcripts needed to explain how the instruction system was designed. Include a README even if the source artifacts are not yet published. Never commit credentials or private conversation contents without permission.

## Known pending archive

`AI-Knowledge-Atlas-40-Project-Sources.zip` is designated as the latest canonical Atlas package, but its bytes have not been recovered. Until verified and uploaded, keep it out of `registry.json` and do not create a misleading package ZIP.
