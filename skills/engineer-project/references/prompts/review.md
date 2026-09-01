# Review Prompts

## Diagnose before fixing

```text
Diagnose {{failure}} using {{evidence}}. Classify the primary cause, state a falsifiable hypothesis, propose the smallest experiment, and identify the narrowest correction. Separate symptom, root cause, contributing conditions, and regression coverage. Do not change multiple variables at once.
```

## Pre-ship gate

```text
Gate this release against product acceptance criteria, architecture, trust boundaries, schemas, authorization, data integrity, tests, security, performance, observability, cost, rollback, and incident readiness. Return PASS, CONDITIONAL PASS, or FAIL with evidence. Unknown evidence is not a pass.
```
