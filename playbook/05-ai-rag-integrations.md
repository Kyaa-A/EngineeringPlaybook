# AI, RAG, and External Services

## Decision rule

Use deterministic code for exact rules, retrieval for private or changing knowledge, an LLM for interpretation or generation, and an agent only for dynamic multi-step tool selection.

## AI contract

Version prompts, minimize context, require JSON Schema or tool output, define insufficient-data behavior, bound repair attempts, and keep consequential actions behind deterministic checks and human approval.

## RAG

Preserve source identity, permissions, and metadata. Chunk by semantic structure, batch embeddings, use authorization-aware retrieval, and add hybrid search or reranking only when evaluation supports it. Citations must resolve to retrieved evidence.

## External services

Define authentication, least privilege, secrets, timeouts, retries, idempotency, quotas, data residency, webhook verification, fallback behavior, and replacement strategy.

## Evaluation

Measure task success, schema validity, recall at K, groundedness, citation correctness, adversarial behavior, latency, tokens, and cost using versioned representative cases.

## Exit gate

- [ ] AI adds measurable value over deterministic alternatives.
- [ ] Authorization and destructive decisions remain deterministic.
- [ ] Output validates against an explicit schema.
- [ ] Evaluations cover normal, boundary, adversarial, and unanswerable cases.
- [ ] Prompt injection and data leakage are tested.
- [ ] Provider failure has a safe degraded mode.
- [ ] Traces include prompt and model versions, latency, tokens, cost, and result.
