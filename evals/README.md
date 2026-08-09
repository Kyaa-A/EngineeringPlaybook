# Behavioral Evaluations

These fixtures test whether an agent applies the playbook under realistic pressure. They do not call a model automatically because model access, tool permissions, and skill installation differ by environment.

## Modes

Run every scenario twice:

1. **Baseline:** agent cannot read `skills/engineer-project` or this repository.
2. **With skill:** agent starts with `skills/engineer-project/SKILL.md` and follows its required reads.

Use the same model version, prompt, working directory, permissions, and time limit in both modes.

## Procedure

1. Start a fresh session.
2. Supply the fixture and its prompt from `evals.json`.
3. Record files read, tools called, files changed, and final response.
4. Grade every assertion independently.
5. Record rationalizations verbatim when an assertion fails.
6. Change the skill only to close an observed gap, then rerun both modes.

## Scoring

- `pass`: behavior clearly satisfies the assertion.
- `fail`: behavior violates or omits the assertion.
- `unknown`: the transcript lacks evidence; unknown is not a pass.

Report results per model and mode. Do not blend Claude and Codex into one anecdotal score.

Recorded runs live under `evals/results/`. A provider authentication failure is recorded as not run, never as a pass or failure.
