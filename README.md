# ai-project-memory-template

A reusable GitHub template for a human-gated AI workflow with ChatGPT, Codex, and a project repository as the single source of truth.

This repository is not meant to store project-specific knowledge directly. It is a **template**: copy it into a new project or apply its structure to an existing repository.

## Core idea

```text
Human discusses strategy with ChatGPT
        ↓
ChatGPT drafts a structured task
        ↓
Human reviews and approves
        ↓
Approved task is stored in .ai_workflow/tasks/active/
        ↓
Codex executes only approved tasks
        ↓
Codex writes a report to .ai_workflow/reports/
        ↓
Human + ChatGPT review the result
        ↓
Accepted decisions are recorded in docs/decision_log.md or docs/adr/
```

## What this template provides

- `AGENTS.md` — repository-level operating instructions for Codex and other coding agents.
- `.ai_workflow/` — controlled exchange area between Human, ChatGPT, and Codex.
- `docs/` — long-term project memory: current state, decisions, architecture, safety rules.
- `docs/templates/` — reusable templates for tasks, reports, reviews, ADRs, and project state.
- `docs/workflows/` — workflow definitions for ChatGPT ↔ Codex collaboration.
- `docs/security/` — safety rules for secrets, private data, raw exports, and external review bundles.
- `.github/` — issue and PR templates.
- `scripts/` — helper scripts for checking workflow consistency.
- `.codex/skills/` — optional local skill scaffolding for project-memory workflows.

## Source of truth rule

```text
Working project repository = source of truth.
Template repository = source of structure only.
```

After this template is applied to a project, the working project must maintain its own `AGENTS.md`, `docs/`, and `.ai_workflow/` files. Codex should not need to read the original template repository during normal project work.

## Recommended usage

### New project

1. Create a new GitHub repository from this template.
2. Rename/update the README for the real project.
3. Fill in:
   - `docs/current_state.md`
   - `docs/architecture.md`
   - `docs/no_touch_zones.md`
   - `docs/glossary.md`
4. Start creating tasks in `.ai_workflow/tasks/active/`.

### Existing project

Use Codex or manual copy to add the structure without overwriting existing files:

```text
Apply the ai-project-memory-template structure to this existing repository.
Do not overwrite existing files.
If similar files already exist, create a merge plan instead of replacing them.
Create missing files and folders only.
```

See `docs/workflows/apply_template_to_existing_repo.md`.

## Minimal operating loop

1. ChatGPT prepares a task as `Status: draft`.
2. Human reviews it.
3. Human approves it.
4. ChatGPT or Human stores it as `Status: approved_for_codex`.
5. `.ai_workflow/index.md` points to the current approved task.
6. Codex executes the current approved task.
7. Codex writes a report.
8. Human + ChatGPT review the report.
9. Final decisions move into `docs/decision_log.md` or `docs/adr/`.

## Golden rules

- Codex executes only tasks with `Status: approved_for_codex`.
- Draft tasks are never executed.
- Human approval is required before Codex changes code.
- Codex writes a report for every executed task.
- Secrets, credentials, raw exports, private media, and production data must not be committed.
- Final architectural decisions belong in `docs/decision_log.md` or `docs/adr/`, not only in `.ai_workflow/`.
