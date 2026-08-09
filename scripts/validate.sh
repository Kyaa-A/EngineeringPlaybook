#!/usr/bin/env bash
set -euo pipefail

export PYTHONDONTWRITEBYTECODE=1

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
  .github/workflows/ci.yml
  examples/support-knowledge-assistant/README.md
  examples/support-knowledge-assistant/PRD.md
  examples/support-knowledge-assistant/TDD.md
  examples/support-knowledge-assistant/ROADMAP.md
  examples/support-knowledge-assistant/RELEASE-CHECKLIST.md
  evals/README.md
  evals/evals.json
  evals/results/2026-08-09-gate-pressure.md
  evals/fixtures/discovery-routing.md
  evals/fixtures/gate-pressure.md
  evals/fixtures/release-evidence.md
  evals/fixtures/small-fix-routing.md
  scripts/check_links.py
  tests/test_check_links.py
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

python3 -m json.tool "$repo_root/evals/evals.json" >/dev/null
python3 -m unittest "$repo_root/tests/test_check_links.py"
python3 "$repo_root/scripts/check_links.py" "$repo_root"

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
