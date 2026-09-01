# Backend, APIs, Data, and Jobs

## Backend structure

- Organize by cohesive domain capability.
- Keep controllers, resolvers, and route handlers thin.
- Put business workflows in services.
- Place provider-specific behavior behind adapters.
- Centralize error mapping and structured logging.

## APIs

Define request and response schemas, server-side authorization, pagination, rate limits, idempotency, safe error codes, and versioning for independently deployed consumers.

## Data

Use constraints for invariants, transactions for multi-write workflows, indexes derived from access patterns, row-level security for exposed multi-tenant data, and forward-only migrations. Define retention, deletion, backup, and restore behavior.

## Jobs

Use background jobs for slow, scheduled, retryable, fan-out, or non-interactive work. Every job needs identity, idempotency, bounded retries, failure visibility, safe replay, and structured logs.

## Exit gate

- [ ] Authorization protects every action and record.
- [ ] Constraints and transactions protect invariants.
- [ ] Collection APIs paginate.
- [ ] Queries avoid N+1 behavior.
- [ ] Migrations are forward-only and retry-safe.
- [ ] Jobs are idempotent and observable.
- [ ] Integration tests use a real database.
- [ ] Secrets and environment configuration are validated.
