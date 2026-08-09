# Release Checklist: Support Knowledge Assistant

This example intentionally remains unchecked. A document cannot prove an unbuilt system is ready.

## Product

- [ ] AC-1 through AC-5 have links to fresh evidence.
- [ ] Answered, insufficient-evidence, denied, timeout, and degraded states pass user acceptance.

## Engineering

- [ ] Typecheck, lint, unit, integration, contract, end-to-end, and build commands pass.
- [ ] Forward-only migrations pass against production-like data.
- [ ] Real tenant identities prove RLS and retrieval isolation.
- [ ] Security and dependency checks pass.
- [ ] Groundedness, citation, injection, latency, and cost thresholds pass.

## Operations

- [ ] Configuration and secrets are validated.
- [ ] Dashboards and alerts are live with named owners.
- [ ] Backups and restore are verified.
- [ ] Feature flag, kill switch, and rollback work.
- [ ] Smoke test and canary window are assigned.

## Evidence required

- Test and build run IDs
- Migration and RLS integration report
- AI evaluation report with dataset and prompt versions
- Load and failure-injection report
- Security approval
- Rollback rehearsal record
