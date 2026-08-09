---
name: engineer-project
description: Use when starting, planning, implementing, reviewing, or releasing a non-trivial software project that needs consistent full-stack and AI engineering guidance.
---

# Engineer Project

## Core rule

Determine the current lifecycle stage, load only its relevant guidance, produce the required artifact, and satisfy its exit gate before advancing.

## Workflow

1. Read the repository's `AGENTS.md`.
2. Classify the request as discovery, PRD, architecture, frontend, backend/data, AI/integrations, security/testing, or delivery/operations.
3. Read the matching chapter under `playbook/` and the matching prompt only when it improves the task.
4. For non-trivial greenfield work, require approved PRD, TDD, and roadmap before implementation.
5. During implementation, test high-risk boundaries first and keep changes within approved scope.
6. Before completion, run fresh verification and report exact evidence.

## Artifact routing

- Product definition: copy `templates/PRD.md`.
- Technical design: copy `templates/TDD.md`.
- Phased delivery: copy `templates/ROADMAP.md`.
- Durable technical choice: copy `templates/ADR.md`.
- Production release: use `templates/RELEASE-CHECKLIST.md`.

## Guardrails

- Ask one blocking question at a time.
- Separate evidence, assumptions, recommendations, and open decisions.
- Prefer a modular monolith until complexity is justified.
- Keep authentication, authorization, billing, and destructive actions deterministic.
- Use structured AI output and representative evaluations.
- Use real database infrastructure for integration boundaries.
- Stop for approval when scope, architecture, security, cost, or external state materially changes.
- Never claim completion from inspection or confidence alone.

## Output contract

State the lifecycle stage, files read, artifact produced or updated, decisions made, unresolved questions, current exit-gate status, and next safe action.
