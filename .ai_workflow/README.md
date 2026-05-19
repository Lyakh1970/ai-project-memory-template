# .ai_workflow

Controlled exchange area between Human, ChatGPT, and Codex.

This folder is not a general notes dump. It is a structured workflow buffer for approved tasks, execution reports, review bundles, and pending decisions.

## Roles

- Human: final approval authority and execution gate.
- ChatGPT: drafts tasks, reviews reports, prepares decision proposals.
- Codex: executes only approved tasks and writes reports.
- GitHub repository: source of truth for project memory and workflow artifacts.

## Folder layout

```text
.ai_workflow/
  README.md
  index.md
  tasks/
    active/
    done/
    rejected/
    blocked/
  reports/
  reviews/
  decisions_pending/
```

## Task status values

Allowed statuses:

- `draft`
- `ready_for_human_review`
- `approved_for_codex`
- `in_progress`
- `done`
- `blocked`
- `rejected`

Codex may execute only tasks with:

```text
Status: approved_for_codex
```

## Operating rules

1. ChatGPT drafts a task as `draft`.
2. Human reviews and approves it.
3. ChatGPT or Human stores the approved task in `.ai_workflow/tasks/active/`.
4. `.ai_workflow/index.md` must point to the current approved task.
5. Codex reads `AGENTS.md`, `.ai_workflow/index.md`, and the current approved task.
6. Codex executes the task and writes a report to `.ai_workflow/reports/`.
7. Human + ChatGPT review the report.
8. Final accepted decisions move to `docs/decision_log.md` or `docs/adr/`.

## Safety rules

Never store secrets, credentials, tokens, raw private exports, private media, production database dumps, or unredacted personal data in `.ai_workflow/`.

If a task requires sensitive data, create a redacted fixture or a review request instead of copying raw data into the repository.

## Anti-patterns

Do not use:

- “latest prompt” logic;
- unstructured prompt dumps;
- silent Codex execution of draft tasks;
- permanent architectural decisions only inside `.ai_workflow/`;
- raw private data as task context.

Use `.ai_workflow/index.md` as the explicit pointer to the current approved task.
