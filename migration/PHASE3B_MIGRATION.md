# Phase 3B full-catalog lookup-first conversion

Run the generator only on the existing draft PR branch. It writes proposed new specialist and coordinator releases while preserving every old ZIP.

Source files are segmented losslessly into manifest-indexed sections. The original entrypoint is retained for audit, and original source documents remain available. Sections are classified using filename heuristics and require human review. Release approval and model-behavior equivalence are NOT_RUN.

Do not merge this PR until owner approval and review of migration provenance, schema validity, source inventory, archives, and runtime compatibility. The user's instruction to skip behavioral verification is not evidence that equivalent behavior has been established.
