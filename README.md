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

## Start a project

Tell your coding agent:

> Read `AGENTS.md` in the EngineeringPlaybook repository. Use the `engineer-project` skill and guide this idea through discovery, PRD, technical design, roadmap, implementation, verification, and release.

Do not copy the entire repository into every project. Link to it, install the skill, or tell the agent its local path.

## Repository map

- `AGENTS.md`: canonical instructions for every agent.
- `playbook/`: lifecycle guidance and quality gates.
- `prompts/`: reusable prompts selected by task.
- `templates/`: project artifacts to copy and complete.
- `skills/engineer-project/`: router skill for Codex and compatible agents.
- `scripts/validate.sh`: structural and content validation.

## Compatibility

- **Codex CLI:** use `AGENTS.md` and install `skills/engineer-project` under `.agents/skills/` or `~/.agents/skills/`.
- **Claude Code:** use `CLAUDE.md` and install the same skill under `.claude/skills/` or `~/.claude/skills/`.
- **Cursor:** the thin rule under `.cursor/rules/` points to the canonical `AGENTS.md`.
- **GitHub Copilot:** `.github/copilot-instructions.md` points to the same workflow.

## Install the skill locally

```bash
cp -R skills/engineer-project ~/.agents/skills/engineer-project
```

Claude Code users can install the same folder under `~/.claude/skills/engineer-project`.

## Validate

```bash
./scripts/validate.sh
```

If your Codex installation includes the official skill creator, also run its `quick_validate.py` against `skills/engineer-project`.

## Community

Contributions are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md). Community participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Citation metadata is available in [CITATION.cff](CITATION.cff).

## License

MIT. Copyright (c) 2026 Asnari (Kyaa-A). See [LICENSE](LICENSE).
