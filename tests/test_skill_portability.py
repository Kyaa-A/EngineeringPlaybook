import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "engineer-project"


class SkillPortabilityTests(unittest.TestCase):
    def test_installed_skill_contains_every_routed_resource(self):
        text = (SKILL / "SKILL.md").read_text()
        links = re.findall(r"\[[^]]+\]\(([^)]+)\)", text)

        self.assertGreaterEqual(len(links), 7)
        for link in links:
            self.assertFalse(link.startswith("../"), link)
            self.assertTrue((SKILL / link).is_file(), link)

    def test_installed_skill_contains_lifecycle_guides_and_templates(self):
        required = [
            "references/discovery-prd.md",
            "references/architecture.md",
            "references/frontend.md",
            "references/backend-data.md",
            "references/ai-rag-integrations.md",
            "references/security-testing.md",
            "references/deployment-operations.md",
            "assets/templates/PRD.md",
            "assets/templates/TDD.md",
            "assets/templates/ROADMAP.md",
            "assets/templates/ADR.md",
            "assets/templates/RELEASE-CHECKLIST.md",
        ]

        for relative in required:
            self.assertTrue((SKILL / relative).is_file(), relative)


if __name__ == "__main__":
    unittest.main()
