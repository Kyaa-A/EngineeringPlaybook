# Worked Example: Support Knowledge Assistant

This fictional example shows how one product idea moves through the playbook. It is evidence of artifact traceability, not a claim that a production application exists.

## Scenario

A support team wants an internal assistant that answers agent questions using approved knowledge-base articles and cites its sources.

## Evidence and assumptions

Evidence supplied for the example:

- Support agents spend a median of six minutes searching for approved answers.
- Policy errors occur when agents rely on stale personal notes.
- The knowledge base contains tenant-specific and shared articles.

Assumptions that require validation:

- Citation-backed answers will reduce search time.
- Existing article permissions are accurate.
- A useful answer can meet the latency budget without an agentic workflow.

## Lifecycle artifacts

| Artifact | Source | Exit gate | Example status |
| --- | --- | --- | --- |
| [PRD](PRD.md) | `templates/PRD.md` | Requirements measurable and approved | Draft for review |
| [TDD](TDD.md) | `templates/TDD.md` | Boundaries, failures, budgets, and tests defined | Draft for review |
| [Roadmap](ROADMAP.md) | `templates/ROADMAP.md` | Phases have evidence and gates | Draft for review |
| [Release checklist](RELEASE-CHECKLIST.md) | `templates/RELEASE-CHECKLIST.md` | Fresh production evidence exists | Not ready |

## Traceability

| PRD criterion | Design control | Roadmap phase | Required release evidence |
| --- | --- | --- | --- |
| AC-1 grounded answer with citations | Retrieval service returns chunk IDs; answer schema requires citations | Phase 2 | Groundedness and citation report |
| AC-2 tenant isolation | Deterministic authorization filters every retrieval query | Phase 1 | Real-auth RLS integration results |
| AC-3 insufficient evidence | Schema supports `insufficient_evidence`; no answer synthesis | Phase 2 | Unanswerable-case evaluation |
| AC-4 latency target | Single retrieval and generation path; streaming response | Phase 3 | Production-like p95 load report |
| AC-5 safe outage behavior | Provider timeout and degraded response | Phase 3 | Failure-injection evidence |

## Deliberate trade-offs

- Use a modular monolith rather than separate retrieval and generation services.
- Use RAG rather than fine-tuning because knowledge changes and citations are required.
- Do not allow the model to modify articles, permissions, or tickets.
- Defer agentic tool use, automatic article ingestion, and external customer access.

## How to use this example

Read the artifacts in lifecycle order. Check that every requirement maps to a design control, delivery phase, and release proof. Replace the fictional evidence and targets rather than copying them into a real product.
