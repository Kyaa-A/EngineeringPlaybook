#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

required_files=(
  AGENTS.md
  CLAUDE.md
  README.md
  LICENSE
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  SECURITY.md
  CITATION.cff
  .cursor/rules/engineering-playbook.mdc
  .github/copilot-instructions.md
  playbook/01-discovery-prd.md
  playbook/02-architecture.md
  playbook/03-frontend.md
  playbook/04-backend-data.md
  playbook/05-ai-rag-integrations.md
  playbook/06-security-testing.md
  playbook/07-deployment-operations.md
  prompts/architecture.md
  prompts/frontend.md
  prompts/backend.md
  prompts/ai-rag.md
  prompts/security.md
  prompts/review.md
  templates/PRD.md
  templates/TDD.md
  templates/ROADMAP.md
  templates/ADR.md
  templates/RELEASE-CHECKLIST.md
  skills/engineer-project/SKILL.md
  skills/engineer-project/agents/openai.yaml
)

for file in "${required_files[@]}"; do
  test -s "$repo_root/$file" || {
    echo "missing or empty: $file" >&2
    exit 1
  }
done

if rg -n 'TODO|Sinag|PhishAlert|CodeGraph|ColinaHealth|FleetOS|Converter' \
  "$repo_root" \
  -g '*.md' \
  -g '*.yaml'; then
  echo "placeholder or project-specific content found" >&2
  exit 1
fi

for chapter in "$repo_root"/playbook/*.md; do
  rg -q '^## Exit gate|^## Completion gate|^## Release gate' "$chapter" || {
    echo "missing gate: ${chapter#$repo_root/}" >&2
    exit 1
  }
done

echo "repository guidance validation passed"
