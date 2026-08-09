# Security Policy

Engineering Playbook is primarily documentation and agent instruction, with a shell validation script. Its security surface includes executable validation logic and guidance that a tool-using agent may follow.

## Reporting a vulnerability

Report security concerns privately to **a.pacalna@asnari.tech** rather than opening a public issue. Include:

- a description of the issue and impact;
- the affected file and lines; and
- safe reproduction steps, if applicable.

Expect an initial response within a few days. Allow a reasonable remediation window before public disclosure.

## In scope

- Hidden or misleading instructions that could induce unsafe agent behavior
- Guidance that leaks secrets or sensitive data
- Instructions that delegate authentication, authorization, billing, or destructive decisions to an LLM
- Prompt-injection or excessive-tool-permission risks in the skill and prompts
- Command injection, unsafe paths, or destructive behavior in `scripts/validate.sh`
- Guidance that falsely permits completion claims without verification

## Out of scope

- Vulnerabilities in Codex, Claude Code, Cursor, GitHub Copilot, or another host application
- General disagreements about engineering style or product workflow
- Vulnerabilities in applications created by users unless directly caused by this repository's guidance

## Supported versions

This project maintains one development line on `main`. Security fixes land on `main`; there are no separately supported release branches.
