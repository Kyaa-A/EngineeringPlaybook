---
name: engineer-project
description: Use when starting, planning, implementing, reviewing, or releasing a non-trivial software project that needs consistent full-stack and AI engineering guidance.
---

# Engineer Project

## Core rule

Determine the current lifecycle stage, load only its relevant guidance, produce the required artifact, and satisfy its exit gate before advancing.

## Workflow

1. Read the active project's instructions and classify the request as discovery, PRD, architecture, frontend, backend/data, AI/integrations, security/testing, or delivery/operations.
2. Read only the matching guide: [discovery and PRD](references/discovery-prd.md), [architecture](references/architecture.md), [frontend](references/frontend.md), [backend and data](references/backend-data.md), [AI, RAG, and integrations](references/ai-rag-integrations.md), [security and testing](references/security-testing.md), or [delivery and operations](references/deployment-operations.md).
3. Read a matching file under `references/prompts/` only when a focused reasoning prompt improves the task.
4. For non-trivial greenfield work, require approved PRD, TDD, and roadmap before implementation.
5. During implementation, test high-risk boundaries first and keep changes within approved scope.
6. Before completion, run fresh verification and report exact evidence.

## Artifact routing

- Product definition: copy [PRD.md](assets/templates/PRD.md).
- Technical design: copy [TDD.md](assets/templates/TDD.md).
- Phased delivery: copy [ROADMAP.md](assets/templates/ROADMAP.md).
- Durable technical choice: copy [ADR.md](assets/templates/ADR.md).
- Production release: use [RELEASE-CHECKLIST.md](assets/templates/RELEASE-CHECKLIST.md).

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
