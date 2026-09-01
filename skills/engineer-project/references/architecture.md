# Architecture and Service Boundaries

## Default

Start with a modular monolith: cohesive domain modules, one primary transactional database, explicit contracts, and a background worker only for slow or retryable work.

Split a service only when independent scaling, isolation, ownership, runtime, or deployment requirements justify the network and operational cost.

## TDD contents

Use `templates/TDD.md`. Document:

- System context and actors
- Components and ownership
- Request and background data flows
- API and event contracts
- Data model and consistency rules
- Trust boundaries and sensitive-data flows
- Timeouts, retries, idempotency, and degraded modes
- Deployment topology
- Availability, latency, capacity, and cost budgets
- Important alternatives and trade-offs

## Exit gate

- [ ] Every component has one clear responsibility.
- [ ] Domain and data boundaries are explicit.
- [ ] Contracts are versioned where consumers can drift.
- [ ] Synchronous and asynchronous work are justified.
- [ ] Failure paths and degraded modes are documented.
- [ ] Trust boundaries are visible.
- [ ] Complexity maps to a current requirement.
- [ ] The TDD is approved.
