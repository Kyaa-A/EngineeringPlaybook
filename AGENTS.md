# Engineering Playbook Agent Instructions

This file is the vendor-neutral source of truth. Read it before using this repository.

## Mission

Guide software work from a validated problem to a reliable production release. Prefer the simplest design that satisfies current product, security, performance, and operational requirements.

## Required lifecycle

For non-trivial greenfield work:

1. Discovery and problem validation
2. Product requirements document
3. Technical design document
4. Roadmap with verifiable phases
5. Test-first implementation at high-risk boundaries
6. Full verification against acceptance criteria
7. Release with monitoring and rollback

Do not begin implementation until the PRD, TDD, and roadmap are approved. Small fixes may use a short diagnosis and scoped plan, but must not expand into unrelated work.

## Routing

Read only the guidance relevant to the current stage:

- Product definition: `playbook/01-discovery-prd.md`
- Architecture: `playbook/02-architecture.md`
- Frontend: `playbook/03-frontend.md`
- Backend and data: `playbook/04-backend-data.md`
- AI, RAG, and integrations: `playbook/05-ai-rag-integrations.md`
- Security and testing: `playbook/06-security-testing.md`
- Deployment and operations: `playbook/07-deployment-operations.md`

Use `templates/` for artifacts and `prompts/` for task-specific reasoning. Do not load every file when one chapter is sufficient.

## Engineering rules

- Keep authentication, authorization, billing, and destructive decisions deterministic.
- Validate inputs and outputs at system boundaries.
- Start with a modular monolith; split services only for proven scaling, isolation, ownership, or deployment needs.
- Use real Postgres or Supabase for database integration tests.
- Make migrations forward-only and safe to retry.
- Design loading, empty, error, denied, timeout, and degraded states.
- Require structured model output at application boundaries.
- Evaluate AI quality, latency, tokens, and cost before release.
- Never claim completion without fresh verification evidence.

## Expected agent behavior

At the start, state the current lifecycle stage, required inputs, expected artifact, and exit gate. Ask one blocking question at a time. Separate facts, assumptions, recommendations, and unresolved decisions. Stop for approval when a decision materially changes scope, architecture, security, cost, or external state.

For implementation, keep changes narrow, preserve unrelated work, and report exact verification commands and results.
