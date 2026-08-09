# Contributing to Engineering Playbook

Thanks for your interest in improving Engineering Playbook. This repository gives humans and coding agents a shared, vendor-neutral workflow from idea to verified production. Contributions should make that workflow clearer, safer, or easier to verify.

## What lives where

- `AGENTS.md`: canonical cross-agent policy.
- `playbook/`: lifecycle guidance and quality gates.
- `prompts/`: task-specific reasoning templates.
- `templates/`: reusable PRD, TDD, roadmap, decision, and release artifacts.
- `skills/engineer-project/`: the compact routing skill.
- `CLAUDE.md`, `.cursor/`, and `.github/`: thin product adapters that must not duplicate canonical rules.
- `scripts/validate.sh`: deterministic repository validation.

## Principles

- Keep guidance vendor-neutral and evidence-driven.
- Preserve PRD, TDD, and roadmap gates for non-trivial work.
- Keep authentication, authorization, billing, and destructive decisions deterministic.
- Prefer practical quality gates over framework dogma.
- Keep the skill concise and load detailed guidance only when relevant.
- Update every affected canonical document, template, prompt, and adapter together.

## Proposing a change

1. Open an issue describing the workflow failure, ambiguity, or missing safety check.
2. Fork the repository and create a focused branch.
3. Make the smallest change that resolves the issue.
4. Run the validation commands below.
5. Open a pull request using a Conventional Commit title, such as `docs: clarify architecture exit gate`.

## Testing locally

Run:

```bash
./scripts/validate.sh
```

If the official Codex skill validator is installed, run its `quick_validate.py` script against `skills/engineer-project`.

For behavior changes to the skill, test the same realistic project scenario before and after the change. Record which files the agent read, the lifecycle stage it selected, the artifact it produced, and whether it respected the exit gate.

## Scope

Engineering Playbook covers the reusable workflow from product discovery through production operations. Framework-specific starter applications, generated products, consulting policy, and project-specific business rules are out of scope.
