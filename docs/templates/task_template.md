# Task YYYY-MM-DD_NNN — Short title

Status: draft
Author: ChatGPT
Human reviewer: TBD
Target branch: TBD
Risk level: low | medium | high

## Goal

Describe exactly what Codex should achieve.

## Context

Explain why this task matters and what prior decisions are relevant.

## Required reading

- `AGENTS.md`
- `docs/current_state.md`
- `docs/no_touch_zones.md`
- Additional project-specific files:
  - TBD

## Scope

Codex may:

- TBD

Codex must not:

- TBD

## Required output

Codex must create a report:

- `.ai_workflow/reports/YYYY-MM-DD_NNN_codex_report.md`

The report must include:

1. Summary
2. Files changed
3. Tests/checks run
4. Risks found
5. Open questions
6. Recommended next step

## Definition of done

- TBD

## Stop conditions

Codex must stop and create a review request instead of proceeding if:

- The task requires secrets, raw private data, or production exports.
- A database migration is required but not explicitly approved.
- The implementation requires changing authentication/authorization.
- The requested scope is unclear.
- There is a risk of destructive data loss.
