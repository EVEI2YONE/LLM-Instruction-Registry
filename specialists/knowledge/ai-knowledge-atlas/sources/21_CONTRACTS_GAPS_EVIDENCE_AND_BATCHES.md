# 21 Contracts Gaps Evidence And Batches

This is an indexed consolidation of the original v2 package. Section headers preserve original source paths. Follow core instructions over illustrative examples.


---

## Original source: `04_contracts/gap_finding.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Atomic Knowledge Gap Finding 1.0",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "finding_id": {
      "type": "string",
      "minLength": 1
    },
    "request_id": {
      "type": "string",
      "minLength": 1
    },
    "topic": {
      "type": "string",
      "minLength": 1
    },
    "status": {
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
    "existing_paths": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "missing_specifics": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "dependencies": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "proposed_paths": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "source_urls_to_verify": {
      "type": "array",
      "items": {
        "type": "string",
        "format": "uri"
      }
    },
    "confidence": {
      "enum": [
        "high",
        "medium",
        "low"
      ]
    },
    "confidence_reason": {
      "type": "string"
    },
    "target_revision": {
      "type": [
        "string",
        "null"
      ]
    },
    "validation_status": {
      "enum": [
        "pass",
        "fail",
        "not_run",
        "not_applicable"
      ]
    }
  },
  "required": [
    "finding_id",
    "request_id",
    "topic",
    "status",
    "priority",
    "existing_paths",
    "missing_specifics",
    "dependencies",
    "proposed_paths",
    "confidence",
    "confidence_reason",
    "validation_status"
  ]
}
```

---

## Original source: `04_contracts/claim_evidence.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Claim-linked Source Evidence 1.0",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "claim_id": {
      "type": "string",
      "minLength": 1
    },
    "claim_text": {
      "type": "string",
      "minLength": 1
    },
    "source_title": {
      "type": "string"
    },
    "source_url": {
      "type": "string"
    },
    "source_version": {
      "type": "string"
    },
    "source_date": {
      "type": "string"
    },
    "checked_date": {
      "type": "string"
    },
    "supporting_location": {
      "type": "string"
    },
    "classification": {
      "enum": [
        "primary_supported",
        "official_documented",
        "engineering_inference",
        "original_measured",
        "comparative_measured",
        "conflicted",
        "hypothesis",
        "unknown",
        "deprecated_or_changed"
      ]
    },
    "review_status": {
      "enum": [
        "verified",
        "partially_verified",
        "not_verified"
      ]
    },
    "limits": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "counterevidence": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "affected_paths": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "claim_id",
    "claim_text",
    "classification",
    "review_status",
    "limits"
  ]
}
```

---

## Original source: `04_contracts/batch_plan.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Knowledge Change Batch Plan 1.0",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "batch_id": {
      "type": "string",
      "minLength": 1
    },
    "request_ids": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1
    },
    "base_revision": {
      "type": [
        "string",
        "null"
      ]
    },
    "scope": {
      "type": "string"
    },
    "authorization_verified": {
      "type": "boolean"
    },
    "gap_finding_ids": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "prerequisites": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "work_items": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "action": {
            "enum": [
              "create",
              "extend",
              "clarify",
              "research",
              "evaluate",
              "implement_reference",
              "update_index"
            ]
          },
          "path": {
            "type": "string"
          },
          "acceptance": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "action",
          "path",
          "acceptance"
        ]
      }
    },
    "test_plan": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "evidence_gaps": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "status": {
      "enum": [
        "proposed",
        "partial",
        "complete",
        "blocked"
      ]
    }
  },
  "required": [
    "batch_id",
    "request_ids",
    "scope",
    "authorization_verified",
    "gap_finding_ids",
    "work_items",
    "test_plan",
    "evidence_gaps",
    "status"
  ]
}
```

---

## Original source: `04_contracts/example_gap_finding.json`

```json
{
  "finding_id": "gap-visual-validation-001",
  "request_id": "img-ref-preservation-001",
  "topic": "Evaluation of image pose alignment versus identity preservation",
  "status": "research_needed",
  "priority": "high",
  "existing_paths": [
    "evaluation/multimodal-upload-grounding.md",
    "architectures/systems/generation/pose-guided-generation.md"
  ],
  "missing_specifics": [
    "Confirm whether controlled comparative measurements for stylized-pose transfer are documented in target revision"
  ],
  "dependencies": [
    "Pose-representation evaluation",
    "Identity-consistency metrics"
  ],
  "proposed_paths": [
    "research/open-research-questions.md"
  ],
  "confidence": "low",
  "confidence_reason": "Example classification only; full current-branch audit and source review not performed",
  "validation_status": "not_run"
}
```

---

## Original source: `04_contracts/example_claim_evidence.json`

```json
{
  "claim_id": "claim-example-rag-001",
  "claim_text": "An Atlas RAG pipeline may combine lexical and vector candidate retrieval before reranking.",
  "source_title": "Atlas RAG pipeline implementation pattern",
  "source_url": "",
  "source_version": "example-document",
  "source_date": "",
  "checked_date": "",
  "supporting_location": "Offline/online workflow description",
  "classification": "engineering_inference",
  "review_status": "not_verified",
  "limits": [
    "Source text was not reverified in this package build; example is illustrative"
  ],
  "counterevidence": [],
  "affected_paths": [
    "implementations/patterns/rag-pipeline.md"
  ]
}
```

---

## Original source: `04_contracts/example_batch_plan.json`

```json
{
  "batch_id": "batch-example-001",
  "request_ids": [
    "img-ref-preservation-001"
  ],
  "base_revision": null,
  "scope": "Documentation-only triage proposal; no repo modifications",
  "authorization_verified": false,
  "gap_finding_ids": [
    "gap-visual-validation-001"
  ],
  "prerequisites": [
    "Inspect current evaluation and generation entries"
  ],
  "work_items": [
    {
      "action": "research",
      "path": "research/open-research-questions.md",
      "acceptance": [
        "Document hypothesis and candidate baselines",
        "Label all results as not run"
      ]
    }
  ],
  "test_plan": [
    "Verify links and source citations if an edit is approved"
  ],
  "evidence_gaps": [
    "No independent visual benchmark has been run for this sample"
  ],
  "status": "proposed"
}
```
