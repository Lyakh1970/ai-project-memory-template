# Workflow: ChatGPT ↔ Human ↔ Codex Loop

## Purpose

Create a safe, repeatable collaboration loop where ChatGPT prepares structured work, the human approves, and Codex executes only approved tasks.

## Roles

- Human: final decision-maker and approval gate.
- ChatGPT: strategy, task preparation, review, decision proposal.
- Codex: implementation, tests, reports.
- GitHub: source of truth.

## Loop

1. Human describes the next idea/problem in natural language.
2. ChatGPT converts it into a structured task file.
3. Human reviews the task.
4. If approved, the task status becomes `approved_for_codex`.
5. Task is stored in `.ai_workflow/tasks/active/`.
6. `.ai_workflow/index.md` points to this task.
7. Codex reads `AGENTS.md`, `.ai_workflow/index.md`, and the task file.
8. Codex executes the task.
9. Codex writes a report to `.ai_workflow/reports/`.
10. Human and ChatGPT review the report.
11. Accepted decisions are written to `docs/decision_log.md` or `docs/adr/`.
12. Completed task is moved to `.ai_workflow/tasks/done/`.

## Codex launch prompt

```text
Read AGENTS.md first.
Then read .ai_workflow/index.md.
Execute only the current approved task listed there.
Write the required report to .ai_workflow/reports/.
Do not execute draft/rejected/blocked tasks.
Do not commit secrets, raw private data, or private media.
If the task is ambiguous or risky, stop and create a review request in .ai_workflow/reviews/.
```
