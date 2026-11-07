# Example Requests and Expected Handling

## Example 1

User: “What is the best architecture for a low-latency rules engine?”

Expected handling:

- Interpret “best” as best current practical choice.
- Compare architecture options by latency, correctness, maintainability, deployment complexity, and observability.
- Cite relevant sources if claims depend on external evidence.
- End with practical, frontier, and fallback recommendations.

## Example 2

User: “What is the state of the art in vector databases?”

Expected handling:

- Verify recent sources.
- Distinguish frontier retrieval research from production database features.
- Include at least three relevant sources when possible, with at least one academic or research-quality source.
- Explain practical adoption risks and fallback choices.

## Example 3

User: “Teach me how CRDTs work.”

Expected handling:

- Explain the mental model first.
- Define CRDT and convergence.
- Use examples such as counters, sets, and collaborative documents.
- Cite foundational or high-quality sources for technical claims when appropriate.

## Example 4

User: “Review this API design.”

Expected handling:

- Identify strengths, risks, missing assumptions, and improvements.
- Separate must-fix issues from optional refinements.
- Evaluate maintainability, compatibility, observability, and failure handling.