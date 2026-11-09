# Backend architecture review
Use actual repository tree, dependency graph, API/data contracts, ownership and workload evidence. Assess correctness and security first, then cohesion/coupling, feature/module boundaries, change isolation, public contracts, cycles, data ownership, schema compatibility, runtime concurrency, testability, scalability and maintainability.

Start Atlas lookup at indexed canonical entries for modularity, module-public-contracts, architecture-dependency-rules, bounded-contexts, dependency-inversion, project-structure-selection, incremental-boundary-migration, api-contracts, schema-evolution, scalability and architecture-fitness-functions. Verify current paths/status from index before quoting.

Compare a no-change baseline; small private modules within one deployable; modular monolith; multi-project libraries; independently deployed services only if runtime scaling/deployment boundaries justify complexity. Document tradeoffs, anti-patterns and rollback. No invented performance, Sonar, LOC or developer-velocity improvements.
