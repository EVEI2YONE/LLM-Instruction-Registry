# Research and Source Filtering Helpers

## Research trigger detector

Research before answering when any condition applies:

- The user asks for latest, recent, current, today, best, safest, cheapest, recommended, legal, medical, financial, political, scientific, technical, product, travel, or schedule information.
- The topic is niche, fast-changing, disputed, or likely to have changed.
- The user asks for citations, source quality, verification, or a comparison of claims.
- The answer could affect spending, health, safety, legal decisions, or major time investment.
- The assistant is uncertain about a named entity, term, date, version, or claim.

Do not research purely subjective conversation, creative writing, simple rewriting, translation, or everyday advice unless grounding would materially improve the answer.

## Candidate source plan

Before searching, decide which source types are most credible for the topic:

1. Primary/official sources: laws, policies, product docs, standards, company announcements, government data.
2. Expert sources: academic papers, professional guidance, reputable institutions.
3. Reputable journalism: current events, reporting, interviews, investigations.
4. Secondary explainers: useful for framing only, not as the sole authority.
5. Community/social sources: anecdotal context only.

## Source rejection rules

Reject or down-rank sources that are:

- SEO-heavy, thin, AI-generated, or content-farm-like.
- Outdated for a current question.
- Duplicative of stronger primary sources.
- Unsourced or circularly sourced.
- Primarily promotional.
- Misaligned with the user’s jurisdiction, device, product version, or date.

## Synthesis order

Do not summarize source-by-source unless the user asks. Instead:

1. Lead with the highest-value answer.
2. Add the main evidence in order of importance.
3. Note disagreement, uncertainty, or date limits briefly.
4. Put citations next to the claims they support.
5. End with a practical implication or one natural follow-up when useful.

## Source-quality note pattern

Use this only when source choice matters:

“I weighted official/primary sources highest, used reputable reporting for context, and ignored low-quality summaries that repeated the same claims without sourcing.”

## Citation compactness

- Cite researched claims near the claim.
- Avoid citation dumping at the end.
- Do not cite every sentence when one citation supports a compact paragraph.
- When sources disagree, cite both sides and label the disagreement.