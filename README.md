# Engineering Playbook

A vendor-neutral guide for taking a software project from idea to verified production. It gives humans and coding agents one shared workflow for product definition, architecture, frontend, backend, data, AI, security, testing, and operations.

## Why it exists

Coding agents can generate implementation quickly, but speed without shared gates often produces the wrong scope, unnecessary architecture, unsafe AI decisions, weak tests, and unverified releases. Engineering Playbook gives the human and agent one lifecycle, one set of artifacts, and explicit exit criteria.

It helps you:

- turn an idea into an approved PRD, TDD, and roadmap;
- choose architecture based on current requirements;
- design complete frontend, backend, data, and AI boundaries;
- test high-risk behavior against real infrastructure; and
- release with evidence, monitoring, and rollback.

## Install

### Claude Code

```text
/plugin marketplace add Kyaa-A/EngineeringPlaybook
/plugin install engineer-project@engineering-playbook
```

### Codex CLI

```bash
codex plugin marketplace add Kyaa-A/EngineeringPlaybook --ref main
codex plugin add engineer-project@engineering-playbook
```

The managed plugin checks for a newer version at session start at most once every 24 hours. It only prints manual update commands; it never updates itself. Set `ENGINEER_PROJECT_UPDATE_CHECK=0` to opt out.

## Start a project

Tell your coding agent:

> Use `engineer-project` and guide this idea through discovery, PRD, technical design, roadmap, implementation, verification, and release.

The installed skill is self-contained. It includes the lifecycle guidance, focused prompts, and artifact templates it routes to.

## Repository map

- `AGENTS.md`: canonical instructions for every agent.
- `playbook/`: lifecycle guidance and quality gates.
- `prompts/`: reusable prompts selected by task.
- `templates/`: project artifacts to copy and complete.
- `examples/`: a traceable idea-to-release worked example.
- `evals/`: repeatable behavioral scenarios for testing the skill.
- `skills/engineer-project/`: router skill for Codex and compatible agents.
- `scripts/validate.sh`: structural and content validation.

## Compatibility

- **Codex CLI:** use `AGENTS.md` and install `skills/engineer-project` under `.agents/skills/` or `~/.agents/skills/`.
- **Claude Code:** use `CLAUDE.md` and install the same skill under `.claude/skills/` or `~/.claude/skills/`.
- **Cursor:** the thin rule under `.cursor/rules/` points to the canonical `AGENTS.md`.
- **GitHub Copilot:** `.github/copilot-instructions.md` points to the same workflow.

## Validate

```bash
npm ci
npm test
npm run validate
./scripts/validate.sh
```

For a plain manual install, copy `skills/engineer-project` to `~/.agents/skills/engineer-project` or `~/.claude/skills/engineer-project`.

If your Codex installation includes the official skill creator, also run its `quick_validate.py` against `skills/engineer-project`.

## Worked example and evaluations

Start with the [Support Knowledge Assistant example](examples/support-knowledge-assistant/README.md) to see requirements traced through design, roadmap, and release evidence.

Use the [behavioral evaluation protocol](evals/README.md) to compare baseline agent behavior with the `engineer-project` skill enabled. The fixtures cover discovery routing, gate pressure, unsupported release claims, small corrections, overengineering, AI trust boundaries, and real database integration boundaries.

## Community

Contributions are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md). Community participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Citation metadata is available in [CITATION.cff](CITATION.cff).

## License

MIT. Copyright (c) 2026 Asnari (Kyaa-A). See [LICENSE](LICENSE).
