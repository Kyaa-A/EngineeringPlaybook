# Product Requirements Document: Support Knowledge Assistant

## Summary

Provide support agents with fast, citation-backed answers from knowledge they are already authorized to access.

## Problem and evidence

Agents spend a median of six minutes locating approved guidance. Stale personal notes create policy errors. The product must reduce lookup time without weakening tenant isolation or hiding uncertainty.

## Target users

- Primary: authenticated support agents answering active tickets
- Secondary: knowledge managers reviewing answer quality and missing coverage

## Goals and success metrics

- Reduce median knowledge lookup time from six minutes to two minutes.
- Achieve at least 90% citation correctness on the approved evaluation set.
- Produce no cross-tenant retrievals in authorization integration tests.
- Keep end-to-end p95 time to first useful answer below four seconds under the defined load profile.

## User journeys

1. An authenticated agent enters a support question.
2. The system retrieves only authorized current articles.
3. The assistant streams an answer with source citations.
4. If evidence is insufficient, the assistant says so and suggests escalation.
5. The agent can rate the answer and report a missing or stale article.

## Functional requirements

- FR-1: Authenticate every user and resolve tenant membership server-side.
- FR-2: Search shared and tenant-specific articles within the user's permissions.
- FR-3: Return structured answers with citations mapped to retrieved chunks.
- FR-4: Return an explicit insufficient-evidence result when grounding is inadequate.
- FR-5: Record feedback and non-sensitive trace metadata for evaluation.

## Non-functional requirements

- Authorization remains deterministic and cannot be overridden by model output.
- Prompts and retrieved documents are treated as untrusted input at different instruction levels.
- Logs exclude article bodies, questions, credentials, and customer personal data by default.
- Provider timeouts return a safe degraded response.
- Every production prompt and evaluation set is versioned.

## Acceptance criteria

- AC-1: Given answerable evaluation questions, the response cites the supporting article and every citation resolves to a retrieved chunk.
- AC-2: Given a user from tenant A, no tenant B chunk appears in retrieval results, traces, or responses.
- AC-3: Given an unanswerable question, the response uses `insufficient_evidence` and does not fabricate an answer.
- AC-4: Under the documented load profile, p95 time to first useful answer is below four seconds.
- AC-5: Given retrieval or model unavailability, the user receives a safe retry or escalation message without a false answer.

## Non-goals

- Editing knowledge articles
- Taking actions on support tickets
- External customer access
- Fine-tuning a model
- Dynamic multi-tool agents

## Risks and open questions

- Knowledge permissions may contain historical errors; knowledge operations owns validation.
- Citation correctness may not imply answer completeness; product and support own rubric approval.
- Real traffic volume and provider-region constraints require confirmation.

## MVP boundary

One authenticated internal web flow: ask a question, retrieve authorized evidence, stream a structured cited answer or insufficient-evidence result, and collect feedback.
