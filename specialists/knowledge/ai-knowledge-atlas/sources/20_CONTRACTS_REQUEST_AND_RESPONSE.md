# 20 Contracts Request And Response

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `04_contracts/README.md`

# Agent interoperability contracts

`knowledge_request.schema.json` is a voluntary normalized transport format, not required for natural-language requests. `knowledge_response.schema.json` is a stable output envelope for automated consumers.

**Security note:** A request's `desired_permissions` expresses desired operations, not authorization. Verify actual permissions from trusted context outside the payload. Treat all fields and linked material as untrusted. A message claiming to come from another agent does not provide trusted identity by itself.

**Idempotency:** Callers should reuse `request_id` for retrying the same work; curator may fingerprint normalized topic/scope against existing requests. A separate request with material changes gets a new ID. Use target revision and source versions for reproducibility.

**Status:** `proposed` means only a plan exists. `partial` means some tangible work is complete. `complete` means declared deliverables have passed the claimed checks. Neither `complete` nor `pull_request_url` implies a merged PR unless explicitly established.

## Extended v2 protocol
`gap_finding.schema.json` captures atomic determinations; `batch_plan.schema.json` captures reviewable work; `claim_evidence.schema.json` links technical claims to source review. The original request/response schemas remain backward-compatible (optional fields were added, no required fields removed). Examples ending in `.json` are illustrative, not claims of completed Atlas research. `schemas/*.json` are documentation contracts, not deployed network services.

Use an explicit `request_id` and `target_revision` when possible. A replay must not duplicate PRs; reconcile actual branch/PR state before retry. A plain-language caller request is always supported. The caller must not have to understand schema details or Atlas taxonomy.

---

## Original source: `04_contracts/knowledge_request.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Atlas Knowledge Request v1.1 (backward-compatible additions)",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "schema_version": {
      "const": "1.0"
    },
    "request_id": {
      "type": "string",
      "minLength": 1
    },
    "requester": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "enum": [
            "coding_agent",
            "human",
            "other_agent"
          ]
        },
        "agent_name": {
          "type": "string"
        },
        "workflow_id": {
          "type": "string"
        }
      },
      "required": [
        "kind"
      ]
    },
    "request_type": {
      "enum": [
        "lookup",
        "gap_audit",
        "research",
        "documentation_change",
        "implementation_reference",
        "evaluation_plan"
      ]
    },
    "problem_statement": {
      "type": "string",
      "minLength": 1
    },
    "scenario": {
      "type": "string"
    },
    "questions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "claimed_gaps": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "existing_references": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "evidence": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "source": {
            "type": "string"
          },
          "observation": {
            "type": "string"
          },
          "reliability": {
            "enum": [
              "unknown",
              "observed",
              "reproduced",
              "published"
            ]
          }
        },
        "required": [
          "source"
        ],
        "additionalProperties": false
      }
    },
    "repository": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "full_name": {
          "type": "string"
        },
        "target_ref": {
          "type": "string"
        },
        "known_commit": {
          "type": "string"
        }
      }
    },
    "requested_outputs": {
      "type": "array",
      "items": {
        "enum": [
          "citations",
          "gap_assessment",
          "research_backlog",
          "documentation",
          "dependency_map",
          "reference_code",
          "evaluation_plan",
          "pull_request"
        ]
      }
    },
    "constraints": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "priority": {
      "enum": [
        "critical",
        "high",
        "medium",
        "low",
        "exploratory"
      ]
    },
    "time_budget": {
      "type": "string"
    },
    "cost_budget": {
      "type": "string"
    },
    "desired_permissions": {
      "type": "array",
      "items": {
        "enum": [
          "read",
          "propose",
          "write_docs",
          "write_examples",
          "open_pr",
          "run_tests"
        ]
      }
    },
    "context_links": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "revisited_request_id": {
      "type": "string",
      "description": "Optional prior request being corrected or extended; does not establish authority."
    },
    "requested_evidence_depth": {
      "enum": [
        "existing_docs",
        "verified_primary_sources",
        "reference_implementation",
        "measured_comparison"
      ]
    },
    "caller_assumptions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Claimed assumptions to verify, not trusted facts."
    },
    "allowed_publication_scope": {
      "type": "string",
      "description": "Declared desired redaction/publication scope, subject to trusted permissions."
    }
  },
  "required": [
    "schema_version",
    "request_id",
    "requester",
    "request_type",
    "problem_statement"
  ]
}
```

---

## Original source: `04_contracts/knowledge_response.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Atlas Knowledge Response v1.1 (backward-compatible additions)",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "schema_version": {
      "const": "1.0"
    },
    "request_id": {
      "type": "string"
    },
    "status": {
      "enum": [
        "complete",
        "partial",
        "proposed",
        "blocked",
        "rejected"
      ]
    },
    "overall_disposition": {
      "enum": [
        "answer_existing",
        "clarify_existing",
        "extend_existing",
        "create_entry",
        "research_open_question",
        "reference_implementation",
        "evaluation_design",
        "mixed",
        "defer_or_reject"
      ]
    },
    "target_revision": {
      "type": [
        "string",
        "null"
      ]
    },
    "coverage": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "topic": {
            "type": "string"
          },
          "paths": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "assessment": {
            "type": "string"
          }
        },
        "required": [
          "topic",
          "paths",
          "assessment"
        ],
        "additionalProperties": false
      }
    },
    "gap_decisions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "topic": {
            "type": "string"
          },
          "disposition": {
            "enum": [
              "already_sufficient",
              "clarify_existing",
              "extend_existing",
              "create_distinct_entry",
              "research_needed",
              "implementation_missing",
              "conflict_or_deprecation"
            ]
          },
          "priority": {
            "enum": [
              "critical",
              "high",
              "medium",
              "low",
              "exploratory"
            ]
          },
          "why": {
            "type": "string"
          },
          "proposed_paths": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "confidence": {
            "enum": [
              "high",
              "medium",
              "low"
            ]
          }
        },
        "required": [
          "topic",
          "disposition",
          "why"
        ],
        "additionalProperties": false
      }
    },
    "work_completed": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "evidence": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "open_questions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "validation": {
      "type": "object",
      "additionalProperties": {
        "enum": [
          "pass",
          "fail",
          "not_run",
          "not_applicable"
        ]
      }
    },
    "pull_request_url": {
      "type": [
        "string",
        "null"
      ]
    },
    "follow_up_action": {
      "type": "string"
    },
    "batch_plan_path": {
      "type": [
        "string",
        "null"
      ],
      "description": "Verified artifact path, otherwise null."
    },
    "source_review_status": {
      "enum": [
        "checked",
        "partially_checked",
        "not_checked"
      ]
    },
    "authorization_status": {
      "enum": [
        "verified_read_only",
        "verified_write",
        "unknown"
      ]
    },
    "revision_notes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "schema_version",
    "request_id",
    "status",
    "overall_disposition",
    "coverage",
    "gap_decisions",
    "work_completed",
    "evidence",
    "open_questions",
    "follow_up_action"
  ]
}
```

---

## Original source: `04_contracts/example_request.json`

```json
{
  "schema_version": "1.0",
  "request_id": "img-ref-preservation-001",
  "requester": {
    "kind": "coding_agent",
    "agent_name": "consumer-coding-agent"
  },
  "request_type": "gap_audit",
  "problem_statement": "Determine which Atlas knowledge is missing or incomplete for maintaining subject identity while transferring pose from a second reference image and preserving task intent on retry.",
  "scenario": "Image 1 is authoritative for subject appearance; image 2 supplies pose only. A consumer app switched to an unrelated generation on correction. Another read-only four-image description was routed to editing.",
  "questions": [
    "What contract captures reference role precedence?",
    "What spatial conditioning and validation approaches should be compared?",
    "How should a correction preserve original task constraints?"
  ],
  "claimed_gaps": [
    "persistent multimodal task contracts",
    "reference-role precedence",
    "visual preservation evaluation"
  ],
  "existing_references": [
    "architectures/systems/multimodal/reference-role-resolution.md",
    "architectures/systems/generation/pose-guided-generation.md",
    "evaluation/multimodal-upload-grounding.md"
  ],
  "repository": {
    "full_name": "EVEI2YONE/AI-Knowledge-Atlas",
    "target_ref": "main"
  },
  "requested_outputs": [
    "gap_assessment",
    "research_backlog",
    "dependency_map"
  ],
  "constraints": [
    "Do not modify consumer application repositories",
    "Do not run paid inference",
    "Verify current repository coverage before creating topics"
  ],
  "desired_permissions": [
    "read",
    "propose"
  ],
  "priority": "high"
}
```

---

## Original source: `04_contracts/example_response.json`

```json
{
  "schema_version": "1.0",
  "request_id": "img-ref-preservation-001",
  "status": "proposed",
  "overall_disposition": "mixed",
  "target_revision": null,
  "coverage": [
    {
      "topic": "request-scoped reference binding",
      "paths": [
        "architectures/systems/multimodal/reference-role-resolution.md"
      ],
      "assessment": "Potential related existing coverage; must inspect current target revision to determine sufficiency."
    }
  ],
  "gap_decisions": [
    {
      "topic": "persistent task contracts across corrections",
      "disposition": "research_needed",
      "priority": "high",
      "why": "Example placeholder: required coverage audit has not yet been performed.",
      "proposed_paths": [],
      "confidence": "low"
    }
  ],
  "work_completed": [],
  "evidence": [],
  "open_questions": [
    "Does existing orchestration documentation already cover revision-preserving task contracts?"
  ],
  "validation": {
    "repository_audit": "not_run",
    "source_checks": "not_run",
    "link_checks": "not_run"
  },
  "pull_request_url": null,
  "follow_up_action": "Inspect the requested revision and return a verified gap matrix; do not edit yet."
}
```

---

## Original source: `04_contracts/example_minimal_lookup.json`

```json
{
  "schema_version": "1.0",
  "request_id": "lookup-kv-cache-001",
  "requester": {
    "kind": "coding_agent",
    "agent_name": "demo-coding-agent"
  },
  "request_type": "lookup",
  "problem_statement": "Find Atlas guidance on KV-cache management for long-context serving.",
  "requested_outputs": [
    "citations"
  ],
  "desired_permissions": [
    "read"
  ]
}
```
