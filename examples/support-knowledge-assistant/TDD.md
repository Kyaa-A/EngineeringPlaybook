# Technical Design Document: Support Knowledge Assistant

## Requirements and constraints

Satisfy AC-1 through AC-5 with deterministic authorization, citation-grounded RAG, safe degraded behavior, and observable latency and quality. Use a modular monolith for the MVP.

## System context

An authenticated browser calls a server application. The server reads users and article metadata from Postgres, retrieves vectors through pgvector, calls an LLM provider, and emits non-sensitive telemetry.

## Components and ownership

- Web route: input, streaming state, citations, feedback, and error states
- Auth boundary: session validation and tenant resolution
- Retrieval service: authorization filters, hybrid candidate retrieval, and chunk IDs
- Answer service: versioned prompt, structured output, grounding checks, and streaming
- Feedback service: ratings and missing-content reports
- Postgres: users, tenants, articles, chunks, embeddings, prompt versions, and feedback

## Request and background data flows

1. Validate session and resolve tenant.
2. Validate the question and enforce quota.
3. Retrieve shared chunks plus chunks whose tenant ID matches the authenticated tenant.
4. Provide retrieved chunks as untrusted evidence to the answer service.
5. Validate the structured response and every citation against retrieved chunk IDs.
6. Stream the safe response and record metadata.

Article parsing and embedding run as idempotent background jobs keyed by article version. Failed jobs use bounded retries and expose a visible failure state.

## API and event contracts

`POST /api/answers` accepts `{ question: string }` from an authenticated session and streams events ending in:

```json
{
  "status": "answered",
  "answer": "...",
  "citations": [{"chunkId": "...", "articleId": "..."}]
}
```

or:

```json
{
  "status": "insufficient_evidence",
  "answer": null,
  "citations": []
}
```

## Data model, consistency, and migrations

- `tenants`, `users`, and membership tables define access.
- `articles` store tenant scope, status, source version, and timestamps.
- `article_chunks` store article ID, tenant scope, text hash, content, and vector.
- `answer_feedback` stores user, trace ID, rating, category, and timestamp.
- RLS protects tenant-scoped rows. Migrations are forward-only and indexes include tenant filters plus HNSW on vectors.

## Authentication, authorization, and trust boundaries

The server derives tenant identity from the session, never request input. Retrieval applies tenant filters before evidence reaches the model. The LLM cannot grant access, select a different tenant, edit data, or invoke destructive tools.

## Failure, retry, idempotency, and degraded modes

- Invalid session: deny without calling retrieval or the model.
- Empty or oversized question: return a validation error.
- Retrieval timeout: return an escalation response; do not call the model without evidence.
- Invalid model schema: attempt one constrained repair, then fail safely.
- Provider outage: return a degraded response with retry guidance.
- Embedding job retry: use article version as the idempotency key.

## Performance, capacity, availability, and cost budgets

- Retrieval p95 below 500 milliseconds.
- Time to first useful answer p95 below four seconds.
- Maximum retrieved context and output token budgets are explicit per prompt version.
- Quotas bound requests per user and tenant.

## Deployment and observability

Trace request ID, tenant ID hash, retrieval duration, candidate count, selected chunk IDs, prompt and model versions, schema status, latency, tokens, cost, and outcome. Do not log raw questions or article content by default. Use a feature flag and kill switch.

## Test strategy

- Unit: chunk selection, citation validation, insufficient-evidence rules, and schema parsing
- Integration: real Postgres migrations, RLS with real auth contexts, tenant-filtered vector queries, and feedback writes
- Contract: provider response schema and stream events
- End-to-end: answerable, unanswerable, denied, timeout, and feedback journeys
- Evaluation: recall at K, groundedness, citation correctness, injection resistance, latency, and cost

## Alternatives and trade-offs

- Fine-tuning rejected because knowledge freshness and citations are primary.
- Separate services rejected until scaling or isolation evidence appears.
- Agentic tools rejected because the MVP only retrieves and generates.

## Open decisions

- Confirm the production load profile.
- Approve the quality rubric and evaluation owners.
- Confirm provider region and retention requirements.
