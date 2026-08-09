# Engineering Playbook

A vendor-neutral guide for taking a software project from idea to verified production. It gives humans and coding agents one shared workflow for product definition, architecture, frontend, backend, data, AI, security, testing, and operations.

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

## Install the skill locally

```bash
cp -R skills/engineer-project ~/.agents/skills/engineer-project
```

Claude Code users can install the same folder under `~/.claude/skills/engineer-project`.

## Validate

```bash
./scripts/validate.sh
python /home/asnari/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/engineer-project
```
