# Roadmap: Support Knowledge Assistant

## Release outcome

An internal authenticated user can receive an authorized, citation-backed answer or a safe insufficient-evidence result, with quality and operational evidence collected before release.

## Phase 1: Deterministic foundation

- Deliverable: auth boundary, tenant model, article/chunk schema, forward-only migrations, RLS, and real-database integration tests
- Dependencies: approved PRD and TDD; representative tenant fixtures
- Verification: migration run, RLS tests under separate tenant identities, typecheck, and API contract tests
- Exit gate: AC-2 passes and unauthorized requests never reach retrieval

## Phase 2: Retrieval and structured answers

- Deliverable: ingestion job, embeddings, authorized retrieval, versioned prompt, answer schema, citation validation, and feedback
- Dependencies: approved evaluation cases and provider configuration
- Verification: recall at K, groundedness, citation correctness, unanswerable behavior, injection tests, and schema tests
- Exit gate: AC-1 and AC-3 meet approved thresholds

## Phase 3: Experience and operations

- Deliverable: streaming UI states, quotas, timeouts, degraded responses, dashboards, alerts, feature flag, and runbooks
- Dependencies: production-like load profile and alert owners
- Verification: end-to-end journeys, accessibility checks, load report, failure injection, smoke test, and rollback rehearsal
- Exit gate: AC-4 and AC-5 pass with named evidence owners

## Release gate

- [ ] All acceptance criteria have fresh evidence.
- [ ] Critical risks are closed or explicitly accepted.
- [ ] Security and privacy review is approved.
- [ ] Dashboards, alerts, runbooks, and ownership are active.
- [ ] Rollback and kill switch are tested.
