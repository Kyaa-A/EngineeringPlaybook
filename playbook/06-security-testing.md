# Security, Testing, and Quality Gates

## Security review

Threat-model authentication, authorization, tenant isolation, inputs, outputs, secrets, CSRF, CORS, CSP, abuse, uploads, webhooks, audit logs, dependencies, prompt injection, tool permissions, encryption, retention, and deletion.

## Test strategy

- Unit tests for pure rules and algorithms
- Real-database integration tests for persistence, migrations, transactions, and RLS
- Contract tests for APIs and provider adapters
- End-to-end tests for critical user journeys
- Accessibility, load, resilience, backup-restore, and AI evaluations where applicable

Use test-first development at boundaries where failure harms users, data, money, privacy, or operations.

## Release gate

- [ ] Typecheck, lint, and tests pass.
- [ ] Critical end-to-end journeys pass.
- [ ] Real auth contexts verify authorization and RLS.
- [ ] Migrations run against production-like data.
- [ ] Accessibility and responsive checks pass.
- [ ] No unresolved critical security findings remain.
- [ ] Performance budgets are met.
- [ ] AI evaluation thresholds are met.
- [ ] Rollback is tested.
