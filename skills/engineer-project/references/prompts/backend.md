# Backend Prompts

## Backend design

```text
Design the backend for {{requirements}}. Define domain modules, APIs, authorization, validation, transactions, idempotency, pagination, errors, data model, constraints, indexes, RLS, migrations, background jobs, provider adapters, logging, metrics, and real-database integration tests. Identify invariants and how each is enforced.
```

## Boundary review

```text
Review the supplied backend slice. Inspect module cohesion, thin transport layers, service responsibilities, authorization, transaction boundaries, idempotency, N+1 queries, pagination, migration safety, logging, errors, and real-database test gaps. Return findings by severity with evidence, impact, and the smallest safe correction. Do not propose unrelated refactors.
```
