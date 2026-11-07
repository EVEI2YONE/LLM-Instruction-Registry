# Composition and component reuse

Use hierarchy: foundations/tokens -> building blocks/primitives -> components -> patterns -> features -> pages and modals. Keep API, slots, variants, states and ownership explicit. Favor semantic composition instead of flag-heavy mega-components. A shared Button belongs in the catalog; a billing checkout workflow likely belongs in its product. Assess adoption, coupling, state complexity, tests, accessibility and migration cost.
