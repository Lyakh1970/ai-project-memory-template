#!/usr/bin/env python3
"""Create a new draft task stub in .ai_workflow/tasks/active."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / ".ai_workflow" / "tasks" / "active"
TEMPLATE = ROOT / "docs" / "templates" / "task_template.md"


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_") or "task"


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: scripts/new_task_stub.py NNN 'Short title'", file=sys.stderr)
        return 2
    number = sys.argv[1]
    title = sys.argv[2]
    today = date.today().isoformat()
    slug = slugify(title)
    filename = f"{today}_{number}_{slug}.md"
    ACTIVE.mkdir(parents=True, exist_ok=True)
    output = ACTIVE / filename
    if output.exists():
        print(f"Task already exists: {output}", file=sys.stderr)
        return 1
    content = TEMPLATE.read_text(encoding="utf-8")
    content = content.replace("YYYY-MM-DD_NNN", f"{today}_{number}")
    content = content.replace("Short title", title)
    output.write_text(content, encoding="utf-8")
    print(output.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
