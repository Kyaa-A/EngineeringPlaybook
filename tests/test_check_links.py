import importlib.util
import tempfile
import unittest
from pathlib import Path


module_path = Path(__file__).parents[1] / "scripts" / "check_links.py"
spec = importlib.util.spec_from_file_location("check_links", module_path)
check_links = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_links)


class CheckLinksTest(unittest.TestCase):
    def test_accepts_existing_relative_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "target.md").write_text("target")
            source = root / "README.md"
            source.write_text("[target](target.md)")
            self.assertEqual([], check_links.find_broken_links(root))

    def test_reports_missing_relative_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "README.md"
            source.write_text("[missing](missing.md)")
            self.assertEqual(
                [(source, "missing.md")],
                check_links.find_broken_links(root),
            )

    def test_ignores_external_anchor_and_code_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "README.md"
            source.write_text(
                "[web](https://example.com) [section](#section) `([fake](missing.md))`"
            )
            self.assertEqual([], check_links.find_broken_links(root))

    def test_ignores_dependency_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            dependency = root / "node_modules" / "package"
            dependency.mkdir(parents=True)
            (dependency / "README.md").write_text("[missing](missing.md)")
            self.assertEqual([], check_links.find_broken_links(root))


if __name__ == "__main__":
    unittest.main()
