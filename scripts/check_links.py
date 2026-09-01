#!/usr/bin/env python3
import re
import sys
from pathlib import Path
from urllib.parse import unquote


link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
inline_code_pattern = re.compile(r"`[^`]*`")
fenced_code_pattern = re.compile(r"```.*?```", re.DOTALL)


def find_broken_links(root: Path):
    broken = []
    for source in root.rglob("*.md"):
        if any(part in {".git", "node_modules"} for part in source.parts):
            continue
        content = fenced_code_pattern.sub("", source.read_text())
        content = inline_code_pattern.sub("", content)
        for match in link_pattern.finditer(content):
            target = match.group(1).strip().split()[0]
            if target.startswith(("http://", "https://", "mailto:", "#", "/")):
                continue
            path_text = unquote(target.split("#", 1)[0])
            if path_text and not (source.parent / path_text).exists():
                broken.append((source, target))
    return broken


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    broken = find_broken_links(root)
    for source, target in broken:
        print(f"{source.relative_to(root)}: broken link: {target}", file=sys.stderr)
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
