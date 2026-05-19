#!/usr/bin/env python3
"""Basic consistency checks for .ai_workflow.

This script is intentionally simple and dependency-free.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".ai_workflow"
INDEX = WORKFLOW / "index.md"
ACTIVE = WORKFLOW / "tasks" / "active"
REPORTS = WORKFLOW / "reports"

STATUS_RE = re.compile(r"^Status:\s*(\S+)", re.MULTILINE)
TASK_LINK_RE = re.compile(r"\.ai_workflow/tasks/active/[^)\s`]+\.md")
ALLOWED = {
    "draft",
    "ready_for_human_review",
    "approved_for_codex",
    "in_progress",
    "done",
    "blocked",
    "rejected",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def warn(message: str) -> None:
    print(f"WARN: {message}")


def main() -> int:
    if not WORKFLOW.exists():
        fail(".ai_workflow directory is missing")
    if not INDEX.exists():
        fail(".ai_workflow/index.md is missing")
    if not ACTIVE.exists():
        fail(".ai_workflow/tasks/active directory is missing")
    if not REPORTS.exists():
        fail(".ai_workflow/reports directory is missing")

    active_tasks = [p for p in ACTIVE.glob("*.md") if p.is_file()]
    approved = []

    for task in active_tasks:
        text = task.read_text(encoding="utf-8")
        match = STATUS_RE.search(text)
        if not match:
            warn(f"{task}: missing Status line")
            continue
        status = match.group(1)
        if status not in ALLOWED:
            warn(f"{task}: unknown status '{status}'")
        if status == "approved_for_codex":
            approved.append(task)

    index_text = INDEX.read_text(encoding="utf-8")
    referenced = TASK_LINK_RE.findall(index_text)

    print(f"Active task files: {len(active_tasks)}")
    print(f"Approved active tasks: {len(approved)}")
    print(f"Task references in index: {len(referenced)}")

    if len(approved) > 1:
        warn("Multiple approved_for_codex tasks exist. Codex should stop unless index selects one explicitly.")

    for ref in referenced:
        path = ROOT / ref
        if not path.exists():
            warn(f"Index references missing task: {ref}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
