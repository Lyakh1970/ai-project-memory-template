# AGENTS.md

Repository-level instructions for Codex and other coding agents.

## Role separation

- **Human** is the final approval authority.
- **ChatGPT** may draft tasks, reviews, decision proposals, and documentation.
- **Codex** may execute approved tasks, modify code, run tests, and produce reports.
- **GitHub repository** is the source of truth for project memory and workflow artifacts.

## Required reading order

Before starting work, read:

1. `AGENTS.md`
2. `docs/current_state.md`
3. `docs/no_touch_zones.md`
4. `.ai_workflow/index.md`
5. The specific task file listed as the current approved task

If any of these files are missing, stop and report what is missing.

## AI workflow rules

- Execute only tasks with `Status: approved_for_codex`.
- Do not execute tasks with `Status: draft`, `ready_for_human_review`, `blocked`, `done`, or `rejected`.
- Do not infer the current task from “latest file” unless `.ai_workflow/index.md` explicitly points to it.
- If multiple active approved tasks exist, stop and ask for human clarification.
- Always write a report to `.ai_workflow/reports/` after executing a task.
- If the task is ambiguous, risky, or under-specified, create a review request in `.ai_workflow/reviews/` instead of guessing.
- Do not silently make architecture decisions. Propose them in `.ai_workflow/decisions_pending/`.
- Accepted architectural decisions belong in `docs/decision_log.md` or `docs/adr/` and require human approval.

## Safety rules

Never commit or expose:

- `.env` files
- API keys, tokens, passwords, cookies, private keys, session files
- raw production database dumps
- raw chat exports containing personal data
- private media files
- authentication state files
- customer/client confidential data unless explicitly redacted and approved

If such data is encountered, do not copy it. Report the finding without exposing the secret value.

## Code-change rules

- Keep changes minimal and reversible.
- Prefer small tasks over large rewrites.
- Do not introduce new dependencies without explicit justification.
- Do not change database schema without migration plan and rollback notes.
- Do not modify unrelated files.
- Do not reformat large files unless the task explicitly asks for it.
- Run relevant tests when available.
- If tests cannot be run, explain why in the report.

## Documentation rules

When work changes project behavior, update the appropriate documentation:

- `docs/current_state.md` for current implementation state.
- `docs/changelog.md` for completed changes.
- `docs/decision_log.md` or `docs/adr/` for accepted decisions.
- `.ai_workflow/reports/` for task execution reports.

## Definition of done

A task is done only when:

- Requested scope is completed or limitations are clearly reported.
- Relevant tests/checks were run or skipped with explanation.
- No secrets/private raw data were committed.
- A report exists in `.ai_workflow/reports/`.
- Any unresolved risk is documented.
