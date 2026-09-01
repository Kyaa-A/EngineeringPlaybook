import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
VERSION = "0.2.0"


class DistributionTests(unittest.TestCase):
    def test_cross_host_manifests_are_aligned(self):
        paths = [
            "package.json",
            ".claude-plugin/plugin.json",
            ".claude-plugin/marketplace.json",
            ".codex-plugin/plugin.json",
            ".agents/plugins/marketplace.json",
            "hooks/hooks.json",
        ]
        docs = {path: json.loads((ROOT / path).read_text()) for path in paths}

        self.assertEqual(docs["package.json"]["version"], VERSION)
        self.assertEqual(docs[".claude-plugin/plugin.json"]["version"], VERSION)
        self.assertEqual(docs[".codex-plugin/plugin.json"]["version"], VERSION)
        self.assertEqual(docs[".claude-plugin/marketplace.json"]["plugins"][0]["version"], VERSION)
        self.assertEqual(docs[".agents/plugins/marketplace.json"]["plugins"][0]["version"], VERSION)
        self.assertNotIn("hooks", docs[".claude-plugin/plugin.json"])
        self.assertNotIn("hooks", docs[".codex-plugin/plugin.json"])

    def test_managed_updater_and_packaging_tests_exist(self):
        required = [
            "scripts/check-update.mjs",
            "scripts/validate-repo.mjs",
            "test/check-update.test.mjs",
            "test/ci-policy.test.mjs",
        ]
        for relative in required:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_behavior_suite_covers_seven_failure_modes(self):
        evals = json.loads((ROOT / "evals/evals.json").read_text())
        ids = [scenario["id"] for scenario in evals["scenarios"]]
        self.assertEqual(ids, [
            "discovery-routing",
            "gate-pressure",
            "release-evidence",
            "small-fix-routing",
            "architecture-overengineering",
            "ai-trust-boundary",
            "database-integration-boundary",
        ])


if __name__ == "__main__":
    unittest.main()
